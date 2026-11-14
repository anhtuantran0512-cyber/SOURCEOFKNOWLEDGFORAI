---
source: "codefronts"
url: "https://codefronts.com/components/css-multi-step-form/e-commerce-multi-step-checkout/"
title: "E-Commerce Multi-Step Checkout"
section: "components"
category: "css-multi-step-form"
category_name: "CSS Multi-Step Form UI"
description: "A conversion-focused 3-step checkout wizard — Shipping → Payment → Review — with a numbered progress stepper that fills as you advance, inline field…"
has_js: "true"
---

Here's a working CSS Multi-Step Form UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Multi-Step Checkout
Source: https://codefronts.com/components/css-multi-step-form/e-commerce-multi-step-checkout/

A conversion-focused 3-step checkout wizard — Shipping → Payment → Review — with a numbered progress stepper that fills as you advance, inline field validation, and a sticky order summary. Chunking checkout into small wins is the single most proven pattern for cutting cart abandonment on e-commerce sites.
## HTML
```html
<section class="msf-01" aria-label="E-commerce checkout demo">
  <form class="msf-01__form" novalidate>
    <header class="msf-01__head">
      <span class="msf-01__logo">acme<b>store</b></span>
      <ol class="msf-01__stepper" style="--progress:0">
        <li class="msf-01__dot is-active" aria-current="step"><i>1</i><span>Shipping</span></li>
        <li class="msf-01__dot"><i>2</i><span>Payment</span></li>
        <li class="msf-01__dot"><i>3</i><span>Review</span></li>
      </ol>
    </header>
    <div class="msf-01__body">
      <div class="msf-01__steps">
        <fieldset class="msf-01__step">
          <h3 class="msf-01__title" tabindex="-1">Where should we ship it?</h3>
          <div class="msf-01__grid">
            <label class="msf-01__field msf-01__field--full"><span>Full name</span><input type="text" name="name" autocomplete="name" required placeholder="Jordan Avery"></label>
            <label class="msf-01__field msf-01__field--full"><span>Street address</span><input type="text" name="address" autocomplete="street-address" required placeholder="2482 Maple Court"></label>
            <label class="msf-01__field"><span>City</span><input type="text" name="city" autocomplete="address-level2" required placeholder="Austin"></label>
            <label class="msf-01__field"><span>ZIP code</span><input type="text" name="zip" autocomplete="postal-code" inputmode="numeric" pattern="[0-9]{5}(-[0-9]{4})?" required placeholder="78701"></label>
          </div>
          <div class="msf-01__nav"><span></span><button type="button" class="msf-01__next">Continue to payment</button></div>
        </fieldset>
        <fieldset class="msf-01__step" hidden>
          <h3 class="msf-01__title" tabindex="-1">How would you like to pay?</h3>
          <div class="msf-01__grid">
            <label class="msf-01__field msf-01__field--full"><span>Card number</span><input type="text" name="card" autocomplete="cc-number" inputmode="numeric" pattern="[0-9 ]{15,19}" required placeholder="4242 4242 4242 4242"></label>
            <label class="msf-01__field"><span>Expiry</span><input type="text" name="exp" autocomplete="cc-exp" pattern="(0[1-9]|1[0-2])\/[0-9]{2}" required placeholder="MM/YY"></label>
            <label class="msf-01__field"><span>CVC</span><input type="text" name="cvc" autocomplete="cc-csc" inputmode="numeric" pattern="[0-9]{3,4}" required placeholder="123"></label>
          </div>
          <div class="msf-01__nav"><button type="button" class="msf-01__back">Back</button><button type="button" class="msf-01__next">Review order</button></div>
        </fieldset>
        <fieldset class="msf-01__step" hidden>
          <h3 class="msf-01__title" tabindex="-1">Everything look right?</h3>
          <dl class="msf-01__review" aria-live="polite"></dl>
          <div class="msf-01__nav"><button type="button" class="msf-01__back">Back</button><button type="button" class="msf-01__next msf-01__next--go">Place order · $148.00</button></div>
        </fieldset>
        <div class="msf-01__done" hidden><b>✓</b><h3>Order placed!</h3><p>A confirmation is on its way to your inbox.</p></div>
      </div>
      <aside class="msf-01__summary" aria-label="Order summary">
        <h4>Order summary</h4>
        <div class="msf-01__row"><span>Studio headphones</span><b>$129.00</b></div>
        <div class="msf-01__row"><span>Carry case</span><b>$19.00</b></div>
        <div class="msf-01__row msf-01__row--muted"><span>Shipping</span><b>Free</b></div>
        <div class="msf-01__row msf-01__row--total"><span>Total</span><b>$148.00</b></div>
      </aside>
    </div>
  </form>
</section>
```
## CSS
```css
.msf-01,
.msf-01 *,
.msf-01 *::before,
.msf-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msf-01 {
  width: 100%;
  min-height: 100vh;
  --brand: oklch(0.55 0.2 262);
  --ink: oklch(0.25 0.03 262);
  --line: oklch(0.9 0.01 262);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  padding: 48px 20px;
  background: oklch(0.97 0.005 262);
  display: grid;
  place-items: center;
}

.msf-01__form {
  width: min(860px,100%);
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 24px 60px -30px oklch(0.55 0.2 262 / .25);
  overflow: hidden;
}

.msf-01__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
  padding: 20px 28px;
  border-bottom: 1px solid var(--line);
}

.msf-01__logo {
  font-size: 18px;
  letter-spacing: -.02em;
}

.msf-01__logo b {
  color: var(--brand);
}

.msf-01__stepper {
  position: relative;
  display: flex;
  gap: 34px;
  list-style: none;
  counter-reset: s;
}

.msf-01__stepper::before {
  content: "";
  position: absolute;
  left: 14px;
  right: 14px;
  top: 14px;
  height: 2px;
  background: var(--line);
}

.msf-01__stepper::after {
  content: "";
  position: absolute;
  left: 14px;
  right: 14px;
  top: 14px;
  height: 2px;
  background: var(--brand);
  transform: scaleX(var(--progress));
  transform-origin: left;
  transition: transform .45s cubic-bezier(.4,0,.2,1);
}

.msf-01__dot {
  position: relative;
  z-index: 1;
  display: grid;
  justify-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  color: oklch(0.55 0.02 262);
}

.msf-01__dot i {
  font-style: normal;
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #fff;
  border: 2px solid var(--line);
  font-size: 12px;
  transition: all .3s;
}

.msf-01__dot.is-active {
  color: var(--brand);
}

.msf-01__dot.is-active i {
  border-color: var(--brand);
  color: var(--brand);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--brand) 15%,transparent);
}

.msf-01__dot.is-done i {
  background: var(--brand);
  border-color: var(--brand);
  color: #fff;
}

.msf-01__body {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
}

@media (max-width: 720px) {
  .msf-01__body {
    grid-template-columns: 1fr;
  }
}

.msf-01__steps {
  padding: 28px;
}

.msf-01__step {
  border: none;
}

.msf-01__title {
  font-size: 20px;
  letter-spacing: -.01em;
  margin-bottom: 18px;
  outline: none;
}

.msf-01__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.msf-01__field {
  display: grid;
  gap: 6px;
  font-size: 12.5px;
  font-weight: 600;
  color: oklch(0.45 0.02 262);
}

.msf-01__field--full {
  grid-column: 1/-1;
}

.msf-01__field input {
  font: inherit;
  font-weight: 500;
  color: var(--ink);
  padding: 11px 13px;
  border: 1.5px solid var(--line);
  border-radius: 10px;
  transition: border-color .2s,box-shadow .2s;
}

.msf-01__field input:focus-visible {
  outline: none;
  border-color: var(--brand);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--brand) 14%,transparent);
}

.msf-01__field input[aria-invalid="true"] {
  border-color: oklch(0.55 0.2 25);
  box-shadow: 0 0 0 4px oklch(0.55 0.2 25 / .12);
}

.msf-01__err {
  grid-column: 1/-1;
  font-size: 12px;
  font-weight: 600;
  color: oklch(0.52 0.2 25);
}

.msf-01__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-top: 24px;
}

.msf-01__next,
.msf-01__back {
  font: inherit;
  font-weight: 700;
  cursor: pointer;
  border-radius: 10px;
  padding: 12px 22px;
  transition: transform .15s,box-shadow .2s,background .2s;
}

.msf-01__next {
  border: none;
  color: #fff;
  background: var(--brand);
  box-shadow: 0 10px 24px -10px var(--brand);
}

.msf-01__next:hover {
  transform: translateY(-1px);
  background: color-mix(in oklab,var(--brand) 88%,black);
}

.msf-01__next--go {
  background: oklch(0.55 0.17 155);
  box-shadow: 0 10px 24px -10px oklch(0.55 0.17 155);
}

.msf-01__back {
  border: 1.5px solid var(--line);
  background: #fff;
  color: var(--ink);
}

.msf-01__back:hover {
  border-color: var(--brand);
  color: var(--brand);
}

.msf-01__next:focus-visible,
.msf-01__back:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 2px;
}

.msf-01__review {
  display: grid;
  gap: 10px;
  font-size: 14px;
}

.msf-01__review div {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 10px 14px;
  background: oklch(0.97 0.005 262);
  border-radius: 10px;
}

.msf-01__review dt {
  font-weight: 600;
  color: oklch(0.5 0.02 262);
}

.msf-01__review dd {
  font-weight: 600;
}

.msf-01__done[hidden] {
  display: none;
}

.msf-01__done {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  padding: 32px 0;
}

.msf-01__done b {
  display: grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: oklch(0.55 0.17 155);
  color: #fff;
  font-size: 24px;
  animation: msf-01-pop .5s cubic-bezier(.34,1.56,.64,1);
}

.msf-01__done p {
  color: oklch(0.5 0.02 262);
  font-size: 14px;
}

.msf-01__summary {
  padding: 28px;
  background: oklch(0.975 0.008 262);
  border-left: 1px solid var(--line);
  display: grid;
  gap: 12px;
  align-content: start;
  font-size: 14px;
}

@media (max-width: 720px) {
  .msf-01__summary {
    border-left: none;
    border-top: 1px solid var(--line);
  }
}

.msf-01__summary h4 {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: oklch(0.5 0.02 262);
}

.msf-01__row {
  display: flex;
  justify-content: space-between;
}

.msf-01__row--muted {
  color: oklch(0.55 0.02 262);
}

.msf-01__row--total {
  border-top: 1px solid var(--line);
  padding-top: 12px;
  font-size: 16px;
}

.msf-01__step:not([hidden]) {
  animation: msf-01-in .35s cubic-bezier(.2,.8,.2,1);
}

@keyframes msf-01-in {
  from {
    opacity: 0;
    transform: translateX(14px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@keyframes msf-01-pop {
  from {
    transform: scale(.4);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .msf-01 * {
    animation: none!important;
    transition-duration: .01ms!important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.msf-01'); if (!root) return;
  const form = root.querySelector('.msf-01__form');
  const steps = [...root.querySelectorAll('.msf-01__step')];
  const dots = [...root.querySelectorAll('.msf-01__dot')];
  const stepper = root.querySelector('.msf-01__stepper');
  let cur = 0;
  const validate = (fs) => {
    let ok = true;
    fs.querySelectorAll('.msf-01__err').forEach(e => e.remove());
    fs.querySelectorAll('input').forEach(inp => {
      const bad = !inp.checkValidity();
      inp.setAttribute('aria-invalid', bad);
      if (bad && ok) {
        ok = false;
        const err = document.createElement('p');
        err.className = 'msf-01__err'; err.id = 'msf-01-err'; err.setAttribute('role','alert');
        err.textContent = inp.validity.valueMissing ? 'Please fill in the highlighted fields.' : 'Please check the highlighted format (e.g. ' + inp.placeholder + ').';
        inp.closest('.msf-01__grid').append(err);
        inp.setAttribute('aria-describedby','msf-01-err');
        inp.focus();
      }
    });
    return ok;
  };
  const show = (i) => {
    cur = i;
    steps.forEach((s, k) => s.hidden = k !== i);
    dots.forEach((d, k) => {
      d.classList.toggle('is-active', k === i);
      d.classList.toggle('is-done', k < i);
      k === i ? d.setAttribute('aria-current','step') : d.removeAttribute('aria-current');
    });
    stepper.style.setProperty('--progress', (i / (steps.length - 1)).toFixed(2));
    if (i === steps.length - 1) buildReview();
    steps[i].querySelector('.msf-01__title').focus();
  };
  const buildReview = () => {
    const d = new FormData(form);
    root.querySelector('.msf-01__review').innerHTML =
      [['Ship to', d.get('name') + ', ' + d.get('address') + ', ' + d.get('city') + ' ' + d.get('zip')],
       ['Card', '•••• ' + String(d.get('card')).replace(/\D/g,'').slice(-4) + '  exp ' + d.get('exp')],
       ['Total', '$148.00']]
      .map(([k, v]) => '<div><dt>' + k + '</dt><dd>' + v + '</dd></div>').join('');
  };
  root.addEventListener('click', (e) => {
    if (e.target.closest('.msf-01__next:not(.msf-01__next--go):not(.msf-01__submit):not(.msf-01__skip)')) { if (validate(steps[cur])) show(cur + 1); }
    if (e.target.closest('.msf-01__back')) show(cur - 1);
  });
  root.addEventListener('click', (e) => {
    if (!e.target.closest('.msf-01__next--go, .msf-01__submit, .msf-01__skip')) return;

    e.preventDefault();
    root.querySelector('.msf-01__steps').style.minHeight = root.querySelector('.msf-01__steps').offsetHeight + 'px';
    steps.forEach(s => s.hidden = true);
    dots.forEach(d => { d.classList.add('is-done'); d.classList.remove('is-active'); });
    stepper.style.setProperty('--progress','1');
    const done = root.querySelector('.msf-01__done'); done.hidden = false;
    done.querySelector('h3').setAttribute('tabindex','-1'); done.querySelector('h3').focus();
    });
})();
```
