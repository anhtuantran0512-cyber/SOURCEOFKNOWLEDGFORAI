---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/minimalist-thick-block-interface/"
title: "Minimalist Thick-Block Interface"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A bold brutalist-inspired UI where the slider track is a 32px-tall rectangular block, the thumb is an oversized red square that fills the track height…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Thick-Block Interface
Source: https://codefronts.com/components/css-range-sliders/minimalist-thick-block-interface/

A bold brutalist-inspired UI where the slider track is a 32px-tall rectangular block, the thumb is an oversized red square that fills the track height completely, and preset quick-set buttons snap the value with keyboard-native feel.
## HTML
```html
<div class="rs-11">
  <div class="rs-11__canvas">
    <div class="rs-11__topbar">
      <span>CONFIG.SYS</span>
      <div class="rs-11__dot-row">
        <div class="rs-11__dot"></div>
        <div class="rs-11__dot"></div>
        <div class="rs-11__dot"></div>
      </div>
    </div>
    <div class="rs-11__body">
      <div class="rs-11__val-display">
        <div class="rs-11__val-num" id="rs-11-num">64</div>
        <div class="rs-11__val-label">Allocation Units</div>
      </div>
      <div class="rs-11__track-wrap">
        <div class="rs-11__track-fill" id="rs-11-fill" style="width:64%"></div>
        <input class="rs-11__input" type="range" min="0" max="100" value="64" id="rs-11-inp">
      </div>
      <div class="rs-11__marks">
        <span class="rs-11__mark">0</span>
        <span class="rs-11__mark">25</span>
        <span class="rs-11__mark">50</span>
        <span class="rs-11__mark">75</span>
        <span class="rs-11__mark">100</span>
      </div>
      <div class="rs-11__controls">
        <button class="rs-11__ctl-btn" data-val="0">Reset</button>
        <button class="rs-11__ctl-btn" data-val="50">Half</button>
        <button class="rs-11__ctl-btn active" data-val="64">Default</button>
        <button class="rs-11__ctl-btn" data-val="100">Max</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-11,
.rs-11 *,
.rs-11 *::before,
.rs-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-11 ::selection {
  background: #000;
  color: #fff;
}

.rs-11 {
  --bg: #f5f0e8;
  --card: #ede8dd;
  --black: #111111;
  --red: #d63427;
  --grey: #ccc6bb;
  --text: #111111;
  --muted: #888;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: 'Courier New', 'SF Mono', monospace;
}

.rs-11__canvas {
  background: var(--card);
  border: 3px solid var(--black);
  max-width: 440px;
  width: 100%;
  padding: 0;
  box-shadow: 6px 6px 0 var(--black);
}

.rs-11__topbar {
  background: var(--black);
  color: #fff;
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.rs-11__dot-row {
  display: flex;
  gap: 6px;
}

.rs-11__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #fff;
  opacity: 0.3;
}

.rs-11__body {
  padding: 32px;
}

.rs-11__val-display {
  margin-bottom: 24px;
}

.rs-11__val-num {
  font-size: 80px;
  font-weight: 900;
  color: var(--black);
  letter-spacing: -6px;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.rs-11__val-label {
  font-size: 12px;
  color: var(--muted);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-top: 4px;
}

.rs-11__track-wrap {
  position: relative;
  height: 32px;
  margin-bottom: 8px;
  border: 2px solid var(--black);
  background: var(--grey);
}

.rs-11__track-fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  background: var(--black);
  transition: width 0.04s;
}

.rs-11__input {
  position: absolute;
  inset: 0;
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
  height: 100%;
  margin: 0;
}

.rs-11__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 28px;
  height: 32px;
  background: var(--red);
  border: none;
  border-right: 2px solid var(--black);
  cursor: ew-resize;
  transition: background 0.15s;
}

.rs-11__input:hover::-webkit-slider-thumb {
  background: #ff3d30;
}

.rs-11__input::-moz-range-thumb {
  width: 28px;
  height: 32px;
  border-radius: 0;
  background: var(--red);
  border: none;
  cursor: ew-resize;
}

.rs-11__marks {
  display: flex;
  justify-content: space-between;
  margin-bottom: 28px;
}

.rs-11__mark {
  font-size: 10px;
  color: var(--muted);
  position: relative;
}

.rs-11__mark::before {
  content: '|';
  display: block;
  text-align: center;
  margin-bottom: 2px;
  color: var(--black);
  font-size: 12px;
}

.rs-11__controls {
  display: flex;
  gap: 0;
}

.rs-11__ctl-btn {
  flex: 1;
  padding: 12px;
  background: transparent;
  border: 2px solid var(--black);
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  color: var(--black);
  transition: background 0.15s, color 0.15s;
}

.rs-11__ctl-btn + .rs-11__ctl-btn {
  border-left: none;
}

.rs-11__ctl-btn:hover {
  background: var(--black);
  color: #fff;
}

.rs-11__ctl-btn.active {
  background: var(--black);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .rs-11__track-fill {
    transition: none;
  }

  .rs-11__ctl-btn {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-11-inp');
  const fill = document.getElementById('rs-11-fill');
  const num = document.getElementById('rs-11-num');
  function update(){
    fill.style.width = inp.value+'%';
    num.textContent = inp.value;
  }
  inp.addEventListener('input', update);
  document.querySelectorAll('.rs-11__ctl-btn').forEach(btn => {
    btn.addEventListener('click', ()=>{
      inp.value = btn.dataset.val;
      update();
      document.querySelectorAll('.rs-11__ctl-btn').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
  update();
})();
```
