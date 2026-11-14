---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/glassmorphism-translucent-slider/"
title: "Glassmorphism Translucent Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "An RGBA color mixer with four frosted-glass slider tracks — red, green, blue, and opacity — over a rich multi-color radial gradient background, with a live…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Translucent Slider
Source: https://codefronts.com/components/css-range-sliders/glassmorphism-translucent-slider/

An RGBA color mixer with four frosted-glass slider tracks — red, green, blue, and opacity — over a rich multi-color radial gradient background, with a live color swatch and hex/rgba code readout.
## HTML
```html
<div class="rs-16">
  <div class="rs-16__glass-card">
    <div class="rs-16__top">
      <div>
        <div class="rs-16__title">Color Mixer</div>
        <div class="rs-16__sub">Glassmorphism RGBA controller</div>
      </div>
      <div class="rs-16__toggle">
        <button class="rs-16__toggle-btn active">RGBA</button>
        <button class="rs-16__toggle-btn">HSL</button>
      </div>
    </div>
    <div class="rs-16__controls">
      <div class="rs-16__row">
        <div class="rs-16__row-header">
          <span class="rs-16__row-name">Red</span>
          <span class="rs-16__row-val" id="rs-16-rv">180</span>
        </div>
        <div class="rs-16__track-glass">
          <div class="rs-16__track-inner">
            <div class="rs-16__track-fill rs-16__track-fill--r" id="rs-16-rf" style="width:70.6%"></div>
            <input class="rs-16__glass-input" type="range" min="0" max="255" value="180" id="rs-16-r">
          </div>
        </div>
      </div>
      <div class="rs-16__row">
        <div class="rs-16__row-header">
          <span class="rs-16__row-name">Green</span>
          <span class="rs-16__row-val" id="rs-16-gv">120</span>
        </div>
        <div class="rs-16__track-glass">
          <div class="rs-16__track-inner">
            <div class="rs-16__track-fill rs-16__track-fill--g" id="rs-16-gf" style="width:47.1%"></div>
            <input class="rs-16__glass-input" type="range" min="0" max="255" value="120" id="rs-16-g">
          </div>
        </div>
      </div>
      <div class="rs-16__row">
        <div class="rs-16__row-header">
          <span class="rs-16__row-name">Blue</span>
          <span class="rs-16__row-val" id="rs-16-bv">240</span>
        </div>
        <div class="rs-16__track-glass">
          <div class="rs-16__track-inner">
            <div class="rs-16__track-fill rs-16__track-fill--b" id="rs-16-bf" style="width:94.1%"></div>
            <input class="rs-16__glass-input" type="range" min="0" max="255" value="240" id="rs-16-b">
          </div>
        </div>
      </div>
      <div class="rs-16__row">
        <div class="rs-16__row-header">
          <span class="rs-16__row-name">Opacity</span>
          <span class="rs-16__row-val" id="rs-16-av">85%</span>
        </div>
        <div class="rs-16__track-glass">
          <div class="rs-16__track-inner">
            <div class="rs-16__track-fill rs-16__track-fill--a" id="rs-16-af" style="width:85%"></div>
            <input class="rs-16__glass-input" type="range" min="0" max="100" value="85" id="rs-16-a">
          </div>
        </div>
      </div>
    </div>
    <div class="rs-16__preview">
      <div class="rs-16__swatch" id="rs-16-swatch"></div>
      <div class="rs-16__preview-text">
        <div class="rs-16__hex" id="rs-16-hex">#B478F0</div>
        <div class="rs-16__rgba" id="rs-16-rgba">rgba(180, 120, 240, 0.85)</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-16,
.rs-16 *,
.rs-16 *::before,
.rs-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-16 ::selection {
  background: rgba(255,255,255,0.4);
  color: #fff;
}

.rs-16 {
  --blur: blur(16px);
  --glass: rgba(255,255,255,0.08);
  --glass-border: rgba(255,255,255,0.2);
  --glass-strong: rgba(255,255,255,0.15);
  --text: #ffffff;
  --muted: rgba(255,255,255,0.5);
  background: radial-gradient(ellipse at 20% 30%, #7c3aed 0%, transparent 50%), radial-gradient(ellipse at 80% 20%, #0891b2 0%, transparent 50%), radial-gradient(ellipse at 60% 80%, #be185d 0%, transparent 50%), radial-gradient(ellipse at 10% 80%, #059669 0%, transparent 50%), #0f0f1a;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-16__glass-card {
  background: var(--glass);
  backdrop-filter: var(--blur);
  -webkit-backdrop-filter: var(--blur);
  border: 1px solid var(--glass-border);
  border-radius: 28px;
  padding: 36px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.2);
}

.rs-16__top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 28px;
}

.rs-16__title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.rs-16__sub {
  font-size: 12px;
  color: var(--muted);
}

.rs-16__toggle {
  display: flex;
  gap: 0;
  background: rgba(0,0,0,0.2);
  border-radius: 10px;
  padding: 2px;
  border: 1px solid var(--glass-border);
}

.rs-16__toggle-btn {
  background: transparent;
  border: none;
  color: var(--muted);
  font-size: 11px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
}

.rs-16__toggle-btn.active {
  background: var(--glass-strong);
  color: var(--text);
}

.rs-16__controls {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.rs-16__row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rs-16__row-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.rs-16__row-name {
  font-size: 12px;
  color: var(--muted);
  font-weight: 500;
}

.rs-16__row-val {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  font-variant-numeric: tabular-nums;
}

.rs-16__track-glass {
  background: rgba(0,0,0,0.25);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 99px;
  padding: 3px;
  position: relative;
  height: 24px;
  display: flex;
  align-items: center;
}

.rs-16__track-inner {
  position: relative;
  width: 100%;
  height: 100%;
}

.rs-16__track-fill {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  border-radius: 99px;
  transition: width 0.05s;
}

.rs-16__track-fill--r {
  background: linear-gradient(90deg, rgba(239,68,68,0.7), rgba(239,68,68,0.9));
  box-shadow: 0 0 12px rgba(239,68,68,0.4);
}

.rs-16__track-fill--g {
  background: linear-gradient(90deg, rgba(34,197,94,0.7), rgba(34,197,94,0.9));
  box-shadow: 0 0 12px rgba(34,197,94,0.4);
}

.rs-16__track-fill--b {
  background: linear-gradient(90deg, rgba(59,130,246,0.7), rgba(59,130,246,0.9));
  box-shadow: 0 0 12px rgba(59,130,246,0.4);
}

.rs-16__track-fill--a {
  background: linear-gradient(90deg, rgba(255,255,255,0.3), rgba(255,255,255,0.7));
  box-shadow: 0 0 8px rgba(255,255,255,0.2);
}

.rs-16__glass-input {
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
}

.rs-16__glass-input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1.5px solid rgba(255,255,255,0.6);
  box-shadow: 0 4px 16px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.4);
  cursor: grab;
  transition: transform 0.15s, box-shadow 0.15s;
}

.rs-16__glass-input:active::-webkit-slider-thumb {
  transform: scale(1.2);
  box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.5), 0 0 0 4px rgba(255,255,255,0.1);
  cursor: grabbing;
}

.rs-16__glass-input::-moz-range-thumb {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  border: 1.5px solid rgba(255,255,255,0.6);
  cursor: grab;
}

.rs-16__preview {
  margin-top: 24px;
  background: rgba(0,0,0,0.2);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 16px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.rs-16__swatch {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  border: 1px solid var(--glass-border);
  flex-shrink: 0;
  transition: background 0.05s;
  box-shadow: 0 4px 16px rgba(0,0,0,0.3);
}

.rs-16__preview-text .rs-16__hex {
  font-size: 18px;
  font-weight: 800;
  color: var(--text);
  letter-spacing: 2px;
  font-family: 'Courier New', monospace;
}

.rs-16__preview-text .rs-16__rgba {
  font-size: 11px;
  color: var(--muted);
  margin-top: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .rs-16__track-fill {
    transition: none;
  }

  .rs-16__glass-input::-webkit-slider-thumb {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const r=document.getElementById('rs-16-r'), g=document.getElementById('rs-16-g'),
        b=document.getElementById('rs-16-b'), a=document.getElementById('rs-16-a');
  const rf=document.getElementById('rs-16-rf'), gf=document.getElementById('rs-16-gf'),
        bf=document.getElementById('rs-16-bf'), af=document.getElementById('rs-16-af');
  const rv=document.getElementById('rs-16-rv'), gv=document.getElementById('rs-16-gv'),
        bv=document.getElementById('rs-16-bv'), av=document.getElementById('rs-16-av');
  const swatch=document.getElementById('rs-16-swatch'),
        hex=document.getElementById('rs-16-hex'),
        rgba=document.getElementById('rs-16-rgba');
  function toHex(n){ return n.toString(16).padStart(2,'0').toUpperCase(); }
  function update(){
    const rv_=+r.value, gv_=+g.value, bv_=+b.value, av_=+a.value;
    rf.style.width=(rv_/255*100)+'%'; gf.style.width=(gv_/255*100)+'%';
    bf.style.width=(bv_/255*100)+'%'; af.style.width=av_+'%';
    rv.textContent=rv_; gv.textContent=gv_; bv.textContent=bv_; av.textContent=av_+'%';
    const color = `rgba(${rv_},${gv_},${bv_},${(av_/100).toFixed(2)})`;
    swatch.style.background = color;
    hex.textContent = '#'+toHex(rv_)+toHex(gv_)+toHex(bv_);
    rgba.textContent = color;
  }
  [r,g,b,a].forEach(i=>i.addEventListener('input',update));
  document.querySelectorAll('.rs-16__toggle-btn').forEach(btn=>{
    btn.addEventListener('click',()=>{
      document.querySelectorAll('.rs-16__toggle-btn').forEach(x=>x.classList.remove('active'));
      btn.classList.add('active');
    });
  });
  update();
})();
```
