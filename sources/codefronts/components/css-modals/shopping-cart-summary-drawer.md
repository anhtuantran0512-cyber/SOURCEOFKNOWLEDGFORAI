---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/shopping-cart-summary-drawer/"
title: "Shopping Cart Summary Drawer"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A right-side mini-cart that slides in over the page: line items with thumbnails and quantity, a free-shipping progress bar, live subtotal and a direct…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shopping Cart Summary Drawer
Source: https://codefronts.com/components/css-modals/shopping-cart-summary-drawer/

A right-side mini-cart that slides in over the page: line items with thumbnails and quantity, a free-shipping progress bar, live subtotal and a direct checkout CTA — the off-canvas drawer pattern, done as an accessible dialog.
## HTML
```html
<div class="cm-06">
  <button class="cm-06__open" type="button">
    <span aria-hidden="true">🛍</span> Your bag <span class="cm-06__count">2</span>
  </button>

  <dialog class="cm-06__dlg" aria-labelledby="cm-06-title">
    <div class="cm-06__card">
      <header class="cm-06__head">
        <h2 id="cm-06-title">Your bag</h2>
        <button class="cm-06__x" type="button" aria-label="Close bag">&times;</button>
      </header>
      <div class="cm-06__ship">
        <p class="cm-06__shiptxt"><b class="cm-06__left">$52</b> away from free shipping</p>
        <div class="cm-06__bar" role="progressbar" aria-valuemin="0" aria-valuemax="200" aria-valuenow="148"><i style="width:74%"></i></div>
      </div>
      <ul class="cm-06__items">
        <li class="cm-06__item">
          <div class="cm-06__thumb" data-label="shot"></div>
          <div class="cm-06__meta"><p class="cm-06__name">Merino Overshirt</p><p class="cm-06__var">Forest · M</p>
            <div class="cm-06__qty"><button type="button" data-d="-1" data-p="98" aria-label="Decrease quantity">−</button><span aria-live="polite">1</span><button type="button" data-d="1" data-p="98" aria-label="Increase quantity">+</button></div>
          </div>
          <p class="cm-06__lp" data-base="98">$98</p>
        </li>
        <li class="cm-06__item">
          <div class="cm-06__thumb" data-label="shot"></div>
          <div class="cm-06__meta"><p class="cm-06__name">Canvas Field Cap</p><p class="cm-06__var">Rust · OS</p>
            <div class="cm-06__qty"><button type="button" data-d="-1" data-p="50" aria-label="Decrease quantity">−</button><span aria-live="polite">1</span><button type="button" data-d="1" data-p="50" aria-label="Increase quantity">+</button></div>
          </div>
          <p class="cm-06__lp" data-base="50">$50</p>
        </li>
      </ul>
      <footer class="cm-06__foot">
        <div class="cm-06__sub"><span>Subtotal</span><b id="cm-06-total">$148</b></div>
        <button type="button" class="cm-06__checkout">Checkout</button>
        <p class="cm-06__note">Shipping &amp; taxes calculated at checkout</p>
      </footer>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-06,
.cm-06 *,
.cm-06 *::before,
.cm-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-06 {
  --accent: oklch(0.7 0.16 25);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#16110f,#0a0706);
}

.cm-06__open {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  padding: 12px 22px;
  border-radius: 11px;
  color: #f3e7e3;
  font: 600 14px system-ui;
  border: 1px solid #33251f;
  background: #1a1310;
  transition: border-color .2s,background .2s;
}

.cm-06__open:hover {
  border-color: var(--accent);
  background: #211712;
}

.cm-06__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-06__count {
  min-width: 22px;
  height: 22px;
  padding: 0 6px;
  display: grid;
  place-items: center;
  border-radius: 11px;
  background: var(--accent);
  color: #180a07;
  font: 700 12px system-ui;
}

.cm-06__dlg {
  margin: 0 0 0 auto;
  height: 100%;
  max-height: 100dvh;
  width: min(400px,100vw);
  padding: 0;
  border: none;
  border-radius: 0;
  color: #efe4e0;
  background: linear-gradient(180deg,#191210,#120c0a);
  box-shadow: -30px 0 80px -20px #000;
  transform: translateX(100%);
  transition: transform .34s cubic-bezier(.4,0,.2,1),overlay .34s allow-discrete,display .34s allow-discrete;
}

.cm-06__dlg[open] {
  transform: none;
}

@starting-style {
  .cm-06__dlg[open] {
    transform: translateX(100%);
  }
}

.cm-06__dlg::backdrop {
  background: rgba(6,4,3,0);
  transition: background .34s,overlay .34s allow-discrete,display .34s allow-discrete;
}

.cm-06__dlg[open]::backdrop {
  background: rgba(6,4,3,.55);
}

@starting-style {
  .cm-06__dlg[open]::backdrop {
    background: rgba(6,4,3,0);
  }
}

.cm-06__card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.cm-06__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 22px 22px 16px;
  border-bottom: 1px solid #2a1e19;
}

.cm-06__head h2 {
  font-size: 18px;
  font-weight: 700;
  color: #f7ede9;
}

.cm-06__x {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: #9a827b;
  font-size: 22px;
  cursor: pointer;
}

.cm-06__x:hover {
  background: #241a16;
  color: #fff;
}

.cm-06__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-06__ship {
  padding: 16px 22px;
  border-bottom: 1px solid #2a1e19;
}

.cm-06__shiptxt {
  font-size: 13px;
  color: #c0aca5;
  margin-bottom: 9px;
}

.cm-06__left {
  color: var(--accent);
}

.cm-06__bar {
  height: 6px;
  border-radius: 6px;
  background: #2a1e19;
  overflow: hidden;
}

.cm-06__bar i {
  display: block;
  height: 100%;
  background: var(--accent);
  border-radius: 6px;
  transition: width .3s;
}

.cm-06__items {
  list-style: none;
  flex: 1;
  overflow: auto;
  padding: 8px 22px;
}

.cm-06__item {
  display: grid;
  grid-template-columns: 56px 1fr auto;
  gap: 14px;
  align-items: center;
  padding: 16px 0;
  border-bottom: 1px solid #241a15;
}

.cm-06__thumb {
  width: 56px;
  height: 64px;
  border-radius: 9px;
  position: relative;
  background: repeating-linear-gradient(135deg,#241a15 0 8px,#1c130f 8px 16px);
  border: 1px solid #33251f;
}

.cm-06__thumb::after {
  content: attr(data-label);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: 9px ui-monospace,monospace;
  letter-spacing: .1em;
  color: #5a463d;
}

.cm-06__name {
  font-size: 14px;
  font-weight: 600;
  color: #f2e7e2;
}

.cm-06__var {
  font-size: 12px;
  color: #9a827b;
  margin: 2px 0 8px;
}

.cm-06__qty {
  display: inline-flex;
  align-items: center;
  border: 1px solid #33251f;
  border-radius: 8px;
  overflow: hidden;
}

.cm-06__qty button {
  width: 30px;
  height: 30px;
  border: none;
  background: #1a1310;
  color: #d8c4bd;
  font-size: 16px;
  cursor: pointer;
}

.cm-06__qty button:hover {
  background: #241a16;
}

.cm-06__qty button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cm-06__qty span {
  min-width: 30px;
  text-align: center;
  font: 600 13px system-ui;
  color: #fff;
}

.cm-06__lp {
  font-size: 14px;
  font-weight: 700;
  color: #f2e7e2;
}

.cm-06__foot {
  padding: 18px 22px 22px;
  border-top: 1px solid #2a1e19;
  background: #140d0b;
}

.cm-06__sub {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 14px;
}

.cm-06__sub span {
  font-size: 14px;
  color: #b09a92;
}

.cm-06__sub b {
  font-size: 22px;
  color: #fff;
}

.cm-06__checkout {
  width: 100%;
  padding: 15px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #180a07;
  font: 700 15px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-06__checkout:hover {
  filter: brightness(1.08);
}

.cm-06__checkout:active {
  transform: translateY(1px);
}

.cm-06__checkout:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.cm-06__note {
  text-align: center;
  font-size: 11.5px;
  color: #7a655d;
  margin-top: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .cm-06__dlg,
    .cm-06__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-06');
  var dlg = root.querySelector('.cm-06__dlg');
  var total = root.querySelector('#cm-06-total');
  var bar = root.querySelector('.cm-06__bar i');
  var left = root.querySelector('.cm-06__left');
  var THRESHOLD = 200;
  root.querySelector('.cm-06__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-06__x').addEventListener('click', function(){ dlg.close(); });
  function recalc(){
    var sum = 0;
    root.querySelectorAll('.cm-06__item').forEach(function(li){
      var q = parseInt(li.querySelector('.cm-06__qty span').textContent,10);
      var base = parseInt(li.querySelector('.cm-06__lp').dataset.base,10);
      li.querySelector('.cm-06__lp').textContent = '$' + (base*q);
      sum += base*q;
    });
    total.textContent = '$' + sum;
    var pct = Math.min(100, sum/THRESHOLD*100);
    bar.style.width = pct + '%';
    var remain = Math.max(0, THRESHOLD - sum);
    left.textContent = '$' + remain;
    root.querySelector('.cm-06__bar').setAttribute('aria-valuenow', sum);
  }
  root.querySelectorAll('.cm-06__qty button').forEach(function(b){
    b.addEventListener('click', function(){
      var span = b.parentNode.querySelector('span');
      var v = Math.max(1, parseInt(span.textContent,10) + parseInt(b.dataset.d,10));
      span.textContent = v; recalc();
    });
  });
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-06__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
