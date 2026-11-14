---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/cursor-tracking-aurora-gradient-button/"
title: "Cursor Tracking Aurora Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A dark glass button whose aurora core and gradient border spotlight both chase the pointer with a lazy trailing glide, then drift back to center when the…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cursor Tracking Aurora Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/cursor-tracking-aurora-gradient-button/

A dark glass button whose aurora core and gradient border spotlight both chase the pointer with a lazy trailing glide, then drift back to center when the cursor leaves — powered by transitions on registered @property percentages.
## HTML
```html
<div class="gx-22">
  <div class="gx-22__card">
    <span class="gx-22__badge">Private beta</span>
    <h3 class="gx-22__title">Lumen is almost ready</h3>
    <p class="gx-22__copy">A calmer way to read the internet. We let a few hundred people in every Friday.</p>
    <button class="gx-22__btn" type="button" id="gx-22-btn">
      <span class="gx-22__spark" aria-hidden="true">✦</span>
      Request an invite
    </button>
    <p class="gx-22__fine">No card required · 2,418 people ahead of you</p>
  </div>
</div>
```
## CSS
```css
.gx-22,
.gx-22 *,
.gx-22 *::before,
.gx-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gx-22 ::selection {
  background: #67e8f9;
  color: #0a0d1c;
}

@property --gx-22-x {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 50%;
}

@property --gx-22-y {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 50%;
}

.gx-22 {
  --bg: #0a0d1c;
  --ink: #e6e9f5;
  --mut: #8a91ad;
  --a1: #67e8f9;
  --a2: #a78bfa;
  --a3: #f0abfc;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(90% 70% at 15% 0%,rgba(103,232,249,.06),transparent 55%), radial-gradient(80% 60% at 90% 100%,rgba(167,139,250,.08),transparent 55%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gx-22__card {
  width: min(400px,100%);
  text-align: center;
  padding: 36px 32px;
  border-radius: 24px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(148,163,184,.12);
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.8);
}

.gx-22__badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 12px;
  border-radius: 999px;
  border: 1px solid rgba(103,232,249,.25);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--a1);
}

.gx-22__badge::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--a1);
  box-shadow: 0 0 8px var(--a1);
}

.gx-22__title {
  margin-top: 18px;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: var(--ink);
}

.gx-22__copy {
  margin: 10px auto 0;
  max-width: 32ch;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
}
/* The button. --gx-22-x / --gx-22-y are registered <percentage> custom
   properties, so they INTERPOLATE: JS writes raw pointer coords, CSS
   transitions them, giving the aurora its lazy trailing glide. */

.gx-22__btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  width: 100%;
  margin-top: 26px;
  padding: 17px 28px;
  border: 0;
  border-radius: 16px;
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: .02em;
  color: var(--ink);
  cursor: pointer;
  isolation: isolate;
  background: radial-gradient(150% 120% at var(--gx-22-x) var(--gx-22-y),rgba(124,58,237,.28),transparent 55%), #10142b;
  transition: --gx-22-x .35s ease-out,--gx-22-y .35s ease-out,transform .3s ease;
}

.gx-22__btn:active {
  transform: scale(.98);
}

.gx-22__btn:focus-visible {
  outline: 2px solid var(--a1);
  outline-offset: 4px;
}
/* Gradient border spotlight, hollowed with a two-layer mask,
   lit around the same tracked point */

.gx-22__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: radial-gradient(130px 90px at var(--gx-22-x) var(--gx-22-y),
      var(--a1),var(--a2) 45%,rgba(148,163,184,.16) 75%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  z-index: -1;
}
/* Soft aurora bloom inside, fades up when the pointer is over */

.gx-22__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(140px 100px at var(--gx-22-x) var(--gx-22-y),
      rgba(103,232,249,.30),rgba(167,139,250,.22) 45%,rgba(240,171,252,.10) 65%,transparent 78%);
  opacity: .35;
  transition: opacity .45s ease;
  z-index: -1;
}

.gx-22__btn.is-lit::after {
  opacity: 1;
}

.gx-22__spark {
  font-size: 17px;
  line-height: 1;
  transform: translateY(-1px);
}

.gx-22__fine {
  margin-top: 14px;
  font-size: 11.5px;
  letter-spacing: .03em;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .gx-22__btn {
    transition: none;
  }

  .gx-22__btn::after {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var btn=document.getElementById('gx-22-btn');
  if(!btn)return;
  btn.addEventListener('pointermove',function(e){
    var r=btn.getBoundingClientRect();
    var x=Math.max(0,Math.min(100,(e.clientX-r.left)/r.width*100));
    var y=Math.max(0,Math.min(100,(e.clientY-r.top)/r.height*100));
    btn.style.setProperty('--gx-22-x',x.toFixed(1)+'%');
    btn.style.setProperty('--gx-22-y',y.toFixed(1)+'%');
  });
  btn.addEventListener('pointerenter',function(){
    btn.classList.add('is-lit');
  });
  btn.addEventListener('pointerleave',function(){
    btn.classList.remove('is-lit');
    /* removing the inline values lets the registered properties
       transition back to their 50%/50% initial values */
    btn.style.removeProperty('--gx-22-x');
    btn.style.removeProperty('--gx-22-y');
  });
})();
```
