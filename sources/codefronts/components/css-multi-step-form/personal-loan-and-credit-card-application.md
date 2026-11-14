---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/personal-loan-and-credit-card-application/"
title: "Personal Loan & Credit Card Application"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A strict fintech application wizard — Amount → Identity → Financials → Review — with field-by-field validation on blur, an explicit 'Step 2 of 4' counter,…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Personal Loan & Credit Card Application
Source: https://codefronts.com/components/css-multi-step-form/personal-loan-and-credit-card-application/

A strict fintech application wizard — Amount → Identity → Financials → Review — with field-by-field validation on blur, an explicit 'Step 2 of 4' counter, formatted currency input, and a locked review screen with per-section edit links. The dark, precise UI signals exactly what a lending product should: nothing slips through.
## HTML
```html
<section class="msf-10" aria-label="Loan application demo">
  <form class="msf-10__card" novalidate>
    <header class="msf-10__head">
      <span class="msf-10__logo">⬡ MERIT<b>CAPITAL</b></span>
      <span class="msf-10__where" aria-live="polite">Step <b class="msf-10__n">1</b> of 4</span>
    </header>
    <div class="msf-10__rail"><i style="--w:.25"></i></div>
    <fieldset class="msf-10__step">
      <h3 class="msf-10__title" tabindex="-1">How much do you need?</h3>
      <div class="msf-10__amount">
        <label class="msf-10__field"><span>Loan amount</span>
          <div class="msf-10__money"><b>$</b><input type="text" name="amount" id="msf-10-amount" inputmode="numeric" required value="15,000" data-msg="Enter an amount between $1,000 and $100,000." aria-label="Loan amount in dollars"></div></label>
        <label class="msf-10__field"><span>Term</span>
          <select name="term" required data-msg="Choose a repayment term."><option value="">Select…</option><option>24 months</option><option selected>36 months</option><option>48 months</option><option>60 months</option></select></label>
      </div>
      <p class="msf-10__apr">Representative 9.9% APR · fixed · no origination fee</p>
      <div class="msf-10__nav"><span></span><button type="button" class="msf-10__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-10__step" hidden>
      <h3 class="msf-10__title" tabindex="-1">Verify your identity</h3>
      <div class="msf-10__grid">
        <label class="msf-10__field"><span>Legal name</span><input type="text" name="name" autocomplete="name" required data-msg="Enter your name exactly as it appears on your ID." placeholder="Jordan A. Ellis"></label>
        <label class="msf-10__field"><span>Date of birth</span><input type="date" name="dob" autocomplete="bday" required data-msg="Enter your date of birth."></label>
        <label class="msf-10__field msf-10__field--full"><span>Home address</span><input type="text" name="addr" autocomplete="street-address" required data-msg="Enter your current home address." placeholder="88 Beacon St, Boston, MA 02108"></label>
      </div>
      <div class="msf-10__nav"><button type="button" class="msf-10__back">Back</button><button type="button" class="msf-10__next">Continue</button></div>
    </fieldset>
    <fieldset class="msf-10__step" hidden>
      <h3 class="msf-10__title" tabindex="-1">Your financials</h3>
      <div class="msf-10__grid">
        <label class="msf-10__field"><span>Annual income (pre-tax)</span><input type="text" name="income" inputmode="numeric" pattern="[$0-9,]{4,}" required data-msg="Enter your annual income, e.g. $85,000." placeholder="$85,000"></label>
        <label class="msf-10__field"><span>Employment</span><select name="emp" required data-msg="Select your employment status."><option value="">Select…</option><option>Full-time</option><option>Part-time</option><option>Self-employed</option><option>Retired</option></select></label>
        <label class="msf-10__field"><span>Monthly housing payment</span><input type="text" name="housing" inputmode="numeric" pattern="[$0-9,]{2,}" required data-msg="Enter rent or mortgage, e.g. $1,800." placeholder="$1,800"></label>
      </div>
      <div class="msf-10__nav"><button type="button" class="msf-10__back">Back</button><button type="button" class="msf-10__next">Review application</button></div>
    </fieldset>
    <fieldset class="msf-10__step" hidden>
      <h3 class="msf-10__title" tabindex="-1">Review &amp; submit</h3>
      <div class="msf-10__review"></div>
      <label class="msf-10__agree"><input type="checkbox" name="agree" required data-msg="You must authorize the credit check to submit."><span>I authorize a soft credit check. This won't affect my score.</span></label>
      <div class="msf-10__nav"><button type="button" class="msf-10__back">Back</button><button type="button" class="msf-10__next msf-10__next--go">Submit application</button></div>
    </fieldset>
    <div class="msf-10__done" hidden><b>⬡</b><h3 tabindex="-1">Application received</h3><p>Decision within 2 business hours. Reference #MC-2027-0483.</p></div>
  </form>
</section>
```
## CSS
```css
.msf-10,
.msf-10 *,
.msf-10 *::before,
.msf-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-10 {
  width: 100%;
  min-height: 100vh;
  --gold: oklch(0.8 0.11 90);
  --bg: oklch(0.16 0.01 270);
  --panel: oklch(0.2 0.012 270);
  --line: oklch(0.32 0.015 270);
  --txt: oklch(0.93 0.004 270);
  --mut: oklch(0.64 0.01 270);
  --bad: oklch(0.68 0.17 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--txt);
  padding: 48px 20px;
  background: var(--bg);
  display: grid;
  place-items: center;
}

.msf-10__card {
  width: min(600px,100%);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 40px 80px -40px rgb(0 0 0/.8);
}

.msf-10__head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 28px;
}

.msf-10__logo {
  font-size: 14px;
  letter-spacing: .14em;
  color: var(--mut);
}

.msf-10__logo b {
  color: var(--gold);
}

.msf-10__where {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
}

.msf-10__where b {
  color: var(--txt);
}

.msf-10__rail {
  height: 3px;
  background: var(--line);
}

.msf-10__rail i {
  display: block;
  height: 100%;
  background: var(--gold);
  transform: scaleX(var(--w));
  transform-origin: left;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.msf-10__step {
  border: none;
  padding: 26px 28px 30px;
}

.msf-10__step:not([hidden]) {
  animation: msf-10-in .3s ease;
}

.msf-10__title {
  font-size: 20px;
  letter-spacing: -.01em;
  margin-bottom: 18px;
  outline: none;
}

.msf-10__amount {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 14px;
}

@media (max-width: 480px) {
  .msf-10__amount {
    grid-template-columns: 1fr;
  }
}

.msf-10__money {
  display: flex;
  align-items: center;
  gap: 2px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  background: oklch(0.16 0.01 270);
  padding-left: 14px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-10__money b {
  font-size: 20px;
  color: var(--gold);
}

.msf-10__money input {
  flex: 1;
  min-width: 0;
  font-size: 22px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--txt);
  background: none;
  border: none;
  outline: none;
  padding: 12px 14px 12px 6px;
}

.msf-10__money:focus-within {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--gold) 22%,transparent);
}

.msf-10__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

@media (max-width: 480px) {
  .msf-10__grid {
    grid-template-columns: 1fr;
  }
}

.msf-10__field {
  display: grid;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.msf-10__field--full {
  grid-column: 1/-1;
}

.msf-10__field input,
.msf-10__field select {
  font: inherit;
  font-weight: 500;
  color: var(--txt);
  padding: 11px 13px;
  background: oklch(0.16 0.01 270);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
  color-scheme: dark;
}

.msf-10__field :is(input,select):focus-visible {
  outline: none;
  border-color: var(--gold);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--gold) 22%,transparent);
}

.msf-10__field :is(input,select)[aria-invalid="true"],
.msf-10__money:has([aria-invalid="true"]) {
  border-color: var(--bad);
}

.msf-10__fielderr {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--bad);
}

.msf-10__apr {
  margin-top: 14px;
  font-size: 12.5px;
  color: var(--mut);
}

.msf-10__review {
  display: grid;
  gap: 10px;
  margin-bottom: 16px;
}

.msf-10__review section {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 4px 12px;
  padding: 13px 16px;
  background: oklch(0.16 0.01 270);
  border: 1px solid var(--line);
  border-radius: 12px;
  font-size: 13.5px;
}

.msf-10__review h4 {
  grid-column: 1;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.msf-10__review p {
  grid-column: 1;
  color: var(--txt);
  line-height: 1.5;
}

.msf-10__review button {
  grid-column: 2;
  grid-row: 1/span 2;
  align-self: center;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--gold);
  background: none;
  border: 1px solid color-mix(in oklab,var(--gold) 40%,transparent);
  border-radius: 8px;
  padding: 7px 14px;
  cursor: pointer;
  transition: background .15s;
}

.msf-10__review button:hover {
  background: color-mix(in oklab,var(--gold) 14%,transparent);
}

.msf-10__review button:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 2px;
}

.msf-10__agree {
  display: flex;
  gap: 11px;
  align-items: flex-start;
  font-size: 13px;
  color: var(--mut);
  cursor: pointer;
  line-height: 1.5;
}

.msf-10__agree input {
  width: 18px;
  height: 18px;
  margin-top: 1px;
  accent-color: var(--gold);
  flex: none;
}

.msf-10__agree input:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.msf-10__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.msf-10__next,
.msf-10__back {
  font: inherit;
  font-weight: 800;
  cursor: pointer;
  border-radius: 10px;
  padding: 12px 26px;
  transition: transform .15s,background .2s,color .2s;
}

.msf-10__next {
  border: none;
  color: oklch(0.2 0.02 90);
  background: var(--gold);
}

.msf-10__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--gold) 88%,white);
}

.msf-10__back {
  border: 1.5px solid var(--line);
  background: none;
  color: var(--mut);
}

.msf-10__back:hover {
  color: var(--txt);
  border-color: var(--mut);
}

.msf-10__next:focus-visible,
.msf-10__back:focus-visible {
  outline: 3px solid var(--gold);
  outline-offset: 2px;
}

.msf-10__done[hidden] {
  display: none;
}

.msf-10__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 40px 28px;
}

.msf-10__done b {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--gold);
  color: oklch(0.2 0.02 90);
  font-size: 24px;
  animation: msf-10-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-10__done p {
  color: var(--mut);
  font-size: 14px;
  font-variant-numeric: tabular-nums;
}

@keyframes msf-10-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-10-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-10 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-10'); if (!root) return;
  const form = root.querySelector('.msf-10__card');
  const steps = [...root.querySelectorAll('.msf-10__step')];
  const n = root.querySelector('.msf-10__n'), rail = root.querySelector('.msf-10__rail i');
  let cur = 0, fromReview = false;
  const showErr = (el, on) => {
    el.setAttribute('aria-invalid', on);
    const label = el.closest('.msf-10__field') || el.closest('.msf-10__agree');
    let err = label.querySelector('.msf-10__fielderr');
    if (on) {
      if (!err) { err = document.createElement('span'); err.className = 'msf-10__fielderr'; err.id = 'msf-10-e-' + el.name; err.setAttribute('role','alert'); label.append(err); }
      err.textContent = el.dataset.msg || 'This field is required.';
      el.setAttribute('aria-describedby', err.id);
    } else if (err) { err.remove(); el.removeAttribute('aria-describedby'); }
  };
  const checkField = (el) => {
    let bad = !el.checkValidity();
    if (el.id === 'msf-10-amount') {
      const v = +el.value.replace(/[^0-9]/g,'');
      bad = !(v >= 1000 && v <= 100000);
    }
    showErr(el, bad);
    return !bad;
  };
  // validate on blur; re-validate on input once flagged
  root.addEventListener('blur', e => { if (e.target.matches('input,select')) checkField(e.target); }, true);
  root.addEventListener('input', e => { if (e.target.getAttribute('aria-invalid') === 'true') checkField(e.target); });
  // live thousands separators
  const amount = root.querySelector('#msf-10-amount');
  amount.addEventListener('input', () => {
    const raw = amount.value.replace(/[^0-9]/g,'').slice(0,6);
    amount.value = raw ? (+raw).toLocaleString('en-US') : '';
  });
  const validate = (fs) => {
    let ok = true, first = null;
    fs.querySelectorAll('input[required],select[required]').forEach(el => {
      if (!checkField(el)) { ok = false; first = first || el; }
    });
    if (first) first.focus();
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s,k) => s.hidden = k!==i);
    n.textContent = i+1;
    rail.style.setProperty('--w', ((i+1)/steps.length).toFixed(2));
    if (i === steps.length-1) buildReview();
    steps[i].querySelector('.msf-10__title').focus();
  };
  const buildReview = () => {
    const d = new FormData(form);
    const secs = [
      ['Loan', '$' + d.get('amount') + ' over ' + d.get('term'), 0],
      ['Identity', d.get('name') + ' \u00b7 born ' + d.get('dob') + ' \u00b7 ' + d.get('addr'), 1],
      ['Financials', d.get('income') + '/yr \u00b7 ' + d.get('emp') + ' \u00b7 housing ' + d.get('housing') + '/mo', 2]];
    const wrap = root.querySelector('.msf-10__review');
    wrap.innerHTML = secs.map(([h,p,i]) => '<section><h4>'+h+'</h4><p>'+p+'</p><button type="button" data-edit="'+i+'">Edit</button></section>').join('');
    wrap.querySelectorAll('[data-edit]').forEach(b => b.addEventListener('click', () => { fromReview = true; show(+b.dataset.edit); }));
  };
  root.addEventListener('click', e => {
    if (e.target.closest('.msf-10__next:not(.msf-10__next--go):not(.msf-10__submit):not(.msf-10__skip)')) {
      if (validate(steps[cur])) { const target = fromReview ? steps.length-1 : cur+1; fromReview = false; show(target); }
    }
    if (e.target.closest('.msf-10__back')) { fromReview = false; show(cur-1); }
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-10__next--go, .msf-10__submit, .msf-10__skip')) return;

    e.preventDefault();
    if (!validate(steps[cur])) return;
    steps.forEach(s => s.hidden = true);
    rail.style.setProperty('--w','1'); n.textContent = steps.length;
    const done = root.querySelector('.msf-10__done'); done.hidden = false; done.querySelector('h3').focus();
    });
})();
```
