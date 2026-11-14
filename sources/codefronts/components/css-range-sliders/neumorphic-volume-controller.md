---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/neumorphic-volume-controller/"
title: "Neumorphic Volume Controller"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A soft neumorphic audio panel with an inset track groove, a heavy extruded thumb, and a live bar-graph visualizer that responds to every drag with ripple…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Volume Controller
Source: https://codefronts.com/components/css-range-sliders/neumorphic-volume-controller/

A soft neumorphic audio panel with an inset track groove, a heavy extruded thumb, and a live bar-graph visualizer that responds to every drag with ripple glow on the active thumb.
## HTML
```html
<div class="rs-02">
  <div class="rs-02__panel">
    <div class="rs-02__icon-row">
      <button class="rs-02__icon-btn" aria-label="Previous">
        <svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <span class="rs-02__label">Volume Control</span>
      <button class="rs-02__icon-btn" aria-label="Next">
        <svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
    <div class="rs-02__track-wrap">
      <input class="rs-02__input" type="range" min="0" max="100" value="60" id="rs-02-vol">
    </div>
    <div class="rs-02__value-row">
      <div class="rs-02__volume-num"><span id="rs-02-num">60</span><span>%</span></div>
      <div class="rs-02__dots" id="rs-02-dots">
        <!-- built by JS -->
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-02,
.rs-02 *,
.rs-02 *::before,
.rs-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-02 ::selection {
  background: #6c63ff;
  color: #fff;
}

.rs-02 {
  --bg: #e0e5ec;
  --shadow-dark: #b8bec7;
  --shadow-light: #ffffff;
  --accent: #6c63ff;
  --accent-glow: rgba(108,99,255,0.35);
  --text: #3d4a5c;
  --muted: #8a9bb5;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-02__panel {
  background: var(--bg);
  border-radius: 28px;
  padding: 40px 36px;
  width: 100%;
  max-width: 380px;
  box-shadow: 10px 10px 30px var(--shadow-dark), -10px -10px 30px var(--shadow-light);
}

.rs-02__icon-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 32px;
}

.rs-02__icon-btn {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: var(--bg);
  box-shadow: 5px 5px 14px var(--shadow-dark), -5px -5px 14px var(--shadow-light);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: box-shadow 0.2s;
  border: none;
  color: var(--muted);
}

.rs-02__icon-btn:active {
  box-shadow: 3px 3px 8px var(--shadow-dark), -3px -3px 8px var(--shadow-light), inset 3px 3px 8px var(--shadow-dark), inset -3px -3px 8px var(--shadow-light);
}

.rs-02__icon-btn svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
}

.rs-02__label {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 0.5px;
}

.rs-02__track-wrap {
  background: var(--bg);
  border-radius: 16px;
  padding: 20px 18px;
  box-shadow: inset 5px 5px 14px var(--shadow-dark), inset -5px -5px 14px var(--shadow-light);
  margin-bottom: 24px;
  position: relative;
}

.rs-02__input {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 8px;
  background: transparent;
  position: relative;
  z-index: 2;
  cursor: pointer;
  outline: none;
}

.rs-02__input::-webkit-slider-runnable-track {
  height: 8px;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--accent) var(--pct,60%), var(--shadow-dark) var(--pct,60%));
}

.rs-02__input::-moz-range-track {
  height: 8px;
  border-radius: 99px;
  background: var(--shadow-dark);
}

.rs-02__input::-moz-range-progress {
  height: 8px;
  border-radius: 99px;
  background: var(--accent);
}

.rs-02__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--bg);
  box-shadow: 5px 5px 14px var(--shadow-dark), -5px -5px 14px var(--shadow-light);
  margin-top: -12px;
  position: relative;
  transition: box-shadow 0.2s;
}

.rs-02__input:active::-webkit-slider-thumb {
  box-shadow: 3px 3px 8px var(--shadow-dark), -3px -3px 8px var(--shadow-light), 0 0 0 4px var(--accent-glow);
}

.rs-02__input::-moz-range-thumb {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: var(--bg);
  box-shadow: 5px 5px 14px var(--shadow-dark), -5px -5px 14px var(--shadow-light);
}

.rs-02__value-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.rs-02__volume-num {
  font-size: 42px;
  font-weight: 900;
  color: var(--text);
  letter-spacing: -2px;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.rs-02__volume-num span {
  font-size: 16px;
  font-weight: 500;
  color: var(--muted);
}

.rs-02__dots {
  display: flex;
  gap: 5px;
  align-items: flex-end;
}

.rs-02__dot {
  width: 6px;
  border-radius: 3px;
  background: var(--shadow-dark);
  transition: background 0.3s, height 0.3s;
}

.rs-02__dot.active {
  background: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .rs-02__dot {
    transition: none;
  }

  .rs-02__input::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-02-vol');
  const num = document.getElementById('rs-02-num');
  const dots = document.getElementById('rs-02-dots');
  const BARS = 12;
  const heights = [10,14,18,22,28,34,28,22,18,14,10,8];
  for(let i=0;i<BARS;i++){
    const d = document.createElement('div');
    d.className = 'rs-02__dot';
    d.style.height = heights[i]+'px';
    dots.appendChild(d);
  }
  function update(){
    const v = +inp.value;
    num.textContent = v;
    inp.style.setProperty('--pct', v+'%');
    const active = Math.round(v/100*BARS);
    dots.querySelectorAll('.rs-02__dot').forEach((d,i)=>{
      d.classList.toggle('active', i < active);
    });
  }
  inp.addEventListener('input', update);
  update();
})();
```
