---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/floating-island/"
title: "Floating Card Shadow CSS Breadcrumb Navigation"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "Each crumb is an elevated white card floating over the surface with a soft layered shadow, connected by faint dotted trails — a clear, tactile step-by-step…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Card Shadow CSS Breadcrumb Navigation
Source: https://codefronts.com/navigation/css-breadcrumbs/floating-island/

Each crumb is an elevated white card floating over the surface with a soft layered shadow, connected by faint dotted trails — a clear, tactile step-by-step path where every node reads as a distinct, liftable card. Hover raises the card higher; the current card rests at the top elevation.
## HTML
```html
<nav class="bc-32" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Library</a></li>
    <li><a href="#">Courses</a></li>
    <li><a href="#" aria-current="page">CSS Mastery</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-32 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.6 0.15 250);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 34px 30px;
  background: oklch(0.95 0.006 250);
  place-items: center;
}

.bc-32 * {
  box-sizing: border-box;
}

.bc-32 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-32 li {
  position: relative;
  display: flex;
  align-items: center;
}

.bc-32 li + li::before {
  content: "";
  position: absolute;
  left: -20px;
  width: 20px;
  height: 0;
  border-top: 2px dotted oklch(0.78 0.01 250);
  z-index: 0;
}

.bc-32 a {
  position: relative;
  z-index: 1;
  display: inline-block;
  padding: 9px 16px;
  border-radius: 11px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.4 0.03 250);
  text-decoration: none;
  background: #fff;
  box-shadow: 0 1px 2px rgba(20,30,60,.1),0 3px 8px rgba(20,30,60,.08);
  transition: transform .2s ease,box-shadow .2s ease,color .18s ease;
}

.bc-32 a:hover {
  transform: translateY(-2px);
  box-shadow: 0 3px 6px rgba(20,30,60,.12),0 10px 22px rgba(20,30,60,.14);
  color: var(--accent);
}

.bc-32 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-32 li[aria-current="page"] a {
  color: var(--accent);
  box-shadow: 0 4px 8px rgba(20,30,60,.14),0 14px 30px rgba(20,30,60,.16);
  box-shadow: 0 4px 8px rgba(20,30,60,.14),0 14px 30px rgba(20,30,60,.16),inset 0 0 0 1.5px color-mix(in oklab,var(--accent) 40%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .bc-32 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each crumb is an elevated card with a two-layer (ambient+key) shadow; hover lifts with translateY + deeper shadow, the current page rests at top elevation. */
```
