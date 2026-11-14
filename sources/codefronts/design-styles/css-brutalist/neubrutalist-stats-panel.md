---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-stats-panel/"
title: "Neubrutalist Stats Panel"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Four big-number blocks in alternating pastels, each with a trend arrow and delta, above a wide panel holding a segmented progress visual built from custom…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Stats Panel
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-stats-panel/

Four big-number blocks in alternating pastels, each with a trend arrow and delta, above a wide panel holding a segmented progress visual built from custom properties. Figures are real text with tabular-nums — not CSS counters — so they are selectable, searchable and readable by assistive tech.
## HTML
```html
<div class="brt-13">
  <input class="brt-13__sr" type="checkbox" id="brt-13-dark">
  <label class="brt-13__theme" for="brt-13-dark">
    <svg class="brt-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-13__vh">Dark theme</span>
  </label>

  <div class="brt-13__stage">
    <section class="brt-13__wrap" aria-labelledby="brt-13-h">
      <header class="brt-13__head">
        <h2 class="brt-13__h" id="brt-13-h">August at a glance</h2>
        <p class="brt-13__sub">Compared with the 30 days before it.</p>
      </header>

      <ul class="brt-13__stats">
        <li class="brt-13__block" style="--fill:var(--butter)">
          <p class="brt-13__n">48,210</p>
          <p class="brt-13__l">Monthly revenue, USD</p>
          <p class="brt-13__pill"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 16 18 8m0 0h-7m7 0v7" stroke="currentColor" stroke-width="2.8" stroke-linecap="square"/></svg>up 12.4%</p>
        </li>
        <li class="brt-13__block" style="--fill:var(--mint)">
          <p class="brt-13__n">1,284</p>
          <p class="brt-13__l">Active workspaces</p>
          <p class="brt-13__pill"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 16 18 8m0 0h-7m7 0v7" stroke="currentColor" stroke-width="2.8" stroke-linecap="square"/></svg>up 3.1%</p>
        </li>
        <li class="brt-13__block" style="--fill:var(--sky)">
          <p class="brt-13__n">41s</p>
          <p class="brt-13__l">Median deploy time</p>
          <p class="brt-13__pill"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 8l12 8m0 0h-7m7 0V9" stroke="currentColor" stroke-width="2.8" stroke-linecap="square"/></svg>down 9s</p>
        </li>
        <li class="brt-13__block" style="--fill:var(--coral)">
          <p class="brt-13__n">1.9%</p>
          <p class="brt-13__l">Monthly churn</p>
          <p class="brt-13__pill"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 8l12 8m0 0h-7m7 0V9" stroke="currentColor" stroke-width="2.8" stroke-linecap="square"/></svg>down 0.4pt</p>
        </li>
      </ul>

      <section class="brt-13__panel" aria-labelledby="brt-13-mixh">
        <header class="brt-13__panelhead">
          <h3 class="brt-13__panelh" id="brt-13-mixh">Revenue by plan</h3>
          <p class="brt-13__panelmeta">1,284 workspaces</p>
        </header>
        <div class="brt-13__bar" role="img" aria-label="Revenue by plan: Solo 46 percent, Studio 31 percent, Agency 23 percent">
          <span class="brt-13__seg" style="--w:46; --fill:var(--lilac)"></span>
          <span class="brt-13__seg" style="--w:31; --fill:var(--mint)"></span>
          <span class="brt-13__seg" style="--w:23; --fill:var(--butter)"></span>
        </div>
        <ul class="brt-13__key">
          <li><span class="brt-13__swatch" style="--fill:var(--lilac)" aria-hidden="true"></span>Solo <b>46%</b></li>
          <li><span class="brt-13__swatch" style="--fill:var(--mint)" aria-hidden="true"></span>Studio <b>31%</b></li>
          <li><span class="brt-13__swatch" style="--fill:var(--butter)" aria-hidden="true"></span>Agency <b>23%</b></li>
        </ul>
      </section>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-13 {
  --page: #f8f5ed;
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

.brt-13 *,
.brt-13 *::before,
.brt-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-13 {
    --page: oklch(0.97 0.016 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-13__theme {
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
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-13__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-13__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-13__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-13__sr:focus-visible + .brt-13__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-13__sun {
  display: none;
}

.brt-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,4.5vw,3.5rem);
}

.brt-13__wrap {
  inline-size: min(72rem,100%);
}

.brt-13__head {
  margin-block-end: clamp(1.5rem,3.5vw,2.25rem);
  padding-inline-end: 3rem;
}

.brt-13__h {
  margin: 0;
  font-size: clamp(1.8rem,4.8vw,2.8rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.brt-13__sub {
  margin: .4rem 0 0;
  font-size: .95rem;
  color: var(--muted);
}

.brt-13__stats {
  list-style: none;
  margin: 0 0 clamp(1.25rem,2.6vw,1.9rem);
  padding: 0;
  display: grid;
  gap: clamp(1rem,2.2vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(min(12rem,100%),1fr));
}

.brt-13__block {
  padding: clamp(1.1rem,2.2vw,1.5rem);
  background: var(--fill,var(--panel));
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 6px 6px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-13__block:hover {
  translate: -1px -2px;
  box-shadow: 9px 9px 0 var(--sh);
}

.brt-13__n {
  margin: 0;
  font-size: clamp(2.2rem,5vw,3.1rem);
  font-weight: 700;
  letter-spacing: -.04em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.brt-13__l {
  margin: .45rem 0 .9rem;
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .78;
}

.brt-13__pill {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  margin: 0;
  padding: .3rem .55rem;
  background: var(--panel);
  color: var(--ink);
  border: 2px solid var(--edge);
  border-radius: 8px;
  font-size: .8rem;
  font-weight: 700;
}

.brt-13__pill svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.brt-13__panel {
  padding: clamp(1.15rem,2.4vw,1.6rem);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 6px 6px 0 var(--sh);
}

.brt-13__panelhead {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1rem;
  align-items: baseline;
  justify-content: space-between;
  margin-block-end: 1rem;
}

.brt-13__panelh {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 700;
  letter-spacing: -.015em;
}

.brt-13__panelmeta {
  margin: 0;
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-13__bar {
  display: flex;
  block-size: 2.6rem;
  overflow: hidden;
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  background: var(--page);
}

.brt-13__seg {
  flex: var(--w,1);
  background: var(--fill,var(--lilac));
  border-inline-end: var(--bw) solid var(--edge);
  animation: brt-13-grow .6s cubic-bezier(.2,.9,.2,1) both;
}

.brt-13__seg:last-child {
  border-inline-end: 0;
}

.brt-13__seg:nth-child(2) {
  animation-delay: .08s;
}

.brt-13__seg:nth-child(3) {
  animation-delay: .16s;
}

@keyframes brt-13-grow {
  from {
    scale: 0 1;
    transform-origin: left center;
  }

  to {
    scale: 1 1;
    transform-origin: left center;
  }
}

.brt-13__key {
  list-style: none;
  margin: 1rem 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem 1.4rem;
  font-size: .88rem;
  color: var(--muted);
}

.brt-13__key li {
  display: flex;
  align-items: center;
  gap: .45rem;
}

.brt-13__key b {
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.brt-13__swatch {
  inline-size: 1rem;
  block-size: 1rem;
  background: var(--fill);
  border: 2px solid var(--edge);
  border-radius: 4px;
}

.brt-13:has(#brt-13-dark:checked) {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-13:has(#brt-13-dark:checked) .brt-13__moon {
  display: none;
}

.brt-13:has(#brt-13-dark:checked) .brt-13__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-13:not(:has(#brt-13-dark:checked)) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-13:not(:has(#brt-13-dark:checked)) .brt-13__moon {
    display: none;
  }

  .brt-13:not(:has(#brt-13-dark:checked)) .brt-13__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-13 *,
    .brt-13 *::before,
    .brt-13 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .brt-13__block,
    .brt-13__panel,
    .brt-13__bar,
    .brt-13__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-13__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
