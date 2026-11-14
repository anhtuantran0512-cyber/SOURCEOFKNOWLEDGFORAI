---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/data-dense-scrollable-grid-sticky-headers-and-columns/"
title: "Data-Dense Scrollable Grid (Sticky Headers & Columns)"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The spreadsheet contract, honored in 20 lines: a 10-column portfolio table scrolls both ways inside its panel while the header row stays pinned to the top,…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data-Dense Scrollable Grid (Sticky Headers & Columns)
Source: https://codefronts.com/layouts/css-dashboard-layouts/data-dense-scrollable-grid-sticky-headers-and-columns/

The spreadsheet contract, honored in 20 lines: a 10-column portfolio table scrolls both ways inside its panel while the header row stays pinned to the top, the ticker column stays frozen to the left, and the corner cell — the one that must win both fights — sits above everything with one z-index. No grid libraries, no virtual DOM: position:sticky on th/td plus a three-layer z-index ladder is the entire engine finance dashboards run on.
## HTML
```html
<section class="cdl-14" aria-label="Sticky header and column data grid demo">
  <div class="cdl-14__panel">
    <header class="cdl-14__head"><h2>Portfolio — live positions</h2><span class="cdl-14__hint">scroll ↓ and → · header and ticker stay pinned</span></header>
    <div class="cdl-14__gridwrap" tabindex="0" role="region" aria-label="Positions table, scrollable">
      <table>
        <caption class="cdl-14__sr">Live positions: price, daily change, position size, market value, profit and loss, weight, beta and 52-week range</caption>
        <thead><tr>
          <th scope="col">Ticker</th><th scope="col" class="cdl-14__num">Price</th><th scope="col" class="cdl-14__num">Δ Day</th><th scope="col" class="cdl-14__num">Δ %</th><th scope="col" class="cdl-14__num">Shares</th><th scope="col" class="cdl-14__num">Mkt value</th><th scope="col" class="cdl-14__num">P/L</th><th scope="col" class="cdl-14__num">Weight</th><th scope="col" class="cdl-14__num">Beta</th><th scope="col">52-wk range</th>
        </tr></thead>
        <tbody>
          <tr><th scope="row">NVAX</th><td class="cdl-14__num">$214.32</td><td class="cdl-14__num cdl-14__up">+3.41</td><td class="cdl-14__num cdl-14__up">+1.62%</td><td class="cdl-14__num">420</td><td class="cdl-14__num">$90,014</td><td class="cdl-14__num cdl-14__up">+$12,480</td><td class="cdl-14__num">18.2%</td><td class="cdl-14__num">1.24</td><td><span class="cdl-14__range"><i style="--p:72%"></i></span></td></tr>
          <tr><th scope="row">ARDN</th><td class="cdl-14__num">$88.10</td><td class="cdl-14__num cdl-14__dn">−1.02</td><td class="cdl-14__num cdl-14__dn">−1.14%</td><td class="cdl-14__num">1,150</td><td class="cdl-14__num">$101,315</td><td class="cdl-14__num cdl-14__up">+$8,905</td><td class="cdl-14__num">20.5%</td><td class="cdl-14__num">0.92</td><td><span class="cdl-14__range"><i style="--p:44%"></i></span></td></tr>
          <tr><th scope="row">SOLV</th><td class="cdl-14__num">$41.77</td><td class="cdl-14__num cdl-14__up">+0.66</td><td class="cdl-14__num cdl-14__up">+1.60%</td><td class="cdl-14__num">2,400</td><td class="cdl-14__num">$100,248</td><td class="cdl-14__num cdl-14__dn">−$3,120</td><td class="cdl-14__num">20.3%</td><td class="cdl-14__num">1.61</td><td><span class="cdl-14__range"><i style="--p:31%"></i></span></td></tr>
          <tr><th scope="row">HXGN</th><td class="cdl-14__num">$132.09</td><td class="cdl-14__num cdl-14__up">+2.18</td><td class="cdl-14__num cdl-14__up">+1.68%</td><td class="cdl-14__num">610</td><td class="cdl-14__num">$80,575</td><td class="cdl-14__num cdl-14__up">+$15,230</td><td class="cdl-14__num">16.3%</td><td class="cdl-14__num">1.05</td><td><span class="cdl-14__range"><i style="--p:86%"></i></span></td></tr>
          <tr><th scope="row">PLTX</th><td class="cdl-14__num">$67.45</td><td class="cdl-14__num cdl-14__dn">−0.34</td><td class="cdl-14__num cdl-14__dn">−0.50%</td><td class="cdl-14__num">890</td><td class="cdl-14__num">$60,031</td><td class="cdl-14__num cdl-14__up">+$4,010</td><td class="cdl-14__num">12.1%</td><td class="cdl-14__num">1.44</td><td><span class="cdl-14__range"><i style="--p:58%"></i></span></td></tr>
          <tr><th scope="row">QBIT</th><td class="cdl-14__num">$18.92</td><td class="cdl-14__num cdl-14__up">+0.87</td><td class="cdl-14__num cdl-14__up">+4.82%</td><td class="cdl-14__num">3,300</td><td class="cdl-14__num">$62,436</td><td class="cdl-14__num cdl-14__dn">−$1,890</td><td class="cdl-14__num">12.6%</td><td class="cdl-14__num">2.10</td><td><span class="cdl-14__range"><i style="--p:12%"></i></span></td></tr>
          <tr><th scope="row">KRYP</th><td class="cdl-14__num">$305.14</td><td class="cdl-14__num cdl-14__up">+5.22</td><td class="cdl-14__num cdl-14__up">+1.74%</td><td class="cdl-14__num">260</td><td class="cdl-14__num">$79,336</td><td class="cdl-14__num cdl-14__up">+$18,940</td><td class="cdl-14__num">16.1%</td><td class="cdl-14__num">1.35</td><td><span class="cdl-14__range"><i style="--p:68%"></i></span></td></tr>
          <tr><th scope="row">LMND</th><td class="cdl-14__num">$52.08</td><td class="cdl-14__num cdl-14__dn">−1.14</td><td class="cdl-14__num cdl-14__dn">−2.14%</td><td class="cdl-14__num">1,780</td><td class="cdl-14__num">$92,702</td><td class="cdl-14__num cdl-14__dn">−$6,410</td><td class="cdl-14__num">18.7%</td><td class="cdl-14__num">1.72</td><td><span class="cdl-14__range"><i style="--p:22%"></i></span></td></tr>
          <tr><th scope="row">MRVL</th><td class="cdl-14__num">$88.72</td><td class="cdl-14__num cdl-14__up">+0.94</td><td class="cdl-14__num cdl-14__up">+1.07%</td><td class="cdl-14__num">620</td><td class="cdl-14__num">$55,006</td><td class="cdl-14__num cdl-14__up">+$3,140</td><td class="cdl-14__num">11.1%</td><td class="cdl-14__num">1.18</td><td><span class="cdl-14__range"><i style="--p:54%"></i></span></td></tr>
          <tr><th scope="row">OCTA</th><td class="cdl-14__num">$142.55</td><td class="cdl-14__num cdl-14__dn">−2.03</td><td class="cdl-14__num cdl-14__dn">−1.40%</td><td class="cdl-14__num">340</td><td class="cdl-14__num">$48,467</td><td class="cdl-14__num cdl-14__dn">−$4,220</td><td class="cdl-14__num">9.8%</td><td class="cdl-14__num">1.42</td><td><span class="cdl-14__range"><i style="--p:38%"></i></span></td></tr>
          <tr><th scope="row">PRSM</th><td class="cdl-14__num">$28.60</td><td class="cdl-14__num cdl-14__up">+0.55</td><td class="cdl-14__num cdl-14__up">+1.96%</td><td class="cdl-14__num">2,200</td><td class="cdl-14__num">$62,920</td><td class="cdl-14__num cdl-14__up">+$5,610</td><td class="cdl-14__num">12.7%</td><td class="cdl-14__num">1.61</td><td><span class="cdl-14__range"><i style="--p:61%"></i></span></td></tr>
          <tr><th scope="row">QSAT</th><td class="cdl-14__num">$71.32</td><td class="cdl-14__num cdl-14__up">+1.87</td><td class="cdl-14__num cdl-14__up">+2.69%</td><td class="cdl-14__num">520</td><td class="cdl-14__num">$37,086</td><td class="cdl-14__num cdl-14__up">+$2,740</td><td class="cdl-14__num">7.5%</td><td class="cdl-14__num">1.09</td><td><span class="cdl-14__range"><i style="--p:48%"></i></span></td></tr>
          <tr><th scope="row">RVLR</th><td class="cdl-14__num">$14.02</td><td class="cdl-14__num cdl-14__dn">−0.28</td><td class="cdl-14__num cdl-14__dn">−1.96%</td><td class="cdl-14__num">4,400</td><td class="cdl-14__num">$61,688</td><td class="cdl-14__num cdl-14__dn">−$3,120</td><td class="cdl-14__num">12.4%</td><td class="cdl-14__num">1.88</td><td><span class="cdl-14__range"><i style="--p:19%"></i></span></td></tr>
          <tr><th scope="row">SNTX</th><td class="cdl-14__num">$96.44</td><td class="cdl-14__num cdl-14__up">+1.31</td><td class="cdl-14__num cdl-14__up">+1.38%</td><td class="cdl-14__num">480</td><td class="cdl-14__num">$46,291</td><td class="cdl-14__num cdl-14__up">+$6,830</td><td class="cdl-14__num">9.3%</td><td class="cdl-14__num">1.14</td><td><span class="cdl-14__range"><i style="--p:76%"></i></span></td></tr>
          <tr><th scope="row">TRVN</th><td class="cdl-14__num">$213.89</td><td class="cdl-14__num cdl-14__dn">−1.72</td><td class="cdl-14__num cdl-14__dn">−0.80%</td><td class="cdl-14__num">210</td><td class="cdl-14__num">$44,917</td><td class="cdl-14__num cdl-14__up">+$1,940</td><td class="cdl-14__num">9.1%</td><td class="cdl-14__num">0.98</td><td><span class="cdl-14__range"><i style="--p:52%"></i></span></td></tr>
          <tr><th scope="row">UBQT</th><td class="cdl-14__num">$8.44</td><td class="cdl-14__num cdl-14__up">+0.36</td><td class="cdl-14__num cdl-14__up">+4.45%</td><td class="cdl-14__num">5,600</td><td class="cdl-14__num">$47,264</td><td class="cdl-14__num cdl-14__dn">−$1,120</td><td class="cdl-14__num">9.6%</td><td class="cdl-14__num">2.24</td><td><span class="cdl-14__range"><i style="--p:15%"></i></span></td></tr>
          <tr><th scope="row">VEDA</th><td class="cdl-14__num">$164.28</td><td class="cdl-14__num cdl-14__up">+2.41</td><td class="cdl-14__num cdl-14__up">+1.49%</td><td class="cdl-14__num">390</td><td class="cdl-14__num">$64,069</td><td class="cdl-14__num cdl-14__up">+$7,420</td><td class="cdl-14__num">13.0%</td><td class="cdl-14__num">1.06</td><td><span class="cdl-14__range"><i style="--p:82%"></i></span></td></tr>
          <tr><th scope="row">WLKN</th><td class="cdl-14__num">$45.66</td><td class="cdl-14__num cdl-14__dn">−0.61</td><td class="cdl-14__num cdl-14__dn">−1.32%</td><td class="cdl-14__num">1,320</td><td class="cdl-14__num">$60,271</td><td class="cdl-14__num cdl-14__dn">−$2,290</td><td class="cdl-14__num">12.2%</td><td class="cdl-14__num">1.51</td><td><span class="cdl-14__range"><i style="--p:34%"></i></span></td></tr>
          <tr><th scope="row">XGRN</th><td class="cdl-14__num">$29.85</td><td class="cdl-14__num cdl-14__up">+0.72</td><td class="cdl-14__num cdl-14__up">+2.47%</td><td class="cdl-14__num">2,050</td><td class="cdl-14__num">$61,193</td><td class="cdl-14__num cdl-14__up">+$4,010</td><td class="cdl-14__num">12.4%</td><td class="cdl-14__num">1.29</td><td><span class="cdl-14__range"><i style="--p:58%"></i></span></td></tr>
          <tr><th scope="row">YOTA</th><td class="cdl-14__num">$118.03</td><td class="cdl-14__num cdl-14__up">+1.55</td><td class="cdl-14__num cdl-14__up">+1.33%</td><td class="cdl-14__num">470</td><td class="cdl-14__num">$55,474</td><td class="cdl-14__num cdl-14__up">+$3,820</td><td class="cdl-14__num">11.2%</td><td class="cdl-14__num">0.87</td><td><span class="cdl-14__range"><i style="--p:67%"></i></span></td></tr>
          <tr><th scope="row">ZPHR</th><td class="cdl-14__num">$78.20</td><td class="cdl-14__num cdl-14__dn">−0.98</td><td class="cdl-14__num cdl-14__dn">−1.24%</td><td class="cdl-14__num">710</td><td class="cdl-14__num">$55,522</td><td class="cdl-14__num cdl-14__dn">−$1,540</td><td class="cdl-14__num">11.2%</td><td class="cdl-14__num">1.36</td><td><span class="cdl-14__range"><i style="--p:41%"></i></span></td></tr>
          <tr><th scope="row">AXNT</th><td class="cdl-14__num">$36.14</td><td class="cdl-14__num cdl-14__up">+0.44</td><td class="cdl-14__num cdl-14__up">+1.23%</td><td class="cdl-14__num">1,850</td><td class="cdl-14__num">$66,859</td><td class="cdl-14__num cdl-14__up">+$5,110</td><td class="cdl-14__num">13.5%</td><td class="cdl-14__num">1.17</td><td><span class="cdl-14__range"><i style="--p:55%"></i></span></td></tr>
          <tr><th scope="row">BLTZ</th><td class="cdl-14__num">$188.66</td><td class="cdl-14__num cdl-14__up">+3.12</td><td class="cdl-14__num cdl-14__up">+1.68%</td><td class="cdl-14__num">300</td><td class="cdl-14__num">$56,598</td><td class="cdl-14__num cdl-14__up">+$9,210</td><td class="cdl-14__num">11.5%</td><td class="cdl-14__num">1.22</td><td><span class="cdl-14__range"><i style="--p:73%"></i></span></td></tr>
          <tr><th scope="row">CVGT</th><td class="cdl-14__num">$52.88</td><td class="cdl-14__num cdl-14__dn">−0.71</td><td class="cdl-14__num cdl-14__dn">−1.32%</td><td class="cdl-14__num">1,140</td><td class="cdl-14__num">$60,283</td><td class="cdl-14__num cdl-14__dn">−$2,780</td><td class="cdl-14__num">12.2%</td><td class="cdl-14__num">1.44</td><td><span class="cdl-14__range"><i style="--p:29%"></i></span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-14,
.cdl-14 *,
.cdl-14 *::before,
.cdl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-14 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --panel: oklch(1 0 0);
  --bg: oklch(0.977 0.004 250);
  --edge: oklch(0.9 0.008 250);
  --ink: oklch(0.25 0.015 250);
  --mut: oklch(0.53 0.015 250);
  --acc: oklch(0.5 0.13 250);
  --up: oklch(0.52 0.13 155);
  --dn: oklch(0.55 0.18 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-14__panel {
  width: 100%;
  height: 100vh;
  border: 1px solid var(--edge);
  background: var(--panel);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.cdl-14__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding: 15px 18px;
  border-bottom: 1px solid var(--edge);
  flex-wrap: wrap;
}

.cdl-14__head h2 {
  font-size: 15px;
  letter-spacing: -.01em;
}

.cdl-14__hint {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 9%,white);
  border-radius: 999px;
  padding: 4px 11px;
}

.cdl-14__gridwrap {
  flex: 1;
  min-height: 0;
  overflow: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
  scrollbar-color: oklch(0.84 0.01 250) transparent;
}

.cdl-14__gridwrap:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-14__gridwrap table {
  border-collapse: separate;
  border-spacing: 0;
  min-width: 920px;
  width: 100%;
  font-size: 12.5px;
}

.cdl-14__gridwrap th,
.cdl-14__gridwrap td {
  padding: 10px 14px;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 60%,transparent);
  white-space: nowrap;
  background: var(--panel);
}

.cdl-14__gridwrap thead th {
  position: sticky;
  top: 0;
  z-index: 2;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
  text-align: left;
  background: var(--bg);
  border-bottom: 1px solid var(--edge);
}

.cdl-14__gridwrap tbody th {
  position: sticky;
  left: 0;
  z-index: 1;
  text-align: left;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--acc);
  width: 96px;
  min-width: 96px;
  box-shadow: inset -8px 0 8px -8px oklch(0.3 0.02 250/.25);
}

.cdl-14__gridwrap thead th:first-child {
  left: 0;
  z-index: 3;
  box-shadow: inset -8px 0 8px -8px oklch(0.3 0.02 250/.25);
}

.cdl-14__gridwrap tbody tr:nth-child(even) td,
.cdl-14__gridwrap tbody tr:nth-child(even) th {
  background: color-mix(in oklch,var(--bg) 60%,white);
}

.cdl-14__gridwrap tbody tr:hover td,
.cdl-14__gridwrap tbody tr:hover th {
  background: color-mix(in oklch,var(--acc) 6%,white);
}

.cdl-14__num {
  text-align: right !important;
  font-variant-numeric: tabular-nums;
}

.cdl-14__up {
  color: var(--up);
  font-weight: 600;
}

.cdl-14__dn {
  color: var(--dn);
  font-weight: 600;
}

.cdl-14__range {
  display: inline-block;
  width: 120px;
  height: 6px;
  border-radius: 999px;
  background: oklch(0.92 0.008 250);
  position: relative;
  vertical-align: middle;
}

.cdl-14__range i {
  position: absolute;
  top: 50%;
  left: var(--p);
  translate: -50% -50%;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--acc);
  border: 2px solid var(--panel);
  box-shadow: 0 1px 3px oklch(0 0 0/.3);
}

.cdl-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdl-14 * {
    transition: none !important;
  }
}
```
