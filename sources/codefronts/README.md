# CodeFronts archive

Public CSS/Tailwind component catalogue from <https://codefronts.com/>, converted into one
ready-to-paste prompt per component. Each file contains the original AI prompt (which already embeds the
working HTML/CSS/JS) plus source metadata.

- Items: **5,047**
- Format: one Markdown file per component, folder = section/category
- License: MIT, as stated inside every CodeFronts prompt
- Manifest: [`manifest.json`](manifest.json)
- Upstream: CodeFronts publishes <https://github.com/codefronts/toolkit> (MIT), but that repo holds three
  standalone CSS tools — **not** this catalogue. The 5,047 components only exist on the site, so this
  folder is collected by crawling `codefronts.com`.

## Coverage

| Folder | Items | What it is |
|---|---:|---|
| `components/` | 1,515 | UI components (buttons, cards, forms, inputs, progress) |
| `motion/` | 953 | Motion and hover effects |
| `navigation/` | 770 | Navigation patterns |
| `layouts/` | 710 | Page and section layouts |
| `snippets/` | 666 | Small snippets (badges, alerts, tooltips, chips) |
| `design-styles/` | 433 | Whole design styles (glass, neon, brutalist, minimal) |

### Categories per section

- **components** — CSS Buttons (51), Tailwind CSS Buttons (51), CSS Toggles & Switches (47), Tailwind CSS Toggles & Switches (47), CSS Modals (36), CSS Search Bars (36), CSS Stacked Cards (36), Tailwind CSS Modals (36)
- **motion** — CSS Button Hover Effects (36), Tailwind CSS Button Hover Effects (36), CSS Card Hover Effects (33), Tailwind CSS Card Hover Effects (33), CSS Hover Effects (30), CSS Keyframe Animations (30), CSS Shake Animations (30), CSS Text Animations (30)
- **navigation** — CSS Breadcrumbs (39), Tailwind CSS Breadcrumbs (39), CSS Accordions — Vertical & Horizontal (32), CSS Tabs (32), Tailwind CSS Accordions — Vertical & Horizontal (32), Tailwind CSS Tabs (32), CSS Hamburger Menus (28), Tailwind Hamburger Menus (28)
- **layouts** — CSS Timelines (32), CSS Hero Sections (31), Tailwind CSS Hero Sections (31), CSS Grid Layouts (30), CSS Sidebar Layouts (30), Tailwind CSS Grid Layouts (30), Tailwind CSS Sidebar Layouts (30), CSS Footer Designs (25)
- **snippets** — CSS Badges (30), CSS Notifications (30), CSS Dividers (26), CSS Blockquotes (25), CSS FAQ Accordions (25), Tailwind CSS Blockquotes (25), Tailwind CSS FAQ Accordion (25), CSS Tags & Chips (24)
- **design-styles** — Tailwind CSS Dark Mode UI (23), CSS Brutalism (22), CSS Dark Mode UI (22), CSS Glassmorphism (22), CSS Neumorphism (22), CSS 3D Effects (20), CSS Claymorphism (20), CSS Gradient Text Designs (20)

## Use

```bash
# find a pattern
jq -r '.[] | select((.title + " " + .category_name) | test("pricing"; "i")) | [.title, .path] | @tsv' \
  sources/codefronts/manifest.json
```

Open the file and send the prompt as-is, or lift only the HTML/CSS block. Keep the `Source:` line.
