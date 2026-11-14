#!/usr/bin/env python3
"""Archive the free MotionSites prompt library (premium items stay locked on purpose).

Source: https://motionsites.ai/sections
Only items flagged `is_free = true` by the site are fetched through its public
`get-prompt` endpoint. Paid prompts are never collected, bypassed or mirrored.
"""

from __future__ import annotations

import asyncio
import json
import re
import sys
import time
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "motionsites"
SUPABASE = "https://mjofeydconwqhnyyylsd.supabase.co"
PUBLIC_KEY = "sb_publishable_m58T-CGj4u5RoaWo2-1ILw_meZ7yjDk"
UA = "SOURCEOFKNOWLEDGFORAI/1.0 (learning archive; +https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI)"


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or "uncategorized"


def headers() -> dict:
    return {"apikey": PUBLIC_KEY, "Authorization": f"Bearer {PUBLIC_KEY}", "User-Agent": UA}


async def fetch_catalog(client: httpx.AsyncClient) -> list[dict]:
    response = await client.get(
        f"{SUPABASE}/rest/v1/prompts",
        params={
            "select": "id,title,category,is_free,type,types,page_type",
            "order": "sort_order.asc",
            "limit": "2000",
        },
        headers=headers(),
    )
    response.raise_for_status()
    return response.json()


async def fetch_prompt(client: httpx.AsyncClient, prompt_id: str, retries: int = 3) -> dict | None:
    for attempt in range(retries):
        try:
            response = await client.post(
                f"{SUPABASE}/functions/v1/get-prompt",
                json={"prompt_id": prompt_id},
                headers={**headers(), "Content-Type": "application/json"},
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("prompt_text"):
                    return data
                return None
            if response.status_code in (401, 403, 404):
                return None
        except (httpx.TimeoutException, httpx.TransportError):
            pass
        await asyncio.sleep(1 + attempt)
    return None


async def run(concurrency: int, limit: int) -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        catalog = await fetch_catalog(client)
        (OUT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        free = [item for item in catalog if item.get("is_free")]
        if limit:
            free = free[:limit]
        print(f"catalog={len(catalog)} free={len(free)}", flush=True)

        semaphore = asyncio.Semaphore(concurrency)
        manifest: list[dict] = []
        failed: list[str] = []

        async def work(item: dict) -> None:
            async with semaphore:
                data = await fetch_prompt(client, item["id"])
                if not data:
                    failed.append(item["id"])
                    return
                category = item.get("category") or "Uncategorized"
                folder = OUT / "prompts" / slugify(category)
                folder.mkdir(parents=True, exist_ok=True)
                prompt = data["prompt_text"].strip()
                front = [
                    "---",
                    'source: "motionsites"',
                    f"id: {json.dumps(item['id'])}",
                    f"title: {json.dumps(item.get('title') or item['id'], ensure_ascii=False)}",
                    f"category: {json.dumps(category, ensure_ascii=False)}",
                    f"type: {json.dumps(item.get('type') or '')}",
                    f"types: {json.dumps(item.get('types') or [])}",
                    'license: "Free prompt published by MotionSites AI — see NOTICE.md"',
                    f'url: "https://motionsites.ai/sections#{item["id"]}"',
                    "---",
                ]
                path = folder / f"{slugify(item['id'])}.md"
                path.write_text("\n".join(front) + "\n\n" + prompt + "\n", encoding="utf-8")
                manifest.append(
                    {
                        "id": item["id"],
                        "title": item.get("title"),
                        "category": category,
                        "type": item.get("type"),
                        "types": item.get("types") or [],
                        "path": str(path.relative_to(ROOT)),
                        "prompt_chars": len(prompt),
                        "section_names": [x.get("name") for x in data.get("section_names") or []],
                    }
                )

        await asyncio.gather(*(work(item) for item in free))

    manifest.sort(key=lambda row: (row["category"] or "", row["title"] or ""))
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if failed:
        (OUT / "_failed.txt").write_text("\n".join(failed), encoding="utf-8")
    print(f"saved={len(manifest)} failed={len(failed)} elapsed={time.time() - started:.0f}s")
    return 0 if manifest else 1


if __name__ == "__main__":
    concurrency = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    sys.exit(asyncio.run(run(concurrency, limit)))
