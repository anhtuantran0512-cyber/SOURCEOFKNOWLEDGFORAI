# Usage recipes

Copy a recipe, fill the bracketed parts, send it to the agent. Every recipe follows the same shape:
**find → choose ≤2 → adapt → verify**. The examples below point at files that exist in this archive.

---

## Recipe 1 — Premium landing hero

```
Read AGENT.md.

Build the hero section for [PRODUCT] in [src/app/page.tsx].
References (max two):
- sources/motionsites/prompts/hero/interactive-discovery.md        (structure + art direction)
- sources/lucianlabs/prompts/interface/001-liquid-glass-button.md   (button motion)

Rules: project palette via tokens, real copy, no lorem ipsum, 390/768/1440,
reduced motion keeps the final state. Report what you verified.
```

Why this pair: MotionSites gives a complete section brief with layout, fonts and asset slots;
lucianLabs gives a small, high-craft interaction that survives the port.

---

## Recipe 2 — Pricing section that does not look templated

```
Build a pricing section for [PRODUCT] with 3 tiers: [NAMES].
Reference: sources/motionsites/prompts/pricing/[pick-one].md
Secondary (optional): sources/codefronts/components/css-3d-tilt-hover-cards/interactive-pricing-tier-card.md

Constraints:
- Prices and features come from [CONFIG FILE], never hard-coded.
- One accent colour only; no purple-to-blue gradients.
- Keyboard focus on every plan card; toggle is a real radio group.
- No fake "most popular" badge unless the data says so.
```

---

## Recipe 3 — Dashboard with real density

```
Build the analytics dashboard shell for [PRODUCT].
References:
- sources/lucianlabs/prompts/interface/[chart-item].md   (chart motion + tokens)
- sources/codefronts/design-styles/[style-item].md       (surface treatment)

Requirements: 12-column grid, cards use the same radius/shadow scale, numbers
have tabular figures, empty and loading states exist, no chart without a legend
and an accessible summary. Verify at 390/768/1440.
```

Look up the exact item first:

```bash
jq -r '.[] | select(.category | test("Widgets|Charts|Analytics"; "i")) | [.id, .title, .path] | @tsv' \
  sources/lucianlabs/manifest.json sources/codefronts/manifest.json
```

---

## Recipe 4 — Auth flow with passkeys / OTP

```
Build sign-in, sign-up and OTP verification for [PRODUCT].
Reference: sources/lucianlabs/prompts/interface/[auth-item].md
Rules: visible labels, errors next to fields, disabled state never hides the
reason, password manager friendly (autocomplete attributes), 44px targets,
works with keyboard only, no dead "social login" buttons.
```

---

## Recipe 5 — Scroll storytelling

```
Build a scroll-driven product story for [PRODUCT].
Reference: sources/codefronts/motion/[scroll-item].md
Rules: content is readable with scripting off; animations use transform/opacity
only; prefers-reduced-motion swaps to a static stacked layout; no scroll-jacking;
each section has a text alternative for the visual.
```

Find candidates:

```bash
jq -r '.[] | select((.title + " " + .category) | test("scroll|parallax|sticky"; "i")) | [.title, .path] | @tsv' \
  sources/codefronts/manifest.json
```

---

## Recipe 6 — Navigation that scales

```
Build the top navigation + mobile drawer for [PRODUCT].
Reference: sources/codefronts/navigation/[pick-one].md
Rules: max 5 primary links, active state is not colour-only, drawer traps focus
and closes on Escape, skip-link present, sticky header does not cover anchors.
```

---

## Recipe 7 — Polish pass on an existing page

```
Audit [PAGE] against AGENT.md §3 and fix only what is broken.
Do not redesign. Report a table: issue, evidence, fix, verified at which viewport.
```

This is the highest-value recipe for existing projects: the archive is only used to source a better
pattern when a section is structurally wrong.

---

## Recipe 8 — Refresh the archive

```bash
python3 scripts/fetch_lucian.py
python3 scripts/fetch_motionsites.py 4      # 4 = concurrency
python3 scripts/crawl_codefronts.py --resume --concurrency 12
python3 scripts/build_index.py
python3 scripts/verify.py
```

Run this on a separate branch, never in the same PR as product work.

---

## Composing two references safely

- Take **structure** from one file and **motion** from another. Never merge two colour systems.
- If both define a token with the same name, the project's token wins.
- If the references disagree on spacing, keep the stricter 8 px scale.
- Strip gallery-specific markup (`body` centering, demo wrappers, theme toggle buttons) before porting.
