---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-shopping-cart-wiggle-on-item-add/"
title: "CSS Shopping Cart Wiggle on Item Add"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Add-to-cart with mass: a shop row where every add makes the cart wiggle and its badge bounce up a number, and a 'catch' variant where a dot physically arcs…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shopping Cart Wiggle on Item Add
Source: https://codefronts.com/motion/css-shake-animation/css-shopping-cart-wiggle-on-item-add/

Add-to-cart with mass: a shop row where every add makes the cart wiggle and its badge bounce up a number, and a 'catch' variant where a dot physically arcs from the button into the cart — which squashes on impact and wiggles it off. The item's arrival is the animation; no toast needed.
## HTML
```html
<div class="shk-16-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-16a" aria-label="Shop row where adding wiggles the cart">
  <div class="shk-16a__shop">
    <header class="shk-16a__top"><span class="shk-16a__logo">grove&nbsp;&amp;&nbsp;co.</span>
      <button class="shk-16a__cartbtn" id="shk-16a-cart" type="button" aria-label="Cart">
        <svg class="shk-16a__cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1.6"></circle><circle cx="19" cy="21" r="1.6"></circle><path d="M2.5 3h2l2.6 12.6a2 2 0 0 0 2 1.4h9.7a2 2 0 0 0 2-1.6L22 7H6"></path></svg>
        <span class="shk-16a__badge" id="shk-16a-badge">0</span>
      </button>
    </header>
    <article class="shk-16a__item">
      <img class="shk-16a__img" src="https://picsum.photos/id/1080/300/300" alt="Bowl of fresh strawberries" loading="lazy">
      <div class="shk-16a__info"><h2 class="shk-16a__name">Market strawberries</h2><p class="shk-16a__meta">500g punnet · organic</p><p class="shk-16a__price">$6.50</p></div>
      <button class="shk-16a__add" id="shk-16a-add" type="button">Add</button>
    </article>
    <p class="shk-16a__hint" aria-hidden="true">every Add re-wiggles the cart from its handle and bumps the badge</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-16b" aria-label="Item flies into the cart which squashes and wiggles">
  <div class="shk-16b__stage" id="shk-16b-stage">
    <button class="shk-16b__add" id="shk-16b-add" type="button"><span class="shk-16b__sw" aria-hidden="true"></span>Add keycap set · $36</button>
    <div class="shk-16b__cartzone">
      <div class="shk-16b__cartwrap" id="shk-16b-cartwrap">
        <svg class="shk-16b__cart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1.6"></circle><circle cx="19" cy="21" r="1.6"></circle><path d="M2.5 3h2l2.6 12.6a2 2 0 0 0 2 1.4h9.7a2 2 0 0 0 2-1.6L22 7H6"></path></svg>
        <span class="shk-16b__badge" id="shk-16b-badge">0</span>
      </div>
    </div>
  </div>
  <p class="shk-16b__hint" aria-hidden="true">linear X + eased Y = a parabola with zero math — the cart squashes exactly when the dot lands</p>
</section>
</div>
```
## CSS
```css
.shk-16-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-16-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-16a,
.shk-16a *,
.shk-16a *::before,
.shk-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-16a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f3f6f1,#e6ece2);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-16a__shop {
  width: min(430px,100%);
}

.shk-16a__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 4px 16px;
}

.shk-16a__logo {
  font-size: 17px;
  font-weight: 900;
  letter-spacing: -.02em;
  color: #22301e;
}

.shk-16a__cartbtn {
  position: relative;
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  border: 1.5px solid rgba(34,48,30,.2);
  border-radius: 13px;
  background: #fff;
  color: #22301e;
  cursor: pointer;
  transition: background .2s;
}

.shk-16a__cartbtn:hover {
  background: #f2f6ef;
}

.shk-16a__cart {
  width: 22px;
  height: 22px;
  transform-origin: 50% 10%;
  transform-box: fill-box;
}

.shk-16a__cartbtn.is-wiggling .shk-16a__cart {
  animation: shk-16a-wiggle .6s ease-in-out;
}

.shk-16a__badge {
  position: absolute;
  top: -7px;
  right: -7px;
  min-width: 20px;
  height: 20px;
  padding: 0 5px;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 800;
  color: #fff;
  background: oklch(0.55 0.16 145);
  border-radius: 999px;
  border: 2px solid #f3f6f1;
}

.shk-16a__cartbtn.is-wiggling .shk-16a__badge {
  animation: shk-16a-bump .45s cubic-bezier(.34,1.56,.64,1);
}

.shk-16a__item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  background: #fff;
  border: 1.5px solid rgba(34,48,30,.12);
  border-radius: 18px;
  box-shadow: 0 20px 45px -28px rgba(34,48,30,.5);
}

.shk-16a__img {
  width: 76px;
  height: 76px;
  border-radius: 12px;
  object-fit: cover;
}

.shk-16a__info {
  flex: 1;
}

.shk-16a__name {
  font-size: 16px;
  font-weight: 800;
  color: #22301e;
  letter-spacing: -.01em;
}

.shk-16a__meta {
  margin-top: 2px;
  font-size: 12px;
  color: rgba(34,48,30,.5);
}

.shk-16a__price {
  margin-top: 6px;
  font-size: 15px;
  font-weight: 900;
  color: #22301e;
}

.shk-16a__add {
  padding: 11px 22px;
  font: inherit;
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  background: #2c4526;
  border: 0;
  border-radius: 11px;
  cursor: pointer;
  transition: background .2s,scale .12s;
}

.shk-16a__add:hover {
  background: #3a5a32;
}

.shk-16a__add:active {
  scale: .94;
}

.shk-16a__hint {
  margin-top: 16px;
  text-align: center;
  font-size: 12px;
  color: rgba(34,48,30,.45);
}

@keyframes shk-16a-wiggle {
  12% {
    rotate: -11deg;
  }

  30% {
    rotate: 9deg;
  }

  48% {
    rotate: -6deg;
  }

  66% {
    rotate: 3deg;
  }

  84% {
    rotate: -1deg;
  }
}

@keyframes shk-16a-bump {
  35% {
    scale: 1.4;
    translate: 0 -3px;
  }

  70% {
    scale: .92;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-16a__cartbtn.is-wiggling .shk-16a__cart,
    .shk-16a__cartbtn.is-wiggling .shk-16a__badge {
    animation: none;
  }
}

.shk-16b,
.shk-16b *,
.shk-16b *::before,
.shk-16b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-16b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 20px;
  padding: 48px 24px;
  background: radial-gradient(110% 110% at 50% 0%,#171223,#0e0b16);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-16b__stage {
  display: flex;
  align-items: center;
  gap: 90px;
  padding: 44px 48px;
  border-radius: 22px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(190,170,255,.16);
}

.shk-16b__add {
  position: relative;
  padding: 15px 24px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 700;
  color: #14101f;
  background: linear-gradient(180deg,oklch(0.85 0.13 315),oklch(0.75 0.15 310));
  border: 0;
  border-radius: 12px;
  cursor: pointer;
  transition: filter .2s,scale .12s;
}

.shk-16b__add:hover {
  filter: brightness(1.07);
}

.shk-16b__add:active {
  scale: .96;
}

.shk-16b__sw {
  position: absolute;
  inset: 0;
  border-radius: 12px;
}

.shk-16b__cartzone {
  position: relative;
}

.shk-16b__cartwrap {
  position: relative;
  width: 64px;
  height: 64px;
  display: grid;
  place-items: center;
  border-radius: 16px;
  background: rgba(255,255,255,.07);
  border: 1px solid rgba(190,170,255,.22);
  color: #e9e2fa;
}

.shk-16b__cartwrap.is-catching {
  animation: shk-16b-catch .5s cubic-bezier(.34,1.56,.64,1);
}

.shk-16b__cart {
  width: 28px;
  height: 28px;
}

.shk-16b__badge {
  position: absolute;
  top: -8px;
  right: -8px;
  min-width: 21px;
  height: 21px;
  padding: 0 5px;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 700;
  color: #14101f;
  background: oklch(0.85 0.13 315);
  border-radius: 999px;
}

.shk-16b__dot {
  position: fixed;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: oklch(0.85 0.13 315);
  box-shadow: 0 0 14px oklch(0.85 0.13 315 / .8);
  pointer-events: none;
  z-index: 9;
  animation: shk-16b-flyx .5s linear both,shk-16b-flyy .5s cubic-bezier(.3,-.55,.65,.7) both;
}

.shk-16b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(233,226,250,.4);
  max-width: 460px;
  justify-self: center;
}

@keyframes shk-16b-flyx {
  to {
    left: var(--tx);
  }
}

@keyframes shk-16b-flyy {
  to {
    top: var(--ty);
  }
}

@keyframes shk-16b-catch {
  0% {
    scale: 1 1;
  }

  25% {
    scale: 1.18 .8;
  }

  55% {
    scale: .92 1.08;
    rotate: -5deg;
  }

  80% {
    scale: 1.03 .98;
    rotate: 3deg;
  }

  100% {
    scale: 1 1;
    rotate: 0deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-16b__dot {
    animation-duration: .01s,.01s;
  }

  .shk-16b__cartwrap.is-catching {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var add=document.getElementById('shk-16a-add'),cart=document.getElementById('shk-16a-cart'),
      badge=document.getElementById('shk-16a-badge'); if(!add) return;
  var n=0;
  cart.addEventListener('animationend',function(){ cart.classList.remove('is-wiggling'); },true);
  add.addEventListener('click',function(){
    n++; badge.textContent=String(n);
    cart.setAttribute('aria-label','Cart: '+n+(n===1?' item':' items'));
    cart.classList.remove('is-wiggling');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ cart.classList.add('is-wiggling'); }); });
  });
})();

(function(){
  var add=document.getElementById('shk-16b-add'),wrap=document.getElementById('shk-16b-cartwrap'),
      badge=document.getElementById('shk-16b-badge'); if(!add) return;
  var n=0;
  wrap.addEventListener('animationend',function(){ wrap.classList.remove('is-catching'); });
  add.addEventListener('click',function(){
    var a=add.getBoundingClientRect(),c=wrap.getBoundingClientRect();
    var dot=document.createElement('span');
    dot.className='shk-16b__dot';
    dot.style.left=(a.right-18)+'px'; dot.style.top=(a.top+a.height/2-7)+'px';
    dot.style.setProperty('--tx',(c.left+c.width/2-7)+'px');
    dot.style.setProperty('--ty',(c.top+c.height/2-7)+'px');
    document.body.appendChild(dot);
    dot.addEventListener('animationend',function once(){
      if(!dot.isConnected) return;
      dot.remove();                                   // both axis animations share one duration
      n++; badge.textContent=String(n);               // count changes AT catch time
      wrap.classList.add('is-catching');
    });
  });
})();
```
