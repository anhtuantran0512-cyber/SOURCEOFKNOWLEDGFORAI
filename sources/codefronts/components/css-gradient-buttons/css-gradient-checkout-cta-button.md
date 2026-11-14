---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-checkout-cta-button/"
title: "CSS Gradient Checkout CTA Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A high-trust order-summary Pay button on a blue-to-green security gradient, with a JS idle → processing → confirmed flow that crossfades three stacked label…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Checkout CTA Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-checkout-cta-button/

A high-trust order-summary Pay button on a blue-to-green security gradient, with a JS idle → processing → confirmed flow that crossfades three stacked label layers.
## HTML
```html
<div class="gb-16">
  <div class="gb-16__summary">
    <h3 class="gb-16__h">Order summary</h3>
    <div class="gb-16__row"><span>Linen overshirt · M</span><b>$88.00</b></div>
    <div class="gb-16__row"><span>Shipping</span><b>Free</b></div>
    <div class="gb-16__row"><span>Tax</span><b>$7.04</b></div>
    <div class="gb-16__row gb-16__row--total"><span>Total</span><b>$95.04</b></div>
    <button class="gb-16__btn" id="gb-16-pay" type="button">
      <span class="gb-16__layer gb-16__layer--idle">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="10" width="16" height="10" rx="2"></rect><path d="M8 10V7a4 4 0 0 1 8 0v3"></path></svg>
        Pay $95.04 securely
      </span>
      <span class="gb-16__layer gb-16__layer--busy" aria-hidden="true">
        <span class="gb-16__spinner"></span>
        Processing…
      </span>
      <span class="gb-16__layer gb-16__layer--done" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 13 4.5 4.5L19 8"></path></svg>
        Payment confirmed
      </span>
    </button>
    <p class="gb-16__trust">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 5 6v5c0 4.4 3 8.4 7 9.6 4-1.2 7-5.2 7-9.6V6l-7-3Z"></path></svg>
      256-bit encrypted · 30-day returns
    </p>
  </div>
</div>
```
## CSS
```css
.gb-16,
.gb-16 *,
.gb-16 *::before,
.gb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-16 ::selection {
  background: #059669;
  color: #fff;
}

.gb-16 {
  --trust-a: #0284c7;
  --trust-b: #0d9488;
  --trust-c: #059669;
  --paid: #10b981;
  --ink: #1e293b;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: #f1f5f9;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-16__summary {
  width: 100%;
  max-width: 380px;
  background: #fff;
  border-radius: 20px;
  padding: 30px 28px;
  box-shadow: 0 20px 50px -28px rgba(30,41,59,.3);
}

.gb-16__h {
  font-size: 17px;
  font-weight: 800;
  color: var(--ink);
  margin-bottom: 20px;
}

.gb-16__row {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #64748b;
  padding: 9px 0;
}

.gb-16__row b {
  color: var(--ink);
  font-weight: 600;
}

.gb-16__row--total {
  border-top: 1.5px dashed #e2e8f0;
  margin-top: 8px;
  padding-top: 16px;
  font-size: 16px;
}

.gb-16__row--total b {
  font-size: 20px;
  font-weight: 800;
}
/* High-trust CTA: deep blue → teal → green reads as "secure + go".
   The JS flow crossfades three stacked label layers; without JS the
   button is a normal styled button. */

.gb-16__btn {
  position: relative;
  width: 100%;
  margin-top: 22px;
  padding: 18px 28px;
  border: none;
  border-radius: 14px;
  font-family: inherit;
  font-size: 16px;
  font-weight: 800;
  color: #fff;
  cursor: pointer;
  overflow: hidden;
  background-image: linear-gradient(110deg,var(--trust-a) 0%,var(--trust-b) 55%,var(--trust-c) 100%);
  background-size: 170% auto;
  background-position: left center;
  box-shadow: 0 12px 28px -10px rgba(13,148,136,.55);
  transition: background-position .5s ease,transform .25s ease,box-shadow .35s ease,filter .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-16__btn:hover {
  background-position: right center;
  transform: translateY(-2px);
  box-shadow: 0 16px 36px -10px rgba(5,150,105,.6);
}

.gb-16__btn:active {
  transform: translateY(0) scale(.99);
}

.gb-16__btn:focus-visible {
  outline: 3px solid var(--trust-b);
  outline-offset: 3px;
}

.gb-16__layer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  transition: opacity .3s ease,transform .3s ease;
}

.gb-16__layer svg {
  width: 17px;
  height: 17px;
  flex: none;
}

.gb-16__layer--busy,
.gb-16__layer--done {
  position: absolute;
  inset: 0;
  opacity: 0;
  transform: translateY(8px);
  pointer-events: none;
}

.gb-16__spinner {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 2.5px solid rgba(255,255,255,.35);
  border-top-color: #fff;
  animation: gb-16-spin .7s linear infinite;
}

@keyframes gb-16-spin {
  to {
    transform: rotate(360deg);
  }
}

.gb-16__btn.is-busy {
  pointer-events: none;
  filter: saturate(.85);
}

.gb-16__btn.is-busy .gb-16__layer--idle {
  opacity: 0;
  transform: translateY(-8px);
}

.gb-16__btn.is-busy .gb-16__layer--busy {
  opacity: 1;
  transform: translateY(0);
}

.gb-16__btn.is-done {
  background-image: linear-gradient(110deg,var(--paid),#059669);
  pointer-events: none;
}

.gb-16__btn.is-done .gb-16__layer--idle,
.gb-16__btn.is-done .gb-16__layer--busy {
  opacity: 0;
}

.gb-16__btn.is-done .gb-16__layer--done {
  opacity: 1;
  transform: translateY(0);
}

.gb-16__trust {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  margin-top: 14px;
  font-size: 12px;
  color: #94a3b8;
}

.gb-16__trust svg {
  width: 13px;
  height: 13px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-16__btn,
    .gb-16__layer {
    transition: none;
  }

  .gb-16__spinner {
    animation: none;
  }

  .gb-16__btn:hover {
    transform: none;
    background-position: left center;
  }
}
```

## JavaScript
```js
(function () {
  var btn = document.getElementById('gb-16-pay');
  if (!btn) return;
  btn.addEventListener('click', function () {
    if (btn.classList.contains('is-busy') || btn.classList.contains('is-done')) return;
    btn.classList.add('is-busy');
    setTimeout(function () {
      btn.classList.remove('is-busy');
      btn.classList.add('is-done');
    }, 1800);
    setTimeout(function () {
      btn.classList.remove('is-done');
    }, 5000);
  });
})();
```
