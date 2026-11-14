---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-table-header-scrollable-div/"
title: "CSS Sticky Table Header Scrollable Div"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The admin-dashboard staple: an orders table inside an overflow: auto div whose column headers pin to the top — and, as a bonus almost nobody ships, a totals…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Table Header Scrollable Div
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-table-header-scrollable-div/

The admin-dashboard staple: an orders table inside an overflow: auto div whose column headers pin to the top — and, as a bonus almost nobody ships, a totals row pinned to the bottom. The whole thing is position: sticky on the th cells plus the one line that makes or breaks sticky tables everywhere: border-collapse: separate. Collapse mode hands cell borders to the table itself, so they scroll away and your 'sticky' header appears to shed its underline.
## HTML
```html
<section class="cst-09" aria-label="Sticky table header in scrollable div demo">
  <div class="cst-09__stage">
    <header class="cst-09__head">
      <div>
        <h1>Orders</h1>
        <p>July 2026 · <strong>16 open</strong> · header pins to the pane, totals pin to its floor</p>
      </div>
      <div class="cst-09__tools">
        <a href="#cst09-filter" aria-current="true">All</a>
        <a href="#cst09-filter">Paid</a>
        <a href="#cst09-filter">Shipped</a>
        <a href="#cst09-filter">Pending</a>
        <a class="cst-09__export" href="#cst09-export">Export CSV</a>
      </div>
    </header>
    <div class="cst-09__pane">
      <div class="cst-09__wrap" tabindex="0" role="region" aria-label="Orders table, scrollable">
        <table>
          <thead><tr><th>Order</th><th>Customer</th><th>Date</th><th>Status</th><th class="cst-09__num">Items</th><th class="cst-09__num">Total</th></tr></thead>
          <tbody>
            <tr><td>#48231</td><td>Nora Whelan</td><td>Jul 28</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">2</td><td class="cst-09__num">$129.00</td></tr>
            <tr><td>#48230</td><td>Dev Patel</td><td>Jul 28</td><td><span class="cst-09__pill" data-s="ship">Shipped</span></td><td class="cst-09__num">1</td><td class="cst-09__num">$68.50</td></tr>
            <tr><td>#48229</td><td>Lena Hoffmann</td><td>Jul 27</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">4</td><td class="cst-09__num">$342.00</td></tr>
            <tr><td>#48228</td><td>Marcus Cole</td><td>Jul 27</td><td><span class="cst-09__pill" data-s="pend">Pending</span></td><td class="cst-09__num">1</td><td class="cst-09__num">$89.99</td></tr>
            <tr><td>#48227</td><td>Yuki Tanaka</td><td>Jul 26</td><td><span class="cst-09__pill" data-s="ship">Shipped</span></td><td class="cst-09__num">5</td><td class="cst-09__num">$415.20</td></tr>
            <tr><td>#48226</td><td>Sadie Brennan</td><td>Jul 26</td><td><span class="cst-09__pill" data-s="ref">Refunded</span></td><td class="cst-09__num">1</td><td class="cst-09__num">$27.00</td></tr>
            <tr><td>#48225</td><td>Omar Haddad</td><td>Jul 25</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">2</td><td class="cst-09__num">$156.75</td></tr>
            <tr><td>#48224</td><td>Grace Liu</td><td>Jul 25</td><td><span class="cst-09__pill" data-s="ship">Shipped</span></td><td class="cst-09__num">3</td><td class="cst-09__num">$210.40</td></tr>
            <tr><td>#48223</td><td>Tom Rasmussen</td><td>Jul 24</td><td><span class="cst-09__pill" data-s="pend">Pending</span></td><td class="cst-09__num">1</td><td class="cst-09__num">$74.25</td></tr>
            <tr><td>#48222</td><td>Ines Moreau</td><td>Jul 24</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">6</td><td class="cst-09__num">$512.60</td></tr>
            <tr><td>#48221</td><td>Jack Osborne</td><td>Jul 23</td><td><span class="cst-09__pill" data-s="ship">Shipped</span></td><td class="cst-09__num">2</td><td class="cst-09__num">$96.00</td></tr>
            <tr><td>#48220</td><td>Priya Nair</td><td>Jul 23</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">3</td><td class="cst-09__num">$189.99</td></tr>
            <tr><td>#48219</td><td>Cody Mitchell</td><td>Jul 22</td><td><span class="cst-09__pill" data-s="ref">Refunded</span></td><td class="cst-09__num">1</td><td class="cst-09__num">$45.50</td></tr>
            <tr><td>#48218</td><td>Femi Adeyemi</td><td>Jul 22</td><td><span class="cst-09__pill" data-s="paid">Paid</span></td><td class="cst-09__num">4</td><td class="cst-09__num">$263.80</td></tr>
            <tr><td>#48217</td><td>Maja Lindqvist</td><td>Jul 21</td><td><span class="cst-09__pill" data-s="pend">Pending</span></td><td class="cst-09__num">2</td><td class="cst-09__num">$118.30</td></tr>
            <tr><td>#48216</td><td>Ryan Gallagher</td><td>Jul 21</td><td><span class="cst-09__pill" data-s="ship">Shipped</span></td><td class="cst-09__num">5</td><td class="cst-09__num">$379.45</td></tr>
          </tbody>
          <tfoot><tr><td colspan="4">Page total · 16 orders</td><td class="cst-09__num">43</td><td class="cst-09__num">$3,118.73</td></tr></tfoot>
        </table>
      </div>
    </div>
    <p class="cst-09__foot">The pane above is a plain <code>overflow: auto</code> div — <code>thead th</code> pins with <code>top: 0</code>, <code>tfoot td</code> with <code>bottom: 0</code>, and <code>border-collapse: separate</code> keeps the lines attached.</p>
  </div>
</section>
```
## CSS
```css
.cst-09,
.cst-09 *,
.cst-09 *::before,
.cst-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-09 {
  --bg: oklch(0.965 0.005 255);
  --pane: oklch(1 0 0);
  --ink: oklch(0.23 0.015 255);
  --mut: oklch(0.52 0.012 255);
  --line: oklch(0.9 0.007 255);
  --acc: oklch(0.55 0.17 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-09__stage {
  width: 100%;
  container: cst09/inline-size;
  height: 100vh;
  height: 100svh;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: var(--bg);
  padding: clamp(14px,3cqi,28px);
}

.cst-09__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px 20px;
}

.cst-09__head h1 {
  font-size: clamp(22px,3.4cqi,30px);
  letter-spacing: -.03em;
  font-weight: 800;
}

.cst-09__head p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 3px;
}

.cst-09__tools {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.cst-09__tools a {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 12.5px;
  font-weight: 650;
  color: var(--mut);
  text-decoration: none;
  border: 1.5px solid var(--line);
  background: var(--pane);
  transition: color .2s,border-color .2s;
}

.cst-09__tools a:hover,
.cst-09__tools a:focus-visible {
  color: var(--ink);
  border-color: oklch(0.75 0.02 255);
}

.cst-09__tools a[aria-current] {
  color: oklch(0.99 0 0);
  background: var(--ink);
  border-color: var(--ink);
}

.cst-09__tools a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-09__export {
  color: var(--acc) !important;
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line)) !important;
}

.cst-09__pane {
  flex: 1;
  min-height: 0;
  border-radius: 16px;
  border: 1px solid var(--line);
  background: var(--pane);
  overflow: hidden;
  box-shadow: 0 1px 3px oklch(0.3 0.02 255/.05);
}

.cst-09__wrap {
  height: 100%;
  overflow: auto;
  scrollbar-width: thin;
}

.cst-09__wrap:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-09__wrap table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13.5px;
}

.cst-09__wrap thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  text-align: left;
  padding: 13px 16px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
  background: var(--pane);
  box-shadow: inset 0 -1px var(--line);
}

.cst-09__wrap tbody td {
  padding: 12px 16px;
  border-bottom: 1px solid color-mix(in oklch,var(--line) 55%,transparent);
  white-space: nowrap;
}

.cst-09__wrap tbody td:first-child {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  color: var(--mut);
}

.cst-09__wrap tbody tr {
  transition: background .15s;
}

.cst-09__wrap tbody tr:hover {
  background: oklch(0.975 0.006 255);
}

.cst-09__num {
  text-align: right !important;
  font-variant-numeric: tabular-nums;
}

.cst-09__pill {
  display: inline-grid;
  place-items: center;
  min-height: 24px;
  padding: 0 10px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
}

.cst-09__pill[data-s="paid"] {
  color: oklch(0.42 0.12 155);
  background: oklch(0.93 0.05 155);
}

.cst-09__pill[data-s="ship"] {
  color: oklch(0.42 0.11 255);
  background: oklch(0.93 0.04 255);
}

.cst-09__pill[data-s="pend"] {
  color: oklch(0.5 0.12 75);
  background: oklch(0.95 0.06 85);
}

.cst-09__pill[data-s="ref"] {
  color: oklch(0.45 0.13 25);
  background: oklch(0.94 0.05 25);
}

.cst-09__wrap tfoot td {
  position: sticky;
  bottom: 0;
  z-index: 2;
  padding: 13px 16px;
  font-weight: 800;
  background: var(--pane);
  box-shadow: inset 0 1px var(--line);
}

.cst-09__wrap tfoot td:first-child {
  font-size: 12px;
  color: var(--mut);
  font-weight: 650;
}

.cst-09__foot {
  font-size: 12px;
  color: var(--mut);
}

.cst-09__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  background: oklch(0.92 0.008 255);
  padding: 1px 5px;
  border-radius: 4px;
}

@container cst09 (width < 560px) {
  .cst-09__wrap table {
    font-size: 12.5px;
  }

  .cst-09__wrap tbody td,
    .cst-09__wrap thead th,
    .cst-09__wrap tfoot td {
    padding-inline: 10px;
  }

  .cst-09__wrap tbody td:nth-child(3),
    .cst-09__wrap thead th:nth-child(3) {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-09 * {
    transition-duration: .01ms !important;
  }
}
```
