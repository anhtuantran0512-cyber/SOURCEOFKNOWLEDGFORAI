#!/usr/bin/env python3
"""Archive the public lucianLabs UX/UI Prompt library (400 MIT-licensed elements).

Source: https://lucianlabs.dev/en/uxui-prompt/
Every element ships as a ready-to-paste agent prompt plus a standalone demo file.
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import httpx

BASE = "https://lucianlabs.dev"
PAGE = f"{BASE}/en/uxui-prompt/"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "lucianlabs"
UA = "SOURCEOFKNOWLEDGFORAI/1.0 (learning archive; +https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI)"
HANGUL = re.compile(r"[ㄱ-ㆎ가-힣]")
ESCAPES = {"n": "\n", "t": "\t", "r": "\r", "'": "'", '"': '"', "\\": "\\", "/": "/"}


def js_strings(block: str) -> list[str]:
    out = []
    for raw in re.findall(r"'((?:\\.|[^'\\])*)'", block, re.S):
        out.append(re.sub(r"\\(.)", lambda m: ESCAPES.get(m.group(1), m.group(1)), raw))
    return out


def load_text(client: httpx.Client, url: str) -> str:
    response = client.get(url)
    response.raise_for_status()
    return response.text


def ux_localize(code: str, kind: str, pairs: list) -> str:
    out = str(code)
    if kind == "html":
        out = re.sub(r"<!--[\s\S]*?-->", lambda m: "" if HANGUL.search(m.group(0)) else m.group(0), out)
        out = re.sub(r"/\*[\s\S]*?\*/", lambda m: "" if HANGUL.search(m.group(0)) else m.group(0), out)
    else:
        out = re.sub(r"/\*[\s\S]*?\*/", lambda m: "" if HANGUL.search(m.group(0)) else m.group(0), out)
        out = "\n".join(line for line in out.split("\n") if not (re.match(r"^\s*//", line) and HANGUL.search(line)))
        out = re.sub(
            r"([^\s:'\"\\])([ \t]+)// [^\n'\"]*$",
            lambda m: m.group(1) if HANGUL.search(m.group(0)) else m.group(0),
            out,
            flags=re.M,
        )
    if pairs:
        mapping: dict[str, str] = {}
        for pair in pairs:
            if pair and len(pair) == 2 and pair[0] not in mapping:
                mapping[pair[0]] = pair[1]
        keys = sorted(mapping, key=len, reverse=True)
        if keys:
            pattern = re.compile("|".join(re.escape(key) for key in keys))
            out = pattern.sub(lambda m: mapping[m.group(0)], out)
    return out


def slug_path(entry: dict) -> tuple[str, str]:
    return ("animation" if entry["set"] == 2 else "interface"), f"{entry['id']}-{entry['slug']}"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    with httpx.Client(headers={"User-Agent": UA}, timeout=60, follow_redirects=True) as client:
        page = load_text(client, PAGE)
        catalog_url = BASE + re.search(r'src="(/uxui-prompt/assets/catalog\.[^"]+\.js)"', page).group(1)
        gallery_url = BASE + re.search(r'src="(/uxui-prompt/assets/gallery\.[^"]+\.js)"', page).group(1)
        print(f"catalog: {catalog_url}", flush=True)
        catalog_js = load_text(client, catalog_url)
        gallery_js = load_text(client, gallery_url)

        raw = catalog_js[catalog_js.index("window.UXG_DATA=") + len("window.UXG_DATA="):].strip().rstrip(";")
        data = json.loads(raw)
        items = data["items"]
        tokens = data["tokens"]
        (OUT / "tokens.css").write_text(tokens.strip() + "\n", encoding="utf-8")

        guide_block = gallery_js[gallery_js.index("GUIDE = {"):]
        guide_en_block = guide_block[guide_block.index("en: ["): guide_block.index("].join", guide_block.index("en: ["))]
        guide_en = "\n".join(js_strings(guide_en_block))

        cat_block = gallery_js[gallery_js.index("var CAT_EN"):]
        cat_block = cat_block[: cat_block.index("};")]
        cat_en = dict(re.findall(r"'((?:\\.|[^'\\])*)':\s*'((?:\\.|[^'\\])*)'", cat_block))

        sources = sorted({item["source"] for item in items})
        previews: dict[str, dict] = {}
        for index, rel in enumerate(sources, 1):
            url = BASE + "/uxui-prompt/" + rel.removeprefix("./")
            payload = client.get(url)
            payload.raise_for_status()
            for entry in payload.json()["items"]:
                previews[entry["id"]] = entry
            if index % 10 == 0:
                print(f"  previews {index}/{len(sources)}", flush=True)

        missing = [item["id"] for item in items if item["id"] not in previews]
        manifest = []
        for item in items:
            preview = previews.get(item["id"])
            if not preview:
                continue
            english = item.get("en") or {}
            pairs = preview.get("map") or []
            html = ux_localize(preview.get("html", ""), "html", pairs)
            js = ux_localize(preview.get("js", ""), "js", pairs)
            title = english.get("title") or item["title"]
            summary = english.get("summary") or item["summary"]
            hint = english.get("hint") or item.get("hint") or ""
            category = cat_en.get(item["category"], item["category"])
            license_line = (
                f"<!-- Lucian UX/UI Prompt #{item['id']} · MIT License (c) 2026 Seokwoooo · "
                f"https://lucianlabs.dev/uxui-prompt/#{item['id']} -->"
            )
            code = f"{license_line}\n<style>\n{tokens.strip()}\n</style>\n\n{html}\n\n<script>\n{js}\n</script>\n"
            prompt = (
                f"[Element] {title} ({item['id']}, {category})\n"
                f"[What it does] {summary}\n"
                + (f"[How to use it] {hint}\n" if hint else "")
                + f"\n{guide_en}\n\n"
                + "--- Code start (this whole code is the working original) ---\n"
                + code
                + "--- Code end ---\n"
            )
            folder_name, file_stem = slug_path(item)
            target_dir = OUT / "prompts" / folder_name
            target_dir.mkdir(parents=True, exist_ok=True)
            front = [
                "---",
                'source: "lucianlabs"',
                f'id: "{item["id"]}"',
                f"title: {json.dumps(title, ensure_ascii=False)}",
                f"category: {json.dumps(category, ensure_ascii=False)}",
                f'collection: "{folder_name}"',
                f'url: "https://lucianlabs.dev/en/uxui-prompt/#{item["id"]}"',
                f"tags: {json.dumps(item.get('tags') or [], ensure_ascii=False)}",
                'license: "MIT (c) 2026 Seokwoooo"',
                "---",
            ]
            (target_dir / f"{file_stem}.md").write_text("\n".join(front) + "\n\n" + prompt, encoding="utf-8")

            demo_dir = OUT / "demos" / folder_name
            demo_dir.mkdir(parents=True, exist_ok=True)
            demo = (
                "<!doctype html>\n"
                + license_line
                + "\n<html lang=\"en\" data-theme=\"light\">\n<head>\n<meta charset=\"utf-8\">\n"
                + "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
                + f"<title>{title} · lucianLabs UI</title>\n<style>\n{tokens.strip()}\n</style>\n"
                + "<style>\nbody{margin:0;min-height:100vh;display:grid;place-items:center;padding:48px 24px;"
                + "background:var(--ux-page);box-sizing:border-box}\n"
                + ".ux-theme-btn{position:fixed;top:16px;right:16px;height:38px;padding:0 16px;border-radius:999px;"
                + "border:1px solid var(--ux-line-2);background:var(--ux-surface);color:var(--ux-ink);"
                + "font:600 13px/1 system-ui,sans-serif;cursor:pointer}\n</style>\n</head>\n<body>\n"
                + "<button class=\"ux-theme-btn\" type=\"button\" onclick=\"document.documentElement.dataset.theme="
                + "document.documentElement.dataset.theme==='dark'?'light':'dark'\">Light / Dark</button>\n"
                + html
                + f"\n<script>\n{js}\n</script>\n</body>\n</html>\n"
            )
            (demo_dir / f"{file_stem}.html").write_text(demo, encoding="utf-8")

            manifest.append(
                {
                    "id": item["id"],
                    "slug": item["slug"],
                    "title": title,
                    "category": category,
                    "collection": folder_name,
                    "tags": item.get("tags") or [],
                    "url": f"https://lucianlabs.dev/en/uxui-prompt/#{item['id']}",
                    "prompt_path": str((OUT / "prompts" / folder_name / f"{file_stem}.md").relative_to(ROOT)),
                    "demo_path": str((OUT / "demos" / folder_name / f"{file_stem}.html").relative_to(ROOT)),
                    "prompt_chars": len(prompt),
                }
            )

    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (OUT / "catalog.json").write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"items={len(manifest)} missing={len(missing)} elapsed={time.time() - started:.0f}s")
    if missing:
        (OUT / "_missing.txt").write_text("\n".join(missing), encoding="utf-8")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
