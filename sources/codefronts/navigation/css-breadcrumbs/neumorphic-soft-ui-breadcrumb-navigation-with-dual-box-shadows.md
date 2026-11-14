---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/neumorphic-soft-ui-breadcrumb-navigation-with-dual-box-shadows/"
title: "Neumorphic Soft UI Breadcrumb Navigation with Dual Box Shadows"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The soft-UI / neumorphism treatment: breadcrumb nodes appear extruded from a single-colour surface using two opposing box-shadows (a light source and a dark…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft UI Breadcrumb Navigation with Dual Box Shadows
Source: https://codefronts.com/navigation/css-breadcrumbs/neumorphic-soft-ui-breadcrumb-navigation-with-dual-box-shadows/

The soft-UI / neumorphism treatment: breadcrumb nodes appear extruded from a single-colour surface using two opposing box-shadows (a light source and a dark source), and the current crumb presses INWARD with inset shadows. The whole effect is one background colour plus shadow pairs — the defining neumorphic recipe.
## HTML
```html
<nav class="bc-06" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Apps</a></li>
    <li><a href="#">Finance</a></li>
    <li><a href="#" aria-current="page">Wallet</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-06 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --surface: oklch(0.9 0.01 255);
  --dark: oklch(0.78 0.02 255);
  --light: oklch(0.99 0.005 255);
  --accent: oklch(0.5 0.16 265);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 40px 30px;
  background: var(--surface);
  place-items: center;
}

.bc-06 * {
  box-sizing: border-box;
}

.bc-06 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-06 li {
  display: flex;
  align-items: center;
}

.bc-06 li + li::before {
  content: "";
  width: 6px;
  height: 6px;
  margin-right: 16px;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: inset 1px 1px 2px var(--dark),inset -1px -1px 2px var(--light);
}

.bc-06 a {
  display: inline-block;
  padding: 9px 16px;
  border-radius: 14px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: var(--accent);
  text-decoration: none;
  background: var(--surface);
  box-shadow: 5px 5px 10px var(--dark),-5px -5px 10px var(--light);
  transition: box-shadow .2s ease,color .2s ease;
}

.bc-06 a:hover {
  box-shadow: 7px 7px 14px var(--dark),-7px -7px 14px var(--light);
}

.bc-06 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.bc-06 li[aria-current="page"] a {
  color: oklch(0.4 0.03 255);
  box-shadow: inset 3px 3px 6px var(--dark),inset -3px -3px 6px var(--light);
}

@media (prefers-reduced-motion: reduce) {
  .bc-06 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dual mirrored box-shadows extrude each crumb from a same-colour surface; the current page uses inset shadows to press inward. */
```
