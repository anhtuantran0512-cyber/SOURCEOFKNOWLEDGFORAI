---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/monthly-annual-toggle-switch/"
title: "Monthly / Annual Toggle Switch"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "The single most-copied SaaS pattern: a pill toggle slides between Monthly and Annual billing, and every price on the 3-card grid flips to its discounted…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Monthly / Annual Toggle Switch
Source: https://codefronts.com/components/css-pricing-tables/monthly-annual-toggle-switch/

The single most-copied SaaS pattern: a pill toggle slides between Monthly and Annual billing, and every price on the 3-card grid flips to its discounted yearly value with a smooth vertical roll — zero JavaScript, driven entirely by :has() and a checkbox.
## HTML
```html
<section class="prc-01" aria-label="Pricing with monthly and annual billing toggle">
  <header class="prc-01__head">
    <h2>Simple, honest pricing</h2>
    <div class="prc-01__toggle">
      <span id="prc-01-mo-label">Monthly</span>
      <input type="checkbox" id="prc-01-bill" class="prc-01__sr" aria-label="Bill annually and save 20%">
      <label for="prc-01-bill" class="prc-01__pill" aria-hidden="true"><span class="prc-01__knob"></span></label>
      <span id="prc-01-yr-label">Annual</span>
      <span class="prc-01__save">Save 20%</span>
    </div>
  </header>
  <div class="prc-01__grid">
    <article class="prc-01__card">
      <h3>Starter</h3>
      <div class="prc-01__prices"><span class="prc-01__price prc-01__price--mo">$12<small>/mo</small></span><span class="prc-01__price prc-01__price--yr">$9<small>/mo</small></span></div>
      <ul><li>3 projects</li><li>2 GB storage</li><li>Community support</li></ul>
      <a href="#" class="prc-01__cta">Start free</a>
    </article>
    <article class="prc-01__card prc-01__card--hot">
      <h3>Pro</h3>
      <div class="prc-01__prices"><span class="prc-01__price prc-01__price--mo">$29<small>/mo</small></span><span class="prc-01__price prc-01__price--yr">$23<small>/mo</small></span></div>
      <ul><li>Unlimited projects</li><li>200 GB storage</li><li>Priority support</li><li>API access</li></ul>
      <a href="#" class="prc-01__cta prc-01__cta--hot">Choose Pro</a>
    </article>
    <article class="prc-01__card">
      <h3>Team</h3>
      <div class="prc-01__prices"><span class="prc-01__price prc-01__price--mo">$79<small>/mo</small></span><span class="prc-01__price prc-01__price--yr">$63<small>/mo</small></span></div>
      <ul><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Dedicated CSM</li></ul>
      <a href="#" class="prc-01__cta">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
.prc-01,
.prc-01 *,
.prc-01 *::before,
.prc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-01 {
  --accent: oklch(0.58 0.19 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f6f7fb;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
  color: #171a26;
}

.prc-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-01__head {
  text-align: center;
  margin-bottom: 40px;
}

.prc-01__head h2 {
  font-size: clamp(26px,4vw,36px);
  font-weight: 800;
  letter-spacing: -.02em;
  margin-bottom: 20px;
}

.prc-01__toggle {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 14px;
  font-weight: 600;
  color: #5a6074;
}

.prc-01__pill {
  width: 52px;
  height: 28px;
  border-radius: 99px;
  background: #d8dbe6;
  cursor: pointer;
  position: relative;
  transition: background .3s;
}

.prc-01__knob {
  position: absolute;
  inset: 3px auto 3px 3px;
  width: 22px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(20,24,50,.25);
  transition: transform .3s cubic-bezier(.5,1.6,.4,1);
}

.prc-01:has(.prc-01__sr:checked) .prc-01__pill {
  background: var(--accent);
}

.prc-01:has(.prc-01__sr:checked) .prc-01__knob {
  transform: translateX(24px);
}

.prc-01__sr:focus-visible + .prc-01__pill {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.prc-01__save {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 99px;
  background: oklch(0.93 0.05 150);
  color: oklch(0.45 0.12 150);
  opacity: .45;
  transform: scale(.94);
  transition: opacity .3s,transform .3s;
}

.prc-01:has(.prc-01__sr:checked) .prc-01__save {
  opacity: 1;
  transform: scale(1);
}

.prc-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: 20px;
  width: min(920px,100%);
  margin: 0 auto;
}

.prc-01__card {
  background: #fff;
  border: 1px solid #e4e7f0;
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.prc-01__card--hot {
  border-color: var(--accent);
  box-shadow: 0 18px 44px -24px oklch(0.58 0.19 264 / .5);
}

.prc-01__card h3 {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: #5a6074;
}

.prc-01__prices {
  display: grid;
  height: 52px;
  overflow: hidden;
}

.prc-01__price {
  grid-area: 1/1;
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 52px;
  transition: transform .45s cubic-bezier(.6,0,.2,1),opacity .3s;
}

.prc-01__price small {
  font-size: 15px;
  font-weight: 600;
  color: #8a90a4;
  letter-spacing: 0;
}

.prc-01__price--yr {
  transform: translateY(110%);
  opacity: 0;
}

.prc-01:has(.prc-01__sr:checked) .prc-01__price--mo {
  transform: translateY(-110%);
  opacity: 0;
}

.prc-01:has(.prc-01__sr:checked) .prc-01__price--yr {
  transform: translateY(0);
  opacity: 1;
}

.prc-01__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 9px;
  font-size: 14px;
  color: #464c60;
  flex: 1;
}

.prc-01__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 9px;
}

.prc-01__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid #d8dbe6;
  color: #171a26;
  transition: border-color .2s,background .2s;
}

.prc-01__cta:hover {
  border-color: var(--accent);
}

.prc-01__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.prc-01__cta--hot:hover {
  background: oklch(0.52 0.19 264);
}

.prc-01__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-01 .prc-01__price,
    .prc-01 .prc-01__knob,
    .prc-01 .prc-01__save {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — a hidden checkbox + :has() drives the billing state; both prices share one grid cell and roll via transform/opacity, so the swap is compositor-only with zero layout shift. */
```
