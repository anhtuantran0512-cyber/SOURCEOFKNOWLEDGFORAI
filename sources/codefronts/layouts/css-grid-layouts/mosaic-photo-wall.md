---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/mosaic-photo-wall/"
title: "Mosaic Photo Wall"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A hand-set photo mosaic — not a uniform grid, not random masonry, but a designed arrangement: a repeating 6-column composition where spans are chosen so…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mosaic Photo Wall
Source: https://codefronts.com/layouts/css-grid-layouts/mosaic-photo-wall/

A hand-set photo mosaic — not a uniform grid, not random masonry, but a designed arrangement: a repeating 6-column composition where spans are chosen so tiles interlock without holes. The organic, editorial look of a curated print wall, with the repeat unit documented so you can extend it infinitely.
## HTML
```html
<section class="cgl-23" aria-label="Mosaic photo wall demo">
  <div class="cgl-23__wall">
    <figure class="cgl-23__t" style="--s:3;--r:2;--g:linear-gradient(140deg,oklch(0.62 0.11 140),oklch(0.35 0.07 160))" tabindex="0"><figcaption>Fern gully</figcaption></figure>
    <figure class="cgl-23__t" style="--s:2;--r:2;--g:linear-gradient(140deg,oklch(0.7 0.1 90),oklch(0.45 0.08 70))" tabindex="0"><figcaption>Lichen study</figcaption></figure>
    <figure class="cgl-23__t" style="--s:1;--r:1;--g:linear-gradient(140deg,oklch(0.55 0.09 180),oklch(0.35 0.06 200))" tabindex="0"><figcaption>Creek stone</figcaption></figure>
    <figure class="cgl-23__t" style="--s:1;--r:1;--g:linear-gradient(140deg,oklch(0.5 0.1 120),oklch(0.3 0.06 140))" tabindex="0"><figcaption>Moss detail</figcaption></figure>
    <figure class="cgl-23__t" style="--s:2;--r:3;--g:linear-gradient(180deg,oklch(0.65 0.1 110),oklch(0.3 0.07 150))" tabindex="0"><figcaption>Old-growth trunk, portrait</figcaption></figure>
    <figure class="cgl-23__t" style="--s:2;--r:1;--g:linear-gradient(140deg,oklch(0.72 0.09 80),oklch(0.5 0.08 60))" tabindex="0"><figcaption>Dry grass</figcaption></figure>
    <figure class="cgl-23__t" style="--s:2;--r:2;--g:linear-gradient(140deg,oklch(0.45 0.08 200),oklch(0.28 0.05 230))" tabindex="0"><figcaption>River bend</figcaption></figure>
    <figure class="cgl-23__t" style="--s:2;--r:1;--g:linear-gradient(140deg,oklch(0.58 0.1 130),oklch(0.4 0.07 110))" tabindex="0"><figcaption>Canopy light</figcaption></figure>
    <figure class="cgl-23__t" style="--s:3;--r:1;--g:linear-gradient(90deg,oklch(0.6 0.09 150),oklch(0.38 0.06 170))" tabindex="0"><figcaption>Ridge line, panorama</figcaption></figure>
    <figure class="cgl-23__t" style="--s:1;--r:1;--g:linear-gradient(140deg,oklch(0.68 0.11 100),oklch(0.44 0.08 90))" tabindex="0"><figcaption>Seed pod</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.cgl-23,
.cgl-23 *,
.cgl-23 *::before,
.cgl-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-23 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.2 0.02 140);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-23 .cgl-23__wall {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  grid-auto-rows: minmax(64px,auto);
  gap: 10px;
}

.cgl-23 .cgl-23__t {
  grid-column: span var(--s,1);
  grid-row: span var(--r,1);
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  background: var(--g);
  cursor: pointer;
}

.cgl-23 .cgl-23__t::after {
  content: "";
  position: absolute;
  inset: 0;
  background: oklch(0.15 0.02 140/.0);
  transition: background .3s ease;
}

.cgl-23 .cgl-23__t:hover::after,
.cgl-23 .cgl-23__t:focus-visible::after {
  background: oklch(0.15 0.02 140/.35);
}

.cgl-23 figcaption {
  position: absolute;
  inset: auto 0 0 0;
  z-index: 1;
  padding: 1.4rem .7rem .55rem;
  font-size: .7rem;
  color: oklch(0.97 0.01 120);
  background: linear-gradient(180deg,transparent,oklch(0.12 0.02 140/.8));
  opacity: 0;
  transition: opacity .3s ease;
}

.cgl-23 .cgl-23__t:hover figcaption,
.cgl-23 .cgl-23__t:focus-visible figcaption {
  opacity: 1;
}

.cgl-23 .cgl-23__t:focus-visible {
  outline: 2px solid oklch(0.85 0.12 120);
  outline-offset: 2px;
}

@media (max-width: 520px) {
  .cgl-23 .cgl-23__wall {
    grid-template-columns: repeat(3,1fr);
  }

  .cgl-23 .cgl-23__t {
    --s: min(var(--s-m,var(--s)),3);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgl-23 .cgl-23__t::after,
    .cgl-23 figcaption {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a designed span sequence (rows summing to 6 columns) interlocks the mosaic in source order. */
```
