---
source: "codefronts"
url: "https://codefronts.com/components/css-forms/checkout-payment-form-with-order-summary/"
title: "Checkout Payment Form with Order Summary"
section: "components"
category: "css-forms"
category_name: "CSS Forms"
description: "A two-column checkout that collapses with a container query, not a viewport query: a live 3D card preview that mirrors what you type and flips to show the…"
has_js: "true"
---

Here's a working CSS Form from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Checkout Payment Form with Order Summary
Source: https://codefronts.com/components/css-forms/checkout-payment-form-with-order-summary/

A two-column checkout that collapses with a container query, not a viewport query: a live 3D card preview that mirrors what you type and flips to show the CVC when that field is focused (pure :has(), no JS for the flip), automatic card-number spacing with Visa/Mastercard/Amex detection, a payment-method switcher built from radios, quantity steppers, a working promo code, and a Pay button that always shows the real total.
## HTML
```html
<div class="frm-03" data-brand="none">
  <button type="button" class="frm-03__theme" data-theme-toggle aria-label="Dark mode" aria-pressed="false" title="Switch to dark mode"><svg class="frm-03__moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg><svg class="frm-03__sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <div class="frm-03__stage">
    <div class="frm-03__wrap">
      <div class="frm-03__grid">
        <section class="frm-03__pay" role="form" aria-labelledby="frm-03-title">
          <div class="frm-03__steps" aria-label="Checkout progress"><span>Cart</span><span>Shipping</span><span aria-current="step">Payment</span></div>
          <h2 id="frm-03-title">Payment</h2>
          <fieldset class="frm-03__methods">
            <legend class="frm-03__sr">Payment method</legend>
            <label><input type="radio" name="frm-03-m" value="card" checked><span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="2.5"/><path d="M2.5 10h19M6 15h4"/></svg>Card</span></label>
            <label><input type="radio" name="frm-03-m" value="wallet"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7.5A2.5 2.5 0 0 1 6.5 5H18v3"/><rect x="3" y="8" width="18" height="11" rx="2.5"/><circle cx="16.5" cy="13.5" r="1.3"/></svg>Wallet</span></label>
            <label><input type="radio" name="frm-03-m" value="bank"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m3 9 9-5 9 5M5 10v7M9.5 10v7M14.5 10v7M19 10v7M3 20h18"/></svg>Bank</span></label>
          </fieldset>
          <div class="frm-03__panel frm-03__panel--card">
            <div class="frm-03__card3d" aria-hidden="true">
              <div class="frm-03__face frm-03__face--front">
                <div class="frm-03__chiprow"><span class="frm-03__chip"></span><span class="frm-03__brand"></span></div>
                <div class="frm-03__pnum">•••• •••• •••• ••••</div>
                <div class="frm-03__prow"><span><small>Card holder</small><b class="frm-03__pname">Your name</b></span><span><small>Expires</small><b class="frm-03__pexp">MM/YY</b></span></div>
              </div>
              <div class="frm-03__face frm-03__face--back"><i></i><span class="frm-03__pcvc">•••</span></div>
            </div>
            <div class="frm-03__field">
              <label for="frm-03-num">Card number</label>
              <div class="frm-03__numwrap">
                <input id="frm-03-num" type="text" inputmode="numeric" autocomplete="cc-number" placeholder="1234 1234 1234 1234" maxlength="19" required aria-describedby="frm-03-brand-live">
                <span class="frm-03__badge" aria-hidden="true"></span>
              </div>
              <span class="frm-03__sr" id="frm-03-brand-live" aria-live="polite"></span>
            </div>
            <div class="frm-03__row">
              <div class="frm-03__field"><label for="frm-03-exp">Expiry</label><input id="frm-03-exp" type="text" inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" maxlength="7" required></div>
              <div class="frm-03__field"><label for="frm-03-cvc">CVC</label><input id="frm-03-cvc" type="text" inputmode="numeric" autocomplete="cc-csc" placeholder="123" maxlength="4" required></div>
            </div>
            <div class="frm-03__field"><label for="frm-03-name">Name on card</label><input id="frm-03-name" type="text" autocomplete="cc-name" placeholder="Taylor Morgan" required></div>
          </div>
          <div class="frm-03__panel frm-03__panel--wallet"><p>You'll confirm with your device wallet after pressing Pay. Supported: Apple&nbsp;Pay, Google&nbsp;Pay and Link.</p></div>
          <div class="frm-03__panel frm-03__panel--bank"><p>Pay directly from your bank via secure open-banking. You'll be redirected to approve the payment.</p></div>
          <label class="frm-03__save"><input type="checkbox" checked><span>Save this payment method for next time</span></label>
          <button class="frm-03__paybtn" type="button"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg><span>Pay <b class="frm-03__paytotal">$0.00</b></span></button>
          <p class="frm-03__secure" role="status">Encrypted end-to-end. You won't be charged until you confirm.</p>
        </section>
        <aside class="frm-03__summary" aria-labelledby="frm-03-sum">
          <h3 id="frm-03-sum">Order summary</h3>
          <ul class="frm-03__items">
            <li data-i="0">
              <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=240&h=240&fit=crop&auto=format&q=70" width="72" height="72" alt="Matte white over-ear wireless headphones" loading="lazy" decoding="async">
              <div><b>Studio Wireless</b><small>Chalk white</small><div class="frm-03__qty"><button type="button" data-d="-1" aria-label="Decrease Studio Wireless quantity">−</button><output aria-live="polite">1</output><button type="button" data-d="1" aria-label="Increase Studio Wireless quantity">+</button></div></div>
              <span class="frm-03__price"></span>
            </li>
            <li data-i="1">
              <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=240&h=240&fit=crop&auto=format&q=70" width="72" height="72" alt="Minimal analogue wristwatch with a white dial" loading="lazy" decoding="async">
              <div><b>Field Watch 38</b><small>Steel / white dial</small><div class="frm-03__qty"><button type="button" data-d="-1" aria-label="Decrease Field Watch quantity">−</button><output aria-live="polite">1</output><button type="button" data-d="1" aria-label="Increase Field Watch quantity">+</button></div></div>
              <span class="frm-03__price"></span>
            </li>
          </ul>
          <div class="frm-03__promo">
            <label for="frm-03-code" class="frm-03__sr">Promo code</label>
            <input id="frm-03-code" type="text" placeholder="Promo code (try SAVE10)" autocomplete="off" aria-describedby="frm-03-code-msg">
            <button type="button" class="frm-03__apply">Apply</button>
          </div>
          <p class="frm-03__codemsg" id="frm-03-code-msg" aria-live="polite"></p>
          <dl class="frm-03__totals">
            <div><dt>Subtotal</dt><dd data-k="sub"></dd></div>
            <div class="frm-03__disc"><dt>Discount</dt><dd data-k="disc"></dd></div>
            <div><dt>Shipping</dt><dd data-k="ship"></dd></div>
            <div><dt>Estimated tax</dt><dd data-k="tax"></dd></div>
            <div class="frm-03__grand"><dt>Total</dt><dd data-k="total"></dd></div>
          </dl>
        </aside>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap');

.frm-03 {
  --bg: #eef1f5;
  --surface: #ffffff;
  --sum: #f7f8fb;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --accent: #4f46e5;
  --on-accent: #fff;
  --ok: #059669;
  --bad: #dc2626;
  --card-a: #1e293b;
  --card-b: #475569;
  --sans: "Figtree",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,Menlo,monospace;
  --ease: cubic-bezier(.16,1,.3,1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: dark) {
  .frm-03:not([data-theme="light"]) {
    --bg: #0b0f17;
    --surface: #121826;
    --sum: #0f1520;
    --ink: #e7ecf5;
    --muted: #8a96ab;
    --line: #232c3d;
    --accent: #818cf8;
    --on-accent: #0b0d24;
    --ok: #34d399;
    --bad: #f87171;
  }
}

.frm-03[data-theme="dark"] {
  --bg: #0b0f17;
  --surface: #121826;
  --sum: #0f1520;
  --ink: #e7ecf5;
  --muted: #8a96ab;
  --line: #232c3d;
  --accent: #818cf8;
  --on-accent: #0b0d24;
  --ok: #34d399;
  --bad: #f87171;
}

.frm-03[data-brand="visa"] {
  --card-a: #1a1f71;
  --card-b: #3b5bdb;
}

.frm-03[data-brand="mastercard"] {
  --card-a: #2b1b10;
  --card-b: #c2410c;
}

.frm-03[data-brand="amex"] {
  --card-a: #0b4f6c;
  --card-b: #14b8a6;
}

.frm-03,
.frm-03 *,
.frm-03 *::before,
.frm-03 *::after {
  box-sizing: border-box;
}

.frm-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3.5rem);
}

.frm-03__wrap {
  container-type: inline-size;
  width: 100%;
  max-width: 68rem;
}

.frm-03__grid {
  display: grid;
  grid-template-columns: 1fr;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 1px 2px rgba(15,23,42,.04), 0 30px 70px -35px rgba(15,23,42,.35);
}

@container (min-width: 52rem) {
  .frm-03__grid {
    grid-template-columns: minmax(0,1.25fr) minmax(0,1fr);
  }
}

.frm-03__pay {
  display: grid;
  gap: 1.1rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.75rem);
}

.frm-03__summary {
  display: grid;
  gap: 1rem;
  align-content: start;
  padding: clamp(1.25rem,4cqi,2.75rem);
  background: var(--sum);
  border-top: 1px solid var(--line);
}

@container (min-width: 52rem) {
  .frm-03__summary {
    border-top: 0;
    border-left: 1px solid var(--line);
  }
}

@container (max-width: 51.99rem) {
  .frm-03__summary {
    order: -1;
    border-top: 0;
    border-bottom: 1px solid var(--line);
  }
}

.frm-03__steps {
  display: flex;
  gap: .5rem;
  font-size: .8rem;
  color: var(--muted);
}

.frm-03__steps span {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.frm-03__steps span:not(:last-child)::after {
  content: '';
  width: 1.25rem;
  height: 1px;
  background: var(--line);
}

.frm-03__steps [aria-current] {
  color: var(--ink);
  font-weight: 600;
}

.frm-03 h2 {
  margin: 0;
  font-size: 1.75rem;
  letter-spacing: -.03em;
}

.frm-03 h3 {
  margin: 0;
  font-size: 1.1rem;
  letter-spacing: -.01em;
}

.frm-03__methods {
  border: 0;
  margin: 0;
  padding: .3rem;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .3rem;
  background: var(--sum);
  border-radius: 1rem;
  border: 1px solid var(--line);
}

.frm-03__methods label {
  position: relative;
}

.frm-03__methods input {
  position: absolute;
  inset: 0;
  opacity: 0;
  margin: 0;
  cursor: pointer;
}

.frm-03__methods span {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  min-height: 2.75rem;
  border-radius: .75rem;
  font-size: .9rem;
  font-weight: 600;
  color: var(--muted);
  transition: background .25s, color .25s, box-shadow .25s;
}

.frm-03__methods svg {
  width: 1.15rem;
  height: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-03__methods input:checked + span {
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 1px 2px rgba(0,0,0,.06), 0 4px 12px -4px rgba(0,0,0,.12);
}

.frm-03__methods input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.frm-03__panel {
  display: none;
  gap: 1rem;
}

.frm-03__panel p {
  margin: 0;
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  background: var(--sum);
  border: 1px dashed var(--line);
  color: var(--muted);
  line-height: 1.55;
}

.frm-03:has([value="card"]:checked) .frm-03__panel--card,
.frm-03:has([value="wallet"]:checked) .frm-03__panel--wallet,
.frm-03:has([value="bank"]:checked) .frm-03__panel--bank {
  display: grid;
  animation: frm-03-in .45s var(--ease);
}

@keyframes frm-03-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }
}

.frm-03__card3d {
  position: relative;
  width: min(100%,21rem);
  aspect-ratio: 1.586;
  margin: .25rem auto .5rem;
  transform-style: preserve-3d;
  transition: rotate .8s var(--ease);
  perspective: 1000px;
}

.frm-03:has(#frm-03-cvc:focus) .frm-03__card3d {
  rotate: y 180deg;
}

.frm-03__face {
  position: absolute;
  inset: 0;
  border-radius: 1rem;
  padding: 1.15rem 1.25rem;
  color: #fff;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  background: radial-gradient(120% 140% at 0% 0%, color-mix(in oklab,var(--card-b) 90%,white), transparent 55%), linear-gradient(135deg,var(--card-a),var(--card-b));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.25), 0 24px 40px -18px color-mix(in oklab,var(--card-a) 80%,black);
  transition: background .5s;
}

.frm-03__face--front {
  display: grid;
  grid-template-rows: auto 1fr auto;
}

.frm-03__face--front::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(115deg,transparent 30%,rgba(255,255,255,.18) 45%,transparent 60%);
  pointer-events: none;
}

.frm-03__face--back {
  rotate: y 180deg;
  display: grid;
  align-content: center;
  gap: .8rem;
  padding: 1.15rem 0;
}

.frm-03__face--back i {
  height: 2.4rem;
  background: #0a0a0a;
}

.frm-03__pcvc {
  justify-self: end;
  margin-right: 1.25rem;
  padding: .35rem .7rem;
  background: #f8fafc;
  color: #0f172a;
  border-radius: .35rem;
  font: 500 .95rem var(--mono);
  letter-spacing: .15em;
}

.frm-03__chiprow {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.frm-03__chip {
  width: 2.4rem;
  height: 1.75rem;
  border-radius: .35rem;
  background: linear-gradient(135deg,#f5d77a,#b8913a);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.2);
}

.frm-03__brand {
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: .04em;
  font-style: italic;
}

.frm-03__pnum {
  align-self: center;
  font: 500 clamp(1rem,4.6cqi,1.3rem) var(--mono);
  letter-spacing: .08em;
  text-shadow: 0 1px 1px rgba(0,0,0,.3);
  white-space: nowrap;
}

.frm-03__prow {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.frm-03__prow span {
  display: grid;
  gap: .1rem;
  min-width: 0;
}

.frm-03__prow small {
  font-size: .6rem;
  text-transform: uppercase;
  letter-spacing: .12em;
  opacity: .7;
}

.frm-03__prow b {
  font-size: .85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .04em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.frm-03__field {
  display: grid;
  gap: .4rem;
}

.frm-03__field label {
  font-size: .85rem;
  font-weight: 600;
}

.frm-03__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.frm-03 input[type="text"] {
  width: 100%;
  min-height: 3rem;
  padding: .7rem .95rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  font: inherit;
  font-size: 1rem;
  transition: border-color .2s, box-shadow .25s var(--ease);
}

.frm-03 input[inputmode="numeric"] {
  font-family: var(--mono);
  font-size: .95rem;
  letter-spacing: .02em;
}

.frm-03 ::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.frm-03 input:focus-visible {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px color-mix(in oklab,var(--accent) 18%,transparent);
}

.frm-03 input:user-invalid {
  border-color: var(--bad);
}

.frm-03__numwrap {
  position: relative;
}

.frm-03 .frm-03__numwrap input {
  padding-right: 4.25rem;
}

.frm-03__badge {
  position: absolute;
  right: .6rem;
  top: 50%;
  translate: 0 -50%;
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: .3rem .5rem;
  border-radius: .35rem;
  background: var(--sum);
  color: var(--muted);
  border: 1px solid var(--line);
  opacity: 0;
  scale: .8;
  transition: opacity .25s, scale .3s var(--ease);
}

.frm-03:not([data-brand="none"]) .frm-03__badge {
  opacity: 1;
  scale: 1;
}

.frm-03__save {
  display: flex;
  align-items: center;
  gap: .6rem;
  font-size: .9rem;
  color: var(--muted);
  cursor: pointer;
  min-height: 2.75rem;
}

.frm-03__save input {
  width: 1.1rem;
  height: 1.1rem;
  accent-color: var(--accent);
  margin: 0;
}

.frm-03__paybtn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .6rem;
  min-height: 3.4rem;
  border: 0;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--on-accent);
  background: var(--accent);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 12px 26px -12px color-mix(in oklab,var(--accent) 90%,black);
  transition: translate .2s var(--ease), filter .2s;
}

.frm-03__paybtn svg {
  width: 1.15rem;
  height: 1.15rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
}

.frm-03__paybtn b {
  font-variant-numeric: tabular-nums;
}

.frm-03__paybtn:hover {
  translate: 0 -2px;
  filter: brightness(1.07);
}

.frm-03__paybtn:active {
  translate: 0 1px;
}

.frm-03__paybtn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.frm-03__paybtn[aria-busy="true"] {
  pointer-events: none;
  filter: saturate(.6);
}

.frm-03__secure {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
  text-align: center;
}

.frm-03__items {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.frm-03__items li {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: .9rem;
  align-items: center;
}

.frm-03__items img {
  width: 4.5rem;
  height: 4.5rem;
  object-fit: cover;
  border-radius: .9rem;
  background: var(--line);
  border: 1px solid var(--line);
}

.frm-03__items b {
  display: block;
  font-size: .95rem;
}

.frm-03__items small {
  display: block;
  color: var(--muted);
  font-size: .8rem;
  margin: .1rem 0 .4rem;
}

.frm-03__price {
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.frm-03__qty {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--line);
  border-radius: .6rem;
  background: var(--surface);
}

.frm-03__qty button {
  width: 2.25rem;
  height: 2.25rem;
  border: 0;
  background: transparent;
  color: var(--ink);
  font-size: 1.1rem;
  cursor: pointer;
  border-radius: .55rem;
}

.frm-03__qty button:hover {
  background: var(--sum);
}

.frm-03__qty button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.frm-03__qty output {
  min-width: 1.75rem;
  text-align: center;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.frm-03__promo {
  display: flex;
  gap: .5rem;
}

.frm-03__promo input {
  flex: 1;
  min-width: 0;
  text-transform: uppercase;
}

.frm-03__promo input::placeholder {
  text-transform: none;
}

.frm-03__apply {
  min-height: 3rem;
  padding: 0 1.1rem;
  border-radius: .75rem;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  font: inherit;
  font-weight: 600;
  cursor: pointer;
}

.frm-03__apply:hover {
  border-color: var(--ink);
}

.frm-03__apply:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.frm-03__codemsg {
  margin: -.5rem 0 0;
  font-size: .8rem;
  min-height: 1em;
}

.frm-03__codemsg[data-ok="true"] {
  color: var(--ok);
}

.frm-03__codemsg[data-ok="false"] {
  color: var(--bad);
}

.frm-03__totals {
  margin: 0;
  display: grid;
  gap: .6rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.frm-03__totals div {
  display: flex;
  justify-content: space-between;
  font-size: .92rem;
}

.frm-03__totals dt {
  color: var(--muted);
}

.frm-03__totals dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.frm-03__disc {
  color: var(--ok);
}

.frm-03__disc dt {
  color: inherit !important;
}

.frm-03:not(.has-disc) .frm-03__disc {
  display: none !important;
}

.frm-03__grand {
  padding-top: .8rem;
  border-top: 1px dashed var(--line);
  font-size: 1.15rem !important;
  font-weight: 700;
}

.frm-03__grand dt {
  color: var(--ink) !important;
}

.frm-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .frm-03 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .frm-03__face {
    background: Canvas;
    border: 1px solid CanvasText;
    color: CanvasText;
  }

  .frm-03__methods input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .frm-03__paybtn {
    border: 1px solid ButtonText;
  }
}
/* Theme toggle — top-right of the demo. Ink-relative colours, so it suits light and dark. */

.frm-03 {
  position: relative;
  padding-top: 72px;
  box-sizing: border-box;
}

.frm-03__theme {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 20;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  padding: 0;
  border-radius: 999px;
  border: 1px solid color-mix(in srgb, currentColor 22%, transparent);
  background: color-mix(in srgb, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background-color .2s, transform .2s;
}

.frm-03__theme:hover {
  background: color-mix(in srgb, currentColor 14%, transparent);
}

.frm-03__theme:active {
  transform: scale(.94);
}

.frm-03__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.frm-03__theme svg {
  width: 20px;
  height: 20px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.frm-03__theme .frm-03__sun,
.frm-03__theme[aria-pressed="true"] .frm-03__moon {
  display: none;
}

.frm-03__theme[aria-pressed="true"] .frm-03__sun {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .frm-03__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .frm-03__theme {
    border-color: ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
// Theme toggle (top-right): flips data-theme on the root and mirrors outside changes.
(() => {
  document.querySelectorAll('.frm-03').forEach((root) => {
    const btn = root.querySelector(':scope > [data-theme-toggle]');
    if (!btn || btn.dataset.wired) return;
    btn.dataset.wired = '1';
    const mq = matchMedia('(prefers-color-scheme: dark)');
    const isDark = () => (root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches);
    const sync = () => {
      const dark = isDark();
      btn.setAttribute('aria-pressed', String(dark));
      btn.title = dark ? 'Switch to light mode' : 'Switch to dark mode';
    };
    btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
    mq.addEventListener('change', sync);
    new MutationObserver(sync).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
    sync();
  });
})();
(() => {
  const root = document.querySelector('.frm-03');
  if (!root) return;
  const fmt = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' });
  const items = [{ price: 249, qty: 1 }, { price: 189, qty: 1 }];
  const CODES = { SAVE10: 0.10, WELCOME15: 0.15 };
  const TAX = 0.0825, FREE_SHIP = 300;
  let discount = 0;
  const $ = (s) => root.querySelector(s);
  const render = () => {
    root.querySelectorAll('.frm-03__items li').forEach((li, i) => {
      li.querySelector('output').textContent = items[i].qty;
      li.querySelector('.frm-03__price').textContent = fmt.format(items[i].price * items[i].qty);
    });
    const sub = items.reduce((a, it) => a + it.price * it.qty, 0);
    const disc = sub * discount, ship = sub - disc >= FREE_SHIP || sub === 0 ? 0 : 12;
    const tax = (sub - disc) * TAX, total = sub - disc + ship + tax;
    $('[data-k="sub"]').textContent = fmt.format(sub);
    $('[data-k="disc"]').textContent = '−' + fmt.format(disc);
    $('[data-k="ship"]').textContent = ship ? fmt.format(ship) : 'Free';
    $('[data-k="tax"]').textContent = fmt.format(tax);
    $('[data-k="total"]').textContent = fmt.format(total);
    $('.frm-03__paytotal').textContent = fmt.format(total);
    root.classList.toggle('has-disc', discount > 0);
  };
  root.querySelectorAll('.frm-03__qty button').forEach((b) => b.addEventListener('click', () => {
    const it = items[b.closest('li').dataset.i];
    it.qty = Math.max(0, Math.min(9, it.qty + Number(b.dataset.d)));
    render();
  }));
  $('.frm-03__apply').addEventListener('click', () => {
    const code = $('#frm-03-code').value.trim().toUpperCase(), msg = $('.frm-03__codemsg');
    discount = CODES[code] || 0;
    msg.dataset.ok = discount > 0;
    msg.textContent = discount ? code + ' applied — ' + Math.round(discount * 100) + '% off.' : code ? 'That code isn\'t valid.' : '';
    render();
  });
  const num = $('#frm-03-num'), exp = $('#frm-03-exp'), cvc = $('#frm-03-cvc'), name = $('#frm-03-name');
  const brandOf = (d) => /^3[47]/.test(d) ? 'amex' : /^4/.test(d) ? 'visa' : /^(5[1-5]|2[2-7])/.test(d) ? 'mastercard' : 'none';
  const label = { visa: 'VISA', mastercard: 'Mastercard', amex: 'AMEX', none: '' };
  num.addEventListener('input', () => {
    const before = num.value.slice(0, num.selectionStart).replace(/\D/g, '').length;
    const d = num.value.replace(/\D/g, '').slice(0, 16), brand = brandOf(d);
    const groups = brand === 'amex' ? [4, 6, 5] : [4, 4, 4, 4];
    let out = '', i = 0;
    groups.forEach((g) => { const part = d.slice(i, i + g); if (part) out += (out ? ' ' : '') + part; i += g; });
    num.value = out;
    let pos = 0, seen = 0;
    while (pos < out.length && seen < before) { if (/\d/.test(out[pos])) seen++; pos++; }
    num.setSelectionRange(pos, pos);
    if (root.dataset.brand !== brand) $('#frm-03-brand-live').textContent = label[brand] ? label[brand] + ' detected' : '';
    root.dataset.brand = brand;
    $('.frm-03__badge').textContent = label[brand];
    $('.frm-03__brand').textContent = label[brand];
    const mask = (brand === 'amex' ? '•••• •••••• •••••' : '•••• •••• •••• ••••');
    $('.frm-03__pnum').textContent = out + mask.slice(out.length);
    num.setCustomValidity(d.length >= (brand === 'amex' ? 15 : 16) ? '' : 'Incomplete card number');
  });
  exp.addEventListener('input', (e) => {
    let d = exp.value.replace(/\D/g, '').slice(0, 4);
    if (d.length === 1 && Number(d) > 1) d = '0' + d;
    exp.value = d.length > 2 ? d.slice(0, 2) + ' / ' + d.slice(2) : (d.length === 2 && e.inputType !== 'deleteContentBackward' ? d + ' / ' : d);
    $('.frm-03__pexp').textContent = d.length ? (d.slice(0, 2) + '/' + d.slice(2)).replace(/\/$/, '') : 'MM/YY';
  });
  cvc.addEventListener('input', () => { cvc.value = cvc.value.replace(/\D/g, ''); $('.frm-03__pcvc').textContent = cvc.value || '•••'; });
  name.addEventListener('input', () => { $('.frm-03__pname').textContent = name.value || 'Your name'; });
  $('.frm-03__paybtn').addEventListener('click', () => {
    const btn = $('.frm-03__paybtn'), status = $('.frm-03__secure');
    if (root.querySelector('[value="card"]').checked) {
      const bad = [num, exp, cvc, name].find((f) => !f.value || !f.checkValidity());
      if (bad) { bad.focus(); status.textContent = 'Please complete your card details.'; return; }
    }
    btn.setAttribute('aria-busy', 'true'); btn.querySelector('span').textContent = 'Processing…';
    setTimeout(() => { btn.removeAttribute('aria-busy'); btn.querySelector('span').textContent = 'Paid — thank you'; status.textContent = 'Payment confirmed. A receipt is on its way.'; }, 1400);
  });
  render();
})();
```
