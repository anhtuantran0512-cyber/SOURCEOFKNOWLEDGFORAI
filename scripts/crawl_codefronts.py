#!/usr/bin/env python3
"""Archive the public CodeFronts component catalogue as ready-to-use agent prompts.

Source: https://codefronts.com/ (MIT licensed snippets, see each prompt header)
Output: sources/codefronts/<section>/<category>/<slug>.md + manifest.json
"""

from __future__ import annotations

import argparse
import asyncio
import html
import json
import random
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import httpx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "codefronts"
SITEMAP = "https://codefronts.com/sitemap-0.xml"
SECTIONS = ("components", "motion", "navigation", "layouts", "snippets", "design-styles")
UA = "SOURCEOFKNOWLEDGFORAI/1.0 (learning archive; +https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI)"

RAW_RE = re.compile(r'<pre class="dp-raw"[^>]*>(.*?)</pre>', re.S)
AI_RE = re.compile(r'<pre class="dp-ai-preview"[^>]*>(.*?)</pre>', re.S)
JSONLD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
SCRIPT_RE = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
STYLE_RE = re.compile(r"<style\b[^>]*>.*?</style>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")


def text_of(fragment: str) -> str:
    return html.unescape(TAG_RE.sub("", fragment)).strip()


SECRET_RE = re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]+")


def redact(text: str) -> str:
    return SECRET_RE.sub("sk-demo-REDACTED", text)


def parse_page(url: str, page: str) -> dict | None:
    blocks = [text_of(b) for b in RAW_RE.findall(page)]
    ai = [text_of(b) for b in AI_RE.findall(page)]
    if not blocks and not ai:
        return None

    h1 = re.findall(r"<h1[^>]*>(.*?)</h1>", page, re.S)
    title = text_of(h1[0]) if h1 else urlparse(url).path.strip("/").split("/")[-1].replace("-", " ").title()

    desc = re.findall(r'<meta name="description" content="([^"]*)"', page)
    description = html.unescape(desc[0]).strip() if desc else ""

    category_name = ""
    section_name = ""
    for payload in JSONLD_RE.findall(page):
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "BreadcrumbList":
            names = [str(x.get("name", "")) for x in data.get("itemListElement", [])]
            if len(names) >= 4:
                section_name = names[1]
                category_name = re.sub(r"^\d+\s+", "", names[2])
                break

    prompt = ai[0] if ai else ""
    if not prompt:
        body = [f"# {title}", "", description, "", f"Source: {url}", ""]
        for index, block in enumerate(blocks):
            lang = "html" if block.lstrip().startswith("<") else ("css" if "{" in block else "js")
            body += [f"## Block {index + 1}", f"```{lang}", block, "```", ""]
        prompt = "\n".join(body)

    return {
        "title": title,
        "description": description,
        "section_name": section_name,
        "category_name": category_name,
        "prompt": redact(prompt),
        "has_js": any("addEventListener" in b or "querySelector" in b for b in blocks),
    }


def targets() -> list[str]:
    import xml.etree.ElementTree as ET

    with httpx.Client(timeout=60, headers={"User-Agent": UA}) as client:
        xml = client.get(SITEMAP).text
    root = ET.fromstring(xml)
    urls = [node.text.strip() for node in root.iter() if node.tag.endswith("loc") and node.text]
    keep = []
    for url in urls:
        parts = urlparse(url).path.strip("/").split("/")
        if len(parts) == 3 and parts[0] in SECTIONS:
            keep.append(url)
    return keep


def frontmatter(entry: dict) -> str:
    rows = [
        ("source", "codefronts"),
        ("url", entry["url"]),
        ("title", entry["title"]),
        ("section", entry["section"]),
        ("category", entry["category"]),
        ("category_name", entry["category_name"] or entry["category"]),
        ("description", entry["description"]),
        ("has_js", "true" if entry["has_js"] else "false"),
    ]
    lines = ["---"]
    for key, value in rows:
        lines.append(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    lines.append("---")
    return "\n".join(lines)


async def worker(queue: asyncio.Queue, client: httpx.AsyncClient, args, stats: dict, lock: asyncio.Lock):
    while True:
        url = await queue.get()
        if url is None:
            queue.task_done()
            return
        try:
            data = await fetch_one(client, url, args.retries)
            if data is None:
                stats["failed"].append(url)
            else:
                write_item(data, stats)
        finally:
            queue.task_done()


async def fetch_one(client: httpx.AsyncClient, url: str, retries: int) -> dict | None:
    for attempt in range(retries + 1):
        try:
            response = await client.get(url)
            if response.status_code == 200:
                parsed = parse_page(url, response.text)
                if parsed:
                    parts = urlparse(url).path.strip("/").split("/")
                    parsed["section"] = parts[0]
                    parsed["category"] = parts[1]
                    parsed["slug"] = parts[2]
                    parsed["url"] = url
                    return parsed
                return None
            if response.status_code in (404, 410):
                return None
        except (httpx.TimeoutException, httpx.TransportError):
            pass
        await asyncio.sleep(0.5 * (attempt + 1) + random.random() * 0.4)
    return None


def write_item(item: dict, stats: dict) -> None:
    folder = OUT / item["section"] / item["category"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{item['slug']}.md"
    body = frontmatter(item) + "\n\n" + item["prompt"].strip() + "\n"
    path.write_text(body, encoding="utf-8")
    entry = {
        "id": f"{item['section']}/{item['category']}/{item['slug']}",
        "title": item["title"],
        "section": item["section"],
        "section_name": item["section_name"],
        "category": item["category"],
        "category_name": item["category_name"],
        "description": item["description"],
        "url": item["url"],
        "path": str(path.relative_to(ROOT)),
        "prompt_chars": len(item["prompt"]),
        "has_js": item["has_js"],
    }
    with (OUT / "_manifest.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    stats["ok"] += 1


async def run(args) -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = OUT / "_manifest.jsonl"
    done: set[str] = set()
    if args.resume and manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            try:
                done.add(json.loads(line)["url"])
            except (json.JSONDecodeError, KeyError):
                continue
    elif manifest.exists():
        manifest.unlink()

    urls = targets()
    pending = [u for u in urls if u not in done]
    if args.limit:
        pending = pending[: args.limit]
    if args.shuffle:
        random.shuffle(pending)

    print(f"targets={len(urls)} done={len(done)} pending={len(pending)}", flush=True)
    queue: asyncio.Queue = asyncio.Queue()
    for url in pending:
        queue.put_nowait(url)
    stats = {"ok": 0, "failed": []}
    started = time.time()

    headers = {"User-Agent": UA, "Accept": "text/html,application/xhtml+xml", "Accept-Language": "en"}
    limits = httpx.Limits(max_connections=args.concurrency, max_keepalive_connections=args.concurrency)
    async with httpx.AsyncClient(headers=headers, timeout=45, limits=limits, follow_redirects=True) as client:
        tasks = [asyncio.create_task(worker(queue, client, args, stats, asyncio.Lock())) for _ in range(args.concurrency)]
        while any(not task.done() for task in tasks):
            await asyncio.sleep(10)
            print(f"  progress ok={stats['ok']} failed={len(stats['failed'])} elapsed={time.time() - started:.0f}s", flush=True)
            if args.limit and stats["ok"] + len(stats["failed"]) >= args.limit:
                break
        for _ in tasks:
            queue.put_nowait(None)
        await asyncio.gather(*tasks, return_exceptions=True)

    rows = []
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    rows.sort(key=lambda row: (row["section"], row["category"], row["title"]))
    (OUT / "manifest.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"done ok={stats['ok']} failed={len(stats['failed'])} in {time.time() - started:.0f}s", flush=True)
    if stats["failed"]:
        (OUT / "_failed.txt").write_text("\n".join(stats["failed"]), encoding="utf-8")
    return 0 if stats["ok"] else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=10)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--shuffle", action="store_true")
    return asyncio.run(run(parser.parse_args()))


if __name__ == "__main__":
    sys.exit(main())
