---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/push-content-sidebar/"
title: "Push Content Sidebar Navigation Layout with Smooth CSS Transitions"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The drawer that pushes instead of covering: when it opens, the entire canvas slides right by exactly the drawer's width, staying fully visible — the…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Push Content Sidebar Navigation Layout with Smooth CSS Transitions
Source: https://codefronts.com/layouts/css-sidebar-layouts/push-content-sidebar/

The drawer that pushes instead of covering: when it opens, the entire canvas slides right by exactly the drawer's width, staying fully visible — the interaction pattern of Material's 'standard drawer' — with both elements sharing one width variable and one transition curve so they can never drift out of sync.
## HTML
```html
<section class="sbl-18">
  <input type="checkbox" id="sbl18-p" class="sbl-18__state">
  <aside class="sbl-18__drawer" aria-label="Layers">
    <h2>Layers</h2>
    <nav><a href="#" aria-current="page">Base map</a><a href="#">Traffic density</a><a href="#">Transit lines</a><a href="#">Bike network</a><a href="#">3D buildings</a></nav>
  </aside>
  <div class="sbl-18__canvas">
    <header class="sbl-18__bar"><label for="sbl18-p" class="sbl-18__toggle"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg><span>Layers</span></label><strong>Metroview</strong></header>
    <main class="sbl-18__map"><p>Open Layers — the whole canvas slides right by exactly 280px (one shared variable), never squeezing. Both moves are GPU transforms.</p></main>
  </div>
</section>
```
## CSS
```css
.sbl-18,
.sbl-18 *,
.sbl-18 *::before,
.sbl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-18 {
  --w: 280px;
  --panel: oklch(0.18 0.015 220);
  --ink: oklch(0.94 0.005 220);
  --mut: oklch(0.64 0.012 220);
  --line: oklch(0.29 0.016 220);
  --accent: oklch(0.75 0.13 220);
  position: relative;
  height: 100vh;
  height: 100dvh;
  overflow: hidden;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.14 0.012 220);
  color: var(--ink);
}

.sbl-18__state {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-18__drawer {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: var(--w);
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 20px 14px;
  transform: translate3d(-100%,0,0);
  transition: transform .32s cubic-bezier(.4,0,.2,1);
  z-index: 2;
}

.sbl-18:has(#sbl18-p:checked) .sbl-18__drawer {
  transform: translate3d(0,0,0);
}

.sbl-18__drawer h2 {
  font: 600 12px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: var(--mut);
  padding: 0 10px 14px;
}

.sbl-18__drawer nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-18__drawer a {
  padding: 11px 14px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .18s ease,color .18s ease;
}

.sbl-18__drawer a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-18__drawer a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-18__drawer a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-18__canvas {
  height: 100%;
  display: grid;
  grid-template-rows: auto 1fr;
  transform: translate3d(0,0,0);
  transition: transform .32s cubic-bezier(.4,0,.2,1);
}

.sbl-18:has(#sbl18-p:checked) .sbl-18__canvas {
  transform: translate3d(var(--w),0,0);
}

.sbl-18__bar {
  display: flex;
  align-items: center;
  gap: 14px;
  height: 54px;
  padding: 0 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  font: 600 15px/1 system-ui,sans-serif;
}

.sbl-18__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 13px;
  margin-left: -4px;
  border-radius: 10px;
  border: 1px solid var(--line);
  font: 500 13px/1 system-ui,sans-serif;
  color: var(--ink);
  cursor: pointer;
  transition: background-color .2s ease;
}

.sbl-18__toggle:hover {
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-18:has(#sbl18-p:focus-visible) .sbl-18__toggle {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-18__toggle svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
}

.sbl-18__map {
  display: grid;
  place-items: center;
  background: repeating-linear-gradient(0deg,transparent 0 39px,oklch(0.2 0.014 220) 39px 40px),repeating-linear-gradient(90deg,transparent 0 39px,oklch(0.2 0.014 220) 39px 40px),oklch(0.16 0.012 220);
}

.sbl-18__map p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 40ch;
  text-align: center;
  padding: 0 24px;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-18__drawer,
    .sbl-18__canvas,
    .sbl-18__toggle {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — drawer and canvas move as one welded unit: both transition translate3d over the same curve, displaced by one shared --w variable. */
```
