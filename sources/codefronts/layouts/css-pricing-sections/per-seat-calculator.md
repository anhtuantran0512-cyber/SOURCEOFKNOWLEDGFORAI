---
source: "codefronts"
url: "https://codefronts.com/layouts/css-pricing-sections/per-seat-calculator/"
title: "Per-Seat Calculator"
section: "layouts"
category: "css-pricing-sections"
category_name: "CSS Pricing Sections"
description: "Real interactive math — adjust the seat count with native +/− buttons (proper aria-label) and the per-seat × seats × cycle cost recomputes live."
has_js: "true"
---

Here's a working CSS Pricing Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Per-Seat Calculator
Source: https://codefronts.com/layouts/css-pricing-sections/per-seat-calculator/

Real interactive math — adjust the seat count with native +/− buttons (proper aria-label) and the per-seat × seats × cycle cost recomputes live. Indigo + sky palette. The pattern Linear / Notion / Slack use to let buyers self-serve estimates.
## HTML
```html
<section class="ps-11" aria-label="Per-seat calculator">
  <header class="ps-11__head">
    <span class="ps-11__eye">Build your plan</span>
    <h2>Per-seat pricing, calculated live.</h2>
    <p>One number to change. Everything else updates with you.</p>
  </header>
  <div class="ps-11__card">
    <div class="ps-11__controls">
      <fieldset class="ps-11__cycle">
        <legend class="ps-11__sr">Billing cycle</legend>
        <input type="radio" name="ps-11__cycle" id="ps-11__m" checked />
        <label for="ps-11__m">Monthly</label>
        <input type="radio" name="ps-11__cycle" id="ps-11__y" />
        <label for="ps-11__y">Yearly · save 25%</label>
      </fieldset>
      <div class="ps-11__stepper">
        <span class="ps-11__stp-lbl">Team size</span>
        <div class="ps-11__stp">
          <button type="button" class="ps-11__btn" id="ps-11__dec" aria-label="Decrease team size">
            −
          </button>
          <input
            type="number"
            id="ps-11__seats"
            value="5"
            min="1"
            max="500"
            inputmode="numeric"
            pattern="[0-9]*"
            aria-label="Number of team members"
          />
          <button type="button" class="ps-11__btn" id="ps-11__inc" aria-label="Increase team size">
            +
          </button>
        </div>
        <span class="ps-11__stp-hint">Up to 500 seats. Above that, we’ll talk.</span>
      </div>
    </div>
    <div class="ps-11__summary">
      <div class="ps-11__row"><span>Seats</span><strong id="ps-11__out-seats">5</strong></div>
      <div class="ps-11__row">
        <span>Per seat</span><strong id="ps-11__out-per">$12 /mo</strong>
      </div>
      <div class="ps-11__row"><span>Cycle</span><strong id="ps-11__out-cyc">Monthly</strong></div>
      <hr />
      <div class="ps-11__row ps-11__total">
        <span>Total today</span>
        <strong id="ps-11__out-total">$60.00</strong>
      </div>
      <p class="ps-11__foot" id="ps-11__out-foot">Billed monthly · cancel any time</p>
      <a class="ps-11__cta" href="#start">Start 14-day trial →</a>
    </div>
  </div>
</section>
```
## CSS
```css
.ps-11 {
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  width: 100%;
  min-height: 100vh;
  background: radial-gradient(60% 80% at 80% 0%, rgba(99,102,241,0.18), transparent 60%), radial-gradient(60% 80% at 0% 100%, rgba(56,189,248,0.14), transparent 60%), #07091a;
  color: #e6e9ff;
  font-family: 'Inter', system-ui, sans-serif;
}

.ps-11__head {
  text-align: center;
  margin-bottom: clamp(24px, 4vw, 36px);
}

.ps-11__eye {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #818cf8;
  padding: 5px 12px;
  background: rgba(129,140,248,0.12);
  border: 1px solid rgba(129,140,248,0.28);
  border-radius: 999px;
  margin-bottom: 14px;
}

.ps-11__head h2 {
  font-size: clamp(22px, 3.4vw, 32px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin: 0 0 8px;
  color: #fff;
}

.ps-11__head p {
  color: #9aa3c8;
  margin: 0;
  font-size: 14px;
}

.ps-11__card {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 0;
  max-width: 820px;
  margin: 0 auto;
  background: rgba(20,22,48,0.7);
  border: 1px solid rgba(129,140,248,0.2);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 24px 60px rgba(0,0,0,0.35);
  backdrop-filter: blur(8px);
}

.ps-11__controls {
  padding: clamp(22px, 4vw, 32px);
  border-right: 1px solid rgba(129,140,248,0.15);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.ps-11__summary {
  padding: clamp(22px, 4vw, 32px);
  background: linear-gradient(180deg, rgba(99,102,241,0.1), rgba(56,189,248,0.06));
  display: flex;
  flex-direction: column;
}

.ps-11__cycle {
  border: 1px solid rgba(129,140,248,0.2);
  border-radius: 10px;
  padding: 4px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  background: rgba(7,9,26,0.4);
  margin: 0;
}

.ps-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.ps-11__cycle input[type="radio"] {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.ps-11__cycle label {
  text-align: center;
  padding: 9px 12px;
  font-size: 12.5px;
  font-weight: 600;
  color: #9aa3c8;
  cursor: pointer;
  border-radius: 7px;
  transition: background 0.18s, color 0.18s;
}

.ps-11__cycle input:checked + label {
  background: linear-gradient(135deg, #6366f1, #38bdf8);
  color: #fff;
}

.ps-11__cycle input:focus-visible + label {
  outline: 2px solid #818cf8;
  outline-offset: 2px;
}

.ps-11__stp-lbl {
  display: block;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #9aa3c8;
  margin-bottom: 8px;
}

.ps-11__stp {
  display: grid;
  grid-template-columns: 44px 1fr 44px;
  border: 1px solid rgba(129,140,248,0.25);
  border-radius: 10px;
  overflow: hidden;
  background: rgba(7,9,26,0.5);
}

.ps-11__btn {
  background: transparent;
  border: 0;
  cursor: pointer;
  font-size: 22px;
  font-weight: 700;
  color: #818cf8;
  font-family: inherit;
  transition: background 0.15s, color 0.15s;
}

.ps-11__btn:hover {
  background: rgba(129,140,248,0.15);
  color: #fff;
}

.ps-11__btn:focus-visible {
  outline: 2px solid #818cf8;
  outline-offset: -2px;
}

.ps-11__btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.ps-11__stp input[type="number"] {
  background: transparent;
  border: 0;
  outline: 0;
  text-align: center;
  color: #fff;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -0.01em;
  font-family: inherit;
  border-left: 1px solid rgba(129,140,248,0.18);
  border-right: 1px solid rgba(129,140,248,0.18);
  -moz-appearance: textfield;
}

.ps-11__stp input::-webkit-outer-spin-button,
.ps-11__stp input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.ps-11__stp input:focus-visible {
  background: rgba(129,140,248,0.12);
}

.ps-11__stp-hint {
  display: block;
  font-size: 11.5px;
  color: #6c759b;
  margin-top: 8px;
}

.ps-11__row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 10px 0;
  font-size: 13.5px;
}

.ps-11__row span {
  color: #9aa3c8;
}

.ps-11__row strong {
  color: #fff;
  font-weight: 600;
}

.ps-11__summary hr {
  border: 0;
  border-top: 1px dashed rgba(129,140,248,0.25);
  margin: 4px 0;
}

.ps-11__total span {
  color: #93c5fd;
  font-size: 13px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.ps-11__total strong {
  font-size: clamp(28px, 4vw, 38px);
  font-weight: 800;
  letter-spacing: -0.02em;
  background: linear-gradient(90deg, #818cf8, #38bdf8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.ps-11__foot {
  font-size: 12px;
  color: #6c759b;
  margin: 4px 0 16px;
}

.ps-11__cta {
  display: block;
  text-align: center;
  padding: 12px 18px;
  border-radius: 10px;
  background: linear-gradient(135deg, #6366f1, #38bdf8);
  color: #fff;
  text-decoration: none;
  font-size: 14px;
  font-weight: 700;
  margin-top: auto;
  box-shadow: 0 10px 24px rgba(99,102,241,0.3);
  transition: transform 0.18s;
}

.ps-11__cta:hover {
  transform: translateY(-1px);
}

.ps-11__cta:focus-visible {
  outline: 2px solid #818cf8;
  outline-offset: 3px;
}

@media (max-width: 720px) {
  .ps-11__card {
    grid-template-columns: 1fr;
  }

  .ps-11__controls {
    border-right: 0;
    border-bottom: 1px solid rgba(129,140,248,0.15);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ps-11__cta,
    .ps-11__btn,
    .ps-11__cycle label {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var seats   = document.getElementById('ps-11__seats');
  var dec     = document.getElementById('ps-11__dec');
  var inc     = document.getElementById('ps-11__inc');
  var rM      = document.getElementById('ps-11__m');
  var rY      = document.getElementById('ps-11__y');
  var outSeats= document.getElementById('ps-11__out-seats');
  var outPer  = document.getElementById('ps-11__out-per');
  var outCyc  = document.getElementById('ps-11__out-cyc');
  var outTot  = document.getElementById('ps-11__out-total');
  var outFoot = document.getElementById('ps-11__out-foot');
  if (!seats || !inc) return;

  var BASE_MONTHLY = 12;       // $12 / seat / mo
  var YEARLY_DISC  = 0.25;     // 25% off when yearly

  function clamp(v) {
    if (isNaN(v) || v < 1) return 1;
    if (v > 500) return 500;
    return v;
  }
  function fmt(n) { return '$' + n.toFixed(2); }

  function update() {
    var n = clamp(parseInt(seats.value, 10));
    seats.value = n;
    var yearly = rY.checked;
    var per    = yearly ? BASE_MONTHLY * (1 - YEARLY_DISC) : BASE_MONTHLY;
    var months = yearly ? 12 : 1;
    var total  = per * n * months;

    outSeats.textContent = n + (n === 1 ? ' member' : ' members');
    outPer.textContent   = '$' + per.toFixed(2) + ' / mo';
    outCyc.textContent   = yearly ? 'Yearly (–25%)' : 'Monthly';
    outTot.textContent   = fmt(total);
    outFoot.textContent  = yearly
      ? 'Billed yearly · ' + fmt(total) + ' once, then renews annually'
      : 'Billed monthly · cancel any time';

    dec.disabled = n <= 1;
    inc.disabled = n >= 500;
  }

  dec.addEventListener('click', function () { seats.value = clamp(parseInt(seats.value, 10) - 1); update(); });
  inc.addEventListener('click', function () { seats.value = clamp(parseInt(seats.value, 10) + 1); update(); });
  seats.addEventListener('input', update);
  rM.addEventListener('change', update);
  rY.addEventListener('change', update);
  update();
})();
```
