---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/mortgage-and-home-loan-application/"
title: "Mortgage & Home Loan Application"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A trust-building 4-step mortgage pre-qualification flow with styled range sliders that live-update loan figures, big radio cards for property type, and a…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mortgage & Home Loan Application
Source: https://codefronts.com/components/css-multi-step-form/mortgage-and-home-loan-application/

A trust-building 4-step mortgage pre-qualification flow with styled range sliders that live-update loan figures, big radio cards for property type, and a percentage progress readout. The kind of long financial form that only converts when it's chunked, calm, and shows people how far along they are.
## HTML
```html
<section class="msf-04" aria-label="Mortgage application demo">
  <form class="msf-04__card" novalidate>
    <header class="msf-04__head">
      <div><p class="msf-04__kicker">Meridian Home Loans</p><h3 class="msf-04__h">See what you qualify for</h3></div>
      <div class="msf-04__meter"><b class="msf-04__pct" aria-hidden="true">25%</b><div class="msf-04__bar" role="progressbar" aria-label="Application progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="25"><i style="--w:.25"></i></div><small>Step <span class="msf-04__stepnow">1</span> of 4</small></div>
    </header>
    <fieldset class="msf-04__step">
      <legend class="msf-04__title" tabindex="-1">What are you buying?</legend>
      <div class="msf-04__cards" role="radiogroup" aria-label="Property type">
        <label class="msf-04__radio"><input type="radio" name="ptype" value="Single-family home" checked><b>🏠</b><span>Single-family</span></label>
        <label class="msf-04__radio"><input type="radio" name="ptype" value="Condo"><b>🏢</b><span>Condo</span></label>
        <label class="msf-04__radio"><input type="radio" name="ptype" value="Townhouse"><b>🏘️</b><span>Townhouse</span></label>
        <label class="msf-04__radio"><input type="radio" name="ptype" value="Multi-family"><b>🏗️</b><span>Multi-family</span></label>
      </div>
      <div class="msf-04__usecards" role="radiogroup" aria-label="Property use">
        <label class="msf-04__pill"><input type="radio" name="use" value="Primary residence" checked><span>Primary residence</span></label>
        <label class="msf-04__pill"><input type="radio" name="use" value="Second home"><span>Second home</span></label>
        <label class="msf-04__pill"><input type="radio" name="use" value="Investment"><span>Investment</span></label>
      </div>
      <div class="msf-04__nav"><span></span><button type="button" class="msf-04__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-04__step" hidden>
      <legend class="msf-04__title" tabindex="-1">Your numbers</legend>
      <div class="msf-04__slider">
        <div class="msf-04__sliderhead"><span>Home price</span><output id="msf-04-price-out">$425,000</output></div>
        <input type="range" id="msf-04-price" min="100000" max="1500000" step="5000" value="425000" aria-label="Home price">
      </div>
      <div class="msf-04__slider">
        <div class="msf-04__sliderhead"><span>Down payment</span><output id="msf-04-down-out">$85,000 · 20%</output></div>
        <input type="range" id="msf-04-down" min="3" max="50" step="1" value="20" aria-label="Down payment percent">
      </div>
      <p class="msf-04__estimate" aria-live="polite">Estimated payment <b id="msf-04-monthly">$2,153/mo</b> <small>at 6.4% APR · 30-yr fixed</small></p>
      <div class="msf-04__nav"><button type="button" class="msf-04__back">Back</button><button type="button" class="msf-04__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-04__step" hidden>
      <legend class="msf-04__title" tabindex="-1">Income &amp; employment</legend>
      <div class="msf-04__grid">
        <label class="msf-04__field"><span>Annual household income</span><input type="text" name="income" inputmode="numeric" pattern="[$0-9,]{4,}" required placeholder="$120,000"></label>
        <label class="msf-04__field"><span>Employment status</span><select name="emp" required><option value="">Select…</option><option>Employed (W-2)</option><option>Self-employed</option><option>Retired</option><option>Other</option></select></label>
      </div>
      <div class="msf-04__nav"><button type="button" class="msf-04__back">Back</button><button type="button" class="msf-04__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-04__step" hidden>
      <legend class="msf-04__title" tabindex="-1">Where do we send your rate?</legend>
      <div class="msf-04__grid">
        <label class="msf-04__field"><span>Full name</span><input type="text" name="name" autocomplete="name" required placeholder="Alex Morgan"></label>
        <label class="msf-04__field"><span>Email</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
      </div>
      <p class="msf-04__legal">Checking rates won't affect your credit score.</p>
      <div class="msf-04__nav"><button type="button" class="msf-04__back">Back</button><button type="button" class="msf-04__next msf-04__next--go">Get my rate</button></div>
    </fieldset>
    <div class="msf-04__done" hidden><b>%</b><h3 tabindex="-1">You're pre-qualified to shop</h3><p>Your personalized rate sheet is on its way.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-04,
.msf-04 *,
.msf-04 *::before,
.msf-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-04 {
  width: 100%;
  min-height: 100vh;
  --navy: oklch(0.32 0.06 255);
  --gold: oklch(0.75 0.13 85);
  --line: oklch(0.89 0.01 255);
  --ink: oklch(0.26 0.03 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: linear-gradient(180deg,oklch(0.95 0.01 255),oklch(0.92 0.015 255));
  display: grid;
  place-items: center;
}

.msf-04__card {
  width: min(640px,100%);
  background: #fff;
  border-radius: 18px;
  padding: 30px 34px 34px;
  box-shadow: 0 30px 70px -35px oklch(0.32 0.06 255/.5);
}

.msf-04__head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 18px;
  flex-wrap: wrap;
  padding-bottom: 20px;
  margin-bottom: 24px;
  border-bottom: 1px solid var(--line);
}

.msf-04__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--gold);
}

.msf-04__h {
  font-size: 21px;
  letter-spacing: -.01em;
  color: var(--navy);
}

.msf-04__meter {
  display: grid;
  justify-items: end;
  gap: 5px;
  min-width: 150px;
}

.msf-04__pct {
  font-size: 20px;
  color: var(--navy);
  font-variant-numeric: tabular-nums;
}

.msf-04__bar {
  width: 150px;
  height: 6px;
  border-radius: 99px;
  background: var(--line);
  overflow: hidden;
}

.msf-04__bar i {
  display: block;
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--navy),var(--gold));
  transform: scaleX(var(--w));
  transform-origin: left;
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.msf-04__meter small {
  font-size: 11.5px;
  color: oklch(0.55 0.02 255);
}

.msf-04__step {
  border: none;
}

.msf-04__step:not([hidden]) {
  animation: msf-04-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-04__title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
  outline: none;
  color: var(--navy);
}

.msf-04__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(110px,1fr));
  gap: 10px;
  margin-bottom: 14px;
}

.msf-04__radio {
  display: grid;
  justify-items: center;
  gap: 6px;
  padding: 16px 10px;
  border: 2px solid var(--line);
  border-radius: 14px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 700;
  transition: border-color .2s,background .2s,transform .15s;
}

.msf-04__radio b {
  font-size: 24px;
}

.msf-04__radio input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-04__radio:hover {
  transform: translateY(-2px);
}

.msf-04__radio:has(:checked) {
  border-color: var(--navy);
  background: color-mix(in oklab,var(--navy) 6%,white);
  box-shadow: 0 0 0 1px var(--navy);
}

.msf-04__radio:has(:focus-visible) {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.msf-04__usecards {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.msf-04__pill {
  position: relative;
  font-size: 13px;
  font-weight: 700;
  padding: 9px 16px;
  border: 1.5px solid var(--line);
  border-radius: 999px;
  cursor: pointer;
  transition: all .2s;
}

.msf-04__pill input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-04__pill:has(:checked) {
  border-color: var(--navy);
  background: var(--navy);
  color: #fff;
}

.msf-04__pill:has(:focus-visible) {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.msf-04__slider {
  margin-bottom: 22px;
}

.msf-04__sliderhead {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  font-weight: 700;
  color: oklch(0.45 0.02 255);
  margin-bottom: 10px;
}

.msf-04__sliderhead output {
  font-size: 16px;
  color: var(--navy);
  font-variant-numeric: tabular-nums;
}

.msf-04 input[type="range"] {
  --fill: 50%;
  width: 100%;
  height: 6px;
  border-radius: 99px;
  appearance: none;
  -webkit-appearance: none;
  background: linear-gradient(90deg,var(--navy) var(--fill),var(--line) var(--fill));
  cursor: pointer;
}

.msf-04 input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--navy);
  box-shadow: 0 3px 8px oklch(0.32 0.06 255/.35);
  transition: transform .15s;
}

.msf-04 input[type="range"]::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.msf-04 input[type="range"]::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--navy);
  box-shadow: 0 3px 8px oklch(0.32 0.06 255/.35);
}

.msf-04 input[type="range"]:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 4px;
}

.msf-04__estimate {
  padding: 14px 18px;
  border-radius: 12px;
  background: color-mix(in oklab,var(--gold) 14%,white);
  border: 1px solid color-mix(in oklab,var(--gold) 40%,white);
  font-size: 14px;
}

.msf-04__estimate b {
  font-size: 18px;
  color: var(--navy);
  font-variant-numeric: tabular-nums;
}

.msf-04__estimate small {
  color: oklch(0.5 0.03 255);
}

.msf-04__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 520px) {
  .msf-04__grid {
    grid-template-columns: 1fr;
  }
}

.msf-04__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: oklch(0.45 0.02 255);
}

.msf-04__field input,
.msf-04__field select {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-04__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--navy);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--navy) 12%,transparent);
}

.msf-04__field :is(input,select)[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-04__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
}

.msf-04__legal {
  font-size: 12px;
  color: oklch(0.55 0.02 255);
  margin-top: 12px;
}

.msf-04__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-04__next,
.msf-04__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 10px;
  padding: 13px 26px;
  transition: transform .15s,background .2s;
}

.msf-04__next {
  border: none;
  color: #fff;
  background: var(--navy);
  box-shadow: 0 12px 26px -12px var(--navy);
}

.msf-04__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--navy) 85%,black);
}

.msf-04__next--go {
  background: var(--gold);
  color: var(--navy);
}

.msf-04__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--ink);
}

.msf-04__back:hover {
  border-color: var(--navy);
}

.msf-04__next:focus-visible,
.msf-04__back:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.msf-04__done[hidden] {
  display: none;
}

.msf-04__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 36px 0 14px;
}

.msf-04__done b {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: var(--gold);
  color: var(--navy);
  font-size: 22px;
  animation: msf-04-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-04__done p {
  color: oklch(0.5 0.02 255);
  font-size: 14px;
}

@keyframes msf-04-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-04-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-04 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-04'); if (!root) return;
  const form = root.querySelector('.msf-04__card');
  const steps = [...root.querySelectorAll('.msf-04__step')];
  const bar = root.querySelector('.msf-04__bar'), fill = bar.querySelector('i');
  const pct = root.querySelector('.msf-04__pct'), stepNow = root.querySelector('.msf-04__stepnow');
  let cur = 0;
  const fmt = n => '$' + Math.round(n).toLocaleString('en-US');
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-04__err').forEach(e => e.remove());
    fs.querySelectorAll('input[required],select[required]').forEach(el => {
      const bad = !el.checkValidity();
      el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-04__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields to continue.';
        el.closest('.msf-04__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    const p = Math.round(((i+1)/steps.length)*100);
    pct.textContent = p + '%'; stepNow.textContent = i+1;
    bar.setAttribute('aria-valuenow', p);
    fill.style.setProperty('--w', ((i+1)/steps.length).toFixed(2));
    steps[i].querySelector('.msf-04__title').focus();
  };
  // sliders + live estimate
  const price = root.querySelector('#msf-04-price'), down = root.querySelector('#msf-04-down');
  const priceOut = root.querySelector('#msf-04-price-out'), downOut = root.querySelector('#msf-04-down-out'), monthly = root.querySelector('#msf-04-monthly');
  const RATE = 0.064, YEARS = 30;
  const update = () => {
    [price, down].forEach(r => r.style.setProperty('--fill', ((r.value - r.min)/(r.max - r.min)*100) + '%'));
    const P = +price.value, dp = P * (+down.value/100);
    priceOut.textContent = fmt(P);
    downOut.textContent = fmt(dp) + ' \u00b7 ' + down.value + '%';
    const L = P - dp, r = RATE/12, n = YEARS*12;
    monthly.textContent = fmt(L * r * Math.pow(1+r,n) / (Math.pow(1+r,n)-1)) + '/mo';
  };
  [price, down].forEach(r => r.addEventListener('input', update)); update();
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-04__next:not(.msf-04__next--go):not(.msf-04__submit):not(.msf-04__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-04__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-04__next--go, .msf-04__submit, .msf-04__skip')) return;

    e.preventDefault();
    steps.forEach(s => s.hidden = true);
    pct.textContent = '100%'; fill.style.setProperty('--w','1'); bar.setAttribute('aria-valuenow',100);
    const done = root.querySelector('.msf-04__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
