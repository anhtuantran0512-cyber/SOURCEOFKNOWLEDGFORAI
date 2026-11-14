---
source: "codefronts"
url: "https://codefronts.com/components/css-form-validation/minimalist-checkout-field-validation/"
title: "Minimalist Checkout Field Validation"
section: "components"
category: "css-form-validation"
category_name: "CSS Form Validation"
description: "Card number, expiry and CVC in a dense three-field grid."
has_js: "true"
---

Here's a working CSS Form Validation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Checkout Field Validation
Source: https://codefronts.com/components/css-form-validation/minimalist-checkout-field-validation/

Card number, expiry and CVC in a dense three-field grid. Format comes from pattern and inputmode="numeric", and a Luhn check runs through setCustomValidity() so the native constraint system delivers the verdict. The autocomplete tokens are the detail most checkout demos get wrong — cc-number, cc-exp and cc-csc are what make browser autofill work at all.
## HTML
```html
<section class="fv-15" aria-labelledby="fv-15-h">
  <fieldset class="fv-15__theme">
    <legend class="fv-15__themelegend">Theme</legend>
    <input class="fv-15__themeinput" type="radio" name="fv-15-theme" id="fv-15-theme-auto" checked>
    <label class="fv-15__themeopt" for="fv-15-theme-auto">Auto</label>
    <input class="fv-15__themeinput" type="radio" name="fv-15-theme" id="fv-15-theme-light">
    <label class="fv-15__themeopt" for="fv-15-theme-light">Light</label>
    <input class="fv-15__themeinput" type="radio" name="fv-15-theme" id="fv-15-theme-dark">
    <label class="fv-15__themeopt" for="fv-15-theme-dark">Dark</label>
  </fieldset>
  <div class="fv-15__stage">
    <form class="fv-15__form" data-brand="none" aria-labelledby="fv-15-h">
      <header class="fv-15__head">
        <p class="fv-15__eyebrow">Aesop · order 44 812</p>
        <h2 class="fv-15__h" id="fv-15-h">Payment</h2>
        <p class="fv-15__total">£148.00 · delivery included</p>
      </header>

      <div class="fv-15__field fv-15__field--wide">
        <div class="fv-15__labelrow">
          <label class="fv-15__label" for="fv-15-number">Card number</label>
          <span class="fv-15__brand">Card</span>
        </div>
        <input class="fv-15__input" id="fv-15-number" name="fv-15-number" type="text" required pattern="[0-9]{13,19}" inputmode="numeric" autocomplete="cc-number" placeholder="4242424242424242" value="4242424242424241" aria-describedby="fv-15-number-msg">
        <p class="fv-15__msg" id="fv-15-number-msg">
          <svg class="fv-15__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
          <span>Check the card number — one of the digits is off</span>
        </p>
      </div>

      <div class="fv-15__row">
        <div class="fv-15__field">
          <label class="fv-15__label" for="fv-15-exp">Expiry</label>
          <input class="fv-15__input" id="fv-15-exp" name="fv-15-exp" type="text" required pattern="(0[1-9]|1[0-2])/[0-9]{2}" inputmode="numeric" autocomplete="cc-exp" placeholder="04/29" value="04/29" aria-describedby="fv-15-exp-msg">
          <p class="fv-15__msg" id="fv-15-exp-msg">
            <svg class="fv-15__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>Use MM/YY, like 04/29</span>
          </p>
        </div>

        <div class="fv-15__field">
          <label class="fv-15__label" for="fv-15-cvc">CVC</label>
          <input class="fv-15__input" id="fv-15-cvc" name="fv-15-cvc" type="text" required pattern="[0-9]{3,4}" inputmode="numeric" autocomplete="cc-csc" placeholder="123" value="12" aria-describedby="fv-15-cvc-msg">
          <p class="fv-15__msg" id="fv-15-cvc-msg">
            <svg class="fv-15__icon" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8" fill="none" stroke="currentColor" stroke-width="1.7"></circle><path d="M10 5.9v5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"></path><circle cx="10" cy="14.2" r="1.05" fill="currentColor"></circle></svg>
            <span>3 digits on the back, or 4 on the front for Amex</span>
          </p>
        </div>
      </div>

      <div class="fv-15__field fv-15__field--wide">
        <label class="fv-15__label" for="fv-15-name">Name on card</label>
        <input class="fv-15__input fv-15__input--text" id="fv-15-name" name="fv-15-name" type="text" required autocomplete="cc-name" placeholder="Alex Chen" value="Alex Chen">
      </div>

      <button class="fv-15__btn" type="button">Pay £148.00</button>
      <p class="fv-15__legal">Luhn runs locally through <code>setCustomValidity()</code>. It catches typos, not declines.</p>
    </form>
  </div>
</section>
```
## CSS
```css
.fv-15 {
  --page: #e8e4dd;
  --surface: #f7f5f1;
  --well: #efece6;
  --ink: #23211d;
  --muted: #6d6862;
  --rule: #cfc9c0;
  --accent: #3f3a33;
  --error: #9b2c2c;
  --error-ink: #83201f;
  --inset: inset 0 1px 2px rgba(35, 33, 29, 0.12);
  --font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  --font-num: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

@supports (color: oklch(0 0 0)) {
  .fv-15 {
    --error: oklch(0.44 0.16 25);
    --error-ink: oklch(0.38 0.16 25);
  }
}

.fv-15 *,
.fv-15 *::before,
.fv-15 *::after {
  box-sizing: border-box;
}

.fv-15__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  max-inline-size: 100%;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
}

.fv-15__form {
  inline-size: min(100%, 27rem);
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
  padding: clamp(1.125rem, 3.5vw, 1.625rem);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 0.125rem;
}

.fv-15__head {
  min-inline-size: 0;
  margin-block-end: 0.25rem;
}

.fv-15__eyebrow {
  margin: 0 0 0.375rem;
  font-size: 0.625rem;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-15__h {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 3.6vw, 1.7rem);
  font-weight: 500;
  letter-spacing: -0.01em;
  line-height: 1.1;
}

.fv-15__total {
  margin: 0;
  font-family: var(--font-num);
  font-size: 0.8125rem;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}

.fv-15__row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 7.5rem), 1fr));
  gap: 0.75rem;
  min-inline-size: 0;
}

.fv-15__field {
  display: grid;
  gap: 0.3125rem;
  min-inline-size: 0;
  align-content: start;
}

.fv-15__labelrow {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.5rem;
  min-inline-size: 0;
}

.fv-15__label {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.fv-15__brand {
  padding: 0.1rem 0.4rem;
  border: 1px solid var(--rule);
  border-radius: 0.125rem;
  background: var(--well);
  font-family: var(--font-num);
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.fv-15__form[data-brand="Visa"] .fv-15__brand,
.fv-15__form[data-brand="Mastercard"] .fv-15__brand,
.fv-15__form[data-brand="Amex"] .fv-15__brand {
  border-color: var(--accent);
  color: var(--ink);
  background: #ffffff;
}

.fv-15__input {
  min-inline-size: 0;
  inline-size: 100%;
  block-size: 2.75rem;
  padding: 0 0.75rem;
  font-family: var(--font-num);
  font-size: 0.9375rem;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.06em;
  color: var(--ink);
  background: var(--well);
  border: 1px solid var(--rule);
  border-radius: 0.125rem;
  box-shadow: var(--inset);
}

.fv-15__input--text {
  font-family: system-ui, sans-serif;
  letter-spacing: 0.01em;
}

.fv-15__input::placeholder {
  color: #a6a097;
}

.fv-15__input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fv-15__msg {
  display: none;
  gap: 0.375rem;
  align-items: flex-start;
  margin: 0;
  min-inline-size: 0;
  font-size: 0.75rem;
  line-height: 1.45;
  color: var(--error-ink);
}

.fv-15__msg span {
  min-inline-size: 0;
}

.fv-15__icon {
  flex: none;
  inline-size: 0.9375rem;
  block-size: 0.9375rem;
  margin-block-start: 0.1rem;
}

.fv-15__input:invalid:not(:placeholder-shown):not(:focus) {
  border-color: var(--error);
  box-shadow: var(--inset), inset 0 -2px 0 var(--error);
}

.fv-15__input:invalid:not(:placeholder-shown):not(:focus) + .fv-15__msg {
  display: flex;
}

.fv-15__input:user-invalid {
  border-color: var(--error);
  box-shadow: var(--inset), inset 0 -2px 0 var(--error);
}

.fv-15__input:user-invalid + .fv-15__msg {
  display: flex;
}

.fv-15__input:user-valid {
  border-color: #4a6b4a;
}

.fv-15__btn {
  min-block-size: 2.875rem;
  min-inline-size: 44px;
  margin-block-start: 0.25rem;
  padding: 0.8125rem 1.25rem;
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--surface);
  background: var(--ink);
  border: 0;
  border-radius: 0.125rem;
  cursor: pointer;
}

.fv-15__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fv-15__legal {
  margin: 0;
  min-inline-size: 0;
  font-size: 0.6875rem;
  line-height: 1.5;
  color: var(--muted);
}

.fv-15__legal code {
  font-family: var(--font-num);
  font-size: 0.94em;
}

@media (prefers-color-scheme: dark) {
  .fv-15:not(:has(#fv-15-theme-light:checked)) {
    --page: #141311;
    --surface: #1c1b18;
    --well: #171614;
    --ink: #efece5;
    --muted: #9c968d;
    --rule: #322f2a;
    --accent: #d6cfc2;
    --error: #ff8b7a;
    --error-ink: #ffa697;
    --inset: inset 0 1px 2px rgba(0, 0, 0, 0.5);
  }

  .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__input::placeholder {
    color: #6b665e;
  }

  .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__form[data-brand="Visa"] .fv-15__brand,
    .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__form[data-brand="Mastercard"] .fv-15__brand,
    .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__form[data-brand="Amex"] .fv-15__brand {
    background: #262421;
  }

  .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__btn {
    color: #141311;
    background: #efece5;
  }
}

[data-theme="dark"] .fv-15:not(:has(#fv-15-theme-light:checked)) {
  --page: #141311;
  --surface: #1c1b18;
  --well: #171614;
  --ink: #efece5;
  --muted: #9c968d;
  --rule: #322f2a;
  --accent: #d6cfc2;
  --error: #ff8b7a;
  --error-ink: #ffa697;
}

[data-theme="dark"] .fv-15:not(:has(#fv-15-theme-light:checked)) .fv-15__btn {
  color: #141311;
  background: #efece5;
}

.fv-15 {
  position: relative;
}

.fv-15__stage {
  padding-block-start: 4.75rem;
}

.fv-15__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 6;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 7%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.fv-15__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-15__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.fv-15__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 1.875rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.fv-15__themeopt:hover {
  opacity: 0.85;
}

.fv-15__themeinput:checked + .fv-15__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.fv-15__themeinput:focus-visible + .fv-15__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .fv-15__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .fv-15__themeinput:checked + .fv-15__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

.fv-15:has(#fv-15-theme-dark:checked) {
  --page: #141311;
  --surface: #1c1b18;
  --well: #171614;
  --ink: #efece5;
  --muted: #9c968d;
  --rule: #322f2a;
  --accent: #d6cfc2;
  --error: #ff8b7a;
  --error-ink: #ffa697;
  --inset: inset 0 1px 2px rgba(0, 0, 0, 0.5);
}

.fv-15:has(#fv-15-theme-dark:checked) .fv-15__input::placeholder {
  color: #6b665e;
}

.fv-15:has(#fv-15-theme-dark:checked) .fv-15__form[data-brand="Visa"] .fv-15__brand,
.fv-15:has(#fv-15-theme-dark:checked) .fv-15__form[data-brand="Mastercard"] .fv-15__brand,
.fv-15:has(#fv-15-theme-dark:checked) .fv-15__form[data-brand="Amex"] .fv-15__brand {
  background: #262421;
}

.fv-15:has(#fv-15-theme-dark:checked) .fv-15__btn {
  color: #141311;
  background: #efece5;
}
```

## JavaScript
```js
(() => {
  const form = document.querySelector('.fv-15__form');
  if (!form || form.dataset.fv15) return;
  form.dataset.fv15 = '1';
  const num = form.querySelector('#fv-15-number');
  const chip = form.querySelector('.fv-15__brand');
  const luhn = (s) => {
    let sum = 0, alt = false;
    for (let i = s.length - 1; i >= 0; i -= 1) {
      let d = Number(s[i]);
      if (alt) { d *= 2; if (d > 9) d -= 9; }
      sum += d;
      alt = !alt;
    }
    return sum % 10 === 0;
  };
  const brandOf = (s) => (/^4/.test(s) ? 'Visa' : /^5[1-5]/.test(s) ? 'Mastercard' : /^3[47]/.test(s) ? 'Amex' : '');
  const sync = () => {
    const digits = num.value.replace(/[^0-9]/g, '');
    const brand = brandOf(digits);
    form.dataset.brand = brand || 'none';
    chip.textContent = brand || 'Card';
    num.setCustomValidity(digits.length >= 13 && !luhn(digits) ? 'Check the card number — one of the digits is off.' : '');
  };
  ['input', 'change'].forEach((ev) => num.addEventListener(ev, sync));
  form.querySelector('.fv-15__btn').addEventListener('click', () => { sync(); if (!form.checkValidity()) form.reportValidity(); });
  form.addEventListener('keydown', (e) => { if (e.key === 'Enter' && e.target.tagName === 'INPUT') { e.preventDefault(); sync(); form.reportValidity(); } });
  sync();
})();
```
