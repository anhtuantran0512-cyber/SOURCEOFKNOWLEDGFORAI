---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/disabled-button-shake-css/"
title: "Disabled Button Shake CSS"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The disabled-button problem solved twice: a pure-CSS version where hovering the wrapper makes the dead button shake its head and float its reason ('accept…"
has_js: "true"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Disabled Button Shake CSS
Source: https://codefronts.com/motion/css-shake-animation/disabled-button-shake-css/

The disabled-button problem solved twice: a pure-CSS version where hovering the wrapper makes the dead button shake its head and float its reason ('accept the terms first'), and the full JavaScript pattern that catches clicks on a wrapper — because disabled buttons swallow their own click events — then shakes, explains, and unlocks live when the checklist completes.
## HTML
```html
<div class="shk-14-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-14a" aria-label="Disabled button that shakes its head on hover">
  <div class="shk-14a__card">
    <h2 class="shk-14a__title">Almost there</h2>
    <label class="shk-14a__check"><input class="shk-14a__box" id="shk-14a-terms" type="checkbox"><span>I've read the <b>terms of service</b></span></label>
    <span class="shk-14a__gate">
      <button class="shk-14a__btn" type="button" disabled>Create account</button>
      <span class="shk-14a__tip" role="tooltip">Accept the terms first</span>
    </span>
    <p class="shk-14a__hint" aria-hidden="true">hover the dead button — it shakes “no”; tick the box and CSS :has() wakes it up</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-14b" aria-label="Disabled deploy button that shakes and explains when clicked">
  <div class="shk-14b__card">
    <div class="shk-14b__head"><h2 class="shk-14b__title">Deploy to production</h2><span class="shk-14b__env">v2.4.1</span></div>
    <ul class="shk-14b__list" id="shk-14b-list">
      <li><label class="shk-14b__item"><input type="checkbox" checked> Tests passing <em>412/412</em></label></li>
      <li><label class="shk-14b__item"><input type="checkbox" id="shk-14b-review"> Code review approved</label></li>
      <li><label class="shk-14b__item"><input type="checkbox" id="shk-14b-migr"> Migrations dry-run</label></li>
    </ul>
    <span class="shk-14b__gate" id="shk-14b-gate">
      <button class="shk-14b__btn" id="shk-14b-btn" type="button" disabled>Deploy</button>
    </span>
    <p class="shk-14b__why" id="shk-14b-why" aria-live="polite">2 checks remaining</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-14-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-14-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-14a,
.shk-14a *,
.shk-14a *::before,
.shk-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-14a {
  --ink: #1d2025;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f4f5f6,#e9ebed);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-14a__card {
  width: min(400px,100%);
  padding: 36px;
  border-radius: 20px;
  background: #fff;
  border: 1px solid rgba(29,32,37,.1);
  box-shadow: 0 30px 70px -40px rgba(29,32,37,.45);
  display: grid;
  gap: 18px;
}

.shk-14a__title {
  font-size: 23px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
}

.shk-14a__check {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: rgba(29,32,37,.75);
  cursor: pointer;
  user-select: none;
}

.shk-14a__check b {
  color: var(--ink);
}

.shk-14a__box {
  width: 19px;
  height: 19px;
  accent-color: var(--ink);
  cursor: pointer;
}

.shk-14a__gate {
  position: relative;
  display: block;
}

.shk-14a__btn {
  width: 100%;
  padding: 15px;
  font: inherit;
  font-size: 15px;
  font-weight: 800;
  border: 0;
  border-radius: 13px;
  color: #fff;
  background: var(--ink);
  cursor: pointer;
  transition: opacity .25s,background .25s,scale .12s;
}

.shk-14a__btn:not(:disabled):hover {
  background: #31353c;
}

.shk-14a__btn:not(:disabled):active {
  scale: .98;
}

.shk-14a__btn:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.shk-14a__gate:hover .shk-14a__btn:disabled {
  animation: shk-14a-headshake .5s ease-in-out;
}

.shk-14a__tip {
  position: absolute;
  left: 50%;
  bottom: calc(100% + 10px);
  translate: -50% 4px;
  white-space: nowrap;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  background: var(--ink);
  padding: 7px 12px;
  border-radius: 8px;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s,translate .2s;
}

.shk-14a__tip::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 100%;
  translate: -50% 0;
  border: 5px solid transparent;
  border-top-color: var(--ink);
}

.shk-14a__gate:hover .shk-14a__tip {
  opacity: 1;
  translate: -50% 0;
}

.shk-14a__card:has(.shk-14a__box:checked) .shk-14a__btn {
  opacity: 1;
  cursor: pointer;
  background: oklch(0.55 0.15 155);
}

.shk-14a__card:has(.shk-14a__box:checked) .shk-14a__gate:hover .shk-14a__btn {
  animation: shk-14a-nod .45s cubic-bezier(.34,1.56,.64,1);
}

.shk-14a__card:has(.shk-14a__box:checked) .shk-14a__tip {
  display: none;
}

.shk-14a__hint {
  font-size: 11.5px;
  color: rgba(29,32,37,.45);
}

@keyframes shk-14a-headshake {
  0%,
    100% {
    rotate: 0deg;
  }

  20% {
    rotate: -4deg;
  }

  45% {
    rotate: 3.5deg;
  }

  70% {
    rotate: -2deg;
  }

  88% {
    rotate: 1deg;
  }
}

@keyframes shk-14a-nod {
  30% {
    translate: 0 5px;
  }

  65% {
    translate: 0 -3px;
  }

  88% {
    translate: 0 1px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-14a__gate:hover .shk-14a__btn:disabled,
    .shk-14a__card:has(.shk-14a__box:checked) .shk-14a__gate:hover .shk-14a__btn {
    animation: none;
  }
}

.shk-14b,
.shk-14b *,
.shk-14b *::before,
.shk-14b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-14b {
  --ok: oklch(0.75 0.16 155);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#12151c,#0b0d12);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-14b__card {
  width: min(420px,100%);
  padding: 30px;
  border-radius: 18px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(160,185,220,.15);
  box-shadow: 0 40px 90px -50px rgba(0,0,0,.9);
}

.shk-14b__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.shk-14b__title {
  font-size: 19px;
  font-weight: 700;
  color: #e9eefa;
  letter-spacing: -.01em;
}

.shk-14b__env {
  font-size: 12px;
  font-weight: 600;
  color: rgba(210,225,250,.5);
}

.shk-14b__list {
  margin-top: 18px;
  list-style: none;
  display: grid;
  gap: 9px;
}

.shk-14b__item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: rgba(226,234,250,.8);
  padding: 11px 13px;
  background: rgba(8,11,16,.5);
  border: 1px solid rgba(160,185,220,.12);
  border-radius: 11px;
  cursor: pointer;
}

.shk-14b__item input {
  width: 17px;
  height: 17px;
  accent-color: oklch(0.75 0.16 155);
}

.shk-14b__item em {
  margin-left: auto;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(210,225,250,.45);
}

.shk-14b__gate {
  display: block;
  margin-top: 18px;
}

.shk-14b__btn {
  width: 100%;
  padding: 15px;
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  border: 0;
  border-radius: 12px;
  color: #0b0d12;
  background: var(--ok);
  cursor: pointer;
  transition: opacity .25s,filter .2s,scale .12s;
}

.shk-14b__btn:disabled {
  opacity: .32;
  cursor: not-allowed;
}

.shk-14b__btn:not(:disabled):hover {
  filter: brightness(1.08);
}

.shk-14b__btn:not(:disabled):active {
  scale: .98;
}

.shk-14b__gate.is-nope .shk-14b__btn {
  animation: shk-14b-shake .5s cubic-bezier(.36,.07,.19,.97);
}

.shk-14b__why {
  margin-top: 12px;
  font-size: 12.5px;
  color: rgba(210,225,250,.5);
  text-align: center;
  min-height: 18px;
}

.shk-14b__why.err {
  color: oklch(0.78 0.13 25);
  font-weight: 600;
}

.shk-14b__why.ok {
  color: var(--ok);
  font-weight: 600;
}

@keyframes shk-14b-shake {
  15% {
    translate: -7px 0;
  }

  32% {
    translate: 6px 0;
  }

  50% {
    translate: -4px 0;
  }

  68% {
    translate: 2px 0;
  }

  85% {
    translate: -1px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-14b__gate.is-nope .shk-14b__btn {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover lands on the WRAPPER (disabled buttons still render :hover styles but swallow events), which drives both the head-shake and the tooltip. :has(:checked) restyles the button and swaps the head-shake for a nod. (CSS can't flip the real disabled attribute — see variant b.) */

(function(){
  var gate=document.getElementById('shk-14b-gate'); if(!gate) return;
  var btn=document.getElementById('shk-14b-btn'),why=document.getElementById('shk-14b-why'),
      list=document.getElementById('shk-14b-list');
  function pending(){ return [].filter.call(list.querySelectorAll('input'),function(c){ return !c.checked; }).length; }
  function sync(){
    var n=pending();
    btn.disabled=n>0;
    why.className='shk-14b__why'+(n?'':' ok');
    why.textContent=n?n+(n===1?' check':' checks')+' remaining':'All checks green — safe to deploy.';
  }
  list.addEventListener('change',sync);
  gate.addEventListener('animationend',function(){ gate.classList.remove('is-nope'); });
  // Disabled <button> elements DO NOT dispatch click events (modern spec —
  // Chromium, Firefox, Safari all agree). But pointerdown DOES fire and
  // bubble even when the target is disabled — so the wrapper listens on
  // pointerdown to catch the "user tried to click a disabled button"
  // gesture. When the button becomes enabled, the same wrapper handles
  // the enabled path via click on the button itself.
  gate.addEventListener('pointerdown',function(e){
    if(!btn.disabled) return;   // let the button's own click handler run when enabled
    if(e.target!==btn && !btn.contains(e.target)) return;  // only shake for clicks on the button itself
    gate.classList.remove('is-nope');
    requestAnimationFrame(function(){ requestAnimationFrame(function(){ gate.classList.add('is-nope'); }); });
    why.className='shk-14b__why err';
    why.textContent='Blocked: '+pending()+' unchecked item'+(pending()===1?'':'s')+' above.';
  });
  // Enabled-button path: real click dispatches normally once the button
  // is no longer disabled.
  btn.addEventListener('click',function(){
    why.className='shk-14b__why ok';
    why.textContent='Deploying v2.4.1…';
  });
  sync();
})();
```
