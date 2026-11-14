---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/skewed-isometric-perspective-slider/"
title: "Skewed Isometric Perspective Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "An innovative slider that appears to lie flat on a tilted isometric desktop plane via CSS 3D transforms, with a grid-line surface, perspective shadow beneath…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skewed Isometric Perspective Slider
Source: https://codefronts.com/components/css-range-sliders/skewed-isometric-perspective-slider/

An innovative slider that appears to lie flat on a tilted isometric desktop plane via CSS 3D transforms, with a grid-line surface, perspective shadow beneath the thumb, and three live metric cards for power, speed, and efficiency.
## HTML
```html
<div class="rs-15">
  <div class="rs-15__stage">
    <div class="rs-15__label-row">
      <div class="rs-15__title">3D Isometric Slider</div>
      <div class="rs-15__val-display">
        <div class="rs-15__val-big"><span id="rs-15-val">65</span>%</div>
        <div class="rs-15__val-label">INTENSITY</div>
      </div>
    </div>
    <div class="rs-15__iso-wrap">
      <div class="rs-15__iso-surface"></div>
      <div class="rs-15__track-container">
        <div class="rs-15__track-outer">
          <div class="rs-15__track-bg">
            <div class="rs-15__track-fill" id="rs-15-fill" style="width:65%"></div>
            <input class="rs-15__input" type="range" min="0" max="100" value="65" id="rs-15-inp">
          </div>
        </div>
        <div class="rs-15__shadow" id="rs-15-shadow" style="width:65%;margin-left:0"></div>
        <div class="rs-15__ticks-iso">
          <span class="rs-15__tick-iso">0</span>
          <span class="rs-15__tick-iso">25</span>
          <span class="rs-15__tick-iso">50</span>
          <span class="rs-15__tick-iso">75</span>
          <span class="rs-15__tick-iso">100</span>
        </div>
      </div>
    </div>
    <div class="rs-15__metrics">
      <div class="rs-15__metric">
        <div class="rs-15__metric-val" id="rs-15-pow">65W</div>
        <div class="rs-15__metric-label">POWER</div>
      </div>
      <div class="rs-15__metric">
        <div class="rs-15__metric-val" id="rs-15-spd">4.2m/s</div>
        <div class="rs-15__metric-label">SPEED</div>
      </div>
      <div class="rs-15__metric">
        <div class="rs-15__metric-val" id="rs-15-eff">A+</div>
        <div class="rs-15__metric-label">EFFICIENCY</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-15,
.rs-15 *,
.rs-15 *::before,
.rs-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-15 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.rs-15 {
  --bg: #0d0d1f;
  --violet: #8b5cf6;
  --violet-glow: rgba(139,92,246,0.5);
  --cyan: #22d3ee;
  --text: #f0f0ff;
  --muted: #555580;
  --grid: rgba(139,92,246,0.12);
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px 40px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  perspective: 800px;
}

.rs-15__stage {
  width: 100%;
  max-width: 460px;
}

.rs-15__label-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 20px;
}

.rs-15__title {
  font-size: 20px;
  font-weight: 800;
  color: var(--text);
}

.rs-15__val-display {
  text-align: right;
}

.rs-15__val-big {
  font-size: 36px;
  font-weight: 900;
  letter-spacing: -1px;
  color: var(--violet);
  text-shadow: 0 0 20px var(--violet-glow);
  font-variant-numeric: tabular-nums;
}

.rs-15__val-label {
  font-size: 11px;
  color: var(--muted);
  letter-spacing: 1px;
}

.rs-15__iso-wrap {
  transform: rotateX(30deg) rotateZ(-10deg);
  transform-style: preserve-3d;
  position: relative;
  padding: 32px 24px;
}

.rs-15__iso-surface {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(139,92,246,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(139,92,246,0.06) 1px, transparent 1px);
  background-size: 24px 24px;
  border: 1px solid rgba(139,92,246,0.2);
  border-radius: 8px;
}

.rs-15__iso-surface::before {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: -8px;
  height: 8px;
  background: rgba(139,92,246,0.12);
  transform: rotateX(-90deg);
  transform-origin: top;
}

.rs-15__track-container {
  position: relative;
  z-index: 2;
}

.rs-15__track-outer {
  background: rgba(0,0,0,0.6);
  border: 1px solid rgba(139,92,246,0.3);
  border-radius: 8px;
  padding: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.05);
}

.rs-15__track-bg {
  height: 10px;
  background: rgba(0,0,0,0.5);
  border-radius: 5px;
  position: relative;
}

.rs-15__track-fill {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  background: linear-gradient(90deg, var(--violet), var(--cyan));
  border-radius: 5px;
  box-shadow: 0 0 20px var(--violet-glow);
  transition: width 0.05s;
}

.rs-15__input {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  -webkit-appearance: none;
  appearance: none;
  background: transparent;
  cursor: ew-resize;
  outline: none;
  z-index: 2;
}

.rs-15__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 30px;
  background: linear-gradient(180deg, #c4b5fd, #8b5cf6);
  border: none;
  border-radius: 4px 4px 0 0;
  box-shadow: 0 -4px 12px var(--violet-glow), 0 4px 0 rgba(0,0,0,0.4);
  cursor: ew-resize;
  transition: transform 0.15s;
}

.rs-15__input:active::-webkit-slider-thumb {
  transform: scaleY(1.1);
}

.rs-15__input::-moz-range-thumb {
  width: 24px;
  height: 30px;
  border-radius: 4px;
  border: none;
  background: var(--violet);
  cursor: ew-resize;
}

.rs-15__shadow {
  height: 4px;
  background: radial-gradient(ellipse at center, rgba(139,92,246,0.4) 0%, transparent 70%);
  margin-top: 4px;
  transition: width 0.05s, margin-left 0.05s;
  position: relative;
}

.rs-15__ticks-iso {
  display: flex;
  justify-content: space-between;
  margin-top: 14px;
}

.rs-15__tick-iso {
  font-size: 10px;
  color: var(--muted);
}

.rs-15__metrics {
  display: flex;
  gap: 12px;
  margin-top: 20px;
  transform: rotateX(0deg);
}

.rs-15__metric {
  flex: 1;
  background: rgba(139,92,246,0.08);
  border: 1px solid rgba(139,92,246,0.2);
  border-radius: 10px;
  padding: 12px;
  text-align: center;
}

.rs-15__metric-val {
  font-size: 18px;
  font-weight: 800;
  color: var(--violet);
}

.rs-15__metric-label {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 1px;
}

@media (prefers-reduced-motion: reduce) {
  .rs-15__track-fill,
    .rs-15__shadow {
    transition: none;
  }

  .rs-15__iso-wrap {
    transform: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-15-inp');
  const fill = document.getElementById('rs-15-fill');
  const valEl = document.getElementById('rs-15-val');
  const pow = document.getElementById('rs-15-pow');
  const spd = document.getElementById('rs-15-spd');
  const eff = document.getElementById('rs-15-eff');
  const grades = ['D','C','C+','B','B+','A','A+'];
  function update(){
    const v = +inp.value;
    fill.style.width = v+'%';
    valEl.textContent = v;
    pow.textContent = v+'W';
    spd.textContent = (v/100*8).toFixed(1)+'m/s';
    eff.textContent = grades[Math.floor(v/100*6)];
  }
  inp.addEventListener('input', update);
  update();
})();
```
