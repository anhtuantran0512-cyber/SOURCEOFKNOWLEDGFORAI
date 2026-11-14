---
source: "codefronts"
url: "https://codefronts.com/layouts/css-settings-pages/payment-method-settings-card/"
title: "Payment Method Settings Card"
section: "layouts"
category: "css-settings-pages"
category_name: "CSS Settings Pages"
description: "A premium payment-methods panel: a glossy 3D card preview that mirrors the add-card form as you type and flips to show the CVC when that field is focused,…"
has_js: "true"
---

Here's a working CSS Settings Page from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Payment Method Settings Card
Source: https://codefronts.com/layouts/css-settings-pages/payment-method-settings-card/

A premium payment-methods panel: a glossy 3D card preview that mirrors the add-card form as you type and flips to show the CVC when that field is focused, auto-formatted card number and expiry with brand detection (Visa, Mastercard, Amex), saved methods as radio rows where :has() highlights the default, and an 'expires soon' warning. Uses the right autocomplete tokens so browsers and password managers can autofill.
## HTML
```html
<section class="csp-05">
  <div class="csp-05__panel">
    <header class="csp-05__head">
      <h1>Payment methods</h1>
      <p>Your default method is charged on Nov 14 for the Pro plan.</p>
    </header>

    <div class="csp-05__stage" aria-hidden="true">
      <div class="csp-05__cc">
        <div class="csp-05__face csp-05__face--front">
          <div class="csp-05__ccrow"><span class="csp-05__chip"></span><span class="csp-05__brand" data-brand>VISA</span></div>
          <span class="csp-05__num" data-pnum>•••• •••• •••• 4242</span>
          <div class="csp-05__ccrow csp-05__ccrow--meta"><span><small>Card holder</small><b data-pname>AVA MITCHELL</b></span><span><small>Expires</small><b data-pexp>08/28</b></span></div>
        </div>
        <div class="csp-05__face csp-05__face--back">
          <span class="csp-05__stripe"></span>
          <span class="csp-05__cvcbox"><small>CVC</small><b data-pcvc>•••</b></span>
        </div>
      </div>
    </div>

    <fieldset class="csp-05__methods">
      <legend class="csp-05__sr">Saved payment methods</legend>
      <label class="csp-05__method">
        <input type="radio" name="csp05-m" checked>
        <span class="csp-05__logo csp-05__logo--visa">VISA</span>
        <span class="csp-05__mtext"><b>Visa ending 4242</b><small>Expires 08/2028</small></span>
        <span class="csp-05__tag">Default</span>
      </label>
      <label class="csp-05__method">
        <input type="radio" name="csp05-m">
        <span class="csp-05__logo csp-05__logo--mc"><i></i><i></i></span>
        <span class="csp-05__mtext"><b>Mastercard ending 8210</b><small class="csp-05__warn">Expires 11/2026 · update soon</small></span>
        <span class="csp-05__tag">Default</span>
      </label>
      <label class="csp-05__method">
        <input type="radio" name="csp05-m">
        <span class="csp-05__logo csp-05__logo--bank">BANK</span>
        <span class="csp-05__mtext"><b>US bank account ••6789</b><small>ACH · verified</small></span>
        <span class="csp-05__tag">Default</span>
      </label>
    </fieldset>

    <details class="csp-05__add">
      <summary>Add a new card</summary>
      <form class="csp-05__form" data-form>
        <label class="csp-05__field csp-05__field--full"><span>Card number</span><input data-num inputmode="numeric" autocomplete="cc-number" placeholder="1234 1234 1234 1234" maxlength="19" required></label>
        <label class="csp-05__field"><span>Expiry</span><input data-exp inputmode="numeric" autocomplete="cc-exp" placeholder="MM / YY" maxlength="7" required></label>
        <label class="csp-05__field"><span>CVC</span><input data-cvc inputmode="numeric" autocomplete="cc-csc" placeholder="123" maxlength="4" required></label>
        <label class="csp-05__field csp-05__field--full"><span>Name on card</span><input data-name autocomplete="cc-name" placeholder="Ava Mitchell" required></label>
        <label class="csp-05__check csp-05__field--full"><input type="checkbox" checked> Set as default payment method</label>
        <button class="csp-05__btn csp-05__field--full" type="submit">Save card</button>
        <p class="csp-05__secure csp-05__field--full">Encrypted and processed by our PCI DSS Level 1 payment partner.</p>
      </form>
    </details>
  </div>
</section>
```
## CSS
```css
.csp-05,
.csp-05 *,
.csp-05 *::before,
.csp-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.csp-05 {
  --bg: oklch(0.14 0.012 285);
  --surface: oklch(0.19 0.015 285);
  --raised: oklch(0.23 0.018 285);
  --text: oklch(0.96 0.005 285);
  --muted: oklch(0.7 0.015 285);
  --line: oklch(0.3 0.02 285);
  --accent: oklch(0.74 0.15 295);
  --warn: oklch(0.8 0.14 75);
  color-scheme: dark;
  display: grid;
  align-items: center;
  justify-items: center;
  min-height: 100vh;
  min-height: 100dvh;
  padding: 40px 20px;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: radial-gradient(70% 50% at 50% 0%,oklch(0.28 0.08 295/.6),transparent 70%),var(--bg);
  color: var(--text);
  accent-color: var(--accent);
  width: 100%;
}

.csp-05__sr {
  position: absolute!important;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.csp-05__panel {
  width: min(480px,100%);
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 28px;
  border: 1px solid var(--line);
  border-radius: 24px;
  background: var(--surface);
  box-shadow: 0 40px 80px -40px oklch(0 0 0/.8);
}

.csp-05__head h1 {
  font: 700 22px/1.15 system-ui,sans-serif;
  letter-spacing: -.02em;
}

.csp-05__head p {
  font: 400 14px/1.5 system-ui,sans-serif;
  color: var(--muted);
  margin-top: 6px;
}

.csp-05__stage {
  perspective: 1200px;
}

.csp-05__cc {
  position: relative;
  aspect-ratio: 1.586;
  border-radius: 18px;
  transform-style: preserve-3d;
  transition: rotate .7s cubic-bezier(.3,.7,.2,1);
}

.csp-05:has([data-cvc]:focus) .csp-05__cc {
  rotate: y 180deg;
}

.csp-05__face {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 22px;
  border-radius: inherit;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  overflow: hidden;
  color: #fff;
  background: radial-gradient(120% 90% at 0% 0%,oklch(0.6 0.2 300),transparent 55%),radial-gradient(90% 90% at 100% 100%,oklch(0.55 0.17 250),transparent 60%),oklch(0.28 0.08 280);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.25),0 24px 48px -20px oklch(0.4 0.2 290/.7);
}

.csp-05__face::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(115deg,transparent 30%,oklch(1 0 0/.18) 45%,transparent 60%);
  pointer-events: none;
}

.csp-05__face--back {
  rotate: y 180deg;
  justify-content: flex-start;
  gap: 22px;
  padding: 22px 0;
}

.csp-05__ccrow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.csp-05__ccrow--meta {
  align-items: flex-end;
}

.csp-05__ccrow--meta span {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.csp-05__ccrow small {
  font: 600 9.5px/1 system-ui,sans-serif;
  letter-spacing: .12em;
  text-transform: uppercase;
  opacity: .7;
}

.csp-05__ccrow b {
  font: 600 14px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .06em;
  max-width: 220px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.csp-05__chip {
  width: 42px;
  height: 32px;
  border-radius: 7px;
  background: linear-gradient(135deg,oklch(0.88 0.08 85),oklch(0.72 0.1 75));
  box-shadow: inset 0 0 0 1px oklch(0.6 0.08 75/.6);
}

.csp-05__brand {
  font: italic 800 20px/1 system-ui,sans-serif;
  letter-spacing: .02em;
}

.csp-05__num {
  font: 500 clamp(16px,5vw,21px)/1 ui-monospace,Menlo,monospace;
  letter-spacing: .12em;
  text-shadow: 0 1px 1px oklch(0 0 0/.3);
}

.csp-05__stripe {
  height: 42px;
  background: oklch(0.12 0.01 285);
}

.csp-05__cvcbox {
  align-self: flex-end;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 22px;
  padding: 8px 12px;
  border-radius: 6px;
  background: #fff;
  color: oklch(0.2 0.02 285);
}

.csp-05__cvcbox b {
  font: 700 15px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .1em;
}

.csp-05__methods {
  border: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.csp-05__method {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--raised);
  cursor: pointer;
  transition: border-color .2s,background .2s;
}

.csp-05__method:hover {
  border-color: oklch(0.4 0.03 285);
}

.csp-05__method:has(input:checked) {
  border-color: var(--accent);
  background: oklch(0.74 0.15 295/.08);
}

.csp-05__method:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-05__method input {
  width: 18px;
  height: 18px;
  flex: none;
}

.csp-05__logo {
  flex: none;
  display: grid;
  place-items: center;
  width: 46px;
  height: 32px;
  border-radius: 6px;
  font: italic 800 11px/1 system-ui,sans-serif;
  background: #fff;
  color: oklch(0.35 0.15 265);
}

.csp-05__logo--mc {
  position: relative;
  background: oklch(0.22 0.01 285);
}

.csp-05__logo--mc i {
  position: absolute;
  top: 8px;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: oklch(0.63 0.22 27);
}

.csp-05__logo--mc i:first-child {
  left: 10px;
}

.csp-05__logo--mc i:last-child {
  left: 20px;
  background: oklch(0.8 0.16 75);
  mix-blend-mode: screen;
}

.csp-05__logo--bank {
  font-style: normal;
  font-size: 9.5px;
  letter-spacing: .08em;
  color: var(--text);
  background: oklch(0.3 0.02 285);
}

.csp-05__mtext {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 3px;
  min-width: 0;
}

.csp-05__mtext b {
  font: 600 14px/1.2 system-ui,sans-serif;
}

.csp-05__mtext small {
  font: 400 12.5px/1.2 system-ui,sans-serif;
  color: var(--muted);
}

.csp-05__mtext .csp-05__warn {
  color: var(--warn);
}

.csp-05__tag {
  display: none;
  padding: 4px 9px;
  border-radius: 999px;
  font: 650 11px/1 system-ui,sans-serif;
  color: oklch(0.2 0.05 295);
  background: var(--accent);
}

.csp-05__method:has(input:checked) .csp-05__tag {
  display: inline-block;
}

.csp-05__add {
  border: 1px dashed var(--line);
  border-radius: 14px;
  transition: border-color .2s;
}

.csp-05__add[open] {
  border-style: solid;
}

.csp-05__add summary {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 52px;
  padding: 0 16px;
  font: 600 14px/1 system-ui,sans-serif;
  cursor: pointer;
  list-style: none;
  border-radius: 14px;
}

.csp-05__add summary::-webkit-details-marker {
  display: none;
}

.csp-05__add summary::before {
  content: "+";
  display: grid;
  place-items: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: oklch(1 0 0/.08);
  font: 500 16px/1 system-ui,sans-serif;
  transition: rotate .25s;
}

.csp-05__add[open] summary::before {
  rotate: 45deg;
}

.csp-05__add summary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.csp-05__form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  padding: 4px 16px 18px;
}

.csp-05__field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  font: 550 12.5px/1 system-ui,sans-serif;
  color: var(--muted);
}

.csp-05__field--full {
  grid-column: 1/-1;
}

.csp-05__field input {
  min-height: 46px;
  padding: 0 14px;
  border: 1px solid var(--line);
  border-radius: 11px;
  background: var(--bg);
  color: var(--text);
  font: 500 15px/1 ui-monospace,Menlo,monospace;
  letter-spacing: .04em;
  transition: border-color .15s,box-shadow .15s;
}

.csp-05__field input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.74 0.15 295/.2);
}

.csp-05__field input:user-invalid {
  border-color: oklch(0.65 0.2 25);
}

.csp-05__check {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 32px;
  font: 500 13.5px/1 system-ui,sans-serif;
  color: var(--text);
}

.csp-05__check input {
  width: 18px;
  height: 18px;
}

.csp-05__btn {
  min-height: 48px;
  border: 0;
  border-radius: 12px;
  font: 650 15px/1 system-ui,sans-serif;
  color: oklch(0.18 0.05 295);
  background: var(--accent);
  cursor: pointer;
  transition: filter .15s,transform .1s;
}

.csp-05__btn:hover {
  filter: brightness(1.08);
}

.csp-05__btn:active {
  transform: scale(.99);
}

.csp-05__btn:focus-visible {
  outline: 2px solid var(--text);
  outline-offset: 3px;
}

.csp-05__secure {
  font: 400 12px/1.4 system-ui,sans-serif;
  color: var(--muted);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .csp-05__cc {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var root = document.querySelector('.csp-05');
  var num = root.querySelector('[data-num]'), exp = root.querySelector('[data-exp]');
  var cvc = root.querySelector('[data-cvc]'), name = root.querySelector('[data-name]');
  var pnum = root.querySelector('[data-pnum]'), pexp = root.querySelector('[data-pexp]');
  var pcvc = root.querySelector('[data-pcvc]'), pname = root.querySelector('[data-pname]');
  var brand = root.querySelector('[data-brand]');

  function detect(d) {
    if (/^3[47]/.test(d)) return 'AMEX';
    if (/^(5[1-5]|2[2-7])/.test(d)) return 'MASTERCARD';
    if (/^4/.test(d)) return 'VISA';
    if (/^6(011|5)/.test(d)) return 'DISCOVER';
    return 'CARD';
  }
  num.addEventListener('input', function () {
    var d = num.value.replace(/\D/g, '').slice(0, 16);
    var b = detect(d), groups = b === 'AMEX' ? [4, 6, 5] : [4, 4, 4, 4], out = [], i = 0;
    groups.forEach(function (g) { if (d.slice(i, i + g)) out.push(d.slice(i, i + g)); i += g; });
    num.value = out.join(' ');
    brand.textContent = d ? b : 'VISA';
    var mask = (b === 'AMEX' ? '•••• •••••• •••••' : '•••• •••• •••• ••••');
    pnum.textContent = d ? num.value + mask.slice(num.value.length) : '•••• •••• •••• 4242';
  });
  exp.addEventListener('input', function (e) {
    var d = exp.value.replace(/\D/g, '').slice(0, 4);
    if (d.length === 1 && d > 1) d = '0' + d;
    exp.value = d.length > 2 ? d.slice(0, 2) + ' / ' + d.slice(2) : (d.length === 2 && e.inputType !== 'deleteContentBackward' ? d + ' / ' : d);
    pexp.textContent = d ? (d.slice(0, 2) + '/' + (d.slice(2) || 'YY')) : '08/28';
  });
  cvc.addEventListener('input', function () {
    cvc.value = cvc.value.replace(/\D/g, '').slice(0, 4);
    pcvc.textContent = cvc.value || '•••';
  });
  name.addEventListener('input', function () { pname.textContent = name.value.toUpperCase() || 'AVA MITCHELL'; });

  root.querySelector('[data-form]').addEventListener('submit', function (e) {
    e.preventDefault();
    var btn = e.target.querySelector('button');
    btn.textContent = 'Card saved';
    setTimeout(function () { btn.textContent = 'Save card'; }, 1800);
  });
})();
```
