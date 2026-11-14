---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/frosted-glass/"
title: "Frosted Glass Dark UI CSS Breadcrumb Component"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A dark-mode frosted-glass breadcrumb: a translucent charcoal panel with backdrop blur over a moody gradient, hairline top-edge sheen, and cool accent links —…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Dark UI CSS Breadcrumb Component
Source: https://codefronts.com/navigation/css-breadcrumbs/frosted-glass/

A dark-mode frosted-glass breadcrumb: a translucent charcoal panel with backdrop blur over a moody gradient, hairline top-edge sheen, and cool accent links — the dark counterpart to the glassmorphism demo, tuned for modern dark dashboards and creative dark UIs.
## HTML
```html
<nav class="bc-38" aria-label="Breadcrumb">
  <ol>
    <li><a href="#">Studio</a></li>
    <li><a href="#">Sessions</a></li>
    <li><a href="#">Mixes</a></li>
    <li><a href="#" aria-current="page">Midnight Set</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-38 {
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.72 0.15 200);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 48px 32px;
  display: flex;
  justify-content: center;
  background: radial-gradient(120% 140% at 20% 0%,oklch(0.32 0.09 280),oklch(0.14 0.03 260) 55%,oklch(0.1 0.02 240));
  align-items: center;
  justify-content: center;
}

.bc-38 * {
  box-sizing: border-box;
}

.bc-38 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 11px 16px;
  border-radius: 15px;
  background: oklch(0.2 0.02 265/.55);
  border: 1px solid oklch(0.35 0.02 265/.5);
  border-bottom-color: oklch(0.08 0.01 265/.6);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  backdrop-filter: blur(14px) saturate(160%);
  box-shadow: 0 10px 40px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.12);
}

.bc-38 li {
  display: flex;
  align-items: center;
}

.bc-38 li + li::before {
  content: "›";
  margin: 0 9px;
  color: oklch(0.6 0.02 265);
}

.bc-38 a {
  padding: 5px 10px;
  border-radius: 9px;
  font: 500 14px/1 system-ui,sans-serif;
  color: oklch(0.82 0.02 265);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.bc-38 a:hover {
  color: #fff;
  background: oklch(0.4 0.02 265/.5);
}

.bc-38 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.bc-38 li[aria-current="page"] a {
  color: #fff;
  background: color-mix(in oklab,var(--accent) 26%,oklch(0.25 0.02 265));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.15);
}

@media (prefers-reduced-motion: reduce) {
  .bc-38 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dark translucent fill under blur(14px) saturate(160%) with a lit top rim; light text and a solid-ish current wash keep dark glass readable. */
```
