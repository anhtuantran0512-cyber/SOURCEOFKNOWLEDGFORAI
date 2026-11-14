---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/currency-switcher-price-morph/"
title: "Currency Switcher Price Morph"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "A regional pricing pattern for global SaaS: pick USD, GBP, EUR or AUD from a native select and every price on the grid fades down, morphs to the localized…"
has_js: "true"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Currency Switcher Price Morph
Source: https://codefronts.com/components/css-pricing-tables/currency-switcher-price-morph/

A regional pricing pattern for global SaaS: pick USD, GBP, EUR or AUD from a native select and every price on the grid fades down, morphs to the localized value, and fades back in — announced politely to screen readers.
## HTML
```html
<section class="prc-02" aria-label="Pricing with currency switcher">
  <header class="prc-02__head">
    <h2>Priced for wherever you build</h2>
    <label class="prc-02__picker">Currency
      <select id="prc-02-cur">
        <option value="USD" selected>$ USD</option>
        <option value="GBP">£ GBP</option>
        <option value="EUR">€ EUR</option>
        <option value="AUD">A$ AUD</option>
      </select>
    </label>
  </header>
  <div class="prc-02__grid" aria-live="polite">
    <article class="prc-02__card"><h3>Hobby</h3><p class="prc-02__amount" data-usd="9">$9</p><span class="prc-02__per">per month</span><ul><li>1 site</li><li>10k visits</li></ul><a href="#" class="prc-02__cta">Get Hobby</a></article>
    <article class="prc-02__card prc-02__card--hot"><h3>Studio</h3><p class="prc-02__amount" data-usd="24">$24</p><span class="prc-02__per">per month</span><ul><li>10 sites</li><li>500k visits</li><li>Analytics</li></ul><a href="#" class="prc-02__cta prc-02__cta--hot">Get Studio</a></article>
    <article class="prc-02__card"><h3>Agency</h3><p class="prc-02__amount" data-usd="69">$69</p><span class="prc-02__per">per month</span><ul><li>Unlimited sites</li><li>5M visits</li><li>White-label</li></ul><a href="#" class="prc-02__cta">Get Agency</a></article>
  </div>
</section>
```
## CSS
```css
.prc-02,
.prc-02 *,
.prc-02 *::before,
.prc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-02 {
  --accent: oklch(0.65 0.15 200);
  --swapDur: .28s;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #101420;
  color: #eef1f8;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
}

.prc-02__head {
  text-align: center;
  margin-bottom: 36px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  align-items: center;
}

.prc-02__head h2 {
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.prc-02__picker {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  font-weight: 600;
  color: #9aa2b8;
}

.prc-02__picker select {
  font: inherit;
  font-weight: 700;
  color: #eef1f8;
  background: #1a2030;
  border: 1px solid #2c3450;
  border-radius: 10px;
  padding: 9px 12px;
  cursor: pointer;
}

.prc-02__picker select:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 18px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-02__card {
  background: #171d2e;
  border: 1px solid #242c46;
  border-radius: 16px;
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.prc-02__card--hot {
  border-color: var(--accent);
}

.prc-02__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: #9aa2b8;
}

.prc-02__amount {
  font-size: 44px;
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.15;
  height: 51px;
  transition: opacity var(--swapDur),transform var(--swapDur),filter var(--swapDur);
}

.prc-02__swap .prc-02__amount {
  opacity: 0;
  transform: translateY(6px);
  filter: blur(2px);
}

.prc-02__per {
  font-size: 12px;
  color: #7d859c;
  margin-bottom: 14px;
}

.prc-02__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 13.5px;
  color: #b8bfd4;
  flex: 1;
  margin-bottom: 18px;
}

.prc-02__card li::before {
  content: "—";
  color: var(--accent);
  margin-right: 8px;
}

.prc-02__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 11px;
  border-radius: 10px;
  border: 1px solid #2c3450;
  color: #eef1f8;
  transition: border-color .2s;
}

.prc-02__cta:hover {
  border-color: var(--accent);
}

.prc-02__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: #0d1118;
}

.prc-02__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-02 {
    --swapDur: .01s;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.prc-02');
  const grid = root.querySelector('.prc-02__grid');
  const sel = root.querySelector('#prc-02-cur');
  const RATES = { USD: { r: 1, c: 'USD' }, GBP: { r: 0.78, c: 'GBP' }, EUR: { r: 0.92, c: 'EUR' }, AUD: { r: 1.5, c: 'AUD' } };
  const fmt = (v, cur) => new Intl.NumberFormat('en', { style: 'currency', currency: cur, maximumFractionDigits: 0 }).format(v);
  const dur = () => parseFloat(getComputedStyle(root).getPropertyValue('--swapDur')) * 1000;
  sel.addEventListener('change', () => {
    const { r, c } = RATES[sel.value];
    grid.classList.add('prc-02__swap');
    setTimeout(() => {
      grid.querySelectorAll('.prc-02__amount').forEach(el => {
        el.textContent = fmt(Math.round(el.dataset.usd * r), c);
      });
      grid.classList.remove('prc-02__swap');
    }, dur());
  });
})();
```
