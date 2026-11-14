---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-shopping-cart-item-count-badge/"
title: "CSS Shopping Cart Item Count Badge"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two add-to-cart moments worth shipping: a fly-to-cart animation where a dot arcs from the product button into the cart along a JS-built offset-path (the…"
has_js: "true"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shopping Cart Item Count Badge
Source: https://codefronts.com/snippets/css-notifications/css-shopping-cart-item-count-badge/

Two add-to-cart moments worth shipping: a fly-to-cart animation where a dot arcs from the product button into the cart along a JS-built offset-path (the badge pops only when the dot lands), and an odometer badge whose digits roll vertically on a translated strip — the counter equivalent of a mechanical split-flap.
## HTML
```html
<div class="ntf-12-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-12a" aria-label="Add to cart with flying dot and badge count">
  <div class="ntf-12a__shop" id="ntf-12a-shop">
    <header class="ntf-12a__bar">
      <span class="ntf-12a__logo">atelier</span>
      <button class="ntf-12a__cart" id="ntf-12a-cart" type="button" aria-label="Cart, 0 items">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/></svg>
        <span class="ntf-12a__badge is-zero" id="ntf-12a-badge" aria-hidden="true">0</span>
      </button>
    </header>
    <div class="ntf-12a__grid">
      <article class="ntf-12a__prod"><span class="ntf-12a__ph" style="--c1:oklch(0.85 0.07 60);--c2:oklch(0.7 0.1 40)" aria-hidden="true"></span><b>Clay mug</b><small>$24</small><button class="ntf-12a__add" type="button">Add to cart</button></article>
      <article class="ntf-12a__prod"><span class="ntf-12a__ph" style="--c1:oklch(0.82 0.06 250);--c2:oklch(0.6 0.1 260)" aria-hidden="true"></span><b>Linen throw</b><small>$58</small><button class="ntf-12a__add" type="button">Add to cart</button></article>
    </div>
    <p class="ntf-12a__live" id="ntf-12a-live" role="status" aria-live="polite"></p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<section class="ntf-12b" aria-label="Cart badge with rolling odometer digits">
  <div class="ntf-12b__panel">
    <div class="ntf-12b__cartrow">
      <span class="ntf-12b__carticon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/></svg></span>
      <span class="ntf-12b__odo" aria-hidden="true"><span class="ntf-12b__strip" id="ntf-12b-strip"><i>0</i><i>1</i><i>2</i><i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i></span></span>
      <span class="ntf-12b__lbl" id="ntf-12b-lbl" role="status" aria-live="polite">0 items</span>
    </div>
    <div class="ntf-12b__row">
      <button class="ntf-12b__btn" id="ntf-12b-less" type="button" aria-label="Remove one">&#8722;</button>
      <button class="ntf-12b__btn ntf-12b__btn--add" id="ntf-12b-more" type="button">Add item</button>
    </div>
    <p class="ntf-12b__cap">The badge is a 1em window over a strip of digits — changing the count translates the strip by <b>count × -1em</b> with a spring.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-12-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-12-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-12a,
.ntf-12a *,
.ntf-12a *::before,
.ntf-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-12a {
  --ink: #232019;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f7f3ea,#efe7d7);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-12a__shop {
  position: relative;
  width: min(430px,100%);
}

.ntf-12a__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  border-radius: 16px;
  background: #fffdf8;
  border: 1px solid rgba(35,32,25,.1);
  box-shadow: 0 18px 40px -24px rgba(35,32,25,.45);
}

.ntf-12a__logo {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--ink);
}

.ntf-12a__cart {
  position: relative;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 12px;
  color: var(--ink);
  background: rgba(35,32,25,.06);
  cursor: pointer;
  transition: background .15s;
}

.ntf-12a__cart:hover {
  background: rgba(35,32,25,.12);
}

.ntf-12a__cart svg {
  width: 20px;
  height: 20px;
}

.ntf-12a__cart.is-hit {
  animation: ntf-12a-hit .3s cubic-bezier(.22,1.6,.36,1);
}

@keyframes ntf-12a-hit {
  40% {
    scale: 1.12;
  }
}

.ntf-12a__badge {
  position: absolute;
  top: -6px;
  inset-inline-end: -6px;
  min-inline-size: 19px;
  block-size: 19px;
  display: grid;
  place-items: center;
  padding-inline: 5px;
  border-radius: 999px;
  font-size: 10.5px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: #fffdf8;
  background: oklch(0.55 0.15 40);
  border: 2px solid #fffdf8;
  transition: scale .25s cubic-bezier(.22,1.4,.36,1);
}

.ntf-12a__badge.is-zero {
  scale: 0;
}

.ntf-12a__grid {
  margin-top: 16px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.ntf-12a__prod {
  display: grid;
  gap: 4px;
  padding: 14px;
  border-radius: 16px;
  background: #fffdf8;
  border: 1px solid rgba(35,32,25,.1);
}

.ntf-12a__ph {
  height: 88px;
  border-radius: 11px;
  background: radial-gradient(120% 130% at 30% 20%,var(--c1),var(--c2));
}

.ntf-12a__prod b {
  margin-top: 6px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--ink);
}

.ntf-12a__prod small {
  font-size: 12px;
  color: rgba(35,32,25,.55);
}

.ntf-12a__add {
  margin-top: 8px;
  padding: 10px;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: #fffdf8;
  background: var(--ink);
  border: 0;
  border-radius: 10px;
  cursor: pointer;
  transition: background .2s,scale .12s;
}

.ntf-12a__add:hover {
  background: #3a362c;
}

.ntf-12a__add:active {
  scale: .96;
}

.ntf-12a__flyer {
  position: absolute;
  left: 0;
  top: 0;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: oklch(0.55 0.15 40);
  box-shadow: 0 4px 10px -2px oklch(0.55 0.15 40 / .6);
  pointer-events: none;
  offset-rotate: 0deg;
  animation: ntf-12a-fly .7s cubic-bezier(.3,0,.8,.4) forwards;
}

@keyframes ntf-12a-fly {
  to {
    offset-distance: 100%;
    scale: .55;
  }
}

.ntf-12a__flyer--fallback {
  animation: ntf-12a-fade .35s ease forwards;
}

@keyframes ntf-12a-fade {
  to {
    opacity: 0;
    scale: .4;
  }
}

.ntf-12a__live {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-12a__flyer {
    animation: ntf-12a-fade .01s forwards;
  }

  .ntf-12a__cart.is-hit {
    animation: none;
  }
}

.ntf-12b,
.ntf-12b *,
.ntf-12b *::before,
.ntf-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-12b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#171c28,#0c0f16);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-12b__panel {
  width: min(380px,100%);
  padding: 28px;
  border-radius: 20px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(165,190,230,.16);
  box-shadow: 0 30px 70px -40px rgba(0,0,0,.9);
  display: grid;
  gap: 20px;
}

.ntf-12b__cartrow {
  display: flex;
  align-items: center;
  gap: 14px;
}

.ntf-12b__carticon {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border-radius: 14px;
  color: #e8eefc;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(165,190,230,.18);
}

.ntf-12b__carticon svg {
  width: 22px;
  height: 22px;
}

.ntf-12b__odo {
  display: block;
  height: 1em;
  overflow: hidden;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 30px;
  font-weight: 700;
  line-height: 1;
  color: oklch(0.8 0.14 60);
  background: oklch(0.8 0.14 60 / .1);
  border: 1px solid oklch(0.8 0.14 60 / .3);
  padding: 8px 12px;
  border-radius: 12px;
  height: auto;
}

.ntf-12b__odo {
  height: calc(1em + 16px);
}

.ntf-12b__strip {
  display: block;
  height: 1em;
  line-height: 1;
  transition: translate .55s linear(0,0.35 8%,0.78 17%,1.05 26%,1.14 32%,1.06 42%,0.98 52%,1.01 66%,1);
}

.ntf-12b__strip i {
  display: block;
  height: 1em;
  font-style: normal;
  text-align: center;
}

.ntf-12b__lbl {
  margin-left: auto;
  font-size: 13px;
  color: rgba(212,224,246,.6);
}

.ntf-12b__row {
  display: flex;
  gap: 10px;
}

.ntf-12b__btn {
  flex: none;
  width: 48px;
  padding: 12px 0;
  font: inherit;
  font-size: 18px;
  font-weight: 600;
  color: #e8eefc;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(165,190,230,.2);
  border-radius: 11px;
  cursor: pointer;
  transition: background .15s,scale .12s;
}

.ntf-12b__btn--add {
  flex: 1;
  width: auto;
  font-size: 14px;
  color: #0c0f16;
  background: oklch(0.8 0.14 60);
  border: 0;
}

.ntf-12b__btn:hover {
  background: rgba(255,255,255,.13);
}

.ntf-12b__btn--add:hover {
  background: oklch(0.85 0.14 60);
}

.ntf-12b__btn:active {
  scale: .95;
}

.ntf-12b__cap {
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(212,224,246,.45);
  text-wrap: pretty;
}

.ntf-12b__cap b {
  color: rgba(232,238,252,.85);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-12b__strip {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
(function(){
  var shop=document.getElementById('ntf-12a-shop'); if(!shop) return;
  var cart=document.getElementById('ntf-12a-cart'),badge=document.getElementById('ntf-12a-badge'),
      live=document.getElementById('ntf-12a-live'),count=0,
      arcs=CSS.supports('offset-path','path("M 0 0 L 1 1")');
  shop.querySelectorAll('.ntf-12a__add').forEach(function(btn){
    btn.addEventListener('click',function(){
      var s=shop.getBoundingClientRect(),a=btn.getBoundingClientRect(),b=cart.getBoundingClientRect();
      var x0=a.left-s.left+a.width/2,y0=a.top-s.top+a.height/2,
          x1=b.left-s.left+b.width/2,y1=b.top-s.top+b.height/2;
      var flyer=document.createElement('i');
      if(arcs){
        flyer.className='ntf-12a__flyer';
        flyer.style.offsetPath='path("M '+x0+' '+y0+' Q '+((x0+x1)/2)+' '+(Math.min(y0,y1)-90)+' '+x1+' '+y1+'")';
      }else{
        flyer.className='ntf-12a__flyer ntf-12a__flyer--fallback';
        flyer.style.translate=x1+'px '+y1+'px';
      }
      flyer.addEventListener('animationend',function(){
        flyer.remove(); count++;
        badge.textContent=String(count); badge.classList.remove('is-zero');
        cart.classList.remove('is-hit'); void 0; cart.classList.add('is-hit');
        cart.setAttribute('aria-label','Cart, '+count+(count===1?' item':' items'));
        live.textContent='Added to cart. '+count+(count===1?' item':' items')+' total.';
      });
      cart.addEventListener('animationend',function(){ cart.classList.remove('is-hit'); });
      shop.appendChild(flyer);
    });
  });
})();

(function(){
  var strip=document.getElementById('ntf-12b-strip'); if(!strip) return;
  var lbl=document.getElementById('ntf-12b-lbl'),count=0;
  function render(){
    strip.style.translate='0 '+(count*-1)+'em';   /* 1em per digit — font-size agnostic */
    lbl.textContent=count+(count===1?' item':' items');
  }
  document.getElementById('ntf-12b-more').addEventListener('click',function(){ if(count<9){count++;render();} });
  document.getElementById('ntf-12b-less').addEventListener('click',function(){ if(count>0){count--;render();} });
})();
```
