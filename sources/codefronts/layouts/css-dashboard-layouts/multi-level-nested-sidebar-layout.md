---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/multi-level-nested-sidebar-layout/"
title: "Multi-Level Nested Sidebar Layout"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The cloud-console pattern (AWS, GCP, Azure all converged on it): a slim dark icon rail for top-level sections, a secondary drawer whose contents swap with…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Level Nested Sidebar Layout
Source: https://codefronts.com/layouts/css-dashboard-layouts/multi-level-nested-sidebar-layout/

The cloud-console pattern (AWS, GCP, Azure all converged on it): a slim dark icon rail for top-level sections, a secondary drawer whose contents swap with the rail selection, and the work area. Rail selection is a radio group — :has() swaps the sub-nav lists and the breadcrumb with zero JS — and a checkbox chevron folds the whole drawer away when you know the console by heart. Three grid columns; two of them are navigation.
## HTML
```html
<section class="cdl-11" aria-label="Nested sidebar console demo">
  <div class="cdl-11__console">
    <input type="radio" name="cdl11" id="cdl11-r1" class="cdl-11__state" checked><input type="radio" name="cdl11" id="cdl11-r2" class="cdl-11__state"><input type="radio" name="cdl11" id="cdl11-r3" class="cdl-11__state"><input type="radio" name="cdl11" id="cdl11-r4" class="cdl-11__state"><input type="checkbox" id="cdl11-fold" class="cdl-11__state">
    <nav class="cdl-11__rail" aria-label="Sections">
      <span class="cdl-11__mark" aria-hidden="true"></span>
      <label class="cdl-11__ri" for="cdl11-r1" data-tip="Overview"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12 12 4l9 8"/><path d="M5 10v10h14V10"/></svg></label>
      <label class="cdl-11__ri" for="cdl11-r2" data-tip="Compute"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="5" width="14" height="14" rx="2"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg></label>
      <label class="cdl-11__ri" for="cdl11-r3" data-tip="Storage"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg></label>
      <label class="cdl-11__ri" for="cdl11-r4" data-tip="Security"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 3v6c0 4.4-3 7.4-7 9-4-1.6-7-4.6-7-9V6Z"/><path d="m9 12 2 2 4-4"/></svg></label>
      <label class="cdl-11__ri cdl-11__fold" for="cdl11-fold" data-tip="Fold panel"><svg class="cdl-11__chev" viewBox="0 0 24 24" aria-hidden="true"><path d="m14 6-6 6 6 6"/></svg></label>
    </nav>
    <div class="cdl-11__drawer">
      <div class="cdl-11__sub cdl-11__sub--1"><h2>Overview</h2><a href="#dash" aria-current="page" class="cdl-11__on">Dashboard</a><a href="#usage">Usage &amp; cost</a><a href="#quotas">Quotas</a><a href="#activity">Activity log</a></div>
      <div class="cdl-11__sub cdl-11__sub--2"><h2>Compute</h2><a href="#instances" aria-current="page" class="cdl-11__on">Instances <b>12</b></a><a href="#images">Machine images</a><a href="#groups">Instance groups</a><a href="#lb">Load balancers</a><a href="#autoscale">Autoscaling</a></div>
      <div class="cdl-11__sub cdl-11__sub--3"><h2>Storage</h2><a href="#buckets" aria-current="page" class="cdl-11__on">Buckets <b>8</b></a><a href="#disks">Disks</a><a href="#snapshots">Snapshots</a><a href="#lifecycle">Lifecycle rules</a></div>
      <div class="cdl-11__sub cdl-11__sub--4"><h2>Security</h2><a href="#iam" aria-current="page" class="cdl-11__on">IAM &amp; roles</a><a href="#keys">API keys</a><a href="#firewall">Firewall</a><a href="#audit">Audit trail</a></div>
    </div>
    <main class="cdl-11__work">
      <p class="cdl-11__crumb"><span>console</span><i aria-hidden="true">›</i><b class="cdl-11__crumbsec"></b></p>
      <div class="cdl-11__rows">
        <article><b>prod-api-01</b><span>us-east1 · e2-standard-4</span><i class="cdl-11__ok">Running</i></article>
        <article><b>prod-api-02</b><span>us-east1 · e2-standard-4</span><i class="cdl-11__ok">Running</i></article>
        <article><b>staging-worker</b><span>eu-west2 · e2-small</span><i class="cdl-11__off">Stopped</i></article>
        <article><b>batch-runner</b><span>us-central1 · c3-highcpu-8</span><i class="cdl-11__ok">Running</i></article>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.cdl-11,
.cdl-11 *,
.cdl-11 *::before,
.cdl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-11 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --rail: oklch(0.2 0.03 265);
  --drawer: oklch(0.965 0.008 265);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.012 265);
  --ink: oklch(0.26 0.02 265);
  --mut: oklch(0.55 0.02 265);
  --acc: oklch(0.62 0.17 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-11__console {
  width: 100%;
  height: 100vh;
  position: relative;
  display: grid;
  grid-template-columns: 64px 228px minmax(0,1fr);
  overflow: hidden;
  border: 1px solid var(--edge);
  background: var(--panel);
  transition: grid-template-columns .3s cubic-bezier(.2,.7,.2,1);
}

.cdl-11__console:has(#cdl11-fold:checked) {
  grid-template-columns: 64px 0px minmax(0,1fr);
}

.cdl-11__state {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cdl-11__rail {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 12px 0;
  background: var(--rail);
}

.cdl-11__mark {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  margin-bottom: 10px;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.75 0.13 200));
}

.cdl-11__ri {
  position: relative;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  color: oklch(0.7 0.02 265);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.cdl-11__ri svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.cdl-11__ri:hover {
  background: oklch(0.27 0.03 265);
  color: oklch(0.95 0 0);
}

.cdl-11__ri::before {
  content: "";
  position: absolute;
  left: -10px;
  top: 50%;
  translate: 0 -50%;
  width: 3px;
  height: 0;
  border-radius: 3px;
  background: var(--acc);
  transition: height .2s;
}

.cdl-11__ri::after {
  content: attr(data-tip);
  position: absolute;
  left: calc(100% + 12px);
  top: 50%;
  translate: 0 -50%;
  background: oklch(0.24 0.02 265);
  color: oklch(0.97 0 0);
  font-size: 11.5px;
  font-weight: 600;
  padding: 5px 10px;
  border-radius: 7px;
  white-space: nowrap;
  opacity: 0;
  scale: .9;
  pointer-events: none;
  transition: opacity .15s,scale .15s;
  z-index: 6;
}

.cdl-11__ri:hover::after {
  opacity: 1;
  scale: 1;
}

.cdl-11__console:has(#cdl11-r1:checked) [for=cdl11-r1],
.cdl-11__console:has(#cdl11-r2:checked) [for=cdl11-r2],
.cdl-11__console:has(#cdl11-r3:checked) [for=cdl11-r3],
.cdl-11__console:has(#cdl11-r4:checked) [for=cdl11-r4] {
  background: oklch(0.3 0.05 265);
  color: oklch(0.98 0 0);
}

.cdl-11__console:has(#cdl11-r1:checked) [for=cdl11-r1]::before,
.cdl-11__console:has(#cdl11-r2:checked) [for=cdl11-r2]::before,
.cdl-11__console:has(#cdl11-r3:checked) [for=cdl11-r3]::before,
.cdl-11__console:has(#cdl11-r4:checked) [for=cdl11-r4]::before {
  height: 22px;
}

.cdl-11__console:has(.cdl-11__state:focus-visible) .cdl-11__rail {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 14px;
}

.cdl-11__fold {
  margin-top: auto;
}

.cdl-11__chev {
  transition: rotate .3s;
}

.cdl-11__console:has(#cdl11-fold:checked) .cdl-11__chev {
  rotate: 180deg;
}

.cdl-11__drawer {
  min-width: 0;
  overflow: hidden;
  background: var(--drawer);
  border-right: 1px solid var(--edge);
  visibility: visible;
  transition: visibility 0s linear 0s;
}

.cdl-11__console:has(#cdl11-fold:checked) .cdl-11__drawer {
  visibility: hidden;
  transition-delay: .3s;
}

.cdl-11__sub {
  display: none;
  width: 228px;
  padding: 18px 12px;
  flex-direction: column;
  gap: 3px;
  opacity: 1;
  translate: 0 0;
  transition: opacity .35s,translate .35s;
}

@starting-style {
  .cdl-11__sub {
    opacity: 0;
    translate: 0 8px;
  }
}

.cdl-11__console:has(#cdl11-r1:checked) .cdl-11__sub--1 {
  display: flex;
}

.cdl-11__console:has(#cdl11-r2:checked) .cdl-11__sub--2 {
  display: flex;
}

.cdl-11__console:has(#cdl11-r3:checked) .cdl-11__sub--3 {
  display: flex;
}

.cdl-11__console:has(#cdl11-r4:checked) .cdl-11__sub--4 {
  display: flex;
}

.cdl-11__sub h2 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 0 10px;
  margin-bottom: 10px;
}

.cdl-11__sub a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 9px 11px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: background .15s,color .15s;
}

.cdl-11__sub a:hover {
  background: oklch(0.925 0.012 265);
  color: var(--ink);
}

.cdl-11__sub a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-11__sub a.cdl-11__on {
  background: color-mix(in oklch,var(--acc) 12%,white);
  color: color-mix(in oklch,var(--acc) 80%,black);
}

.cdl-11__sub b {
  font-size: 10.5px;
  background: var(--acc);
  color: oklch(1 0 0);
  border-radius: 999px;
  padding: 1px 7px;
}

.cdl-11__work {
  min-width: 0;
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  overflow-y: auto;
  overscroll-behavior: contain;
}

.cdl-11__crumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  color: var(--mut);
}

.cdl-11__crumb i {
  font-style: normal;
  opacity: .6;
}

.cdl-11__crumbsec {
  color: var(--ink);
}

.cdl-11__console:has(#cdl11-r1:checked) .cdl-11__crumbsec::after {
  content: "Overview";
}

.cdl-11__console:has(#cdl11-r2:checked) .cdl-11__crumbsec::after {
  content: "Compute";
}

.cdl-11__console:has(#cdl11-r3:checked) .cdl-11__crumbsec::after {
  content: "Storage";
}

.cdl-11__console:has(#cdl11-r4:checked) .cdl-11__crumbsec::after {
  content: "Security";
}

.cdl-11__rows {
  display: grid;
  gap: 10px;
}

.cdl-11__rows article {
  display: grid;
  grid-template-columns: minmax(0,1fr) auto;
  gap: 2px 12px;
  align-items: center;
  border: 1px solid var(--edge);
  border-radius: 12px;
  padding: 13px 16px;
  background: var(--panel);
  transition: border-color .15s,box-shadow .15s;
}

.cdl-11__rows article:hover {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--edge));
  box-shadow: 0 8px 20px -16px oklch(0.4 0.06 265/.6);
}

.cdl-11__rows b {
  font-size: 13.5px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.cdl-11__rows span {
  grid-column: 1;
  font-size: 11.5px;
  color: var(--mut);
}

.cdl-11__rows i {
  grid-row: 1/3;
  grid-column: 2;
  font-style: normal;
  font-size: 11px;
  font-weight: 700;
  border-radius: 999px;
  padding: 4px 11px;
}

.cdl-11__ok {
  color: oklch(0.5 0.13 155);
  background: color-mix(in oklch,oklch(0.6 0.15 155) 14%,white);
}

.cdl-11__off {
  color: var(--mut);
  background: oklch(0.93 0.008 265);
}

@container (max-width: 640px) {
  .cdl-11__console:not(:has(#cdl11-fold:checked)) {
    grid-template-columns: 64px 0px minmax(0,1fr);
  }

  .cdl-11__console:not(:has(#cdl11-fold:checked)) .cdl-11__drawer {
    visibility: hidden;
  }

  .cdl-11__console:has(#cdl11-fold:checked) {
    grid-template-columns: 64px 228px minmax(0,1fr);
  }

  .cdl-11__console:has(#cdl11-fold:checked) .cdl-11__drawer {
    visibility: visible;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-11 * {
    transition-duration: .01s !important;
  }
}
```
