# sources/ — the six libraries

**7,662 reference items.** Open the `INDEX.md` of a folder to see every item it holds; open `README.md` for how that source was collected and licensed.

## Read in this order

| # | Folder | Items | Read first | Why |
|---|---|---:|---|---|
| 1 | [`pinui/`](pinui/) | 41 | [`INDEX.md`](pinui/INDEX.md) | Real React source, MIT, installable. Start here for interactive components. |
| 2 | [`threeui/`](threeui/) | 961 | [`INDEX.md`](threeui/INDEX.md) | 3D / WebGL / motion direction with runtime and live demo. Metadata only. |
| 3 | [`motionsites/`](motionsites/) | 321 | [`INDEX.md`](motionsites/INDEX.md) | Whole-section briefs and art direction. Free prompts only. |
| 4 | [`lucianlabs/`](lucianlabs/) | 400 | [`INDEX.md`](lucianlabs/INDEX.md) | Highest craft per element: MIT, working code, runnable demo. |
| 5 | [`codefronts/`](codefronts/) | 5047 | [`INDEX.md`](codefronts/INDEX.md) | Breadth: 5,047 CSS/Tailwind components, layouts, motion, design styles. |
| 6 | [`getlayers/`](getlayers/) | 892 | [`INDEX.md`](getlayers/INDEX.md) | Five libraries — templates, 3D scenes, sections, backgrounds, gradients — with stack, tone and measured performance. Free prompts + metadata. |

## Choosing rule

1. Interactive component with behaviour → **pinui** (real React source).
2. Micro-interaction, chart, form, dashboard → **lucianlabs** (MIT, working code).
3. Whole section or landing-page structure → **motionsites**.
4. 3D, WebGL, scroll-driven hero → **threeui** for direction, then build.
5. Anything else — layout, navigation, motion, design style → **codefronts**.
6. Whole page or hero with a named stack and a measured perf budget → **getlayers**.

All six must be checked before code is written; the coverage block is defined in [`../START_HERE.md`](../START_HERE.md).

## Machine-readable

- `manifest.json` per folder: id, title, category, tags, path.
- `catalog.json` per folder: original catalogue metadata.
- Root [`catalog.json`](../catalog.json): totals for every source.
