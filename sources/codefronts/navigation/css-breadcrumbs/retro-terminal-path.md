---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/retro-terminal-path/"
title: "Minimalist CSS Breadcrumb with Custom SVG Separators"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The cleanest possible breadcrumb: text links divided by CSS-generated separators you can switch between a slash, a dot, or a themed SVG chevron in one line —…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist CSS Breadcrumb with Custom SVG Separators
Source: https://codefronts.com/navigation/css-breadcrumbs/retro-terminal-path/

The cleanest possible breadcrumb: text links divided by CSS-generated separators you can switch between a slash, a dot, or a themed SVG chevron in one line — with the SVG recoloured automatically via mask-image so separators always match your text colour. A --sep custom property makes the divider a one-token swap.
## HTML
```html
<nav class="bc-26" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Blog</a></li>
    <li><a href="#">CSS</a></li>
    <li><a href="#" aria-current="page">Minimal Separators</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-26 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --sep-svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 6l6 6-6 6' fill='none' stroke='black' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  --accent: oklch(0.55 0.16 255);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.99 0.003 250);
  place-items: center;
}

.bc-26 * {
  box-sizing: border-box;
}

.bc-26 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-26 li {
  display: flex;
  align-items: center;
  color: oklch(0.55 0.01 250);
}

.bc-26 li:not(:last-child)::after {
  content: "";
  width: 14px;
  height: 14px;
  margin: 0 10px;
  background: currentColor;
  -webkit-mask: var(--sep-svg) center/contain no-repeat;
  mask: var(--sep-svg) center/contain no-repeat;
  opacity: .5;
}

.bc-26 a {
  font: 500 14px/1 system-ui,sans-serif;
  letter-spacing: .01em;
  color: oklch(0.5 0.02 250);
  text-decoration: none;
  padding: 3px 4px;
  border-radius: 6px;
  transition: color .15s ease;
}

.bc-26 a:hover {
  color: var(--accent);
}

.bc-26 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-26 li[aria-current="page"] {
  color: oklch(0.3 0.01 250);
}

.bc-26 li[aria-current="page"] a {
  color: oklch(0.3 0.01 250);
  font-weight: 600;
}
```

## JavaScript
```js
/* No JavaScript — decorative separators are a mask-image pseudo-element painted with currentColor, so the SVG chevron matches text colour automatically; swap --sep-svg for slash/dot. */
```
