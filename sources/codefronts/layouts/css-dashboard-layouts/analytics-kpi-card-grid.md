---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/analytics-kpi-card-grid/"
title: "Analytics KPI Card Grid"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "One line of CSS replaces every breakpoint you were about to write: repeat(auto-fit, minmax(min(240px,100%),1fr)) flows four KPI cards into 4 → 2 → 1 columns…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Analytics KPI Card Grid
Source: https://codefronts.com/layouts/css-dashboard-layouts/analytics-kpi-card-grid/

One line of CSS replaces every breakpoint you were about to write: repeat(auto-fit, minmax(min(240px,100%),1fr)) flows four KPI cards into 4 → 2 → 1 columns purely from available space. Each card ships the full metric anatomy — label, tabular-nums value, trend delta pill, and a pure-CSS sparkline that staggers up on load. Zero media queries, zero JS; this is the header row of every analytics dashboard.
## HTML
```html
<section class="cdl-03" aria-label="KPI card grid demo">
  <div class="cdl-03__stage">
    <header class="cdl-03__head"><h2>Performance</h2><span class="cdl-03__range">Last 28 days ▾</span></header>
    <div class="cdl-03__grid">
      <article class="cdl-03__card">
        <h3>Revenue</h3>
        <p class="cdl-03__val">$86,410</p>
        <p class="cdl-03__row"><span class="cdl-03__delta cdl-03__good">▲ 12.4%</span><span class="cdl-03__vs">vs prior 28d</span></p>
        <div class="cdl-03__spark" aria-hidden="true"><i style="--i:0;--h:38%"></i><i style="--i:1;--h:52%"></i><i style="--i:2;--h:46%"></i><i style="--i:3;--h:64%"></i><i style="--i:4;--h:58%"></i><i style="--i:5;--h:78%"></i><i style="--i:6;--h:100%"></i></div>
      </article>
      <article class="cdl-03__card">
        <h3>Orders</h3>
        <p class="cdl-03__val">4,203</p>
        <p class="cdl-03__row"><span class="cdl-03__delta cdl-03__good">▲ 3.1%</span><span class="cdl-03__vs">vs prior 28d</span></p>
        <div class="cdl-03__spark" aria-hidden="true"><i style="--i:0;--h:55%"></i><i style="--i:1;--h:48%"></i><i style="--i:2;--h:66%"></i><i style="--i:3;--h:60%"></i><i style="--i:4;--h:74%"></i><i style="--i:5;--h:69%"></i><i style="--i:6;--h:88%"></i></div>
      </article>
      <article class="cdl-03__card">
        <h3>Conversion rate</h3>
        <p class="cdl-03__val">3.42%</p>
        <p class="cdl-03__row"><span class="cdl-03__delta cdl-03__bad">▼ 0.4 pts</span><span class="cdl-03__vs">vs prior 28d</span></p>
        <div class="cdl-03__spark" aria-hidden="true"><i style="--i:0;--h:82%"></i><i style="--i:1;--h:74%"></i><i style="--i:2;--h:88%"></i><i style="--i:3;--h:70%"></i><i style="--i:4;--h:64%"></i><i style="--i:5;--h:58%"></i><i style="--i:6;--h:52%"></i></div>
      </article>
      <article class="cdl-03__card">
        <h3>Avg. order value</h3>
        <p class="cdl-03__val">$20.56</p>
        <p class="cdl-03__row"><span class="cdl-03__delta cdl-03__good">▲ 5.8%</span><span class="cdl-03__vs">vs prior 28d</span></p>
        <div class="cdl-03__spark" aria-hidden="true"><i style="--i:0;--h:44%"></i><i style="--i:1;--h:58%"></i><i style="--i:2;--h:50%"></i><i style="--i:3;--h:62%"></i><i style="--i:4;--h:70%"></i><i style="--i:5;--h:66%"></i><i style="--i:6;--h:80%"></i></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-03,
.cdl-03 *,
.cdl-03 *::before,
.cdl-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-03 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.975 0.006 180);
  --panel: oklch(1 0 0);
  --edge: oklch(0.905 0.012 180);
  --ink: oklch(0.25 0.02 200);
  --mut: oklch(0.54 0.02 200);
  --acc: oklch(0.6 0.13 190);
  --good: oklch(0.55 0.14 155);
  --bad: oklch(0.58 0.19 22);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-03__stage {
  width: 100%;
  height: 100vh;
  border: 1px solid var(--edge);
  background: linear-gradient(175deg,var(--bg),oklch(0.955 0.01 180));
  padding: 22px;
}

.cdl-03__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 16px;
}

.cdl-03__head h2 {
  font-size: 17px;
  letter-spacing: -.01em;
}

.cdl-03__range {
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
  border: 1px solid var(--edge);
  background: var(--panel);
  border-radius: 999px;
  padding: 6px 12px;
}

.cdl-03__grid {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(240px,100%),1fr));
}

.cdl-03__card {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 16px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  transition: translate .2s ease,box-shadow .25s ease,border-color .25s ease;
}

.cdl-03__card:hover {
  translate: 0 -3px;
  border-color: color-mix(in oklch,var(--acc) 45%,var(--edge));
  box-shadow: 0 14px 30px -18px oklch(0.4 0.06 190 / .5);
}

.cdl-03__card h3 {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-03__val {
  font-size: clamp(24px,2.4cqi + 18px,30px);
  font-weight: 700;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.cdl-03__row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.cdl-03__delta {
  font-size: 11.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  border-radius: 999px;
  padding: 3px 9px;
}

.cdl-03__good {
  color: var(--good);
  background: color-mix(in oklch,var(--good) 13%,transparent);
}

.cdl-03__bad {
  color: var(--bad);
  background: color-mix(in oklch,var(--bad) 12%,transparent);
}

.cdl-03__vs {
  font-size: 11px;
  color: var(--mut);
}

.cdl-03__spark {
  margin-top: 10px;
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 44px;
}

.cdl-03__spark i {
  flex: 1;
  height: var(--h);
  border-radius: 3px 3px 0 0;
  background: color-mix(in oklch,var(--acc) 45%,transparent);
  transform-origin: bottom;
  animation: cdl03-rise .6s cubic-bezier(.2,.7,.2,1) backwards;
  animation-delay: calc(var(--i)*60ms);
}

.cdl-03__spark i:last-child {
  background: var(--acc);
}

@keyframes cdl03-rise {
  from {
    scale: 1 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-03 * {
    animation: none !important;
    transition: none !important;
  }
}
```
