---
source: "codefronts"
url: "https://codefronts.com/components/css-modals/quick-view-product-details/"
title: "Quick View Product Details"
section: "components"
category: "css-modals"
category_name: "CSS Modals"
description: "A two-column product quick-view that pops from a grid — gallery, price, star rating, colour/size variant chips, a quantity stepper and Add to Bag — so…"
has_js: "true"
---

Here's a working CSS Modal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Quick View Product Details
Source: https://codefronts.com/components/css-modals/quick-view-product-details/

A two-column product quick-view that pops from a grid — gallery, price, star rating, colour/size variant chips, a quantity stepper and Add to Bag — so shoppers evaluate an item without a page reload. Collapses to one column on mobile.
## HTML
```html
<div class="cm-05">
  <div class="cm-05__grid-demo">
    <button class="cm-05__open" type="button">Quick view</button>
    <span class="cm-05__hint">(product-grid trigger)</span>
  </div>

  <dialog class="cm-05__dlg" aria-labelledby="cm-05-title">
    <div class="cm-05__card">
      <button class="cm-05__x" type="button" aria-label="Close">&times;</button>
      <div class="cm-05__media">
        <div class="cm-05__ph" data-label="product shot"></div>
      </div>
      <div class="cm-05__info">
        <p class="cm-05__brand">FIELD &amp; FORGE</p>
        <h2 id="cm-05-title" class="cm-05__title">Merino Trail Overshirt</h2>
        <div class="cm-05__rate" aria-label="Rated 4.5 of 5"><span>★★★★</span><span class="cm-05__half">★</span> <b>4.5</b> · 218 reviews</div>
        <div class="cm-05__price">$148<small>USD</small></div>
        <fieldset class="cm-05__opt"><legend>Colour</legend>
          <label class="cm-05__sw" style="--sw:#3a4a3f"><input type="radio" name="cm-05-c" aria-label="Forest" checked></label>
          <label class="cm-05__sw" style="--sw:#5a3f2f"><input type="radio" name="cm-05-c" aria-label="Rust"></label>
          <label class="cm-05__sw" style="--sw:#2c3440"><input type="radio" name="cm-05-c" aria-label="Slate"></label>
        </fieldset>
        <fieldset class="cm-05__opt"><legend>Size</legend>
          <label class="cm-05__size"><input type="radio" name="cm-05-s" aria-label="Small">S</label>
          <label class="cm-05__size"><input type="radio" name="cm-05-s" aria-label="Medium" checked>M</label>
          <label class="cm-05__size"><input type="radio" name="cm-05-s" aria-label="Large">L</label>
          <label class="cm-05__size"><input type="radio" name="cm-05-s" aria-label="Extra large">XL</label>
        </fieldset>
        <div class="cm-05__buy">
          <div class="cm-05__qty">
            <button type="button" class="cm-05__step" data-d="-1" aria-label="Decrease quantity">−</button>
            <span class="cm-05__n" id="cm-05-n" aria-live="polite">1</span>
            <button type="button" class="cm-05__step" data-d="1" aria-label="Increase quantity">+</button>
          </div>
          <button type="button" class="cm-05__add">Add to bag</button>
        </div>
      </div>
    </div>
  </dialog>
</div>
```
## CSS
```css
.cm-05,
.cm-05 *,
.cm-05 *::before,
.cm-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cm-05 {
  --accent: oklch(0.72 0.15 150);
  font-family: system-ui,'Segoe UI',sans-serif;
  min-height: 100dvh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(120% 120% at 50% 0%,#101512,#080a09);
}

.cm-05__grid-demo {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.cm-05__open {
  cursor: pointer;
  padding: 13px 26px;
  border-radius: 11px;
  color: #eafaf1;
  font: 600 15px system-ui;
  border: 1px solid color-mix(in oklch,var(--accent) 45%,#233029);
  background: color-mix(in oklch,var(--accent) 14%,#0e1512);
  transition: background .2s,border-color .2s;
}

.cm-05__open:hover {
  border-color: var(--accent);
  background: color-mix(in oklch,var(--accent) 22%,#0e1512);
}

.cm-05__open:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-05__hint {
  font: 12px ui-monospace,monospace;
  letter-spacing: .14em;
  color: #5a6a60;
}

.cm-05__dlg {
  margin: auto;
  width: min(720px,94vw);
  padding: 0;
  border: none;
  border-radius: 20px;
  color: #e6efe9;
  background: linear-gradient(180deg,#141a17,#0f1412);
  box-shadow: 0 40px 90px -30px #000,0 0 0 1px #223029;
  max-block-size: 90dvh;
  overflow: auto;
  opacity: 0;
  transform: scale(.97);
  transition: opacity .28s,transform .28s,overlay .28s allow-discrete,display .28s allow-discrete;
}

.cm-05__dlg[open] {
  opacity: 1;
  transform: none;
}

@starting-style {
  .cm-05__dlg[open] {
    opacity: 0;
    transform: scale(.97);
  }
}

.cm-05__dlg::backdrop {
  background: rgba(4,7,6,0);
  backdrop-filter: blur(0);
  transition: background .3s,backdrop-filter .3s,overlay .3s allow-discrete,display .3s allow-discrete;
}

.cm-05__dlg[open]::backdrop {
  background: rgba(4,7,6,.6);
  backdrop-filter: blur(5px);
}

@starting-style {
  .cm-05__dlg[open]::backdrop {
    background: rgba(4,7,6,0);
    backdrop-filter: blur(0);
  }
}

.cm-05__card {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.cm-05__x {
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 3;
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 8px;
  background: rgba(10,14,12,.7);
  color: #c9d6cf;
  font-size: 22px;
  cursor: pointer;
}

.cm-05__x:hover {
  background: #1c2620;
  color: #fff;
}

.cm-05__x:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-05__media {
  background: #0c110e;
  padding: 18px;
}

.cm-05__ph {
  width: 100%;
  height: 100%;
  min-height: 280px;
  border-radius: 14px;
  position: relative;
  background: repeating-linear-gradient(135deg,#18211c 0 12px,#141b17 12px 24px);
  border: 1px solid #26332b;
}

.cm-05__ph::after {
  content: attr(data-label);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font: 12px ui-monospace,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #4d5c53;
}

.cm-05__info {
  padding: 30px 30px 26px;
}

.cm-05__brand {
  font-size: 11px;
  letter-spacing: .2em;
  color: var(--accent);
  margin-bottom: 8px;
}

.cm-05__title {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: #f0f7f3;
  margin-bottom: 10px;
}

.cm-05__rate {
  font-size: 12.5px;
  color: #93a49a;
  margin-bottom: 16px;
}

.cm-05__rate span {
  color: var(--accent);
  letter-spacing: 1px;
}

.cm-05__rate .cm-05__half {
  opacity: .5;
}

.cm-05__rate b {
  color: #dbe6df;
}

.cm-05__price {
  font-size: 26px;
  font-weight: 800;
  color: #fff;
  margin-bottom: 22px;
}

.cm-05__price small {
  font-size: 12px;
  font-weight: 500;
  color: #8a9a90;
  margin-left: 6px;
}

.cm-05__opt {
  border: none;
  margin-bottom: 18px;
}

.cm-05__opt legend {
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #8a9a90;
  margin-bottom: 10px;
}

.cm-05__opt {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.cm-05__opt legend {
  flex-basis: 100%;
}

.cm-05__sw {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--sw);
  cursor: pointer;
  position: relative;
  box-shadow: inset 0 0 0 2px #0f1412,0 0 0 1px #33413a;
}

.cm-05__sw input {
  position: absolute;
  opacity: 0;
  inset: 0;
  cursor: pointer;
}

.cm-05__sw:has(:checked) {
  box-shadow: inset 0 0 0 2px #0f1412,0 0 0 2px var(--accent);
}

.cm-05__sw:has(:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cm-05__size {
  min-width: 44px;
  height: 40px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  cursor: pointer;
  font: 600 14px system-ui;
  color: #b7c6bd;
  border: 1px solid #2c3a32;
  background: #0f1512;
  transition: all .15s;
}

.cm-05__size input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.cm-05__size:has(:checked) {
  border-color: var(--accent);
  color: #fff;
  background: color-mix(in oklch,var(--accent) 20%,#0f1512);
}

.cm-05__size:has(:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cm-05__buy {
  display: flex;
  gap: 12px;
  margin-top: 8px;
}

.cm-05__qty {
  display: flex;
  align-items: center;
  border: 1px solid #2c3a32;
  border-radius: 11px;
  overflow: hidden;
}

.cm-05__step {
  width: 42px;
  height: 48px;
  border: none;
  background: #0f1512;
  color: #cde0d6;
  font-size: 20px;
  cursor: pointer;
  transition: background .15s;
}

.cm-05__step:hover {
  background: #18211c;
}

.cm-05__step:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cm-05__n {
  min-width: 40px;
  text-align: center;
  font: 600 16px system-ui;
  color: #fff;
}

.cm-05__add {
  flex: 1;
  border: none;
  border-radius: 11px;
  background: var(--accent);
  color: #04140b;
  font: 700 15px system-ui;
  cursor: pointer;
  transition: filter .2s,transform .1s;
}

.cm-05__add:hover {
  filter: brightness(1.08);
}

.cm-05__add:active {
  transform: translateY(1px);
}

.cm-05__add:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (max-width: 560px) {
  .cm-05__card {
    grid-template-columns: 1fr;
  }

  .cm-05__ph {
    min-height: 200px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cm-05__dlg,
    .cm-05__dlg::backdrop {
    transition-duration: .001s;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.querySelector('.cm-05');
  var dlg = root.querySelector('.cm-05__dlg');
  var n = root.querySelector('#cm-05-n');
  root.querySelector('.cm-05__open').addEventListener('click', function(){ dlg.showModal(); });
  root.querySelector('.cm-05__x').addEventListener('click', function(){ dlg.close(); });
  root.querySelectorAll('.cm-05__step').forEach(function(b){
    b.addEventListener('click', function(){
      var v = Math.max(1, parseInt(n.textContent,10) + parseInt(b.dataset.d,10));
      n.textContent = v;
    });
  });
  root.querySelector('.cm-05__add').addEventListener('click', function(){
    this.textContent = 'Added ✓';
    var self = this; setTimeout(function(){ self.textContent = 'Add to bag'; }, 1400);
  });
  dlg.addEventListener('click', function(e){
    var c = dlg.querySelector('.cm-05__card').getBoundingClientRect();
    if(e.clientX < c.left || e.clientX > c.right || e.clientY < c.top || e.clientY > c.bottom) dlg.close();
  });
})();
```
