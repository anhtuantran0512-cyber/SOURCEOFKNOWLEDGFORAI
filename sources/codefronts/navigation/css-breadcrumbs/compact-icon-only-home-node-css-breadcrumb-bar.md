---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/compact-icon-only-home-node-css-breadcrumb-bar/"
title: "Compact Icon-Only Home Node CSS Breadcrumb Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A space-saving breadcrumb that replaces the word 'Home' with an accessible house icon while keeping the full text for screen readers — the compact convention…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compact Icon-Only Home Node CSS Breadcrumb Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/compact-icon-only-home-node-css-breadcrumb-bar/

A space-saving breadcrumb that replaces the word 'Home' with an accessible house icon while keeping the full text for screen readers — the compact convention seen across modern apps. Demonstrates the correct visually-hidden pattern so the icon-only node never loses its accessible name.
## HTML
```html
<nav class="bc-14" aria-label="Breadcrumb">
  <ol>
    <li><a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span class="bc-14__sr">Home</span></a></li>
    <li><a href="#">Help Center</a></li>
    <li><a href="#">Billing</a></li>
    <li><a href="#" aria-current="page">Refunds</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-14 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.14 235);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.98 0.004 235);
  place-items: center;
}

.bc-14 * {
  box-sizing: border-box;
}

.bc-14 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-14 li {
  display: flex;
  align-items: center;
}

.bc-14 li + li::before {
  content: "›";
  margin: 0 8px;
  color: oklch(0.72 0.02 235);
}

.bc-14 a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  min-height: 40px;
  padding: 6px 10px;
  border-radius: 9px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.46 0.05 235);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.bc-14 a:hover {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
}

.bc-14 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-14 svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.bc-14 li[aria-current="page"] a {
  color: oklch(0.3 0.02 235);
  font-weight: 700;
}

.bc-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

@media (prefers-reduced-motion: reduce) {
  .bc-14 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the home node is an SVG plus a visually-hidden .sr-only "Home" label (clip-path:inset(50%)), so screen readers keep the name while sighted users see only the icon. */
```
