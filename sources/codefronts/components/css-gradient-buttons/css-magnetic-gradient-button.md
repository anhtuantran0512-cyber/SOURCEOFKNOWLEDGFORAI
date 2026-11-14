---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-magnetic-gradient-button/"
title: "CSS Magnetic Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A conversion-research SaaS CTA whose gradient button attracts the cursor when it approaches — subtly translates toward the pointer while the radial hotspot…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magnetic Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/css-magnetic-gradient-button/

A conversion-research SaaS CTA whose gradient button attracts the cursor when it approaches — subtly translates toward the pointer while the radial hotspot tracks its exact position, then springs back to center with a soft bounce when the pointer leaves.
## HTML
```html
<div class="gb-02">
  <div class="gb-02__card">
    <p class="gb-02__kicker"><span class="gb-02__kicker-dot">★</span> Conversion research</p>
    <h3 class="gb-02__title">Buttons that reach for you.</h3>
    <p class="gb-02__copy">Our A/B test: magnetic buttons lift click-through 41% vs static. The physics take ~30 lines of JS. Same brand, same copy — different pull.</p>
    <div class="gb-02__wrap" id="gb-02-wrap">
      <button class="gb-02__btn" type="button" id="gb-02-btn">
        <span class="gb-02__lab">Try the magnet</span>
        <svg class="gb-02__arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M5 12h14M13 5l7 7-7 7"/>
        </svg>
      </button>
    </div>
    <p class="gb-02__foot">Live demo · move your cursor near the button</p>
  </div>
</div>
```
## CSS
```css
.gb-02,
.gb-02 *,
.gb-02 *::before,
.gb-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-02 ::selection {
  background: #a78bfa;
  color: #0b0e1a;
}

.gb-02 {
  --bg: #0a0e1c;
  --panel: #141a2e;
  --line: rgba(148,163,184,.14);
  --c1: #7c6cff;
  --c2: #22d3ee;
  --c3: #a78bfa;
  --ink: #e2e8f0;
  --mut: #8b93ab;
  --gb-02-x: 0;
  --gb-02-y: 0;
  --gb-02-hx: 50%;
  --gb-02-hy: 50%;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(90% 120% at 20% -10%, rgba(124,108,255,.16) 0%, transparent 55%), radial-gradient(80% 100% at 100% 100%, rgba(34,211,238,.10) 0%, transparent 60%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  color: var(--ink);
}

.gb-02__card {
  width: min(460px,100%);
  background: linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,0)),var(--panel);
  border: 1px solid var(--line);
  border-radius: 20px;
  padding: 32px 32px 28px;
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.7);
  text-align: center;
}

.gb-02__kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--c3);
  margin-bottom: 14px;
}

.gb-02__kicker-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: linear-gradient(135deg,var(--c1),var(--c2));
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  color: #fff;
}

.gb-02__title {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.01em;
  line-height: 1.15;
  margin-bottom: 10px;
}

.gb-02__copy {
  font-size: 14px;
  line-height: 1.55;
  color: var(--mut);
  margin-bottom: 28px;
}

.gb-02__wrap {
  padding: 44px 60px;
  display: inline-flex;
  justify-content: center;
  border-radius: 24px;
  cursor: default;
}

.gb-02__btn {
  --dur: .14s;
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 26px;
  border: 0;
  border-radius: 14px;
  color: #fff;
  font-family: inherit;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .01em;
  cursor: pointer;
  background: radial-gradient(180px 180px at var(--gb-02-hx) var(--gb-02-hy), rgba(255,255,255,.35), transparent 55%), linear-gradient(135deg, var(--c1) 0%, var(--c3) 55%, var(--c2) 100%);
  box-shadow: 0 18px 32px -14px rgba(124,108,255,.55), 0 2px 8px -2px rgba(34,211,238,.35), inset 0 1px 0 rgba(255,255,255,.24);
  transform: translate3d(calc(var(--gb-02-x) * .35px), calc(var(--gb-02-y) * .35px), 0);
  transition: box-shadow var(--dur) ease, transform 0s;
  will-change: transform;
}

.gb-02__btn.is-releasing {
  transition: transform .55s cubic-bezier(.34,1.56,.64,1), box-shadow .3s ease;
}

.gb-02__btn::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: 18px;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  opacity: 0;
  filter: blur(18px);
  z-index: -1;
  transition: opacity .3s;
}

.gb-02__btn:hover::before {
  opacity: .6;
}

.gb-02__btn:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.gb-02__lab {
  position: relative;
  z-index: 1;
}

.gb-02__arrow {
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
  position: relative;
  z-index: 1;
}

.gb-02__btn:hover .gb-02__arrow {
  transform: translateX(4px);
}

.gb-02__foot {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: .02em;
  margin-top: 24px;
}

@media (prefers-reduced-motion: reduce) {
  .gb-02__btn {
    transform: none !important;
    transition: none;
  }

  .gb-02__btn.is-releasing {
    transition: none;
  }

  .gb-02__arrow {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  var wrap = document.getElementById('gb-02-wrap');
  var btn  = document.getElementById('gb-02-btn');
  if(!wrap || !btn) return;
  // Skip on touch devices — magnetic pull relies on a pointing cursor.
  if(!matchMedia('(pointer: fine)').matches) return;

  var rect = null;

  function onEnter(){
    rect = btn.getBoundingClientRect();
    btn.classList.remove('is-releasing');
  }
  function onMove(e){
    if(!rect) rect = btn.getBoundingClientRect();
    var cx = rect.left + rect.width  / 2;
    var cy = rect.top  + rect.height / 2;
    var dx = e.clientX - cx;
    var dy = e.clientY - cy;
    btn.style.setProperty('--gb-02-x', dx);
    btn.style.setProperty('--gb-02-y', dy);
    var hx = ((e.clientX - rect.left) / rect.width  * 100);
    var hy = ((e.clientY - rect.top)  / rect.height * 100);
    btn.style.setProperty('--gb-02-hx', hx + '%');
    btn.style.setProperty('--gb-02-hy', hy + '%');
  }
  function onLeave(){
    btn.classList.add('is-releasing');
    btn.style.setProperty('--gb-02-x', 0);
    btn.style.setProperty('--gb-02-y', 0);
    btn.style.setProperty('--gb-02-hx', '50%');
    btn.style.setProperty('--gb-02-hy', '50%');
    rect = null;
  }
  wrap.addEventListener('pointerenter', onEnter);
  wrap.addEventListener('pointermove',  onMove);
  wrap.addEventListener('pointerleave', onLeave);
})();
```
