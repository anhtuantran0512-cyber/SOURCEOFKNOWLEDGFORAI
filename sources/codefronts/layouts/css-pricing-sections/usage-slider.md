---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/usage-slider/"
title: "Usage Slider"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Native <input type=\"range\"> drives a live monthly estimate."
has_js: "true"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Usage Slider
Source: https://codefronts.com/layouts/css-pricing-sections/usage-slider/

Native <input type="range"> drives a live monthly estimate. Drag the slider, the requests count, total price, and recommended tier all update — with aria-valuetext announcing the result to screen readers. Magenta accent, the usage-based pricing pattern from Twilio / Stripe.
## HTML
```html
<section class="ps-05" aria-label="Usage-based pricing">
  <header class="ps-05__head">
    <span class="ps-05__eye">Pay-as-you-go</span>
    <h2>Only pay for what you actually send.</h2>
    <p>
      Slide to estimate your monthly bill — we round up to the nearest tier so you’re never
      surprised.
    </p>
  </header>
  <div class="ps-05__card">
    <div class="ps-05__stage">
      <div class="ps-05__display">
        <span class="ps-05__label" id="ps-05__lbl">Estimated monthly cost</span>
        <span class="ps-05__amount"><em>$</em><span id="ps-05__price">12</span></span>
        <span class="ps-05__detail"
          ><span id="ps-05__units">10,000</span> requests on the
          <strong id="ps-05__tier">Starter</strong> tier</span
        >
      </div>
      <div class="ps-05__track-wrap">
        <label class="ps-05__sr" for="ps-05__range">Monthly request volume</label>
        <input
          type="range"
          id="ps-05__range"
          class="ps-05__range"
          min="0"
          max="100"
          step="1"
          value="10"
          aria-labelledby="ps-05__lbl"
          aria-valuetext="10,000 requests, Starter tier, 12 dollars per month"
        />
        <div class="ps-05__ticks" aria-hidden="true">
          <span>10K</span><span>100K</span><span>500K</span><span>1M</span><span>5M+</span>
        </div>
      </div>
      <ul class="ps-05__feats">
        <li>No setup fee, no minimum spend</li>
        <li>Auto-tier switching at every milestone</li>
        <li>Usage cap option to prevent surprises</li>
      </ul>
      <a class="ps-05__cta" href="#start">Start with this plan →</a>
    </div>
  </div>
</section>
```
## CSS
```css
.ps-05 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: #1a0a18;
  color: #fde7f4;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-05__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-05__eye {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #f472b6;
  padding: 5px 12px;
  background: rgba(244,114,182,0.12);
  border: 1px solid rgba(244,114,182,0.25);
  border-radius: 999px;
  margin-bottom: 14px;
}

.ps-05__head h2 {
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 10px;
  color: #fff;
}

.ps-05__head p {
  color: #c2a0b6;
  margin: 0 auto;
  max-width: 520px;
  font-size: 14px;
  line-height: 1.6;
}

.ps-05__card {
  max-width: 580px;
  margin: 0 auto;
  background: linear-gradient(180deg, #2a1227, #1a0a18);
  border: 1px solid rgba(244,114,182,0.2);
  border-radius: 18px;
  padding: clamp(24px, 4vw, 36px) clamp(20px, 4vw, 32px);
  box-shadow: 0 22px 60px rgba(244,114,182,0.12);
}

.ps-05__display {
  text-align: center;
  padding-bottom: 22px;
  margin-bottom: 22px;
  border-bottom: 1px dashed rgba(244,114,182,0.2);
}

.ps-05__label {
  display: block;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #c2a0b6;
}

.ps-05__amount {
  display: flex;
  justify-content: center;
  align-items: baseline;
  gap: 4px;
  font-size: 64px;
  font-weight: 800;
  letter-spacing: -0.04em;
  margin: 8px 0 6px;
  background: linear-gradient(180deg, #f472b6, #be185d);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-05__amount em {
  font-size: 28px;
  font-style: normal;
  align-self: flex-start;
  padding-top: 12px;
  opacity: 0.7;
}

.ps-05__detail {
  font-size: 13px;
  color: #c2a0b6;
}

.ps-05__detail strong {
  color: #f472b6;
  font-weight: 700;
}

.ps-05__track-wrap {
  padding: 0 4px 22px;
}

.ps-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.ps-05__range {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  background: transparent;
  cursor: pointer;
  margin: 8px 0 12px;
}

.ps-05__range::-webkit-slider-runnable-track {
  height: 6px;
  border-radius: 999px;
  background: linear-gradient(90deg, #f472b6 0%, #f472b6 var(--ps-05__fill, 10%), #3a1a30 var(--ps-05__fill, 10%), #3a1a30 100%);
}

.ps-05__range::-moz-range-track {
  height: 6px;
  border-radius: 999px;
  background: #3a1a30;
}

.ps-05__range::-moz-range-progress {
  height: 6px;
  border-radius: 999px;
  background: #f472b6;
}

.ps-05__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 22px;
  height: 22px;
  margin-top: -8px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid #f472b6;
  box-shadow: 0 4px 12px rgba(244,114,182,0.4);
  cursor: grab;
}

.ps-05__range::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid #f472b6;
  box-shadow: 0 4px 12px rgba(244,114,182,0.4);
  cursor: grab;
}

.ps-05__range:focus-visible::-webkit-slider-thumb {
  outline: 3px solid #f9a8d4;
  outline-offset: 2px;
}

.ps-05__range:focus-visible::-moz-range-thumb {
  outline: 3px solid #f9a8d4;
  outline-offset: 2px;
}

.ps-05__ticks {
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 10.5px;
  color: #8a647a;
}

.ps-05__feats {
  list-style: none;
  padding: 0;
  margin: 0 0 22px;
  font-size: 13px;
  line-height: 1.9;
  color: #d8b8cc;
}

.ps-05__feats li::before {
  content: '✦';
  color: #f472b6;
  display: inline-block;
  width: 20px;
}

.ps-05__cta {
  display: block;
  text-align: center;
  padding: 13px 18px;
  border-radius: 10px;
  background: linear-gradient(135deg, #f472b6, #be185d);
  color: #fff;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.02em;
  box-shadow: 0 8px 22px rgba(190,24,93,0.35);
  transition: transform 0.18s;
}

.ps-05__cta:hover {
  transform: translateY(-1px);
}

.ps-05__cta:focus-visible {
  outline: 2px solid #f9a8d4;
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ps-05__cta {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var range = document.getElementById('ps-05__range');
  var priceEl = document.getElementById('ps-05__price');
  var unitsEl = document.getElementById('ps-05__units');
  var tierEl  = document.getElementById('ps-05__tier');
  if (!range || !priceEl) return;

  // 5 tiers — index → { units (k), price ($), tier name }
  var tiers = [
    { units: 10,    price: 12,   name: 'Starter' },
    { units: 100,   price: 49,   name: 'Starter' },
    { units: 500,   price: 149,  name: 'Growth'  },
    { units: 1000,  price: 249,  name: 'Growth'  },
    { units: 5000,  price: 749,  name: 'Scale'   }
  ];

  function fmtUnits(k) { return k >= 1000 ? (k / 1000).toFixed(k % 1000 ? 1 : 0) + 'M' : k.toLocaleString() + 'K'; }

  function update() {
    var v = parseInt(range.value, 10);
    // map 0..100 → 0..4 with stops at 10/30/55/80/100
    var idx = v < 25 ? 0 : v < 50 ? 1 : v < 75 ? 2 : v < 95 ? 3 : 4;
    var t = tiers[idx];
    priceEl.textContent = t.price.toLocaleString();
    unitsEl.textContent = fmtUnits(t.units) + ' requests';
    // strip the trailing " requests" when re-using textContent below — show only the formatted number
    unitsEl.textContent = fmtUnits(t.units);
    tierEl.textContent  = t.name;
    range.style.setProperty('--ps-05__fill', v + '%');
    range.setAttribute('aria-valuetext',
      fmtUnits(t.units) + ' requests, ' + t.name + ' tier, ' + t.price + ' dollars per month');
  }

  range.addEventListener('input', update);
  update();
})();
```
