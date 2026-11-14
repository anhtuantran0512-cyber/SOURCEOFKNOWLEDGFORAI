---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/checkout-pay-button-with-pending-lock/"
title: "Checkout Pay Button with Pending Lock"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "The highest-stakes async button on the web."
has_js: "true"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Checkout Pay Button with Pending Lock
Source: https://codefronts.com/components/css-loading-buttons/checkout-pay-button-with-pending-lock/

The highest-stakes async button on the web. It locks for the full duration of the charge, states plainly that the window must stay open, holds a minimum visible duration so a fast authorisation cannot flicker, and never finds its own way back to idle — only an explicit success or an explicit decline moves it. Deliberately a payment button, not an add-to-cart button.
## HTML
```html
<div class="lb-11">
  <div class="lb-11__stage">
    <section class="lb-11__checkout" aria-labelledby="lb-11-h">
      <p class="lb-11__eyebrow">Order 4471-B</p>
      <h2 class="lb-11__h" id="lb-11-h">Confirm and pay</h2>

      <dl class="lb-11__lines">
        <div class="lb-11__line"><dt>Field Notes annual</dt><dd>$108.00</dd></div>
        <div class="lb-11__line"><dt>Archive access</dt><dd>$14.00</dd></div>
        <div class="lb-11__line"><dt>Tax</dt><dd>$6.40</dd></div>
        <div class="lb-11__line lb-11__line--total"><dt>Total</dt><dd>$128.40</dd></div>
      </dl>

      <p class="lb-11__card">Visa ending 4242 · Alex Chen</p>

      <button class="lb-11__pay" type="button" id="lb-11-btn" data-state="idle" aria-busy="false">
        <span class="lb-11__spin" aria-hidden="true"></span>
        <span class="lb-11__paylabel" id="lb-11-label">Pay $128.40</span>
      </button>

      <p class="lb-11__warn" id="lb-11-warn">Do not close this window while the payment is processing.</p>
      <p class="lb-11__live" id="lb-11-live" role="status" aria-live="polite">Card on file. Nothing has been charged yet.</p>
      <p class="lb-11__alert" id="lb-11-alert" role="alert"></p>

      <label class="lb-11__toggle"><input type="checkbox" id="lb-11-decline"> Simulate a declined card</label>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f4f1ea;
  --surface: #fffefb;
  --ink: #1a1916;
  --muted: #6f6a60;
  --rule: #e2ddd1;
  --accent: #1a1916;
  --on-accent: #fffefb;
  --ok: #1f6f4a;
  --bad: #a02f22;
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  background: var(--paper);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-11 *,
.lb-11 *::before,
.lb-11 *::after {
  box-sizing: border-box;
}

.lb-11__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-11__checkout {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 26px 24px 22px;
  box-shadow: 0 24px 48px -34px rgba(26, 25, 22, .55);
}

.lb-11__eyebrow {
  margin: 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 10.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.lb-11__h {
  margin: 8px 0 20px;
  font-size: 25px;
  font-weight: 500;
  letter-spacing: -.02em;
}

.lb-11__lines {
  margin: 0;
  display: grid;
  gap: 9px;
  padding-block-end: 14px;
  border-block-end: 1px solid var(--rule);
}

.lb-11__line {
  display: flex;
  gap: 14px;
  justify-content: space-between;
  font-size: 14px;
  min-inline-size: 0;
}

.lb-11__line dt {
  color: var(--muted);
  min-inline-size: 0;
}

.lb-11__line dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
  flex: none;
}

.lb-11__line--total {
  padding-block-start: 9px;
  border-block-start: 1px solid var(--rule);
  font-size: 16px;
}

.lb-11__line--total dt,
.lb-11__line--total dd {
  color: var(--ink);
  font-weight: 600;
}

.lb-11__card {
  margin: 14px 0 18px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 12px;
  color: var(--muted);
}

.lb-11__pay {
  appearance: none;
  inline-size: 100%;
  border: 0;
  background: var(--accent);
  color: var(--on-accent);
  border-radius: 8px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 14.5px;
  font-weight: 600;
  padding: 0 18px;
  min-block-size: 52px;
  min-inline-size: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  cursor: pointer;
  transition: background 200ms ease, opacity 200ms ease;
}

.lb-11__pay:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-11__pay:disabled {
  cursor: progress;
  opacity: .9;
}

.lb-11__pay[data-state="done"] {
  background: var(--ok);
}

.lb-11__pay[data-state="error"] {
  background: var(--bad);
}

.lb-11__paylabel {
  min-inline-size: 0;
}

.lb-11__spin {
  inline-size: 0;
  block-size: 16px;
  border-radius: 50%;
  border: 2px solid currentColor;
  border-inline-end-color: transparent;
  opacity: 0;
  transition: inline-size 160ms ease, opacity 160ms ease;
}

.lb-11__pay[data-state="pending"] .lb-11__spin {
  inline-size: 16px;
  opacity: 1;
  animation: lb-11-spin 680ms linear infinite;
}

@keyframes lb-11-spin {
  to {
    transform: rotate(1turn);
  }
}

.lb-11__warn {
  margin: 12px 0 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: var(--bad);
  visibility: hidden;
  min-inline-size: 0;
}

.lb-11[data-charging="true"] .lb-11__warn {
  visibility: visible;
}

.lb-11__live {
  margin: 10px 0 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 12px;
  color: var(--muted);
  min-inline-size: 0;
}

.lb-11__alert {
  margin: 6px 0 0;
  min-block-size: 17px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--bad);
  min-inline-size: 0;
}

.lb-11__toggle {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin: 10px 0 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
}

.lb-11__toggle input {
  accent-color: var(--accent);
  inline-size: 15px;
  block-size: 15px;
}

@media (prefers-reduced-motion: reduce) {
  .lb-11__spin {
    animation: none !important;
    transition: none;
  }

  .lb-11__pay[data-state="pending"] .lb-11__spin {
    border-inline-end-color: currentColor;
    opacity: .55;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-11 {
    --paper: #14130f;
    --surface: #1c1a16;
    --ink: #f1ede3;
    --muted: #a29a8b;
    --rule: #302c24;
    --accent: #f1ede3;
    --on-accent: #14130f;
    --ok: #58b98a;
    --bad: #ef8171;
  }
}

[data-theme="dark"] .lb-11 {
  --paper: #14130f;
  --surface: #1c1a16;
  --ink: #f1ede3;
  --muted: #a29a8b;
  --rule: #302c24;
  --accent: #f1ede3;
  --on-accent: #14130f;
  --ok: #58b98a;
  --bad: #ef8171;
}
```

## JavaScript
```js
const root = document.querySelector('.lb-11');
const btn = document.getElementById('lb-11-btn');
const label = document.getElementById('lb-11-label');
const live = document.getElementById('lb-11-live');
const alertBox = document.getElementById('lb-11-alert');
const decline = document.getElementById('lb-11-decline');
const FLOOR = 600;
let timer;
let key = '';

const guard = (event) => { event.preventDefault(); return ''; };

btn.addEventListener('click', () => {
  if (btn.disabled) return;
  clearTimeout(timer);
  key = self.crypto && crypto.randomUUID ? crypto.randomUUID().slice(0, 8) : String(Math.random()).slice(2, 10);
  btn.disabled = true;
  btn.dataset.state = 'pending';
  btn.setAttribute('aria-busy', 'true');
  root.dataset.charging = 'true';
  label.textContent = 'Processing payment';
  alertBox.textContent = '';
  live.textContent = 'Authorising card, idempotency key ' + key;
  window.addEventListener('beforeunload', guard);
  const started = performance.now();
  timer = setTimeout(() => {
    const held = Math.max(0, FLOOR - (performance.now() - started));
    timer = setTimeout(() => {
      window.removeEventListener('beforeunload', guard);
      root.dataset.charging = 'false';
      btn.setAttribute('aria-busy', 'false');
      if (decline.checked) {
        btn.dataset.state = 'error';
        btn.disabled = false;
        label.textContent = 'Try another card';
        alertBox.textContent = 'Declined by the issuer (code 51). Nothing was charged. Retry reuses key ' + key + '.';
      } else {
        btn.dataset.state = 'done';
        label.textContent = 'Paid $128.40';
        live.textContent = 'Payment authorised. Receipt sent to [email protected].';
      }
    }, held);
  }, 900);
});
```
