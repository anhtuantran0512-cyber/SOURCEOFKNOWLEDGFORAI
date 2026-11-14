---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-input-field-shake-on-wrong-value/"
title: "CSS Input Field Shake on Wrong Value"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Two 'wrong value' flavors that go beyond format validation: a promo-code field that shakes when the code exists in the wrong universe (with a working demo…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Input Field Shake on Wrong Value
Source: https://codefronts.com/motion/css-shake-animation/css-input-field-shake-on-wrong-value/

Two 'wrong value' flavors that go beyond format validation: a promo-code field that shakes when the code exists in the wrong universe (with a working demo code), and a pure-CSS quantity stepper that rattles via :out-of-range the instant the number leaves its min/max window.
## HTML
```html
<div class="shk-04-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="shk-04a" aria-label="Promo code field that shakes on a wrong code">
  <div class="shk-04a__card">
    <div class="shk-04a__head"><h2 class="shk-04a__title">Order summary</h2><span class="shk-04a__total">$132.00</span></div>
    <div class="shk-04a__row"><span>Aurora desk mat × 2</span><span>$96.00</span></div>
    <div class="shk-04a__row"><span>Keycap set · fog</span><span>$36.00</span></div>
    <form class="shk-04a__promo" id="shk-04a-form" novalidate>
      <div class="shk-04a__wrap" id="shk-04a-wrap">
        <input class="shk-04a__input" id="shk-04a-code" type="text" placeholder="PROMO CODE" aria-label="Promo code" aria-describedby="shk-04a-msg" autocomplete="off" spellcheck="false">
        <button class="shk-04a__apply" type="submit">Apply</button>
      </div>
      <p class="shk-04a__msg" id="shk-04a-msg" aria-live="polite">Psst — <b>SHAKE30</b> works. Anything else gets rejected.</p>
    </form>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="shk-04b" aria-label="Quantity stepper that shakes when out of range">
  <div class="shk-04b__card">
    <p class="shk-04b__badge">:out-of-range powers the shake</p>
    <h2 class="shk-04b__name">Studio headphones</h2>
    <p class="shk-04b__limit">Limit <b>1–8</b> per order</p>
    <div class="shk-04b__qty" id="shk-04b-qty">
      <button class="shk-04b__step" type="button" data-d="-1" aria-label="Decrease quantity">−</button>
      <input class="shk-04b__num" id="shk-04b-num" type="number" value="1" min="1" max="8" aria-label="Quantity">
      <button class="shk-04b__step" type="button" data-d="1" aria-label="Increase quantity">+</button>
    </div>
    <p class="shk-04b__note"><span>Out of range — we can only ship 1 to 8 units.</span></p>
    <p class="shk-04b__hint" aria-hidden="true">step past 8 (or type 99) — CSS notices, no validation code at all</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-04-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-04-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-04a,
.shk-04a *,
.shk-04a *::before,
.shk-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-04a {
  --ink: #1d2129;
  --err: oklch(0.6 0.2 25);
  --ok: oklch(0.55 0.14 155);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f4f5f7,#e8eaee);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-04a__card {
  width: min(430px,100%);
  padding: 30px;
  border-radius: 18px;
  background: #fff;
  border: 1px solid rgba(29,33,41,.1);
  box-shadow: 0 30px 70px -35px rgba(29,33,41,.4);
}

.shk-04a__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding-bottom: 14px;
  border-bottom: 1.5px dashed rgba(29,33,41,.15);
}

.shk-04a__title {
  font-size: 19px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
}

.shk-04a__total {
  font-size: 19px;
  font-weight: 800;
  color: var(--ink);
}

.shk-04a__row {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
  font-size: 13.5px;
  color: rgba(29,33,41,.6);
}

.shk-04a__promo {
  margin-top: 20px;
}

.shk-04a__wrap {
  display: flex;
  gap: 8px;
  padding: 6px;
  background: #f2f3f6;
  border: 1.5px solid rgba(29,33,41,.12);
  border-radius: 13px;
  transition: border-color .2s,background .2s;
}

.shk-04a__wrap:focus-within {
  border-color: var(--ink);
}

.shk-04a__wrap.is-wrong {
  border-color: var(--err);
  background: oklch(0.6 0.2 25 / .06);
  animation: shk-04a-shake .48s cubic-bezier(.36,.07,.19,.97);
}

.shk-04a__wrap.is-ok {
  border-color: var(--ok);
  background: oklch(0.55 0.14 155 / .07);
}

.shk-04a__input {
  flex: 1;
  min-width: 0;
  border: 0;
  outline: none;
  background: transparent;
  padding: 9px 10px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .12em;
  color: var(--ink);
  text-transform: uppercase;
}

.shk-04a__input::placeholder {
  color: rgba(29,33,41,.35);
}

.shk-04a__apply {
  flex: none;
  border: 0;
  border-radius: 9px;
  padding: 10px 18px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: #fff;
  background: var(--ink);
  cursor: pointer;
  transition: transform .15s,background .2s;
}

.shk-04a__apply:hover {
  background: #343b47;
}

.shk-04a__apply:active {
  transform: scale(.96);
}

.shk-04a__msg {
  margin-top: 10px;
  font-size: 12.5px;
  color: rgba(29,33,41,.5);
  min-height: 18px;
}

.shk-04a__msg b {
  color: var(--ink);
}

.shk-04a__msg.err {
  color: var(--err);
}

.shk-04a__msg.ok {
  color: var(--ok);
  font-weight: 600;
}

@keyframes shk-04a-shake {
  20% {
    translate: -8px 0;
  }

  40% {
    translate: 7px 0;
  }

  60% {
    translate: -5px 0;
  }

  80% {
    translate: 2px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-04a__wrap.is-wrong {
    animation: none;
  }
}

.shk-04b,
.shk-04b *,
.shk-04b *::before,
.shk-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-04b {
  --err: oklch(0.66 0.21 24);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 100% at 50% 0%,#171326,#0d0b16);
  font-family: 'Sora','Segoe UI',system-ui,sans-serif;
}

.shk-04b__card {
  width: min(400px,100%);
  padding: 34px;
  border-radius: 22px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(185,170,255,.16);
  box-shadow: 0 40px 90px -45px rgba(0,0,0,.9);
  text-align: center;
}

.shk-04b__badge {
  display: inline-block;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.78 0.13 300);
  background: oklch(0.78 0.13 300 / .1);
  border: 1px solid oklch(0.78 0.13 300 / .3);
  padding: 5px 11px;
  border-radius: 999px;
}

.shk-04b__name {
  margin-top: 16px;
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: #f0edff;
}

.shk-04b__limit {
  margin-top: 6px;
  font-size: 13px;
  color: rgba(226,220,250,.5);
}

.shk-04b__limit b {
  color: rgba(226,220,250,.85);
}

.shk-04b__qty {
  margin: 22px auto 0;
  display: flex;
  align-items: stretch;
  gap: 8px;
  width: max-content;
  padding: 7px;
  background: rgba(8,6,16,.55);
  border: 1.5px solid rgba(185,170,255,.2);
  border-radius: 16px;
  transition: border-color .2s;
}

.shk-04b__qty:has(.shk-04b__num:out-of-range) {
  border-color: var(--err);
  animation: shk-04b-shake .45s cubic-bezier(.36,.07,.19,.97);
}

.shk-04b__step {
  width: 46px;
  border: 0;
  border-radius: 10px;
  background: rgba(255,255,255,.08);
  color: #f0edff;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.shk-04b__step:hover {
  background: rgba(255,255,255,.14);
}

.shk-04b__step:active {
  scale: .93;
}

.shk-04b__num {
  width: 76px;
  text-align: center;
  border: 0;
  outline: none;
  background: transparent;
  font: inherit;
  font-size: 22px;
  font-weight: 700;
  color: #f0edff;
  -moz-appearance: textfield;
  appearance: textfield;
}

.shk-04b__num::-webkit-outer-spin-button,
.shk-04b__num::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.shk-04b__num:out-of-range {
  color: var(--err);
}

.shk-04b__note {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s,margin-top .3s;
  font-size: 12.5px;
  color: var(--err);
}

.shk-04b__note span {
  overflow: hidden;
}

.shk-04b__card:has(.shk-04b__num:out-of-range) .shk-04b__note {
  grid-template-rows: 1fr;
  margin-top: 12px;
}

.shk-04b__hint {
  margin-top: 18px;
  font-size: 11.5px;
  color: rgba(226,220,250,.35);
}

@keyframes shk-04b-shake {
  20% {
    translate: -8px 0;
  }

  40% {
    translate: 7px 0;
  }

  60% {
    translate: -4px 0;
  }

  80% {
    translate: 2px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-04b__qty:has(.shk-04b__num:out-of-range) {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var form=document.getElementById('shk-04a-form'); if(!form) return;
  var wrap=document.getElementById('shk-04a-wrap'),input=document.getElementById('shk-04a-code'),msg=document.getElementById('shk-04a-msg');
  wrap.addEventListener('animationend',function(){ wrap.classList.remove('is-wrong'); });
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var code=input.value.trim().toUpperCase();
    if(code==='SHAKE30'){
      wrap.classList.remove('is-wrong'); wrap.classList.add('is-ok');
      msg.className='shk-04a__msg ok'; msg.textContent='SHAKE30 applied — 30% off, new total $92.40.';
      return;
    }
    wrap.classList.remove('is-ok','is-wrong');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ wrap.classList.add('is-wrong'); }); });
    msg.className='shk-04a__msg err';
    msg.textContent=code===''?'Enter a code first.':'“'+code+'” isn\u2019t a valid code — try SHAKE30.';
    input.select();
  });
})();

(function(){
  // The steppers are the only JS — the shake itself is pure CSS via :out-of-range.
  // They intentionally step past min/max so you can feel the pseudo-class fire.
  var qty=document.getElementById('shk-04b-qty'); if(!qty) return;
  var num=document.getElementById('shk-04b-num');
  qty.addEventListener('click',function(e){
    var b=e.target.closest('[data-d]'); if(!b) return;
    num.value=String((parseInt(num.value||'0',10))+parseInt(b.dataset.d,10));
  });
})();
```
