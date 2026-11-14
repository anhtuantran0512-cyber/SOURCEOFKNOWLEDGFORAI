#!/usr/bin/env python3
"""Build the repository index files from the collected manifests."""

from __future__ import annotations

import json
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"


def read_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def codefronts_stats(manifest: list[dict]) -> tuple[Counter, dict[str, Counter]]:
    sections = Counter()
    categories: dict[str, Counter] = defaultdict(Counter)
    for row in manifest:
        sections[row["section"]] += 1
        categories[row["section"]][row["category_name"] or row["category"]] += 1
    return sections, categories


def table(rows: list[tuple[str, str, str]]) -> str:
    out = ["| Folder | Items | What it is |", "|---|---:|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    return "\n".join(out)


def build_codefronts(manifest: list[dict]) -> None:
    sections, categories = codefronts_stats(manifest)
    names = {
        "components": "UI components (buttons, cards, forms, inputs, progress)",
        "motion": "Motion and hover effects",
        "layouts": "Page and section layouts",
        "navigation": "Navigation patterns",
        "snippets": "Small snippets (badges, alerts, tooltips, chips)",
        "design-styles": "Whole design styles (glass, neon, brutalist, minimal)",
    }
    rows = [(f"`{key}/`", f"{count:,}", names.get(key, key)) for key, count in sections.most_common()]
    cat_rows = []
    for section, _ in sections.most_common():
        top = ", ".join(f"{name} ({count})" for name, count in categories[section].most_common(8))
        cat_rows.append(f"- **{section}** — {top}")
    body = f"""# CodeFronts archive

Public CSS/Tailwind component catalogue from <https://codefronts.com/>, converted into one
ready-to-paste prompt per component. Each file contains the original AI prompt (which already embeds the
working HTML/CSS/JS) plus source metadata.

- Items: **{len(manifest):,}**
- Format: one Markdown file per component, folder = section/category
- License: MIT, as stated inside every CodeFronts prompt
- Manifest: [`manifest.json`](manifest.json)

## Coverage

{table(rows)}

### Categories per section

{chr(10).join(cat_rows)}

## Use

```bash
# find a pattern
jq -r '.[] | select((.title + " " + .category_name) | test("pricing"; "i")) | [.title, .path] | @tsv' \\
  sources/codefronts/manifest.json
```

Open the file and send the prompt as-is, or lift only the HTML/CSS block. Keep the `Source:` line.
"""
    (SOURCES / "codefronts" / "README.md").write_text(body, encoding="utf-8")


def build_lucian(manifest: list[dict]) -> None:
    collections = Counter(row["collection"] for row in manifest)
    categories = Counter(row["category"] for row in manifest)
    cat_rows = "\n".join(f"- {name} — {count}" for name, count in categories.most_common())
    body = f"""# lucianLabs UX/UI Prompt archive

400 MIT-licensed UI elements from <https://lucianlabs.dev/en/uxui-prompt/>. Every element is stored as a
complete, ready-to-paste prompt that includes the working code, the site's application guide and the
license line.

- Elements: **{len(manifest)}** ({collections.get('interface', 0)} interface, {collections.get('animation', 0)} animation)
- Prompts: `prompts/<collection>/<id>-<slug>.md`
- Runnable demos: `demos/<collection>/<id>-<slug>.html` (open directly in a browser)
- Theme tokens: [`tokens.css`](tokens.css)
- License: MIT (c) 2026 Seokwoooo — kept in every file
- Manifest: [`manifest.json`](manifest.json)

## Categories

{cat_rows}

## Use

```bash
jq -r '.[] | select((.title + " " + .category + " " + (.tags | join(" "))) | test("chart|dashboard"; "i")) | [.id, .title, .prompt_path] | @tsv' \\
  sources/lucianlabs/manifest.json
```

Read the prompt file. The `[Element]` block and the code are the source of truth; do not rewrite the
motion values. Keep the license comment when you port the code.
"""
    (SOURCES / "lucianlabs" / "README.md").write_text(body, encoding="utf-8")


def build_motionsites(manifest: list[dict], catalog: list[dict]) -> None:
    categories = Counter(row["category"] or "Uncategorized" for row in manifest)
    locked = [row for row in catalog if not row.get("is_free")]
    cat_rows = "\n".join(f"- {name} — {count}" for name, count in categories.most_common())
    body = f"""# MotionSites AI — free prompt archive

Website-section prompts published as free on <https://motionsites.ai/sections>.

- Free prompts archived: **{len(manifest)}**
- Catalogue entries seen: **{len(catalog)}** (of which **{len(locked)}** are paid/locked and intentionally not archived)
- Format: one Markdown file per prompt, folder = category
- Rights: prompts remain the property of MotionSites AI and their authors; not relicensed here.
  See [`NOTICE.md`](../../NOTICE.md).
- Manifest: [`manifest.json`](manifest.json) · full public catalogue: [`catalog.json`](catalog.json)

## Categories

{cat_rows}

## Use

These prompts are best used as **section briefs**: they specify layout, fonts, spacing and interaction in
detail. Keep the structure and adapt the brand. The prompts often reference third-party asset URLs; replace
them with your own files.

```bash
jq -r '.[] | select(.category == "Hero") | [.title, .path] | @tsv' sources/motionsites/manifest.json
```

Paid prompts are deliberately absent. Do not try to reconstruct them from previews.
"""
    (SOURCES / "motionsites" / "README.md").write_text(body, encoding="utf-8")


def best_of() -> str:
    picks = [
        ("Liquid glass button", "sources/lucianlabs/prompts/interface/001-liquid-glass-button.md", "magnetic glass button with loading + success states"),
        ("Course skill learning card", "sources/codefronts/components/css-3d-tilt-hover-cards/course-skill-learning-card.md", "3D tilt card where progress is the hero"),
        ("Dark tech feature grid card", "sources/codefronts/components/css-3d-tilt-hover-cards/dark-mode-tech-feature-grid-card.md", "cursor-tracking border light on a feature grid"),
        ("Interactive discovery (hero)", "sources/motionsites/prompts/hero/interactive-discovery.md", "spotlight-reveal hero with a second image"),
        ("Rising isometric data blocks", "sources/lucianlabs/prompts/animation/202-iso-data-blocks.md", "animated isometric bar chart"),
        ("Sticky stacked cards", "sources/codefronts/components/css-cards/stacked-card-cascade.md", "cards that stack and scale on scroll"),
    ]
    rows = ["| Pattern | File | Why |", "|---|---|---|"]
    for title, path, why in picks:
        rows.append(f"| {title} | `{path}` | {why} |")
    return "\n".join(rows)


def main() -> int:
    cf = read_json(SOURCES / "codefronts" / "manifest.json") or []
    lu = read_json(SOURCES / "lucianlabs" / "manifest.json") or []
    ms = read_json(SOURCES / "motionsites" / "manifest.json") or []
    ms_catalog = read_json(SOURCES / "motionsites" / "catalog.json") or []

    if cf:
        build_codefronts(cf)
    if lu:
        build_lucian(lu)
    if ms:
        build_motionsites(ms, ms_catalog)

    total = len(cf) + len(lu) + len(ms)
    index = f"""# INDEX

Auto-generated entry point for the archive. Last build: {time.strftime('%Y-%m-%d')}.

{table([
    ('`sources/codefronts/`', f'{len(cf):,}', 'Components, layouts, navigation, motion, snippets, design styles'),
    ('`sources/lucianlabs/`', f'{len(lu):,}', 'MIT UI elements with runnable demos and ready prompts'),
    ('`sources/motionsites/`', f'{len(ms):,}', 'Free website-section prompts (paid prompts excluded)'),
])}

**Total reference files: {total:,}**

## Start here

- Read [`AGENT.md`](AGENT.md) — the working rules for any agent.
- Read [`docs/usage-recipes.md`](docs/usage-recipes.md) — copy/paste build briefs.
- Connect Arena with [`docs/arena-setup.md`](docs/arena-setup.md).

## Highest-value picks

{best_of()}

## How to search without loading everything

```bash
# all sources, filter by text across title/category/tags
for f in sources/*/manifest.json; do
  jq -r --arg q "dashboard" '.[] | select((.title + " " + (.category // "") + " " + ((.tags // []) | join(" "))) | test($q; "i")) | [.title, .path] | @tsv' "$f"
done
```

## License

Each file keeps its origin and license. See [`NOTICE.md`](NOTICE.md). Paid MotionSites content is not
included.
"""
    (ROOT / "INDEX.md").write_text(index, encoding="utf-8")

    summary = {
        "generated": time.strftime("%Y-%m-%d"),
        "totals": {"all": total, "codefronts": len(cf), "lucianlabs": len(lu), "motionsites_free": len(ms)},
        "sources": {
            "codefronts": {"manifest": "sources/codefronts/manifest.json", "readme": "sources/codefronts/README.md"},
            "lucianlabs": {"manifest": "sources/lucianlabs/manifest.json", "readme": "sources/lucianlabs/README.md"},
            "motionsites": {
                "manifest": "sources/motionsites/manifest.json",
                "catalog": "sources/motionsites/catalog.json",
                "readme": "sources/motionsites/README.md",
                "locked_entries": len([row for row in ms_catalog if not row.get('is_free')]),
            },
        },
    }
    (ROOT / "catalog.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"index built: {summary['totals']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
