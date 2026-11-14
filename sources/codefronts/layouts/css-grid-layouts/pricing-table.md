---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/pricing-table/"
title: "Pricing Table"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A three-tier pricing table where feature lists of different lengths can't misalign the CTAs: rows come from subgrid, the featured tier lifts with a scale…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pricing Table
Source: https://codefronts.com/layouts/css-grid-layouts/pricing-table/

A three-tier pricing table where feature lists of different lengths can't misalign the CTAs: rows come from subgrid, the featured tier lifts with a scale transform (which doesn't disturb the grid), and price typography uses tabular numerals so $9/$29/$99 align by digit.
## HTML
```html
<section class="cgl-17" aria-label="Pricing table demo">
  <div class="cgl-17__tiers">
    <article class="cgl-17__tier">
      <p class="cgl-17__badge">&nbsp;</p>
      <h4>Hobby</h4>
      <p class="cgl-17__price"><data value="9">$9</data><span>/mo</span></p>
      <ul><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul>
      <a href="#0" class="cgl-17__cta">Start free</a>
    </article>
    <article class="cgl-17__tier cgl-17__tier--hot">
      <p class="cgl-17__badge">Most popular</p>
      <h4>Pro</h4>
      <p class="cgl-17__price"><data value="29">$29</data><span>/mo</span></p>
      <ul><li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li><li>Custom domains</li><li>Analytics suite</li></ul>
      <a href="#0" class="cgl-17__cta cgl-17__cta--hot">Go Pro</a>
    </article>
    <article class="cgl-17__tier">
      <p class="cgl-17__badge">&nbsp;</p>
      <h4>Team</h4>
      <p class="cgl-17__price"><data value="99">$99</data><span>/mo</span></p>
      <ul><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Unlimited seats</li><li>SLA 99.9%</li></ul>
      <a href="#0" class="cgl-17__cta">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
.cgl-17,
.cgl-17 *,
.cgl-17 *::before,
.cgl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-17 {
  width: 100%;
  min-height: 100vh;
  --violet: oklch(0.62 0.21 295);
  --bg: oklch(0.97 0.01 300);
  --ink: oklch(0.25 0.04 295);
  font-family: system-ui,sans-serif;
  background: linear-gradient(180deg,var(--bg),oklch(0.93 0.02 295));
  padding: 1.8rem 1.4rem;
}

.cgl-17 .cgl-17__tiers {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(180px,100%),1fr));
  grid-auto-rows: auto;
  gap: 14px;
  max-inline-size: 720px;
  margin-inline: auto;
}

.cgl-17 .cgl-17__tier {
  grid-row: span 5;
  display: grid;
  grid-template-rows: subgrid;
  row-gap: .7rem;
  background: white;
  border: 1px solid oklch(0.88 0.03 295);
  border-radius: 18px;
  padding: 1.3rem;
}

.cgl-17 .cgl-17__tier--hot {
  scale: 1.04;
  z-index: 1;
  border-color: var(--violet);
  box-shadow: 0 24px 48px -24px color-mix(in oklab,var(--violet) 50%,transparent);
}

.cgl-17 .cgl-17__badge {
  font-size: .62rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--violet);
  font-weight: 700;
}

.cgl-17 h4 {
  font-size: 1.1rem;
  color: var(--ink);
}

.cgl-17 .cgl-17__price data {
  font-size: 2.1rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
  letter-spacing: -.02em;
}

.cgl-17 .cgl-17__price span {
  font-size: .8rem;
  color: color-mix(in oklab,var(--ink) 55%,white);
}

.cgl-17 ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: .45rem;
  align-content: start;
}

.cgl-17 li {
  font-size: .8rem;
  color: color-mix(in oklab,var(--ink) 75%,white);
  padding-inline-start: 1.2em;
  position: relative;
}

.cgl-17 li::before {
  content: "✓";
  position: absolute;
  inset-inline-start: 0;
  color: var(--violet);
  font-weight: 700;
}

.cgl-17 .cgl-17__cta {
  align-self: end;
  text-align: center;
  font-size: .85rem;
  font-weight: 600;
  color: var(--violet);
  border: 1.5px solid var(--violet);
  border-radius: 999px;
  text-decoration: none;
  padding: .6rem 1rem;
  min-block-size: 2.75rem;
  display: grid;
  align-items: center;
}

.cgl-17 .cgl-17__cta:hover {
  background: color-mix(in oklab,var(--violet) 10%,white);
}

.cgl-17 .cgl-17__cta--hot {
  background: var(--violet);
  color: white;
}

.cgl-17 .cgl-17__cta--hot:hover {
  background: color-mix(in oklab,var(--violet) 85%,black);
}

.cgl-17 .cgl-17__cta:focus-visible {
  outline: 2px solid var(--violet);
  outline-offset: 3px;
}

@supports not (grid-template-rows: subgrid) {
  .cgl-17 .cgl-17__tier {
    grid-template-rows: auto auto auto 1fr auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — subgrid shares five row tracks across tiers; the featured tier lifts with scale, which never disturbs grid layout. */
```
