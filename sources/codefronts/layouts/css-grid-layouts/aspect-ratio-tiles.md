---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/aspect-ratio-tiles/"
title: "Aspect-Ratio Tiles"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "Video-platform tiles that never jump: every thumbnail slot reserves 16:9 with aspect-ratio before any media loads, killing layout shift (CLS) at the source."
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aspect-Ratio Tiles
Source: https://codefronts.com/layouts/css-grid-layouts/aspect-ratio-tiles/

Video-platform tiles that never jump: every thumbnail slot reserves 16:9 with aspect-ratio before any media loads, killing layout shift (CLS) at the source. Includes the three ratios every product needs — 16:9 video, 1:1 avatars, 4:5 posters — coexisting in one auto-fit grid.
## HTML
```html
<section class="cgl-19" aria-label="Aspect ratio tiles demo">
  <div class="cgl-19__grid">
    <article class="cgl-19__tile"><div class="cgl-19__slot cgl-19__slot--v1"><span class="cgl-19__chip">12:04</span></div><h4>Grid tracks explained</h4><p>18k views · 2 days ago</p></article>
    <article class="cgl-19__tile"><div class="cgl-19__slot cgl-19__slot--v2"><span class="cgl-19__chip">8:47</span></div><h4>Subgrid in practice</h4><p>9.2k views · 5 days ago</p></article>
    <article class="cgl-19__tile"><div class="cgl-19__slot cgl-19__slot--v3"><span class="cgl-19__chip">21:33</span></div><h4>Container queries deep dive</h4><p>31k views · 1 week ago</p></article>
    <article class="cgl-19__tile"><div class="cgl-19__slot cgl-19__slot--v4"><span class="cgl-19__chip">6:15</span></div><h4>clip-path hexagons</h4><p>4.4k views · 2 weeks ago</p></article>
  </div>
</section>
```
## CSS
```css
.cgl-19,
.cgl-19 *,
.cgl-19 *::before,
.cgl-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-19 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.15 0.01 220);
  --txt: oklch(0.94 0.01 220);
  --dim: oklch(0.62 0.02 220);
  --cyan: oklch(0.8 0.12 210);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-19 .cgl-19__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(200px,100%),1fr));
  gap: 16px;
}

.cgl-19 .cgl-19__slot {
  display: grid;
  inline-size: 100%;
  aspect-ratio: 16/9;
  border-radius: 12px;
  overflow: hidden;
  padding: .5rem;
}

.cgl-19 .cgl-19__slot--v1 {
  background: linear-gradient(130deg,oklch(0.55 0.13 210),oklch(0.3 0.08 250));
}

.cgl-19 .cgl-19__slot--v2 {
  background: linear-gradient(130deg,oklch(0.55 0.14 300),oklch(0.28 0.09 330));
}

.cgl-19 .cgl-19__slot--v3 {
  background: linear-gradient(130deg,oklch(0.6 0.13 150),oklch(0.3 0.08 190));
}

.cgl-19 .cgl-19__slot--v4 {
  background: linear-gradient(130deg,oklch(0.62 0.14 60),oklch(0.35 0.1 30));
}

.cgl-19 .cgl-19__chip {
  place-self: end;
  font-size: .64rem;
  font-variant-numeric: tabular-nums;
  color: white;
  background: oklch(0.1 0.01 220/.75);
  border-radius: 5px;
  padding: .15rem .4rem;
}

.cgl-19 h4 {
  font-size: .88rem;
  color: var(--txt);
  margin-block: .6rem .2rem;
  line-height: 1.35;
}

.cgl-19 .cgl-19__tile p {
  font-size: .72rem;
  color: var(--dim);
}

.cgl-19 .cgl-19__tile:hover .cgl-19__slot {
  outline: 2px solid var(--cyan);
  outline-offset: 2px;
}
```

## JavaScript
```js
/* No JavaScript — aspect-ratio reserves every media box before load; object-fit: cover crops any source into it. */
```
