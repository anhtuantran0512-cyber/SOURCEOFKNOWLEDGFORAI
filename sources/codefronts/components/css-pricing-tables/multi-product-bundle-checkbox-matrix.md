---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/multi-product-bundle-checkbox-matrix/"
title: "Multi-Product Bundle Checkbox Matrix"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "A build-your-own-bundle calculator: tick add-ons on and off and the order summary re-tallies live, each line item sliding in, the total ticking over with a…"
has_js: "true"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Product Bundle Checkbox Matrix
Source: https://codefronts.com/components/css-pricing-tables/multi-product-bundle-checkbox-matrix/

A build-your-own-bundle calculator: tick add-ons on and off and the order summary re-tallies live, each line item sliding in, the total ticking over with a pop, and a bundle discount unlocking automatically at three or more add-ons.
## HTML
```html
<section class="prc-14" aria-label="Build your bundle pricing calculator">
  <div class="prc-14__wrap">
    <div class="prc-14__pick">
      <h2>Build your bundle</h2>
      <p class="prc-14__sub">Base platform $29/mo · add what you need · 3+ add-ons save 10%</p>
      <ul class="prc-14__list">
        <li><input type="checkbox" id="prc-14-a" data-price="12" data-name="Analytics"><label for="prc-14-a"><span>Analytics</span><b>$12</b></label></li>
        <li><input type="checkbox" id="prc-14-b" data-price="9" data-name="Automations"><label for="prc-14-b"><span>Automations</span><b>$9</b></label></li>
        <li><input type="checkbox" id="prc-14-c" data-price="15" data-name="AI Assist"><label for="prc-14-c"><span>AI Assist</span><b>$15</b></label></li>
        <li><input type="checkbox" id="prc-14-d" data-price="7" data-name="Forms"><label for="prc-14-d"><span>Forms</span><b>$7</b></label></li>
        <li><input type="checkbox" id="prc-14-e" data-price="19" data-name="White-label"><label for="prc-14-e"><span>White-label</span><b>$19</b></label></li>
      </ul>
    </div>
    <aside class="prc-14__summary" aria-live="polite">
      <h3>Your plan</h3>
      <ul class="prc-14__lines" id="prc-14-lines">
        <li class="prc-14__line prc-14__line--base prc-14__on"><span>Platform</span><b>$29</b></li>
        <li class="prc-14__line" data-for="prc-14-a"><span>Analytics</span><b>$12</b></li>
        <li class="prc-14__line" data-for="prc-14-b"><span>Automations</span><b>$9</b></li>
        <li class="prc-14__line" data-for="prc-14-c"><span>AI Assist</span><b>$15</b></li>
        <li class="prc-14__line" data-for="prc-14-d"><span>Forms</span><b>$7</b></li>
        <li class="prc-14__line" data-for="prc-14-e"><span>White-label</span><b>$19</b></li>
        <li class="prc-14__line prc-14__line--disc" id="prc-14-disc"><span>Bundle −10%</span><b id="prc-14-disc-amt">−$0</b></li>
      </ul>
      <p class="prc-14__total"><span>Total</span><output id="prc-14-total">$29</output><small>/mo</small></p>
      <a href="#" class="prc-14__cta">Start with this bundle</a>
    </aside>
  </div>
</section>
```
## CSS
```css
.prc-14,
.prc-14 *,
.prc-14 *::before,
.prc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-14 {
  --accent: oklch(0.63 0.19 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fbf7f4;
  color: #241a15;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
}

.prc-14__wrap {
  display: grid;
  grid-template-columns: 1.2fr .9fr;
  gap: 28px;
  width: min(860px,100%);
}

@media (max-width: 680px) {
  .prc-14__wrap {
    grid-template-columns: 1fr;
  }
}

.prc-14__pick h2 {
  font-size: clamp(24px,3.4vw,32px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.prc-14__sub {
  font-size: 13.5px;
  color: #7d6f65;
  margin: 8px 0 22px;
}

.prc-14__list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.prc-14__list input {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-14__list label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  background: #fff;
  border: 1.5px solid #eadfd7;
  border-radius: 13px;
  padding: 14px 18px;
  font-size: 14.5px;
  font-weight: 600;
  cursor: pointer;
  transition: border-color .25s,background .25s,transform .15s;
}

.prc-14__list label b {
  font-variant-numeric: tabular-nums;
  color: #7d6f65;
}

.prc-14__list label span::before {
  content: "";
  display: inline-block;
  width: 18px;
  height: 18px;
  border-radius: 6px;
  border: 2px solid #d8cabf;
  margin-right: 12px;
  vertical-align: -4px;
  transition: background .2s,border-color .2s;
  background: center/12px no-repeat;
}

.prc-14__list li:has(input:checked) label {
  border-color: var(--accent);
  background: oklch(0.63 0.19 30/.06);
}

.prc-14__list li:has(input:checked) label span::before {
  background-color: var(--accent);
  border-color: var(--accent);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2 6.5 4.8 9 10 3.5' fill='none' stroke='white' stroke-width='2.2' stroke-linecap='round'/%3E%3C/svg%3E");
}

.prc-14__list label:active {
  transform: scale(.985);
}

.prc-14__list input:focus-visible + label {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.prc-14__summary {
  background: #241a15;
  color: #f5ede7;
  border-radius: 20px;
  padding: 26px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  height: max-content;
}

.prc-14__summary h3 {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #b3a294;
}

.prc-14__lines {
  list-style: none;
  display: flex;
  flex-direction: column;
}

.prc-14__line {
  display: flex;
  justify-content: space-between;
  font-size: 13.5px;
  height: 0;
  opacity: 0;
  transform: translateX(-6px);
  overflow: hidden;
  transition: height .3s,opacity .3s,transform .3s;
}

.prc-14__line b {
  font-variant-numeric: tabular-nums;
}

.prc-14__line.prc-14__on {
  height: 26px;
  opacity: 1;
  transform: none;
}

.prc-14__line--disc {
  color: oklch(0.8 0.13 145);
}

.prc-14__total {
  display: flex;
  align-items: baseline;
  gap: 8px;
  border-top: 1px solid #4a3a2f;
  padding-top: 14px;
  font-size: 14px;
  font-weight: 600;
}

.prc-14__total output {
  margin-left: auto;
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.prc-14__total output.prc-14__pop {
  animation: prc-14-pop .35s cubic-bezier(.3,1.6,.4,1);
}

@keyframes prc-14-pop {
  40% {
    transform: scale(1.14);
    color: oklch(0.78 0.15 30);
  }
}

.prc-14__total small {
  color: #b3a294;
}

.prc-14__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 13px;
  border-radius: 11px;
  background: var(--accent);
  color: #fff;
  transition: filter .2s;
}

.prc-14__cta:hover {
  filter: brightness(1.1);
}

.prc-14__cta:focus-visible {
  outline: 3px solid #f5ede7;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-14__line,
    .prc-14__list label {
    transition-duration: .01s;
  }

  .prc-14__total output.prc-14__pop {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.prc-14');
  const boxes = [...root.querySelectorAll('.prc-14__list input')];
  const total = root.querySelector('#prc-14-total');
  const disc = root.querySelector('#prc-14-disc');
  const discAmt = root.querySelector('#prc-14-disc-amt');
  const BASE = 29, DISC_AT = 3, DISC_PCT = 0.10;
  function update() {
    const picked = boxes.filter(b => b.checked);
    boxes.forEach(b => {
      root.querySelector('[data-for="' + b.id + '"]').classList.toggle('prc-14__on', b.checked);
    });
    let sum = BASE + picked.reduce((s, b) => s + +b.dataset.price, 0);
    const hasDisc = picked.length >= DISC_AT;
    const off = hasDisc ? Math.round(sum * DISC_PCT) : 0;
    disc.classList.toggle('prc-14__on', hasDisc);
    discAmt.textContent = '−$' + off;
    total.textContent = '$' + (sum - off);
    total.classList.remove('prc-14__pop');
    requestAnimationFrame(() => requestAnimationFrame(() => total.classList.add('prc-14__pop')));
  }
  boxes.forEach(b => b.addEventListener('change', update));
})();
```
