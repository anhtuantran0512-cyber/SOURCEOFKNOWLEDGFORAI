---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/responsive-media-gallery/"
title: "Responsive Media Gallery"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "An auto-fill photo gallery that handles mixed aspect ratios without a single media query: portrait, landscape and square media all snap to a consistent…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Media Gallery
Source: https://codefronts.com/layouts/css-grid-layouts/responsive-media-gallery/

An auto-fill photo gallery that handles mixed aspect ratios without a single media query: portrait, landscape and square media all snap to a consistent rhythm because aspect-ratio + object-fit normalise every cell. Captions ride as gradient overlays inside real <figure> elements — the markup search engines and screen readers want.
## HTML
```html
<section class="cgl-03" aria-label="Responsive media gallery demo">
  <div class="cgl-03__wall">
    <figure class="cgl-03__cell cgl-03__cell--wide" tabindex="0"><div class="cgl-03__img cgl-03__img--1" role="img" aria-label="Dune ridges at dusk"></div><figcaption>Dune ridges, 21:9 crop</figcaption></figure>
    <figure class="cgl-03__cell" tabindex="0"><div class="cgl-03__img cgl-03__img--2" role="img" aria-label="Tide pool"></div><figcaption>Tide pool</figcaption></figure>
    <figure class="cgl-03__cell cgl-03__cell--tall" tabindex="0"><div class="cgl-03__img cgl-03__img--3" role="img" aria-label="Canyon slot, portrait"></div><figcaption>Canyon slot, portrait</figcaption></figure>
    <figure class="cgl-03__cell" tabindex="0"><div class="cgl-03__img cgl-03__img--4" role="img" aria-label="Salt flat"></div><figcaption>Salt flat</figcaption></figure>
    <figure class="cgl-03__cell" tabindex="0"><div class="cgl-03__img cgl-03__img--5" role="img" aria-label="Ember sky"></div><figcaption>Ember sky</figcaption></figure>
    <figure class="cgl-03__cell" tabindex="0"><div class="cgl-03__img cgl-03__img--6" role="img" aria-label="Basalt coast"></div><figcaption>Basalt coast</figcaption></figure>
    <figure class="cgl-03__cell cgl-03__cell--wide" tabindex="0"><div class="cgl-03__img cgl-03__img--7" role="img" aria-label="Storm shelf, panorama"></div><figcaption>Storm shelf, panorama</figcaption></figure>
    <figure class="cgl-03__cell" tabindex="0"><div class="cgl-03__img cgl-03__img--8" role="img" aria-label="Alpine meadow"></div><figcaption>Alpine meadow</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.cgl-03,
.cgl-03 *,
.cgl-03 *::before,
.cgl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-03 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.16 0.02 300);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.2rem;
}

.cgl-03 .cgl-03__wall {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(min(160px,100%),1fr));
  grid-auto-rows: auto;
  grid-auto-flow: dense;
  gap: 10px;
}

.cgl-03 .cgl-03__cell {
  position: relative;
  overflow: hidden;
  border-radius: 12px;
  aspect-ratio: 1;
}

.cgl-03 .cgl-03__cell--wide {
  grid-column: span 2;
  aspect-ratio: 2.05/1;
}

.cgl-03 .cgl-03__cell--tall {
  grid-row: span 2;
  aspect-ratio: auto;
}

.cgl-03 .cgl-03__img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  transition: scale .5s ease;
}

.cgl-03 .cgl-03__cell:hover .cgl-03__img,
.cgl-03 .cgl-03__cell:focus-within .cgl-03__img,
.cgl-03 .cgl-03__cell:focus .cgl-03__img {
  scale: 1.06;
}

.cgl-03 .cgl-03__img--1 {
  background: linear-gradient(120deg,oklch(0.7 0.15 55),oklch(0.45 0.12 25));
}

.cgl-03 .cgl-03__img--2 {
  background: radial-gradient(circle at 30% 30%,oklch(0.75 0.12 200),oklch(0.4 0.1 250));
}

.cgl-03 .cgl-03__img--3 {
  background: linear-gradient(180deg,oklch(0.65 0.16 40),oklch(0.3 0.08 20));
}

.cgl-03 .cgl-03__img--4 {
  background: linear-gradient(150deg,oklch(0.9 0.05 90),oklch(0.6 0.08 60));
}

.cgl-03 .cgl-03__img--5 {
  background: radial-gradient(circle at 70% 20%,oklch(0.72 0.18 30),oklch(0.35 0.1 310));
}

.cgl-03 .cgl-03__img--6 {
  background: linear-gradient(200deg,oklch(0.55 0.06 240),oklch(0.25 0.04 260));
}

.cgl-03 .cgl-03__img--7 {
  background: linear-gradient(90deg,oklch(0.4 0.08 270),oklch(0.6 0.1 320),oklch(0.35 0.07 250));
}

.cgl-03 .cgl-03__img--8 {
  background: linear-gradient(160deg,oklch(0.78 0.14 130),oklch(0.45 0.1 160));
}

.cgl-03 figcaption {
  position: absolute;
  inset: auto 0 0 0;
  padding: 1.6rem .8rem .6rem;
  font-size: .75rem;
  color: oklch(0.97 0.01 90);
  background: linear-gradient(180deg,transparent,oklch(0.1 0.02 300/.85));
  opacity: 0;
  translate: 0 6px;
  transition: opacity .3s ease,translate .3s ease;
}

.cgl-03 .cgl-03__cell:hover figcaption,
.cgl-03 .cgl-03__cell:focus-within figcaption,
.cgl-03 .cgl-03__cell:focus figcaption {
  opacity: 1;
  translate: 0 0;
}

.cgl-03 .cgl-03__cell:focus-visible {
  outline: 2px solid oklch(0.8 0.15 55);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cgl-03 .cgl-03__img,
    .cgl-03 figcaption {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — auto-fill + minmax(min(160px,100%),1fr) sizes the wall; aspect-ratio + object-fit normalise mixed media. */
```
