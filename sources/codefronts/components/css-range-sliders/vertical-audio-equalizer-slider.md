---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/vertical-audio-equalizer-slider/"
title: "Vertical Audio Equalizer Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A 10-band mixing console equalizer with copper-toned vertical pill sliders sitting in inset steel grooves, per-channel dB readouts, and one-click preset…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Audio Equalizer Slider
Source: https://codefronts.com/components/css-range-sliders/vertical-audio-equalizer-slider/

A 10-band mixing console equalizer with copper-toned vertical pill sliders sitting in inset steel grooves, per-channel dB readouts, and one-click preset buttons for Flat, Bass Boost, Treble, and Vocal modes.
## HTML
```html
<div class="rs-07">
  <div class="rs-07__console">
    <div class="rs-07__header">
      <div class="rs-07__title">Equalizer</div>
      <div class="rs-07__leds">
        <div class="rs-07__led"></div>
        <div class="rs-07__led"></div>
        <div class="rs-07__led"></div>
      </div>
    </div>
    <div class="rs-07__eq-row" id="rs-07-row"></div>
    <div class="rs-07__presets">
      <button class="rs-07__preset active" data-preset="flat">Flat</button>
      <button class="rs-07__preset" data-preset="bass">Bass Boost</button>
      <button class="rs-07__preset" data-preset="treble">Treble</button>
      <button class="rs-07__preset" data-preset="vocal">Vocal</button>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-07,
.rs-07 *,
.rs-07 *::before,
.rs-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-07 ::selection {
  background: #b87333;
  color: #fff;
}

.rs-07 {
  --bg: #111318;
  --panel: #1a1d24;
  --border: #2d3240;
  --copper: #b87333;
  --copper-lit: #d4925a;
  --steel: #4a5568;
  --text: #e2e8f0;
  --muted: #64748b;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-07__console {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 28px 32px;
  max-width: 480px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.6);
}

.rs-07__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
}

.rs-07__title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 2px;
  text-transform: uppercase;
}

.rs-07__leds {
  display: flex;
  gap: 5px;
}

.rs-07__led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.rs-07__led:nth-child(1) {
  background: #ff5f57;
  box-shadow: 0 0 6px #ff5f57;
}

.rs-07__led:nth-child(2) {
  background: #febc2e;
  box-shadow: 0 0 6px #febc2e;
}

.rs-07__led:nth-child(3) {
  background: #28c840;
  box-shadow: 0 0 6px #28c840;
}

.rs-07__eq-row {
  display: flex;
  gap: 0;
  justify-content: space-around;
  align-items: flex-end;
  height: 200px;
  margin-bottom: 16px;
}

.rs-07__channel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  height: 100%;
}

.rs-07__slider-wrap {
  position: relative;
  height: 160px;
  width: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.rs-07__groove {
  position: absolute;
  width: 6px;
  height: 100%;
  background: linear-gradient(180deg, #2d3240 0%, #1a1d24 100%);
  border-radius: 3px;
  box-shadow: inset 2px 2px 4px rgba(0,0,0,0.6), inset -1px -1px 3px rgba(255,255,255,0.04);
}

.rs-07__vert-input {
  -webkit-appearance: slider-vertical;
  writing-mode: vertical-lr;
  direction: rtl;
  appearance: none;
  width: 32px;
  height: 160px;
  background: transparent;
  outline: none;
  cursor: pointer;
  position: relative;
  z-index: 2;
}

.rs-07__vert-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 30px;
  height: 18px;
  background: linear-gradient(180deg, #c8a07a 0%, #8b5e3c 50%, #c8a07a 100%);
  border-radius: 4px;
  border: 1px solid rgba(255,255,255,0.15);
  box-shadow: 0 2px 8px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.2);
  position: relative;
  cursor: grab;
  transition: box-shadow 0.15s;
}

.rs-07__vert-input::-webkit-slider-thumb::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 20%;
  right: 20%;
  height: 2px;
  background: rgba(0,0,0,0.4);
  transform: translateY(-50%);
}

.rs-07__vert-input:active::-webkit-slider-thumb {
  box-shadow: 0 0 0 4px rgba(184,115,51,0.3), 0 2px 8px rgba(0,0,0,0.5);
  cursor: grabbing;
}

.rs-07__vert-input::-moz-range-thumb {
  width: 30px;
  height: 18px;
  border-radius: 4px;
  background: linear-gradient(180deg, #c8a07a 0%, #8b5e3c 50%, #c8a07a 100%);
  border: 1px solid rgba(255,255,255,0.15);
  cursor: grab;
}

.rs-07__chan-label {
  font-size: 10px;
  font-weight: 600;
  color: var(--copper);
  letter-spacing: 1px;
  text-transform: uppercase;
}

.rs-07__chan-val {
  font-size: 10px;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-width: 28px;
  text-align: center;
}

.rs-07__presets {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  padding-top: 16px;
  border-top: 1px solid var(--border);
}

.rs-07__preset {
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
  padding: 5px 12px;
  border-radius: 20px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}

.rs-07__preset:hover,
.rs-07__preset.active {
  border-color: var(--copper);
  color: var(--copper);
  background: rgba(184,115,51,0.1);
}

@media (prefers-reduced-motion: reduce) {
  .rs-07__preset {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const channels = [
    {label:'32', val:50}, {label:'64', val:60}, {label:'125', val:70},
    {label:'250', val:65}, {label:'500', val:50}, {label:'1K', val:55},
    {label:'2K', val:60}, {label:'4K', val:58}, {label:'8K', val:50}, {label:'16K', val:45}
  ];
  const presets = {
    flat: [50,50,50,50,50,50,50,50,50,50],
    bass: [80,78,72,65,55,48,44,42,40,38],
    treble: [40,40,42,44,50,58,68,75,78,80],
    vocal: [38,42,50,65,72,70,65,55,48,42],
  };
  const row = document.getElementById('rs-07-row');
  const sliders = [];
  channels.forEach((ch, i) => {
    const col = document.createElement('div');
    col.className = 'rs-07__channel';
    const valEl = document.createElement('div');
    valEl.className = 'rs-07__chan-val';
    valEl.textContent = (ch.val - 50 >= 0 ? '+' : '') + (ch.val - 50);
    const wrap = document.createElement('div');
    wrap.className = 'rs-07__slider-wrap';
    const groove = document.createElement('div');
    groove.className = 'rs-07__groove';
    const inp = document.createElement('input');
    inp.type = 'range'; inp.min = 0; inp.max = 100; inp.value = ch.val;
    inp.className = 'rs-07__vert-input';
    inp.setAttribute('orient','vertical');
    inp.addEventListener('input', () => {
      valEl.textContent = (+inp.value - 50 >= 0 ? '+' : '') + (+inp.value - 50);
    });
    wrap.appendChild(groove); wrap.appendChild(inp);
    const label = document.createElement('div');
    label.className = 'rs-07__chan-label';
    label.textContent = ch.label;
    col.appendChild(valEl); col.appendChild(wrap); col.appendChild(label);
    row.appendChild(col);
    sliders.push(inp);
  });
  document.querySelectorAll('.rs-07__preset').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.rs-07__preset').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const vals = presets[btn.dataset.preset];
      sliders.forEach((s, i) => {
        s.value = vals[i];
        s.dispatchEvent(new Event('input'));
      });
    });
  });
})();
```
