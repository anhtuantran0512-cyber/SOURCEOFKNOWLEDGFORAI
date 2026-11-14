---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/fixed-header-and-independent-scroll-panels-layout/"
title: "Fixed Header & Independent Scroll Panels Layout"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The app-shell scroll model: the frame never moves — header pinned, page scrollbar dead — while the activity feed and the deploy table scroll independently…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fixed Header & Independent Scroll Panels Layout
Source: https://codefronts.com/layouts/css-dashboard-layouts/fixed-header-and-independent-scroll-panels-layout/

The app-shell scroll model: the frame never moves — header pinned, page scrollbar dead — while the activity feed and the deploy table scroll independently inside their own panels, each with sticky section headers that shingle as you go. The whole trick is three lines developers hunt for at 2am: minmax(0,1fr) on the row, min-height:0 on the chain, overflow:auto on the panel. This demo is those three lines, labeled.
## HTML
```html
<section class="cdl-05" aria-label="Independent scroll panels demo">
  <div class="cdl-05__frame">
    <header class="cdl-05__bar">
      <strong><span class="cdl-05__logo" aria-hidden="true"></span>Opsdeck</strong>
      <nav aria-label="Primary"><a href="#activity" aria-current="page" class="cdl-05__on">Activity</a><a href="#deploys">Deploys</a><a href="#alerts">Alerts</a></nav>
      <span class="cdl-05__env">production ▾</span>
    </header>
    <div class="cdl-05__body">
      <section class="cdl-05__panel" aria-label="Activity feed">
        <h2 class="cdl-05__ph">Activity <span class="cdl-05__tag">scrolls independently ↓</span></h2>
        <div class="cdl-05__scroll" tabindex="0">
          <h3 class="cdl-05__sticky">Today</h3>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>api-eu</b> autoscaled to 12 pods <time>09:41</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>maya</b> merged <em>fix/checkout-402</em> <time>09:20</time></p>
          <p class="cdl-05__item"><i class="cdl-05__warn" aria-hidden="true"></i><b>queue-workers</b> latency above 400ms <time>08:57</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>cron</b> nightly backup verified <time>06:00</time></p>
          <h3 class="cdl-05__sticky">Yesterday</h3>
          <p class="cdl-05__item"><i class="cdl-05__bad" aria-hidden="true"></i><b>payments</b> incident #221 opened <time>18:12</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>payments</b> incident #221 resolved <time>18:44</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>tom</b> rotated API keys <time>16:03</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>web</b> cache hit rate 97.2% <time>12:30</time></p>
          <h3 class="cdl-05__sticky">Mon, Jul 27</h3>
          <p class="cdl-05__item"><i class="cdl-05__warn" aria-hidden="true"></i><b>db-01</b> slow query flagged <time>15:22</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>lena</b> invited 2 teammates <time>11:08</time></p>
          <p class="cdl-05__item"><i class="cdl-05__ok" aria-hidden="true"></i><b>api-us</b> deploy <em>v2.41.0</em> <time>09:00</time></p>
        </div>
      </section>
      <section class="cdl-05__panel" aria-label="Recent deploys">
        <h2 class="cdl-05__ph">Deploys <span class="cdl-05__tag">scrolls independently ↓</span></h2>
        <div class="cdl-05__scroll" tabindex="0">
          <table class="cdl-05__table">
            <caption class="cdl-05__sr">Recent deploys with status and duration</caption>
            <thead><tr><th scope="col">Ref</th><th scope="col">Service</th><th scope="col">Status</th><th scope="col">Time</th></tr></thead>
            <tbody>
              <tr><td>v2.41.2</td><td>api-eu</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>2m 04s</td></tr>
              <tr><td>v2.41.1</td><td>web</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>1m 41s</td></tr>
              <tr><td>v2.41.0</td><td>api-us</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>2m 12s</td></tr>
              <tr><td>v2.40.9</td><td>workers</td><td><span class="cdl-05__pill cdl-05__pbad">Rolled back</span></td><td>0m 58s</td></tr>
              <tr><td>v2.40.8</td><td>web</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>1m 39s</td></tr>
              <tr><td>v2.40.7</td><td>api-eu</td><td><span class="cdl-05__pill cdl-05__pwarn">Canary</span></td><td>3m 20s</td></tr>
              <tr><td>v2.40.6</td><td>db-migrator</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>4m 02s</td></tr>
              <tr><td>v2.40.5</td><td>web</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>1m 47s</td></tr>
              <tr><td>v2.40.4</td><td>api-us</td><td><span class="cdl-05__pill cdl-05__pok">Live</span></td><td>2m 30s</td></tr>
            </tbody>
          </table>
        </div>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-05,
.cdl-05 *,
.cdl-05 *::before,
.cdl-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-05 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.975 0.005 255);
  --panel: oklch(1 0 0);
  --edge: oklch(0.905 0.01 255);
  --ink: oklch(0.26 0.02 255);
  --mut: oklch(0.55 0.02 255);
  --acc: oklch(0.55 0.17 255);
  --ok: oklch(0.62 0.15 155);
  --warn: oklch(0.72 0.15 80);
  --bad: oklch(0.6 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cdl-05__frame {
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-rows: 56px minmax(0,1fr);
  border: 1px solid var(--edge);
  overflow: hidden;
  background: var(--bg);
}

.cdl-05__bar {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 0 18px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.cdl-05__bar strong {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.5px;
}

.cdl-05__logo {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,var(--acc),oklch(0.68 0.14 200));
}

.cdl-05__bar nav {
  display: flex;
  gap: 4px;
}

.cdl-05__bar nav a {
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  padding: 8px 13px;
  border-radius: 9px;
  transition: background .15s,color .15s;
}

.cdl-05__bar nav a:hover {
  background: oklch(0.955 0.008 255);
  color: var(--ink);
}

.cdl-05__bar nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-05__on {
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  color: var(--acc) !important;
}

.cdl-05__env {
  margin-left: auto;
  font-size: 12px;
  font-weight: 600;
  color: var(--mut);
  border: 1px solid var(--edge);
  border-radius: 999px;
  padding: 6px 12px;
  background: var(--bg);
}

.cdl-05__body {
  display: grid;
  grid-template-columns: minmax(0,1.1fr) minmax(0,1fr);
  gap: 14px;
  padding: 14px;
  min-height: 0;
}

.cdl-05__panel {
  min-height: 0;
  display: flex;
  flex-direction: column;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 13px;
  overflow: hidden;
}

.cdl-05__ph {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 13px;
  padding: 13px 16px;
  border-bottom: 1px solid var(--edge);
}

.cdl-05__tag {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 9%,transparent);
  border-radius: 999px;
  padding: 3px 9px;
}

.cdl-05__scroll {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
  scrollbar-color: oklch(0.85 0.01 255) transparent;
}

.cdl-05__scroll:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cdl-05__sticky {
  position: sticky;
  top: 0;
  z-index: 1;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 10px 16px 8px;
  background: color-mix(in oklch,var(--panel) 82%,transparent);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 60%,transparent);
}

.cdl-05__item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  padding: 11px 16px;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 45%,transparent);
}

.cdl-05__item em {
  font-style: normal;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  background: var(--bg);
  border: 1px solid var(--edge);
  border-radius: 6px;
  padding: 1px 6px;
}

.cdl-05__item time {
  margin-left: auto;
  font-size: 11px;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.cdl-05__ok,
.cdl-05__warn,
.cdl-05__bad {
  width: 8px;
  height: 8px;
  flex: none;
  border-radius: 50%;
}

.cdl-05__ok {
  background: var(--ok);
}

.cdl-05__warn {
  background: var(--warn);
}

.cdl-05__bad {
  background: var(--bad);
}

.cdl-05__table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.cdl-05__table th {
  position: sticky;
  top: 0;
  z-index: 1;
  text-align: left;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 11px 16px 9px;
  background: color-mix(in oklch,var(--panel) 88%,transparent);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid var(--edge);
}

.cdl-05__table td {
  padding: 11px 16px;
  border-bottom: 1px solid color-mix(in oklch,var(--edge) 45%,transparent);
  font-variant-numeric: tabular-nums;
}

.cdl-05__table td:first-child {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
}

.cdl-05__table tbody tr:hover {
  background: oklch(0.975 0.005 255);
}

.cdl-05__pill {
  font-size: 11px;
  font-weight: 700;
  border-radius: 999px;
  padding: 3px 10px;
}

.cdl-05__pok {
  color: var(--ok);
  background: color-mix(in oklch,var(--ok) 13%,transparent);
}

.cdl-05__pwarn {
  color: oklch(0.55 0.13 80);
  background: color-mix(in oklch,var(--warn) 18%,transparent);
}

.cdl-05__pbad {
  color: var(--bad);
  background: color-mix(in oklch,var(--bad) 11%,transparent);
}

@container (max-width: 680px) {
  .cdl-05__body {
    grid-template-columns: minmax(0,1fr);
    grid-template-rows: minmax(0,1fr) minmax(0,1fr);
  }

  .cdl-05__bar nav {
    display: none;
  }
}

.cdl-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .cdl-05 * {
    transition: none !important;
  }
}
```
