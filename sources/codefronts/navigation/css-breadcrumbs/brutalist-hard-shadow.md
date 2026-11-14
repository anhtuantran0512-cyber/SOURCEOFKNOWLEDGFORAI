---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/brutalist-hard-shadow/"
title: "Outline Border-Only Geometric CSS Breadcrumbs"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A wireframe breadcrumb with no solid fills: each crumb is an outlined chevron shape drawn with borders and a clip-path cutout, so the trail reads as clean…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Outline Border-Only Geometric CSS Breadcrumbs
Source: https://codefronts.com/navigation/css-breadcrumbs/brutalist-hard-shadow/

A wireframe breadcrumb with no solid fills: each crumb is an outlined chevron shape drawn with borders and a clip-path cutout, so the trail reads as clean line-art. Hover fills the outline; the current crumb inverts to a solid. The technical, blueprint aesthetic for developer tools and design systems.
## HTML
```html
<nav class="bc-36" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">System</a></li>
    <li><a href="#">Modules</a></li>
    <li><a href="#" aria-current="page">Renderer</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-36 {
  width: 100%;
  min-height: 100vh;
  --d: 15px;
  --accent: oklch(0.55 0.16 200);
  font-family: 'SF Mono',ui-monospace,'Cascadia Code',monospace;
  padding: 30px;
  background: oklch(0.98 0.005 200);
  display: flex;
  align-items: center;
  justify-content: center;
}

.bc-36 * {
  box-sizing: border-box;
}

.bc-36 ol {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-36 a {
  display: flex;
  align-items: center;
  height: 38px;
  padding: 0 16px 0 24px;
  margin-inline-start: calc(var(--d) * -1);
  font: 600 12px/1 ui-monospace,monospace;
  letter-spacing: .02em;
  color: var(--accent);
  text-decoration: none;
  background: transparent;
  box-shadow: inset 0 0 0 1.5px var(--accent);
  clip-path: polygon(0 0,calc(100% - var(--d)) 0,100% 50%,calc(100% - var(--d)) 100%,0 100%,var(--d) 50%);
  transition: background-color .18s ease,color .18s ease;
}

.bc-36 li:first-child a {
  margin-inline-start: 0;
  padding-left: 18px;
  clip-path: polygon(0 0,calc(100% - var(--d)) 0,100% 50%,calc(100% - var(--d)) 100%,0 100%);
}

.bc-36 li:last-child a {
  padding-right: 20px;
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%,var(--d) 50%);
}

.bc-36 a:hover {
  background: color-mix(in oklab,var(--accent) 12%,transparent);
  color: oklch(0.4 0.16 205);
}

.bc-36 a:focus-visible {
  outline: none;
  box-shadow: inset 0 0 0 1.5px var(--accent),inset 0 0 0 4px color-mix(in oklab,var(--accent) 30%,transparent);
}

.bc-36 li[aria-current="page"] a {
  background: var(--accent);
  color: #fff;
  box-shadow: none;
}

@media (prefers-reduced-motion: reduce) {
  .bc-36 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — outlined chevrons drawn with inset box-shadow (so clip-path keeps the border crisp); hover fills the outline, the current page inverts to a solid. */
```
