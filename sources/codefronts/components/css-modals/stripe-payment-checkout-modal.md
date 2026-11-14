---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/stripe-payment-checkout-modal/"
title: "Stripe Payment Checkout Modal"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A Stripe Elements-style payment checkout modal with a signature 3D Paper Fold entrance — the modal opens like an envelope unfolding via rotateX(-70deg → 0)…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stripe Payment Checkout Modal
Source: https://codefronts.com/components/css-modals/stripe-payment-checkout-modal/

A Stripe Elements-style payment checkout modal with a signature 3D Paper Fold entrance — the modal opens like an envelope unfolding via rotateX(-70deg → 0) with perspective on the parent, giving the payment surface a distinct arrival that reads as "opening a physical checkout" rather than a generic overlay. Muted intensity (70° start instead of 90°, no overshoot) because payment forms require trust — the fold is present but subtle enough to not undermine the transactional gravity.
## HTML
```html
<div class="md-04">
  <button class="md-04__trigger" id="md-04-open">Complete purchase · $29.00</button>
  <div class="md-04__backdrop" id="md-04-dialog" role="dialog" aria-modal="true" aria-labelledby="md-04-title">
    <div class="md-04__stage">
      <div class="md-04__modal">
        <button class="md-04__x md-04__close" aria-label="Close">✕</button>
        <div class="md-04__brand">
          <span class="md-04__lock" aria-hidden="true">🔒</span>
          Secured by Stripe
        </div>
        <h2 class="md-04__title" id="md-04-title">Complete your purchase</h2>
        <div class="md-04__summary">
          <div class="md-04__row"><span>Pro plan · monthly</span><strong>$25.00</strong></div>
          <div class="md-04__row"><span>Tax (16%)</span><strong>$4.00</strong></div>
          <div class="md-04__row md-04__row--total"><span>Total</span><strong>$29.00 USD</strong></div>
        </div>
        <form class="md-04__form" onsubmit="event.preventDefault()">
          <label class="md-04__label">
            <span>Card number</span>
            <input type="text" name="cc-number" autocomplete="cc-number" placeholder="1234 1234 1234 1234" inputmode="numeric" required />
          </label>
          <div class="md-04__row-fields">
            <label class="md-04__label">
              <span>Expiry</span>
              <input type="text" name="cc-exp" autocomplete="cc-exp" placeholder="MM / YY" inputmode="numeric" required />
            </label>
            <label class="md-04__label">
              <span>CVC</span>
              <input type="text" name="cc-csc" autocomplete="cc-csc" placeholder="CVC" inputmode="numeric" pattern="[0-9]{3,4}" required />
            </label>
          </div>
          <div class="md-04__row-fields">
            <label class="md-04__label md-04__label--wide">
              <span>Cardholder name</span>
              <input type="text" name="cc-name" autocomplete="cc-name" placeholder="Alex Chen" required />
            </label>
            <label class="md-04__label">
              <span>ZIP</span>
              <input type="text" name="postal-code" autocomplete="postal-code" placeholder="94103" required />
            </label>
          </div>
          <button type="submit" class="md-04__submit">Pay $29.00</button>
        </form>
        <div class="md-04__foot">
          <span class="md-04__cards" aria-hidden="true">VISA · MC · AMEX · DISC</span>
          <p>You'll be charged $29.00 today. Cancel anytime.</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-04 {
  --page-bg: #f7f8fa;
  --card: #ffffff;
  --input: #ffffff;
  --input-border: #e6e8ec;
  --ink: #0a0e27;
  --sub: #697386;
  --brand: #635bff;
  --brand-tint: rgba(99,91,255,.06);
  --line: #e6e8ec;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  background: var(--page-bg);
  color: var(--ink);
}

.md-04 *,
.md-04 *::before,
.md-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-04 ::selection {
  background: var(--brand);
  color: #fff;
}

.md-04__trigger {
  padding: 12px 26px;
  border: none;
  border-radius: 8px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 8px 20px -6px rgba(99,91,255,.5);
  transition: transform .12s ease,background .18s ease;
}

.md-04__trigger:hover {
  background: #4f46e5;
  transform: translateY(-1px);
}

.md-04__backdrop {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background: rgba(10,14,39,.55);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .25s ease,visibility 0s linear .25s;
}

.md-04__backdrop.is-open {
  opacity: 1;
  visibility: visible;
  transition: opacity .25s ease,visibility 0s linear 0s;
}
/* 3D stage for Paper Fold — perspective gives depth to the envelope opening */

.md-04__stage {
  perspective: 1600px;
  width: min(460px,100%);
}

.md-04__modal {
  position: relative;
  padding: 32px 32px 24px;
  border-radius: 12px;
  background: var(--card);
  box-shadow: 0 40px 60px -20px rgba(10,14,39,.35);
  /* Signature entrance: 3D Paper Fold — modal unfolds from top like envelope */
  opacity: 0;
  transform: rotateX(-70deg);
  transform-origin: top center;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transition: opacity .3s ease .05s,transform .5s cubic-bezier(.22,1,.36,1) .05s;
}

.md-04__backdrop.is-open .md-04__modal {
  opacity: 1;
  transform: rotateX(0);
}

.md-04__x {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--sub);
  font-family: inherit;
  font-size: 16px;
  cursor: pointer;
  transition: background .18s ease,color .18s ease;
}

.md-04__x:hover {
  background: #f1f5f9;
  color: var(--ink);
}

.md-04__brand {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: .72rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
  margin-bottom: 14px;
}

.md-04__lock {
  font-size: 12px;
}

.md-04__title {
  font-size: 1.45rem;
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1.2;
  margin-bottom: 18px;
}

.md-04__summary {
  padding: 16px 18px;
  background: #fafbfc;
  border: 1px solid var(--line);
  border-radius: 9px;
  margin-bottom: 20px;
}

.md-04__row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 5px 0;
  font-size: .88rem;
  color: var(--sub);
}

.md-04__row strong {
  color: var(--ink);
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.md-04__row--total {
  padding-top: 10px;
  margin-top: 5px;
  border-top: 1px solid var(--line);
  font-size: .95rem;
}

.md-04__row--total span {
  font-weight: 700;
  color: var(--ink);
}

.md-04__row--total strong {
  font-size: 1rem;
  font-weight: 800;
}

.md-04__form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 18px;
}

.md-04__label {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.md-04__label span {
  font-size: .75rem;
  font-weight: 600;
  color: var(--sub);
  letter-spacing: .02em;
}

.md-04__label input {
  padding: 11px 14px;
  border: 1px solid var(--input-border);
  border-radius: 8px;
  background: var(--input);
  color: var(--ink);
  font-family: inherit;
  font-size: .92rem;
  font-variant-numeric: tabular-nums;
  transition: border-color .18s ease,box-shadow .18s ease;
}

.md-04__label input:focus {
  outline: none;
  border-color: var(--brand);
  box-shadow: 0 0 0 3px var(--brand-tint);
}

.md-04__row-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.md-04__label--wide {
  grid-column: span 1;
}

.md-04__submit {
  padding: 13px 22px;
  border: none;
  border-radius: 8px;
  background: var(--brand);
  color: #fff;
  font-family: inherit;
  font-size: .98rem;
  font-weight: 700;
  cursor: pointer;
  font-variant-numeric: tabular-nums;
  transition: background .18s ease,transform .12s ease;
  margin-top: 6px;
}

.md-04__submit:hover {
  background: #4f46e5;
}

.md-04__submit:active {
  transform: translateY(1px);
}

.md-04__submit:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 3px;
}

.md-04__foot {
  padding-top: 16px;
  border-top: 1px solid var(--line);
  text-align: center;
}

.md-04__cards {
  display: block;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: .72rem;
  font-weight: 700;
  color: var(--sub);
  letter-spacing: .14em;
  margin-bottom: 6px;
}

.md-04__foot p {
  font-size: .72rem;
  color: var(--sub);
}

@media (prefers-reduced-motion: reduce) {
  .md-04__backdrop,
    .md-04__modal {
    transition: none!important;
  }

  .md-04__modal {
    transform: none!important;
  }
}

@media (max-width: 400px) {
  .md-04__row-fields {
    grid-template-columns: 1fr;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.md-04');
  if (!root) return;
  var openBtn = root.querySelector('#md-04-open');
  var dialog = root.querySelector('#md-04-dialog');
  var closeBtns = root.querySelectorAll('.md-04__close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    dialog.classList.add('is-open');
    document.documentElement.style.overflow = 'hidden';
    var firstInput = dialog.querySelector('input[autocomplete=cc-number]');
    if (firstInput) firstInput.focus();
    document.addEventListener('keydown', onKey);
  }
  function close() {
    dialog.classList.remove('is-open');
    document.documentElement.style.overflow = '';
    document.removeEventListener('keydown', onKey);
    if (lastFocus) lastFocus.focus();
  }
  function onKey(e) {
    if (e.key === 'Escape') {
      var hasInput = Array.prototype.some.call(dialog.querySelectorAll('input'), function(i){ return i.value.length > 0; });
      if (hasInput) {
        if (!confirm('You have unsaved payment info. Leave anyway?')) return;
      }
      close();
    }
  }

  openBtn.addEventListener('click', open);
  closeBtns.forEach(function(b){ b.addEventListener('click', close); });
  dialog.addEventListener('click', function(e){ if (e.target === dialog) close(); });
})();
```
