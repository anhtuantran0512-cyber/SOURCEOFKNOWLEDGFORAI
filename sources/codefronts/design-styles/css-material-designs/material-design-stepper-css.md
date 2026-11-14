---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-material-designs/material-design-stepper-css/"
title: "Material Design Stepper CSS"
section: "design-styles"
category: "css-material-designs"
category_name: "Material Design CSS Components"
description: "Horizontal step indicator with done/active/error states, vertical accordion stepper, and a linear checkout stepper — built entirely with CSS counter and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Stepper CSS
Source: https://codefronts.com/design-styles/css-material-designs/material-design-stepper-css/

Horizontal step indicator with done/active/error states, vertical accordion stepper, and a linear checkout stepper — built entirely with CSS counter and radio-hack.
## HTML
```html
<div class="md-09">
  <div class="md-09__wrap">
    <div class="md-09__page-title">Material Design Steppers CSS</div>
    <div class="md-09__page-sub">Horizontal, vertical and linear checkout steppers — state indicators, connectors and panel content</div>

    <!-- Horizontal Stepper -->
    <div class="md-09__card">
      <div class="md-09__card-title">Horizontal Stepper — Order Progress</div>
      <div class="md-09__hstep">
        <div class="md-09__hstep-item md-09__hstep-item--done">
          <div class="md-09__step-circle">✓</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Cart</div><div class="md-09__step-sub">Completed</div></div>
        </div>
        <div class="md-09__hstep-item md-09__hstep-item--done">
          <div class="md-09__step-circle">✓</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Shipping</div><div class="md-09__step-sub">Completed</div></div>
        </div>
        <div class="md-09__hstep-item md-09__hstep-item--active">
          <div class="md-09__step-circle">3</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Payment</div><div class="md-09__step-sub">In progress</div></div>
        </div>
        <div class="md-09__hstep-item">
          <div class="md-09__step-circle">4</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Review</div><div class="md-09__step-sub">Pending</div></div>
        </div>
        <div class="md-09__hstep-item">
          <div class="md-09__step-circle">5</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Confirm</div><div class="md-09__step-sub">Pending</div></div>
        </div>
      </div>
      <div class="md-09__step-content">
        <div class="md-09__step-content-title">Step 3 — Payment Details</div>
        <div class="md-09__step-content-body">Enter your payment method. All transactions are secured with 256-bit SSL encryption. We accept Visa, Mastercard, American Express and PayPal.</div>
      </div>
      <div class="md-09__step-actions">
        <button class="md-09__btn md-09__btn--ghost">← Back</button>
        <button class="md-09__btn md-09__btn--p">Continue →</button>
      </div>
    </div>

    <!-- Horizontal with Error -->
    <div class="md-09__card">
      <div class="md-09__card-title">Horizontal Stepper — With Error State</div>
      <div class="md-09__hstep">
        <div class="md-09__hstep-item md-09__hstep-item--done">
          <div class="md-09__step-circle">✓</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Upload</div><div class="md-09__step-sub">Done</div></div>
        </div>
        <div class="md-09__hstep-item md-09__hstep-item--error">
          <div class="md-09__step-circle">!</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Validate</div><div class="md-09__step-sub">Error</div></div>
        </div>
        <div class="md-09__hstep-item">
          <div class="md-09__step-circle">3</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Process</div><div class="md-09__step-sub">Waiting</div></div>
        </div>
        <div class="md-09__hstep-item">
          <div class="md-09__step-circle">4</div>
          <div class="md-09__step-label"><div class="md-09__step-name">Publish</div><div class="md-09__step-sub">Waiting</div></div>
        </div>
      </div>
      <div class="md-09__step-content" style="border-color:#ffcdd2;background:#fff8f8">
        <div class="md-09__step-content-title" style="color:#c62828">⚠ Validation Failed</div>
        <div class="md-09__step-content-body">3 columns in your CSV are missing required values. Please fix the errors and re-upload your file.</div>
      </div>
      <div class="md-09__step-actions">
        <button class="md-09__btn md-09__btn--ghost">← Back</button>
        <button class="md-09__btn md-09__btn--p" style="background:#c62828">Fix Errors</button>
      </div>
    </div>

    <!-- Vertical Stepper -->
    <div class="md-09__card">
      <div class="md-09__card-title">Vertical Stepper (Accordion)</div>
      <div class="md-09__vstep">
        <div class="md-09__vstep-item">
          <input class="md-09__vstep-in" type="radio" name="md09v" id="md09v1" checked>
          <div class="md-09__vstep-left">
            <label class="md-09__vstep-circle" for="md09v1">1</label>
            <div class="md-09__vstep-connector"></div>
          </div>
          <div class="md-09__vstep-body">
            <div class="md-09__vstep-head">
              <label class="md-09__vstep-title" for="md09v1">Account Information</label>
            </div>
            <div class="md-09__vstep-panel">
              <div class="md-09__vstep-panel-inner">
                <p>Provide your name, email and password to create your account. We'll send a verification email once you submit.</p>
                <div style="margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:12px">
                  <div class="md-09__field"><label>First Name</label><input type="text" placeholder="Alex"></div>
                  <div class="md-09__field"><label>Last Name</label><input type="text" placeholder="Thompson"></div>
                  <div class="md-09__field" style="grid-column:1/-1"><label>Email</label><input type="email" placeholder="[email protected]"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="md-09__vstep-item">
          <input class="md-09__vstep-in" type="radio" name="md09v" id="md09v2">
          <div class="md-09__vstep-left">
            <label class="md-09__vstep-circle" for="md09v2">2</label>
            <div class="md-09__vstep-connector"></div>
          </div>
          <div class="md-09__vstep-body">
            <div class="md-09__vstep-head">
              <label class="md-09__vstep-title" for="md09v2">Choose Your Plan</label>
            </div>
            <div class="md-09__vstep-panel">
              <div class="md-09__vstep-panel-inner">
                <p>Select the plan that best fits your needs. You can upgrade or downgrade at any time.</p>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:12px">
                  <div style="border:2px solid var(--divider);border-radius:8px;padding:12px;text-align:center"><div style="font-weight:700">Free</div><div style="font-size:1.2rem;font-weight:700;margin:4px 0">$0</div><div style="font-size:.75rem;color:var(--ink2)">5 projects</div></div>
                  <div style="border:2px solid var(--primary);border-radius:8px;padding:12px;text-align:center;background:rgba(230,81,0,.06)"><div style="font-weight:700;color:var(--primary)">Pro ★</div><div style="font-size:1.2rem;font-weight:700;margin:4px 0;color:var(--primary)">$12</div><div style="font-size:.75rem;color:var(--ink2)">Unlimited</div></div>
                  <div style="border:2px solid var(--divider);border-radius:8px;padding:12px;text-align:center"><div style="font-weight:700">Team</div><div style="font-size:1.2rem;font-weight:700;margin:4px 0">$49</div><div style="font-size:.75rem;color:var(--ink2)">20 seats</div></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="md-09__vstep-item">
          <input class="md-09__vstep-in" type="radio" name="md09v" id="md09v3">
          <div class="md-09__vstep-left">
            <label class="md-09__vstep-circle" for="md09v3">3</label>
          </div>
          <div class="md-09__vstep-body">
            <div class="md-09__vstep-head">
              <label class="md-09__vstep-title" for="md09v3">Confirm &amp; Launch</label>
            </div>
            <div class="md-09__vstep-panel">
              <div class="md-09__vstep-panel-inner">
                <p>Review your selections and confirm. Your workspace will be ready in seconds.</p>
                <button class="md-09__btn md-09__btn--p" style="margin-top:12px">🚀 Create Account</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Checkout Stepper -->
    <div class="md-09__card" style="padding:0;overflow:hidden">
      <input class="md-09__checkout-in" type="radio" name="md09co" id="md09co1" checked>
      <input class="md-09__checkout-in" type="radio" name="md09co" id="md09co2">
      <input class="md-09__checkout-in" type="radio" name="md09co" id="md09co3">
      <div class="md-09__checkout-steps">
        <label class="md-09__checkout-step-lbl md-09__cslbl-1" for="md09co1">1 · Shipping</label>
        <label class="md-09__checkout-step-lbl md-09__cslbl-2" for="md09co2">2 · Payment</label>
        <label class="md-09__checkout-step-lbl md-09__cslbl-3" for="md09co3">3 · Review</label>
      </div>
      <div class="md-09__checkout-panels">
        <div class="md-09__checkout-panel md-09__cpanel-1">
          <div style="font-size:.95rem;font-weight:700;margin-bottom:16px">Shipping Address</div>
          <div class="md-09__field-row">
            <div class="md-09__field"><label>First Name</label><input type="text" placeholder="Alex"></div>
            <div class="md-09__field"><label>Last Name</label><input type="text" placeholder="Thompson"></div>
          </div>
          <div class="md-09__field"><label>Address Line 1</label><input type="text" placeholder="123 Main Street"></div>
          <div class="md-09__field-row">
            <div class="md-09__field"><label>City</label><input type="text" placeholder="San Francisco"></div>
            <div class="md-09__field"><label>ZIP</label><input type="text" placeholder="94102"></div>
          </div>
          <div style="text-align:right;margin-top:8px"><label class="md-09__btn md-09__btn--p" for="md09co2" style="cursor:pointer;display:inline-flex;align-items:center">Next: Payment →</label></div>
        </div>
        <div class="md-09__checkout-panel md-09__cpanel-2">
          <div style="font-size:.95rem;font-weight:700;margin-bottom:16px">Payment Details</div>
          <div class="md-09__field"><label>Card Number</label><input type="text" placeholder="4111 1111 1111 1111"></div>
          <div class="md-09__field-row">
            <div class="md-09__field"><label>Expiry</label><input type="text" placeholder="MM / YY"></div>
            <div class="md-09__field"><label>CVC</label><input type="text" placeholder="123"></div>
          </div>
          <div style="display:flex;justify-content:space-between;margin-top:8px">
            <label class="md-09__btn md-09__btn--ghost" for="md09co1" style="cursor:pointer;display:inline-flex;align-items:center">← Back</label>
            <label class="md-09__btn md-09__btn--p" for="md09co3" style="cursor:pointer;display:inline-flex;align-items:center">Next: Review →</label>
          </div>
        </div>
        <div class="md-09__checkout-panel md-09__cpanel-3">
          <div style="font-size:.95rem;font-weight:700;margin-bottom:16px">Order Review</div>
          <div style="background:#fff8f0;border-radius:8px;padding:16px;margin-bottom:16px;border:1px solid var(--divider)">
            <div style="display:flex;justify-content:space-between;font-size:.88rem;color:var(--ink2);margin-bottom:8px"><span>Aurora Pro (12 months)</span><span>$144.00</span></div>
            <div style="display:flex;justify-content:space-between;font-size:.88rem;color:var(--ink2);margin-bottom:8px"><span>Shipping</span><span>Free</span></div>
            <div style="height:1px;background:var(--divider);margin:8px 0"></div>
            <div style="display:flex;justify-content:space-between;font-weight:700;color:var(--primary)"><span>Total</span><span>$144.00</span></div>
          </div>
          <div style="display:flex;justify-content:space-between;margin-top:8px">
            <label class="md-09__btn md-09__btn--ghost" for="md09co2" style="cursor:pointer;display:inline-flex;align-items:center">← Back</label>
            <button class="md-09__btn md-09__btn--p">✓ Place Order</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.md-09,
.md-09 *,
.md-09 *::before,
.md-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.md-09 ::selection {
  background: #e65100;
  color: #fff;
}

.md-09 {
  --primary: #e65100;
  --primary-l: #ff8a65;
  --success: #2e7d32;
  --surface: #fff;
  --bg: #fff3e0;
  --ink: #212121;
  --ink2: #546e7a;
  --ink3: #90a4ae;
  --divider: #ffcc80;
  font-family: 'Roboto',sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 48px 24px 80px;
  color: var(--ink);
}

.md-09__wrap {
  max-width: 860px;
  margin: 0 auto;
}

.md-09__page-title {
  font-size: clamp(1.4rem,4vw,2rem);
  font-weight: 700;
  margin-bottom: 4px;
}

.md-09__page-sub {
  font-size: .9rem;
  color: var(--ink2);
  margin-bottom: 40px;
}

.md-09__card {
  background: var(--surface);
  border-radius: 12px;
  padding: 32px;
  margin-bottom: 28px;
  box-shadow: 0 1px 4px rgba(0,0,0,.1);
}

.md-09__card-title {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink2);
  margin-bottom: 28px;
}
/* ── HORIZONTAL STEPPER ── */

.md-09__hstep {
  display: flex;
  align-items: flex-start;
  position: relative;
  margin-bottom: 32px;
}
/* connector lines between steps */

.md-09__hstep-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  position: relative;
}

.md-09__hstep-item:not(:last-child)::after {
  content: '';
  position: absolute;
  top: 20px;
  left: 50%;
  right: -50%;
  height: 2px;
  background: var(--divider);
  z-index: 0;
}

.md-09__hstep-item--done:not(:last-child)::after {
  background: var(--success);
}

.md-09__hstep-item--active:not(:last-child)::after {
  background: linear-gradient(to right,var(--primary),var(--divider));
}
/* step circle */

.md-09__step-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .9rem;
  font-weight: 700;
  border: 2px solid var(--divider);
  background: var(--surface);
  color: var(--ink3);
  position: relative;
  z-index: 1;
  transition: all .25s;
  flex-shrink: 0;
}

.md-09__hstep-item--done .md-09__step-circle {
  background: var(--success);
  border-color: var(--success);
  color: #fff;
}

.md-09__hstep-item--active .md-09__step-circle {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
  box-shadow: 0 0 0 4px rgba(230,81,0,.2);
}

.md-09__hstep-item--error .md-09__step-circle {
  background: #c62828;
  border-color: #c62828;
  color: #fff;
}

.md-09__step-label {
  margin-top: 10px;
  text-align: center;
  padding: 0 4px;
}

.md-09__step-name {
  font-size: .8rem;
  font-weight: 500;
  color: var(--ink);
  line-height: 1.3;
}

.md-09__hstep-item--done .md-09__step-name {
  color: var(--success);
}

.md-09__hstep-item--active .md-09__step-name {
  color: var(--primary);
  font-weight: 700;
}

.md-09__hstep-item--error .md-09__step-name {
  color: #c62828;
}

.md-09__step-sub {
  font-size: .72rem;
  color: var(--ink3);
  margin-top: 2px;
}
/* ── CONTENT PANEL ── */

.md-09__step-content {
  border: 1px solid var(--divider);
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 20px;
  background: #fffef9;
}

.md-09__step-content-title {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--ink);
}

.md-09__step-content-body {
  font-size: .9rem;
  line-height: 1.7;
  color: var(--ink2);
}

.md-09__step-actions {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.md-09__btn {
  height: 36px;
  padding: 0 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: 'Roboto';
  font-size: .875rem;
  font-weight: 500;
  letter-spacing: .089em;
  text-transform: uppercase;
  transition: box-shadow .15s;
}

.md-09__btn--p {
  background: var(--primary);
  color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,.2);
}

.md-09__btn--p:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,.25);
}

.md-09__btn--ghost {
  background: transparent;
  color: var(--primary);
  border: 1px solid rgba(230,81,0,.4);
}
/* ── VERTICAL STEPPER (checkbox-hack) ── */

.md-09__vstep {
  display: flex;
  flex-direction: column;
}

.md-09__vstep-in {
  display: none;
}

.md-09__vstep-item {
  display: flex;
  gap: 0;
  position: relative;
}

.md-09__vstep-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 48px;
  flex-shrink: 0;
}

.md-09__vstep-circle {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .8rem;
  font-weight: 700;
  background: var(--surface);
  border: 2px solid var(--divider);
  color: var(--ink3);
  flex-shrink: 0;
  cursor: pointer;
  z-index: 1;
  transition: all .2s;
}

.md-09__vstep-in:checked ~ .md-09__vstep-body .md-09__vstep-circle {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
  box-shadow: 0 0 0 3px rgba(230,81,0,.2);
}

.md-09__vstep-connector {
  width: 2px;
  flex: 1;
  background: var(--divider);
  margin: 4px 0;
  min-height: 24px;
}

.md-09__vstep-body {
  flex: 1;
  padding-bottom: 24px;
}

.md-09__vstep-head {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 32px;
}

.md-09__vstep-title {
  font-size: .95rem;
  font-weight: 500;
  cursor: pointer;
  user-select: none;
  color: var(--ink2);
}

.md-09__vstep-in:checked ~ .md-09__vstep-body .md-09__vstep-title {
  color: var(--primary);
  font-weight: 700;
}

.md-09__vstep-panel {
  overflow: hidden;
  max-height: 0;
  transition: max-height .3s ease;
}

.md-09__vstep-in:checked ~ .md-09__vstep-body .md-09__vstep-panel {
  max-height: 400px;
}

.md-09__vstep-panel-inner {
  padding: 12px 0;
  font-size: .88rem;
  color: var(--ink2);
  line-height: 1.7;
}
/* ── LINEAR CHECKOUT STEPS (radio) ── */

.md-09__checkout {
  position: relative;
  overflow: hidden;
}

.md-09__checkout-in {
  display: none;
}

.md-09__checkout-steps {
  display: flex;
  background: var(--primary);
  padding: 0 16px;
}

.md-09__checkout-step-lbl {
  flex: 1;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: .8rem;
  font-weight: 500;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: rgba(255,255,255,.6);
  cursor: pointer;
  position: relative;
  transition: color .2s;
  user-select: none;
}

.md-09__checkout-step-lbl::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #fff;
  transform: scaleX(0);
  transition: transform .25s;
}

#md09co1:checked ~ .md-09__checkout-steps .md-09__cslbl-1,
#md09co2:checked ~ .md-09__checkout-steps .md-09__cslbl-2,
#md09co3:checked ~ .md-09__checkout-steps .md-09__cslbl-3 {
  color: #fff;
}

#md09co1:checked ~ .md-09__checkout-steps .md-09__cslbl-1::after,
#md09co2:checked ~ .md-09__checkout-steps .md-09__cslbl-2::after,
#md09co3:checked ~ .md-09__checkout-steps .md-09__cslbl-3::after {
  transform: scaleX(1);
}

.md-09__checkout-panels {
  padding: 24px;
}

.md-09__checkout-panel {
  display: none;
}

#md09co1:checked ~ .md-09__checkout-panels .md-09__cpanel-1,
#md09co2:checked ~ .md-09__checkout-panels .md-09__cpanel-2,
#md09co3:checked ~ .md-09__checkout-panels .md-09__cpanel-3 {
  display: block;
}

.md-09__field {
  margin-bottom: 16px;
}

.md-09__field label {
  font-size: .78rem;
  color: var(--ink2);
  display: block;
  margin-bottom: 4px;
}

.md-09__field input,
.md-09__field select {
  width: 100%;
  height: 44px;
  padding: 0 12px;
  border: 1px solid var(--divider);
  border-radius: 4px;
  font-family: 'Roboto';
  font-size: .875rem;
  outline: none;
  transition: border-color .15s;
}

.md-09__field input:focus,
.md-09__field select:focus {
  border-color: var(--primary);
}

.md-09__field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .md-09 * {
    transition: none!important;
    animation: none!important;
  }
}
```
