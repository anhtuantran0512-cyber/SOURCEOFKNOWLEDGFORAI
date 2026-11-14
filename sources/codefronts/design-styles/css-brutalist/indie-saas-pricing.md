---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/indie-saas-pricing/"
title: "Brutalist Indie SaaS Pricing"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Three plans as bordered monochrome blocks with no hierarchy trickery — no scaling, no colour, no badge glow."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Indie SaaS Pricing
Source: https://codefronts.com/design-styles/css-brutalist/indie-saas-pricing/

Three plans as bordered monochrome blocks with no hierarchy trickery — no scaling, no colour, no badge glow. The recommended plan is simply filled black. Prices are oversized in the system UI font, features are a plain bulleted list, and a comparison table below states everything the blocks leave out.
## HTML
```html
<div class="brt-19">
  <input class="brt-19__sr" type="checkbox" id="brt-19-dark">
  <label class="brt-19__theme" for="brt-19-dark">
    <svg class="brt-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-19__vh">Dark theme</span>
  </label>

  <div class="brt-19__stage">
    <section class="brt-19__wrap" aria-labelledby="brt-19-h">
      <header class="brt-19__head">
        <h1 class="brt-19__h" id="brt-19-h">PRICING</h1>
        <p class="brt-19__meta">Three plans. One product. No sales calls, no seat minimums, no annual lock-in. VAT added at checkout where applicable.</p>
      </header>

      <ul class="brt-19__plans">
        <li class="brt-19__plan">
          <h2 class="brt-19__tier">HOBBY</h2>
          <p class="brt-19__price"><span class="brt-19__cur">$</span>9<span class="brt-19__per">per month</span></p>
          <p class="brt-19__for">For one person shipping side projects.</p>
          <ul class="brt-19__feat">
            <li>3 projects</li>
            <li>25 GB bandwidth</li>
            <li>Community forum</li>
            <li>Weekly backups</li>
          </ul>
          <button class="brt-19__cta" type="button">CHOOSE HOBBY</button>
        </li>

        <li class="brt-19__plan brt-19__plan--rec">
          <h2 class="brt-19__tier">STANDARD <span class="brt-19__rec">RECOMMENDED</span></h2>
          <p class="brt-19__price"><span class="brt-19__cur">$</span>29<span class="brt-19__per">per month</span></p>
          <p class="brt-19__for">For freelancers with paying clients.</p>
          <ul class="brt-19__feat">
            <li>25 projects</li>
            <li>500 GB bandwidth</li>
            <li>Email support, 1 business day</li>
            <li>Hourly backups, 30-day restore</li>
            <li>Custom domains, unlimited</li>
          </ul>
          <button class="brt-19__cta" type="button">CHOOSE STANDARD</button>
        </li>

        <li class="brt-19__plan">
          <h2 class="brt-19__tier">STUDIO</h2>
          <p class="brt-19__price"><span class="brt-19__cur">$</span>79<span class="brt-19__per">per month</span></p>
          <p class="brt-19__for">For a small team with shared billing.</p>
          <ul class="brt-19__feat">
            <li>Unlimited projects</li>
            <li>2 TB bandwidth</li>
            <li>10 members, shared billing</li>
            <li>Audit log, SSO</li>
            <li>Uptime SLA, 99.9%</li>
          </ul>
          <button class="brt-19__cta" type="button">CHOOSE STUDIO</button>
        </li>
      </ul>

      <section class="brt-19__compare" aria-labelledby="brt-19-ch">
        <h2 class="brt-19__ch" id="brt-19-ch">WHAT THE BLOCKS LEAVE OUT</h2>
        <div class="brt-19__scroll">
          <table class="brt-19__table">
            <thead><tr><th scope="col">Feature</th><th scope="col">Hobby</th><th scope="col">Standard</th><th scope="col">Studio</th></tr></thead>
            <tbody>
              <tr><th scope="row">Deploy previews</th><td>—</td><td>YES</td><td>YES</td></tr>
              <tr><th scope="row">Password-protected sites</th><td>—</td><td>YES</td><td>YES</td></tr>
              <tr><th scope="row">Data export, self-serve</th><td>YES</td><td>YES</td><td>YES</td></tr>
              <tr><th scope="row">Invoice billing</th><td>—</td><td>—</td><td>YES</td></tr>
              <tr><th scope="row">Log retention</th><td>7 days</td><td>30 days</td><td>1 year</td></tr>
            </tbody>
          </table>
        </div>
        <p class="brt-19__note">Cancel from the dashboard at any time. We prorate to the day and refund the difference.</p>
      </section>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-19 {
  --page: #f1f0ec;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3a3a3a;
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
  font-family: system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  font-size: 16px;
}

.brt-19 *,
.brt-19 *::before,
.brt-19 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-19 {
    --page: oklch(0.952 0.005 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.34 0 0);
  }
}

.brt-19__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-19__theme {
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

.brt-19__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-19__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-19__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-19__sr:focus-visible + .brt-19__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-19__sun {
  display: none;
}

.brt-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1rem,3vw,2.5rem);
}

.brt-19__wrap {
  inline-size: min(72rem,100%);
}

.brt-19__head {
  padding-inline-end: 3.5rem;
  padding-block-end: 1.1rem;
  border-block-end: 5px solid var(--edge);
}

.brt-19__h {
  margin: 0;
  font-size: clamp(2.2rem,8vw,4.5rem);
  font-weight: 700;
  letter-spacing: -.045em;
  line-height: .9;
}

.brt-19__meta {
  margin: .6rem 0 0;
  max-inline-size: 60ch;
  font-family: var(--mono);
  font-size: .8rem;
  line-height: 1.6;
  letter-spacing: .03em;
  color: var(--muted);
}

.brt-19__plans {
  list-style: none;
  margin: 2rem 0 0;
  padding: 0;
  display: grid;
  gap: 0;
  grid-template-columns: repeat(auto-fit,minmax(min(15rem,100%),1fr));
}

.brt-19__plan {
  display: flex;
  flex-direction: column;
  gap: .5rem;
  padding: 1.1rem 1.1rem 1.35rem;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  margin-inline-end: -3px;
  margin-block-end: -3px;
}

.brt-19__plan--rec {
  background: var(--ink);
  color: var(--page);
}

.brt-19__tier {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
  font-family: var(--mono);
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .18em;
}

.brt-19__rec {
  padding: .15rem .4rem;
  border: 2px solid currentColor;
  font-size: .62rem;
  letter-spacing: .14em;
}

.brt-19__price {
  margin: .8rem 0 0;
  display: flex;
  align-items: baseline;
  gap: .15rem;
  font-size: clamp(3rem,7vw,4.2rem);
  font-weight: 700;
  letter-spacing: -.05em;
  line-height: .9;
  font-variant-numeric: tabular-nums;
}

.brt-19__cur {
  font-size: .4em;
  translate: 0 -.85em;
}

.brt-19__per {
  margin-inline-start: .4rem;
  font-family: var(--mono);
  font-size: .18em;
  font-weight: 400;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.brt-19__for {
  margin: .7rem 0 .3rem;
  padding-block-end: .8rem;
  border-block-end: 2px solid currentColor;
  font-size: .95rem;
  line-height: 1.4;
}

.brt-19__feat {
  margin: 0 0 1.25rem;
  padding-inline-start: 1.15rem;
  list-style: disc;
  display: grid;
  gap: .4rem;
  font-size: .95rem;
  line-height: 1.35;
}

.brt-19__cta {
  margin-block-start: auto;
  min-block-size: 2.9rem;
  padding: .75rem 1rem;
  font-family: var(--mono);
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .12em;
  cursor: pointer;
  background: var(--ink);
  color: var(--panel);
  border: var(--bw) solid currentColor;
  box-shadow: 4px 4px 0 currentColor;
}

.brt-19__plan--rec .brt-19__cta {
  background: var(--page);
  color: var(--ink);
}

.brt-19__cta:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 currentColor;
}

.brt-19__cta:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: -8px;
}

.brt-19__compare {
  margin-block-start: 2.5rem;
}

.brt-19__ch {
  margin: 0 0 .9rem;
  font-family: var(--mono);
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .18em;
}

.brt-19__scroll {
  overflow: auto;
  border: var(--bw) solid var(--edge);
}

.brt-19__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: .9rem;
  background: var(--panel);
}

.brt-19__table th,
.brt-19__table td {
  padding: .6rem .7rem;
  text-align: start;
  border-block-end: 1px solid var(--edge);
  white-space: nowrap;
}

.brt-19__table thead th {
  background: var(--ink);
  color: var(--panel);
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  border-block-end: var(--bw) solid var(--edge);
}

.brt-19__table tbody th {
  font-weight: 700;
  white-space: normal;
}

.brt-19__table td {
  font-family: var(--mono);
  font-size: .82rem;
  letter-spacing: .06em;
}

.brt-19__table tbody tr:last-child th,
.brt-19__table tbody tr:last-child td {
  border-block-end: 0;
}

.brt-19__note {
  margin: .9rem 0 0;
  font-family: var(--mono);
  font-size: .76rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.brt-19:has(#brt-19-dark:checked) {
  --page: #000000;
  --panel: #0a0a0a;
  --ink: #ffffff;
  --muted: #bdbdbd;
  --edge: #ffffff;
  --sh: #ffffff;
}

.brt-19:has(#brt-19-dark:checked) .brt-19__moon {
  display: none;
}

.brt-19:has(#brt-19-dark:checked) .brt-19__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-19:not(:has(#brt-19-dark:checked)) {
    --page: #000000;
    --panel: #0a0a0a;
    --ink: #ffffff;
    --muted: #bdbdbd;
    --edge: #ffffff;
    --sh: #ffffff;
  }

  .brt-19:not(:has(#brt-19-dark:checked)) .brt-19__moon {
    display: none;
  }

  .brt-19:not(:has(#brt-19-dark:checked)) .brt-19__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-19 *,
    .brt-19 *::before,
    .brt-19 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-19__plan,
    .brt-19__cta,
    .brt-19__scroll,
    .brt-19__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-19__plan--rec {
    background: Canvas;
    color: CanvasText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-19__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
