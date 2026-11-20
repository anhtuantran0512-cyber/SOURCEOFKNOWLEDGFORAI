#!/usr/bin/env python3
"""Archive the public GetLayers template library.

Source: https://www.getlayers.ai/templates

Every template in the public catalogue is collected:

* the full public record the site ships to the browser — tier, stack, tags,
  tone, mood, keywords, type tags, publish date, likes, measured frame
  timings, Lighthouse scores and audits, and every public asset URL;
* the poster still and the Figma preview image;
* the prompt, verbatim, **for free templates only**, through the same public
  server action the "Copy prompt" button calls.

Premium prompts answer `{"_apiError":{"code":"forbidden"}}` and are never
requested twice, guessed, reconstructed or bypassed. Their brief links to the
live page instead, exactly like the MotionSites and ThreeUI collectors.

The anonymous copy grant is **one prompt per visitor per day**; a signed-in
account lifts it (the site answers "sign in for unlimited free prompts"). Pass
`--cookie` / `--cookie-file` with your own session cookie to finish the free
prompts in one run, or re-run the collector once a day. Nothing here creates an
account or works around the limit.

Usage:
    python3 scripts/fetch_getlayers.py                 # metadata + stills + free prompts
    python3 scripts/fetch_getlayers.py --media video   # also the four mockup videos
    python3 scripts/fetch_getlayers.py --media all     # videos + Lighthouse report HTML
    python3 scripts/fetch_getlayers.py --force         # re-download existing files
    python3 scripts/fetch_getlayers.py --cookie-file ~/gl-cookies.txt   # signed-in run
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import time
from pathlib import Path
from typing import Any

import httpx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "getlayers"
SITE = "https://www.getlayers.ai"
UA = (
    "SOURCEOFKNOWLEDGFORAI/1.0 (learning archive; "
    "+https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI)"
)
LICENSE = "GetLayers preview and prompt — property of GetLayers / Textura; see NOTICE.md"

# Server action behind the "Copy prompt" button, read from the site's own
# client bundle (chunk exporting `composeLayerPromptAction`).
PROMPT_ACTION = "403fa889b319ba840b88a1254758da70b2fc5fb1e1"

VIDEO_FIELDS = ("posterVideo", "posterVideoPreview", "mockupDesktop", "mockupMobile")
IMAGE_FIELDS = ("image", "figmaPreview")


# --------------------------------------------------------------------------
# RSC parsing
# --------------------------------------------------------------------------
PUSH = re.compile(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', re.S)
TEXT_CHUNK = re.compile(r'(?:^|\n)([0-9a-f]+):T([0-9a-f]+),')


def rsc_payload(html: str) -> str:
    """Join the React Server Component flight chunks into one string."""
    return "".join(json.loads(chunk) for chunk in PUSH.findall(html))


def text_chunks(payload: str) -> dict[str, str]:
    """Return the length-prefixed `id:T<hex>,<text>` chunks of a flight stream.

    The prefix counts **UTF-8 bytes**, not characters — slicing the Python string by
    that number over-reads by one character per multi-byte codepoint and drags the
    next stream line into the prompt.
    """
    out: dict[str, str] = {}
    i = 0
    while True:
        match = TEXT_CHUNK.search(payload, i)
        if not match:
            break
        length = int(match.group(2), 16)
        start = match.end()
        window = payload[start : start + length + 64]
        text = window.encode("utf-8")[:length].decode("utf-8", errors="ignore")
        out[match.group(1)] = text
        i = start + len(text)
    return out


def json_array(payload: str, key: str) -> list[dict[str, Any]]:
    """Extract the first `"<key>":[...]` array from a flight payload."""
    marker = f'"{key}":['
    start = payload.find(marker)
    if start < 0:
        raise ValueError(f"{key} not found in payload")
    start = payload.index("[", start)
    depth = 0
    for index in range(start, len(payload)):
        char = payload[index]
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return json.loads(payload[start : index + 1])
    raise ValueError(f"unterminated {key} array")


def json_ld(html: str) -> list[dict[str, Any]]:
    blocks = re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.S
    )
    out = []
    for block in blocks:
        try:
            out.append(json.loads(block))
        except json.JSONDecodeError:
            continue
    return out


# --------------------------------------------------------------------------
# Collection
# --------------------------------------------------------------------------
def slug(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower() or "template"


async def get(client: httpx.AsyncClient, url: str, *, retries: int = 3) -> httpx.Response:
    for attempt in range(retries):
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return response
            if response.status_code in (403, 404):
                return response
        except (httpx.TimeoutException, httpx.TransportError):
            pass
        await asyncio.sleep(1 + attempt)
    raise RuntimeError(f"GET failed: {url}")


async def fetch_catalog(client: httpx.AsyncClient) -> list[dict[str, Any]]:
    response = await get(client, f"{SITE}/templates")
    items = json_array(rsc_payload(response.text), "items")
    return [item for item in items if item.get("category") == "template"]


async def fetch_prompt(client: httpx.AsyncClient, item: dict[str, Any]) -> tuple[str | None, str]:
    """Call the public copy-prompt action. Returns (prompt, status)."""
    body = json.dumps([{"layerId": item["id"], "uiTemplateKey": None}])
    response = await client.post(
        f"{SITE}/layer/{item['id']}",
        content=body,
        headers={
            "Content-Type": "text/plain;charset=UTF-8",
            "Accept": "text/x-component",
            "Origin": SITE,
            "Referer": f"{SITE}/layer/{item['id']}",
            "Next-Action": PROMPT_ACTION,
        },
    )
    if response.status_code != 200:
        return None, f"http_{response.status_code}"
    payload = response.text
    match = re.search(r'\{"prompt":"\$([0-9a-f]+)"\}', payload)
    if match:
        prompt = text_chunks(payload).get(match.group(1))
        if prompt:
            return prompt, "ok"
        return None, "empty_prompt_chunk"
    error = re.search(r'"_apiError":\{"code":"([a-z_]+)"', payload)
    if error:
        return None, error.group(1)
    return None, "unknown_response"


def performance_table(item: dict[str, Any]) -> str:
    report = item.get("optimizationReport") or {}
    rows = ["| Viewport | p50 | p95 | p99 | max | dropped | verdict |", "|---|---:|---:|---:|---:|---:|---|"]
    for view in ("mobile", "desktop"):
        perf = (report.get("performance") or {}).get(view)
        if not perf:
            continue
        rows.append(
            f"| {view} {perf['viewport']['width']}×{perf['viewport']['height']} | "
            f"{perf.get('p50', '—')} ms | {perf.get('p95', '—')} ms | {perf.get('p99', '—')} ms | "
            f"{perf.get('max', '—')} ms | {perf.get('droppedPct', '—')}% | {perf.get('verdict', '—')} |"
        )
    return "\n".join(rows) if len(rows) > 2 else "_No frame-timing run published._"


def seo_table(item: dict[str, Any]) -> str:
    report = item.get("optimizationReport") or {}
    rows = ["| Viewport | Perf | A11y | Best practices | SEO | LCP | CLS |", "|---|---:|---:|---:|---:|---:|---:|"]
    for view in ("mobile", "desktop"):
        seo = (report.get("seo") or {}).get(view)
        if not seo:
            continue
        scores = seo.get("scores") or {}
        metrics = seo.get("metrics") or {}
        rows.append(
            f"| {view} | {scores.get('performance', '—')} | {scores.get('accessibility', '—')} | "
            f"{scores.get('bestPractices', '—')} | {scores.get('seo', '—')} | "
            f"{metrics.get('LCP', '—')} ms | {metrics.get('CLS', '—')} |"
        )
    return "\n".join(rows) if len(rows) > 2 else "_No Lighthouse run published._"


def item_markdown(item: dict[str, Any], prompt_status: str) -> str:
    ident = item["id"]
    free = item.get("tier") == "Free"
    tags = ", ".join(item.get("tags") or []) or "—"
    stack = ", ".join(item.get("stack") or []) or "—"
    mood = ", ".join(item.get("mood") or []) or "—"
    types = ", ".join(item.get("typeTags") or []) or "—"
    front = [
        "---",
        'source: "getlayers"',
        f'id: "{ident}"',
        f'title: {json.dumps(item["title"], ensure_ascii=False)}',
        f'category: {json.dumps(item.get("category", ""))}',
        f'tier: "{item.get("tier", "")}"',
        f'tone: "{item.get("tone", "")}"',
        f'created: "{item.get("createdAt", "")}"',
        f"likes: {item.get('likes', 0)}",
        f'stack: {json.dumps(item.get("stack") or [], ensure_ascii=False)}',
        f'tags: {json.dumps(item.get("tags") or [], ensure_ascii=False)}',
        f'license: "{LICENSE}"',
        f'url: "{SITE}/layer/{ident}"',
        "---",
        "",
    ]
    body = [
        f"# {item['title']}",
        "",
        f"> {item.get('description', '').strip()}",
        "",
        f"- Category: `{item.get('category')}` · tier: **{item.get('tier')}** · tone: `{item.get('tone')}`",
        f"- Stack: {stack}",
        f"- Tags: {tags}",
        f"- Type tags: {types}",
        f"- Mood: {mood}",
        f"- Published: {item.get('createdAt', '—')} · likes: {item.get('likes', 0)}",
        f"- Live page: {SITE}/layer/{ident}",
        f"- Preview still: [`assets/{ident}.webp`](../../assets/{ident}.webp)",
        f"- Figma preview: "
        + (
            f"[`assets/{ident}-figma.webp`](../../assets/{ident}-figma.webp)"
            if item.get("figmaPreview")
            else "_not published for this template_"
        ),
        "",
        "## Measured performance",
        "",
        performance_table(item),
        "",
        "## Lighthouse",
        "",
        seo_table(item),
        "",
    ]
    report = item.get("optimizationReport") or {}
    links = []
    for view in ("mobile", "desktop"):
        url = ((report.get("seo") or {}).get(view) or {}).get("reportUrl")
        if url:
            links.append(f"- {view}: {url}")
    if links:
        body += ["Full reports:", "", *links, ""]

    body += ["## Prompt", ""]
    if free and prompt_status in ("ok", "cached"):
        body += [
            f"Free prompt, verbatim: [`prompts/{ident}.md`](../../prompts/{ident}.md)",
            "",
            "It rebuilds the page as one self-contained `index.html` and states every constant,",
            "asset URL and interaction the reference uses.",
        ]
    elif free and prompt_status == "rate_limited":
        body += [
            "The prompt is published free on the site, but its copy endpoint grants **one prompt per",
            "anonymous visitor per day** and that grant was already spent when this archive ran.",
            "Nothing is guessed here. Re-run `scripts/fetch_getlayers.py` on a later day, or pass a",
            "signed-in session cookie (`--cookie-file`) to capture every free prompt in one pass:",
            f"{SITE}/layer/{ident}",
        ]
    elif free:
        body += [
            f"The prompt could not be read on this run (`{prompt_status}`). Re-run the collector;",
            f"the page is {SITE}/layer/{ident}.",
        ]
    else:
        body += [
            "**Premium — not collected.** The copy-prompt action answers",
            '`{"_apiError":{"code":"forbidden","message":"Upgrade to access this prompt."}}`',
            "for this template. This archive does not bypass, guess or reconstruct it:",
            f"buy or preview the prompt at {SITE}/layer/{ident}.",
        ]

    body += [
        "",
        "## Public assets",
        "",
        "| Asset | URL |",
        "|---|---|",
    ]
    for field in ("image", "posterVideo", "posterVideoPreview", "mockupDesktop", "mockupMobile", "figmaPreview"):
        if item.get(field):
            body.append(f"| `{field}` | {item[field]} |")
    body += [
        "",
        "## Use",
        "",
        "Adapt the structure, motion values and art direction to the project's own copy, imagery and",
        "tokens. Never ship the demo text or third-party media. Keep the attribution in `NOTICE.md`.",
        "",
    ]
    return "\n".join(front + body)


def prompt_markdown(item: dict[str, Any], prompt: str) -> str:
    front = [
        "---",
        'source: "getlayers"',
        f'id: "{item["id"]}"',
        f'title: {json.dumps(item["title"], ensure_ascii=False)}',
        f'category: {json.dumps(item.get("category", ""))}',
        f'tier: "{item.get("tier", "")}"',
        f'license: "{LICENSE}"',
        f'url: "{SITE}/layer/{item["id"]}"',
        "---",
        "",
    ]
    return "\n".join(front) + prompt.rstrip() + "\n"


async def download(
    client: httpx.AsyncClient, url: str, path: Path, force: bool
) -> str:
    if path.exists() and not force and path.stat().st_size > 0:
        return "cached"
    response = await get(client, url)
    if response.status_code != 200:
        return f"http_{response.status_code}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(response.content)
    return f"{len(response.content)} bytes"


async def run(args: argparse.Namespace) -> int:
    started = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "items").mkdir(exist_ok=True)
    (OUT / "prompts").mkdir(exist_ok=True)
    (OUT / "assets").mkdir(exist_ok=True)

    headers = {"User-Agent": UA}
    if args.cookie:
        headers["Cookie"] = args.cookie
    async with httpx.AsyncClient(
        timeout=90, follow_redirects=True, headers=headers
    ) as client:
        catalog = await fetch_catalog(client)
        catalog.sort(key=lambda item: (item.get("tier") != "Free", -(item.get("likes") or 0)))
        (OUT / "catalog.json").write_text(
            json.dumps(catalog, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )
        free = [item for item in catalog if item.get("tier") == "Free"]
        print(f"templates={len(catalog)} free={len(free)} premium={len(catalog) - len(free)}", flush=True)

        manifest: list[dict[str, Any]] = []
        prompt_status: dict[str, str] = {}

        for index, item in enumerate(catalog, 1):
            ident = item["id"]
            record: dict[str, Any] = {
                "fetchedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "source": f"{SITE}/templates",
                "item": item,
            }

            page = await get(client, f"{SITE}/layer/{ident}")
            if page.status_code == 200:
                record["page"] = {
                    "url": f"{SITE}/layer/{ident}",
                    "jsonLd": json_ld(page.text),
                }
            await asyncio.sleep(0.25)

            status = "premium" if item.get("tier") != "Free" else "pending"
            prompt_file = OUT / "prompts" / f"{ident}.md"
            if item.get("tier") != "Free":
                record["prompt"] = {"status": "premium"}
            elif prompt_file.exists() and not args.force:
                status = "cached"
                record["prompt"] = {
                    "status": "cached",
                    "path": f"sources/getlayers/prompts/{ident}.md",
                    "chars": len(prompt_file.read_text(encoding="utf-8")),
                }
            else:
                prompt, status = await fetch_prompt(client, item)
                prompt_status[ident] = status
                if prompt:
                    prompt_file.write_text(prompt_markdown(item, prompt), encoding="utf-8")
                    record["prompt"] = {
                        "status": status,
                        "path": f"sources/getlayers/prompts/{ident}.md",
                        "chars": len(prompt),
                    }
                else:
                    record["prompt"] = {"status": status}
                await asyncio.sleep(1.5)

            # Stills are always bundled; videos and reports are opt-in.
            for field in IMAGE_FIELDS:
                url = item.get(field)
                if not url:
                    continue
                suffix = "-figma" if field == "figmaPreview" else ""
                result = await download(client, url, OUT / "assets" / f"{ident}{suffix}.webp", args.force)
                record.setdefault("files", {})[f"{ident}{suffix}.webp"] = result
            if args.media in ("video", "all"):
                for field in VIDEO_FIELDS:
                    url = item.get(field)
                    if not url:
                        continue
                    suffix = {
                        "posterVideo": "",
                        "posterVideoPreview": "-preview",
                        "mockupDesktop": "-desktop",
                        "mockupMobile": "-mobile",
                    }[field]
                    result = await download(client, url, OUT / "assets" / f"{ident}{suffix}.mp4", args.force)
                    record.setdefault("files", {})[f"{ident}{suffix}.mp4"] = result
            if args.media == "all":
                for view in ("mobile", "desktop"):
                    url = ((item.get("optimizationReport") or {}).get("seo") or {}).get(view, {}).get("reportUrl")
                    if not url:
                        continue
                    result = await download(
                        client, url, OUT / "reports" / f"{ident}-{view}.html", args.force
                    )
                    record.setdefault("files", {})[f"reports/{ident}-{view}.html"] = result

            item_dir = OUT / "items" / ident
            item_dir.mkdir(parents=True, exist_ok=True)
            (item_dir / "metadata.json").write_text(
                json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
            )
            (item_dir / "ITEM.md").write_text(item_markdown(item, status), encoding="utf-8")

            type_tags = item.get("typeTags") or []
            manifest.append(
                {
                    "id": ident,
                    "title": item["title"],
                    "kind": "template",
                    "layout": type_tags[0] if type_tags else "—",
                    "industries": [tag for tag in type_tags if tag not in ("hero", "full-page")],
                    "typeTags": type_tags,
                    "category": item.get("category", "template"),
                    "tier": item.get("tier"),
                    "tone": item.get("tone"),
                    "tags": item.get("tags") or [],
                    "stack": item.get("stack") or [],
                    "mood": item.get("mood") or [],
                    "createdAt": item.get("createdAt"),
                    "likes": item.get("likes", 0),
                    "description": item.get("description", ""),
                    "path": f"sources/getlayers/items/{ident}/ITEM.md",
                    "prompt_path": (
                        f"sources/getlayers/prompts/{ident}.md"
                        if (OUT / "prompts" / f"{ident}.md").exists()
                        else None
                    ),
                    "preview": (
                        f"sources/getlayers/assets/{ident}.webp"
                        if (OUT / "assets" / f"{ident}.webp").exists()
                        else None
                    ),
                    "url": f"{SITE}/layer/{ident}",
                    "license": LICENSE,
                }
            )
            print(f"  [{index:>2}/{len(catalog)}] {ident:<24} {item.get('tier'):<8} {status}", flush=True)

        (OUT / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
        )

    captured = sum(1 for row in manifest if row["prompt_path"])
    print(
        f"done in {time.time() - started:.1f}s · items={len(manifest)} "
        f"prompts={captured} stills={sum(1 for row in manifest if row['preview'])}",
        flush=True,
    )
    return 0 if len(manifest) == len(catalog) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--media",
        choices=("none", "video", "all"),
        default="none",
        help="none: stills only (default) · video: + four mockup mp4 per template · all: + Lighthouse HTML",
    )
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    parser.add_argument(
        "--cookie",
        default="",
        help="raw Cookie header from your own signed-in session (name=value; …)",
    )
    parser.add_argument(
        "--cookie-file",
        type=Path,
        help="file holding the raw Cookie header, for a signed-in run",
    )
    args = parser.parse_args()
    if args.cookie_file:
        args.cookie = args.cookie_file.read_text(encoding="utf-8").strip()
    return asyncio.run(run(args))


if __name__ == "__main__":
    raise SystemExit(main())
