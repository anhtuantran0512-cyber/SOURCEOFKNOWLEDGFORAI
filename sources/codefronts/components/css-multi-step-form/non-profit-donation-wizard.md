---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/non-profit-donation-wizard/"
title: "Non-Profit Donation Wizard"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A warm, generous giving flow — Amount → Your details → Payment — with a monthly/one-time frequency switch, preset amount buttons plus a custom field, and a…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Non-Profit Donation Wizard
Source: https://codefronts.com/components/css-multi-step-form/non-profit-donation-wizard/

A warm, generous giving flow — Amount → Your details → Payment — with a monthly/one-time frequency switch, preset amount buttons plus a custom field, and a live impact line ('$50 feeds a family for a week') that reframes numbers as outcomes. The pattern every high-performing nonprofit form shares: default to monthly, show impact, ask for details last.
## HTML
```html
<section class="msf-16" aria-label="Donation wizard demo">
  <form class="msf-16__card" novalidate>
    <header class="msf-16__head">
      <b class="msf-16__mark">☀</b>
      <div><h3>Bright Table Foundation</h3><p>Every dollar becomes a meal on someone's table.</p></div>
    </header>
    <div class="msf-16__dots"><i class="is-on"></i><i></i><i></i></div>
    <fieldset class="msf-16__step">
      <h4 class="msf-16__title" tabindex="-1">Choose your gift</h4>
      <div class="msf-16__freq" role="radiogroup" aria-label="Donation frequency">
        <label class="msf-16__freqopt"><input type="radio" name="freq" value="monthly" checked><span>Monthly ♥</span></label>
        <label class="msf-16__freqopt"><input type="radio" name="freq" value="one-time"><span>One-time</span></label>
      </div>
      <div class="msf-16__amounts" role="radiogroup" aria-label="Amount">
        <label class="msf-16__amt"><input type="radio" name="amt" value="10"><span>$10</span></label>
        <label class="msf-16__amt"><input type="radio" name="amt" value="25" checked><span>$25</span></label>
        <label class="msf-16__amt"><input type="radio" name="amt" value="50"><span>$50</span></label>
        <label class="msf-16__amt"><input type="radio" name="amt" value="100"><span>$100</span></label>
        <label class="msf-16__custom"><span aria-hidden="true">$</span><input type="number" name="custom" id="msf-16-custom" min="1" max="25000" placeholder="Other" aria-label="Custom amount in dollars"></label>
      </div>
      <p class="msf-16__impact" aria-live="polite"></p>
      <div class="msf-16__nav"><span></span><button type="button" class="msf-16__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-16__step" hidden>
      <h4 class="msf-16__title" tabindex="-1">About you</h4>
      <div class="msf-16__grid">
        <label class="msf-16__field"><span>Full name</span><input type="text" name="name" autocomplete="name" required placeholder="Rowan Ellis"></label>
        <label class="msf-16__field"><span>Email for your receipt</span><input type="email" name="email" autocomplete="email" required placeholder="[email protected]"></label>
      </div>
      <label class="msf-16__anon"><input type="checkbox" name="anon" value="yes"><span>Make my gift anonymous</span></label>
      <div class="msf-16__nav"><button type="button" class="msf-16__back">Back</button><button type="button" class="msf-16__next">Continue to payment</button></div>
    </fieldset>
    <fieldset class="msf-16__step" hidden>
      <h4 class="msf-16__title" tabindex="-1">Payment</h4>
      <div class="msf-16__wallets"><button type="button" class="msf-16__wallet"> Pay</button><button type="button" class="msf-16__wallet">G Pay</button></div>
      <p class="msf-16__or"><span>or card</span></p>
      <div class="msf-16__grid">
        <label class="msf-16__field msf-16__field--full"><span>Card number</span><input type="text" name="card" autocomplete="cc-number" inputmode="numeric" pattern="[0-9 ]{15,19}" required placeholder="4242 4242 4242 4242"></label>
        <label class="msf-16__field"><span>Expiry</span><input type="text" name="exp" autocomplete="cc-exp" pattern="(0[1-9]|1[0-2])\/[0-9]{2}" required placeholder="MM/YY"></label>
        <label class="msf-16__field"><span>CVC</span><input type="text" name="cvc" autocomplete="cc-csc" inputmode="numeric" pattern="[0-9]{3,4}" required placeholder="123"></label>
      </div>
      <div class="msf-16__nav"><button type="button" class="msf-16__back">Back</button><button type="button" class="msf-16__next msf-16__next--go">Give $25 monthly ♥</button></div>
    </fieldset>
    <div class="msf-16__done" hidden><b>☀</b><h4 tabindex="-1">Thank you, truly.</h4><p class="msf-16__donemsg"></p></div>
    <footer class="msf-16__foot">🔒 Secure · tax-deductible · cancel monthly gifts anytime</footer>
  </form>
</section>
```
## CSS
```css
.msf-16,
.msf-16 *,
.msf-16 *::before,
.msf-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-16 {
  width: 100%;
  min-height: 100vh;
  --warm: oklch(0.62 0.16 35);
  --deep: oklch(0.35 0.08 35);
  --ink: oklch(0.27 0.03 35);
  --mut: oklch(0.52 0.03 35);
  --line: oklch(0.9 0.015 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.96 0.018 75);
  display: grid;
  place-items: center;
}

.msf-16__card {
  width: min(520px,100%);
  background: #fff;
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 30px 70px -35px oklch(0.5 0.12 35/.5);
}

.msf-16__head {
  display: flex;
  gap: 14px;
  align-items: center;
  padding: 24px 28px 18px;
}

.msf-16__mark {
  display: grid;
  place-items: center;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.75 0.15 60),var(--warm));
  color: #fff;
  font-size: 22px;
  flex: none;
}

.msf-16__head h3 {
  font-family: Georgia,'Times New Roman',serif;
  font-size: 19px;
  color: var(--deep);
}

.msf-16__head p {
  font-size: 13px;
  color: var(--mut);
}

.msf-16__dots {
  display: flex;
  gap: 5px;
  padding: 0 28px;
  margin-bottom: 16px;
}

.msf-16__dots i {
  height: 5px;
  flex: 1;
  border-radius: 99px;
  background: var(--line);
  transition: background .3s;
}

.msf-16__dots i.is-on {
  background: var(--warm);
}

.msf-16__step {
  border: none;
  padding: 6px 28px 24px;
}

.msf-16__step:not([hidden]) {
  animation: msf-16-in .35s cubic-bezier(.2,.8,.2,1);
}

.msf-16__title {
  font-family: Georgia,serif;
  font-size: 21px;
  font-weight: 600;
  color: var(--deep);
  margin-bottom: 14px;
  outline: none;
}

.msf-16__freq {
  display: grid;
  grid-template-columns: 1fr 1fr;
  padding: 4px;
  background: oklch(0.955 0.012 60);
  border-radius: 12px;
  margin-bottom: 14px;
}

.msf-16__freqopt {
  position: relative;
  text-align: center;
  font-size: 14px;
  font-weight: 800;
  padding: 11px;
  border-radius: 9px;
  cursor: pointer;
  color: var(--mut);
  transition: all .2s;
}

.msf-16__freqopt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-16__freqopt:has(:checked) {
  background: #fff;
  color: var(--deep);
  box-shadow: 0 2px 8px oklch(0.4 0.08 35/.18);
}

.msf-16__freqopt:has(:focus-visible) {
  outline: 3px solid var(--warm);
  outline-offset: 2px;
}

.msf-16__amounts {
  display: grid;
  grid-template-columns: repeat(4,1fr) 1.3fr;
  gap: 8px;
}

@media (max-width: 440px) {
  .msf-16__amounts {
    grid-template-columns: repeat(3,1fr);
  }

  .msf-16__custom {
    grid-column: span 3;
  }
}

.msf-16__amt {
  position: relative;
  text-align: center;
  font-size: 16px;
  font-weight: 800;
  padding: 14px 4px;
  border: 2px solid var(--line);
  border-radius: 12px;
  cursor: pointer;
  font-variant-numeric: tabular-nums;
  transition: all .15s;
}

.msf-16__amt input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.msf-16__amt:hover {
  border-color: var(--warm);
  transform: translateY(-2px);
}

.msf-16__amt:has(:checked) {
  border-color: var(--warm);
  background: color-mix(in oklab,var(--warm) 10%,white);
  color: var(--deep);
}

.msf-16__amt:has(:focus-visible) {
  outline: 3px solid var(--warm);
  outline-offset: 2px;
}

.msf-16__custom {
  display: flex;
  align-items: center;
  gap: 2px;
  border: 2px solid var(--line);
  border-radius: 12px;
  padding: 0 0 0 12px;
  font-weight: 800;
  color: var(--mut);
  transition: border-color .15s;
}

.msf-16__custom:focus-within {
  border-color: var(--warm);
}

.msf-16__custom:has(input:not(:placeholder-shown)) {
  border-color: var(--warm);
  background: color-mix(in oklab,var(--warm) 10%,white);
}

.msf-16__custom input {
  width: 100%;
  font: inherit;
  font-weight: 800;
  color: var(--deep);
  border: none;
  background: none;
  outline: none;
  padding: 14px 8px 14px 2px;
  font-variant-numeric: tabular-nums;
  -moz-appearance: textfield;
}

.msf-16__custom input::-webkit-outer-spin-button,
.msf-16__custom input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.msf-16__impact {
  min-height: 44px;
  margin-top: 14px;
  padding: 12px 16px;
  border-radius: 12px;
  background: color-mix(in oklab,var(--warm) 9%,white);
  border: 1.5px solid color-mix(in oklab,var(--warm) 30%,white);
  font-size: 13.5px;
  line-height: 1.5;
}

.msf-16__impact b {
  color: var(--deep);
}

.msf-16__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 13px;
}

@media (max-width: 440px) {
  .msf-16__grid {
    grid-template-columns: 1fr;
  }
}

.msf-16__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
}

.msf-16__field--full {
  grid-column: 1/-1;
}

.msf-16__field input {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-16__field input:focus-visible {
  outline: none;
  border-color: var(--warm);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--warm) 16%,transparent);
}

.msf-16__field input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
}

.msf-16__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.19 25);
}

.msf-16__anon {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-top: 14px;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  color: var(--mut);
}

.msf-16__anon input {
  width: 18px;
  height: 18px;
  accent-color: var(--warm);
}

.msf-16__anon input:focus-visible {
  outline: 3px solid var(--warm);
  outline-offset: 2px;
}

.msf-16__wallets {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.msf-16__wallet {
  font: inherit;
  font-weight: 800;
  font-size: 15px;
  padding: 13px;
  border: none;
  border-radius: 10px;
  background: var(--ink);
  color: #fff;
  cursor: pointer;
  transition: transform .15s;
}

.msf-16__wallet:hover {
  transform: translateY(-1px);
}

.msf-16__wallet:focus-visible {
  outline: 3px solid var(--warm);
  outline-offset: 2px;
}

.msf-16__or {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 14px 0;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.msf-16__or::before,
.msf-16__or::after {
  content: "";
  flex: 1;
  height: 1.5px;
  background: var(--line);
}

.msf-16__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
}

.msf-16__next,
.msf-16__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 999px;
  padding: 13px 26px;
  transition: transform .15s,background .2s;
}

.msf-16__next {
  border: none;
  color: #fff;
  background: var(--warm);
  box-shadow: 0 14px 30px -12px var(--warm);
}

.msf-16__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--warm) 88%,black);
}

.msf-16__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-16__back:hover {
  color: var(--ink);
}

.msf-16__next:focus-visible,
.msf-16__back:focus-visible {
  outline: 3px solid var(--deep);
  outline-offset: 2px;
}

.msf-16__done[hidden] {
  display: none;
}

.msf-16__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 34px 28px 14px;
}

.msf-16__done b {
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%,oklch(0.75 0.15 60),var(--warm));
  color: #fff;
  font-size: 24px;
  animation: msf-16-pop .6s cubic-bezier(.34,1.56,.64,1);
}

.msf-16__done h4 {
  font-family: Georgia,serif;
  font-size: 22px;
  color: var(--deep);
}

.msf-16__done p {
  color: var(--mut);
  font-size: 14px;
}

.msf-16__foot {
  padding: 14px 28px;
  border-top: 1px solid var(--line);
  text-align: center;
  font-size: 12px;
  color: var(--mut);
}

@keyframes msf-16-in {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-16-pop {
  from {
    transform: scale(.3) rotate(-30deg);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-16 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-16'); if (!root) return;
  const form = root.querySelector('.msf-16__card');
  const steps = [...root.querySelectorAll('.msf-16__step')];
  const dots = [...root.querySelectorAll('.msf-16__dots i')];
  const custom = root.querySelector('#msf-16-custom');
  const impact = root.querySelector('.msf-16__impact');
  const IMPACT = [
    [10, 'provides <b>12 meals</b> for neighbors in need'],
    [25, 'feeds <b>a family of four for a weekend</b>'],
    [50, 'feeds <b>a family for a full week</b>'],
    [100, 'stocks <b>a community pantry shelf for a month</b>'],
    [Infinity, 'helps us <b>open one more table</b> in a new neighborhood']];
  let cur = 0;
  const amount = () => {
    const c = parseInt(custom.value, 10);
    if (c >= 1) return c;
    const r = root.querySelector('[name="amt"]:checked');
    return r ? +r.value : 0;
  };
  const freq = () => root.querySelector('[name="freq"]:checked').value;
  const sync = () => {
    const a = amount(), monthly = freq() === 'monthly';
    const line = IMPACT.find(([cap]) => a <= cap)[1];
    impact.innerHTML = a > 0
      ? 'Your <b>$' + a + (monthly ? '/month' : '') + '</b> gift ' + line + (monthly ? ', every single month.' : '.')
      : 'Choose an amount to see your impact.';
    root.querySelector('.msf-16__next--go').textContent = 'Give $' + (a||0) + (monthly ? ' monthly' : ' once') + ' \u2665';
  };
  custom.addEventListener('focus', () => root.querySelectorAll('[name="amt"]').forEach(r => r.checked = false));
  custom.addEventListener('input', sync);
  root.addEventListener('change', e => {
    if (e.target.name === 'amt') custom.value = '';
    if (e.target.name === 'amt' || e.target.name === 'freq') sync();
  });
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-16__err').forEach(e => e.remove());
    if (fs.querySelector('.msf-16__amounts') && amount() < 1) {
      const err = document.createElement('p'); err.className='msf-16__err'; err.setAttribute('role','alert');
      err.textContent = 'Choose or enter a gift amount.'; fs.querySelector('.msf-16__amounts').after(err); return false;
    }
    fs.querySelectorAll('input[required]').forEach(el => {
      const bad = !el.checkValidity(); el.setAttribute('aria-invalid', bad);
      if (bad && ok) { ok = false;
        const err = document.createElement('p'); err.className='msf-16__err'; err.setAttribute('role','alert');
        err.textContent = 'Please complete the highlighted fields.'; el.closest('.msf-16__grid').append(err); el.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    dots.forEach((d,k) => d.classList.toggle('is-on', k<=i));
    steps[i].querySelector('.msf-16__title').focus();
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-16__next:not(.msf-16__next--go):not(.msf-16__submit):not(.msf-16__skip)')) { if (validate(steps[cur])) show(cur+1); }
    if (e.target.closest('.msf-16__back')) show(cur-1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-16__next--go, .msf-16__submit, .msf-16__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    const monthly = freq() === 'monthly';
    steps.forEach(s => s.hidden = true);
    dots.forEach(d => d.classList.add('is-on'));
    root.querySelector('.msf-16__donemsg').textContent =
      'Your $' + amount() + (monthly ? '/month' : '') + ' gift is at work. Receipt sent to ' + (new FormData(form)).get('email') + '.';
    const done = root.querySelector('.msf-16__done'); done.hidden = false; done.querySelector('h4').focus();
    });
  sync();
})();
```
