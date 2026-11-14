---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/food-delivery-card-with-quantity/"
title: "Food-Delivery Card with Quantity"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A restaurant/delivery-app dish card with dietary badges (Vegan, GF), a prep-time and rating line, dynamic pricing and a +/− quantity stepper that updates a…"
has_js: "true"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Food-Delivery Card with Quantity
Source: https://codefronts.com/components/css-product-cards/food-delivery-card-with-quantity/

A restaurant/delivery-app dish card with dietary badges (Vegan, GF), a prep-time and rating line, dynamic pricing and a +/− quantity stepper that updates a running total. The food-delivery layout devs building menu UIs search for.
## HTML
```html
<article class="cpc-16" id="cpc-16" data-price="12.5">
  <div class="cpc-16__card">
    <div class="cpc-16__img" role="img" aria-label="Dish photo: Miso ramen bowl"><span>dish shot</span></div>
    <div class="cpc-16__body">
      <div class="cpc-16__head">
        <h3 class="cpc-16__name">Miso Ramen Bowl</h3>
        <div class="cpc-16__badges"><span class="cpc-16__b cpc-16__b--v">Vegan</span><span class="cpc-16__b cpc-16__b--g">GF</span></div>
      </div>
      <p class="cpc-16__desc">Rich miso broth, corn, spring onion, marinated tofu.</p>
      <p class="cpc-16__meta"><span aria-hidden="true">★</span> 4.7 · 20–30 min · $2.99 delivery</p>
      <div class="cpc-16__foot">
        <div class="cpc-16__stepper" role="group" aria-label="Quantity">
          <button type="button" id="cpc-16-dec" aria-label="Decrease quantity">−</button>
          <span class="cpc-16__qty" id="cpc-16-qty">1</span>
          <button type="button" id="cpc-16-inc" aria-label="Increase quantity">+</button>
        </div>
        <button class="cpc-16__add" type="button" id="cpc-16-add" aria-live="polite">Add · $12.50</button>
      </div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-16,
.cpc-16 *,
.cpc-16 *::before,
.cpc-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-16 ::selection {
  background: oklch(0.65 0.18 40);
  color: #fff;
}

.cpc-16 {
  --accent: oklch(0.62 0.19 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f6f3ee;
}

.cpc-16__card {
  width: 340px;
  border-radius: 18px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 16px 40px -22px rgba(60,40,20,.4);
}

.cpc-16__img {
  aspect-ratio: 16/10;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#f0e4d4,#e6d2b8),repeating-linear-gradient(45deg,rgba(255,255,255,.4) 0 14px,transparent 14px 28px);
}

.cpc-16__img {
  background-image: url("https://images.unsplash.com/photo-1416879595882-3373a0480b5b?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-16__img span {
  display: none;
}

.cpc-16__body {
  padding: 18px 20px 20px;
}

.cpc-16__head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.cpc-16__name {
  font-size: 18px;
  font-weight: 700;
  color: #2a1e12;
}

.cpc-16__badges {
  display: flex;
  gap: 6px;
  flex-shrink: 0;
}

.cpc-16__b {
  padding: 4px 9px;
  border-radius: 999px;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.cpc-16__b--v {
  background: oklch(0.92 0.06 150);
  color: oklch(0.42 0.12 150);
}

.cpc-16__b--g {
  background: oklch(0.93 0.05 250);
  color: oklch(0.44 0.12 255);
}

.cpc-16__desc {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.5;
  color: #6b5d4d;
}

.cpc-16__meta {
  margin-top: 10px;
  font-size: 13px;
  color: #8a7a66;
}

.cpc-16__meta span {
  color: oklch(0.72 0.16 70);
}

.cpc-16__foot {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.cpc-16__stepper {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  border: 1px solid #e4dccf;
  border-radius: 12px;
  overflow: hidden;
}

.cpc-16__stepper button {
  width: 40px;
  height: 44px;
  border: none;
  cursor: pointer;
  background: #faf7f2;
  color: #2a1e12;
  font-size: 20px;
  font-weight: 600;
  line-height: 1;
}

.cpc-16__stepper button:hover {
  background: #f0e8db;
}

.cpc-16__stepper button:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.cpc-16__stepper button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.cpc-16__qty {
  min-width: 34px;
  text-align: center;
  font-size: 15px;
  font-weight: 700;
  color: #2a1e12;
}

.cpc-16__add {
  flex: 1;
  height: 46px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
}

.cpc-16__add:hover {
  filter: brightness(1.05);
}

.cpc-16__add:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('cpc-16');
  if(!root) return;
  var unit = parseFloat(root.getAttribute('data-price')) || 0;
  var qtyEl = document.getElementById('cpc-16-qty');
  var addEl = document.getElementById('cpc-16-add');
  var inc = document.getElementById('cpc-16-inc');
  var dec = document.getElementById('cpc-16-dec');
  var qty = 1;
  function render(){
    qtyEl.textContent = qty;
    addEl.textContent = 'Add · $' + (unit * qty).toFixed(2);
    dec.disabled = qty <= 1;
  }
  inc.addEventListener('click', function(){ if(qty < 20){ qty++; render(); }});
  dec.addEventListener('click', function(){ if(qty > 1){ qty--; render(); }});
  render();
})();
```
