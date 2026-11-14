---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/dashboard-skeleton/"
title: "Dashboard Skeleton"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The full admin-app frame: pinned sidebar, topbar with search, a 4-up KPI strip, main chart area with side panel — every region a named grid area, nested…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard Skeleton
Source: https://codefronts.com/layouts/css-grid-layouts/dashboard-skeleton/

The full admin-app frame: pinned sidebar, topbar with search, a 4-up KPI strip, main chart area with side panel — every region a named grid area, nested grids for the widgets, and the exact overflow discipline that keeps app shells from growing phantom scrollbars.
## HTML
```html
<section class="cgl-16" aria-label="Dashboard skeleton demo">
  <div class="cgl-16__app">
    <nav class="cgl-16__rail" aria-label="App navigation">
      <strong class="cgl-16__logo">◮ Vantage</strong>
      <a href="#0" class="is-active">Overview</a><a href="#0">Revenue</a><a href="#0">Customers</a><a href="#0">Settings</a>
    </nav>
    <header class="cgl-16__top"><span class="cgl-16__search">⌕ Search anything…</span><span class="cgl-16__avatar" aria-label="Account: A. Rivera">AR</span></header>
    <main class="cgl-16__body">
      <div class="cgl-16__kpis">
        <article class="cgl-16__kpi"><span>MRR</span><strong>$84.2k</strong><em>+6.1%</em></article>
        <article class="cgl-16__kpi"><span>Active users</span><strong>12,406</strong><em>+2.4%</em></article>
        <article class="cgl-16__kpi"><span>Churn</span><strong>1.9%</strong><em class="is-down">−0.3pt</em></article>
        <article class="cgl-16__kpi"><span>NPS</span><strong>61</strong><em>+4</em></article>
      </div>
      <div class="cgl-16__split">
        <article class="cgl-16__chartcard"><h4>Weekly revenue</h4>
          <div class="cgl-16__chart" role="img" aria-label="Bar chart: revenue rising across 12 weeks">
            <i style="--v:35%"></i><i style="--v:48%"></i><i style="--v:42%"></i><i style="--v:60%"></i><i style="--v:55%"></i><i style="--v:70%"></i><i style="--v:64%"></i><i style="--v:78%"></i><i style="--v:72%"></i><i style="--v:88%"></i><i style="--v:82%"></i><i style="--v:96%"></i>
          </div>
        </article>
        <aside class="cgl-16__panel"><h4>Activity</h4><p>Nested grid, own scroll if needed — the shell never moves.</p><p>Only the body region owns overflow-y.</p></aside>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.cgl-16,
.cgl-16 *,
.cgl-16 *::before,
.cgl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-16 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.16 0.02 255);
  --panel: oklch(0.2 0.025 255);
  --line: oklch(0.3 0.03 255);
  --txt: oklch(0.93 0.01 250);
  --dim: oklch(0.65 0.02 250);
  --blue: oklch(0.72 0.14 240);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  color: var(--txt);
  padding: 1.2rem;
}

.cgl-16 .cgl-16__app {
  display: grid;
  grid-template-areas: "rail top" "rail body";
  grid-template-columns: 170px minmax(0,1fr);
  grid-template-rows: auto minmax(0,1fr);
  block-size: 420px;
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
}

.cgl-16 .cgl-16__rail {
  grid-area: rail;
  background: oklch(0.13 0.02 255);
  border-inline-end: 1px solid var(--line);
  padding: 1rem .7rem;
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.cgl-16 .cgl-16__logo {
  font-size: .9rem;
  color: var(--blue);
  margin-block-end: 1rem;
  padding-inline: .5rem;
}

.cgl-16 .cgl-16__rail a {
  font-size: .8rem;
  color: var(--dim);
  text-decoration: none;
  padding: .5rem .6rem;
  border-radius: 8px;
  min-block-size: 2.2rem;
  display: flex;
  align-items: center;
}

.cgl-16 .cgl-16__rail a:hover {
  color: var(--txt);
  background: var(--panel);
}

.cgl-16 .cgl-16__rail a.is-active {
  color: var(--txt);
  background: color-mix(in oklab,var(--blue) 18%,transparent);
}

.cgl-16 .cgl-16__rail a:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

.cgl-16 .cgl-16__top {
  grid-area: top;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .7rem 1rem;
  border-block-end: 1px solid var(--line);
  background: var(--panel);
}

.cgl-16 .cgl-16__search {
  font-size: .78rem;
  color: var(--dim);
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: .45rem .8rem;
  flex: 1;
  max-inline-size: 280px;
}

.cgl-16 .cgl-16__avatar {
  inline-size: 32px;
  block-size: 32px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: .68rem;
  font-weight: 700;
  background: var(--blue);
  color: oklch(0.15 0.03 255);
}

.cgl-16 .cgl-16__body {
  grid-area: body;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cgl-16 .cgl-16__kpis {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(120px,100%),1fr));
  gap: 10px;
}

.cgl-16 .cgl-16__kpi {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 11px;
  padding: .7rem .8rem;
  display: flex;
  flex-direction: column;
  gap: .15rem;
}

.cgl-16 .cgl-16__kpi span {
  font-size: .64rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--dim);
}

.cgl-16 .cgl-16__kpi strong {
  font-size: 1.25rem;
  font-variant-numeric: tabular-nums;
}

.cgl-16 .cgl-16__kpi em {
  font-style: normal;
  font-size: .68rem;
  color: oklch(0.78 0.16 150);
}

.cgl-16 .cgl-16__kpi em.is-down {
  color: oklch(0.72 0.17 25);
}

.cgl-16 .cgl-16__split {
  display: grid;
  grid-template-columns: minmax(0,2fr) minmax(0,1fr);
  gap: 10px;
}

.cgl-16 .cgl-16__chartcard,
.cgl-16 .cgl-16__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 11px;
  padding: .9rem;
}

.cgl-16 h4 {
  font-size: .82rem;
  margin-block-end: .7rem;
}

.cgl-16 .cgl-16__chart {
  display: grid;
  grid-template-columns: repeat(12,1fr);
  align-items: end;
  gap: 5px;
  block-size: 110px;
}

.cgl-16 .cgl-16__chart i {
  block-size: var(--v);
  background: linear-gradient(180deg,var(--blue),color-mix(in oklab,var(--blue) 45%,var(--bg)));
  border-radius: 3px 3px 0 0;
}

.cgl-16 .cgl-16__panel p {
  font-size: .75rem;
  line-height: 1.6;
  color: var(--dim);
  margin-block-end: .5rem;
}

@media (max-width: 640px) {
  .cgl-16 .cgl-16__app {
    grid-template-areas: "top" "body";
    grid-template-columns: minmax(0,1fr);
  }

  .cgl-16 .cgl-16__rail {
    display: none;
  }

  .cgl-16 .cgl-16__split {
    grid-template-columns: minmax(0,1fr);
  }
}
```

## JavaScript
```js
/* No JavaScript — two-level nested grids: shell chrome via named areas, widgets via RAM + an align-items:end bar chart. */
```
