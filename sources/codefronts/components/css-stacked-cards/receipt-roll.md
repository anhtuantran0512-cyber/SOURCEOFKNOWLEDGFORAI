---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/receipt-roll/"
title: "Receipt Roll"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A stack of line items bound tightly at the top that, on toggle, unrolls downward like a continuous paper receipt — perforated edges, monospace totals and all…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Receipt Roll
Source: https://codefronts.com/components/css-stacked-cards/receipt-roll/

A stack of line items bound tightly at the top that, on toggle, unrolls downward like a continuous paper receipt — perforated edges, monospace totals and all — then rolls neatly back up. A delightful metaphor for order summaries.
## HTML
```html
<section class="scd-26" aria-label="Unrolling receipt">
  <div class="scd-26__receipt">
    <input type="checkbox" id="scd-26-t" class="scd-26__t" checked>
    <label class="scd-26__stub" for="scd-26-t"><b>CODEFRONTS · Order #2261</b><span class="scd-26__toggle">Tap to roll</span></label>
    <div class="scd-26__wrap"><div class="scd-26__body">
      <div class="scd-26__row"><span>Stacked Cards Pack</span><span>$29.00</span></div>
      <div class="scd-26__row"><span>Carousel Add-on</span><span>$14.00</span></div>
      <div class="scd-26__row"><span>Lifetime updates</span><span>$12.00</span></div>
      <div class="scd-26__row scd-26__row--sub"><span>Subtotal</span><span>$55.00</span></div>
      <div class="scd-26__row"><span>Tax</span><span>$4.40</span></div>
      <div class="scd-26__row scd-26__row--tot"><span>Total</span><span>$59.40</span></div>
      <p class="scd-26__thanks">★ Thank you for your order ★</p>
    </div></div>
    <span class="scd-26__perf"></span>
  </div>
</section>
```
## CSS
```css
.scd-26,
.scd-26 *,
.scd-26 *::before,
.scd-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-26 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding: 10vh 20px;
  background: #2b2a28;
}

.scd-26__receipt {
  position: relative;
  width: min(300px,100%);
  background: #fbfaf5;
  border-radius: 4px 4px 0 0;
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.6);
  padding-bottom: 14px;
}

.scd-26__t {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
}

.scd-26__stub {
  display: flex;
  flex-direction: column;
  gap: 4px;
  align-items: center;
  padding: 20px 16px 14px;
  cursor: pointer;
  border-bottom: 2px dashed #d8d4c8;
}

.scd-26__stub b {
  font-size: 13px;
  letter-spacing: .06em;
  color: #2a2620;
  font-weight: 800;
}

.scd-26__toggle {
  font-size: 11px;
  color: #a09a88;
  text-transform: uppercase;
  letter-spacing: .12em;
}

.scd-26__wrap {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .55s cubic-bezier(.4,.9,.3,1);
}

.scd-26__body {
  overflow: hidden;
  font-family: 'Courier New',ui-monospace,monospace;
}

.scd-26__t:checked ~ .scd-26__wrap {
  grid-template-rows: 1fr;
}

.scd-26__t:checked ~ .scd-26__stub .scd-26__toggle::after {
  content: " ▲";
}

.scd-26__t:not(:checked) ~ .scd-26__stub .scd-26__toggle::after {
  content: " ▼";
}

.scd-26__row {
  display: flex;
  justify-content: space-between;
  padding: 9px 20px;
  font-size: 13px;
  color: #3a352c;
}

.scd-26__row--sub {
  border-top: 1px dashed #d8d4c8;
  margin-top: 6px;
}

.scd-26__row--tot {
  border-top: 2px solid #2a2620;
  font-weight: 800;
  font-size: 15px;
  color: #1a1712;
}

.scd-26__thanks {
  text-align: center;
  padding: 14px 0 6px;
  font-size: 12px;
  color: #8a8474;
  letter-spacing: .1em;
}

.scd-26__perf {
  display: block;
  height: 12px;
  background: #fbfaf5;
  -webkit-mask: radial-gradient(9px at 50% 0,transparent 98%,#000) repeat-x 0 0/18px 12px;
  mask: radial-gradient(9px at 50% 0,transparent 98%,#000) repeat-x 0 0/18px 12px;
}

.scd-26__t:focus-visible ~ .scd-26__stub {
  outline: 3px solid oklch(0.6 0.17 250);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-26__wrap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a checkbox animates grid-template-rows 0fr→1fr to unroll the receipt body, with a CSS mask cutting the perforated paper edge. */
```
