---
source: "codefronts"
url: "https://codefronts.com/navigation/css-breadcrumbs/editorial-numbered/"
title: "Circular Icon & Numbered CSS Step Breadcrumbs"
section: "navigation"
category: "css-breadcrumbs"
category_name: "CSS Breadcrumbs"
description: "A breadcrumb where each crumb leads with a circular badge holding a number or an SVG icon, followed by its label — the polished 'stepper meets breadcrumb'…"
has_js: "false"
---

Here's a working CSS Breadcrumb from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Icon & Numbered CSS Step Breadcrumbs
Source: https://codefronts.com/navigation/css-breadcrumbs/editorial-numbered/

A breadcrumb where each crumb leads with a circular badge holding a number or an SVG icon, followed by its label — the polished 'stepper meets breadcrumb' pattern for onboarding, dashboards and multi-part guides. Badges auto-number via CSS counters; icons swap in per crumb; connectors trace the path.
## HTML
```html
<nav class="bc-37" aria-label="Breadcrumb">
  <ol>
    <li><a href="#"><span class="bc-37__badge" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg></span>Home</a></li>
    <li><a href="#"><span class="bc-37__badge bc-37__num" aria-hidden="true"></span>Account</a></li>
    <li><a href="#"><span class="bc-37__badge bc-37__num" aria-hidden="true"></span>Profile</a></li>
    <li><a href="#" aria-current="page"><span class="bc-37__badge bc-37__num" aria-hidden="true"></span>Preferences</a></li>
  </ol>
</nav>
```
## CSS
```css
.bc-37 {
  display: grid;
  width: 100%;
  min-height: 100vh;
  --accent: oklch(0.58 0.16 260);
  --tint: oklch(0.92 0.03 260);
  font-family: system-ui,'Segoe UI',sans-serif;
  padding: 32px;
  background: oklch(0.98 0.004 260);
  counter-reset: bcstep;
  place-items: center;
}

.bc-37 * {
  box-sizing: border-box;
}

.bc-37 ol {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 18px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.bc-37 li {
  position: relative;
  display: flex;
  align-items: center;
}

.bc-37 li + li::before {
  content: "";
  position: absolute;
  left: -18px;
  width: 18px;
  border-top: 2px solid oklch(0.85 0.01 260);
}

.bc-37 a {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  font: 600 13.5px/1 system-ui,sans-serif;
  color: oklch(0.45 0.03 260);
  text-decoration: none;
  transition: color .15s ease;
}

.bc-37__badge {
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  flex: none;
  border-radius: 50%;
  background: var(--tint);
  color: var(--accent);
  font: 700 12px/1 system-ui,sans-serif;
}

.bc-37__badge svg {
  width: 15px;
  height: 15px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.bc-37__num {
  counter-increment: bcstep;
}

.bc-37__num::after {
  content: counter(bcstep);
}

.bc-37 a:hover {
  color: oklch(0.36 0.13 260);
}

.bc-37 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 6px;
}

.bc-37 li[aria-current="page"] a {
  color: oklch(0.28 0.02 260);
}

.bc-37 li[aria-current="page"] .bc-37__badge {
  background: var(--accent);
  color: #fff;
}

@media (max-width: 520px) {
  .bc-37 a {
    gap: 0;
    font-size: 0;
  }

  .bc-37 a .bc-37__badge {
    font-size: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bc-37 a {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — circular badges hold either an inline SVG or a CSS-counter number (content:counter(bcstep)); connectors trace the path, the current badge takes the accent fill. */
```
