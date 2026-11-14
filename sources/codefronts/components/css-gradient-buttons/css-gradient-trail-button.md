---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-trail-button/"
title: "CSS Gradient Trail Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A checkout-confirmation CTA that emits ten tiny gradient particles from the click point on release — each a small radial gradient, scattered at random…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Trail Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-trail-button/

A checkout-confirmation CTA that emits ten tiny gradient particles from the click point on release — each a small radial gradient, scattered at random angles, fading opacity and scaling down over 800ms. Reward without confetti overload.
## HTML
```html
<div class="gb-17">
  <div class="gb-17__card">
    <p class="gb-17__kicker"><span class="gb-17__kicker-mark">✱</span> Micro-moments</p>
    <h3 class="gb-17__title">Confirmations that celebrate.</h3>
    <p class="gb-17__copy">Every checkout finishes with a moment. Ours emits ten tiny gradient particles that fade over 800ms — reward without confetti overload. Copy-paste, ~30 lines of JS.</p>
    <div class="gb-17__row">
      <div class="gb-17__price">
        <span class="gb-17__price-lab">Order total</span>
        <span class="gb-17__price-num">$47.00</span>
      </div>
      <button class="gb-17__btn" type="button" id="gb-17-btn">
        <span class="gb-17__lab">
          <svg class="gb-17__lock" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="4" y="11" width="16" height="10" rx="2"/>
            <path d="M8 11V7a4 4 0 0 1 8 0v4"/>
          </svg>
          Complete purchase
        </span>
      </button>
    </div>
    <p class="gb-17__foot">Click the button · particles emit + fade in 800ms</p>
  </div>
</div>
```
## CSS
```css
.gb-17,
.gb-17 *,
.gb-17 *::before,
.gb-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-17 ::selection {
  background: #7c6cff;
  color: #fff;
}

.gb-17 {
  --bg: #0a0e1c;
  --panel: #141a2e;
  --line: rgba(148,163,184,.14);
  --c1: #7c6cff;
  --c2: #a78bfa;
  --c3: #22d3ee;
  --success: #22c55e;
  --ink: #e2e8f0;
  --mut: #8b93ab;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(90% 120% at 20% -10%, rgba(124,108,255,.14) 0%, transparent 55%), radial-gradient(80% 100% at 100% 100%, rgba(34,211,238,.10) 0%, transparent 60%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--ink);
}

.gb-17__card {
  width: min(500px,100%);
  background: linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 32px 32px 28px;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
}

.gb-17__kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--c2);
  margin-bottom: 14px;
}

.gb-17__kicker-mark {
  color: var(--c2);
  font-size: 12px;
  line-height: 1;
}

.gb-17__title {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.01em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.gb-17__copy {
  font-size: 14px;
  line-height: 1.55;
  color: var(--mut);
  margin-bottom: 24px;
}

.gb-17__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 16px 18px;
  border-radius: 14px;
  background: rgba(255,255,255,.03);
  border: 1px solid var(--line);
  flex-wrap: wrap;
}

.gb-17__price {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.gb-17__price-lab {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
}

.gb-17__price-num {
  font-size: 20px;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
  font-feature-settings: "tnum";
}

.gb-17__btn {
  position: relative;
  overflow: visible;
  display: inline-flex;
  align-items: center;
  padding: 13px 22px;
  border: 0;
  border-radius: 12px;
  color: #fff;
  font-family: inherit;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .01em;
  cursor: pointer;
  background: linear-gradient(135deg, var(--c1) 0%, var(--c2) 55%, var(--c3) 100%);
  box-shadow: 0 14px 28px -12px rgba(124,108,255,.55), inset 0 1px 0 rgba(255,255,255,.24);
  transition: transform .12s ease, box-shadow .3s ease;
}

.gb-17__btn:hover {
  transform: translateY(-1px);
}

.gb-17__btn:active {
  transform: translateY(0);
}

.gb-17__btn.is-firing {
  background: linear-gradient(135deg, var(--success) 0%, var(--c3) 100%);
  box-shadow: 0 20px 40px -14px rgba(34,197,94,.65);
  transition: background .35s ease, box-shadow .35s ease;
}

.gb-17__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.gb-17__lab {
  position: relative;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.gb-17__lock {
  opacity: .9;
}

.gb-17__spark {
  position: absolute;
  left: var(--gb-17-x);
  top: var(--gb-17-y);
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: radial-gradient(circle at 40% 40%, #fff 0%, var(--c2) 45%, transparent 75%);
  pointer-events: none;
  transform: translate(-50%, -50%);
  animation: gb-17-fly 800ms ease-out forwards;
  will-change: transform,opacity;
}

@keyframes gb-17-fly {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
    filter: blur(0);
  }

  100% {
    transform: translate(
          calc(-50% + cos(var(--gb-17-a)) * var(--gb-17-d)),
          calc(-50% + sin(var(--gb-17-a)) * var(--gb-17-d))
        ) scale(.2);
    opacity: 0;
    filter: blur(2px);
  }
}

.gb-17__foot {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: .02em;
  margin-top: 20px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-17__btn {
    transition: none;
  }

  .gb-17__btn.is-firing {
    transition: none;
  }

  .gb-17__spark {
    animation: none;
    opacity: 0;
  }
}

@media (max-width: 520px) {
  .gb-17__row {
    gap: 10px;
  }

  .gb-17__btn {
    width: 100%;
    justify-content: center;
  }
}
```

## JavaScript
```js
(function(){
  var btn = document.getElementById('gb-17-btn');
  if(!btn) return;
  var N_SPARKS = 10;
  var LIFESPAN = 900;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  btn.addEventListener('click', function(e){
    // Flash the button gradient to a success-tinted state briefly.
    btn.classList.add('is-firing');
    setTimeout(function(){ btn.classList.remove('is-firing'); }, 420);
    if(reduced) return;

    var rect = btn.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;

    for(var i = 0; i < N_SPARKS; i++){
      var spark = document.createElement('span');
      spark.className = 'gb-17__spark';
      // Random angle in radians + distance 60-90px + small size jitter.
      var angle = Math.random() * Math.PI * 2;
      var dist  = 60 + Math.random() * 30;
      var size  = 10 + Math.random() * 8;
      spark.style.setProperty('--gb-17-x', x + 'px');
      spark.style.setProperty('--gb-17-y', y + 'px');
      spark.style.setProperty('--gb-17-a', angle + 'rad');
      spark.style.setProperty('--gb-17-d', dist + 'px');
      spark.style.width  = size + 'px';
      spark.style.height = size + 'px';
      btn.appendChild(spark);
    }

    setTimeout(function(){
      var sparks = btn.querySelectorAll('.gb-17__spark');
      for(var j = 0; j < sparks.length; j++){
        sparks[j].remove();
      }
    }, LIFESPAN);
  });
})();
```
