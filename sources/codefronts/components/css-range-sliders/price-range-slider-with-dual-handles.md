---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/price-range-slider-with-dual-handles/"
title: "Price Range Slider with Dual Handles"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A sleek e-commerce dual-handle range slider where two independent thumb knobs control min and max price, with a glowing emerald fill segment between them and…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Price Range Slider with Dual Handles
Source: https://codefronts.com/components/css-range-sliders/price-range-slider-with-dual-handles/

A sleek e-commerce dual-handle range slider where two independent thumb knobs control min and max price, with a glowing emerald fill segment between them and live product count feedback.
## HTML
```html
<div class="rs-01" id="rs-01-root">
  <div class="rs-01__card">
    <div class="rs-01__header">
      <div>
        <div class="rs-01__title">Price Range</div>
        <div class="rs-01__subtitle">Filter products by budget</div>
      </div>
      <div class="rs-01__badge">E-SHOP</div>
    </div>
    <div class="rs-01__prices">
      <div class="rs-01__price-box">
        <div class="rs-01__price-label">Min Price</div>
        <div class="rs-01__price-value"><span>$</span><span id="rs-01-min-val">20</span></div>
      </div>
      <div class="rs-01__price-box">
        <div class="rs-01__price-label">Max Price</div>
        <div class="rs-01__price-value"><span>$</span><span id="rs-01-max-val">150</span></div>
      </div>
    </div>
    <div class="rs-01__range-wrap" id="rs-01-wrap">
      <div class="rs-01__track-bg"></div>
      <div class="rs-01__track-fill" id="rs-01-fill"></div>
      <input class="rs-01__input" type="range" id="rs-01-lo" min="0" max="200" value="20">
      <input class="rs-01__input" type="range" id="rs-01-hi" min="0" max="200" value="150">
      <div class="rs-01__thumb" id="rs-01-thumb-lo">
        <div class="rs-01__tooltip" id="rs-01-tip-lo">$20</div>
      </div>
      <div class="rs-01__thumb" id="rs-01-thumb-hi">
        <div class="rs-01__tooltip" id="rs-01-tip-hi">$150</div>
      </div>
    </div>
    <div class="rs-01__ticks">
      <span class="rs-01__tick">$0</span>
      <span class="rs-01__tick">$50</span>
      <span class="rs-01__tick">$100</span>
      <span class="rs-01__tick">$150</span>
      <span class="rs-01__tick">$200</span>
    </div>
    <div class="rs-01__results">
      <div class="rs-01__count"><strong id="rs-01-count">247</strong> products found</div>
      <button class="rs-01__btn">Apply Filter</button>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-01,
.rs-01 *,
.rs-01 *::before,
.rs-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-01 ::selection {
  background: #00c896;
  color: #0a1628;
}

.rs-01 {
  --bg: #0a1628;
  --surface: #111d35;
  --card: #162040;
  --border: #1e3058;
  --emerald: #00c896;
  --emerald-dim: rgba(0,200,150,0.15);
  --emerald-glow: rgba(0,200,150,0.4);
  --text: #e8f0fe;
  --muted: #6b82a8;
  --track-h: 6px;
  --thumb-size: 22px;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-01__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 32px;
  width: 100%;
  max-width: 460px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04);
}

.rs-01__header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 28px;
}

.rs-01__title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.3px;
}

.rs-01__subtitle {
  font-size: 12px;
  color: var(--muted);
  margin-top: 3px;
}

.rs-01__badge {
  background: var(--emerald-dim);
  border: 1px solid var(--emerald-glow);
  color: var(--emerald);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  letter-spacing: 0.5px;
}

.rs-01__prices {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.rs-01__price-box {
  text-align: center;
}

.rs-01__price-label {
  font-size: 11px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 4px;
}

.rs-01__price-value {
  font-size: 26px;
  font-weight: 800;
  color: var(--emerald);
  letter-spacing: -1px;
  font-variant-numeric: tabular-nums;
}

.rs-01__price-value span {
  font-size: 14px;
  font-weight: 500;
  color: var(--muted);
  vertical-align: super;
}

.rs-01__range-wrap {
  position: relative;
  height: 52px;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.rs-01__track-bg {
  position: absolute;
  width: 100%;
  height: var(--track-h);
  background: var(--border);
  border-radius: 99px;
  top: 50%;
  transform: translateY(-50%);
}

.rs-01__track-fill {
  position: absolute;
  height: var(--track-h);
  background: linear-gradient(90deg, #00c896, #00e5b0);
  border-radius: 99px;
  top: 50%;
  transform: translateY(-50%);
  box-shadow: 0 0 12px var(--emerald-glow);
  transition: left 0.05s, width 0.05s;
}

.rs-01__input {
  position: absolute;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
  margin: 0;
  -webkit-appearance: none;
  pointer-events: none;
}

.rs-01__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  pointer-events: all;
  width: var(--thumb-size);
  height: var(--thumb-size);
  border-radius: 50%;
  cursor: grab;
}

.rs-01__input::-moz-range-thumb {
  pointer-events: all;
  width: var(--thumb-size);
  height: var(--thumb-size);
  border-radius: 50%;
  cursor: grab;
}

.rs-01__thumb {
  position: absolute;
  width: var(--thumb-size);
  height: var(--thumb-size);
  background: #fff;
  border: 3px solid var(--emerald);
  border-radius: 50%;
  top: 50%;
  transform: translateY(-50%) translateX(-50%);
  pointer-events: none;
  box-shadow: 0 0 0 4px var(--emerald-dim), 0 4px 12px rgba(0,0,0,0.4);
  transition: box-shadow 0.2s, transform 0.15s;
}

.rs-01__thumb--active {
  box-shadow: 0 0 0 8px var(--emerald-dim), 0 0 20px var(--emerald-glow);
  transform: translateY(-50%) translateX(-50%) scale(1.15);
}

.rs-01__tooltip {
  position: absolute;
  bottom: calc(100% + 10px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--emerald);
  color: #0a1628;
  font-size: 11px;
  font-weight: 800;
  padding: 3px 7px;
  border-radius: 6px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s;
}

.rs-01__tooltip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 4px solid transparent;
  border-top-color: var(--emerald);
}

.rs-01__thumb--active .rs-01__tooltip {
  opacity: 1;
}

.rs-01__ticks {
  display: flex;
  justify-content: space-between;
  padding: 0 2px;
}

.rs-01__tick {
  font-size: 11px;
  color: var(--muted);
}

.rs-01__results {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.rs-01__count {
  font-size: 13px;
  color: var(--muted);
}

.rs-01__count strong {
  color: var(--emerald);
}

.rs-01__btn {
  background: var(--emerald);
  color: #0a1628;
  border: none;
  padding: 8px 20px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
}

.rs-01__btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px var(--emerald-glow);
}

@media (prefers-reduced-motion: reduce) {
  .rs-01__track-fill {
    transition: none;
  }

  .rs-01__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const lo = document.getElementById('rs-01-lo');
  const hi = document.getElementById('rs-01-hi');
  const fill = document.getElementById('rs-01-fill');
  const thumbLo = document.getElementById('rs-01-thumb-lo');
  const thumbHi = document.getElementById('rs-01-thumb-hi');
  const tipLo = document.getElementById('rs-01-tip-lo');
  const tipHi = document.getElementById('rs-01-tip-hi');
  const minVal = document.getElementById('rs-01-min-val');
  const maxVal = document.getElementById('rs-01-max-val');
  const count = document.getElementById('rs-01-count');

  function pct(v){ return ((v - lo.min)/(lo.max - lo.min))*100; }
  function update(){
    let a = Math.min(+lo.value, +hi.value);
    let b = Math.max(+lo.value, +hi.value);
    if(b - a < 10){ b = a + 10; hi.value = b; }
    fill.style.left = pct(a)+'%';
    fill.style.width = (pct(b)-pct(a))+'%';
    thumbLo.style.left = pct(+lo.value)+'%';
    thumbHi.style.left = pct(+hi.value)+'%';
    tipLo.textContent = '$'+lo.value;
    tipHi.textContent = '$'+hi.value;
    minVal.textContent = a;
    maxVal.textContent = b;
    count.textContent = Math.round(247*(b-a)/200);
  }
  [lo, hi].forEach(inp => {
    inp.addEventListener('input', update);
    inp.addEventListener('mousedown', ()=>{
      const t = inp === lo ? thumbLo : thumbHi;
      t.classList.add('rs-01__thumb--active');
    });
    inp.addEventListener('mouseup', ()=>{
      const t = inp === lo ? thumbLo : thumbHi;
      t.classList.remove('rs-01__thumb--active');
    });
    inp.addEventListener('touchstart', ()=>{
      const t = inp === lo ? thumbLo : thumbHi;
      t.classList.add('rs-01__thumb--active');
    }, {passive:true});
    inp.addEventListener('touchend', ()=>{
      const t = inp === lo ? thumbLo : thumbHi;
      t.classList.remove('rs-01__thumb--active');
    });
  });
  update();
})();
```
