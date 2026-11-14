---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/subway-line/"
title: "Pure CSS Ribbon-Style Chevron Breadcrumb Trail"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A bold ribbon-banner breadcrumb: overlapping coloured segments with folded-ribbon notches at each join, built from rotated pseudo-elements and layered fills…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Ribbon-Style Chevron Breadcrumb Trail
Source: https://codefronts.com/navigation/css-breadcrumbs/subway-line/

A bold ribbon-banner breadcrumb: overlapping coloured segments with folded-ribbon notches at each join, built from rotated pseudo-elements and layered fills — the tactile, physical 'paper ribbon' look for playful product and marketing UIs, done entirely in CSS.
## HTML
```html
<nav class="bc-28" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Shop</a></li>
    <li><a href="#">Toys</a></li>
    <li><a href="#" aria-current="page">Building Blocks</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-28 {
  width: 100%;
  min-height: 100vh;
  --d: 18px;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.96 0.02 60);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bc-28 * {
  box-sizing: border-box;
}

.bc-28 ol {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-28 li {
  display: flex;
  position: relative;
}

.bc-28 li:nth-child(1) {
  z-index: 4;
}

.bc-28 li:nth-child(2) {
  z-index: 3;
}

.bc-28 li:nth-child(3) {
  z-index: 2;
}

.bc-28 li:nth-child(4) {
  z-index: 1;
}

.bc-28 a {
  display: flex;
  align-items: center;
  height: 42px;
  padding: 0 20px 0 30px;
  margin-inline-start: calc(var(--d) * -1);
  font: 700 13.5px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  background: oklch(0.68 0.17 40);
  clip-path: polygon(0 0,calc(100% - var(--d)) 0,100% 50%,calc(100% - var(--d)) 100%,0 100%,var(--d) 50%);
  box-shadow: inset 14px 0 14px -12px rgba(0,0,0,.35);
  transition: filter .18s ease;
}

.bc-28 li:nth-child(2) a {
  background: oklch(0.7 0.16 25);
}

.bc-28 li:nth-child(3) a {
  background: oklch(0.72 0.15 15);
}

.bc-28 li:first-child a {
  margin-inline-start: 0;
  padding-left: 22px;
  clip-path: polygon(0 0,calc(100% - var(--d)) 0,100% 50%,calc(100% - var(--d)) 100%,0 100%);
}

.bc-28 li:last-child a {
  padding-right: 24px;
  background: oklch(0.66 0.19 350);
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%,var(--d) 50%);
}

.bc-28 a:hover {
  filter: brightness(1.08);
}

.bc-28 a:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 2.5px #fff;
}

@media (prefers-reduced-motion: reduce) {
  .bc-28 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — overlapping clip-path chevron segments with an inset fold-shadow and ascending z-index read as a continuous folded ribbon. */
```
