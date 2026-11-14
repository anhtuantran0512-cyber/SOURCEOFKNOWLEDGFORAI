# INDEX

Auto-generated entry point for the archive. Last build: 2026-11-14.

| Folder | Items | What it is |
|---|---:|---|
| `sources/codefronts/` | 5,047 | Components, layouts, navigation, motion, snippets, design styles |
| `sources/lucianlabs/` | 400 | MIT UI elements with runnable demos and ready prompts |
| `sources/motionsites/` | 321 | Free website-section prompts (paid prompts excluded) |

**Total reference files: 5,768**

## Start here

- Read [`AGENT.md`](AGENT.md) — the working rules for any agent.
- Read [`docs/usage-recipes.md`](docs/usage-recipes.md) — copy/paste build briefs.
- Connect Arena with [`docs/arena-setup.md`](docs/arena-setup.md).

## Highest-value picks

| Pattern | File | Why |
|---|---|---|
| Liquid glass button | `sources/lucianlabs/prompts/interface/001-liquid-glass-button.md` | magnetic glass button with loading + success states |
| Course skill learning card | `sources/codefronts/components/css-3d-tilt-hover-cards/course-skill-learning-card.md` | 3D tilt card where progress is the hero |
| Dark tech feature grid card | `sources/codefronts/components/css-3d-tilt-hover-cards/dark-mode-tech-feature-grid-card.md` | cursor-tracking border light on a feature grid |
| Interactive discovery (hero) | `sources/motionsites/prompts/hero/interactive-discovery.md` | spotlight-reveal hero with a second image |
| Rising isometric data blocks | `sources/lucianlabs/prompts/animation/202-iso-data-blocks.md` | animated isometric bar chart |
| Sticky stacked cards | `sources/codefronts/components/css-cards/stacked-card-cascade.md` | cards that stack and scale on scroll |

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
