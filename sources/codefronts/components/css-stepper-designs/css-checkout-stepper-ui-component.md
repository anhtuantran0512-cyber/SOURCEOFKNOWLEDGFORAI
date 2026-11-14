---
source: "codefronts"
url: "https://codefronts.com/components/css-stepper-designs/css-checkout-stepper-ui-component/"
title: "CSS Checkout Stepper UI Component"
section: "components"
category: "css-stepper-designs"
category_name: "CSS Steppers"
description: "A dark navy e-commerce checkout flow with a tab-rail step header, sidebar order summary, three product line items, running totals, and an SSL trust badge —…"
has_js: "false"
---

Here's a working CSS Stepper from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Checkout Stepper UI Component
Source: https://codefronts.com/components/css-stepper-designs/css-checkout-stepper-ui-component/

A dark navy e-commerce checkout flow with a tab-rail step header, sidebar order summary, three product line items, running totals, and an SSL trust badge — step state driven by JS class toggling.
## HTML
```html
<div class="stp-03">
  <div class="stp-03__shell">
    <!-- Step tabs -->
    <div class="stp-03__bar">
      <div class="stp-03__tab done">
        <div class="stp-03__tab-icon">✓</div>
        <div class="stp-03__tab-info"><div class="stp-03__tab-step">Step 1</div><div class="stp-03__tab-name">Cart</div></div>
      </div>
      <div class="stp-03__tab done">
        <div class="stp-03__tab-icon">✓</div>
        <div class="stp-03__tab-info"><div class="stp-03__tab-step">Step 2</div><div class="stp-03__tab-name">Address</div></div>
      </div>
      <div class="stp-03__tab active">
        <div class="stp-03__tab-icon">3</div>
        <div class="stp-03__tab-info"><div class="stp-03__tab-step">Step 3</div><div class="stp-03__tab-name">Payment</div></div>
      </div>
      <div class="stp-03__tab">
        <div class="stp-03__tab-icon">4</div>
        <div class="stp-03__tab-info"><div class="stp-03__tab-step">Step 4</div><div class="stp-03__tab-name">Review</div></div>
      </div>
    </div>

    <!-- Body -->
    <div class="stp-03__body">
      <div class="stp-03__main">
        <div class="stp-03__section-title">Payment Details</div>
        <div class="stp-03__field">
          <label class="stp-03__field-label">Cardholder Name</label>
          <input class="stp-03__input" placeholder="Jordan Blake" value="Jordan Blake">
        </div>
        <div class="stp-03__field">
          <label class="stp-03__field-label">Card Number</label>
          <input class="stp-03__input" placeholder="4242 4242 4242 4242">
        </div>
        <div class="stp-03__grid3">
          <div class="stp-03__field">
            <label class="stp-03__field-label">Expiry Month</label>
            <input class="stp-03__input" placeholder="MM">
          </div>
          <div class="stp-03__field">
            <label class="stp-03__field-label">Year</label>
            <input class="stp-03__input" placeholder="YY">
          </div>
          <div class="stp-03__field">
            <label class="stp-03__field-label">CVV</label>
            <input class="stp-03__input" placeholder="•••">
          </div>
        </div>
        <div class="stp-03__field" style="margin-top:8px">
          <label class="stp-03__field-label">Billing ZIP</label>
          <input class="stp-03__input" placeholder="90210" style="max-width:160px">
        </div>
      </div>

      <!-- Sidebar -->
      <div class="stp-03__aside">
        <div class="stp-03__aside-title">Order Summary</div>
        <div class="stp-03__item">
          <div class="stp-03__item-thumb" style="background:rgba(14,165,233,.15)">👟</div>
          <div><div class="stp-03__item-name">Air Max Pro</div><div class="stp-03__item-sku">Size 10 · Black</div></div>
          <div class="stp-03__item-price">$129</div>
        </div>
        <div class="stp-03__item">
          <div class="stp-03__item-thumb" style="background:rgba(6,182,212,.15)">🎒</div>
          <div><div class="stp-03__item-name">Trail Pack 24L</div><div class="stp-03__item-sku">Navy · x1</div></div>
          <div class="stp-03__item-price">$89</div>
        </div>
        <div class="stp-03__item">
          <div class="stp-03__item-thumb" style="background:rgba(245,158,11,.15)">🧢</div>
          <div><div class="stp-03__item-name">Sport Cap</div><div class="stp-03__item-sku">One Size · x2</div></div>
          <div class="stp-03__item-price">$38</div>
        </div>
        <div class="stp-03__totals">
          <div class="stp-03__total-row"><span>Subtotal</span><span>$256</span></div>
          <div class="stp-03__total-row"><span>Shipping</span><span>Free</span></div>
          <div class="stp-03__total-row"><span>Tax (8%)</span><span>$20.48</span></div>
          <div class="stp-03__total-row grand"><span>Total</span><span>$276.48</span></div>
        </div>
      </div>
    </div>

    <!-- Nav -->
    <div class="stp-03__nav" style="background:var(--card);border:1px solid var(--border);border-top:none;border-radius:0 0 16px 16px">
      <button class="stp-03__btn stp-03__btn--ghost">← Back</button>
      <span class="stp-03__lock">🔒 256-bit SSL encrypted</span>
      <button class="stp-03__btn stp-03__btn--primary">Place Order →</button>
    </div>
  </div>
</div>
```
## CSS
```css
.stp-03,
.stp-03 *,
.stp-03 *::before,
.stp-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.stp-03 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.stp-03 {
  --bg: #0a0f1e;
  --card: #0f1629;
  --border: #1e2d4a;
  --blue: #0ea5e9;
  --cyan: #06b6d4;
  --white: #e8f4fd;
  --muted: #4a6080;
  --success: #22c55e;
  --warning: #f59e0b;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background-image: radial-gradient(ellipse at 20% 50%,rgba(14,165,233,.06) 0%,transparent 50%), radial-gradient(ellipse at 80% 50%,rgba(6,182,212,.04) 0%,transparent 50%);
}

.stp-03__shell {
  max-width: 820px;
  width: 100%;
}
/* top stepper bar */

.stp-03__bar {
  display: flex;
  align-items: stretch;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px 16px 0 0;
  overflow: hidden;
  border-bottom: none;
}

.stp-03__tab {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 18px 20px;
  position: relative;
  border-right: 1px solid var(--border);
  transition: background .3s;
}

.stp-03__tab:last-child {
  border-right: none;
}

.stp-03__tab.done {
  background: rgba(34,197,94,.05);
}

.stp-03__tab.active {
  background: rgba(14,165,233,.08);
}

.stp-03__tab-icon {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  background: var(--border);
  color: var(--muted);
  transition: all .3s;
  font-weight: 700;
}

.stp-03__tab.done .stp-03__tab-icon {
  background: rgba(34,197,94,.2);
  color: var(--success);
}

.stp-03__tab.active .stp-03__tab-icon {
  background: rgba(14,165,233,.2);
  color: var(--blue);
}

.stp-03__tab-info {
  min-width: 0;
}

.stp-03__tab-step {
  font-size: 10px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
}

.stp-03__tab-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--muted);
  transition: color .3s;
  white-space: nowrap;
}

.stp-03__tab.done .stp-03__tab-name {
  color: var(--success);
}

.stp-03__tab.active .stp-03__tab-name {
  color: var(--white);
}
/* active underline */

.stp-03__tab.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg,var(--blue),var(--cyan));
}
/* body */

.stp-03__body {
  background: var(--card);
  border: 1px solid var(--border);
  border-top: none;
  border-radius: 0 0 16px 16px;
  display: grid;
  grid-template-columns: 1fr 300px;
}

.stp-03__main {
  padding: 32px;
  border-right: 1px solid var(--border);
}

.stp-03__section-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.stp-03__section-title::before {
  content: '';
  width: 3px;
  height: 18px;
  background: linear-gradient(180deg,var(--blue),var(--cyan));
  border-radius: 2px;
  display: block;
}

.stp-03__field {
  margin-bottom: 14px;
}

.stp-03__field-label {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--muted);
  margin-bottom: 6px;
  display: block;
}

.stp-03__input {
  width: 100%;
  padding: 11px 14px;
  background: rgba(255,255,255,.03);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--white);
  font-size: 14px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.stp-03__input::placeholder {
  color: var(--muted);
}

.stp-03__input:focus {
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(14,165,233,.15);
}

.stp-03__grid2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.stp-03__grid3 {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 12px;
}
/* order summary sidebar */

.stp-03__aside {
  padding: 24px;
}

.stp-03__aside-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 16px;
}

.stp-03__item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border);
}

.stp-03__item:last-of-type {
  border-bottom: none;
}

.stp-03__item-thumb {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}

.stp-03__item-name {
  font-size: 12px;
  color: var(--white);
  font-weight: 600;
}

.stp-03__item-sku {
  font-size: 10px;
  color: var(--muted);
}

.stp-03__item-price {
  font-size: 13px;
  font-weight: 700;
  color: var(--blue);
  margin-left: auto;
}

.stp-03__totals {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
}

.stp-03__total-row {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: var(--muted);
  padding: 3px 0;
}

.stp-03__total-row.grand {
  font-size: 15px;
  font-weight: 700;
  color: var(--white);
  padding-top: 8px;
  border-top: 1px solid var(--border);
  margin-top: 6px;
}
/* nav */

.stp-03__nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 32px;
  border-top: 1px solid var(--border);
}

.stp-03__btn {
  padding: 11px 28px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all .2s;
}

.stp-03__btn--ghost {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
}

.stp-03__btn--ghost:hover {
  color: var(--white);
  border-color: var(--blue);
}

.stp-03__btn--primary {
  background: linear-gradient(135deg,var(--blue),var(--cyan));
  color: #fff;
  box-shadow: 0 4px 20px rgba(14,165,233,.35);
}

.stp-03__btn--primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(14,165,233,.45);
}

.stp-03__lock {
  font-size: 12px;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: 6px;
}

@media (max-width: 640px) {
  .stp-03__body {
    grid-template-columns: 1fr;
  }

  .stp-03__aside {
    display: none;
  }

  .stp-03__tab-info {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .stp-03__btn--primary,
    .stp-03__tab {
    transition: none;
  }
}
```
