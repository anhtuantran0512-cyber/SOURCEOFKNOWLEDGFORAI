---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/expandable-feature-comparison-rows/"
title: "Expandable Feature Comparison Rows"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "The minimal-first pattern conversion teams love: a clean 3-card grid with one \"Compare all features\" toggle that smoothly unfolds a full feature matrix…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Feature Comparison Rows
Source: https://codefronts.com/components/css-pricing-tables/expandable-feature-comparison-rows/

The minimal-first pattern conversion teams love: a clean 3-card grid with one "Compare all features" toggle that smoothly unfolds a full feature matrix beneath — a real, screen-reader-friendly <table> that was there all along, revealed with the grid-rows 0fr→1fr trick.
## HTML
```html
<section class="prc-03" aria-label="Pricing with expandable feature comparison">
  <div class="prc-03__grid">
    <article class="prc-03__card"><h3>Basic</h3><p class="prc-03__price">$0</p><span class="prc-03__per">forever</span><a href="#" class="prc-03__cta">Sign up</a></article>
    <article class="prc-03__card prc-03__card--hot"><h3>Pro</h3><p class="prc-03__price">$19</p><span class="prc-03__per">per user / month</span><a href="#" class="prc-03__cta prc-03__cta--hot">Start trial</a></article>
    <article class="prc-03__card"><h3>Enterprise</h3><p class="prc-03__price">Custom</p><span class="prc-03__per">annual contract</span><a href="#" class="prc-03__cta">Talk to us</a></article>
  </div>
  <input type="checkbox" id="prc-03-more" class="prc-03__sr">
  <label for="prc-03-more" class="prc-03__toggle">
    <span class="prc-03__labels"><span>Compare all features</span><span>Hide comparison</span></span>
    <svg class="prc-03__chev" width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
  </label>
  <div class="prc-03__fold">
    <div class="prc-03__clip">
      <table class="prc-03__table">
        <thead><tr><th scope="col">Feature</th><th scope="col">Basic</th><th scope="col">Pro</th><th scope="col">Enterprise</th></tr></thead>
        <tbody>
          <tr><th scope="row">Projects</th><td>3</td><td>Unlimited</td><td>Unlimited</td></tr>
          <tr><th scope="row">Storage</th><td>1 GB</td><td>100 GB</td><td>Unlimited</td></tr>
          <tr><th scope="row">API access</th><td aria-label="not included">—</td><td aria-label="included">✓</td><td aria-label="included">✓</td></tr>
          <tr><th scope="row">SSO / SAML</th><td aria-label="not included">—</td><td aria-label="not included">—</td><td aria-label="included">✓</td></tr>
          <tr><th scope="row">Audit log</th><td aria-label="not included">—</td><td aria-label="included">✓</td><td aria-label="included">✓</td></tr>
          <tr><th scope="row">Support SLA</th><td>Community</td><td>24 h</td><td>1 h</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
.prc-03,
.prc-03 *,
.prc-03 *::before,
.prc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-03 {
  --accent: oklch(0.55 0.16 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fbfbf9;
  color: #1b1f1c;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-03__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: 18px;
  width: min(860px,100%);
  margin: 0 auto;
}

.prc-03__card {
  background: #fff;
  border: 1px solid #e5e6e0;
  border-radius: 16px;
  padding: 26px;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.prc-03__card--hot {
  border-color: var(--accent);
  box-shadow: 0 16px 40px -26px oklch(0.55 0.16 155/.6);
}

.prc-03__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6a7068;
}

.prc-03__price {
  font-size: 40px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-03__per {
  font-size: 12px;
  color: #8a9086;
  margin-bottom: 18px;
}

.prc-03__cta {
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 11px;
  border-radius: 10px;
  border: 1.5px solid #dcded6;
  color: #1b1f1c;
  transition: border-color .2s;
}

.prc-03__cta:hover {
  border-color: var(--accent);
}

.prc-03__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-03__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-03__toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  width: max-content;
  margin: 26px auto 0;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--accent);
  cursor: pointer;
  padding: 9px 16px;
  border-radius: 99px;
  border: 1.5px solid oklch(0.55 0.16 155/.35);
  transition: background .2s;
}

.prc-03__toggle:hover {
  background: oklch(0.55 0.16 155/.08);
}

.prc-03__sr:focus-visible + .prc-03__toggle {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-03__labels {
  display: grid;
  text-align: left;
}

.prc-03__labels span {
  grid-area: 1/1;
  transition: opacity .25s;
}

.prc-03__labels span:last-child {
  opacity: 0;
}

.prc-03:has(.prc-03__sr:checked) .prc-03__labels span:first-child {
  opacity: 0;
}

.prc-03:has(.prc-03__sr:checked) .prc-03__labels span:last-child {
  opacity: 1;
}

.prc-03__chev {
  transition: transform .35s;
}

.prc-03:has(.prc-03__sr:checked) .prc-03__chev {
  transform: rotate(180deg);
}

.prc-03__fold {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .5s cubic-bezier(.6,0,.2,1);
  width: min(860px,100%);
  margin: 0 auto;
}

.prc-03:has(.prc-03__sr:checked) .prc-03__fold {
  grid-template-rows: 1fr;
}

.prc-03__clip {
  overflow: hidden;
  min-height: 0;
}

.prc-03__table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 22px;
  background: #fff;
  border: 1px solid #e5e6e0;
  border-radius: 14px;
  overflow: hidden;
  font-size: 13.5px;
}

.prc-03__table th,
.prc-03__table td {
  padding: 12px 16px;
  text-align: left;
  border-bottom: 1px solid #eef0ea;
}

.prc-03__table thead th {
  font-size: 11.5px;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #6a7068;
  background: #f4f5f0;
}

.prc-03__table tbody th {
  font-weight: 600;
  color: #3a403b;
}

.prc-03__table td {
  color: #4a504a;
}

.prc-03__table tr:last-child th,
.prc-03__table tr:last-child td {
  border-bottom: none;
}

@media (prefers-reduced-motion: reduce) {
  .prc-03__fold,
    .prc-03__chev,
    .prc-03__labels span {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden checkbox + :has() flips the fold wrapper from grid-template-rows:0fr to 1fr, animating to the table's natural height with no measurement code. */
```
