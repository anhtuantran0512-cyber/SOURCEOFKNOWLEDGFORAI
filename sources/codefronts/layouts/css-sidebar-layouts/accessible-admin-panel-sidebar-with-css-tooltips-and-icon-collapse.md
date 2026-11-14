---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/accessible-admin-panel-sidebar-with-css-tooltips-and-icon-collapse/"
title: "Accessible Admin Panel Sidebar with CSS Tooltips and Icon Collapse"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "An enterprise admin rail that collapses from 240px of labeled navigation down to a 64px icon strip — and when collapsed, every icon grows a floating tooltip…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Admin Panel Sidebar with CSS Tooltips and Icon Collapse
Source: https://codefronts.com/layouts/css-sidebar-layouts/accessible-admin-panel-sidebar-with-css-tooltips-and-icon-collapse/

An enterprise admin rail that collapses from 240px of labeled navigation down to a 64px icon strip — and when collapsed, every icon grows a floating tooltip on hover AND keyboard focus, built from a data-tooltip attribute and one pseudo-element. The collapse animates the grid track itself, so main content reflows smoothly with it.
## HTML
```html
<section class="sbl-02">
  <input type="checkbox" id="sbl02-fold" class="sbl-02__check">
  <aside class="sbl-02__sidebar">
    <label for="sbl02-fold" class="sbl-02__fold" data-tooltip="Expand"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m14 6-6 6 6 6"/></svg><span class="sbl-02__label">Collapse</span></label>
    <nav class="sbl-02__nav" aria-label="Admin">
      <a class="sbl-02__link" href="#" aria-current="page" data-tooltip="Dashboard"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="sbl-02__label">Dashboard</span></a>
      <a class="sbl-02__link" href="#" data-tooltip="Users"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg><span class="sbl-02__label">Users</span></a>
      <a class="sbl-02__link" href="#" data-tooltip="Reports"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="sbl-02__label">Reports</span></a>
      <a class="sbl-02__link" href="#" data-tooltip="Audit log"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3.5 6h.01M3.5 12h.01M3.5 18h.01"/></svg><span class="sbl-02__label">Audit log</span></a>
      <a class="sbl-02__link" href="#" data-tooltip="Settings"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="sbl-02__label">Settings</span></a>
    </nav>
  </aside>
  <main class="sbl-02__main"><h1>User management</h1><p>Toggle the chevron — labels fold into a 0fr grid track and tooltips take over.</p></main>
</section>
```
## CSS
```css
.sbl-02,
.sbl-02 *,
.sbl-02 *::before,
.sbl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-02 {
  --panel: oklch(0.16 0.02 275);
  --ink: oklch(0.92 0.005 275);
  --mut: oklch(0.64 0.012 275);
  --line: oklch(0.27 0.02 275);
  --accent: oklch(0.68 0.17 275);
  display: grid;
  grid-template-columns: 240px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.015 275);
  color: var(--ink);
  transition: grid-template-columns .3s ease;
}

.sbl-02:has(#sbl02-fold:checked) {
  grid-template-columns: 64px 1fr;
}

.sbl-02__check {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.sbl-02__sidebar {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 14px 10px;
  background: var(--panel);
  border-right: 1px solid var(--line);
  overflow: visible;
}

.sbl-02__fold,
.sbl-02__link {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr;
  align-items: center;
  gap: 0 12px;
  min-height: 44px;
  padding: 0 13px;
  border-radius: 10px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  cursor: pointer;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-02__fold {
  margin-bottom: 10px;
  color: var(--ink);
}

.sbl-02__fold svg,
.sbl-02__link svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .3s ease;
}

.sbl-02__label {
  display: grid;
  grid-template-columns: 1fr;
  overflow: hidden;
  white-space: nowrap;
  transition: grid-template-columns .3s ease,opacity .25s ease;
}

.sbl-02:has(#sbl02-fold:checked) .sbl-02__label {
  grid-template-columns: 0fr;
  opacity: 0;
}

.sbl-02:has(#sbl02-fold:checked) .sbl-02__fold svg {
  rotate: 180deg;
}

.sbl-02__link:hover,
.sbl-02__fold:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-02__link[aria-current="page"] {
  color: var(--ink);
  background: color-mix(in oklab,var(--accent) 20%,transparent);
}

.sbl-02__link:focus-visible,
.sbl-02:has(#sbl02-fold:focus-visible) .sbl-02__fold {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-02__fold::after,
.sbl-02__link::after {
  content: attr(data-tooltip);
  position: absolute;
  left: calc(100% + 14px);
  top: 50%;
  translate: -4px -50%;
  padding: 7px 11px;
  border-radius: 8px;
  background: oklch(0.24 0.02 275);
  border: 1px solid var(--line);
  color: var(--ink);
  font: 500 12.5px/1 system-ui,sans-serif;
  white-space: nowrap;
  box-shadow: 0 6px 18px oklch(0 0 0 / .4);
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease .15s,translate .2s ease .15s;
  z-index: 5;
}

.sbl-02:has(#sbl02-fold:checked) .sbl-02__link:hover::after,
.sbl-02:has(#sbl02-fold:checked) .sbl-02__link:focus-visible::after,
.sbl-02:has(#sbl02-fold:checked) .sbl-02__fold:hover::after {
  opacity: 1;
  translate: 0 -50%;
}

.sbl-02__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-02__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-02__main p {
  color: var(--mut);
  font-size: 14px;
  max-width: 44ch;
  line-height: 1.6;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-02,
    .sbl-02 .sbl-02__label,
    .sbl-02 .sbl-02__fold svg {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid-template-columns animates 240px→64px via :has(:checked); labels collapse to a 0fr track; tooltips are [data-tooltip]::after. */
```
