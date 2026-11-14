---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/pill-breadcrumbs/"
title: "Pill-Shape Badge CSS Breadcrumb Bar UI"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Each crumb is a rounded capsule with a soft tinted background and comfortable gap spacing — the friendly 'pill' breadcrumb common in modern dashboards and…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pill-Shape Badge CSS Breadcrumb Bar UI
Source: https://codefronts.com/navigation/css-breadcrumbs/pill-breadcrumbs/

Each crumb is a rounded capsule with a soft tinted background and comfortable gap spacing — the friendly 'pill' breadcrumb common in modern dashboards and mobile apps. Full 9999px radius, subtle hover fill lift, and an accent-filled current pill, laid out with flex + gap so it wraps cleanly.
## HTML
```html
<nav class="bc-29" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Team</a></li>
    <li><a href="#">Design</a></li>
    <li><a href="#" aria-current="page">Tokens</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-29 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.58 0.16 285);
  --surface: oklch(0.98 0.004 285);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: var(--surface);
  place-items: center;
}

.bc-29 * {
  box-sizing: border-box;
}

.bc-29 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-29 li {
  display: flex;
  align-items: center;
  gap: 8px;
}

.bc-29 li:not(:last-child)::after {
  content: "›";
  color: oklch(0.7 0.02 285);
  font-size: 14px;
}

.bc-29 a {
  display: inline-block;
  padding: 8px 15px;
  border-radius: 9999px;
  font: 600 13px/1 system-ui,sans-serif;
  color: oklch(0.42 0.08 285);
  text-decoration: none;
  background: color-mix(in oklab,var(--accent) 10%,var(--surface));
  transition: background-color .18s ease,color .18s ease;
}

.bc-29 a:hover {
  background: color-mix(in oklab,var(--accent) 20%,var(--surface));
  color: oklch(0.32 0.12 285);
}

.bc-29 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-29 li[aria-current="page"] a {
  background: var(--accent);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .bc-29 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each crumb is a 9999px pill tinted with color-mix(); flex + gap keeps even spacing and clean wrapping, the current page is a solid accent pill. */
```
