---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/circular-radial-dial-range-input/"
title: "Circular Radial Dial Range Input"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A smart-home thermostat dial with an SVG arc that fills clockwise as temperature rises, a live numeric center display, dynamic ETA calculation, and mode tabs…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Radial Dial Range Input
Source: https://codefronts.com/components/css-range-sliders/circular-radial-dial-range-input/

A smart-home thermostat dial with an SVG arc that fills clockwise as temperature rises, a live numeric center display, dynamic ETA calculation, and mode tabs for Heat, Cool, and Fan settings.
## HTML
```html
<div class="rs-08">
  <div class="rs-08__panel">
    <div class="rs-08__mode-tabs">
      <button class="rs-08__tab active">Heat</button>
      <button class="rs-08__tab">Cool</button>
      <button class="rs-08__tab">Fan</button>
    </div>
    <div class="rs-08__dial-wrap">
      <svg class="rs-08__svg" viewBox="0 0 180 180">
        <defs>
          <linearGradient id="rs-08-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#3b82f6"/>
            <stop offset="100%" stop-color="#f97316"/>
          </linearGradient>
        </defs>
        <circle class="rs-08__track-ring" cx="90" cy="90" r="75"/>
        <circle class="rs-08__fill-ring" id="rs-08-ring" cx="90" cy="90" r="75"/>
      </svg>
      <div class="rs-08__center">
        <div class="rs-08__temp" id="rs-08-temp">22</div>
        <div class="rs-08__unit">°C</div>
        <div class="rs-08__label">Target</div>
      </div>
    </div>
    <div class="rs-08__ticks">
      <span class="rs-08__tick">10°</span>
      <span class="rs-08__tick">20°</span>
      <span class="rs-08__tick">30°</span>
    </div>
    <input class="rs-08__input" type="range" min="10" max="32" value="22" id="rs-08-inp">
    <div class="rs-08__status-row">
      <div class="rs-08__status">
        <div class="rs-08__status-label">Current</div>
        <div class="rs-08__status-val">18°C</div>
      </div>
      <div class="rs-08__status">
        <div class="rs-08__status-label">Humidity</div>
        <div class="rs-08__status-val">64%</div>
      </div>
      <div class="rs-08__status">
        <div class="rs-08__status-label">ETA</div>
        <div class="rs-08__status-val" id="rs-08-eta">24m</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-08,
.rs-08 *,
.rs-08 *::before,
.rs-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-08 ::selection {
  background: #f97316;
  color: #fff;
}

.rs-08 {
  --bg: #0f1117;
  --card: #161b27;
  --border: #1e2d4a;
  --orange: #f97316;
  --orange-dim: rgba(249,115,22,0.2);
  --orange-glow: rgba(249,115,22,0.5);
  --blue: #3b82f6;
  --text: #f1f5f9;
  --muted: #475569;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-08__panel {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 28px;
  padding: 40px 36px;
  max-width: 360px;
  width: 100%;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.rs-08__mode-tabs {
  display: flex;
  background: rgba(255,255,255,0.04);
  border-radius: 10px;
  padding: 3px;
  margin-bottom: 32px;
}

.rs-08__tab {
  flex: 1;
  padding: 7px;
  font-size: 12px;
  font-weight: 600;
  border: none;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  border-radius: 8px;
  transition: background 0.2s, color 0.2s;
}

.rs-08__tab.active {
  background: var(--orange);
  color: #fff;
}

.rs-08__dial-wrap {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto 28px;
}

.rs-08__svg {
  width: 200px;
  height: 200px;
  transform: rotate(-135deg);
}

.rs-08__track-ring {
  fill: none;
  stroke: var(--border);
  stroke-width: 14;
  stroke-linecap: round;
}

.rs-08__fill-ring {
  fill: none;
  stroke: url(#rs-08-grad);
  stroke-width: 14;
  stroke-linecap: round;
  stroke-dasharray: 471;
  stroke-dashoffset: 118;
  transition: stroke-dashoffset 0.08s linear;
  filter: drop-shadow(0 0 6px var(--orange-glow));
}

.rs-08__center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.rs-08__temp {
  font-size: 52px;
  font-weight: 900;
  color: var(--text);
  letter-spacing: -2px;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.rs-08__unit {
  font-size: 18px;
  color: var(--muted);
  font-weight: 400;
}

.rs-08__label {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-top: 6px;
}

.rs-08__ticks {
  display: flex;
  justify-content: space-between;
  padding: 0 8px;
  margin-bottom: 16px;
}

.rs-08__tick {
  font-size: 11px;
  color: var(--muted);
}

.rs-08__input {
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 6px;
  background: var(--border);
  border-radius: 99px;
  outline: none;
  cursor: pointer;
  margin-bottom: 20px;
}

.rs-08__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--orange);
  box-shadow: 0 0 12px var(--orange-glow);
  cursor: grab;
  transition: transform 0.15s;
}

.rs-08__input:active::-webkit-slider-thumb {
  transform: scale(1.2);
  cursor: grabbing;
}

.rs-08__input::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: none;
  background: var(--orange);
  box-shadow: 0 0 12px var(--orange-glow);
}

.rs-08__status-row {
  display: flex;
  gap: 10px;
}

.rs-08__status {
  flex: 1;
  padding: 10px;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
}

.rs-08__status-label {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.rs-08__status-val {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
}

@media (prefers-reduced-motion: reduce) {
  .rs-08__fill-ring {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-08-inp');
  const ring = document.getElementById('rs-08-ring');
  const temp = document.getElementById('rs-08-temp');
  const eta = document.getElementById('rs-08-eta');
  const CIRC = 2*Math.PI*75;
  const ARC = CIRC * 0.75;
  function update(){
    const v = +inp.value;
    const pct = (v - +inp.min) / (+inp.max - +inp.min);
    const offset = CIRC - ARC * pct;
    ring.style.strokeDashoffset = offset;
    temp.textContent = v;
    eta.textContent = Math.abs(v - 18)*3 + 'm';
  }
  inp.addEventListener('input', update);
  document.querySelectorAll('.rs-08__tab').forEach(t => {
    t.addEventListener('click', ()=>{
      document.querySelectorAll('.rs-08__tab').forEach(x=>x.classList.remove('active'));
      t.classList.add('active');
    });
  });
  update();
})();
```
