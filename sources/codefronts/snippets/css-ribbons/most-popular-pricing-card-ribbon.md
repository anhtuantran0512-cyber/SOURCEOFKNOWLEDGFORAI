---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/most-popular-pricing-card-ribbon/"
title: "Most Popular Pricing Card Ribbon"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The conversion workhorse: a horizontal ribbon wrapped across the top of the recommended plan, overhanging both edges with folded ends tucked behind the card."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Most Popular Pricing Card Ribbon
Source: https://codefronts.com/snippets/css-ribbons/most-popular-pricing-card-ribbon/

The conversion workhorse: a horizontal ribbon wrapped across the top of the recommended plan, overhanging both edges with folded ends tucked behind the card. Modern touches throughout — :has() lifts the whole row's shadow when any card is hovered, the featured card is elevated in the grid with a negative block margin, and the ribbon text is bound to the plan with aria-describedby so it is announced, not just seen.
## HTML
```html
<section class="rib-08" aria-label="Pricing card most popular horizontal ribbon demo">
  <div class="rib-08__stage">
    <header class="rib-08__head">
      <p class="rib-08__eyebrow">Pricing</p>
      <h2 class="rib-08__title">Plans that scale with the team</h2>
      <p class="rib-08__sub">Billed annually. Switch or cancel any time — no seat minimums.</p>
    </header>
    <div class="rib-08__row">
      <article class="rib-08__card">
        <div class="rib-08__inner">
          <h3 class="rib-08__plan">Starter</h3>
          <p class="rib-08__price"><span class="rib-08__cur">$</span>0<span class="rib-08__per">/mo</span></p>
          <p class="rib-08__blurb">For solo builders shipping their first product.</p>
          <ul class="rib-08__list">
            <li>1 project</li><li>Community support</li><li>7-day history</li>
          </ul>
          <button class="rib-08__btn" type="button">Start free</button>
        </div>
      </article>
      <article class="rib-08__card rib-08__card--featured">
        <div class="rib-08__ribbon" id="rib-08-pop">Most popular<span class="rib-08__pill">Save 22%</span></div>
        <div class="rib-08__inner">
          <h3 class="rib-08__plan" aria-describedby="rib-08-pop">Team</h3>
          <p class="rib-08__price"><span class="rib-08__cur">$</span>24<span class="rib-08__per">/user/mo</span></p>
          <p class="rib-08__blurb">Everything a product team needs to ship weekly.</p>
          <ul class="rib-08__list">
            <li>Unlimited projects</li><li>SSO &amp; audit log</li><li>Priority support</li><li>12-month history</li>
          </ul>
          <button class="rib-08__btn rib-08__btn--solid" type="button">Choose Team</button>
        </div>
      </article>
      <article class="rib-08__card">
        <div class="rib-08__inner">
          <h3 class="rib-08__plan">Scale</h3>
          <p class="rib-08__price"><span class="rib-08__cur">$</span>62<span class="rib-08__per">/user/mo</span></p>
          <p class="rib-08__blurb">Compliance, residency and a named engineer.</p>
          <ul class="rib-08__list">
            <li>Everything in Team</li><li>Data residency</li><li>99.99% SLA</li>
          </ul>
          <button class="rib-08__btn" type="button">Talk to sales</button>
        </div>
      </article>
    </div>
    <p class="rib-08__chip" aria-hidden="true">inset-inline overhang · clip-path folds · :has(:hover) sibling dim · aria-describedby</p>
  </div>
</section>
```
## CSS
```css
.rib-08,
.rib-08 *,
.rib-08 *::before,
.rib-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-08-bg: #f4f5f8;
  --rib-08-bg: oklch(0.96 0.005 265);
  --rib-08-card: #fff;
  --rib-08-card: oklch(1 0 0);
  --rib-08-ink: #1a1d24;
  --rib-08-ink: oklch(0.24 0.014 265);
  --rib-08-mut: #6d7382;
  --rib-08-mut: oklch(0.57 0.016 265);
  --rib-08-acc: #5b47e0;
  --rib-08-acc: oklch(0.53 0.2 285);
  --rib-08-over: 18px;
  --rib-08-fold: 14px;
  background: var(--rib-08-bg);
  color: var(--rib-08-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3.4vw,34px);
  padding: clamp(20px,4vw,56px);
}

.rib-08__head {
  display: grid;
  gap: 9px;
  text-align: center;
  max-width: 52ch;
}

.rib-08__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--rib-08-acc);
}

.rib-08__title {
  font-size: clamp(25px,4.4vw,38px);
  font-weight: 660;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.rib-08__sub {
  font-size: 14.5px;
  line-height: 1.55;
  color: var(--rib-08-mut);
  text-wrap: pretty;
}

.rib-08__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: clamp(14px,2.2vw,20px);
  width: min(100%,980px);
  align-items: start;
  padding-block-start: 26px;
}

.rib-08__card {
  position: relative;
  border-radius: 20px;
  background: var(--rib-08-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.045),0 16px 36px -22px oklch(0.3 0.03 265/.5);
  transition: opacity .35s cubic-bezier(.16,1,.3,1),scale .35s cubic-bezier(.16,1,.3,1),box-shadow .35s;
}

.rib-08__row:has(.rib-08__card:hover) .rib-08__card:not(:hover) {
  opacity: .7;
  scale: .985;
}

.rib-08__card--featured {
  overflow: visible;
  margin-block: -18px 0;
  border: 1.5px solid color-mix(in oklch,var(--rib-08-acc) 45%,transparent);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 26px 58px -24px color-mix(in oklch,var(--rib-08-acc) 55%,transparent);
}

.rib-08__ribbon {
  position: absolute;
  z-index: 2;
  inset-block-start: -14px;
  inset-inline: calc(var(--rib-08-over) * -1);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 11px 14px;
  border-radius: 6px;
  background: #5b47e0;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-08-acc) 100%,white 14%),var(--rib-08-acc));
  color: oklch(0.99 0 0);
  font-size: 12.5px;
  font-weight: 750;
  letter-spacing: .1em;
  text-transform: uppercase;
  box-shadow: 0 10px 22px -10px color-mix(in oklch,var(--rib-08-acc) 70%,transparent);
}

.rib-08__pill {
  padding: 3px 8px;
  border-radius: 99px;
  background: oklch(1 0 0/.22);
  font-size: 10.5px;
  letter-spacing: .06em;
}

.rib-08__ribbon::before,
.rib-08__ribbon::after {
  content: '';
  position: absolute;
  inset-block-start: 100%;
  inline-size: var(--rib-08-over);
  block-size: var(--rib-08-fold);
  background: #3b2ba8;
  background: color-mix(in oklch,var(--rib-08-acc) 55%,black);
  z-index: -1;
}

.rib-08__ribbon::before {
  inset-inline-start: 0;
  clip-path: polygon(0 0,100% 0,100% 100%);
}

.rib-08__ribbon::after {
  inset-inline-end: 0;
  clip-path: polygon(0 0,100% 0,0 100%);
}

.rib-08__inner {
  display: grid;
  gap: 11px;
  padding: clamp(22px,3vw,28px);
  padding-block-start: clamp(28px,4vw,36px);
}

.rib-08__card--featured .rib-08__inner {
  padding-block-start: clamp(36px,5vw,46px);
}

.rib-08__plan {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--rib-08-mut);
}

.rib-08__price {
  display: flex;
  align-items: baseline;
  font-size: clamp(34px,6vw,44px);
  font-weight: 750;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
}

.rib-08__cur {
  font-size: .52em;
  font-weight: 640;
  margin-inline-end: 2px;
  color: var(--rib-08-mut);
}

.rib-08__per {
  font-size: .32em;
  font-weight: 520;
  margin-inline-start: 5px;
  color: var(--rib-08-mut);
  letter-spacing: 0;
}

.rib-08__blurb {
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--rib-08-mut);
  text-wrap: pretty;
}

.rib-08__list {
  display: grid;
  gap: 9px;
  margin-block: 6px;
  padding: 0;
  list-style: none;
  font-size: 13.5px;
}

.rib-08__list li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  line-height: 1.4;
}

.rib-08__list li::before {
  content: '';
  flex: none;
  inline-size: 16px;
  block-size: 16px;
  margin-block-start: 1px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--rib-08-acc) 16%,transparent);
  background-image: linear-gradient(transparent,transparent);
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--rib-08-acc) 30%,transparent);
}

.rib-08__btn {
  margin-block-start: 8px;
  min-height: 48px;
  border-radius: 12px;
  border: 1.5px solid color-mix(in oklch,var(--rib-08-ink) 18%,transparent);
  background: transparent;
  color: var(--rib-08-ink);
  font: inherit;
  font-size: 14.5px;
  font-weight: 650;
  cursor: pointer;
  transition: border-color .25s,background .25s,translate .2s,color .25s;
}

.rib-08__btn:hover {
  border-color: var(--rib-08-acc);
  color: var(--rib-08-acc);
  translate: 0 -1px;
}

.rib-08__btn--solid {
  border-color: transparent;
  background: var(--rib-08-acc);
  color: oklch(0.99 0 0);
}

.rib-08__btn--solid:hover {
  color: oklch(0.99 0 0);
  filter: brightness(1.07);
}

.rib-08__btn:focus-visible {
  outline: 3px solid var(--rib-08-acc);
  outline-offset: 3px;
}

.rib-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-08-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
}

@media (max-width: 720px) {
  .rib-08__card--featured {
    margin-block: 14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rib-08 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
