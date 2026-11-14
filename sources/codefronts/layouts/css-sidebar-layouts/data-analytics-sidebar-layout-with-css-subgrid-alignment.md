---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/data-analytics-sidebar-layout-with-css-subgrid-alignment/"
title: "Data Analytics Sidebar Layout with CSS Subgrid Alignment"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The alignment problem every dashboard sidebar has — icons, labels of wildly different lengths, live metric values, and status badges drifting out of column —…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Analytics Sidebar Layout with CSS Subgrid Alignment
Source: https://codefronts.com/layouts/css-sidebar-layouts/data-analytics-sidebar-layout-with-css-subgrid-alignment/

The alignment problem every dashboard sidebar has — icons, labels of wildly different lengths, live metric values, and status badges drifting out of column — solved properly with grid-template-columns: subgrid. Every row inherits the SAME four tracks from the list parent, so '99.98%' under 'Uptime' and '4' under 'Alerts' sit on identical rails, no hard-coded widths anywhere.
## HTML
```html
<section class="sbl-06">
  <aside class="sbl-06__rail" aria-label="Service metrics">
    <h2 class="sbl-06__brand">ops<span>/grid</span></h2>
    <ul class="sbl-06__list">
      <li class="sbl-06__head">Core services</li>
      <li class="sbl-06__row"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="6" rx="1.5"/><rect x="3" y="13" width="18" height="6" rx="1.5"/><path d="M6.5 8h.01M6.5 16h.01"/></svg><a href="#">API gateway</a><data value="99.98">99.98%</data><span class="sbl-06__dot sbl-06__dot--ok" title="Healthy"></span></li>
      <li class="sbl-06__row"><svg viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg><a href="#">Postgres primary</a><data value="12">12ms</data><span class="sbl-06__dot sbl-06__dot--ok" title="Healthy"></span></li>
      <li class="sbl-06__row"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 3 4 14h6l-1 7 9-11h-6z"/></svg><a href="#">Job queue</a><data value="1482">1,482</data><span class="sbl-06__dot sbl-06__dot--warn" title="Degraded"></span></li>
      <li class="sbl-06__head">Observability</li>
      <li class="sbl-06__row"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><a href="#">Error rate</a><data value="0.42">0.42%</data><span class="sbl-06__dot sbl-06__dot--ok" title="Healthy"></span></li>
      <li class="sbl-06__row"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8m-4.3 11a2 2 0 0 1-3.4 0"/></svg><a href="#">Open alerts</a><data value="4">4</data><span class="sbl-06__dot sbl-06__dot--crit" title="Critical"></span></li>
    </ul>
  </aside>
  <main class="sbl-06__main"><h1>Infrastructure</h1><p>Labels, values and badges align on shared subgrid rails — inspect the value column: no fixed widths anywhere.</p></main>
</section>
```
## CSS
```css
.sbl-06,
.sbl-06 *,
.sbl-06 *::before,
.sbl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-06 {
  --panel: oklch(0.16 0.015 260);
  --ink: oklch(0.93 0.005 260);
  --mut: oklch(0.62 0.012 260);
  --line: oklch(0.27 0.015 260);
  --ok: oklch(0.75 0.17 155);
  --warn: oklch(0.8 0.15 85);
  --crit: oklch(0.66 0.21 25);
  display: grid;
  grid-template-columns: 288px 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 260);
  color: var(--ink);
}

.sbl-06__rail {
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 20px 14px;
  overflow-y: auto;
}

.sbl-06__brand {
  font: 700 15px/1 ui-monospace,Menlo,monospace;
  padding: 2px 8px 18px;
}

.sbl-06__brand span {
  color: var(--mut);
}

.sbl-06__list {
  list-style: none;
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  gap: 2px 0;
}

.sbl-06__head {
  grid-column: 1/-1;
  font: 600 10.5px/1 system-ui,sans-serif;
  text-transform: uppercase;
  letter-spacing: .09em;
  color: var(--mut);
  padding: 16px 8px 8px;
}

.sbl-06__row {
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: subgrid;
  align-items: center;
  column-gap: 11px;
  min-height: 40px;
  padding: 0 8px;
  border-radius: 9px;
  transition: background-color .15s ease;
}

.sbl-06__row:hover {
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.sbl-06__row svg {
  width: 16px;
  height: 16px;
  fill: none;
  stroke: var(--mut);
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-06__row a {
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--ink);
  text-decoration: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sbl-06__row a:focus-visible {
  outline: 2px solid var(--ok);
  outline-offset: 3px;
  border-radius: 4px;
}

.sbl-06__row data {
  font: 500 12.5px/1 ui-monospace,Menlo,monospace;
  font-variant-numeric: tabular-nums;
  color: var(--mut);
  text-align: end;
}

.sbl-06__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  justify-self: center;
}

.sbl-06__dot--ok {
  background: var(--ok);
  box-shadow: 0 0 8px color-mix(in oklab,var(--ok) 60%,transparent);
}

.sbl-06__dot--warn {
  background: var(--warn);
  box-shadow: 0 0 8px color-mix(in oklab,var(--warn) 60%,transparent);
}

.sbl-06__dot--crit {
  background: var(--crit);
  box-shadow: 0 0 8px color-mix(in oklab,var(--crit) 60%,transparent);
}

.sbl-06__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-06__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-06__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 48ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-06__row {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the <ul> owns four master tracks; every <li> is grid-template-columns:subgrid, so values and badges align across rows with no fixed widths. */
```
