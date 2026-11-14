---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/vertical-stacked/"
title: "Multi-Line Aligned CSS Grid Subgrid Breadcrumb Layout"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb where icon, label and separator stay in perfect vertical alignment even when the trail wraps across multiple lines — solved with CSS subgrid."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Line Aligned CSS Grid Subgrid Breadcrumb Layout
Source: https://codefronts.com/navigation/css-breadcrumbs/vertical-stacked/

A breadcrumb where icon, label and separator stay in perfect vertical alignment even when the trail wraps across multiple lines — solved with CSS subgrid. Each crumb inherits the parent grid's column tracks, so every icon column and every separator lines up down the whole wrapped trail like a table, without a table.
## HTML
```html
<nav class="bc-24" aria-label="Breadcrumb">
  <ol>
    <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><a href="#">Home</a><span class="bc-24__sep" aria-hidden="true">›</span></li>
    <li><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/></svg><a href="#">Documentation</a><span class="bc-24__sep" aria-hidden="true">›</span></li>
    <li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h10"/></svg><a href="#">CSS Layout Techniques</a><span class="bc-24__sep" aria-hidden="true">›</span></li>
    <li><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/></svg><a href="#" aria-current="page">Subgrid Alignment Guide</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-24 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: oklch(0.97 0.006 200);
  place-items: center;
}

.bc-24 * {
  box-sizing: border-box;
}

.bc-24 ol {
  display: grid;
  grid-template-columns: repeat(3,auto);
  justify-content: start;
  align-items: center;
  column-gap: 9px;
  row-gap: 10px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-24 li {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 3;
  align-items: center;
  gap: 9px;
}

.bc-24 svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  color: oklch(0.55 0.06 200);
}

.bc-24 a {
  font: 600 14px/1 system-ui,sans-serif;
  color: oklch(0.45 0.08 210);
  text-decoration: none;
  padding: 3px 4px;
  border-radius: 6px;
  transition: color .15s ease;
}

.bc-24 a:hover {
  color: oklch(0.38 0.13 215);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.bc-24 a:focus-visible {
  outline: 2px solid oklch(0.5 0.15 215);
  outline-offset: 2px;
}

.bc-24__sep {
  color: oklch(0.72 0.03 200);
  font-size: 15px;
  justify-self: center;
}

.bc-24 li[aria-current="page"] {
  grid-column: span 2;
}

.bc-24 li[aria-current="page"] a {
  color: oklch(0.3 0.02 210);
  font-weight: 700;
}
```

## JavaScript
```js
/* No JavaScript — each <li> is grid-template-columns:subgrid spanning the parent's [icon][label][sep] tracks, so every column stays aligned even when the trail wraps. */
```
