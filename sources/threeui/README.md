# ThreeUI — 3D, WebGL and motion catalogue

Catalogue of interactive 3D and animated web design from <https://threeui.com/browse?sort=recent>.
This folder is an index of the **public catalogue**: what exists, which runtime it needs, and where the
live demo is. It is not a source dump.

- Site: <https://threeui.com/>
- Upstream repository: none. ThreeUI publishes no GitHub repo; the component source is sold through
  their authenticated Pro MCP.
- Items: **961** · tag pages: **1,485**
- Files: `items/<category>/<slug>.md` (one brief per item), `manifest.json`, `catalog.json`,
  `catalog.jsonl`, `tags.json`

## Categories

| Category | Items |
|---|---:|
| Sections | 222 |
| Backgrounds | 151 |
| Three.js | 140 |
| Landing pages | 98 |
| 3D assets | 96 |
| Buttons | 96 |
| UI elements | 57 |
| Hero | 38 |
| Motion design | 31 |
| Text animation | 19 |
| CSS | 13 |

## What a brief contains

Title, category, subcategory, runtime (Three.js / GSAP / CSS / R3F…), description, canonical URL, live
demo link and preview image. No component code.

## Why no source

ThreeUI sells component source through an authenticated Pro MCP (`https://threeui.com/mcp`) and premium
templates. This archive does not bypass, guess or reconstruct that. Use the catalogue to **choose a
direction and a runtime**, then build the effect yourself or buy the file.

## Use

```bash
# 3D-capable items
jq -r '.[] | select(.runtime | test("three|webgl|r3f"; "i")) | [.title, .url] | @tsv' \
  sources/threeui/manifest.json

# everything in a category
jq -r '.[] | select(.category=="Hero") | [.title, .path] | @tsv' sources/threeui/manifest.json

# tag index
jq -r '.[0:20][] | [.tag, .count] | @tsv' sources/threeui/tags.json
```

## Adapt rules

1. Reference the **effect**, not the asset. Do not copy preview images or brand video.
2. Match the runtime to the project: do not add Three.js for a hover effect CSS can do.
3. Budget for it — WebGL scenes need a perf check (frame time, mobile GPU, `prefers-reduced-motion`).
4. Every 3D hero needs a static poster and a no-WebGL fallback.
