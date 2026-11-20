# INDEX

Auto-generated entry point for the archive. Last build: 2026-11-20.

| Folder | Items | What it is |
|---|---:|---|
| `sources/codefronts/` | 5,047 | Components, layouts, navigation, motion, snippets, design styles |
| `sources/getlayers/` | 892 | Five libraries (templates, 3D scenes, sections, backgrounds, gradients): stack, tone, frame timings, Lighthouse, previews, 18 free prompts |
| `sources/lucianlabs/` | 400 | MIT UI elements with runnable demos and ready prompts |
| `sources/motionsites/` | 321 | Free website-section prompts (paid prompts excluded) |
| `sources/pinui/` | 41 | 30 React components + 11 blocs, TSX/CSS source, shadcn install |
| `sources/threeui/` | 961 | 3D/WebGL/motion catalogue + 1,485 tag pages (metadata only) |

**Total reference items: 7,662** (+1,485 ThreeUI tag pages)

## Source priority

1. **Pin UI** — real React source, correct behaviour, MIT. Start here for interactive components.
2. **ThreeUI** — 3D/WebGL/motion direction with runtime and live demo; reference only, no source.
3. **MotionSites** — whole-section briefs and art direction.
4. **lucianLabs** — highest craft per element, working code, runnable demo.
5. **CodeFronts** — widest coverage, component-sized CSS/Tailwind snippets.
6. **GetLayers** — five libraries of immersive work (templates, 3D scenes, sections, backgrounds,
   gradients) with stack, tone and a measured performance budget; free prompts verbatim, premium locked.

Each library has a generated `INDEX.md` listing every item: `sources/<name>/INDEX.md`.

## Start here

- Read [`START_HERE.md`](START_HERE.md) — binding rules, 100% coverage gate, priority order, verification.
- Machine map for crawlers: [`llms.txt`](llms.txt).
- What is in each library, item by item: [`sources/README.md`](sources/README.md) → `sources/<name>/INDEX.md`.
- Read [`docs/RETRIEVAL_GUIDE.md`](docs/RETRIEVAL_GUIDE.md) — lookup workflow in detail.
- Read [`docs/usage-recipes.md`](docs/usage-recipes.md) — copy/paste build briefs.
- Connect an agent with [`docs/arena-setup.md`](docs/arena-setup.md).

## Highest-value picks

| Pattern | File | Why |
|---|---|---|
| Liquid glass button | `sources/lucianlabs/prompts/interface/001-liquid-glass-button.md` | magnetic glass button with loading + success states |
| Theme switch (rain/drip/fireworks) | `sources/pinui/registry/theme-switch/` | dark-mode toggle with a real state engine, TSX + CSS |
| Course skill learning card | `sources/codefronts/components/css-3d-tilt-hover-cards/course-skill-learning-card.md` | 3D tilt card where progress is the hero |
| Dark tech feature grid card | `sources/codefronts/components/css-3d-tilt-hover-cards/dark-mode-tech-feature-grid-card.md` | cursor-tracking border light on a feature grid |
| Smart pricing block | `sources/pinui/blocx/smart-pricing/` | whole pricing section, source included |
| Interactive discovery (hero) | `sources/motionsites/prompts/hero/interactive-discovery.md` | spotlight-reveal hero with a second image |
| Rising isometric data blocks | `sources/lucianlabs/prompts/animation/202-iso-data-blocks.md` | animated isometric bar chart |
| WebGL particle background | `sources/threeui/items/backgrounds/` | direction + runtime for canvas/Three.js backgrounds |
| Sticky stacked cards | `sources/codefronts/components/css-cards/stacked-card-cascade.md` | cards that stack and scale on scroll |
| Cinematic 3D product hero | `sources/getlayers/items/soda/ITEM.md` | free prompt: one-file Three.js hero, 37 KB brief, measured at 60 fps |

## How to search without loading everything

```bash
# all sources, filter by text across title/category/tags
for f in sources/*/manifest.json; do
  jq -r --arg q "dashboard" '.[] | select((.title + " " + (.category // "") + " " + ((.tags // []) | join(" "))) | test($q; "i")) | [.title, .path] | @tsv' "$f"
done
```

## License

Each file keeps its origin and license. See [`NOTICE.md`](NOTICE.md). Paid MotionSites content,
ThreeUI source files and the 874 premium GetLayers items are not included.
