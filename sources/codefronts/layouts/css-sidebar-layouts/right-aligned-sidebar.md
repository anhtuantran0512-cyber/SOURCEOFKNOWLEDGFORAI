---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/right-aligned-sidebar/"
title: "Right-Aligned CSS Sidebar Layout for Secondary Tool Panels"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The design-tool inspector: a right-hand properties panel that mirrors everything a left nav does — but tuned for its actual job: dense labeled controls,…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Right-Aligned CSS Sidebar Layout for Secondary Tool Panels
Source: https://codefronts.com/layouts/css-sidebar-layouts/right-aligned-sidebar/

The design-tool inspector: a right-hand properties panel that mirrors everything a left nav does — but tuned for its actual job: dense labeled controls, section dividers, logical-property-driven borders so the whole layout flips for RTL locales automatically, and a canvas pane that stays the star of the show.
## HTML
```html
<section class="sbl-11">
  <main class="sbl-11__canvas" aria-label="Canvas">
    <div class="sbl-11__artboard"><div class="sbl-11__shape" aria-hidden="true"></div><span>hero-card</span></div>
  </main>
  <aside class="sbl-11__panel" aria-label="Properties">
    <h2 class="sbl-11__title">Design</h2>
    <div class="sbl-11__group">
      <h3>Layout</h3>
      <div class="sbl-11__row"><label for="sbl11-w">W</label><input id="sbl11-w" type="number" value="320"><label for="sbl11-h">H</label><input id="sbl11-h" type="number" value="180"></div>
      <div class="sbl-11__row"><label for="sbl11-x">X</label><input id="sbl11-x" type="number" value="64"><label for="sbl11-y">Y</label><input id="sbl11-y" type="number" value="42"></div>
    </div>
    <div class="sbl-11__group">
      <h3>Appearance</h3>
      <div class="sbl-11__row"><label for="sbl11-r">Radius</label><input id="sbl11-r" type="number" value="16"><label for="sbl11-o">Opacity</label><input id="sbl11-o" type="number" value="100"></div>
      <div class="sbl-11__row sbl-11__row--fill"><label for="sbl11-f">Fill</label><input id="sbl11-f" type="color" value="#7c6ff0"><code>#7C6FF0</code></div>
    </div>
    <div class="sbl-11__group">
      <h3>Export</h3>
      <button class="sbl-11__btn" type="button">Export PNG ·2x</button>
    </div>
  </aside>
</section>
```
## CSS
```css
.sbl-11,
.sbl-11 *,
.sbl-11 *::before,
.sbl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-11 {
  --panel: oklch(0.19 0.012 280);
  --ink: oklch(0.93 0.005 280);
  --mut: oklch(0.6 0.012 280);
  --line: oklch(0.29 0.015 280);
  --accent: oklch(0.66 0.17 285);
  display: grid;
  grid-template-columns: 1fr 300px;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.15 0.01 280);
  color: var(--ink);
}

.sbl-11__canvas {
  display: grid;
  place-items: center;
  overflow: auto;
  background: radial-gradient(oklch(0.22 0.012 280) 1px,transparent 1px);
  background-size: 22px 22px;
}

.sbl-11__artboard {
  display: grid;
  gap: 10px;
  justify-items: center;
  font: 500 12px/1 ui-monospace,Menlo,monospace;
  color: var(--mut);
}

.sbl-11__shape {
  width: 320px;
  height: 180px;
  border-radius: 16px;
  background: linear-gradient(135deg,oklch(0.62 0.17 285),oklch(0.55 0.19 320));
  outline: 1.5px solid var(--accent);
  outline-offset: 4px;
}

.sbl-11__panel {
  border-inline-start: 1px solid var(--line);
  background: var(--panel);
  overflow-y: auto;
  padding: 18px 16px;
}

.sbl-11__title {
  font: 600 14px/1 system-ui,sans-serif;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--line);
}

.sbl-11__group {
  padding: 16px 0;
  border-bottom: 1px solid var(--line);
  display: grid;
  gap: 10px;
}

.sbl-11__group h3 {
  font: 600 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: var(--mut);
}

.sbl-11__row {
  display: grid;
  grid-template-columns: auto 1fr auto 1fr;
  align-items: center;
  gap: 8px;
}

.sbl-11__row label {
  font: 500 11.5px/1 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-11__row input[type="number"] {
  min-width: 0;
  width: 100%;
  padding: 7px 9px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: oklch(0.16 0.01 280);
  color: var(--ink);
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  font-variant-numeric: tabular-nums;
}

.sbl-11__row input:focus-visible,
.sbl-11__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.sbl-11__row--fill {
  grid-template-columns: auto auto 1fr;
}

.sbl-11__row--fill code {
  font: 500 12px/1 ui-monospace,Menlo,monospace;
  color: var(--mut);
}

.sbl-11__row input[type="color"] {
  width: 30px;
  height: 30px;
  padding: 2px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: none;
  cursor: pointer;
}

.sbl-11__btn {
  padding: 10px;
  border-radius: 9px;
  border: 1px solid color-mix(in oklab,var(--accent) 50%,transparent);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
  color: var(--ink);
  font: 600 12.5px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: background-color .2s ease;
}

.sbl-11__btn:hover {
  background: color-mix(in oklab,var(--accent) 26%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .sbl-11__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a mirrored grid shell (1fr 300px) with logical border-inline-start, so RTL locales flip the panel side automatically. */
```
