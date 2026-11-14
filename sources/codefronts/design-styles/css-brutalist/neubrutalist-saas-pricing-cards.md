---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-saas-pricing-cards/"
title: "Neubrutalist SaaS Pricing Cards"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Three pastel tiers in flat blocks with a 3px black edge and a zero-blur 4px 4px 0 shadow — the whole neubrutalist grammar in one surface."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist SaaS Pricing Cards
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-saas-pricing-cards/

Three pastel tiers in flat blocks with a 3px black edge and a zero-blur 4px 4px 0 shadow — the whole neubrutalist grammar in one surface. The monthly/yearly switch is a real radio group read with :has(), so prices, savings copy and the billing note all change with zero JavaScript, and the CTA buttons demonstrate the press mechanic the rest of the collection reuses: translate: 2px 2px while the shadow halves.
## HTML
```html
<div class="brt-01">
  <input class="brt-01__sr" type="checkbox" id="brt-01-dark">
  <label class="brt-01__theme" for="brt-01-dark">
    <svg class="brt-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-01__vh">Dark theme</span>
  </label>

  <div class="brt-01__stage">
    <section class="brt-01__wrap" aria-labelledby="brt-01-h">
      <header class="brt-01__head">
        <p class="brt-01__eyebrow">Pricing</p>
        <h2 class="brt-01__h" id="brt-01-h">Ship faster, pay less</h2>
        <fieldset class="brt-01__cycle">
          <legend class="brt-01__vh">Billing period</legend>
          <input class="brt-01__sr" type="radio" name="brt-01-cycle" id="brt-01-monthly" value="monthly" checked>
          <label class="brt-01__seg" for="brt-01-monthly">Monthly</label>
          <input class="brt-01__sr" type="radio" name="brt-01-cycle" id="brt-01-yearly" value="yearly">
          <label class="brt-01__seg" for="brt-01-yearly">Yearly <span class="brt-01__save">-20%</span></label>
        </fieldset>
      </header>

      <ul class="brt-01__grid">
        <li class="brt-01__card brt-01__card--a">
          <h3 class="brt-01__tier">Solo</h3>
          <p class="brt-01__blurb">One maker, one product, no seats to manage.</p>
          <p class="brt-01__price"><span class="brt-01__cur">$</span><span class="brt-01__mo">19</span><span class="brt-01__yr">15</span><span class="brt-01__per">/mo</span></p>
          <p class="brt-01__note"><span class="brt-01__mo">Billed monthly</span><span class="brt-01__yr">$180 billed yearly</span></p>
          <ul class="brt-01__list">
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>1 project, unlimited deploys</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>10 GB bandwidth</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>Community support</li>
          </ul>
          <button class="brt-01__cta" type="button">Start free</button>
        </li>

        <li class="brt-01__card brt-01__card--b" data-featured="true">
          <p class="brt-01__badge">Most popular</p>
          <h3 class="brt-01__tier">Studio</h3>
          <p class="brt-01__blurb">For small teams shipping to real customers.</p>
          <p class="brt-01__price"><span class="brt-01__cur">$</span><span class="brt-01__mo">49</span><span class="brt-01__yr">39</span><span class="brt-01__per">/mo</span></p>
          <p class="brt-01__note"><span class="brt-01__mo">Billed monthly</span><span class="brt-01__yr">$468 billed yearly</span></p>
          <ul class="brt-01__list">
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>10 projects, 5 seats</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>250 GB bandwidth</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>Preview environments</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>Email support, 1 business day</li>
          </ul>
          <button class="brt-01__cta brt-01__cta--dark" type="button">Start 14-day trial</button>
        </li>

        <li class="brt-01__card brt-01__card--c">
          <h3 class="brt-01__tier">Agency</h3>
          <p class="brt-01__blurb">Client work, audit trails and invoicing built in.</p>
          <p class="brt-01__price"><span class="brt-01__cur">$</span><span class="brt-01__mo">129</span><span class="brt-01__yr">103</span><span class="brt-01__per">/mo</span></p>
          <p class="brt-01__note"><span class="brt-01__mo">Billed monthly</span><span class="brt-01__yr">$1,236 billed yearly</span></p>
          <ul class="brt-01__list">
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>Unlimited projects, 25 seats</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>1 TB bandwidth</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>SSO and audit log</li>
            <li><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 12.6l5.2 5L20 6.6" stroke="currentColor" stroke-width="3.4" stroke-linecap="square"/></svg>Shared Slack channel</li>
          </ul>
          <button class="brt-01__cta" type="button">Talk to sales</button>
        </li>
      </ul>
      <p class="brt-01__foot">Prices in USD. Cancel any time — no reactivation fee.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-01 {
  /* sRGB baseline — upgraded to oklch below */
  --page: #fdf9f3;
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
  font-synthesis: none;
  -webkit-text-size-adjust: 100%;
}

.brt-01 *,
.brt-01 *::before,
.brt-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-01 {
    --page: oklch(0.983 0.012 85);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.brt-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}
/* theme toggle — pure CSS, 40px box with a 44px hit area */

.brt-01__theme {
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

.brt-01__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-01__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-01__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-01__sr:focus-visible + .brt-01__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-01__sun {
  display: none;
}

.brt-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.brt-01__wrap {
  inline-size: min(72rem,100%);
}

.brt-01__head {
  display: grid;
  justify-items: center;
  gap: .85rem;
  text-align: center;
  margin-block-end: clamp(1.75rem,4vw,2.75rem);
}

.brt-01__eyebrow {
  margin: 0;
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-01__h {
  margin: 0;
  font-size: clamp(2rem,5vw,3.1rem);
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1.02;
  text-wrap: balance;
}

.brt-01__cycle {
  display: inline-flex;
  gap: 0;
  margin: .35rem 0 0;
  padding: .3rem;
  border: var(--bw) solid var(--edge);
  border-radius: 999px;
  background: var(--panel);
  box-shadow: 4px 4px 0 var(--sh);
}

.brt-01__seg {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.5rem;
  padding: .5rem 1.1rem;
  border-radius: 999px;
  font-size: .95rem;
  font-weight: 700;
  cursor: pointer;
  color: var(--ink);
  transition: background .14s ease, color .14s ease;
}

.brt-01__save {
  font-size: .72rem;
  font-weight: 700;
  padding: .15rem .4rem;
  border: 2px solid currentColor;
  border-radius: 6px;
}

.brt-01:has(#brt-01-monthly:checked) .brt-01__seg[for="brt-01-monthly"],
.brt-01:has(#brt-01-yearly:checked) .brt-01__seg[for="brt-01-yearly"] {
  background: var(--ink);
  color: var(--page);
}

.brt-01__sr:focus-visible + .brt-01__seg {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-01__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1.25rem,2.6vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(min(15.5rem,100%),1fr));
  align-items: start;
}

.brt-01__card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: .7rem;
  padding: clamp(1.25rem,2.2vw,1.75rem);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 6px 6px 0 var(--sh);
  color: var(--on);
}

.brt-01__card--a {
  background: var(--mint);
}

.brt-01__card--b {
  background: var(--lilac);
  box-shadow: 8px 8px 0 var(--sh);
  z-index: 1;
}

.brt-01__card--c {
  background: var(--butter);
}

@media (min-width: 56rem) {
  .brt-01__card--b {
    margin-block: -1.25rem;
    padding-block: 2.6rem;
  }
}

.brt-01__badge {
  position: absolute;
  inset-block-start: -1.1rem;
  inset-inline-end: -.75rem;
  rotate: -6deg;
  margin: 0;
  padding: .4rem .75rem;
  background: var(--coral);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 8px;
  box-shadow: 3px 3px 0 var(--sh);
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.brt-01__tier {
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.brt-01__blurb {
  margin: 0;
  font-size: .95rem;
  line-height: 1.45;
  color: var(--on);
  opacity: .75;
  text-wrap: pretty;
}

.brt-01__price {
  margin: .35rem 0 0;
  display: flex;
  align-items: baseline;
  gap: .15rem;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  font-size: clamp(2.6rem,6vw,3.4rem);
  line-height: 1;
}

.brt-01__cur {
  font-size: .42em;
  translate: 0 -.9em;
}

.brt-01__per {
  font-size: .3em;
  font-weight: 600;
  letter-spacing: 0;
  opacity: .7;
}

.brt-01__note {
  margin: 0;
  font-size: .8rem;
  font-weight: 600;
  opacity: .7;
}

.brt-01__yr {
  display: none;
}

.brt-01:has(#brt-01-yearly:checked) .brt-01__mo {
  display: none;
}

.brt-01:has(#brt-01-yearly:checked) .brt-01__yr {
  display: inline;
}

.brt-01__list {
  list-style: none;
  margin: .5rem 0 auto;
  padding: 0;
  display: grid;
  gap: .6rem;
  font-size: .95rem;
}

.brt-01__list li {
  display: grid;
  grid-template-columns: 1.4rem 1fr;
  gap: .55rem;
  align-items: start;
  line-height: 1.35;
}

.brt-01__list svg {
  inline-size: 1.4rem;
  block-size: 1.4rem;
  padding: .15rem;
  border: 2px solid var(--edge);
  border-radius: 5px;
  background: var(--panel);
  color: var(--ink);
}

.brt-01__cta {
  margin-block-start: 1.25rem;
  min-block-size: 2.75rem;
  padding: .8rem 1.1rem;
  font: inherit;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: .01em;
  cursor: pointer;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease, background .14s ease;
}

.brt-01__cta--dark {
  background: var(--ink);
  color: var(--page);
}

.brt-01__cta:hover {
  translate: -1px -1px;
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-01__cta:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-01__cta:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-01__foot {
  margin: clamp(1.5rem,3vw,2.25rem) 0 0;
  text-align: center;
  font-size: .85rem;
  color: var(--muted);
}
/* dark: pastels stay, page darkens, shadow flips to light */

.brt-01:has(#brt-01-dark:checked) {
  --page: #141319;
  --panel: #221f2b;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-01:has(#brt-01-dark:checked) .brt-01__moon {
  display: none;
}

.brt-01:has(#brt-01-dark:checked) .brt-01__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-01:not(:has(#brt-01-dark:checked)) {
    --page: #141319;
    --panel: #221f2b;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-01:not(:has(#brt-01-dark:checked)) .brt-01__moon {
    display: none;
  }

  .brt-01:not(:has(#brt-01-dark:checked)) .brt-01__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-01 *,
    .brt-01 *::before,
    .brt-01 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-01__card,
    .brt-01__cta,
    .brt-01__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-01__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
