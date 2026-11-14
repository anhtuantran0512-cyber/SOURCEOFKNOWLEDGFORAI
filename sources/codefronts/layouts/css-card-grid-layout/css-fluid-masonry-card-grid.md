---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-fluid-masonry-card-grid/"
title: "CSS Fluid Masonry Card Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "A Pinterest-style photography wall where cards of naturally varied aspect ratios pack tightly into vertical columns using native multi-column flow, with no…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Fluid Masonry Card Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-fluid-masonry-card-grid/

A Pinterest-style photography wall where cards of naturally varied aspect ratios pack tightly into vertical columns using native multi-column flow, with no JS bin-packing required.
## HTML
```html
<div class="cg-04">
  <div class="cg-04__grid">
    <figure class="cg-04__card" style="--h:280px"><div class="cg-04__img" style="background:linear-gradient(160deg,#fbcfe8,#a855f7)"></div><figcaption class="cg-04__caption">Portrait Study</figcaption></figure>
    <figure class="cg-04__card" style="--h:180px"><div class="cg-04__img" style="background:linear-gradient(160deg,#bae6fd,#0284c7)"></div><figcaption class="cg-04__caption">Harbor Light</figcaption></figure>
    <figure class="cg-04__card" style="--h:340px"><div class="cg-04__img" style="background:linear-gradient(160deg,#fde68a,#d97706)"></div><figcaption class="cg-04__caption">Desert Bloom</figcaption></figure>
    <figure class="cg-04__card" style="--h:220px"><div class="cg-04__img" style="background:linear-gradient(160deg,#bbf7d0,#15803d)"></div><figcaption class="cg-04__caption">Quiet Forest</figcaption></figure>
    <figure class="cg-04__card" style="--h:300px"><div class="cg-04__img" style="background:linear-gradient(160deg,#fecaca,#b91c1c)"></div><figcaption class="cg-04__caption">Red Canyon</figcaption></figure>
    <figure class="cg-04__card" style="--h:200px"><div class="cg-04__img" style="background:linear-gradient(160deg,#ddd6fe,#6d28d9)"></div><figcaption class="cg-04__caption">Twilight Field</figcaption></figure>
  </div>
</div>
```
## CSS
```css
.cg-04,
.cg-04 *,
.cg-04 *::before,
.cg-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-04 ::selection {
  background: #a855f7;
  color: #fff;
}

.cg-04 {
  background: #111114;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  padding: 48px 24px;
}

.cg-04__grid {
  max-width: 900px;
  margin: 0 auto;
  column-count: 3;
  column-gap: 16px;
}

.cg-04__card {
  display: inline-block;
  width: 100%;
  margin-bottom: 16px;
  break-inside: avoid;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  background: #1a1a1f;
}

.cg-04__img {
  width: 100%;
  height: var(--h);
  transition: transform .4s ease;
}

.cg-04__card:hover .cg-04__img {
  transform: scale(1.05);
}

.cg-04__caption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 10px 12px;
  font-size: .78rem;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(0deg,rgba(0,0,0,.6),transparent);
  opacity: 0.85;
  transition: opacity .25s ease;
}

.cg-04__card:hover .cg-04__caption {
  opacity: 1;
}

@media (max-width: 640px) {
  .cg-04__grid {
    column-count: 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cg-04__img,
    .cg-04__caption {
    transition: none;
  }
}
```
