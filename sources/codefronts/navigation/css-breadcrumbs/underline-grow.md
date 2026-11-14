---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/underline-grow/"
title: "Interactive Breadcrumb Links with Animated CSS Underline Glow"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A minimalist breadcrumb whose links grow a directional animated underline on hover — wiping in from the left on enter, out to the right on leave — with a…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Breadcrumb Links with Animated CSS Underline Glow
Source: https://codefronts.com/navigation/css-breadcrumbs/underline-grow/

A minimalist breadcrumb whose links grow a directional animated underline on hover — wiping in from the left on enter, out to the right on leave — with a soft accent glow beneath the text. A tactile micro-interaction built from one ::after pseudo-element and a transform-origin flip, running fully on the compositor.
## HTML
```html
<nav class="bc-25" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Journal</a></li>
    <li><a href="#">Typography</a></li>
    <li><a href="#" aria-current="page">Variable Fonts</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-25 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.7 0.17 300);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 30px;
  background: oklch(0.16 0.02 300);
  place-items: center;
}

.bc-25 * {
  box-sizing: border-box;
}

.bc-25 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-25 li {
  display: flex;
  align-items: center;
}

.bc-25 li + li::before {
  content: "/";
  margin: 0 14px;
  color: oklch(0.45 0.02 300);
}

.bc-25 a {
  position: relative;
  padding: 3px 1px;
  font: 600 15px/1 system-ui,sans-serif;
  color: oklch(0.8 0.02 300);
  text-decoration: none;
  transition: color .2s ease;
}

.bc-25 a::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: -4px;
  height: 2.5px;
  border-radius: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform .35s cubic-bezier(0.25,1,0.5,1);
  filter: drop-shadow(0 0 5px var(--accent));
}

.bc-25 a:hover,
.bc-25 a:focus-visible {
  color: #fff;
  outline: none;
}

.bc-25 a:hover::after,
.bc-25 a:focus-visible::after {
  transform: scaleX(1);
  transform-origin: left;
}

.bc-25 a:focus-visible {
  text-decoration: underline;
  text-underline-offset: 6px;
  text-decoration-color: transparent;
}

.bc-25 li[aria-current="page"] a {
  color: #fff;
  cursor: default;
}

.bc-25 li[aria-current="page"] a::after {
  transform: scaleX(1);
  transform-origin: left;
}

@media (prefers-reduced-motion: reduce) {
  .bc-25 a::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one ::after underline flips transform-origin between rest (right) and hover (left) for a directional wipe, with a drop-shadow accent glow. */
```
