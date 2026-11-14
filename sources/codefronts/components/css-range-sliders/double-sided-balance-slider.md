---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/double-sided-balance-slider/"
title: "Double-Sided Balance Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "An audio panning control centered at zero where the fill extends left or right from the midpoint in opposing channel colors, with a live bar graph…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Double-Sided Balance Slider
Source: https://codefronts.com/components/css-range-sliders/double-sided-balance-slider/

An audio panning control centered at zero where the fill extends left or right from the midpoint in opposing channel colors, with a live bar graph visualizer, percentage readouts per channel, and a center reset button.
## HTML
```html
<div class="rs-13">
  <div class="rs-13__card">
    <div class="rs-13__header">
      <div class="rs-13__title">Audio Pan Control</div>
      <div class="rs-13__sub">Drag from center to pan left or right</div>
    </div>
    <div class="rs-13__channels">
      <div class="rs-13__chan">
        <div class="rs-13__chan-name">Left</div>
        <div class="rs-13__chan-pct" id="rs-13-left" style="color:var(--left)">50%</div>
      </div>
      <div class="rs-13__center-indicator">
        <div class="rs-13__center-dot" id="rs-13-cdot"></div>
        <div class="rs-13__center-label">C</div>
      </div>
      <div class="rs-13__chan">
        <div class="rs-13__chan-name">Right</div>
        <div class="rs-13__chan-pct" id="rs-13-right" style="color:var(--right)">50%</div>
      </div>
    </div>
    <div class="rs-13__track-wrap">
      <div class="rs-13__track-bg"></div>
      <div class="rs-13__center-line"></div>
      <div class="rs-13__left-fill" id="rs-13-lf" style="width:0%"></div>
      <div class="rs-13__right-fill" id="rs-13-rf" style="width:0%"></div>
      <input class="rs-13__input" type="range" min="-100" max="100" value="0" id="rs-13-inp">
    </div>
    <div class="rs-13__labels">
      <span class="rs-13__side-label" style="color:var(--left)">◀ L</span>
      <span class="rs-13__side-label" style="color:var(--right)">R ▶</span>
    </div>
    <div class="rs-13__vis" id="rs-13-vis"></div>
    <button class="rs-13__reset-btn" id="rs-13-reset">⊙ Reset to Center</button>
  </div>
</div>
```
## CSS
```css
.rs-13,
.rs-13 *,
.rs-13 *::before,
.rs-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-13 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.rs-13 {
  --bg: #0a0f1e;
  --card: #0f1729;
  --border: #1a2744;
  --left: #0ea5e9;
  --right: #f43f5e;
  --center: #a3e635;
  --text: #e2e8f0;
  --muted: #475569;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-13__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

.rs-13__header {
  text-align: center;
  margin-bottom: 32px;
}

.rs-13__title {
  font-size: 18px;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.rs-13__sub {
  font-size: 13px;
  color: var(--muted);
}

.rs-13__channels {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.rs-13__chan {
  text-align: center;
}

.rs-13__chan-name {
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 4px;
}

.rs-13__chan-pct {
  font-size: 28px;
  font-weight: 900;
  letter-spacing: -1px;
  font-variant-numeric: tabular-nums;
}

.rs-13__center-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.rs-13__center-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--center);
  transition: opacity 0.3s;
  box-shadow: 0 0 8px var(--center);
}

.rs-13__center-label {
  font-size: 10px;
  color: var(--center);
  font-weight: 600;
  letter-spacing: 1px;
}

.rs-13__track-wrap {
  position: relative;
  height: 48px;
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.rs-13__track-bg {
  position: absolute;
  width: 100%;
  height: 8px;
  background: var(--border);
  border-radius: 99px;
}

.rs-13__center-line {
  position: absolute;
  left: 50%;
  width: 2px;
  height: 20px;
  background: var(--center);
  transform: translateX(-50%);
  opacity: 0.5;
}

.rs-13__left-fill {
  position: absolute;
  right: 50%;
  height: 8px;
  background: var(--left);
  border-radius: 99px 0 0 99px;
  transition: width 0.05s;
  box-shadow: 0 0 12px rgba(14,165,233,0.4);
}

.rs-13__right-fill {
  position: absolute;
  left: 50%;
  height: 8px;
  background: var(--right);
  border-radius: 0 99px 99px 0;
  transition: width 0.05s;
  box-shadow: 0 0 12px rgba(244,63,94,0.4);
}

.rs-13__input {
  position: absolute;
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 48px;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
}

.rs-13__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #1a2744;
  border: 3px solid #e2e8f0;
  box-shadow: 0 4px 16px rgba(0,0,0,0.5);
  cursor: grab;
  transition: border-color 0.3s, transform 0.15s;
}

.rs-13__input:active::-webkit-slider-thumb {
  transform: scale(1.15);
  cursor: grabbing;
}

.rs-13__input::-moz-range-thumb {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 3px solid #e2e8f0;
  background: #1a2744;
  cursor: grab;
}

.rs-13__labels {
  display: flex;
  justify-content: space-between;
  margin-bottom: 28px;
}

.rs-13__side-label {
  font-size: 11px;
  font-weight: 600;
}

.rs-13__vis {
  display: flex;
  gap: 3px;
  height: 60px;
  align-items: flex-end;
}

.rs-13__vis-bar {
  flex: 1;
  border-radius: 3px 3px 0 0;
  transition: height 0.15s, background 0.3s;
}

.rs-13__divider {
  width: 2px;
  background: var(--center);
  height: 100%;
  flex-shrink: 0;
  opacity: 0.3;
}

.rs-13__reset-btn {
  display: block;
  width: 100%;
  margin-top: 20px;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 12px;
  font-weight: 600;
  padding: 10px;
  border-radius: 10px;
  cursor: pointer;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: border-color 0.2s, color 0.2s;
}

.rs-13__reset-btn:hover {
  border-color: var(--center);
  color: var(--center);
}

@media (prefers-reduced-motion: reduce) {
  .rs-13__left-fill,
    .rs-13__right-fill,
    .rs-13__vis-bar {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-13-inp');
  const leftPct = document.getElementById('rs-13-left');
  const rightPct = document.getElementById('rs-13-right');
  const lf = document.getElementById('rs-13-lf');
  const rf = document.getElementById('rs-13-rf');
  const cdot = document.getElementById('rs-13-cdot');
  const vis = document.getElementById('rs-13-vis');
  const BARS = 24;
  for(let i=0;i<BARS;i++){
    const b = document.createElement('div');
    b.className = 'rs-13__vis-bar';
    vis.appendChild(b);
    if(i===BARS/2-1){ const d=document.createElement('div'); d.className='rs-13__divider'; vis.appendChild(d); }
  }
  function update(){
    const v = +inp.value; // -100 to 100
    const absV = Math.abs(v);
    const pct = absV/2; // 0-50% of track
    if(v<0){ lf.style.width=pct+'%'; rf.style.width='0%'; }
    else if(v>0){ rf.style.width=pct+'%'; lf.style.width='0%'; }
    else { lf.style.width='0%'; rf.style.width='0%'; }
    cdot.style.opacity = v===0 ? 1 : 0.3;
    const l = Math.round(50 - v/2);
    const r = Math.round(50 + v/2);
    leftPct.textContent = l+'%';
    rightPct.textContent = r+'%';
    // Update vis bars
    const bars = vis.querySelectorAll('.rs-13__vis-bar');
    bars.forEach((bar,i)=>{
      const isLeft = i < BARS/2;
      const distFromCenter = isLeft ? (BARS/2 - 1 - i) : (i - BARS/2);
      let h;
      if(v < 0 && isLeft){
        h = 10 + (distFromCenter/((BARS/2)-1))*absV*0.5;
      } else if(v > 0 && !isLeft){
        h = 10 + (distFromCenter/((BARS/2)-1))*absV*0.5;
      } else {
        h = 10 + (1-distFromCenter/((BARS/2)))*20;
      }
      bar.style.height = Math.min(60, h)+'px';
      bar.style.background = isLeft ? 'var(--left)' : 'var(--right)';
      bar.style.opacity = 0.3 + (h/60)*0.7;
    });
  }
  inp.addEventListener('input', update);
  document.getElementById('rs-13-reset').addEventListener('click', ()=>{ inp.value=0; update(); });
  update();
})();
```
