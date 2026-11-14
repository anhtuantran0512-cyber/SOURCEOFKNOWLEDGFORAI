---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/fixed-first-column-data-sheet/"
title: "Fixed First Column Data Sheet"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A wide financial balance sheet with a sticky first column and scrollable remaining columns, separated by a deep box-shadow \"slide-under\" effect — no…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fixed First Column Data Sheet
Source: https://codefronts.com/snippets/css-table-styles/fixed-first-column-data-sheet/

A wide financial balance sheet with a sticky first column and scrollable remaining columns, separated by a deep box-shadow "slide-under" effect — no JavaScript, no wrapper tricks.
## HTML
```html
<div class="ct-07">
  <div class="ct-07__topbar">
    <div class="ct-07__heading">📊 Revenue Balance Sheet — FY 2025</div>
    <div class="ct-07__hint">Scroll horizontally</div>
  </div>
  <div class="ct-07__outer">
    <div class="ct-07__scroll">
      <table>
        <thead>
          <tr>
            <th>Product Line</th>
            <th>Jan</th><th>Feb</th><th>Mar</th>
            <th>Q1 Total</th>
            <th>Apr</th><th>May</th><th>Jun</th>
            <th>Q2 Total</th>
            <th>Jul</th><th>Aug</th><th>Sep</th>
            <th>Q3 Total</th>
            <th>YTD</th>
            <th>vs. Target</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Cloud Storage API</td>
            <td>$148K</td><td>$162K</td><td>$178K</td>
            <td class="ct-07__total-col">$488K</td>
            <td>$195K</td><td>$210K</td><td>$224K</td>
            <td class="ct-07__total-col">$629K</td>
            <td>$238K</td><td>$251K</td><td>$267K</td>
            <td class="ct-07__total-col">$756K</td>
            <td style="font-weight:800">$1.87M</td>
            <td><span class="ct-07__pill ct-07__pill--up">▲ +12%</span></td>
          </tr>
          <tr>
            <td>AI Inference Engine</td>
            <td>$82K</td><td>$94K</td><td>$110K</td>
            <td class="ct-07__total-col">$286K</td>
            <td>$128K</td><td>$145K</td><td>$162K</td>
            <td class="ct-07__total-col">$435K</td>
            <td>$180K</td><td>$198K</td><td>$220K</td>
            <td class="ct-07__total-col">$598K</td>
            <td style="font-weight:800">$1.32M</td>
            <td><span class="ct-07__pill ct-07__pill--up">▲ +34%</span></td>
          </tr>
          <tr>
            <td>Analytics Dashboard</td>
            <td>$61K</td><td>$59K</td><td>$63K</td>
            <td class="ct-07__total-col">$183K</td>
            <td>$58K</td><td>$60K</td><td>$55K</td>
            <td class="ct-07__total-col">$173K</td>
            <td>$49K</td><td>$52K</td><td>$48K</td>
            <td class="ct-07__total-col">$149K</td>
            <td style="font-weight:800">$505K</td>
            <td><span class="ct-07__pill ct-07__pill--dn">▼ −8%</span></td>
          </tr>
          <tr>
            <td>Auth & Identity</td>
            <td>$40K</td><td>$42K</td><td>$45K</td>
            <td class="ct-07__total-col">$127K</td>
            <td>$47K</td><td>$50K</td><td>$53K</td>
            <td class="ct-07__total-col">$150K</td>
            <td>$55K</td><td>$58K</td><td>$61K</td>
            <td class="ct-07__total-col">$174K</td>
            <td style="font-weight:800">$451K</td>
            <td><span class="ct-07__pill ct-07__pill--up">▲ +5%</span></td>
          </tr>
          <tr>
            <td>Edge CDN</td>
            <td>$32K</td><td>$29K</td><td>$31K</td>
            <td class="ct-07__total-col">$92K</td>
            <td>$33K</td><td>$31K</td><td>$28K</td>
            <td class="ct-07__total-col">$92K</td>
            <td>$26K</td><td>$24K</td><td>$22K</td>
            <td class="ct-07__total-col">$72K</td>
            <td style="font-weight:800">$256K</td>
            <td><span class="ct-07__pill ct-07__pill--dn">▼ −18%</span></td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>Grand Total</td>
            <td>$363K</td><td>$386K</td><td>$427K</td>
            <td class="ct-07__total-col" style="font-size:13px">$1.18M</td>
            <td>$461K</td><td>$496K</td><td>$522K</td>
            <td class="ct-07__total-col" style="font-size:13px">$1.48M</td>
            <td>$548K</td><td>$583K</td><td>$618K</td>
            <td class="ct-07__total-col" style="font-size:13px">$1.75M</td>
            <td style="font-size:14px;color:var(--blue)">$4.40M</td>
            <td><span class="ct-07__pill ct-07__pill--up">▲ +11%</span></td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</div>
```
## CSS
```css
.ct-07,
.ct-07 *,
.ct-07 *::before,
.ct-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-07 ::selection {
  background: #3b82f6;
  color: #fff;
}

.ct-07 {
  --bg: #0a0e1a;
  --surface: #0f1624;
  --surface2: #151d2e;
  --border: #1e2d42;
  --fixed-bg: #0d1525;
  --fixed-shadow: rgba(0,0,0,0.8);
  --text: #d8e4f0;
  --muted: #4d6280;
  --blue: #3b82f6;
  --green: #10b981;
  --red: #ef4444;
  --yellow: #f59e0b;
  --header-text: #8ba3c0;
  font-family: 'Segoe UI', monospace, system-ui;
  background: var(--bg);
  padding: 28px 20px;
  min-height: 100vh;
  color: var(--text);
}

.ct-07__topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 10px;
}

.ct-07__heading {
  font-size: 17px;
  font-weight: 700;
}

.ct-07__hint {
  font-size: 12px;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 6px;
}

.ct-07__hint::before {
  content: '←→';
  background: var(--surface2);
  border: 1px solid var(--border);
  padding: 3px 8px;
  border-radius: 5px;
  font-size: 11px;
}

.ct-07__outer {
  border: 1px solid var(--border);
  border-radius: 14px;
  overflow: hidden;
  position: relative;
}
/* Scroll container – only the inner wrap scrolls */

.ct-07__scroll {
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--border) transparent;
}

.ct-07__scroll::-webkit-scrollbar {
  height: 6px;
}

.ct-07__scroll::-webkit-scrollbar-track {
  background: transparent;
}

.ct-07__scroll::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: 3px;
}

.ct-07 table {
  border-collapse: collapse;
  width: max-content;
  min-width: 100%;
}
/* FIXED FIRST COLUMN */

.ct-07 th:first-child,
.ct-07 td:first-child {
  position: sticky;
  left: 0;
  z-index: 3;
  background: var(--fixed-bg);
  min-width: 160px;
  max-width: 200px;
  /* Shadow on the right to indicate scrollable content under it */
  box-shadow: 4px 0 16px var(--fixed-shadow), 2px 0 0 var(--border);
}

.ct-07 th:first-child {
  z-index: 4;
}
/* HEAD */

.ct-07 thead tr {
  position: sticky;
  top: 0;
  z-index: 3;
  background: var(--surface2);
  border-bottom: 2px solid var(--border);
}

.ct-07 thead th {
  padding: 12px 18px;
  text-align: right;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--header-text);
  white-space: nowrap;
  min-width: 120px;
}

.ct-07 thead th:first-child {
  text-align: left;
}
/* BODY */

.ct-07 tbody tr {
  border-bottom: 1px solid var(--border);
  transition: background 0.15s;
}

.ct-07 tbody tr:last-child {
  border-bottom: none;
}

.ct-07 tbody tr:hover td {
  background: rgba(59,130,246,0.04) !important;
}

.ct-07 tbody tr:hover td:first-child {
  background: rgba(59,130,246,0.08) !important;
}

.ct-07 tbody td {
  padding: 13px 18px;
  font-size: 13px;
  text-align: right;
  white-space: nowrap;
  vertical-align: middle;
  transition: background 0.15s;
}

.ct-07 tbody td:first-child {
  text-align: left;
  font-weight: 700;
  font-size: 13px;
  color: var(--blue);
}

.ct-07__pos {
  color: var(--green);
  font-weight: 700;
}

.ct-07__neg {
  color: var(--red);
  font-weight: 700;
}

.ct-07__neutral {
  color: var(--muted);
}
/* Growth indicator pill */

.ct-07__pill {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 5px;
}

.ct-07__pill--up {
  background: rgba(16,185,129,0.12);
  color: var(--green);
}

.ct-07__pill--dn {
  background: rgba(239,68,68,0.12);
  color: var(--red);
}
/* Quarter TOTAL column highlight */

.ct-07 tbody td.ct-07__total-col {
  color: var(--text);
  font-weight: 800;
  background: rgba(59,130,246,0.06);
  border-left: 2px solid rgba(59,130,246,0.2);
}
/* TOTALS ROW */

.ct-07 tfoot tr {
  background: var(--surface2);
  border-top: 2px solid var(--border);
}

.ct-07 tfoot td {
  padding: 12px 18px;
  font-size: 12px;
  font-weight: 700;
  text-align: right;
  color: var(--text);
  white-space: nowrap;
}

.ct-07 tfoot td:first-child {
  text-align: left;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .ct-07 tbody tr,
    .ct-07 tbody td {
    transition: none;
  }
}
```
