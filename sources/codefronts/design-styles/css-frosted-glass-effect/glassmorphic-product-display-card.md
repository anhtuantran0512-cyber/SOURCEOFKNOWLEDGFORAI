---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphic-product-display-card/"
title: "Glassmorphic Product Display Card"
section: "design-styles"
category: "css-frosted-glass-effect"
category_name: "CSS Frosted Glass Effects"
description: "A premium e-commerce product card with a CSS-art headphone product illustration that floats on a gradient stage, a frosted glass bottom overlay, badge chips,…"
has_js: "true"
---

Here's a working CSS Frosted Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Product Display Card
Source: https://codefronts.com/design-styles/css-frosted-glass-effect/glassmorphic-product-display-card/

A premium e-commerce product card with a CSS-art headphone product illustration that floats on a gradient stage, a frosted glass bottom overlay, badge chips, star rating, quantity counter, wishlist heart, and multi-state add-to-cart button.
## HTML
```html
<div class="fg-10">
  <div class="fg-10__bg" aria-hidden="true">
    <div class="fg-10__glow fg-10__glow--1"></div>
    <div class="fg-10__glow fg-10__glow--2"></div>
  </div>
  <div class="fg-10__card">
    <div class="fg-10__stage">
      <div class="fg-10__stage-tags">
        <span class="fg-10__badge fg-10__badge--new">New Drop</span>
        <span class="fg-10__badge fg-10__badge--ship">Free Shipping</span>
      </div>
      <button class="fg-10__wish" id="fg-10-wish" aria-label="Add to wishlist">
        <svg class="fg-10__wish-e" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
        <svg class="fg-10__wish-f" width="19" height="19" viewBox="0 0 24 24" fill="#f87171" stroke="#f87171" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
      </button>
      <div class="fg-10__art" aria-hidden="true">
        <div class="fg-10__art-glow"></div>
        <div class="fg-10__art-prod">
          <svg viewBox="0 0 160 140" width="160" height="140" fill="none">
            <path d="M80 14C40 14 10 44 10 80L10 102L32 102L32 80C32 56 54 36 80 36C106 36 128 56 128 80L128 102L150 102L150 80C150 44 120 14 80 14Z" fill="rgba(139,92,246,.12)" stroke="rgba(139,92,246,.3)" stroke-width="1.5"/>
            <rect x="4" y="88" width="26" height="32" rx="9" fill="rgba(139,92,246,.55)" stroke="rgba(167,139,250,.7)" stroke-width="1.2"/>
            <rect x="130" y="88" width="26" height="32" rx="9" fill="rgba(139,92,246,.55)" stroke="rgba(167,139,250,.7)" stroke-width="1.2"/>
            <circle cx="80" cy="80" r="24" fill="rgba(139,92,246,.18)" stroke="rgba(139,92,246,.4)" stroke-width="1.5"/>
            <circle cx="80" cy="80" r="13" fill="rgba(139,92,246,.38)" stroke="rgba(167,139,250,.6)" stroke-width="1.2"/>
            <circle cx="80" cy="80" r="5" fill="rgba(255,255,255,.6)"/>
            <circle cx="80" cy="80" r="2" fill="rgba(255,255,255,.9)"/>
          </svg>
        </div>
      </div>
      <div class="fg-10__overlay">
        <div class="fg-10__stars" aria-label="Rating 4.8 out of 5">
          <svg width="68" height="12" viewBox="0 0 68 12" fill="#f59e0b">
            <path d="M6 .5l1.4 4.2H12L8.4 7.4l1.4 4.2L6 9.2 2.2 11.6l1.4-4.2L0 4.7h4.6z"/>
            <path d="M20 .5l1.4 4.2H26L22.4 7.4l1.4 4.2L20 9.2l-3.8 2.4 1.4-4.2L14 4.7h4.6z"/>
            <path d="M34 .5l1.4 4.2H40L36.4 7.4l1.4 4.2L34 9.2l-3.8 2.4 1.4-4.2L28 4.7h4.6z"/>
            <path d="M48 .5l1.4 4.2H54L50.4 7.4l1.4 4.2L48 9.2l-3.8 2.4 1.4-4.2L42 4.7h4.6z"/>
            <path d="M62 .5l1.4 4.2H68L64.4 7.4l1.4 4.2L62 9.2l-3.8 2.4 1.4-4.2L56 4.7h4.6z" opacity=".3"/>
          </svg>
          <span>4.8 <small>(2.4K reviews)</small></span>
        </div>
      </div>
    </div>
    <div class="fg-10__body">
      <h2 class="fg-10__name">Quantum Arc Pro</h2>
      <p class="fg-10__desc">Spatial audio &amp; AI noise cancellation. 40-hour battery, feather-light titanium frame.</p>
      <div class="fg-10__price-row">
        <span class="fg-10__price">$299<sup>.00</sup></span>
        <span class="fg-10__price-old">$399.00</span>
        <span class="fg-10__save">Save 25%</span>
      </div>
      <div class="fg-10__buy-row">
        <div class="fg-10__qty" role="group" aria-label="Quantity">
          <button class="fg-10__qty-btn" id="fg-10-minus" aria-label="Decrease quantity">&#8722;</button>
          <span class="fg-10__qty-n" id="fg-10-qty" aria-live="polite">1</span>
          <button class="fg-10__qty-btn" id="fg-10-plus" aria-label="Increase quantity">+</button>
        </div>
        <button class="fg-10__cart" id="fg-10-cart">Add to Cart</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fg-10,
.fg-10 *,
.fg-10 *::before,
.fg-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fg-10 ::selection {
  background: rgba(139,92,246,.5);
  color: #fff;
}

.fg-10 {
  --c-bg: #080812;
  --c-a: #8b5cf6;
  --c-a2: #3b82f6;
  --c-glass: rgba(255,255,255,.06);
  --c-border: rgba(255,255,255,.1);
  --c-text: #eef0ff;
  --c-muted: rgba(238,240,255,.55);
  --t: .25s ease;
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--c-bg);
  position: relative;
  overflow: hidden;
  padding: 40px 20px;
}

.fg-10__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}

.fg-10__glow {
  position: absolute;
  border-radius: 50%;
}

.fg-10__glow--1 {
  width: 420px;
  height: 420px;
  background: radial-gradient(circle,rgba(139,92,246,.28),transparent 70%);
  top: -100px;
  left: -80px;
  animation: fg-10-g1 20s ease-in-out infinite alternate;
}

.fg-10__glow--2 {
  width: 360px;
  height: 360px;
  background: radial-gradient(circle,rgba(59,130,246,.22),transparent 70%);
  bottom: -80px;
  right: -80px;
  animation: fg-10-g2 25s ease-in-out infinite alternate;
}

@keyframes fg-10-g1 {
  to {
    transform: translate(60px,80px) scale(1.15);
  }
}

@keyframes fg-10-g2 {
  to {
    transform: translate(-70px,-60px) scale(1.2);
  }
}

.fg-10__card {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 318px;
  background: var(--c-glass);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  border: 1px solid var(--c-border);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 48px rgba(0,0,0,.55);
  transition: transform .3s,box-shadow .3s;
}

.fg-10__card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 64px rgba(0,0,0,.65);
}

.fg-10__stage {
  position: relative;
  height: 220px;
  background: linear-gradient(135deg,#0f0c24,#1a1060 40%,#2d1b6e 70%,#1a1060);
  overflow: hidden;
}

.fg-10__stage-tags {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  gap: 6px;
  z-index: 3;
}

.fg-10__badge {
  font-size: 10px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 20px;
  letter-spacing: .3px;
}

.fg-10__badge--new {
  background: rgba(139,92,246,.8);
  color: #fff;
  border: 1px solid rgba(139,92,246,.9);
}

.fg-10__badge--ship {
  background: rgba(16,185,129,.14);
  color: #34d399;
  border: 1px solid rgba(16,185,129,.3);
}

.fg-10__wish {
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 3;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.15);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,.7);
  transition: background var(--t),transform .15s;
}

.fg-10__wish:hover {
  background: rgba(255,255,255,.2);
  transform: scale(1.1);
}

.fg-10__wish-f {
  display: none;
}

.fg-10__art {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.fg-10__art-glow {
  position: absolute;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(139,92,246,.28),transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
}

.fg-10__art-prod {
  position: relative;
  z-index: 1;
  animation: fg-10-float 4s ease-in-out infinite;
}

@keyframes fg-10-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-9px);
  }
}

.fg-10__overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 8px 14px 10px;
  background: rgba(8,8,18,.5);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 2;
}

.fg-10__stars {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: rgba(255,255,255,.85);
  font-weight: 600;
}

.fg-10__stars small {
  font-size: 11px;
  font-weight: 400;
  color: var(--c-muted);
}

.fg-10__body {
  padding: 18px 18px 20px;
}

.fg-10__name {
  font-size: 18px;
  font-weight: 800;
  color: var(--c-text);
  letter-spacing: -.3px;
  margin-bottom: 5px;
}

.fg-10__desc {
  font-size: 12px;
  color: var(--c-muted);
  line-height: 1.55;
  margin-bottom: 14px;
}

.fg-10__price-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 16px;
}

.fg-10__price {
  font-size: 28px;
  font-weight: 800;
  color: var(--c-text);
}

.fg-10__price sup {
  font-size: 13px;
  vertical-align: super;
}

.fg-10__price-old {
  font-size: 13px;
  color: var(--c-muted);
  text-decoration: line-through;
}

.fg-10__save {
  font-size: 11px;
  font-weight: 700;
  color: #34d399;
  background: rgba(16,185,129,.12);
  border: 1px solid rgba(16,185,129,.25);
  padding: 2px 8px;
  border-radius: 20px;
  margin-left: auto;
}

.fg-10__buy-row {
  display: flex;
  gap: 10px;
  align-items: center;
}

.fg-10__qty {
  display: flex;
  align-items: center;
  background: rgba(255,255,255,.06);
  border: 1px solid var(--c-border);
  border-radius: 10px;
  overflow: hidden;
}

.fg-10__qty-btn {
  width: 34px;
  height: 38px;
  border: none;
  background: transparent;
  color: var(--c-text);
  font-size: 18px;
  cursor: pointer;
  transition: background var(--t);
}

.fg-10__qty-btn:hover {
  background: rgba(255,255,255,.1);
}

.fg-10__qty-n {
  width: 28px;
  text-align: center;
  font-size: 14px;
  font-weight: 700;
  color: var(--c-text);
}

.fg-10__cart {
  flex: 1;
  height: 38px;
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg,var(--c-a),var(--c-a2));
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: transform .15s,box-shadow .2s,background .3s;
  box-shadow: 0 4px 18px rgba(139,92,246,.4);
}

.fg-10__cart:hover:not(.is-added) {
  transform: translateY(-1px);
  box-shadow: 0 6px 24px rgba(139,92,246,.55);
}

.fg-10__cart.is-added {
  background: linear-gradient(135deg,#10b981,#34d399);
  box-shadow: 0 4px 18px rgba(16,185,129,.4);
}

@media (prefers-reduced-motion: reduce) {
  .fg-10__glow,
    .fg-10__art-prod {
    animation: none;
  }

  .fg-10__card,
    .fg-10__cart,
    .fg-10__wish {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var r=document.querySelector('.fg-10');
  if(!r)return;
  var qty=1;
  var qEl=r.querySelector('#fg-10-qty');
  r.querySelector('#fg-10-minus').addEventListener('click',function(){if(qty>1){qty--;qEl.textContent=qty}});
  r.querySelector('#fg-10-plus').addEventListener('click',function(){if(qty<9){qty++;qEl.textContent=qty}});
  var cart=r.querySelector('#fg-10-cart');
  cart.addEventListener('click',function(){
    if(cart.classList.contains('is-added'))return;
    cart.classList.add('is-added');cart.textContent='Added ✓';
    setTimeout(function(){cart.classList.remove('is-added');cart.textContent='Add to Cart'},2000);
  });
  var wish=r.querySelector('#fg-10-wish');
  wish.addEventListener('click',function(){
    var on=wish.classList.toggle('is-wished');
    wish.querySelector('.fg-10__wish-e').style.display=on?'none':'block';
    wish.querySelector('.fg-10__wish-f').style.display=on?'block':'none';
  });
})();
```
