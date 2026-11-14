---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/data-dashboard/"
title: "Brutalist Data Dashboard"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Information density over comfort: a monochrome operations dashboard with a heavy-ruled data table, a black-and-white pure-CSS bar chart and stat blocks…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Data Dashboard
Source: https://codefronts.com/design-styles/css-brutalist/data-dashboard/

Information density over comfort: a monochrome operations dashboard with a heavy-ruled data table, a black-and-white pure-CSS bar chart and stat blocks divided by 3px rules. Every number is monospace with tabular figures so columns line up to the pixel, and there is not a single rounded corner or coloured pixel in it.
## HTML
```html
<div class="brt-17">
  <input class="brt-17__sr" type="checkbox" id="brt-17-dark">
  <label class="brt-17__theme" for="brt-17-dark">
    <svg class="brt-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-17__vh">Dark theme</span>
  </label>

  <div class="brt-17__stage">
    <section class="brt-17__sheet" aria-labelledby="brt-17-h">
      <header class="brt-17__head">
        <h1 class="brt-17__h" id="brt-17-h">OPERATIONS / 12 AUG 2026</h1>
        <p class="brt-17__stamp">LAST WRITE 09:41:02 UTC · SOURCE: LEDGER-PRIMARY · ROWS 5 OF 2,914</p>
      </header>

      <ul class="brt-17__stats">
        <li class="brt-17__stat"><span class="brt-17__statl">GROSS / MTD</span><span class="brt-17__statn">48,210.40</span><span class="brt-17__statd">+12.4% MoM</span></li>
        <li class="brt-17__stat"><span class="brt-17__statl">ACTIVE ACCTS</span><span class="brt-17__statn">1,284</span><span class="brt-17__statd">+39 this week</span></li>
        <li class="brt-17__stat"><span class="brt-17__statl">FAILED CHARGES</span><span class="brt-17__statn">17</span><span class="brt-17__statd">£2,193 at risk</span></li>
        <li class="brt-17__stat"><span class="brt-17__statl">P95 LATENCY</span><span class="brt-17__statn">214 ms</span><span class="brt-17__statd">SLO 300 ms</span></li>
      </ul>

      <div class="brt-17__split">
        <section class="brt-17__chart" aria-labelledby="brt-17-ch">
          <h2 class="brt-17__sub" id="brt-17-ch">THROUGHPUT vs ERRORS / 8 WEEKS</h2>
          <ul class="brt-17__plot">
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:52"></span><span class="brt-17__bar brt-17__bar--b" style="--v:14"></span><span class="brt-17__x">W27</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:61"></span><span class="brt-17__bar brt-17__bar--b" style="--v:19"></span><span class="brt-17__x">W28</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:48"></span><span class="brt-17__bar brt-17__bar--b" style="--v:26"></span><span class="brt-17__x">W29</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:73"></span><span class="brt-17__bar brt-17__bar--b" style="--v:11"></span><span class="brt-17__x">W30</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:69"></span><span class="brt-17__bar brt-17__bar--b" style="--v:9"></span><span class="brt-17__x">W31</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:88"></span><span class="brt-17__bar brt-17__bar--b" style="--v:16"></span><span class="brt-17__x">W32</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:81"></span><span class="brt-17__bar brt-17__bar--b" style="--v:7"></span><span class="brt-17__x">W33</span></li>
            <li class="brt-17__col"><span class="brt-17__bar" style="--v:96"></span><span class="brt-17__bar brt-17__bar--b" style="--v:5"></span><span class="brt-17__x">W34</span></li>
          </ul>
          <ul class="brt-17__key">
            <li><span class="brt-17__sw" aria-hidden="true"></span>REQUESTS (10K)</li>
            <li><span class="brt-17__sw brt-17__sw--b" aria-hidden="true"></span>5XX ERRORS (100)</li>
          </ul>
        </section>

        <section class="brt-17__side" aria-labelledby="brt-17-qh">
          <h2 class="brt-17__sub" id="brt-17-qh">QUEUE DEPTH</h2>
          <ul class="brt-17__queue">
            <li><b>webhooks</b><span class="brt-17__num">1,204</span></li>
            <li><b>invoices</b><span class="brt-17__num">318</span></li>
            <li><b>exports</b><span class="brt-17__num">42</span></li>
            <li><b>emails</b><span class="brt-17__num">9</span></li>
            <li><b>dead letter</b><span class="brt-17__num">3</span></li>
          </ul>
          <p class="brt-17__warn">DEAD LETTER &gt; 0 — REVIEW REQUIRED</p>
        </section>
      </div>

      <section class="brt-17__tablewrap" aria-labelledby="brt-17-th">
        <h2 class="brt-17__sub" id="brt-17-th">LEDGER / LAST 24H</h2>
        <div class="brt-17__scroll">
          <table class="brt-17__table">
            <caption class="brt-17__vh">Ledger entries for the last 24 hours</caption>
            <thead>
              <tr><th scope="col">TIME</th><th scope="col">ACCOUNT</th><th scope="col">EVENT</th><th scope="col">PLAN</th><th scope="col" class="brt-17__num">AMOUNT</th><th scope="col">STATE</th></tr>
            </thead>
            <tbody>
              <tr><td class="brt-17__num">09:38:11</td><th scope="row">Northwind Studio</th><td>plan.upgraded</td><td>STUDIO</td><td class="brt-17__num">49.00</td><td>SETTLED</td></tr>
              <tr><td class="brt-17__num">09:12:47</td><th scope="row">Ellis &amp; Fern</th><td>charge.failed</td><td>AGENCY</td><td class="brt-17__num">129.00</td><td>RETRY 2/4</td></tr>
              <tr><td class="brt-17__num">08:55:03</td><th scope="row">Alex Chen</th><td>invoice.paid</td><td>SOLO</td><td class="brt-17__num">19.00</td><td>SETTLED</td></tr>
              <tr><td class="brt-17__num">08:31:29</td><th scope="row">Peartree Labs</th><td>seat.added</td><td>AGENCY</td><td class="brt-17__num">12.00</td><td>SETTLED</td></tr>
              <tr><td class="brt-17__num">07:44:58</td><th scope="row">Jordan Lee</th><td>trial.started</td><td>STUDIO</td><td class="brt-17__num">0.00</td><td>OPEN</td></tr>
            </tbody>
          </table>
        </div>
      </section>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-17 {
  --page: #f1f0eb;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3c3c3c;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --mono: ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--mono);
  font-size: 15px;
}

.brt-17 *,
.brt-17 *::before,
.brt-17 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-17 {
    --page: oklch(0.952 0.005 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.35 0 0);
  }
}

.brt-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-17__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
}

.brt-17__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-17__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-17__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-17__sr:focus-visible + .brt-17__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-17__sun {
  display: none;
}

.brt-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(.75rem,2.4vw,2rem);
}

.brt-17__sheet {
  inline-size: min(80rem,100%);
  background: var(--panel);
  border: 5px solid var(--edge);
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-17__head {
  padding: 1rem 1.1rem .9rem;
  padding-inline-end: 4rem;
  border-block-end: 5px solid var(--edge);
}

.brt-17__h {
  margin: 0;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  font-size: clamp(1.35rem,3.6vw,2.1rem);
  font-weight: 700;
  letter-spacing: -.02em;
}

.brt-17__stamp {
  margin: .35rem 0 0;
  font-size: .72rem;
  letter-spacing: .08em;
  color: var(--muted);
}

.brt-17__stats {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(11rem,100%),1fr));
  border-block-end: var(--bw) solid var(--edge);
}

.brt-17__stat {
  display: grid;
  gap: .15rem;
  padding: .85rem 1rem;
  border-inline-end: var(--bw) solid var(--edge);
}

.brt-17__stat:last-child {
  border-inline-end: 0;
}

.brt-17__statl {
  font-size: .68rem;
  letter-spacing: .14em;
  color: var(--muted);
}

.brt-17__statn {
  font-size: clamp(1.5rem,3.6vw,2rem);
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.brt-17__statd {
  font-size: .7rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.brt-17__split {
  display: grid;
  grid-template-columns: minmax(0,1fr);
  border-block-end: var(--bw) solid var(--edge);
}

@media (min-width: 56rem) {
  .brt-17__split {
    grid-template-columns: minmax(0,1fr) 16rem;
  }
}

.brt-17__sub {
  margin: 0 0 .8rem;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .16em;
}

.brt-17__chart {
  padding: 1rem 1.1rem 1.1rem;
}

.brt-17__plot {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: .35rem;
  block-size: clamp(8rem,20vh,12rem);
  border-block-end: var(--bw) solid var(--edge);
}

.brt-17__col {
  display: grid;
  grid-template-rows: 1fr auto;
  grid-auto-flow: column;
  align-items: end;
  column-gap: 2px;
}

.brt-17__bar {
  grid-row: 1;
  align-self: end;
  block-size: calc(var(--v) * 1%);
  background: var(--ink);
  border: 2px solid var(--edge);
}

.brt-17__bar--b {
  background: repeating-linear-gradient(45deg, var(--ink) 0 3px, var(--panel) 3px 7px);
}

.brt-17__x {
  grid-row: 2;
  grid-column: 1 / -1;
  padding-block-start: .35rem;
  font-size: .64rem;
  letter-spacing: .06em;
  text-align: center;
  color: var(--muted);
}

.brt-17__key {
  list-style: none;
  margin: .9rem 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  font-size: .68rem;
  letter-spacing: .1em;
}

.brt-17__key li {
  display: flex;
  align-items: center;
  gap: .4rem;
}

.brt-17__sw {
  inline-size: .9rem;
  block-size: .9rem;
  background: var(--ink);
  border: 2px solid var(--edge);
}

.brt-17__sw--b {
  background: repeating-linear-gradient(45deg, var(--ink) 0 3px, var(--panel) 3px 7px);
}

.brt-17__side {
  padding: 1rem 1.1rem 1.1rem;
  border-block-start: var(--bw) solid var(--edge);
}

@media (min-width: 56rem) {
  .brt-17__side {
    border-block-start: 0;
    border-inline-start: var(--bw) solid var(--edge);
  }
}

.brt-17__queue {
  list-style: none;
  margin: 0;
  padding: 0;
}

.brt-17__queue li {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding: .45rem 0;
  border-block-end: 1px solid var(--edge);
  font-size: .82rem;
}

.brt-17__queue li:first-child {
  border-block-start: 1px solid var(--edge);
}

.brt-17__queue b {
  font-weight: 400;
  letter-spacing: .04em;
}

.brt-17__num {
  font-family: var(--mono);
  font-variant-numeric: tabular-nums;
  text-align: end;
}

.brt-17__warn {
  margin: .9rem 0 0;
  padding: .4rem .5rem;
  background: var(--ink);
  color: var(--panel);
  font-size: .66rem;
  font-weight: 700;
  letter-spacing: .12em;
}

.brt-17__tablewrap {
  padding: 1rem 1.1rem 1.1rem;
}

.brt-17__scroll {
  max-block-size: 18rem;
  overflow: auto;
  border: var(--bw) solid var(--edge);
}

.brt-17__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: .8rem;
}

.brt-17__table th,
.brt-17__table td {
  padding: .5rem .6rem;
  text-align: start;
  border-block-end: 1px solid var(--edge);
  white-space: nowrap;
}

.brt-17__table thead th {
  position: sticky;
  inset-block-start: 0;
  background: var(--ink);
  color: var(--panel);
  font-size: .66rem;
  letter-spacing: .14em;
  border-block-end: var(--bw) solid var(--edge);
}

.brt-17__table thead th.brt-17__num {
  text-align: end;
}

.brt-17__table tbody tr:nth-child(even) {
  background: color-mix(in srgb, var(--ink) 4%, transparent);
}

.brt-17__table tbody th {
  font-weight: 700;
}

.brt-17__table tbody tr:hover {
  background: var(--ink);
  color: var(--panel);
}

.brt-17:has(#brt-17-dark:checked) {
  --page: #000000;
  --panel: #080808;
  --ink: #ffffff;
  --muted: #bdbdbd;
  --edge: #ffffff;
  --sh: #ffffff;
}

.brt-17:has(#brt-17-dark:checked) .brt-17__moon {
  display: none;
}

.brt-17:has(#brt-17-dark:checked) .brt-17__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-17:not(:has(#brt-17-dark:checked)) {
    --page: #000000;
    --panel: #080808;
    --ink: #ffffff;
    --muted: #bdbdbd;
    --edge: #ffffff;
    --sh: #ffffff;
  }

  .brt-17:not(:has(#brt-17-dark:checked)) .brt-17__moon {
    display: none;
  }

  .brt-17:not(:has(#brt-17-dark:checked)) .brt-17__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-17 *,
    .brt-17 *::before,
    .brt-17 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media print {
  .brt-17 {
    background: #fff;
  }

  .brt-17__sheet {
    box-shadow: none;
  }

  .brt-17__theme {
    display: none;
  }

  .brt-17__scroll {
    max-block-size: none;
    overflow: visible;
  }
}

@media (forced-colors: active) {
  .brt-17__sheet,
    .brt-17__scroll,
    .brt-17__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-17__bar {
    background: CanvasText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-17__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
