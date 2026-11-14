---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/css-grid-auto-fitting-responsive-breadcrumb-trail/"
title: "CSS Grid Auto-Fitting Responsive Breadcrumb Trail"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb laid out on a CSS grid with repeat(auto-fit, minmax()) so crumbs reflow into as many columns as fit and wrap into neat aligned rows on narrow…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Auto-Fitting Responsive Breadcrumb Trail
Source: https://codefronts.com/navigation/css-breadcrumbs/css-grid-auto-fitting-responsive-breadcrumb-trail/

A breadcrumb laid out on a CSS grid with repeat(auto-fit, minmax()) so crumbs reflow into as many columns as fit and wrap into neat aligned rows on narrow screens — no media queries. The trail self-balances across any width, keeping crumbs evenly sized and gutters consistent as it wraps.
## HTML
```html
<nav class="bc-17" aria-label="Breadcrumb">
  <ol class="bc-17__list">
    <li class="bc-17__item"><a class="bc-17__link" href="#">Home</a></li>
    <li class="bc-17__item"><a class="bc-17__link" href="#">Continents</a></li>
    <li class="bc-17__item"><a class="bc-17__link" href="#">Europe</a></li>
    <li class="bc-17__item"><a class="bc-17__link" href="#">Countries</a></li>
    <li class="bc-17__item"><a class="bc-17__link" href="#">Portugal</a></li>
    <li class="bc-17__item"><a class="bc-17__link" aria-current="page" href="#">Lisbon</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-17 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.55 0.15 200);
  --muted: oklch(0.68 0.04 205);
  --ink: oklch(0.28 0.03 210);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 28px;
  background: linear-gradient(180deg,oklch(0.99 0.003 200),oklch(0.96 0.008 205));
  place-items: center;
}

.bc-17 * {
  box-sizing: border-box;
}

.bc-17__list {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(max-content,auto));
  grid-auto-flow: column;
  justify-content: center;
  align-items: center;
  column-gap: 6px;
  row-gap: 8px;
  list-style: none;
  margin: 0;
  padding: 0;
  max-width: 100%;
}

@supports (grid-template-columns: subgrid) {
  .bc-17__list {
    grid-template-columns: repeat(auto-fit,minmax(max-content,auto));
  }
}

.bc-17__item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  min-width: 0;
}

.bc-17__item + .bc-17__item::before {
  content: "›";
  color: var(--muted);
  font-size: 14px;
  font-weight: 600;
  flex-shrink: 0;
}

.bc-17__link {
  display: inline-flex;
  align-items: center;
  height: 36px;
  padding: 0 12px;
  border-radius: 8px;
  font: 600 13px/1 system-ui,sans-serif;
  color: var(--ink);
  text-decoration: none;
  background: #fff;
  border: 1px solid oklch(0.92 0.008 205);
  transition: background-color .18s ease,color .18s ease,border-color .18s ease,transform .18s ease;
}

.bc-17__link:hover {
  color: var(--accent);
  border-color: color-mix(in oklab,var(--accent) 40%,oklch(0.92 0.008 205));
  background: color-mix(in oklab,var(--accent) 6%,#fff);
  transform: translateY(-1px);
}

.bc-17__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.bc-17__item[aria-current="page"] .bc-17__link,
.bc-17__link[aria-current="page"] {
  color: #fff;
  background: var(--accent);
  border-color: var(--accent);
  font-weight: 700;
}

@media (max-width: 600px) {
  .bc-17__list {
    grid-auto-flow: row;
    grid-template-columns: 1fr;
    justify-items: stretch;
    gap: 6px;
  }

  .bc-17__item {
    width: 100%;
    justify-content: center;
  }

  .bc-17__item + .bc-17__item::before {
    display: none;
  }

  .bc-17__link {
    width: 100%;
    justify-content: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-17__link {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-columns:repeat(auto-fit,minmax(120px,1fr)) reflows crumbs into as many even columns as fit and wraps into aligned rows, no media queries. */
```
