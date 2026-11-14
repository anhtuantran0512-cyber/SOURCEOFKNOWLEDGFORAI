---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/multi-tier-tabbed-panels/"
title: "Multi-Tier Tabbed Panels"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "For product suites too broad for one grid: three radio-driven tabs (\"Marketing\", \"Sales\", \"Support\") cross-fade entire pricing panels beneath a sliding tab…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Tier Tabbed Panels
Source: https://codefronts.com/components/css-pricing-tables/multi-tier-tabbed-panels/

For product suites too broad for one grid: three radio-driven tabs ("Marketing", "Sales", "Support") cross-fade entire pricing panels beneath a sliding tab indicator — arrow keys move between tabs natively because they're a real radio group.
## HTML
```html
<section class="prc-12" aria-label="Pricing by product suite">
  <h2 class="prc-12__title">One platform, three suites</h2>
  <div class="prc-12__tabs" role="tablist" aria-label="Product suite">
    <input type="radio" name="prc-12-tab" id="prc-12-t1" class="prc-12__sr" checked>
    <input type="radio" name="prc-12-tab" id="prc-12-t2" class="prc-12__sr">
    <input type="radio" name="prc-12-tab" id="prc-12-t3" class="prc-12__sr">
    <div class="prc-12__bar">
      <label for="prc-12-t1">Marketing</label>
      <label for="prc-12-t2">Sales</label>
      <label for="prc-12-t3">Support</label>
    </div>
  </div>
  <div class="prc-12__panels">
    <div class="prc-12__panel prc-12__panel--1">
      <article class="prc-12__card"><h3>Email</h3><p class="prc-12__price">$15<small>/mo</small></p><ul><li>10k sends</li><li>Templates</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
      <article class="prc-12__card prc-12__card--hot"><h3>Omni</h3><p class="prc-12__price">$45<small>/mo</small></p><ul><li>Email + SMS + push</li><li>Journeys</li></ul><a href="#" class="prc-12__cta prc-12__cta--hot">Choose</a></article>
      <article class="prc-12__card"><h3>ABM</h3><p class="prc-12__price">$120<small>/mo</small></p><ul><li>Account targeting</li><li>Intent data</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
    </div>
    <div class="prc-12__panel prc-12__panel--2">
      <article class="prc-12__card"><h3>CRM</h3><p class="prc-12__price">$20<small>/seat</small></p><ul><li>Pipeline</li><li>Email sync</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
      <article class="prc-12__card prc-12__card--hot"><h3>Engage</h3><p class="prc-12__price">$55<small>/seat</small></p><ul><li>Sequences</li><li>Dialer</li><li>Forecasting</li></ul><a href="#" class="prc-12__cta prc-12__cta--hot">Choose</a></article>
      <article class="prc-12__card"><h3>Revenue</h3><p class="prc-12__price">$140<small>/seat</small></p><ul><li>Deal intelligence</li><li>Quotas</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
    </div>
    <div class="prc-12__panel prc-12__panel--3">
      <article class="prc-12__card"><h3>Inbox</h3><p class="prc-12__price">$12<small>/seat</small></p><ul><li>Shared inbox</li><li>Macros</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
      <article class="prc-12__card prc-12__card--hot"><h3>Desk</h3><p class="prc-12__price">$38<small>/seat</small></p><ul><li>SLAs &amp; routing</li><li>Knowledge base</li></ul><a href="#" class="prc-12__cta prc-12__cta--hot">Choose</a></article>
      <article class="prc-12__card"><h3>AI Agent</h3><p class="prc-12__price">$0.90<small>/resolution</small></p><ul><li>Autonomous replies</li><li>Pay per outcome</li></ul><a href="#" class="prc-12__cta">Choose</a></article>
    </div>
  </div>
</section>
```
## CSS
```css
.prc-12,
.prc-12 *,
.prc-12 *::before,
.prc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-12 {
  --accent: oklch(0.55 0.2 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f5f6fa;
  color: #181b28;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-12__title {
  text-align: center;
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 26px;
}

.prc-12__tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 34px;
}

.prc-12__bar {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,120px);
  background: #e6e8f0;
  border-radius: 99px;
  padding: 5px;
}

.prc-12__bar::before {
  content: "";
  position: absolute;
  inset: 5px auto 5px 5px;
  width: 120px;
  border-radius: 99px;
  background: #fff;
  box-shadow: 0 3px 10px rgba(24,27,40,.14);
  transition: transform .35s cubic-bezier(.55,0,.2,1.2);
}

.prc-12__tabs:has(#prc-12-t2:checked) .prc-12__bar::before {
  transform: translateX(120px);
}

.prc-12__tabs:has(#prc-12-t3:checked) .prc-12__bar::before {
  transform: translateX(240px);
}

.prc-12__bar label {
  position: relative;
  text-align: center;
  font-size: 13.5px;
  font-weight: 700;
  color: #666c82;
  padding: 10px 0;
  cursor: pointer;
  border-radius: 99px;
  transition: color .25s;
}

.prc-12__tabs:has(#prc-12-t1:checked) label[for=prc-12-t1],
.prc-12__tabs:has(#prc-12-t2:checked) label[for=prc-12-t2],
.prc-12__tabs:has(#prc-12-t3:checked) label[for=prc-12-t3] {
  color: #181b28;
}

.prc-12__sr:focus-visible ~ .prc-12__bar {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.prc-12__panels {
  display: grid;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-12__panel {
  grid-area: 1/1;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
  gap: 18px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: opacity .35s,transform .35s,visibility 0s .35s;
  pointer-events: none;
}

.prc-12:has(#prc-12-t1:checked) .prc-12__panel--1,
.prc-12:has(#prc-12-t2:checked) .prc-12__panel--2,
.prc-12:has(#prc-12-t3:checked) .prc-12__panel--3 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition: opacity .35s .1s,transform .35s .1s,visibility 0s;
  pointer-events: auto;
}

.prc-12__card {
  background: #fff;
  border: 1px solid #e2e5ef;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.prc-12__card--hot {
  border-color: var(--accent);
}

.prc-12__card h3 {
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #666c82;
}

.prc-12__price {
  font-size: 36px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-12__price small {
  font-size: 13.5px;
  font-weight: 600;
  color: #8a90a6;
}

.prc-12__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 7px;
  font-size: 13.5px;
  color: #4a5066;
  flex: 1;
  margin: 8px 0 16px;
}

.prc-12__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 8px;
}

.prc-12__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13px;
  padding: 11px;
  border-radius: 10px;
  border: 1.5px solid #dfe2ee;
  color: #181b28;
  transition: border-color .2s;
}

.prc-12__cta:hover {
  border-color: var(--accent);
}

.prc-12__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-12__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 480px) {
  .prc-12__bar {
    grid-template-columns: repeat(3,96px);
  }

  .prc-12__bar::before {
    width: 96px;
  }

  .prc-12__tabs:has(#prc-12-t2:checked) .prc-12__bar::before {
    transform: translateX(96px);
  }

  .prc-12__tabs:has(#prc-12-t3:checked) .prc-12__bar::before {
    transform: translateX(192px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .prc-12__panel,
    .prc-12__bar::before,
    .prc-12__bar label {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radio group powers the tabs (free arrow-key navigation); :has(:checked) slides the indicator pseudo-element and cross-fades stacked panels, with visibility swaps keeping hidden panels out of the tab order. */
```
