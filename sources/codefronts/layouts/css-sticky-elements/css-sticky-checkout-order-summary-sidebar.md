---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-checkout-order-summary-sidebar/"
title: "CSS Sticky Checkout Order Summary Sidebar"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The checkout layout that measurably reduces abandonment: form fields on the left, order summary pinned on the right, so the total never leaves the buyer's…"
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Checkout Order Summary Sidebar
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-checkout-order-summary-sidebar/

The checkout layout that measurably reduces abandonment: form fields on the left, order summary pinned on the right, so the total never leaves the buyer's sight while they type a shipping address. One grid, one sticky aside with align-self: start, and real form semantics — labels, autocomplete tokens, focus rings — because a checkout demo without them teaches the wrong lesson. On narrow screens the summary un-sticks and stacks on top, the honest mobile translation.
## HTML
```html
<section class="cst-13" aria-label="Sticky checkout order summary demo">
  <div class="cst-13__stage" id="cst13-top">
    <header class="cst-13__mast">
      <a class="cst-13__brand" href="#cst13-top">Foundry Supply Co.</a>
      <p class="cst-13__steps"><span>Cart</span><i aria-hidden="true">→</i><strong aria-current="step">Checkout</strong><i aria-hidden="true">→</i><span>Done</span></p>
      <span class="cst-13__secure"><svg viewBox="0 0 20 20" width="13" height="13" aria-hidden="true"><rect x="4" y="9" width="12" height="8" rx="2" fill="currentColor"/><path d="M7 9V6.5a3 3 0 0 1 6 0V9" fill="none" stroke="currentColor" stroke-width="2"/></svg>256-bit TLS</span>
    </header>
    <form class="cst-13__checkout" onsubmit="return false">
      <div class="cst-13__form">
        <section>
          <h2><span>1</span>Contact</h2>
          <div class="cst-13__field"><label for="cst13-email">Email</label><input id="cst13-email" type="email" autocomplete="email" placeholder="[email protected]"></div>
        </section>
        <section>
          <h2><span>2</span>Shipping</h2>
          <div class="cst-13__row">
            <div class="cst-13__field"><label for="cst13-fn">First name</label><input id="cst13-fn" autocomplete="given-name"></div>
            <div class="cst-13__field"><label for="cst13-ln">Last name</label><input id="cst13-ln" autocomplete="family-name"></div>
          </div>
          <div class="cst-13__field"><label for="cst13-addr">Address</label><input id="cst13-addr" autocomplete="street-address" placeholder="Street and number"></div>
          <div class="cst-13__row">
            <div class="cst-13__field"><label for="cst13-city">City</label><input id="cst13-city" autocomplete="address-level2"></div>
            <div class="cst-13__field"><label for="cst13-zip">Postcode</label><input id="cst13-zip" autocomplete="postal-code" inputmode="numeric"></div>
          </div>
          <div class="cst-13__field"><label for="cst13-country">Country</label><select id="cst13-country" autocomplete="country-name"><option>United States</option><option>Canada</option><option>United Kingdom</option><option>Australia</option><option>New Zealand</option></select></div>
        </section>
        <section>
          <h2><span>3</span>Payment</h2>
          <div class="cst-13__field"><label for="cst13-card">Card number</label><input id="cst13-card" autocomplete="cc-number" inputmode="numeric" placeholder="4242 4242 4242 4242"></div>
          <div class="cst-13__row">
            <div class="cst-13__field"><label for="cst13-exp">Expiry</label><input id="cst13-exp" autocomplete="cc-exp" inputmode="numeric" placeholder="MM / YY"></div>
            <div class="cst-13__field"><label for="cst13-cvc">Security code</label><input id="cst13-cvc" autocomplete="cc-csc" inputmode="numeric" placeholder="CVC"></div>
          </div>
          <button class="cst-13__pay" type="submit">Pay $347.88</button>
          <p class="cst-13__fine">Charged in USD. The summary on the right is <code>position: sticky; top: 24px; align-self: start</code> — the total never scrolls out of sight.</p>
        </section>
      </div>
      <aside class="cst-13__summary" aria-label="Order summary">
        <h2>Order summary</h2>
        <ul>
          <li><i style="--img:url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=400&auto=format&fit=crop')"></i><div><strong>Atlas field watch</strong><span>38mm · sand strap</span></div><em>$189.00</em></li>
          <li><i style="--img:url('https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=400&auto=format&fit=crop')"></i><div><strong>Canvas weekender</strong><span>Waxed olive</span></div><em>$98.00</em></li>
          <li><i style="--img:url('https://images.unsplash.com/photo-1523362628745-0c100150b504?q=80&w=400&auto=format&fit=crop')"></i><div><strong>Trail bottle, 750ml</strong><span>Steel</span></div><em>$24.00</em></li>
        </ul>
        <div class="cst-13__promo"><label class="cst-13__vh" for="cst13-promo">Promo code</label><input id="cst13-promo" placeholder="Promo code"><button type="button">Apply</button></div>
        <dl class="cst-13__totals">
          <div><dt>Subtotal</dt><dd>$311.00</dd></div>
          <div><dt>Shipping</dt><dd>$12.00</dd></div>
          <div><dt>Tax (8%)</dt><dd>$24.88</dd></div>
          <div class="cst-13__grand"><dt>Total</dt><dd>$347.88</dd></div>
        </dl>
        <p class="cst-13__promise">Free returns · 60 days · carbon-neutral shipping</p>
      </aside>
    </form>
    <footer class="cst-13__footer"><p><strong>Foundry Supply Co.</strong> — a demo from the CodeFronts sticky-elements collection.</p><a href="#cst13-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-13,
.cst-13 *,
.cst-13 *::before,
.cst-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-13 {
  --bg: oklch(0.972 0.004 270);
  --pane: oklch(1 0 0);
  --ink: oklch(0.23 0.015 270);
  --mut: oklch(0.51 0.012 270);
  --line: oklch(0.9 0.007 270);
  --acc: oklch(0.5 0.16 270);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-13__stage {
  width: 100%;
  container: cst13/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-13__mast {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 10px 22px;
  padding: 18px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
  background: var(--pane);
}

.cst-13__brand {
  font-size: 15.5px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: inherit;
  text-decoration: none;
}

.cst-13__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-13__steps {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-inline: auto;
  font-size: 12.5px;
  color: var(--mut);
}

.cst-13__steps strong {
  color: var(--ink);
  font-weight: 750;
}

.cst-13__steps i {
  font-style: normal;
  opacity: .5;
}

.cst-13__secure {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11.5px;
  font-weight: 700;
  color: oklch(0.45 0.1 155);
}

.cst-13__checkout {
  display: grid;
  grid-template-columns: minmax(0,1fr) 360px;
  gap: clamp(24px,4cqi,56px);
  align-items: start;
  padding: clamp(22px,4cqi,44px) clamp(16px,4cqi,44px);
}

.cst-13__form {
  display: grid;
  gap: 30px;
  max-width: 60ch;
}

.cst-13__form h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 16.5px;
  letter-spacing: -.015em;
  font-weight: 800;
  margin-bottom: 14px;
}

.cst-13__form h2 span {
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  font-size: 12px;
  color: oklch(0.99 0 0);
  background: var(--ink);
}

.cst-13__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.cst-13__field {
  display: grid;
  gap: 6px;
  margin-bottom: 12px;
}

.cst-13__field label {
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
}

.cst-13__field input,
.cst-13__field select {
  width: 100%;
  min-height: 46px;
  padding: 0 14px;
  border-radius: 11px;
  border: 1.5px solid var(--line);
  background: var(--pane);
  font: inherit;
  font-size: 14px;
  color: var(--ink);
  transition: border-color .15s,box-shadow .15s;
}

.cst-13__field input::placeholder {
  color: oklch(0.68 0.008 270);
}

.cst-13__field input:hover,
.cst-13__field select:hover {
  border-color: oklch(0.78 0.015 270);
}

.cst-13__field input:focus-visible,
.cst-13__field select:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 3px oklch(0.5 0.16 270/.16);
}

.cst-13__pay {
  width: 100%;
  min-height: 52px;
  margin-top: 6px;
  border: none;
  border-radius: 13px;
  font: inherit;
  font-size: 15px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: var(--acc);
  cursor: pointer;
  transition: background .2s,translate .2s,box-shadow .2s;
}

.cst-13__pay:hover,
.cst-13__pay:focus-visible {
  background: color-mix(in oklch,var(--acc) 86%,black);
  translate: 0 -1px;
  box-shadow: 0 10px 24px oklch(0.5 0.16 270/.3);
}

.cst-13__pay:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-13__fine {
  margin-top: 12px;
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
}

.cst-13__fine code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.92 0.008 270);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.cst-13__summary {
  position: sticky;
  top: 24px;
  align-self: start;
  max-height: calc(100vh - 48px);
  max-height: calc(100svh - 48px);
  overflow: auto;
  padding: 22px;
  border-radius: 18px;
  background: var(--pane);
  border: 1px solid var(--line);
  box-shadow: 0 1px 3px oklch(0.3 0.02 270/.05);
  scrollbar-width: thin;
}

.cst-13__summary h2 {
  font-size: 15px;
  letter-spacing: -.01em;
  font-weight: 800;
  margin-bottom: 16px;
}

.cst-13__summary ul {
  list-style: none;
  display: grid;
  gap: 14px;
}

.cst-13__summary li {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cst-13__summary li i {
  flex: none;
  width: 52px;
  height: 52px;
  border-radius: 11px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.86 0.03 270),oklch(0.68 0.06 270));
  background-size: cover;
  background-position: center;
  border: 1px solid var(--line);
}

.cst-13__summary li strong {
  display: block;
  font-size: 13.5px;
  letter-spacing: -.005em;
}

.cst-13__summary li span {
  font-size: 11.5px;
  color: var(--mut);
}

.cst-13__summary li em {
  margin-left: auto;
  font-style: normal;
  font-size: 13.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cst-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

.cst-13__promo {
  display: flex;
  gap: 8px;
  margin: 18px 0;
}

.cst-13__promo input {
  flex: 1;
  min-width: 0;
  min-height: 42px;
  padding: 0 12px;
  border-radius: 10px;
  border: 1.5px solid var(--line);
  background: var(--pane);
  font: inherit;
  font-size: 13px;
  transition: border-color .15s,box-shadow .15s;
}

.cst-13__promo input:focus-visible {
  outline: none;
  border-color: var(--acc);
  box-shadow: 0 0 0 3px oklch(0.5 0.16 270/.16);
}

.cst-13__promo button {
  min-height: 42px;
  padding: 0 16px;
  border: none;
  border-radius: 10px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--ink);
  background: oklch(0.93 0.008 270);
  cursor: pointer;
  transition: background .2s;
}

.cst-13__promo button:hover,
.cst-13__promo button:focus-visible {
  background: oklch(0.89 0.012 270);
}

.cst-13__promo button:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-13__totals {
  display: grid;
  gap: 9px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}

.cst-13__totals div {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  color: var(--mut);
}

.cst-13__totals dd {
  font-variant-numeric: tabular-nums;
  font-weight: 600;
  color: var(--ink);
}

.cst-13__grand {
  padding-top: 10px;
  border-top: 1px solid var(--line);
}

.cst-13__grand dt {
  font-size: 14.5px !important;
  font-weight: 800;
  color: var(--ink) !important;
}

.cst-13__grand dd {
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cst-13__promise {
  margin-top: 14px;
  font-size: 11.5px;
  color: var(--mut);
  text-align: center;
}

.cst-13__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 24px clamp(16px,4cqi,44px) 36px;
  border-top: 1px solid var(--line);
}

.cst-13__footer p {
  font-size: 12.5px;
  color: var(--mut);
}

.cst-13__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-13__footer a:hover,
.cst-13__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-13__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst13 (width < 760px) {
  .cst-13__checkout {
    grid-template-columns: 1fr;
  }

  .cst-13__summary {
    position: static;
    max-height: none;
    order: -1;
  }

  .cst-13__steps {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-13 * {
    transition-duration: .01ms !important;
  }
}
```
