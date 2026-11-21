#!/usr/bin/env python3
"""Generate one browsable INDEX.md per source plus `sources/README.md` and `llms.txt`.

An agent that only reaches GitHub reads these markdown files to learn what exists,
without cloning 66 MB or loading the JSON manifests.

Usage: python3 scripts/build_source_indexes.py
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"

PRIORITY = [
    ("pinui", 1, "Real React source, MIT, installable. Start here for interactive components."),
    ("threeui", 2, "3D / WebGL / motion direction with runtime and live demo. Metadata only."),
    ("motionsites", 3, "Whole-section briefs and art direction. Free prompts only."),
    ("lucianlabs", 4, "Highest craft per element: MIT, working code, runnable demo."),
    ("codefronts", 5, "Breadth: 5,047 CSS/Tailwind components, layouts, motion, design styles."),
    ("getlayers", 6, "Five libraries — templates, 3D scenes, sections, backgrounds, gradients — with stack, tone and measured performance. Free prompts + metadata."),
]


def load(name: str) -> list[dict]:
    return json.loads((SOURCES / name / "manifest.json").read_text(encoding="utf-8"))


def rel(link_path: str, name: str) -> str:
    """Manifest paths are repo-relative; INDEX.md sits inside sources/<name>/."""
    prefix = f"sources/{name}/"
    return link_path[len(prefix):] if link_path.startswith(prefix) else link_path


def clip(text: str, limit: int) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"  {path.relative_to(ROOT)}  ({len(text.splitlines())} lines)")


def head(title: str, total: int, rank: int, note: str, extra: str = "") -> str:
    return (
        f"# {title}\n\n"
        f"> Auto-generated from `manifest.json` — do not edit by hand, run "
        f"`scripts/build_source_indexes.py`.\n"
        f"> **{total} items** · priority {rank} of 6 · {note}\n{extra}\n"
    )


def index_pinui() -> None:
    rows = load("pinui")
    groups = defaultdict(list)
    for row in rows:
        groups["Components" if row["kind"] == "component" else "Blocx"].append(row)
    out = head(
        "Pin UI — index", len(rows), 1,
        "MIT components and page sections with real TSX/CSS.",
        "\nInstall any item: `npx shadcn@latest add \"https://www.pinui.xyz/r/<name>.json\"`.\n"
        "Each folder holds `ITEM.md` (what it does + install), `meta.json`, the `.tsx` and its `.css`.\n",
    )
    for group, items in groups.items():
        out += f"\n## {group} ({len(items)})\n\n| Title | What it does | Folder |\n|---|---|---|\n"
        for row in sorted(items, key=lambda r: r["title"]):
            link = rel(row["path"], "pinui")
            out += f"| **{row['title']}** | {clip(row.get('description', ''), 110)} | [`{link}/`]({link}) |\n"
    write(SOURCES / "pinui/INDEX.md", out)


def index_threeui() -> None:
    rows = load("threeui")
    groups = defaultdict(list)
    for row in rows:
        groups[row["category"]].append(row)
    out = head(
        "ThreeUI — index", len(rows), 2,
        "Catalogue of 3D, WebGL and motion work. No source files: choose a direction, then build or buy.",
        "\nRuntime tells you the cost: CSS/GSAP is cheap, Three.js/R3F needs a perf budget.\n",
    )
    out += "\n| Category | Items |\n|---|---:|\n"
    for cat, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        out += f"| {cat} | {len(items)} |\n"
    for cat, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        out += f"\n## {cat} ({len(items)})\n\n| Title | Runtime | Live | Brief |\n|---|---|---|---|\n"
        for row in sorted(items, key=lambda r: r["title"]):
            link = rel(row["path"], "threeui")
            out += (
                f"| {row['title']} | {clip(row.get('runtime', ''), 34)} | "
                f"[demo]({row['url']}) | [`{link.split('/')[-1]}`]({link}) |\n"
            )
    write(SOURCES / "threeui/INDEX.md", out)


def index_motionsites() -> None:
    rows = load("motionsites")
    out = head(
        "MotionSites AI — index", len(rows), 3,
        "Free website-section prompts (hero, pricing, footer, ecommerce, SaaS). Paid prompts excluded.",
        "\nEach file is a section brief with layout, copy direction and the code block the site publishes.\n",
    )
    out += "\n| Title | Category | Brief |\n|---|---|---|\n"
    for row in sorted(rows, key=lambda r: (r["category"], r["title"])):
        link = rel(row["path"], "motionsites")
        out += f"| {row['title']} | {row['category']} | [`{link.split('/')[-1]}`]({link}) |\n"
    write(SOURCES / "motionsites/INDEX.md", out)


def index_lucianlabs() -> None:
    rows = load("lucianlabs")
    groups = defaultdict(list)
    for row in rows:
        groups[row["category"]].append(row)
    out = head(
        "lucianLabs — index", len(rows), 4,
        "MIT elements with working code, theme tokens and a runnable demo. 400/400 matches the upstream repo.",
        "\nEvery prompt is ready to paste; `demos/...html` opens in a browser. Tokens live in `tokens.css`.\n",
    )
    for cat, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        out += f"\n## {cat} ({len(items)})\n\n| # | Title | Tags | Prompt | Demo |\n|---|---|---|---|---|\n"
        for row in sorted(items, key=lambda r: r["id"]):
            tags = ", ".join(row.get("tags", [])[:4])
            prompt_link = rel(row["prompt_path"], "lucianlabs")
            demo_link = rel(row["demo_path"], "lucianlabs")
            out += (
                f"| {row['id']} | {row['title']} | {tags} | "
                f"[`{prompt_link.split('/')[-1]}`]({prompt_link}) | "
                f"[demo]({demo_link}) |\n"
            )
    write(SOURCES / "lucianlabs/INDEX.md", out)


def index_codefronts() -> None:
    rows = load("codefronts")
    sections = Counter(row["section_name"] for row in rows)
    out = head(
        "CodeFronts — index", len(rows), 5,
        "Widest standalone CSS/Tailwind coverage. Each file is a ready-to-paste prompt with code.",
        "\nToo big to read top to bottom: filter `manifest.json` or search this file "
        "(`Ctrl+F` / `grep -i`).\n",
    )
    out += "\n| Section | Items | Full list |\n|---|---:|---|\n"
    grouped = defaultdict(lambda: defaultdict(list))
    for row in rows:
        grouped[row["section_name"]][row["category_name"]].append(row)
    for name, count in sections.most_common():
        slug = name.lower().replace(" & ", "-").replace(" ", "-")
        out += f"| {name} | {count} | [`index/{slug}.md`](index/{slug}.md) |\n"
    out += (
        "\nThe per-section files under `index/` list every item as a link. "
        "Search them with `grep -i \"pricing\" sources/codefronts/index/*.md`.\n"
    )
    (SOURCES / "codefronts/index").mkdir(parents=True, exist_ok=True)
    for section, cats in grouped.items():
        slug = section.lower().replace(" & ", "-").replace(" ", "-")
        part = (
            f"# CodeFronts — {section} ({sum(len(v) for v in cats.values())} items)\n\n"
            f"> Part of [`../INDEX.md`](../INDEX.md). Full metadata: [`../manifest.json`](../manifest.json).\n"
        )
        for cat, items in sorted(cats.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            part += f"\n## {cat} ({len(items)})\n\n"
            for row in sorted(items, key=lambda r: r["title"]):
                part += f"- [{row['title']}](../{rel(row['path'], 'codefronts')})\n"
        write(SOURCES / f"codefronts/index/{slug}.md", part)
    write(SOURCES / "codefronts/INDEX.md", out)


GETLAYERS_GROUPS = [
    ("template", "Templates — full pages and heroes"),
    ("3d_scene", "3D scenes — WebGL, particles, terrain"),
    ("section", "Sections — one block, ready to place"),
    ("background", "Backgrounds — animated and still backdrops"),
    ("gradient", "Gradients — pure-WebGL looks"),
]


def index_getlayers() -> None:
    rows = load("getlayers")
    groups = defaultdict(list)
    for row in rows:
        groups[row.get("category") or "—"].append(row)
    out = head(
        "GetLayers — index", len(rows), 6,
        "Five libraries of immersive web work: templates, 3D scenes, sections, backgrounds, gradients.",
        "\n`ITEM.md` carries the art direction, stack, variants, frame timings and Lighthouse scores; "
        "`prompts/` holds the free prompts verbatim. Premium prompts are not in this archive.\n",
    )
    out += "\n| Library | Items | Free |\n|---|---:|---:|\n"
    for key, label in GETLAYERS_GROUPS:
        items = groups.get(key, [])
        free = sum(1 for row in items if row.get("tier") == "Free")
        out += f"| {label.split(' — ')[0]} | {len(items)} | {free} |\n"
    for key, label in GETLAYERS_GROUPS:
        items = groups.get(key, [])
        if not items:
            continue
        out += (
            f"\n## {label} ({len(items)})\n\n"
            "| Title | Tone | Tier | Likes | Brief |\n|---|---|---|---:|---|\n"
        )
        for row in sorted(items, key=lambda r: -(r.get("likes") or 0)):
            link = rel(row["path"], "getlayers")
            out += (
                f"| {row['title']} | {row.get('tone', '—')} | {row.get('tier', '—')} | "
                f"{row.get('likes', 0)} | [`{link.split('/')[-2]}`]({link}) |\n"
            )
    write(SOURCES / "getlayers/INDEX.md", out)


MEDIA_FIELDS = ("image", "posterVideo", "posterVideoPreview", "mockupDesktop", "mockupMobile", "figmaPreview")


def index_getlayers_media() -> None:
    """Complete media inventory — every published file, its size and its URL.

    The bytes stay on the CDN: 10 GB does not belong in a git repository. This file
    is the map, so nothing is missing and nothing has to be guessed.
    """
    sizes = json.loads((SOURCES / "getlayers" / "media-sizes.json").read_text(encoding="utf-8"))
    seen: dict[str, tuple[str, str, str, int]] = {}
    for key, _label in GETLAYERS_GROUPS:
        items = json.loads((SOURCES / "getlayers" / "catalog" / f"{key}.json").read_text(encoding="utf-8"))
        for item in items:
            pairs = [(field, item.get(field)) for field in MEDIA_FIELDS]
            for variant in item.get("variants") or []:
                pairs += [(f"variant.{field}", variant.get(field)) for field in ("heroVideo", "previewVideo", "poster")]
            for field, url in pairs:
                if url and url not in seen:
                    seen[url] = (key, item["id"], field, sizes.get(url, -1))
    inventory = [(key, ident, field, url, size) for url, (key, ident, field, size) in seen.items()]
    total = sum(max(size, 0) for *_, size in inventory)
    unknown = sum(1 for *_, size in inventory if size < 0)
    out = (
        "# GetLayers — media inventory\n\n"
        "> Auto-generated from `catalog/*.json` and `media-sizes.json` — do not edit by hand, run "
        "`scripts/build_source_indexes.py`.\n"
        f"> **{len(inventory):,} files · {total / 1e9:.1f} GB** — measured with a `HEAD` request on "
        "2026-11-20.\n\n"
        f"The full set is **not committed**: at {total / 1e9:.1f} GB it is far past GitHub's 100 MB per-file "
        "and 5 GB per-repository limits, and a clone would take hours. Every file stays on GetLayers' CDN; this "
        "inventory lists each unique file once, with its size, so a reader can fetch exactly what a "
        "project needs:\n\n"
        "```bash\n"
        "curl -O <url>                                     # one file\n"
        "python3 scripts/fetch_getlayers.py --media video  # mockups + preview clips\n"
        "python3 scripts/fetch_getlayers.py --media all    # + hero video and Lighthouse HTML\n"
        "python3 scripts/fetch_getlayers_free.py          # the free tier, into media/\n"
        "```\n\n"
        "The poster stills for all 892 items *are* committed, in `assets/`.\n"
    )
    free_media = SOURCES / "getlayers" / "media-free.json"
    if free_media.exists():
        free = json.loads(free_media.read_text(encoding="utf-8"))
        out += (
            f"\nThe **free tier is committed** too: {free['items']} free items, {free['files']} files, "
            f"{free['bytes'] / 1e6:.0f} MB, in `media/<id>/` — every video, still and Lighthouse report "
            "the site publishes for them, downloaded by `scripts/fetch_getlayers_free.py`. Premium media "
            "is not fetched at all. To browse that set, open `gallery.html` — it plays the local files "
            "and needs no server.\n"
        )
    out += "\n| Library | Files | Size |\n|---|---:|---:|\n"
    for key, label in GETLAYERS_GROUPS:
        rows = [row for row in inventory if row[0] == key]
        out += f"| {label.split(' — ')[0]} | {len(rows)} | {sum(max(row[4], 0) for row in rows) / 1e9:.2f} GB |\n"
    if unknown:
        out += f"\n_{unknown} files reported no `Content-Length`; counted as 0._\n"
    for key, label in GETLAYERS_GROUPS:
        rows = [row for row in inventory if row[0] == key]
        if not rows:
            continue
        out += f"\n## {label} — {len(rows)} files, {sum(max(row[4], 0) for row in rows) / 1e9:.2f} GB\n\n"
        out += "| Item | Field | Size | URL |\n|---|---|---:|---|\n"
        for _key, ident, field, url, size in rows:
            shown = f"{size / 1e6:.1f} MB" if size >= 0 else "—"
            out += f"| `{ident}` | `{field}` | {shown} | {url} |\n"
    write(SOURCES / "getlayers/MEDIA.md", out)


def write_hub(counts: dict[str, int]) -> None:
    total = sum(counts.values())
    out = (
        "# sources/ — the six libraries\n\n"
        f"**{total:,} reference items.** Open the `INDEX.md` of a folder to see every item it holds; "
        "open `README.md` for how that source was collected and licensed.\n\n"
        "## Read in this order\n\n"
        "| # | Folder | Items | Read first | Why |\n|---|---|---:|---|---|\n"
    )
    for name, rank, note in PRIORITY:
        out += f"| {rank} | [`{name}/`]({name}/) | {counts[name]} | [`INDEX.md`]({name}/INDEX.md) | {note} |\n"
    out += (
        "\n## Choosing rule\n\n"
        "1. Interactive component with behaviour → **pinui** (real React source).\n"
        "2. Micro-interaction, chart, form, dashboard → **lucianlabs** (MIT, working code).\n"
        "3. Whole section or landing-page structure → **motionsites**.\n"
        "4. 3D, WebGL, scroll-driven hero → **threeui** for direction, then build.\n"
        "5. Anything else — layout, navigation, motion, design style → **codefronts**.\n"
        "6. Whole page or hero with a named stack and a measured perf budget → **getlayers**.\n\n"
        "All six must be checked before code is written; the coverage block is defined in "
        "[`../START_HERE.md`](../START_HERE.md).\n\n"
        "## Machine-readable\n\n"
        "- `manifest.json` per folder: id, title, category, tags, path.\n"
        "- `catalog.json` per folder: original catalogue metadata.\n"
        f"- Root [`catalog.json`](../catalog.json): totals for every source.\n"
    )
    write(SOURCES / "README.md", out)


def write_llms_txt(counts: dict[str, int]) -> None:
    total = sum(counts.values())
    out = (
        "# SOURCEOFKNOWLEDGFORAI\n\n"
        f"> {total:,} front-end design references from six public libraries, as markdown briefs with "
        "metadata and source links. Mandatory reference for any UI work: check all six folders, open at "
        "most three files, state what you used.\n\n"
        "## Read first\n\n"
        "- [START_HERE.md](https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/blob/main/START_HERE.md): "
        "binding rules, 100% coverage, verification.\n"
        "- [INDEX.md](https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/blob/main/INDEX.md): totals, "
        "source priority, highest-value picks.\n"
        "- [sources/README.md](https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/blob/main/sources/README.md): "
        "how to choose between the six libraries.\n\n"
        "## Libraries\n\n"
    )
    for name, rank, note in PRIORITY:
        out += (
            f"- [sources/{name}/INDEX.md](https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/blob/main/sources/{name}/INDEX.md): "
            f"{counts[name]} items — {note}\n"
        )
    out += (
        "\n## What each item is\n\n"
        "- pinui: `ITEM.md` + `meta.json` + real `.tsx`/`.css`; install with the shadcn CLI.\n"
        "- lucianlabs: prompt with full working HTML/CSS/JS + runnable demo + `tokens.css`.\n"
        "- motionsites: whole-section brief (free prompts only).\n"
        "- threeui: catalogue brief — title, runtime, live URL, preview. No component source.\n"
        "- codefronts: ready-to-paste prompt containing the component's HTML/CSS/JS.\n"
        "- getlayers: five libraries — template, 3D scene, section, background, gradient — art direction, "
        "variants, frame timings, Lighthouse; free prompts verbatim.\n\n"
        "## Rules\n\n"
        "- Query every folder before choosing; record `## Source coverage (100%)` in the brief.\n"
        "- Keep license headers (MIT comments, `Source:` lines).\n"
        "- Replace demo copy, imagery and brand colours with the project's own tokens.\n"
        "- Never invent an item or a path; if nothing fits, say so and build from first principles.\n\n"
        "## Machine-readable\n\n"
        "- https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/blob/main/catalog.json\n"
        "- https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI/tree/main/sources (each folder has "
        "`manifest.json`)\n"
    )
    write(ROOT / "llms.txt", out)


def main() -> int:
    jobs = [
        index_pinui,
        index_threeui,
        index_motionsites,
        index_lucianlabs,
        index_codefronts,
        index_getlayers,
        index_getlayers_media,
    ]
    print("Generating source indexes…")
    for job in jobs:
        job()
    counts = {name: len(load(name)) for name, _, _ in PRIORITY}
    write_hub(counts)
    write_llms_txt(counts)
    print(f"total items: {sum(counts.values()):,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
