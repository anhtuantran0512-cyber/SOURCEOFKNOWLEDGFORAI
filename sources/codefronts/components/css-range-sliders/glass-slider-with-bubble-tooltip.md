---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/glass-slider-with-bubble-tooltip/"
title: "Glass Slider with Bubble Tooltip"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A range slider where the value tooltip is a drop of Liquid Glass that morphs out of the track itself: as you drag, a bubble stretches up from the filled…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glass Slider with Bubble Tooltip
Source: https://codefronts.com/components/css-range-sliders/glass-slider-with-bubble-tooltip/

A range slider where the value tooltip is a drop of Liquid Glass that morphs out of the track itself: as you drag, a bubble stretches up from the filled portion, detaches with a gooey neck, and floats above the thumb showing the live value — the fluid feedback control from modern iOS settings.
## HTML
```html
<section class="rs-17" aria-label="Glass slider with bubble tooltip demo">
  <svg class="rs-17__defs" aria-hidden="true" width="0" height="0"><filter id="rs-17-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -9"/></filter></svg>
  <article class="rs-17__card">
    <div class="rs-17__head">
      <h3 class="rs-17__title">Display</h3>
      <span class="rs-17__hint">Drag the thumb →</span>
    </div>
    <div class="rs-17__wrap" style="--v:.6">
      <div class="rs-17__row">
        <label class="rs-17__lab" for="rs-17-input"><span class="rs-17__ic" aria-hidden="true">☀︎</span> Brightness</label>
        <span class="rs-17__val" id="rs-17-val">60</span>
      </div>
      <div class="rs-17__slider">
        <span class="rs-17__goo" aria-hidden="true"><span class="rs-17__fill"></span><span class="rs-17__bubble" id="rs-17-bubble">60</span></span>
        <input class="rs-17__input" id="rs-17-input" type="range" min="0" max="100" value="60" aria-label="Brightness">
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.rs-17,
.rs-17 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-17 {
  --accent: oklch(0.8 0.17 65);
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 70% 20%,#1e293b,#0f172a 70%);
}

.rs-17__card {
  width: min(360px,100%);
  padding: 24px;
  border-radius: 24px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 11%,transparent);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 30px 60px -30px rgba(0,0,0,.7);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
}

.rs-17__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 8px;
}

.rs-17__title {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .02em;
}

.rs-17__hint {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,.6);
}

.rs-17__wrap {
  margin-top: 14px;
}

.rs-17__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 12px;
}

.rs-17__lab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.9);
}

.rs-17__ic {
  font-size: 14px;
}

.rs-17__val {
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  font-variant-numeric: tabular-nums;
  min-width: 3ch;
  text-align: right;
}

.rs-17__slider {
  position: relative;
  height: 32px;
  display: flex;
  align-items: center;
}

.rs-17__goo {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  filter: url(#rs-17-goo);
  pointer-events: none;
}

.rs-17__slider::before {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  height: 8px;
  border-radius: 999px;
  background: rgba(255,255,255,.16);
  border: 1px solid rgba(255,255,255,.25);
}

.rs-17__fill {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  height: 8px;
  width: calc(var(--v)*100%);
  border-radius: 999px;
  background: linear-gradient(90deg,color-mix(in oklab,var(--accent) 60%,transparent),var(--accent));
  box-shadow: 0 0 12px -2px var(--accent);
}

.rs-17__bubble {
  position: absolute;
  top: 50%;
  left: calc(var(--v)*100%);
  transform: translate(-50%,-50%);
  width: 22px;
  height: 22px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 0;
  color: #3a2a05;
  background: radial-gradient(circle at 35% 30%,#fff,var(--accent));
  border: 1px solid rgba(255,255,255,.6);
  box-shadow: inset 0 2px 4px rgba(255,255,255,.9),inset 0 -3px 5px rgba(0,0,0,.18),0 6px 14px rgba(0,0,0,.35);
  transition: width .25s cubic-bezier(.34,1.6,.5,1),height .25s cubic-bezier(.34,1.6,.5,1),font-size .18s ease .05s;
}

.rs-17__input {
  position: absolute;
  inset: 0;
  width: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

.rs-17__input:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 6px;
  border-radius: 999px;
}

.rs-17__slider:has(.rs-17__input:active) .rs-17__bubble,
.rs-17__slider:has(.rs-17__input:focus-visible) .rs-17__bubble,
.rs-17__slider:has(.rs-17__input:hover) .rs-17__bubble {
  width: 32px;
  height: 32px;
  font-size: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .rs-17__bubble {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const wrap = document.querySelector('.rs-17__wrap');
  const input = document.querySelector('#rs-17-input');
  const bubble = document.querySelector('#rs-17-bubble');
  const readout = document.querySelector('#rs-17-val');
  if (!input) return;
  const sync = () => {
    const v = input.value / 100;
    wrap.style.setProperty('--v', v);
    if (bubble) bubble.textContent = input.value;
    if (readout) readout.textContent = input.value;
  };
  input.addEventListener('input', sync);
  sync();
})();
```
