# SOURCEOFKNOWLEDGFORAI

Front-end design reference archive with 5,768 structured markdown prompts, metadata indexes, and standalone demos.

## Table of Contents

- [Overview](#overview)
- [Contents](#contents)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Search](#search)
- [Refresh Archive](#refresh-archive)
- [Scope](#scope)
- [License](#license)

## Overview

This repository organizes public UI component prompts, design tokens, and standalone HTML/CSS/JS demos into category folders with machine-readable `manifest.json` indexes.

## Contents

| Source | Items | Contents | License |
| --- | ---: | --- | --- |
| [`sources/codefronts/`](sources/codefronts/) | 5,047 | CSS/Tailwind components, layouts, navigation, and motion prompts | MIT (CodeFronts) |
| [`sources/lucianlabs/`](sources/lucianlabs/) | 400 | 200 interface and 200 animation prompts with demos and tokens | MIT |
| [`sources/motionsites/`](sources/motionsites/) | 321 | Free section briefs (hero, pricing, footer, dashboards) | MotionSites free tier |

Paid MotionSites prompts are excluded. See [`NOTICE.md`](NOTICE.md).

## Quick Start

```bash
git clone https://github.com/broamstuck-cybr/SOURCEOFKNOWLEDGFORAI.git
cd SOURCEOFKNOWLEDGFORAI
```

1. Read [`docs/RETRIEVAL_GUIDE.md`](docs/RETRIEVAL_GUIDE.md) for lookup rules.
2. Browse [`INDEX.md`](INDEX.md) for category totals and entry points.
3. See [`docs/usage-recipes.md`](docs/usage-recipes.md) for query patterns.

## Repository Structure

```text
.
├── INDEX.md
├── NOTICE.md
├── catalog.json
├── docs/
│   ├── RETRIEVAL_GUIDE.md
│   ├── repository-map.md
│   └── usage-recipes.md
├── sources/
│   ├── codefronts/
│   ├── lucianlabs/
│   └── motionsites/
├── scripts/
└── assets/previews/
```

## Search

```bash
jq -r '.[] | select((.title + " " + .category + " " + ((.tags // []) | join(" "))) | test("scroll|parallax"; "i")) | [.title, .path] | @tsv'   sources/lucianlabs/manifest.json
```

## Refresh Archive

```bash
python3 scripts/crawl_codefronts.py --resume --concurrency 12
python3 scripts/fetch_lucian.py
python3 scripts/fetch_motionsites.py 4
python3 scripts/build_index.py
python3 scripts/verify.py
```

## Scope

- Reference archive only; adapt patterns using your own project tokens and assets.
- External media URLs inside third-party prompts remain subject to their original owners.

## License

Archive structure, docs, and scripts: MIT. Third-party prompts keep their original licenses; see [`NOTICE.md`](NOTICE.md).
