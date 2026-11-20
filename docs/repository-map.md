# Repository map

## Top level

| Path | Role |
|---|---|
| `README.md` | Human entry point, counts, quick start. |
| `docs/RETRIEVAL_GUIDE.md` | Rules + retrieval workflow. An agent reads this before writing code. |
| `INDEX.md` | Generated map: totals, categories, best picks, search snippets. |
| `NOTICE.md` | Licenses, attribution, takedown policy. |
| `catalog.json` | Machine summary of every source and count. |
| `verify-report.json` | Output of the last `scripts/verify.py` run. |

## `sources/codefronts/`

```
sources/codefronts/
├── README.md
├── manifest.json                 # 5,047 rows
├── components/<category>/<slug>.md
├── motion/<category>/<slug>.md
├── navigation/<category>/<slug>.md
├── layouts/<category>/<slug>.md
├── snippets/<category>/<slug>.md
└── design-styles/<category>/<slug>.md
```

One file = one component. Frontmatter: `source`, `url`, `title`, `section`, `category`,
`category_name`, `description`, `has_js`. Body: the original CodeFronts AI prompt, which contains the
description, the HTML/CSS/JS blocks and the `Source:` line.

## `sources/lucianlabs/`

```
sources/lucianlabs/
├── README.md
├── manifest.json                 # 400 rows
├── catalog.json                  # original Korean/English metadata
├── tokens.css                    # --ux-* light/dark tokens
├── prompts/
│   ├── interface/001-...md       # 200 items
│   └── animation/201-...md       # 200 items
└── demos/
    ├── interface/001-....html    # runnable standalone demo
    └── animation/201-....html
```

Each prompt is the site's own `[Element] / [What it does] / [How to use it]` block plus the application
guide and the full working code. Each demo is self-contained: open it in a browser; the theme toggle is
in the top-right corner.

## `sources/motionsites/`

```
sources/motionsites/
├── README.md
├── manifest.json                 # 321 free prompts
├── catalog.json                  # 772 public entries, `is_free` marks access
└── prompts/<category>/<id>.md
```

Only free prompts have files. `catalog.json` is an index of public listings and is useful for discovering
what kind of sections exist; `is_free: false` entries have no content here and must stay that way.

## `sources/pinui/`

```
sources/pinui/
├── README.md
├── manifest.json                 # 41 rows
├── catalog.json                  # 50 public pages with URL + preview
├── registry/
│   ├── registry.json             # the site's own shadcn registry
│   ├── summary.json
│   └── <name>/ITEM.md + meta.json + *.tsx + *.css
├── blocx/
│   ├── summary.json
│   └── <name>/ITEM.md + meta.json + *.tsx + *.css
└── pages/<slug>.md               # 50 page briefs
```

Unlike the prompt folders, this one holds **real source code**. Keep the MIT header comment when you
adapt a component, and keep the per-component CSS prefix intact.

## `sources/threeui/`

```
sources/threeui/
├── README.md
├── manifest.json                 # 961 rows
├── catalog.json                  # items + labels + tag list
├── catalog.jsonl                 # one JSON object per line, for streaming
├── tags.json                     # 1,485 tags
└── items/<category>/<slug>.md    # one brief per catalogue item
```

Metadata only: title, category, runtime, description, live URL, preview image. Component source is sold
through ThreeUI's Pro MCP and is deliberately absent — briefs link to the live page instead.

## `sources/getlayers/`

```
sources/getlayers/
├── README.md
├── manifest.json                 # 62 rows
├── catalog.json                  # the public catalogue, as the site ships it
├── INDEX.md
├── items/<id>/ITEM.md            # brief: direction, stack, frame timings, Lighthouse
├── items/<id>/metadata.json      # full public record + page JSON-LD
├── prompts/<id>.md               # free-tier prompts, verbatim
└── assets/<id>.webp              # poster still (+ -figma.webp where published)
```

Whole-page and hero templates. The metadata is complete; the prompts are not. 11 templates are free and
51 are premium — premium copy answers `forbidden` and is never included. Free prompts are copied through
the public copy action, which allows one prompt per anonymous visitor per day.

## Adding a new source

1. Create `sources/<name>/`.
2. Collect only content the source publishes publicly or licenses for reuse.
3. Write one markdown file per item with YAML frontmatter: `source`, `url`, `title`, `category`, `license`.
4. Add `manifest.json` rows with `path`, `title`, `category`, `tags`, `prompt_chars`.
5. Add `README.md` with origin, collection date, license and counts.
6. Update `scripts/build_index.py` if the manifest schema differs.
7. Run `python3 scripts/verify.py` and commit on a branch.

## Naming rules

- Folder names: lowercase, hyphenated (`hero-section`, `css-3d-tilt-hover-cards`).
- Item files: slug of the title, stable over time. lucianLabs keeps its numeric id prefix.
- Never rename a file without updating `manifest.json` — agents resolve paths from there.

## Size policy

The repository is text-only. No videos, no font binaries, no image dumps. Screenshots in
`assets/previews/` are small and only used by the README. If a reference needs media, link to the original
URL instead of committing it.

One named exception: `sources/getlayers/assets/` holds one poster still per template (62 × ~130 KB) and
the Figma preview where the site publishes one (40 × ~150 KB) — about 16 MB, because the still is the
only way to see what a template looks like when the source is premium. Its four mp4 mockups and two
Lighthouse HTML reports per template are **not** committed; those URLs live in each `ITEM.md`.
