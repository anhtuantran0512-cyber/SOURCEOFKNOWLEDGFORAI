---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/diagonal-slash/"
title: "Skewed Parallel Quadrilateral CSS Breadcrumb Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A sporty, angular breadcrumb of parallelogram segments: each crumb is skewed with transform:skewX(-20deg) and its text un-skewed back so labels stay upright…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skewed Parallel Quadrilateral CSS Breadcrumb Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/diagonal-slash/

A sporty, angular breadcrumb of parallelogram segments: each crumb is skewed with transform:skewX(-20deg) and its text un-skewed back so labels stay upright inside slanted blocks — the dynamic, motion-suggesting look common in gaming, sports and automotive UIs.
## HTML
```html
<nav class="bc-35" aria-label="Breadcrumb">
  <ol>
    <li><a href="#"><span>Home</span></a></li>
    <li><a href="#"><span>Garage</span></a></li>
    <li><a href="#"><span>Models</span></a></li>
    <li><a href="#" aria-current="page"><span>GT-R Spec</span></a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-35 {
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.16 0.015 250);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bc-35 * {
  box-sizing: border-box;
}

.bc-35 ol {
  display: flex;
  gap: 5px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-35 a {
  display: block;
  padding: 0;
  transform: skewX(-20deg);
  background: oklch(0.4 0.03 250);
  overflow: hidden;
  transition: background-color .18s ease;
}

.bc-35 a span {
  display: flex;
  align-items: center;
  height: 40px;
  padding: 0 22px;
  transform: skewX(20deg);
  font: 700 13px/1 system-ui,sans-serif;
  letter-spacing: .03em;
  color: oklch(0.9 0.01 250);
  text-transform: uppercase;
}

.bc-35 li:nth-child(2) a {
  background: oklch(0.44 0.04 250);
}

.bc-35 li:nth-child(3) a {
  background: oklch(0.48 0.05 250);
}

.bc-35 a:hover {
  background: oklch(0.55 0.08 250);
}

.bc-35 li:last-child a {
  background: oklch(0.62 0.19 25);
}

.bc-35 li:last-child a:hover {
  background: oklch(0.66 0.2 25);
}

.bc-35 a:focus-visible {
  outline: none;
}

.bc-35 a:focus-visible span {
  outline: 2px solid #fff;
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .bc-35 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each block is skewX(-20deg) into a parallelogram; the inner span is skewX(20deg) to keep the label upright. Focus ring rides the un-skewed span. */
```
