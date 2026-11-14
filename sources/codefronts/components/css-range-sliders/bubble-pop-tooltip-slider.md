---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/bubble-pop-tooltip-slider/"
title: "Bubble Pop Tooltip Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A loan calculator slider where pressing the thumb pops up a teardrop speech bubble with a spring scale animation, live loan amount and monthly payment…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bubble Pop Tooltip Slider
Source: https://codefronts.com/components/css-range-sliders/bubble-pop-tooltip-slider/

A loan calculator slider where pressing the thumb pops up a teardrop speech bubble with a spring scale animation, live loan amount and monthly payment calculations update in real time, and the bubble tracks the thumb position precisely.
## HTML
```html
<div class="rs-10">
  <div class="rs-10__card">
    <div class="rs-10__header">
      <div class="rs-10__title">Loan Calculator</div>
      <div class="rs-10__sub">Drag to adjust your loan amount</div>
    </div>
    <div class="rs-10__amount-row">
      <span class="rs-10__currency">$</span>
      <span class="rs-10__amount" id="rs-10-amount">15,000</span>
      <span class="rs-10__period">loan</span>
    </div>
    <div class="rs-10__track-wrap" id="rs-10-wrap">
      <div class="rs-10__bubble" id="rs-10-bubble">
        <div class="rs-10__bubble-body" id="rs-10-tip">$15,000</div>
        <div class="rs-10__bubble-arrow"></div>
      </div>
      <div class="rs-10__track-bg"></div>
      <div class="rs-10__track-fill" id="rs-10-fill"></div>
      <input class="rs-10__input" type="range" min="1000" max="50000" step="500" value="15000" id="rs-10-inp">
    </div>
    <div class="rs-10__marks">
      <span class="rs-10__mark">$1K</span>
      <span class="rs-10__mark">$10K</span>
      <span class="rs-10__mark">$25K</span>
      <span class="rs-10__mark">$50K</span>
    </div>
    <div class="rs-10__breakdown">
      <div class="rs-10__item">
        <div class="rs-10__item-label">Monthly</div>
        <div class="rs-10__item-val" id="rs-10-mo">$298</div>
      </div>
      <div class="rs-10__item">
        <div class="rs-10__item-label">Rate APR</div>
        <div class="rs-10__item-val">6.9%</div>
      </div>
      <div class="rs-10__item">
        <div class="rs-10__item-label">Term</div>
        <div class="rs-10__item-val">60 mo</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-10,
.rs-10 *,
.rs-10 *::before,
.rs-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-10 ::selection {
  background: #7c3aed;
  color: #fff;
}

.rs-10 {
  --bg: #1e1b4b;
  --card: #2e2a60;
  --violet: #7c3aed;
  --violet-light: #a78bfa;
  --violet-glow: rgba(124,58,237,0.5);
  --text: #ede9fe;
  --muted: #8b80c4;
  --border: #3d3875;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-10__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px;
  max-width: 440px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.rs-10__header {
  margin-bottom: 12px;
}

.rs-10__title {
  font-size: 18px;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.rs-10__sub {
  font-size: 13px;
  color: var(--muted);
}

.rs-10__amount-row {
  display: flex;
  align-items: baseline;
  gap: 4px;
  margin: 20px 0 44px;
}

.rs-10__currency {
  font-size: 24px;
  color: var(--violet-light);
  font-weight: 700;
}

.rs-10__amount {
  font-size: 56px;
  font-weight: 900;
  color: var(--text);
  letter-spacing: -3px;
  font-variant-numeric: tabular-nums;
}

.rs-10__period {
  font-size: 14px;
  color: var(--muted);
  align-self: flex-end;
  margin-bottom: 8px;
}

.rs-10__track-wrap {
  position: relative;
  padding-top: 54px;
  margin-bottom: 16px;
}

.rs-10__bubble {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  pointer-events: none;
  transition: left 0.05s;
}

.rs-10__bubble-body {
  background: var(--violet);
  color: #fff;
  font-size: 13px;
  font-weight: 800;
  padding: 6px 14px;
  border-radius: 20px;
  white-space: nowrap;
  box-shadow: 0 4px 20px var(--violet-glow);
  transform: scale(0);
  transform-origin: bottom center;
  transition: transform 0.25s cubic-bezier(0.34,1.56,0.64,1);
}

.rs-10__bubble-arrow {
  width: 0;
  height: 0;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-top: 8px solid var(--violet);
  margin-top: -1px;
  opacity: 0;
  transition: opacity 0.2s;
}

.rs-10__track-wrap.active .rs-10__bubble-body {
  transform: scale(1);
}

.rs-10__track-wrap.active .rs-10__bubble-arrow {
  opacity: 1;
}

.rs-10__track-bg {
  height: 8px;
  background: rgba(255,255,255,0.08);
  border-radius: 99px;
}

.rs-10__track-fill {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 8px;
  background: linear-gradient(90deg, var(--violet), var(--violet-light));
  border-radius: 99px;
  box-shadow: 0 0 16px var(--violet-glow);
  transition: width 0.05s;
}

.rs-10__input {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 36px;
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
  margin-bottom: -14px;
}

.rs-10__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  border: 3px solid var(--violet);
  box-shadow: 0 0 12px var(--violet-glow);
  cursor: grab;
  transition: transform 0.15s;
}

.rs-10__input:active::-webkit-slider-thumb {
  transform: scale(1.15);
  cursor: grabbing;
}

.rs-10__input::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 3px solid var(--violet);
  background: #fff;
  cursor: grab;
}

.rs-10__marks {
  display: flex;
  justify-content: space-between;
  margin-top: 8px;
}

.rs-10__mark {
  font-size: 11px;
  color: var(--muted);
}

.rs-10__breakdown {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
  display: flex;
  gap: 0;
}

.rs-10__item {
  flex: 1;
  text-align: center;
}

.rs-10__item + .rs-10__item {
  border-left: 1px solid var(--border);
}

.rs-10__item-label {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.rs-10__item-val {
  font-size: 16px;
  font-weight: 700;
  color: var(--text);
}

@media (prefers-reduced-motion: reduce) {
  .rs-10__bubble-body,
    .rs-10__bubble-arrow,
    .rs-10__track-fill {
    transition: none;
  }

  .rs-10__bubble-body {
    transform: scale(1);
  }

  .rs-10__bubble-arrow {
    opacity: 1;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-10-inp');
  const wrap = document.getElementById('rs-10-wrap');
  const bubble = document.getElementById('rs-10-bubble');
  const tip = document.getElementById('rs-10-tip');
  const fill = document.getElementById('rs-10-fill');
  const amount = document.getElementById('rs-10-amount');
  const mo = document.getElementById('rs-10-mo');
  function fmt(n){ return n>=1000? '$'+Math.round(n/1000)+'K' : '$'+n; }
  function update(){
    const v = +inp.value;
    const pct = (v - +inp.min)/(+inp.max - +inp.min)*100;
    fill.style.width = pct+'%';
    bubble.style.left = pct+'%';
    tip.textContent = fmt(v);
    amount.textContent = v.toLocaleString();
    // simple monthly calc: P*r*(1+r)^n / ((1+r)^n-1)
    const r = 0.069/12, n = 60;
    const m = Math.round(v*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1));
    mo.textContent = '$'+m.toLocaleString();
  }
  inp.addEventListener('mousedown', ()=> wrap.classList.add('active'));
  inp.addEventListener('touchstart', ()=> wrap.classList.add('active'), {passive:true});
  document.addEventListener('mouseup', ()=> wrap.classList.remove('active'));
  document.addEventListener('touchend', ()=> wrap.classList.remove('active'));
  inp.addEventListener('input', update);
  update();
})();
```
