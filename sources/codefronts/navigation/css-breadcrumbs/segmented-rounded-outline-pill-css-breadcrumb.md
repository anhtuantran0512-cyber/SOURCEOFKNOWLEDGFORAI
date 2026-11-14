---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/segmented-rounded-outline-pill-css-breadcrumb/"
title: "Segmented Rounded-Outline Pill CSS Breadcrumb"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A refined outline-only pill breadcrumb: each crumb is framed in a thin rounded border with no fill, so the trail reads as a row of elegant capsule outlines."
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Segmented Rounded-Outline Pill CSS Breadcrumb
Source: https://codefronts.com/navigation/css-breadcrumbs/segmented-rounded-outline-pill-css-breadcrumb/

A refined outline-only pill breadcrumb: each crumb is framed in a thin rounded border with no fill, so the trail reads as a row of elegant capsule outlines. Hover fills the pill softly; the current crumb becomes a solid accent capsule. The understated, high-craft treatment for premium product UIs.
## HTML
```html
<nav class="bc-15" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Workspace</a></li>
    <li><a href="#">Boards</a></li>
    <li><a href="#" aria-current="page">Roadmap</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-15 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.15 250);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.99 0.003 250);
  place-items: center;
}

.bc-15 * {
  box-sizing: border-box;
}

.bc-15 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 9px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-15 li {
  display: flex;
  align-items: center;
  gap: 9px;
}

.bc-15 li:not(:last-child)::after {
  content: "›";
  color: oklch(0.75 0.02 250);
  font-size: 13px;
}

.bc-15 a {
  display: inline-block;
  padding: 7px 15px;
  border-radius: 9999px;
  font: 600 13px/1 system-ui,sans-serif;
  color: oklch(0.48 0.03 250);
  text-decoration: none;
  border: 1.5px solid oklch(0.86 0.01 250);
  background: transparent;
  transition: background-color .18s ease,border-color .18s ease,color .18s ease;
}

.bc-15 a:hover {
  color: var(--accent);
  border-color: color-mix(in oklab,var(--accent) 50%,oklch(0.86 0.01 250));
  background: color-mix(in oklab,var(--accent) 8%,transparent);
}

.bc-15 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-15 li[aria-current="page"] a {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .bc-15 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — border-only rounded pills at rest; hover washes a faint color-mix() tint and the current page becomes a solid accent capsule. */
```
