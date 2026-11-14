---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/e-commerce-filter-attribute-breadcrumb-navigation-component/"
title: "E-Commerce Filter & Attribute Breadcrumb Navigation Component"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "The Shopify/Magento-style faceted-filter trail: Home › Women › Shoes plus removable active-filter chips (Size 8, Under $120, In stock) each with a…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Filter & Attribute Breadcrumb Navigation Component
Source: https://codefronts.com/navigation/css-breadcrumbs/e-commerce-filter-attribute-breadcrumb-navigation-component/

The Shopify/Magento-style faceted-filter trail: Home › Women › Shoes plus removable active-filter chips (Size 8, Under $120, In stock) each with a hover-scaling remove badge. Wraps gracefully on mobile with flex-wrap + gap, mixes navigation crumbs and filter tokens in one accessible bar.
## HTML
```html
<div class="bc-04">
  <nav class="bc-04__path" aria-label="Breadcrumb">
    <ol>
      <li><a href="#">Home</a></li>
      <li><a href="#">Women</a></li>
      <li><a href="#" aria-current="page">Shoes</a></li>
    </ol>
  </nav>
  <ul class="bc-04__filters" aria-label="Active filters">
    <li class="bc-04__chip">Size 8<button type="button" aria-label="Remove filter: Size 8"></button></li>
    <li class="bc-04__chip">Under $120<button type="button" aria-label="Remove filter: Under $120"></button></li>
    <li class="bc-04__chip">In stock<button type="button" aria-label="Remove filter: In stock"></button></li>
    <li class="bc-04__chip">Colour: Tan<button type="button" aria-label="Remove filter: Colour Tan"></button></li>
  </ul>
</div>
```
## CSS
```css
.bc-04 {
  width: 100%;
  min-height: 100vh;
  --x: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 6l12 12M18 6L6 18' stroke='black' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E");
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 26px;
  background: oklch(0.98 0.004 90);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  align-items: center;
  justify-content: center;
}

.bc-04 * {
  box-sizing: border-box;
}

.bc-04__path ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-04__path li {
  display: flex;
  align-items: center;
}

.bc-04__path li + li::before {
  content: "›";
  margin: 0 8px;
  color: oklch(0.7 0.02 90);
}

.bc-04__path a {
  padding: 4px 6px;
  border-radius: 6px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.48 0.04 60);
  text-decoration: none;
  transition: color .15s ease;
}

.bc-04__path a:hover {
  color: oklch(0.55 0.14 45);
}

.bc-04__path a:focus-visible {
  outline: 2px solid oklch(0.55 0.14 45);
  outline-offset: 2px;
}

.bc-04__path li[aria-current="page"] a {
  color: oklch(0.28 0.02 60);
}

.bc-04__filters {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-04__chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 8px 6px 13px;
  border-radius: 999px;
  font: 600 12.5px/1 system-ui,sans-serif;
  color: oklch(0.42 0.05 55);
  background: oklch(0.92 0.03 70);
  border: 1px solid oklch(0.86 0.04 65);
  transition: background-color .18s ease,color .18s ease;
}

.bc-04__chip button {
  width: 20px;
  height: 20px;
  flex: none;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  background: oklch(0.55 0.05 55);
  -webkit-mask: var(--x) center/13px no-repeat;
  mask: var(--x) center/13px no-repeat;
  transition: transform .15s ease,background-color .18s ease;
}

.bc-04__chip button:hover,
.bc-04__chip button:focus-visible {
  transform: scale(1.15);
  background: oklch(0.55 0.19 25);
  outline: none;
}

.bc-04__chip:has(button:hover),
.bc-04__chip:has(button:focus-visible) {
  background: color-mix(in oklab,oklch(0.6 0.19 25) 15%,oklch(0.92 0.03 70));
  color: oklch(0.45 0.16 25);
}

.bc-04__chip button:focus-visible {
  outline: 2px solid oklch(0.55 0.19 25);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .bc-04__chip,
    .bc-04__chip button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript for the UI — nav crumbs in an <ol>, removable facet chips in a <ul>; the × is a mask-image button that inherits colour and scales on hover. Wire removal in your framework. */
```
