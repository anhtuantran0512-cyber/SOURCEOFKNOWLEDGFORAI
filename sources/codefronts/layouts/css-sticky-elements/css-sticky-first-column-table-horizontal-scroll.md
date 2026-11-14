---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-first-column-table-horizontal-scroll/"
title: "CSS Sticky First Column Table Horizontal Scroll"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "Twelve months of revenue across a table too wide for any screen — with the row labels frozen at left: 0, the month headers frozen at top: 0, and the corner…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky First Column Table Horizontal Scroll
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-first-column-table-horizontal-scroll/

Twelve months of revenue across a table too wide for any screen — with the row labels frozen at left: 0, the month headers frozen at top: 0, and the corner cell frozen on BOTH axes at once. Freezing columns is identical to freezing headers, rotated 90°; the only genuinely new idea is the z-index ladder that keeps the corner above the column, the column above the rows, and a gradient edge that tells users the table slides.
## HTML
```html
<section class="cst-10" aria-label="Sticky first column with horizontal scroll demo">
  <div class="cst-10__stage">
    <header class="cst-10__head">
      <div>
        <h1>MRR by product line</h1>
        <p>FY2026, $ thousands · drag or shift-scroll sideways — labels stay frozen</p>
      </div>
      <div class="cst-10__legend"><span><i data-k="up"></i>Growing</span><span><i data-k="lump"></i>Lumpy</span></div>
    </header>
    <div class="cst-10__pane">
      <div class="cst-10__wrap" tabindex="0" role="region" aria-label="Monthly recurring revenue table, scrolls horizontally and vertically">
        <table>
          <thead><tr><th scope="col">Product line</th><th scope="col">Jan</th><th scope="col">Feb</th><th scope="col">Mar</th><th scope="col">Apr</th><th scope="col">May</th><th scope="col">Jun</th><th scope="col">Jul</th><th scope="col">Aug</th><th scope="col">Sep</th><th scope="col">Oct</th><th scope="col">Nov</th><th scope="col">Dec</th><th scope="col" class="cst-10__fy">FY26</th></tr></thead>
          <tbody>
            <tr><th scope="row">Starter</th><td>12.4</td><td>12.8</td><td>13.1</td><td>13.5</td><td>13.8</td><td>14.2</td><td>14.6</td><td>15.0</td><td>15.3</td><td>15.7</td><td>16.1</td><td>16.5</td><td class="cst-10__fy">173.0</td></tr>
            <tr><th scope="row">Growth</th><td>28.0</td><td>28.9</td><td>29.7</td><td>30.6</td><td>31.4</td><td>32.5</td><td>33.6</td><td>34.4</td><td>35.2</td><td>36.1</td><td>37.3</td><td>38.4</td><td class="cst-10__fy">396.1</td></tr>
            <tr><th scope="row">Scale</th><td>45.2</td><td>46.0</td><td>47.1</td><td>48.5</td><td>49.8</td><td>51.0</td><td>52.4</td><td>53.9</td><td>55.1</td><td>56.6</td><td>58.2</td><td>59.7</td><td class="cst-10__fy">623.5</td></tr>
            <tr><th scope="row">Enterprise</th><td>88.0</td><td>88.0</td><td>92.5</td><td>92.5</td><td>97.0</td><td>97.0</td><td>103.5</td><td>103.5</td><td>110.0</td><td>110.0</td><td>118.5</td><td>118.5</td><td class="cst-10__fy">1,219.0</td></tr>
            <tr><th scope="row">API add-on</th><td>6.2</td><td>6.4</td><td>6.7</td><td>7.0</td><td>7.2</td><td>7.5</td><td>7.9</td><td>8.2</td><td>8.5</td><td>8.9</td><td>9.3</td><td>9.6</td><td class="cst-10__fy">93.4</td></tr>
            <tr><th scope="row">Priority support</th><td>4.1</td><td>4.1</td><td>4.3</td><td>4.4</td><td>4.6</td><td>4.8</td><td>4.9</td><td>5.1</td><td>5.2</td><td>5.4</td><td>5.6</td><td>5.8</td><td class="cst-10__fy">58.3</td></tr>
            <tr><th scope="row">Marketplace</th><td>9.8</td><td>10.3</td><td>10.9</td><td>11.6</td><td>12.1</td><td>12.8</td><td>13.4</td><td>14.2</td><td>14.9</td><td>15.8</td><td>16.5</td><td>17.4</td><td class="cst-10__fy">159.7</td></tr>
            <tr><th scope="row" data-k="lump">Services</th><td>15.0</td><td>13.2</td><td>16.8</td><td>14.5</td><td>17.9</td><td>16.0</td><td>18.4</td><td>15.8</td><td>19.2</td><td>17.1</td><td>20.3</td><td>18.6</td><td class="cst-10__fy">202.8</td></tr>
          </tbody>
          <tfoot><tr><td>Total</td><td>208.7</td><td>209.7</td><td>221.1</td><td>222.6</td><td>233.8</td><td>235.8</td><td>248.7</td><td>250.1</td><td>263.4</td><td>265.6</td><td>281.8</td><td>284.5</td><td class="cst-10__fy">2,925.8</td></tr></tfoot>
        </table>
      </div>
    </div>
    <p class="cst-10__foot">Corner cell = <code>top: 0</code> AND <code>left: 0</code> with the highest z-index. The gradient at the column's edge is the “more under here” affordance.</p>
  </div>
</section>
```
## CSS
```css
.cst-10,
.cst-10 *,
.cst-10 *::before,
.cst-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-10 {
  --bg: oklch(0.965 0.006 165);
  --pane: oklch(1 0 0);
  --ink: oklch(0.23 0.02 190);
  --mut: oklch(0.5 0.015 190);
  --line: oklch(0.89 0.01 175);
  --acc: oklch(0.55 0.13 175);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-10__stage {
  width: 100%;
  container: cst10/inline-size;
  height: 100vh;
  height: 100svh;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: var(--bg);
  padding: clamp(14px,3cqi,28px);
}

.cst-10__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px 20px;
}

.cst-10__head h1 {
  font-size: clamp(22px,3.4cqi,30px);
  letter-spacing: -.03em;
  font-weight: 800;
}

.cst-10__head p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 3px;
}

.cst-10__legend {
  display: flex;
  gap: 16px;
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
}

.cst-10__legend span {
  display: flex;
  align-items: center;
  gap: 7px;
}

.cst-10__legend i {
  width: 10px;
  height: 10px;
  border-radius: 3px;
}

.cst-10__legend i[data-k="up"] {
  background: var(--acc);
}

.cst-10__legend i[data-k="lump"] {
  background: oklch(0.7 0.13 75);
}

.cst-10__pane {
  flex: 1;
  min-height: 0;
  border-radius: 16px;
  border: 1px solid var(--line);
  background: var(--pane);
  overflow: hidden;
  box-shadow: 0 1px 3px oklch(0.3 0.02 190/.05);
}

.cst-10__wrap {
  height: 100%;
  overflow: auto;
  scrollbar-width: thin;
  overscroll-behavior-x: contain;
}

.cst-10__wrap:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-10__wrap table {
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13px;
  min-width: 100%;
}

.cst-10__wrap thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  min-width: 84px;
  padding: 12px 14px;
  text-align: right;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--mut);
  background: var(--pane);
  box-shadow: inset 0 -1px var(--line);
  white-space: nowrap;
}

.cst-10__wrap tbody td {
  min-width: 84px;
  padding: 11px 14px;
  text-align: right;
  font-variant-numeric: tabular-nums;
  border-bottom: 1px solid color-mix(in oklch,var(--line) 55%,transparent);
  white-space: nowrap;
}

.cst-10__wrap tbody th,
.cst-10__wrap thead th:first-child,
.cst-10__wrap tfoot td:first-child {
  position: sticky;
  left: 0;
  text-align: left;
  min-width: 170px;
  background: var(--pane);
  white-space: nowrap;
}

.cst-10__wrap tbody th {
  z-index: 1;
  padding: 11px 16px;
  font-size: 13px;
  font-weight: 700;
  border-bottom: 1px solid color-mix(in oklch,var(--line) 55%,transparent);
}

.cst-10__wrap tbody th[data-k="lump"]::before {
  content: "";
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 2.5px;
  margin-right: 8px;
  background: oklch(0.7 0.13 75);
}

.cst-10__wrap tbody th:not([data-k])::before {
  content: "";
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 2.5px;
  margin-right: 8px;
  background: var(--acc);
}

.cst-10__wrap thead th:first-child {
  z-index: 3;
  text-align: left;
}

.cst-10__wrap tbody th::after,
.cst-10__wrap thead th:first-child::after,
.cst-10__wrap tfoot td:first-child::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 100%;
  width: 14px;
  background: linear-gradient(to right,oklch(0.3 0.02 190/.09),transparent);
  pointer-events: none;
}

.cst-10__wrap tbody tr:hover td,
.cst-10__wrap tbody tr:hover th {
  background: oklch(0.97 0.008 170);
}

.cst-10__wrap tfoot td {
  position: sticky;
  bottom: 0;
  z-index: 2;
  padding: 12px 14px;
  text-align: right;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  background: var(--pane);
  box-shadow: inset 0 1px var(--line);
  white-space: nowrap;
}

.cst-10__wrap tfoot td:first-child {
  z-index: 3;
  text-align: left;
  font-size: 12px;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.cst-10__fy {
  font-weight: 800;
  color: var(--acc);
  background: oklch(0.96 0.02 175/.6);
}

.cst-10__wrap thead th.cst-10__fy,
.cst-10__wrap tfoot td.cst-10__fy {
  background: var(--pane);
  color: var(--acc);
}

.cst-10__foot {
  font-size: 12px;
  color: var(--mut);
}

.cst-10__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  background: oklch(0.92 0.01 170);
  padding: 1px 5px;
  border-radius: 4px;
}

@container cst10 (width < 560px) {
  .cst-10__wrap tbody th,
    .cst-10__wrap thead th:first-child,
    .cst-10__wrap tfoot td:first-child {
    min-width: 120px;
  }

  .cst-10__legend {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-10 * {
    transition-duration: .01ms !important;
  }
}
```
