---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/pastel-dashboard-with-hard-shadows/"
title: "Pastel Dashboard with Hard Shadows"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A complete admin surface — sidebar, four stat blocks, a pure-CSS bar chart and a recent-activity table — where every panel is a bordered block sitting on its…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pastel Dashboard with Hard Shadows
Source: https://codefronts.com/design-styles/css-brutalist/pastel-dashboard-with-hard-shadows/

A complete admin surface — sidebar, four stat blocks, a pure-CSS bar chart and a recent-activity table — where every panel is a bordered block sitting on its own hard shadow. The chart bars are a grid of <div>s sized from a single --v custom property per bar, so the data lives in the markup and the CSS never changes.
## HTML
```html
<div class="brt-02">
  <input class="brt-02__sr" type="checkbox" id="brt-02-dark">
  <label class="brt-02__theme" for="brt-02-dark">
    <svg class="brt-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-02__vh">Dark theme</span>
  </label>

  <div class="brt-02__stage">
    <div class="brt-02__app">
      <aside class="brt-02__nav" aria-label="Main">
        <p class="brt-02__brand"><span class="brt-02__mark">L</span>Ledgerline</p>
        <nav>
          <ul class="brt-02__navlist">
            <li><a class="brt-02__navlink" href="#brt-02-overview" aria-current="page"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 13h6V4H4zM14 20h6V4h-6zM4 20h6v-4H4z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg><span>Overview</span></a></li>
            <li><a class="brt-02__navlink" href="#brt-02-chart"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 19V9m5 10V5m5 14v-7m5 7V8" stroke="currentColor" stroke-width="2.4" stroke-linecap="square"/></svg><span>Revenue</span></a></li>
            <li><a class="brt-02__navlink" href="#brt-02-activity"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h10" stroke="currentColor" stroke-width="2.4" stroke-linecap="square"/></svg><span>Activity</span></a></li>
            <li><a class="brt-02__navlink" href="#brt-02-activity"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="8.5" r="3.5" stroke="currentColor" stroke-width="2.2"/><path d="M5 20c1.4-3.2 4-4.8 7-4.8s5.6 1.6 7 4.8" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg><span>Customers</span></a></li>
          </ul>
        </nav>
        <div class="brt-02__quota">
          <p class="brt-02__quotal">Seats used</p>
          <p class="brt-02__quotan">17<span>/25</span></p>
        </div>
      </aside>

      <header class="brt-02__head">
        <div>
          <h1 class="brt-02__h">Overview</h1>
          <p class="brt-02__sub">Wednesday, 12 August — all figures live</p>
        </div>
        <p class="brt-02__who"><span class="brt-02__avatar" aria-hidden="true">PS</span>Priya Sharma</p>
      </header>

      <main class="brt-02__body">
        <ul class="brt-02__stats" id="brt-02-overview">
          <li class="brt-02__stat brt-02__stat--a">
            <p class="brt-02__statl">Monthly revenue</p>
            <p class="brt-02__statn">$48,210</p>
            <p class="brt-02__trend"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 16 18 8m0 0h-7m7 0v7" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg>12.4% vs July</p>
          </li>
          <li class="brt-02__stat brt-02__stat--b">
            <p class="brt-02__statl">Active accounts</p>
            <p class="brt-02__statn">1,284</p>
            <p class="brt-02__trend"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 16 18 8m0 0h-7m7 0v7" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg>3.1% vs July</p>
          </li>
          <li class="brt-02__stat brt-02__stat--c">
            <p class="brt-02__statl">Churn</p>
            <p class="brt-02__statn">1.9%</p>
            <p class="brt-02__trend brt-02__trend--down"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 8l12 8m0 0h-7m7 0V9" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg>0.4pt vs July</p>
          </li>
          <li class="brt-02__stat brt-02__stat--d">
            <p class="brt-02__statl">Open invoices</p>
            <p class="brt-02__statn">36</p>
            <p class="brt-02__trend">$21,940 outstanding</p>
          </li>
        </ul>

        <section class="brt-02__panel brt-02__panel--chart" id="brt-02-chart" aria-labelledby="brt-02-charth">
          <header class="brt-02__panelhead">
            <h2 class="brt-02__panelh" id="brt-02-charth">Revenue by month</h2>
            <p class="brt-02__panelmeta">Thousands USD</p>
          </header>
          <ul class="brt-02__chart">
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:46"></span><span class="brt-02__tick">Mar <b>22k</b></span></li>
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:58"></span><span class="brt-02__tick">Apr <b>28k</b></span></li>
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:41"></span><span class="brt-02__tick">May <b>19k</b></span></li>
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:72"></span><span class="brt-02__tick">Jun <b>35k</b></span></li>
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:85"></span><span class="brt-02__tick">Jul <b>43k</b></span></li>
            <li class="brt-02__col"><span class="brt-02__bar" style="--v:96"></span><span class="brt-02__tick">Aug <b>48k</b></span></li>
          </ul>
        </section>

        <section class="brt-02__panel" id="brt-02-activity" aria-labelledby="brt-02-acth">
          <header class="brt-02__panelhead">
            <h2 class="brt-02__panelh" id="brt-02-acth">Recent activity</h2>
            <p class="brt-02__panelmeta">Last 24 hours</p>
          </header>
          <div class="brt-02__scroll">
            <table class="brt-02__table">
              <caption class="brt-02__vh">Recent account activity, most recent first</caption>
              <thead><tr><th scope="col">Account</th><th scope="col">Event</th><th scope="col">Plan</th><th scope="col">Amount</th></tr></thead>
              <tbody>
                <tr><th scope="row">Northwind Studio</th><td>Upgraded plan</td><td>Studio</td><td>$49.00</td></tr>
                <tr><th scope="row">Alex Chen</th><td>Invoice paid</td><td>Solo</td><td>$19.00</td></tr>
                <tr><th scope="row">Peartree Labs</th><td>Seat added</td><td>Agency</td><td>$12.00</td></tr>
                <tr><th scope="row">Jordan Lee</th><td>Trial started</td><td>Studio</td><td>—</td></tr>
                <tr><th scope="row">Ellis &amp; Fern</th><td>Payment failed</td><td>Agency</td><td>$129.00</td></tr>
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-02 {
  --page: #f6f4ee;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 14px;
  --nav: 15rem;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-02 *,
.brt-02 *::before,
.brt-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-02 {
    --page: oklch(0.965 0.012 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-02__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-02__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-02__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-02__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-02__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-02__sr:focus-visible + .brt-02__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-02__sun {
  display: none;
}

.brt-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  padding: clamp(1rem,2.6vw,2rem);
  display: grid;
}

.brt-02__app {
  inline-size: min(84rem,100%);
  min-inline-size: 0;
  margin-inline: auto;
  display: grid;
  gap: clamp(.9rem,1.6vw,1.25rem);
  grid-template: 'nav head' auto 'nav body' 1fr / var(--nav) minmax(0,1fr);
}

@media (max-width: 64rem) {
  .brt-02__app {
    grid-template: 'head' auto 'nav' auto 'body' 1fr / minmax(0,1fr);
  }
}

.brt-02__nav {
  grid-area: nav;
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
  padding: 1.1rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-02__brand {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-weight: 700;
  font-size: 1.05rem;
  letter-spacing: -.01em;
}

.brt-02__mark {
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  background: var(--lilac);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 8px;
  font-size: .9rem;
}

.brt-02__navlist {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .45rem;
}

.brt-02__navlink {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: .55rem .7rem;
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
  font-size: .95rem;
  border: 2px solid transparent;
  border-radius: 9px;
  transition: translate .14s ease, box-shadow .14s ease, background .14s ease;
}

.brt-02__navlink svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.brt-02__navlink:hover {
  background: var(--butter);
  border-color: var(--edge);
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-02__navlink:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-02__navlink[aria-current="page"] {
  background: var(--ink);
  color: var(--page);
  border-color: var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
}

.brt-02__quota {
  margin-block-start: auto;
  padding: .75rem .85rem;
  background: var(--mint);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-02__quotal {
  margin: 0;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.brt-02__quotan {
  margin: .15rem 0 0;
  font-size: 1.5rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.brt-02__quotan span {
  font-size: .9rem;
  opacity: .6;
}

.brt-02__head {
  grid-area: head;
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1rem;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.15rem;
  padding-inline-end: 4rem;
  background: var(--sky);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-02__h {
  margin: 0;
  font-size: clamp(1.35rem,3vw,1.9rem);
  font-weight: 700;
  letter-spacing: -.02em;
}

.brt-02__sub {
  margin: .1rem 0 0;
  font-size: .85rem;
  font-weight: 600;
  opacity: .7;
}

.brt-02__who {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-weight: 700;
  font-size: .95rem;
}

.brt-02__avatar {
  display: grid;
  place-items: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 50%;
  font-size: .78rem;
}

.brt-02__body {
  grid-area: body;
  display: grid;
  grid-template-columns: minmax(0,1fr);
  gap: clamp(.9rem,1.6vw,1.25rem);
  align-content: start;
}

.brt-02__stats {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(.9rem,1.6vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(min(11rem,100%),1fr));
}

.brt-02__stat {
  padding: 1rem 1.1rem;
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 5px 5px 0 var(--sh);
  color: var(--on);
}

.brt-02__stat--a {
  background: var(--butter);
}

.brt-02__stat--b {
  background: var(--mint);
}

.brt-02__stat--c {
  background: var(--coral);
}

.brt-02__stat--d {
  background: var(--panel);
  color: var(--ink);
}

.brt-02__statl {
  margin: 0;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  opacity: .75;
}

.brt-02__statn {
  margin: .3rem 0 .35rem;
  font-size: clamp(1.6rem,3.4vw,2.1rem);
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.brt-02__trend {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .3rem;
  font-size: .8rem;
  font-weight: 700;
}

.brt-02__trend svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.brt-02__trend--down svg {
  color: currentColor;
}

.brt-02__panel {
  padding: 1.1rem 1.15rem 1.25rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-02__panelhead {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1rem;
  align-items: baseline;
  justify-content: space-between;
  margin-block-end: 1rem;
  padding-block-end: .75rem;
  border-block-end: var(--bw) solid var(--edge);
}

.brt-02__panelh {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.brt-02__panelmeta {
  margin: 0;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-02__chart {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: clamp(.5rem,1.4vw,1rem);
  block-size: clamp(9rem,22vh,14rem);
}

.brt-02__col {
  display: grid;
  grid-template-rows: 1fr auto;
  gap: .5rem;
  justify-items: center;
}

.brt-02__bar {
  inline-size: 100%;
  align-self: end;
  block-size: calc(var(--v) * 1%);
  border: var(--bw) solid var(--edge);
  border-radius: 6px 6px 0 0;
  box-shadow: 3px 3px 0 var(--sh);
  transform-origin: bottom center;
  animation: brt-02-grow .55s cubic-bezier(.2,.9,.2,1) both;
}

.brt-02__col:nth-child(odd) .brt-02__bar {
  background: var(--lilac);
}

.brt-02__col:nth-child(even) .brt-02__bar {
  background: var(--mint);
}

.brt-02__col:last-child .brt-02__bar {
  background: var(--coral);
}

.brt-02__col:nth-child(2) .brt-02__bar {
  animation-delay: .06s;
}

.brt-02__col:nth-child(3) .brt-02__bar {
  animation-delay: .12s;
}

.brt-02__col:nth-child(4) .brt-02__bar {
  animation-delay: .18s;
}

.brt-02__col:nth-child(5) .brt-02__bar {
  animation-delay: .24s;
}

.brt-02__col:nth-child(6) .brt-02__bar {
  animation-delay: .3s;
}

@keyframes brt-02-grow {
  from {
    scale: 1 0;
    opacity: 0;
  }

  to {
    scale: 1 1;
    opacity: 1;
  }
}

.brt-02__tick {
  font-size: .75rem;
  font-weight: 600;
  color: var(--muted);
  text-align: center;
  line-height: 1.25;
}

.brt-02__tick b {
  display: block;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.brt-02__scroll {
  max-block-size: 16rem;
  overflow: auto;
}

.brt-02__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: .92rem;
}

.brt-02__table th,
.brt-02__table td {
  text-align: start;
  padding: .7rem .6rem;
  border-block-end: 2px solid var(--edge);
}

.brt-02__table thead th {
  position: sticky;
  inset-block-start: 0;
  background: var(--panel);
  font-size: .74rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  border-block-end: var(--bw) solid var(--edge);
}

.brt-02__table tbody th {
  font-weight: 700;
}

.brt-02__table td:last-child {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
}

.brt-02__table tbody tr:hover th,
.brt-02__table tbody tr:hover td {
  background: var(--butter);
  color: var(--on);
}

.brt-02:has(#brt-02-dark:checked) {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-02:has(#brt-02-dark:checked) .brt-02__moon {
  display: none;
}

.brt-02:has(#brt-02-dark:checked) .brt-02__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-02:not(:has(#brt-02-dark:checked)) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-02:not(:has(#brt-02-dark:checked)) .brt-02__moon {
    display: none;
  }

  .brt-02:not(:has(#brt-02-dark:checked)) .brt-02__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-02 *,
    .brt-02 *::before,
    .brt-02 *::after {
    animation: none !important;
    transition: none !important;
  }

  .brt-02__bar {
    scale: 1 1;
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .brt-02__panel,
    .brt-02__stat,
    .brt-02__nav,
    .brt-02__head {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-02__navlink[aria-current="page"] {
    background: Highlight;
    color: HighlightText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-02__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
