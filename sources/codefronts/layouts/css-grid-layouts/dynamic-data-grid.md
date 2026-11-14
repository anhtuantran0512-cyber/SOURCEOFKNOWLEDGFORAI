---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/dynamic-data-grid/"
title: "Dynamic Data Grid"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A dashboard data table built on grid + subgrid: the header defines the column tracks once, and every row inherits them with grid-template-columns: subgrid —…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Data Grid
Source: https://codefronts.com/layouts/css-grid-layouts/dynamic-data-grid/

A dashboard data table built on grid + subgrid: the header defines the column tracks once, and every row inherits them with grid-template-columns: subgrid — so columns resize gracefully as one unit, numeric columns stay right-aligned, and status pills never wrap the layout. The upgrade path from <table> styling pain.
## HTML
```html
<section class="cgl-05" aria-label="Dynamic data grid demo">
  <div class="cgl-05__table" role="table" aria-label="Deploy activity">
    <div class="cgl-05__row cgl-05__row--head" role="row">
      <span role="columnheader">Service</span><span role="columnheader" class="cgl-05__num">Requests</span><span role="columnheader" class="cgl-05__num">p95 ms</span><span role="columnheader" class="cgl-05__num">Error rate</span><span role="columnheader">Status</span>
    </div>
    <div class="cgl-05__row" role="row">
      <span role="cell">edge-gateway</span><span role="cell" class="cgl-05__num">1,204,118</span><span role="cell" class="cgl-05__num">184</span><span role="cell" class="cgl-05__num">0.02%</span><span role="cell"><em class="cgl-05__pill cgl-05__pill--ok">Healthy</em></span>
    </div>
    <div class="cgl-05__row" role="row">
      <span role="cell">auth-service</span><span role="cell" class="cgl-05__num">386,402</span><span role="cell" class="cgl-05__num">312</span><span role="cell" class="cgl-05__num">0.14%</span><span role="cell"><em class="cgl-05__pill cgl-05__pill--warn">Degraded</em></span>
    </div>
    <div class="cgl-05__row" role="row">
      <span role="cell">billing-worker</span><span role="cell" class="cgl-05__num">92,377</span><span role="cell" class="cgl-05__num">96</span><span role="cell" class="cgl-05__num">0.00%</span><span role="cell"><em class="cgl-05__pill cgl-05__pill--ok">Healthy</em></span>
    </div>
    <div class="cgl-05__row" role="row">
      <span role="cell">search-indexer</span><span role="cell" class="cgl-05__num">14,051</span><span role="cell" class="cgl-05__num">1,240</span><span role="cell" class="cgl-05__num">2.31%</span><span role="cell"><em class="cgl-05__pill cgl-05__pill--down">Failing</em></span>
    </div>
  </div>
</section>
```
## CSS
```css
.cgl-05,
.cgl-05 *,
.cgl-05 *::before,
.cgl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-05 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.15 0.015 160);
  --txt: oklch(0.93 0.02 150);
  --dim: oklch(0.66 0.03 155);
  --grid-line: oklch(0.3 0.04 160);
  --green: oklch(0.8 0.17 150);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  background: var(--bg);
  padding: 1.4rem;
  color: var(--txt);
}

.cgl-05 .cgl-05__table {
  display: grid;
  grid-template-columns: minmax(150px,1.8fr) repeat(2,minmax(80px,1fr)) minmax(90px,1fr) minmax(84px,max-content);
  border: 1px solid var(--grid-line);
  border-radius: 12px;
  overflow: hidden;
  background: oklch(0.18 0.02 160);
}

.cgl-05 .cgl-05__row {
  grid-column: 1/-1;
  display: grid;
  grid-template-columns: subgrid;
  align-items: center;
  column-gap: 14px;
  padding-block: .7rem;
  padding-inline: 1rem;
  border-block-start: 1px solid var(--grid-line);
  font-size: .82rem;
}

.cgl-05 .cgl-05__row--head {
  border-block-start: none;
  background: oklch(0.22 0.025 160);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.cgl-05 .cgl-05__row:not(.cgl-05__row--head):hover {
  background: oklch(0.21 0.025 160);
}

.cgl-05 .cgl-05__num {
  text-align: end;
  font-variant-numeric: tabular-nums;
  color: var(--dim);
}

.cgl-05 .cgl-05__row--head .cgl-05__num {
  color: var(--dim);
}

.cgl-05 .cgl-05__pill {
  font-style: normal;
  font-size: .68rem;
  padding: .22rem .55rem;
  border-radius: 999px;
  border: 1px solid;
}

.cgl-05 .cgl-05__pill--ok {
  color: var(--green);
  border-color: color-mix(in oklab,var(--green) 45%,transparent);
  background: color-mix(in oklab,var(--green) 12%,transparent);
}

.cgl-05 .cgl-05__pill--warn {
  color: oklch(0.83 0.15 85);
  border-color: oklch(0.83 0.15 85/.45);
  background: oklch(0.83 0.15 85/.12);
}

.cgl-05 .cgl-05__pill--down {
  color: oklch(0.72 0.19 25);
  border-color: oklch(0.72 0.19 25/.45);
  background: oklch(0.72 0.19 25/.12);
}

@media (max-width: 600px) {
  .cgl-05 .cgl-05__table {
    grid-template-columns: minmax(120px,1.6fr) minmax(80px,1fr) minmax(84px,max-content);
  }

  .cgl-05 .cgl-05__row>:nth-child(3),
    .cgl-05 .cgl-05__row>:nth-child(4) {
    display: none;
  }
}

@supports not (grid-template-columns: subgrid) {
  .cgl-05 .cgl-05__row {
    grid-template-columns: minmax(150px,1.8fr) repeat(2,minmax(80px,1fr)) minmax(90px,1fr) minmax(84px,max-content);
  }
}
```

## JavaScript
```js
/* No JavaScript — one master track list; every row inherits it via grid-template-columns: subgrid. */
```
