---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/horizontal-navigation-top-bar-dashboard/"
title: "Horizontal Navigation Top-Bar Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The GitHub/Stripe school: no sidebar at all — a global top bar, a tab strip with an animated underline, and content living in a centered min(100% − 48px,…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Navigation Top-Bar Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/horizontal-navigation-top-bar-dashboard/

The GitHub/Stripe school: no sidebar at all — a global top bar, a tab strip with an animated underline, and content living in a centered min(100% − 48px, 920px) column that breathes at every width. Tabs are radios, so :has() swaps the three settings panes and slides each underline in with zero JS; the tab strip sticks under the bar while the page scrolls. The layout for products whose nav fits in seven words.
## HTML
```html
<section class="cdl-17" aria-label="Top-bar navigation dashboard demo">
  <div class="cdl-17__page">
    <header class="cdl-17__bar">
      <span class="cdl-17__logo" aria-hidden="true"></span>
      <nav class="cdl-17__crumbs" aria-label="Breadcrumb"><a href="#org">acme-inc</a><i aria-hidden="true">/</i><b>billing</b></nav>
      <span class="cdl-17__search">Jump to… <kbd>/</kbd></span>
      <span class="cdl-17__me" aria-hidden="true">AR</span>
    </header>
    <div class="cdl-17__scroll">
    <div class="cdl-17__tabs" role="group" aria-label="Billing sections">
      <div class="cdl-17__tabrow">
        <label class="cdl-17__tab"><input type="radio" name="cdl17" id="cdl17-t1" checked><span>Overview</span></label>
        <label class="cdl-17__tab"><input type="radio" name="cdl17" id="cdl17-t2"><span>Plans</span></label>
        <label class="cdl-17__tab"><input type="radio" name="cdl17" id="cdl17-t3"><span>Danger zone</span></label>
      </div>
    </div>
      <main class="cdl-17__content">
        <div class="cdl-17__pane cdl-17__pane--1">
          <h1>Billing overview</h1>
          <div class="cdl-17__row">
            <article class="cdl-17__card"><h3>Current plan</h3><p class="cdl-17__big">Team</p><small>$96 / month · renews Aug 12</small><button type="button" class="cdl-17__ghost">Manage</button></article>
            <article class="cdl-17__card"><h3>Usage this cycle</h3><p class="cdl-17__big">64%</p><span class="cdl-17__meter" aria-hidden="true"><i style="--w:64%"></i></span><small>12,800 / 20,000 build minutes</small></article>
          </div>
          <article class="cdl-17__card">
            <h3>Invoices</h3>
            <p class="cdl-17__line"><b>#0091 · July 2026</b><span>$96.00</span><a href="#dl">PDF</a></p>
            <p class="cdl-17__line"><b>#0087 · June 2026</b><span>$96.00</span><a href="#dl">PDF</a></p>
            <p class="cdl-17__line"><b>#0082 · May 2026</b><span>$84.00</span><a href="#dl">PDF</a></p>
          </article>
        </div>
        <div class="cdl-17__pane cdl-17__pane--2">
          <h1>Plans</h1>
          <div class="cdl-17__row cdl-17__row--3">
            <article class="cdl-17__card"><h3>Starter</h3><p class="cdl-17__big">$0</p><small>2 seats · 2k minutes</small><button type="button" class="cdl-17__ghost">Downgrade</button></article>
            <article class="cdl-17__card cdl-17__now"><h3>Team</h3><p class="cdl-17__big">$96</p><small>10 seats · 20k minutes</small><button type="button" class="cdl-17__ghost" aria-pressed="true">Current plan</button></article>
            <article class="cdl-17__card"><h3>Scale</h3><p class="cdl-17__big">$290</p><small>25 seats · 80k minutes</small><button type="button" class="cdl-17__cta">Upgrade</button></article>
          </div>
        </div>
        <div class="cdl-17__pane cdl-17__pane--3">
          <h1>Danger zone</h1>
          <article class="cdl-17__card cdl-17__danger"><h3>Cancel subscription</h3><p class="cdl-17__note">Billing stops at cycle end; data is retained for 90 days.</p><button type="button" class="cdl-17__red">Cancel plan…</button></article>
          <article class="cdl-17__card cdl-17__danger"><h3>Delete organization</h3><p class="cdl-17__note">Permanently removes acme-inc, its repos and audit history.</p><button type="button" class="cdl-17__red">Delete organization…</button></article>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-17,
.cdl-17 *,
.cdl-17 *::before,
.cdl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-17 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.98 0.003 250);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.008 250);
  --ink: oklch(0.24 0.015 250);
  --mut: oklch(0.52 0.015 250);
  --acc: oklch(0.55 0.16 255);
  --red: oklch(0.55 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-17__page {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--edge);
  overflow: hidden;
  background: var(--bg);
}

.cdl-17__bar {
  flex: none;
  display: flex;
  align-items: center;
  gap: 14px;
  height: 54px;
  padding: 0 18px;
  background: oklch(0.21 0.02 255);
  color: oklch(0.95 0.005 250);
}

.cdl-17__logo {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: conic-gradient(from 200deg,var(--acc),oklch(0.75 0.12 200));
}

.cdl-17__crumbs {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13.5px;
}

.cdl-17__crumbs a {
  color: oklch(0.8 0.02 250);
  text-decoration: none;
  font-weight: 600;
}

.cdl-17__crumbs a:hover {
  color: oklch(0.98 0 0);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cdl-17__crumbs a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 3px;
}

.cdl-17__crumbs i {
  font-style: normal;
  opacity: .45;
}

.cdl-17__crumbs b {
  font-weight: 700;
}

.cdl-17__search {
  margin-left: auto;
  font-size: 12px;
  color: oklch(0.72 0.015 250);
  border: 1px solid oklch(0.35 0.02 255);
  border-radius: 8px;
  padding: 6px 10px;
  display: flex;
  gap: 10px;
  align-items: center;
}

.cdl-17__search kbd {
  font: 600 10px ui-monospace,Menlo,Consolas,monospace;
  border: 1px solid oklch(0.4 0.02 255);
  border-radius: 4px;
  padding: 1px 6px;
}

.cdl-17__me {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 10.5px;
  font-weight: 700;
  background: linear-gradient(140deg,var(--acc),oklch(0.6 0.15 300));
}

.cdl-17__scroll {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  display: flex;
  flex-direction: column;
}

.cdl-17__tabs {
  position: sticky;
  top: 0;
  z-index: 2;
  background: color-mix(in oklch,var(--bg) 82%,transparent);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--edge);
}

.cdl-17__tabrow {
  width: min(100% - 48px,920px);
  margin-inline: auto;
  display: flex;
  gap: 4px;
}

.cdl-17__tab {
  position: relative;
  cursor: pointer;
}

.cdl-17__tab input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cdl-17__tab span {
  display: block;
  padding: 13px 14px 11px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--mut);
  border-radius: 8px 8px 0 0;
  transition: color .15s,background .15s;
}

.cdl-17__tab:hover span {
  color: var(--ink);
  background: oklch(0.945 0.006 250);
}

.cdl-17__tab:has(:focus-visible) span {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-17__tab::after {
  content: "";
  position: absolute;
  left: 8px;
  right: 8px;
  bottom: -1px;
  height: 2.5px;
  border-radius: 3px;
  background: var(--acc);
  scale: 0 1;
  transition: scale .25s cubic-bezier(.2,.7,.2,1);
}

.cdl-17__tab:has(:checked) span {
  color: var(--ink);
}

.cdl-17__tab:has(:checked)::after {
  scale: 1 1;
}

.cdl-17__content {
  width: min(100% - 48px,920px);
  margin-inline: auto;
  padding: 22px 0 28px;
}

.cdl-17__pane {
  display: none;
  gap: 16px;
}

.cdl-17:has(#cdl17-t1:checked) .cdl-17__pane--1 {
  display: grid;
}

.cdl-17:has(#cdl17-t2:checked) .cdl-17__pane--2 {
  display: grid;
}

.cdl-17:has(#cdl17-t3:checked) .cdl-17__pane--3 {
  display: grid;
}

.cdl-17__pane h1 {
  font-size: 19px;
  letter-spacing: -.01em;
}

.cdl-17__row {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit,minmax(min(240px,100%),1fr));
}

.cdl-17__card {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 13px;
  padding: 17px 19px;
  display: grid;
  gap: 8px;
  align-content: start;
  justify-items: start;
}

.cdl-17__card h3 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-17__big {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.cdl-17__card small {
  font-size: 12px;
  color: var(--mut);
}

.cdl-17__now {
  border-color: color-mix(in oklch,var(--acc) 55%,var(--edge));
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--acc) 12%,transparent);
}

.cdl-17__meter {
  width: 100%;
  height: 7px;
  border-radius: 999px;
  background: oklch(0.93 0.006 250);
  overflow: hidden;
}

.cdl-17__meter i {
  display: block;
  height: 100%;
  width: var(--w);
  border-radius: inherit;
  background: linear-gradient(90deg,var(--acc),oklch(0.68 0.13 210));
}

.cdl-17__line {
  width: 100%;
  display: flex;
  align-items: baseline;
  gap: 12px;
  font-size: 13px;
  padding: 9px 0;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 55%,transparent);
}

.cdl-17__line:last-child {
  border-bottom: none;
}

.cdl-17__line b {
  font-weight: 600;
  margin-right: auto;
}

.cdl-17__line span {
  font-variant-numeric: tabular-nums;
  color: var(--mut);
}

.cdl-17__line a {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--acc);
  text-decoration: none;
}

.cdl-17__line a:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cdl-17__line a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 2px;
}

.cdl-17__ghost,
.cdl-17__cta,
.cdl-17__red {
  font: 600 12.5px 'Segoe UI',system-ui,sans-serif;
  border-radius: 9px;
  padding: 8px 14px;
  cursor: pointer;
  transition: background .15s,border-color .15s;
}

.cdl-17__ghost {
  border: 1px solid var(--edge);
  background: var(--bg);
  color: var(--ink);
}

.cdl-17__ghost:hover {
  border-color: oklch(0.75 0.02 250);
}

.cdl-17__cta {
  border: none;
  background: var(--acc);
  color: oklch(1 0 0);
}

.cdl-17__cta:hover {
  background: color-mix(in oklch,var(--acc) 87%,black);
}

.cdl-17__danger {
  border-color: color-mix(in oklch,var(--red) 35%,var(--edge));
}

.cdl-17__note {
  font-size: 12.5px;
  color: var(--mut);
  line-height: 1.5;
}

.cdl-17__red {
  border: 1px solid color-mix(in oklch,var(--red) 45%,var(--edge));
  background: color-mix(in oklch,var(--red) 7%,white);
  color: var(--red);
}

.cdl-17__red:hover {
  background: color-mix(in oklch,var(--red) 14%,white);
}

.cdl-17__ghost:focus-visible,
.cdl-17__cta:focus-visible,
.cdl-17__red:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cdl-17 * {
    transition: none !important;
  }
}
```
