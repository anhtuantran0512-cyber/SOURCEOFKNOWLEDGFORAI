---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/hexagonal-honeycomb/"
title: "Hexagonal Honeycomb"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A true interlocking honeycomb: pointy-top clip-path hexagons in flex rows that overlap the previous row by 30% of hex width, with alternate rows shifted half…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hexagonal Honeycomb
Source: https://codefronts.com/layouts/css-grid-layouts/hexagonal-honeycomb/

A true interlocking honeycomb: pointy-top clip-path hexagons in flex rows that overlap the previous row by 30% of hex width, with alternate rows shifted half a hex sideways so the peaks nest into the previous row's bottom notches. Amber cells glow on hover like dripping honey. The showpiece layout for team pages, skill matrices and NFT-free hexagon needs.
## HTML
```html
<section class="cgl-14" aria-label="Hexagonal honeycomb grid demo">
  <ul class="cgl-14__comb">
    <li class="cgl-14__row"><a href="#0"><strong>UI</strong></a><a href="#0"><strong>UX</strong></a><a href="#0"><strong>CSS</strong></a><a href="#0"><strong>JS</strong></a></li>
    <li class="cgl-14__row cgl-14__row--offset"><a href="#0"><strong>A11y</strong></a><a href="#0"><strong>Perf</strong></a><a href="#0"><strong>SVG</strong></a></li>
    <li class="cgl-14__row"><a href="#0"><strong>API</strong></a><a href="#0"><strong>Git</strong></a><a href="#0"><strong>SEO</strong></a></li>
  </ul>
</section>
```
## CSS
```css
.cgl-14,
.cgl-14 *,
.cgl-14 *::before,
.cgl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-14 {
  width: 100%;
  min-height: 100vh;
  --hex: 104px;
  --honey: oklch(0.8 0.15 80);
  --bg: oklch(0.18 0.03 60);
  font-family: system-ui,sans-serif;
  background: radial-gradient(100% 120% at 50% 0%,oklch(0.24 0.05 70/.9),transparent 60%),var(--bg);
  padding: 2rem 1.4rem;
  display: grid;
  place-items: center;
}
/* Honeycomb via explicit rows: each <li class="cgl-14__row"> is a flex
   row of hexagons; alternate rows carry --row--offset which shifts
   them half a hex sideways AND pulls them up 25% of hex height so the
   hexes interlock instead of stacking with gaps. This is the classic
   flex-based honeycomb pattern (Coyier / MDN) — more predictable than
   grid auto-flow arithmetic when the tile count doesn't divide evenly
   into row counts. */
/* IMPORTANT: align-items:flex-start (not center). With align-items:
   center each row would independently center itself along its own
   width — but row 2 has 3 hexes and row 1/3 have 4/3 hexes, so their
   natural centers differ. Setting all rows to share the LEFT edge
   makes the --offset shift do the actual half-hex work; otherwise
   the auto-centering fights the offset and the middle row drifts
   right (the exact bug from the previous fix pass). */

.cgl-14 .cgl-14__comb {
  list-style: none;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
/* gap:0 within a row — pointy-top hexes touch at flat vertical edges,
   and any gap accumulates differently in rows of different tile counts
   (row 1 has 3 gaps × 2px = +6px; row 2 has 2 gaps × 2px = +4px),
   which drifts the notch positions and prevents the offset row's peaks
   from landing precisely in the row-above notches. Zero gap makes
   hex/2 the mathematically exact half-hex offset. */

.cgl-14 .cgl-14__row {
  list-style: none;
  display: flex;
  gap: 0;
}
/* POINTY-TOP honeycomb math (much simpler than flat-top for row-based
   layouts): each hex box is W wide × 1.155W tall (H = W × 2/√3, since
   the vertical span is corner-to-corner). Same-row hexes touch flat
   vertical edges → no overlap needed within a row (gap:2px is just
   breathing room). Consecutive rows overlap by 25% of hex height (0.25H
   = 0.2887W), so margin-block-start = -0.2887W pulls each new row into
   the previous row's bottom-notch region. Offset rows shift W/2
   sideways so their peaks slot into the diamond gaps between the
   previous row's hex-tops. */

.cgl-14 .cgl-14__row + .cgl-14__row {
  margin-block-start: calc(var(--hex) * -0.3);
}

.cgl-14 .cgl-14__row--offset {
  margin-inline-start: calc(var(--hex) / 2);
}
/* Exact half-hex shift; peaks land in row-above notches. */
/* Adjacent hexes with gap:0 need visual separation to read as
   individual cells rather than one merged blob. Use a nested inner
   hex trick: the outer <a> is a slightly larger hex acting as a
   subtle border; the inner ::before is the fill hex inset by 2px on
   each side. The 2px gap between the outer edge and inner fill reads
   as a hairline outline WITHOUT breaking the honeycomb math (the
   outer hex tiles remain edge-to-edge). */

.cgl-14 .cgl-14__comb a {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: var(--hex);
  aspect-ratio: 1/1.1547;
  clip-path: polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
  background: color-mix(in oklab,var(--honey) 40%,var(--bg));
  text-decoration: none;
  transition: background .25s ease,scale .25s ease;
}

.cgl-14 .cgl-14__comb a::before {
  content: '';
  position: absolute;
  inset: 3px;
  clip-path: polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
  background: color-mix(in oklab,var(--honey) 22%,var(--bg));
  pointer-events: none;
  transition: background .25s ease;
}

.cgl-14 .cgl-14__comb strong {
  position: relative;
  z-index: 1;
}

.cgl-14 .cgl-14__comb a:hover,
.cgl-14 .cgl-14__comb a:focus-visible {
  scale: 1.06;
  outline: none;
  z-index: 1;
}

.cgl-14 .cgl-14__comb a:hover::before,
.cgl-14 .cgl-14__comb a:focus-visible::before {
  background: var(--honey);
}

.cgl-14 .cgl-14__comb a:hover strong,
.cgl-14 .cgl-14__comb a:focus-visible strong {
  color: var(--bg);
}

.cgl-14 .cgl-14__comb strong {
  font-size: .82rem;
  letter-spacing: .06em;
  color: var(--honey);
}

@media (prefers-reduced-motion: reduce) {
  .cgl-14 .cgl-14__comb a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pointy-top hexes in flex rows with -30% margin-block-start overlap; alternate rows shift half a hex sideways via margin-inline-start so peaks nest into the row-above notches; clip-path cuts each hexagon. */
```
