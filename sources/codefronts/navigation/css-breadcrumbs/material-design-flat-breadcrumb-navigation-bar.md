---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/material-design-flat-breadcrumb-navigation-bar/"
title: "Material Design Flat Breadcrumb Navigation Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A clean Material-Design breadcrumb: flat surface, Roboto-style type scale, and an ink-ripple hover cue that radiates from the pointer on each link — the…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Flat Breadcrumb Navigation Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/material-design-flat-breadcrumb-navigation-bar/

A clean Material-Design breadcrumb: flat surface, Roboto-style type scale, and an ink-ripple hover cue that radiates from the pointer on each link — the tactile Material feedback recreated with a pure-CSS radial-gradient ripple, no JS ripple library.
## HTML
```html
<nav class="bc-08" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Materials</a></li>
    <li><a href="#">Components</a></li>
    <li><a href="#" aria-current="page">Navigation</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-08 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --primary: oklch(0.5 0.15 265);
  --on: oklch(0.35 0.01 265);
  --mut: oklch(0.6 0.01 265);
  font-family: 'Roboto',system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.97 0.004 265);
  place-items: center;
}

.bc-08 * {
  box-sizing: border-box;
}

.bc-08 ol {
  display: inline-flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 6px 8px;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 1px 2px rgba(0,0,0,.12),0 1px 3px rgba(0,0,0,.08);
}

.bc-08 li {
  display: flex;
  align-items: center;
}

.bc-08 li + li::before {
  content: "";
  width: 18px;
  height: 18px;
  margin: 0 2px;
  background: var(--mut);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 6l6 6-6 6' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M9 6l6 6-6 6' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;
}

.bc-08 a {
  position: relative;
  overflow: hidden;
  display: inline-block;
  padding: 9px 14px;
  border-radius: 8px;
  font: 500 14px/1 'Roboto',system-ui,sans-serif;
  color: var(--primary);
  text-decoration: none;
  transition: background-color .18s ease;
}

.bc-08 a::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 160%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle,color-mix(in oklab,var(--primary) 40%,transparent),transparent 60%);
  translate: -50% -50%;
  scale: 0;
  opacity: 0;
  pointer-events: none;
  transition: scale .4s ease,opacity .5s ease;
}

.bc-08 a:hover {
  background: color-mix(in oklab,var(--primary) 8%,transparent);
}

.bc-08 a:active::after {
  scale: 1;
  opacity: 1;
  transition: scale 0s,opacity 0s;
}

.bc-08 a:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

.bc-08 li[aria-current="page"] a {
  color: var(--on);
  font-weight: 500;
  cursor: default;
}

@media (prefers-reduced-motion: reduce) {
  .bc-08 a,
    .bc-08 a::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radial-gradient ::after scales up on :active for the Material ink ripple; hover paints a color-mix() state layer. Add --x/--y from pointerdown for a pointer-origin ripple. */
```
