---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/full-width-block-style-segmented-css-breadcrumb-bar/"
title: "Full-Width Block-Style Segmented CSS Breadcrumb Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "An edge-to-edge breadcrumb where each hierarchy step is a distinct full-height coloured block, the segments filling the entire bar width with equal or…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Width Block-Style Segmented CSS Breadcrumb Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/full-width-block-style-segmented-css-breadcrumb-bar/

An edge-to-edge breadcrumb where each hierarchy step is a distinct full-height coloured block, the segments filling the entire bar width with equal or content-sized tracks — the bold, blocky navigation banner for app headers and section dividers. Segments meet flush with a subtle bevel between them.
## HTML
```html
<nav class="bc-11" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Region</a></li>
    <li><a href="#">Country</a></li>
    <li><a href="#" aria-current="page">City Guide</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-11 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.96 0.005 250);
  place-items: center;
}

.bc-11 * {
  box-sizing: border-box;
}

.bc-11 ol {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  width: 100%;
}

.bc-11 li {
  display: flex;
}

.bc-11 li:last-child {
  flex: 1;
}

.bc-11 a {
  display: flex;
  align-items: center;
  width: 100%;
  height: 52px;
  padding: 0 22px;
  font: 700 13px/1 system-ui,sans-serif;
  letter-spacing: .02em;
  text-transform: uppercase;
  color: #fff;
  text-decoration: none;
  box-shadow: inset -1px 0 0 rgba(255,255,255,.18),inset 1px 0 0 rgba(0,0,0,.12);
  transition: filter .18s ease;
}

.bc-11 li:nth-child(1) a {
  background: oklch(0.42 0.05 250);
}

.bc-11 li:nth-child(2) a {
  background: oklch(0.47 0.07 250);
}

.bc-11 li:nth-child(3) a {
  background: oklch(0.52 0.09 250);
}

.bc-11 li:last-child a {
  background: oklch(0.6 0.17 255);
}

.bc-11 a:hover {
  filter: brightness(1.1);
}

.bc-11 a:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 3px #fff;
}

@media (max-width: 560px) {
  .bc-11 ol {
    flex-direction: column;
  }

  .bc-11 li,
    .bc-11 li:last-child {
    flex: none;
  }

  .bc-11 a {
    box-shadow: inset 0 -1px 0 rgba(0,0,0,.15);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-11 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — full-width flex segments with inset-shadow bevels between blocks; a tonal palette ramp encodes depth, the current block right-fills and takes the accent. */
```
