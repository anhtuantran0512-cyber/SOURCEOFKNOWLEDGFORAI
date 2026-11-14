#!/usr/bin/env python3
"""Validate the archive: counts, files, frontmatter and basic content sanity."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def check(rows: list[dict], key: str, min_chars: int, errors: list[str], require_fence: bool = False) -> dict:
    missing = 0
    short = 0
    no_fence = 0
    for row in rows:
        path = ROOT / row[key]
        if not path.exists():
            missing += 1
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if len(text) < min_chars:
            short += 1
        if not text.startswith("---"):
            errors.append(f"missing frontmatter: {row[key]}")
        if require_fence and "```" not in text:
            no_fence += 1
    return {"rows": len(rows), "missing": missing, "short": short, "no_code_fence": no_fence}


def main() -> int:
    errors: list[str] = []
    report: dict[str, object] = {}

    cf = load(SOURCES / "codefronts" / "manifest.json")
    lu = load(SOURCES / "lucianlabs" / "manifest.json")
    ms = load(SOURCES / "motionsites" / "manifest.json")
    ms_catalog = load(SOURCES / "motionsites" / "catalog.json")

    if not cf:
        errors.append("sources/codefronts/manifest.json missing or empty")
    if len(lu) != 400:
        errors.append(f"lucianlabs expected 400 rows, found {len(lu)}")
    if not ms:
        errors.append("sources/motionsites/manifest.json missing or empty")

    report["codefronts"] = check(cf, "path", 400, errors, require_fence=True)
    report["lucianlabs"] = check(lu, "prompt_path", 600, errors)
    report["motionsites"] = check(ms, "path", 400, errors, require_fence=False)

    demo_missing = sum(1 for row in lu if not (ROOT / row["demo_path"]).exists())
    report["lucianlabs"]["demos_missing"] = demo_missing
    if demo_missing:
        errors.append(f"lucianlabs demos missing: {demo_missing}")

    free_ids = {row["id"] for row in ms}
    locked_leaks = [row["id"] for row in ms_catalog if not row.get("is_free") and row["id"] in free_ids]
    report["motionsites"]["locked_leaks"] = len(locked_leaks)
    if locked_leaks:
        errors.append(f"paid prompts present in archive: {locked_leaks[:5]}")

    report["errors"] = errors
    (ROOT / "verify-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for name, stats in report.items():
        if name != "errors":
            print(f"{name}: {stats}")
    print(f"errors: {len(errors)}")
    for error in errors[:20]:
        print(f"  - {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
