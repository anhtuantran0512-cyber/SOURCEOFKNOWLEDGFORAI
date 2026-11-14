---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/neon-trail/"
title: "Gradient Background Glow CSS Breadcrumb Bar"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A vivid breadcrumb bar with a multi-stop gradient fill and a matching coloured glow beneath it, plus gradient-clipped text on the current crumb so its label…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Background Glow CSS Breadcrumb Bar
Source: https://codefronts.com/navigation/css-breadcrumbs/neon-trail/

A vivid breadcrumb bar with a multi-stop gradient fill and a matching coloured glow beneath it, plus gradient-clipped text on the current crumb so its label is painted with the same spectrum. The bold, energetic treatment for landing pages and creative product headers — animated gradient optional.
## HTML
```html
<nav class="bc-31" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Home</a></li>
    <li><a href="#">Studio</a></li>
    <li><a href="#">Work</a></li>
    <li><a href="#" aria-current="page">Spectrum</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-31 {
  width: 100%;
  min-height: 100vh;
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 44px 32px;
  background: oklch(0.15 0.02 285);
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: center;
}

.bc-31 * {
  box-sizing: border-box;
}

.bc-31 ol {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 11px 18px;
  border-radius: 14px;
  background: linear-gradient(100deg,oklch(0.6 0.2 300),oklch(0.62 0.19 260) 50%,oklch(0.68 0.17 200));
}

.bc-31 ol::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: 14px;
  background: inherit;
  filter: blur(18px);
  opacity: .7;
  transform: translateY(8px);
  pointer-events: none;
}

.bc-31 li {
  display: flex;
  align-items: center;
}

.bc-31 li + li::before {
  content: "›";
  margin: 0 9px;
  color: rgba(255,255,255,.7);
}

.bc-31 a {
  padding: 5px 10px;
  border-radius: 8px;
  font: 600 14px/1 system-ui,sans-serif;
  color: #fff;
  text-decoration: none;
  transition: background-color .18s ease;
}

.bc-31 a:hover {
  background: rgba(255,255,255,.16);
}

.bc-31 a:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.bc-31 li[aria-current="page"] a {
  font-weight: 800;
  background: linear-gradient(90deg,#fff,oklch(0.92 0.08 300));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

@media (prefers-reduced-motion: reduce) {
  .bc-31 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the bar's gradient is re-blurred on a ::before to emit a matching glow; the current label uses background-clip:text for gradient-painted type. */
```
