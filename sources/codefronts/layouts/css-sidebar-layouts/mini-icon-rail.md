---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/mini-icon-rail/"
title: "Compact Mini Icon Rail Sidebar Navigation for SaaS Web Apps"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The 68px icon rail perfected: 44px hit targets, an anchor-positioned active pill that GLIDES between icons using CSS anchor positioning, hover tooltips,…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compact Mini Icon Rail Sidebar Navigation for SaaS Web Apps
Source: https://codefronts.com/layouts/css-sidebar-layouts/mini-icon-rail/

The 68px icon rail perfected: 44px hit targets, an anchor-positioned active pill that GLIDES between icons using CSS anchor positioning, hover tooltips, notification dots, and a bottom-pinned avatar. The sliding indicator — the effect teams reach for Framer Motion to get — is pure CSS via anchor-name and position-anchor.
## HTML
```html
<section class="sbl-14">
  <aside class="sbl-14__rail" aria-label="Primary">
    <span class="sbl-14__logo" aria-hidden="true"></span>
    <span class="sbl-14__pill" aria-hidden="true"></span>
    <nav class="sbl-14__nav">
      <label class="sbl-14__item" data-tooltip="Home"><input type="radio" name="sbl14" checked><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5M5.5 9.5V21h13V9.5"/></svg><span class="sbl-14__sr">Home</span></label>
      <label class="sbl-14__item" data-tooltip="Inbox"><input type="radio" name="sbl14"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 13h5l2 3h4l2-3h5M5 5h14l2 8v6H3v-6z"/></svg><span class="sbl-14__sr">Inbox</span><i class="sbl-14__dot" aria-hidden="true"></i></label>
      <label class="sbl-14__item" data-tooltip="Projects"><input type="radio" name="sbl14"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="sbl-14__sr">Projects</span></label>
      <label class="sbl-14__item" data-tooltip="Analytics"><input type="radio" name="sbl14"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="sbl-14__sr">Analytics</span></label>
    </nav>
    <span class="sbl-14__avatar" data-tooltip="Ada Kim">AK</span>
  </aside>
  <main class="sbl-14__main"><h1>Home</h1><p>Click the rail icons — the active pill slides between them with CSS anchor positioning. Hover for tooltips.</p></main>
</section>
```
## CSS
```css
.sbl-14,
.sbl-14 *,
.sbl-14 *::before,
.sbl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-14 {
  --panel: oklch(0.16 0.02 255);
  --ink: oklch(0.93 0.005 255);
  --mut: oklch(0.58 0.014 255);
  --line: oklch(0.27 0.02 255);
  --accent: oklch(0.74 0.14 195);
  display: grid;
  grid-template-columns: 68px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.015 255);
  color: var(--ink);
}

.sbl-14__rail {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 14px 0;
  background: var(--panel);
  border-right: 1px solid var(--line);
}

.sbl-14__logo {
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: conic-gradient(from 45deg,var(--accent),oklch(0.62 0.17 285));
  margin-bottom: 12px;
}

.sbl-14__nav {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sbl-14__item {
  position: relative;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  color: var(--mut);
  cursor: pointer;
  transition: color .2s ease,background-color .2s ease;
  z-index: 1;
}

.sbl-14__item svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-14__item input {
  position: absolute;
  opacity: 0;
  inset: 0;
  margin: 0;
  cursor: pointer;
}

.sbl-14__item:hover {
  color: var(--ink);
}

.sbl-14__item:has(input:checked) {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-14__item:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-14__nav .sbl-14__item:nth-child(1) {
  anchor-name: --sbl14-a1;
}

.sbl-14__nav .sbl-14__item:nth-child(2) {
  anchor-name: --sbl14-a2;
}

.sbl-14__nav .sbl-14__item:nth-child(3) {
  anchor-name: --sbl14-a3;
}

.sbl-14__nav .sbl-14__item:nth-child(4) {
  anchor-name: --sbl14-a4;
}

.sbl-14__pill {
  position: absolute;
  left: 8px;
  width: 3.5px;
  height: 26px;
  border-radius: 4px;
  background: var(--accent);
  box-shadow: 0 0 10px color-mix(in oklab,var(--accent) 60%,transparent);
  top: calc(anchor(top) + 9px);
  position-anchor: --sbl14-a1;
  transition: top .3s cubic-bezier(.5,0,.2,1.2);
}

.sbl-14:has(.sbl-14__item:nth-child(2) input:checked) .sbl-14__pill {
  position-anchor: --sbl14-a2;
}

.sbl-14:has(.sbl-14__item:nth-child(3) input:checked) .sbl-14__pill {
  position-anchor: --sbl14-a3;
}

.sbl-14:has(.sbl-14__item:nth-child(4) input:checked) .sbl-14__pill {
  position-anchor: --sbl14-a4;
}

@supports not (anchor-name: --x) {
  .sbl-14__pill {
    display: none;
  }
}

.sbl-14__dot {
  position: absolute;
  top: 9px;
  right: 9px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(0.68 0.21 25);
  box-shadow: 0 0 0 2.5px var(--panel);
}

.sbl-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sbl-14__item::after,
.sbl-14__avatar::after {
  content: attr(data-tooltip);
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  translate: -4px -50%;
  padding: 7px 11px;
  border-radius: 8px;
  background: oklch(0.24 0.02 255);
  border: 1px solid var(--line);
  color: var(--ink);
  font: 500 12px/1 system-ui,sans-serif;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease .25s,translate .2s ease .25s;
  z-index: 6;
}

.sbl-14__item:hover::after,
.sbl-14__item:has(input:focus-visible)::after,
.sbl-14__avatar:hover::after {
  opacity: 1;
  translate: 0 -50%;
}

.sbl-14__avatar {
  position: relative;
  display: grid;
  place-items: center;
  width: 36px;
  height: 36px;
  margin-top: auto;
  border-radius: 50%;
  font: 700 11.5px/1 system-ui,sans-serif;
  color: #fff;
  background: linear-gradient(135deg,var(--accent),oklch(0.6 0.17 285));
  cursor: pointer;
}

.sbl-14__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-14__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-14__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 46ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-14__pill,
    .sbl-14__item {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each icon declares an anchor-name; the indicator pill re-targets position-anchor via :has(:checked) and transitions between anchors. */
```
