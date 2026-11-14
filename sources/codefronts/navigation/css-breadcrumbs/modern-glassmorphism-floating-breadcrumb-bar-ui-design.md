---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/modern-glassmorphism-floating-breadcrumb-bar-ui-design/"
title: "Modern Glassmorphism Floating Breadcrumb Bar UI Design"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A frosted-glass breadcrumb pill floating over a colourful backdrop: heavy backdrop-filter blur + saturation, a light-catching gradient hairline border, and a…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Glassmorphism Floating Breadcrumb Bar UI Design
Source: https://codefronts.com/navigation/css-breadcrumbs/modern-glassmorphism-floating-breadcrumb-bar-ui-design/

A frosted-glass breadcrumb pill floating over a colourful backdrop: heavy backdrop-filter blur + saturation, a light-catching gradient hairline border, and a shimmer sweep across the bar on hover. The premium 'floating UI' treatment for hero sections and creative landings — kept readable and keyboard-accessible.
## HTML
```html
<div class="bc-05">
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="#">Home</a></li>
      <li><a href="#">Gallery</a></li>
      <li><a href="#">Collections</a></li>
      <li><a href="#" aria-current="page">Aurora Series</a></li>
    </ol>
  </nav>
</div>
```
## CSS
```css
.bc-05 {
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 48px 32px;
  display: flex;
  justify-content: center;
  background: linear-gradient(120deg,oklch(0.55 0.2 300),oklch(0.6 0.18 220) 45%,oklch(0.68 0.16 180));
  align-items: center;
  justify-content: center;
}

.bc-05 * {
  box-sizing: border-box;
}

.bc-05 ol {
  position: relative;
  overflow: hidden;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 10px 16px;
  border-radius: 16px;
  border: 1px solid transparent;
  background: linear-gradient(rgba(255,255,255,.12),rgba(255,255,255,.08)) padding-box,linear-gradient(155deg,rgba(255,255,255,.7),rgba(255,255,255,.15) 40%,rgba(255,255,255,.04)) border-box;
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  backdrop-filter: blur(12px) saturate(180%);
  box-shadow: 0 8px 32px rgba(0,0,0,.12),inset 0 1px 0 rgba(255,255,255,.25);
}

.bc-05 ol::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg,transparent 40%,rgba(255,255,255,.35) 50%,transparent 60%);
  translate: -120% 0;
  transition: translate .7s ease;
  pointer-events: none;
}

.bc-05 ol:hover::after {
  translate: 120% 0;
}

.bc-05 li {
  display: flex;
  align-items: center;
  position: relative;
  z-index: 1;
}

.bc-05 li + li::before {
  content: "›";
  margin: 0 8px;
  color: rgba(255,255,255,.6);
}

.bc-05 a {
  padding: 5px 10px;
  border-radius: 9px;
  font: 600 14px/1 system-ui,sans-serif;
  color: rgba(255,255,255,.82);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.bc-05 a:hover {
  color: #fff;
  background: rgba(255,255,255,.14);
}

.bc-05 a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.bc-05 li[aria-current="page"] a {
  color: #fff;
  background: rgba(255,255,255,.22);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
}

@media (prefers-reduced-motion: reduce) {
  .bc-05 ol::after {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — blur(12px) saturate(180%) frost, a two-layer gradient hairline for the lit rim, and a compositor-only shimmer sweep on hover. */
```
