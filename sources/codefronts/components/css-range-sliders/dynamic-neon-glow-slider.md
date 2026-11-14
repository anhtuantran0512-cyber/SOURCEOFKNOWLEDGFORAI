---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/dynamic-neon-glow-slider/"
title: "Dynamic Neon Glow Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A pitch-black dark-mode slider where a razor-thin track floods with radiant purple-to-cyan gradient light as the glowing neon thumb travels, simulating an…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dynamic Neon Glow Slider
Source: https://codefronts.com/components/css-range-sliders/dynamic-neon-glow-slider/

A pitch-black dark-mode slider where a razor-thin track floods with radiant purple-to-cyan gradient light as the glowing neon thumb travels, simulating an active electrified neon tube.
## HTML
```html
<div class="rs-03">
  <div class="rs-03__box">
    <div class="rs-03__corner rs-03__corner--tl"></div>
    <div class="rs-03__corner rs-03__corner--tr"></div>
    <div class="rs-03__corner rs-03__corner--bl"></div>
    <div class="rs-03__corner rs-03__corner--br"></div>
    <div class="rs-03__top">
      <div class="rs-03__label">Intensity Level</div>
      <div class="rs-03__live">● LIVE</div>
    </div>
    <div class="rs-03__value"><span id="rs-03-val">73</span><span>%</span></div>
    <div class="rs-03__track-wrap">
      <div class="rs-03__track-bg"></div>
      <div class="rs-03__track-fill" id="rs-03-fill" style="width:73%"></div>
      <input class="rs-03__input" type="range" min="0" max="100" value="73" id="rs-03-inp">
    </div>
    <div class="rs-03__ticks">
      <span class="rs-03__tick">0</span>
      <span class="rs-03__tick">25</span>
      <span class="rs-03__tick">50</span>
      <span class="rs-03__tick">75</span>
      <span class="rs-03__tick">100</span>
    </div>
    <div class="rs-03__meter" id="rs-03-meter"></div>
  </div>
</div>
```
## CSS
```css
.rs-03,
.rs-03 *,
.rs-03 *::before,
.rs-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-03 ::selection {
  background: #b400ff;
  color: #fff;
}

.rs-03 {
  --bg: #040408;
  --surface: #0c0c18;
  --purple: #b400ff;
  --cyan: #00f5ff;
  --purple-glow: rgba(180,0,255,0.5);
  --cyan-glow: rgba(0,245,255,0.6);
  --text: #e8e8ff;
  --muted: #555580;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: 'Courier New', monospace;
}

.rs-03__box {
  background: var(--surface);
  border: 1px solid rgba(180,0,255,0.2);
  border-radius: 16px;
  padding: 36px 32px;
  width: 100%;
  max-width: 440px;
  position: relative;
  box-shadow: 0 0 40px rgba(180,0,255,0.08), inset 0 1px 0 rgba(255,255,255,0.05);
}

.rs-03__corner {
  position: absolute;
  width: 12px;
  height: 12px;
  border-color: var(--purple);
  border-style: solid;
  opacity: 0.7;
}

.rs-03__corner--tl {
  top: 10px;
  left: 10px;
  border-width: 2px 0 0 2px;
}

.rs-03__corner--tr {
  top: 10px;
  right: 10px;
  border-width: 2px 2px 0 0;
}

.rs-03__corner--bl {
  bottom: 10px;
  left: 10px;
  border-width: 0 0 2px 2px;
}

.rs-03__corner--br {
  bottom: 10px;
  right: 10px;
  border-width: 0 2px 2px 0;
}

.rs-03__top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 28px;
}

.rs-03__label {
  font-size: 11px;
  letter-spacing: 3px;
  color: var(--muted);
  text-transform: uppercase;
}

.rs-03__live {
  font-size: 11px;
  color: var(--cyan);
  letter-spacing: 2px;
  animation: rs-03-blink 1.4s step-end infinite;
}

@keyframes rs-03-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

.rs-03__value {
  font-size: 72px;
  font-weight: 900;
  letter-spacing: -4px;
  line-height: 1;
  margin-bottom: 32px;
  font-variant-numeric: tabular-nums;
  color: var(--purple);
  text-shadow: 0 0 20px var(--purple-glow), 0 0 60px rgba(180,0,255,0.3);
  transition: text-shadow 0.1s;
}

.rs-03__value span {
  font-size: 28px;
  font-weight: 400;
  color: var(--muted);
  margin-left: 4px;
}

.rs-03__track-wrap {
  position: relative;
  height: 32px;
  display: flex;
  align-items: center;
  margin-bottom: 12px;
}

.rs-03__track-bg {
  position: absolute;
  width: 100%;
  height: 2px;
  background: var(--muted);
  border-radius: 99px;
  opacity: 0.3;
}

.rs-03__track-fill {
  position: absolute;
  height: 2px;
  left: 0;
  background: linear-gradient(90deg, var(--purple), var(--cyan));
  border-radius: 99px;
  box-shadow: 0 0 10px var(--purple-glow), 0 0 30px rgba(180,0,255,0.3);
  transition: width 0.05s;
}

.rs-03__input {
  position: absolute;
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 32px;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
}

.rs-03__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #040408;
  border: 2px solid var(--cyan);
  box-shadow: 0 0 10px var(--cyan-glow), 0 0 30px rgba(0,245,255,0.3);
  transition: box-shadow 0.2s, transform 0.15s;
  cursor: grab;
}

.rs-03__input:active::-webkit-slider-thumb {
  box-shadow: 0 0 20px var(--cyan-glow), 0 0 60px rgba(0,245,255,0.5);
  transform: scale(1.2);
  cursor: grabbing;
}

.rs-03__input::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #040408;
  border: 2px solid var(--cyan);
  box-shadow: 0 0 10px var(--cyan-glow);
  cursor: grab;
}

.rs-03__ticks {
  display: flex;
  justify-content: space-between;
}

.rs-03__tick {
  font-size: 10px;
  color: var(--muted);
}

.rs-03__meter {
  margin-top: 24px;
  display: flex;
  gap: 3px;
}

.rs-03__bar {
  flex: 1;
  height: 4px;
  border-radius: 2px;
  background: rgba(255,255,255,0.06);
  transition: background 0.15s, box-shadow 0.15s;
}

.rs-03__bar.on {
  background: var(--purple);
  box-shadow: 0 0 6px var(--purple-glow);
}

.rs-03__bar.on.hi {
  background: var(--cyan);
  box-shadow: 0 0 6px var(--cyan-glow);
}

@media (prefers-reduced-motion: reduce) {
  .rs-03__live {
    animation: none;
    opacity: 1;
  }

  .rs-03__track-fill,
    .rs-03__bar,
    .rs-03__input::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-03-inp');
  const fill = document.getElementById('rs-03-fill');
  const val = document.getElementById('rs-03-val');
  const meter = document.getElementById('rs-03-meter');
  const BARS = 30;
  for(let i=0;i<BARS;i++){
    const b = document.createElement('div');
    b.className = 'rs-03__bar';
    meter.appendChild(b);
  }
  function update(){
    const v = +inp.value;
    val.textContent = v;
    fill.style.width = v+'%';
    const active = Math.round(v/100*BARS);
    meter.querySelectorAll('.rs-03__bar').forEach((b,i)=>{
      b.classList.toggle('on', i < active);
      b.classList.toggle('hi', i < active && i >= BARS*0.75);
    });
  }
  inp.addEventListener('input', update);
  update();
})();
```
