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


def check_dirs(rows: list[dict], key: str, expected: int, errors: list[str], label: str) -> dict:
    """Manifests whose `path` points at a folder (Pin UI, ThreeUI)."""
    if len(rows) != expected:
        errors.append(f"{label} expected {expected} rows, found {len(rows)}")
    missing = sum(1 for row in rows if not (ROOT / row[key]).exists())
    empty = sum(
        1
        for row in rows
        if (ROOT / row[key]).is_dir() and not any(p.is_file() for p in (ROOT / row[key]).iterdir())
    )
    if missing:
        errors.append(f"{label}: {missing} missing paths")
    if empty:
        errors.append(f"{label}: {empty} empty folders")
    return {"rows": len(rows), "missing": missing, "empty": empty}


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

    pinui = load(SOURCES / "pinui" / "manifest.json")
    threeui = load(SOURCES / "threeui" / "manifest.json")
    report["pinui"] = check_dirs(pinui, "path", 41, errors, "pinui")
    report["threeui"] = check_dirs(threeui, "path", 961, errors, "threeui")
    for name in ("pinui", "threeui"):
        if not (SOURCES / name / "catalog.json").exists():
            errors.append(f"sources/{name}/catalog.json missing")
        if not (SOURCES / name / "README.md").exists():
            errors.append(f"sources/{name}/README.md missing")
    if not (SOURCES / "threeui" / "tags.json").exists():
        errors.append("sources/threeui/tags.json missing")

    gl = load(SOURCES / "getlayers" / "manifest.json")
    report["getlayers"] = check_dirs(gl, "path", 892, errors, "getlayers")
    for category, expected in (
        ("template", 62),
        ("3d_scene", 222),
        ("section", 54),
        ("background", 530),
        ("gradient", 24),
    ):
        rows = sum(1 for row in gl if row.get("category") == category)
        report["getlayers"][f"{category}_rows"] = rows
        if rows != expected:
            errors.append(f"getlayers {category}: {rows} rows, expected {expected}")
    stills_missing = sum(
        1 for row in gl if not row.get("preview") or not (ROOT / row["preview"]).exists()
    )
    report["getlayers"]["stills_missing"] = stills_missing
    if stills_missing:
        errors.append(f"getlayers poster stills missing: {stills_missing}")
    prompt_rows = [row for row in gl if row.get("prompt_path")]
    for row in prompt_rows:
        path = ROOT / row["prompt_path"]
        if not path.exists():
            errors.append(f"getlayers prompt missing: {row['prompt_path']}")
        elif not path.read_text(encoding="utf-8", errors="ignore").startswith("---"):
            errors.append(f"getlayers prompt missing frontmatter: {row['prompt_path']}")
    premium_leaks = [row["id"] for row in gl if row.get("tier") != "Free" and row.get("prompt_path")]
    report["getlayers"]["free_prompts"] = len(prompt_rows)
    report["getlayers"]["premium_leaks"] = len(premium_leaks)
    if premium_leaks:
        errors.append(f"premium GetLayers prompts present in archive: {premium_leaks[:5]}")
    for name in ("getlayers",):
        for required in ("README.md", "INDEX.md", "MEDIA.md", "media-sizes.json"):
            if not (SOURCES / name / required).exists():
                errors.append(f"sources/{name}/{required} missing")
        for category in ("template", "3d_scene", "section", "background", "gradient"):
            if not (SOURCES / name / "catalog" / f"{category}.json").exists():
                errors.append(f"sources/{name}/catalog/{category}.json missing")
    media_rows = (SOURCES / "getlayers" / "MEDIA.md").read_text(encoding="utf-8").count("\n| `")
    media_sizes = len(json.loads((SOURCES / "getlayers" / "media-sizes.json").read_text(encoding="utf-8")))
    report["getlayers"]["media_files"] = media_rows
    if media_rows != media_sizes:
        errors.append(f"MEDIA.md lists {media_rows} files, media-sizes.json has {media_sizes}")

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
