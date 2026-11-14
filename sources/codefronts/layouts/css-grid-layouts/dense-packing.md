---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/dense-packing/"
title: "Dense Packing"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "grid-auto-flow: dense, demonstrated honestly: numbered tiles with mixed spans, where the numbers reveal exactly which items the algorithm pulled backward to…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dense Packing
Source: https://codefronts.com/layouts/css-grid-layouts/dense-packing/

grid-auto-flow: dense, demonstrated honestly: numbered tiles with mixed spans, where the numbers reveal exactly which items the algorithm pulled backward to fill holes. The one grid feature that trades source order for zero gaps — and the demo teaches when that trade is safe.
## HTML
```html
<section class="cgl-24" aria-label="Dense packing demo">
  <p class="cgl-24__note">Numbers = DOM order. Spot the small tiles pulled backward to plug holes.</p>
  <div class="cgl-24__grid">
    <div class="cgl-24__cell" style="--s:2">1</div>
    <div class="cgl-24__cell">2</div>
    <div class="cgl-24__cell" style="--s:2;--r:2">3</div>
    <div class="cgl-24__cell">4</div>
    <div class="cgl-24__cell" style="--s:2">5</div>
    <div class="cgl-24__cell">6</div>
    <div class="cgl-24__cell">7</div>
    <div class="cgl-24__cell" style="--s:2">8</div>
    <div class="cgl-24__cell">9</div>
    <div class="cgl-24__cell">10</div>
    <div class="cgl-24__cell" style="--r:2">11</div>
    <div class="cgl-24__cell">12</div>
    <div class="cgl-24__cell">13</div>
    <div class="cgl-24__cell" style="--s:2">14</div>
    <div class="cgl-24__cell">15</div>
  </div>
</section>
```
## CSS
```css
.cgl-24,
.cgl-24 *,
.cgl-24 *::before,
.cgl-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-24 {
  width: 100%;
  min-height: 100vh;
  --grape: oklch(0.55 0.18 310);
  --bg: oklch(0.17 0.025 310);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-24 .cgl-24__note {
  font-size: .72rem;
  color: oklch(0.7 0.06 310);
  margin-block-end: .9rem;
}

.cgl-24 .cgl-24__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(76px,100%),1fr));
  grid-auto-rows: 64px;
  grid-auto-flow: row dense;
  gap: 8px;
}

.cgl-24 .cgl-24__cell {
  grid-column: span var(--s,1);
  grid-row: span var(--r,1);
  display: grid;
  place-items: center;
  font-size: 1.05rem;
  font-weight: 700;
  color: oklch(0.9 0.05 310);
  background: color-mix(in oklab,var(--grape) 30%,var(--bg));
  border: 1px solid color-mix(in oklab,var(--grape) 50%,var(--bg));
  border-radius: 10px;
}

.cgl-24 .cgl-24__cell:nth-child(odd) {
  background: color-mix(in oklab,var(--grape) 18%,var(--bg));
}
```

## JavaScript
```js
/* No JavaScript — grid-auto-flow: row dense backfills holes; the numbered tiles expose the reordering. */
```
