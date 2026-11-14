---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/subscription-pricing-card/"
title: "Subscription Pricing Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A SaaS / subscription-box pricing card with a big price, a recurring '/mo' interval, a ticked feature list and a highlighted 'Most Popular' accent banner on…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Subscription Pricing Card
Source: https://codefronts.com/components/css-product-cards/subscription-pricing-card/

A SaaS / subscription-box pricing card with a big price, a recurring '/mo' interval, a ticked feature list and a highlighted 'Most Popular' accent banner on the featured tier. The pricing-card structure SaaS and membership sites search for.
## HTML
```html
<article class="cpc-18">
  <div class="cpc-18__card cpc-18__card--featured">
    <span class="cpc-18__banner">Most Popular</span>
    <p class="cpc-18__plan">Pro</p>
    <p class="cpc-18__price"><span class="cpc-18__amt">$24</span><span class="cpc-18__per">/mo</span></p>
    <p class="cpc-18__bill">billed annually · cancel anytime</p>
    <ul class="cpc-18__feat">
      <li>Unlimited projects</li>
      <li>Advanced analytics</li>
      <li>Priority support</li>
      <li>Team roles &amp; permissions</li>
      <li>API access</li>
    </ul>
    <button class="cpc-18__cta" type="button">Start free trial</button>
    <p class="cpc-18__note">14-day trial · no card required</p>
  </div>
</article>
```
## CSS
```css
.cpc-18,
.cpc-18 *,
.cpc-18 *::before,
.cpc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-18 ::selection {
  background: oklch(0.55 0.17 275);
  color: #fff;
}

.cpc-18 {
  --accent: oklch(0.52 0.18 275);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f1f0f7;
}

.cpc-18__card {
  position: relative;
  width: 320px;
  padding: 32px 28px 28px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid #e6e4f0;
  box-shadow: 0 16px 40px -24px rgba(30,20,60,.35);
  text-align: left;
}

.cpc-18__card--featured {
  border: 2px solid var(--accent);
  transform: translateY(-6px);
  box-shadow: 0 30px 60px -28px color-mix(in oklch,var(--accent) 55%,transparent);
}

.cpc-18__banner {
  position: absolute;
  top: -13px;
  left: 28px;
  padding: 6px 14px;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  box-shadow: 0 8px 18px -8px var(--accent);
}

.cpc-18__plan {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.cpc-18__price {
  margin-top: 12px;
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.cpc-18__amt {
  font-size: 52px;
  font-weight: 800;
  line-height: 1;
  color: #1a1430;
  letter-spacing: -.02em;
}

.cpc-18__per {
  font-size: 17px;
  font-weight: 600;
  color: #8a83a3;
}

.cpc-18__bill {
  margin-top: 8px;
  font-size: 13px;
  color: #8a83a3;
}

.cpc-18__feat {
  list-style: none;
  margin: 22px 0 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cpc-18__feat li {
  position: relative;
  padding-left: 30px;
  font-size: 14.5px;
  color: #3a3355;
  line-height: 1.4;
}

.cpc-18__feat li::before {
  content: "✓";
  position: absolute;
  left: 0;
  top: -1px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 800;
  color: #fff;
  background: var(--accent);
}

.cpc-18__cta {
  width: 100%;
  height: 50px;
  border: none;
  border-radius: 13px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  box-shadow: 0 12px 26px -12px var(--accent);
}

.cpc-18__cta:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-18__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

.cpc-18__note {
  margin-top: 12px;
  text-align: center;
  font-size: 12px;
  color: #a49dbb;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — semantic pricing card with an accent border, banner and tick list. */
```
