#!/usr/bin/env python3
"""Download every published media file for the GetLayers items that are free.

`fetch_getlayers.py` records the catalogue and one poster per item; it leaves
the media on the CDN because the full set is 10 GB. The free tier is small
enough to keep in the repository, so this script walks the 47 free items,
streams each asset the site publishes for them into `sources/getlayers/media/
<id>/`, and writes `media-free.json` as the inventory.

    python3 scripts/fetch_getlayers_free.py            # free items only
    python3 scripts/fetch_getlayers_free.py --force     # re-download everything

Only files reachable without an account are touched: an item whose tier is not
`Free` is skipped, so nothing behind the paywall is fetched.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import httpx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources" / "getlayers"
UA = (
    "SOURCEOFKNOWLEDGFORAI/1.0 (learning archive; "
    "+https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI)"
)
HOST = "storage.getlayers.ai"
CONCURRENCY = 4


def media_urls(node: Any, field: str = "item") -> list[tuple[str, str]]:
    """Every storage URL in an item record, paired with the field it came from."""
    found: list[tuple[str, str]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            found.extend(media_urls(value, key))
    elif isinstance(node, list):
        for value in node:
            found.extend(media_urls(value, field))
    elif isinstance(node, str) and node.startswith("http") and HOST in node:
        found.append((field, node))
    return found


def target_name(url: str) -> str:
    return Path(urlsplit(url).path).name or "asset"


async def fetch_one(
    client: httpx.AsyncClient, sem: asyncio.Semaphore, url: str, path: Path, force: bool
) -> dict[str, Any]:
    if path.exists() and not force and path.stat().st_size > 0:
        return {"bytes": path.stat().st_size, "status": "cached"}
    async with sem:
        for attempt in range(3):
            try:
                async with client.stream("GET", url) as response:
                    if response.status_code != 200:
                        return {"bytes": 0, "status": f"http_{response.status_code}"}
                    path.parent.mkdir(parents=True, exist_ok=True)
                    tmp = path.with_suffix(path.suffix + ".part")
                    size = 0
                    with tmp.open("wb") as handle:
                        async for chunk in response.aiter_bytes(65536):
                            handle.write(chunk)
                            size += len(chunk)
                    tmp.replace(path)
                    return {"bytes": size, "status": "ok"}
            except (httpx.HTTPError, OSError) as error:
                if attempt == 2:
                    return {"bytes": 0, "status": f"error:{type(error).__name__}"}
                await asyncio.sleep(1.5 * (attempt + 1))
    return {"bytes": 0, "status": "error"}


async def run(args: argparse.Namespace) -> int:
    manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
    free = [row for row in manifest if row.get("tier") == "Free"]
    if args.limit:
        free = free[: args.limit]
    print(f"free items: {len(free)}", flush=True)

    sem = asyncio.Semaphore(CONCURRENCY)
    inventory: list[dict[str, Any]] = []
    started = time.time()
    total_bytes = 0

    async with httpx.AsyncClient(
        timeout=180, follow_redirects=True, headers={"User-Agent": UA}
    ) as client:
        for index, row in enumerate(free, 1):
            ident = row["id"]
            record = json.loads(
                (OUT / "items" / ident / "metadata.json").read_text(encoding="utf-8")
            )
            pairs = media_urls(record.get("item") or {})
            seen: dict[str, int] = {}
            files: list[dict[str, Any]] = []
            for field, url in pairs:
                name = target_name(url)
                if name in seen:
                    seen[name] += 1
                    name = f"{Path(name).stem}-{seen[name]}{Path(name).suffix}"
                else:
                    seen[name] = 1
                path = OUT / "media" / ident / name
                result = await fetch_one(client, sem, url, path, args.force)
                total_bytes += result["bytes"]
                files.append(
                    {
                        "field": field,
                        "url": url,
                        "path": str(path.relative_to(ROOT)),
                        **result,
                    }
                )
            inventory.append(
                {
                    "id": ident,
                    "title": row["title"],
                    "category": row["category"],
                    "bytes": sum(f["bytes"] for f in files),
                    "files": files,
                }
            )
            failed = [f for f in files if f["status"] not in ("ok", "cached")]
            note = f" ({len(failed)} failed)" if failed else ""
            print(
                f"  [{index:>2}/{len(free)}] {ident:<28} {len(files):>2} files "
                f"{sum(f['bytes'] for f in files) / 1e6:>7.1f} MB{note}",
                flush=True,
            )

    inventory.sort(key=lambda entry: (entry["category"], entry["id"]))
    payload = {
        "source": "https://www.getlayers.ai",
        "collectedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "scope": "items whose tier is Free — everything else stays on the CDN",
        "items": len(inventory),
        "files": sum(len(entry["files"]) for entry in inventory),
        "bytes": total_bytes,
        "entries": inventory,
    }
    (OUT / "media-free.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    failed = sum(
        1
        for entry in inventory
        for file in entry["files"]
        if file["status"] not in ("ok", "cached")
    )
    print(
        f"done in {time.time() - started:.1f}s · items={len(inventory)} "
        f"files={payload['files']} size={total_bytes / 1e9:.2f} GB failed={failed}",
        flush=True,
    )
    return 0 if failed == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="re-download files that already exist")
    parser.add_argument("--limit", type=int, default=0, help="stop after N free items")
    return asyncio.run(run(parser.parse_args()))


if __name__ == "__main__":
    raise SystemExit(main())
