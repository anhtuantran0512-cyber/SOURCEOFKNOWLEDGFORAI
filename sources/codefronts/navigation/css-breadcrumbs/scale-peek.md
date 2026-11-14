---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/scale-peek/"
title: "Modern Micro-Interaction Animated Hover Breadcrumbs"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb built around a delightful hover micro-interaction: each crumb lifts with a subtle translateY, gains a soft shadow, and its separator chevron…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Micro-Interaction Animated Hover Breadcrumbs
Source: https://codefronts.com/navigation/css-breadcrumbs/scale-peek/

A breadcrumb built around a delightful hover micro-interaction: each crumb lifts with a subtle translateY, gains a soft shadow, and its separator chevron nudges forward — small, spring-eased motions that make the trail feel responsive and alive without being distracting. Compositor-only and reduced-motion-safe.
## HTML
```html
<nav class="bc-39" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Products</a></li>
    <li><a href="#">Hardware</a></li>
    <li><a href="#" aria-current="page">Keyboards</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-39 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.58 0.15 285);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 34px 30px;
  background: oklch(0.98 0.004 285);
  place-items: center;
}

.bc-39 * {
  box-sizing: border-box;
}

.bc-39 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-39 li {
  display: flex;
  align-items: center;
}

.bc-39 li:not(:last-child)::after {
  content: "›";
  margin: 0 8px;
  color: oklch(0.7 0.02 285);
  transition: transform .2s cubic-bezier(.34,1.56,.64,1),color .18s ease;
}

.bc-39 li:has(a:hover):not(:last-child)::after {
  transform: translateX(3px);
  color: var(--accent);
}

.bc-39 a {
  display: inline-block;
  padding: 7px 12px;
  border-radius: 9px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.45 0.04 285);
  text-decoration: none;
  background: transparent;
  box-shadow: 0 0 0 rgba(40,20,80,0);
  transition: transform .2s cubic-bezier(.34,1.56,.64,1),box-shadow .2s ease,color .18s ease,background-color .18s ease;
}

.bc-39 a:hover,
.bc-39 a:focus-visible {
  transform: translateY(-2px);
  color: var(--accent);
  background: #fff;
  box-shadow: 0 6px 16px rgba(40,20,80,.14);
  outline: none;
}

.bc-39 a:focus-visible {
  box-shadow: 0 6px 16px rgba(40,20,80,.14),0 0 0 2px var(--accent);
}

.bc-39 li[aria-current="page"] a {
  color: oklch(0.3 0.02 285);
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .bc-39 a,
    .bc-39 li::after {
    transition: none;
  }

  .bc-39 a:hover,
    .bc-39 a:focus-visible {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 2px translateY lift + soft shadow on hover, and a :has()-driven chevron nudge toward the next crumb, all spring-eased and compositor-only. */
```
