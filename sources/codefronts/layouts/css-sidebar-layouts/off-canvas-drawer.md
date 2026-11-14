---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/off-canvas-drawer/"
title: "Off-Canvas Navigation Drawer for Mobile & Desktop Web Apps"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The off-canvas drawer rebuilt on the platform's newest primitive: a <dialog>-grade Popover."
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Off-Canvas Navigation Drawer for Mobile & Desktop Web Apps
Source: https://codefronts.com/layouts/css-sidebar-layouts/off-canvas-drawer/

The off-canvas drawer rebuilt on the platform's newest primitive: a <dialog>-grade Popover. popover="auto" gives you Esc-to-close, click-outside dismissal, focus management and top-layer rendering — the whole 'drawer behavior' checklist browsers now ship natively — and @starting-style animates the entry, so even the open transition is declarative.
## HTML
```html
<section class="sbl-10">
  <header class="sbl-10__bar">
    <button class="sbl-10__open" popovertarget="sbl10-d"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>Menu</button>
    <strong>Waypoint</strong>
  </header>
  <aside class="sbl-10__drawer" popover="auto" id="sbl10-d" aria-label="Navigation drawer">
    <div class="sbl-10__head"><strong>Waypoint</strong><button class="sbl-10__close" popovertarget="sbl10-d" popovertargetaction="hide" aria-label="Close menu"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div>
    <nav class="sbl-10__nav">
      <a href="#" aria-current="page">Trips</a><a href="#">Explore</a><a href="#">Saved places</a><a href="#">Offline maps</a><a href="#">Account</a>
    </nav>
  </aside>
  <main class="sbl-10__main"><h1>Trips</h1><p>Open the drawer, then press <kbd>Esc</kbd> or click outside — dismissal, focus return and the blurred backdrop are all native Popover API behavior. No script.</p></main>
</section>
```
## CSS
```css
.sbl-10,
.sbl-10 *,
.sbl-10 *::before,
.sbl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-10 {
  --panel: oklch(0.18 0.02 165);
  --ink: oklch(0.94 0.005 165);
  --mut: oklch(0.65 0.012 165);
  --line: oklch(0.29 0.02 165);
  --accent: oklch(0.78 0.15 160);
  display: grid;
  grid-template-rows: auto 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.14 0.015 165);
  color: var(--ink);
}

.sbl-10__bar {
  display: flex;
  align-items: center;
  gap: 16px;
  height: 54px;
  padding: 0 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  font: 600 15px/1 system-ui,sans-serif;
}

.sbl-10__open {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid var(--line);
  background: none;
  color: var(--ink);
  font: 500 13.5px/1 system-ui,sans-serif;
  padding: 9px 14px;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color .2s ease;
}

.sbl-10__open:hover {
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-10__open:focus-visible,
.sbl-10__close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-10__open svg,
.sbl-10__close svg {
  width: 17px;
  height: 17px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.9;
  stroke-linecap: round;
}

.sbl-10__drawer {
  position: fixed;
  inset: 0 auto 0 0;
  width: min(300px,85vw);
  height: 100%;
  max-height: none;
  border: none;
  border-right: 1px solid var(--line);
  background: var(--panel);
  color: var(--ink);
  padding: 16px;
  translate: 0 0;
  transition: translate .32s cubic-bezier(.4,0,.2,1),display .32s allow-discrete,overlay .32s allow-discrete;
}

.sbl-10__drawer:not(:popover-open) {
  translate: -100% 0;
}

@starting-style {
  .sbl-10__drawer:popover-open {
    translate: -100% 0;
  }
}

.sbl-10__drawer::backdrop {
  background: oklch(0 0 0 / .45);
  backdrop-filter: blur(3px);
  transition: opacity .32s ease,display .32s allow-discrete,overlay .32s allow-discrete;
  opacity: 1;
}

.sbl-10__drawer:not(:popover-open)::backdrop {
  opacity: 0;
}

@starting-style {
  .sbl-10__drawer:popover-open::backdrop {
    opacity: 0;
  }
}

.sbl-10__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4px 6px 16px;
  font: 700 15px/1 system-ui,sans-serif;
}

.sbl-10__close {
  display: grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 9px;
  background: none;
  color: var(--mut);
  cursor: pointer;
}

.sbl-10__close:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 8%,transparent);
}

.sbl-10__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-10__nav a {
  padding: 12px 14px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-10__nav a:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-10__nav a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-10__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-10__main {
  padding: 28px;
  overflow-y: auto;
}

.sbl-10__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-10__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 48ch;
  text-wrap: pretty;
}

.sbl-10 kbd {
  font: 600 11px ui-monospace,Menlo,monospace;
  background: color-mix(in oklab,var(--ink) 10%,transparent);
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 2px 6px;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-10__drawer,
    .sbl-10__drawer::backdrop {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — popover="auto" + popovertarget give native open/close, Esc, light-dismiss and ::backdrop; @starting-style animates the top-layer entry. */
```
