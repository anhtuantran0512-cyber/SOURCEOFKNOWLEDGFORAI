---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/bank-loan-calculator-slider-reveal/"
title: "Bank Loan Calculator Slider Reveal"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A slider-driven mortgage calculator where three horizontal range sliders (loan amount, term, interest rate) slide in from the left in sequence, revealing a…"
has_js: "true"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bank Loan Calculator Slider Reveal
Source: https://codefronts.com/motion/css-slide-in-animation/bank-loan-calculator-slider-reveal/

A slider-driven mortgage calculator where three horizontal range sliders (loan amount, term, interest rate) slide in from the left in sequence, revealing a large hero payment number that counts up from zero and a horizontal chip row showing total interest, total paid, and APR — the interactive layout used by Bankrate, LendingTree, Chase, and modern lender comparison tools.
## HTML
```html
<div class="sl-09">
  <div class="sl-09__card">
    <span class="sl-09__eyebrow">Home mortgage calculator</span>
    <h2>Estimate your monthly payment</h2>

    <div class="sl-09__slider" style="--fill:65%">
      <div class="sl-09__srow">
        <label>Loan amount</label>
        <strong>$450,000</strong>
      </div>
      <input type="range" min="100000" max="1000000" value="450000" readonly>
      <div class="sl-09__scale"><small>$100K</small><small>$1M</small></div>
    </div>

    <div class="sl-09__slider" style="--fill:80%">
      <div class="sl-09__srow">
        <label>Loan term</label>
        <strong>30 years</strong>
      </div>
      <input type="range" min="10" max="30" value="30" readonly>
      <div class="sl-09__scale"><small>10 yrs</small><small>30 yrs</small></div>
    </div>

    <div class="sl-09__slider" style="--fill:35%">
      <div class="sl-09__srow">
        <label>Interest rate</label>
        <strong>6.75% APR</strong>
      </div>
      <input type="range" min="3" max="12" value="6.75" step="0.25" readonly>
      <div class="sl-09__scale"><small>3.00%</small><small>12.00%</small></div>
    </div>

    <div class="sl-09__hero">
      <p class="sl-09__label">Estimated monthly payment</p>
      <div class="sl-09__amount" data-target="2918">$0<small>/mo</small></div>
    </div>

    <div class="sl-09__chips">
      <div class="sl-09__chip">
        <span>Total interest</span>
        <strong>$600,470</strong>
      </div>
      <div class="sl-09__chip">
        <span>Total paid</span>
        <strong>$1,050,470</strong>
      </div>
      <div class="sl-09__chip">
        <span>APR</span>
        <strong>6.98%</strong>
      </div>
    </div>

    <button class="sl-09__cta">Apply for pre-approval →</button>
    <p class="sl-09__disc">For estimation only. Not a commitment to lend. Actual APR and payment may vary based on credit profile and lender fees. Subject to underwriting approval.</p>
  </div>
</div>
```
## CSS
```css
.sl-09 {
  --bg: #f0f4f9;
  --card: #fff;
  --navy: #003366;
  --accent: #8b5cf6;
  --good: #059669;
  --ink: #0a1e3a;
  --sub: #4a5b73;
  --line: #e0e6ee;
  --track: #dce4ee;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: radial-gradient(70% 90% at 20% 0%, rgba(0,51,102,.06) 0%, transparent 55%), radial-gradient(60% 80% at 100% 100%, rgba(139,92,246,.05) 0%, transparent 60%), var(--bg);
  color: var(--ink);
}

.sl-09 *,
.sl-09 *::before,
.sl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-09 ::selection {
  background: var(--navy);
  color: #fff;
}

.sl-09__card {
  width: min(500px,100%);
  padding: 32px 32px 28px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 24px 48px -20px rgba(0,51,102,.2);
}

.sl-09__eyebrow {
  display: inline-block;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--navy);
  margin-bottom: 6px;
  opacity: 0;
  animation: sl-09-in .4s ease-out .1s forwards;
}

.sl-09__card h2 {
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.15;
  margin-bottom: 24px;
  opacity: 0;
  animation: sl-09-in .4s ease-out .15s forwards;
}

.sl-09__slider {
  margin-bottom: 20px;
  opacity: 0;
  transform: translateX(-30px);
  animation: sl-09-slide .55s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-09__slider:nth-of-type(1) {
  animation-delay: .25s;
}

.sl-09__slider:nth-of-type(2) {
  animation-delay: .4s;
}

.sl-09__slider:nth-of-type(3) {
  animation-delay: .55s;
}

.sl-09__srow {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 8px;
}

.sl-09__srow label {
  font-size: .78rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.sl-09__srow strong {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.sl-09__slider input[type=range] {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 6px;
  border-radius: 3px;
  background: linear-gradient(to right,var(--accent) 0%,var(--accent) var(--fill,50%),var(--track) var(--fill,50%),var(--track) 100%);
  outline: none;
  cursor: pointer;
  margin-bottom: 6px;
}

.sl-09__slider input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--accent);
  border: 3px solid #fff;
  box-shadow: 0 4px 10px -2px rgba(139,92,246,.5);
  cursor: pointer;
}

.sl-09__slider input[type=range]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 3px solid #fff;
  background: var(--accent);
  box-shadow: 0 4px 10px -2px rgba(139,92,246,.5);
  cursor: pointer;
}

.sl-09__scale {
  display: flex;
  justify-content: space-between;
  margin-top: 2px;
}

.sl-09__scale small {
  font-size: .66rem;
  color: var(--sub);
  font-variant-numeric: tabular-nums;
}

.sl-09__hero {
  margin: 26px -12px 18px;
  padding: 22px 24px;
  border-radius: 14px;
  background: linear-gradient(135deg,#003366,#00509d);
  color: #fff;
  text-align: center;
  opacity: 0;
  transform: scale(.92);
  animation: sl-09-hero .5s cubic-bezier(.34,1.4,.64,1) .75s forwards;
}

.sl-09__label {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(255,255,255,.65);
  margin-bottom: 6px;
}

.sl-09__amount {
  font-size: 2.6rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.sl-09__amount small {
  font-size: .85rem;
  font-weight: 500;
  opacity: .7;
  margin-left: 4px;
}

.sl-09__chips {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 8px;
  margin-bottom: 22px;
}

.sl-09__chip {
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: #f7f9fc;
  opacity: 0;
  transform: translateY(12px);
  animation: sl-09-chip .35s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-09__chip:nth-child(1) {
  animation-delay: 1s;
}

.sl-09__chip:nth-child(2) {
  animation-delay: 1.1s;
}

.sl-09__chip:nth-child(3) {
  animation-delay: 1.2s;
}

.sl-09__chip span {
  display: block;
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sub);
  margin-bottom: 3px;
}

.sl-09__chip strong {
  font-size: .88rem;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.sl-09__cta {
  width: 100%;
  padding: 13px 22px;
  border: none;
  border-radius: 9px;
  background: var(--good);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  margin-bottom: 12px;
  opacity: 0;
  animation: sl-09-in .4s ease-out 1.3s forwards;
  transition: background .18s ease,transform .12s ease;
}

.sl-09__cta:hover {
  background: #047857;
  transform: translateY(-1px);
}

.sl-09__disc {
  font-size: .66rem;
  color: var(--sub);
  line-height: 1.5;
  opacity: 0;
  animation: sl-09-in .4s ease-out 1.4s forwards;
}

@keyframes sl-09-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes sl-09-slide {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes sl-09-hero {
  from {
    opacity: 0;
    transform: scale(.92);
  }

  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes sl-09-chip {
  from {
    opacity: 0;
    transform: translateY(12px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-09 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```

## JavaScript
```js
(function(){
  var el = document.querySelector('.sl-09__amount');
  if (!el || el.dataset.animated) return;
  el.dataset.animated = '1';
  var target = parseInt(el.dataset.target, 10) || 0;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) { el.innerHTML = '$' + fmt(target) + '<small>/mo</small>'; return; }
  var duration = 1200;
  var delay = 900;
  setTimeout(function(){
    var start = null;
    function step(ts){
      if (!start) start = ts;
      var t = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - t, 3);
      var v = Math.round(target * eased);
      el.innerHTML = '$' + fmt(v) + '<small>/mo</small>';
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }, delay);
  function fmt(n){
    return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
})();
```
