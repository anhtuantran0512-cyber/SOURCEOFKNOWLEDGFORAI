---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/media-slider-knob-card/"
title: "Media Slider & Knob Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A media-settings card with range sliders whose value tooltip is a drop of Liquid Glass that morphs straight out of the track: drag and a bubble stretches up…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media Slider & Knob Card
Source: https://codefronts.com/components/css-liquid-glass-cards/media-slider-knob-card/

A media-settings card with range sliders whose value tooltip is a drop of Liquid Glass that morphs straight out of the track: drag and a bubble stretches up from the filled portion, detaches with a gooey liquid neck, and floats above the thumb showing the live value. Includes volume and balance controls on a frosted panel.
## HTML
```html
<section class="lg-18" aria-label="Liquid glass media slider and knob card demo">
  <svg class="lg-18__defs" aria-hidden="true" width="0" height="0"><filter id="lg-18-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -9"/></filter></svg>
  <article class="lg-18__card">
    <div class="lg-18__head">
      <h3 class="lg-18__title">Playback</h3>
      <span class="lg-18__hint">Drag the thumbs →</span>
    </div>
    <div class="lg-18__ctrl" style="--v:.7">
      <div class="lg-18__row">
        <label class="lg-18__lab" for="lg-18-vol"><span class="lg-18__ic" aria-hidden="true">🔊</span> Volume</label>
        <span class="lg-18__val" data-val>70</span>
      </div>
      <div class="lg-18__slider">
        <span class="lg-18__goo" aria-hidden="true"><span class="lg-18__fill"></span><span class="lg-18__bubble" data-bubble>70</span></span>
        <input class="lg-18__input" id="lg-18-vol" type="range" min="0" max="100" value="70" aria-label="Volume">
      </div>
    </div>
    <div class="lg-18__ctrl" style="--v:.5">
      <div class="lg-18__row">
        <label class="lg-18__lab" for="lg-18-bal"><span class="lg-18__ic" aria-hidden="true">⇄</span> Balance</label>
        <span class="lg-18__val" data-val>0</span>
      </div>
      <div class="lg-18__slider">
        <span class="lg-18__goo" aria-hidden="true"><span class="lg-18__fill"></span><span class="lg-18__bubble" data-bubble>0</span></span>
        <input class="lg-18__input" id="lg-18-bal" type="range" min="-50" max="50" value="0" aria-label="Balance">
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
.lg-18,
.lg-18 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-18 {
  width: 100%;
  --accent: oklch(0.8 0.17 65);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 70% 20%,#0e7490,#0f172a 70%);
}

.lg-18__card {
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

.lg-18__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 6px;
}

.lg-18__title {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .02em;
}

.lg-18__hint {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,.6);
}

.lg-18__ctrl {
  margin-top: 20px;
}

.lg-18__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 12px;
}

.lg-18__lab {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,.9);
}

.lg-18__ic {
  font-size: 14px;
}

.lg-18__val {
  font-size: 14px;
  font-weight: 800;
  color: #fff;
  font-variant-numeric: tabular-nums;
  min-width: 3ch;
  text-align: right;
}

.lg-18__slider {
  position: relative;
  height: 32px;
  display: flex;
  align-items: center;
}

.lg-18__goo {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  filter: url(#lg-18-goo);
  pointer-events: none;
}

.lg-18__slider::before {
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

.lg-18__fill {
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

.lg-18__bubble {
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

.lg-18__input {
  position: absolute;
  inset: 0;
  width: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

.lg-18__input:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 6px;
  border-radius: 999px;
}

.lg-18__slider:has(.lg-18__input:active) .lg-18__bubble,
.lg-18__slider:has(.lg-18__input:focus-visible) .lg-18__bubble,
.lg-18__slider:has(.lg-18__input:hover) .lg-18__bubble {
  width: 32px;
  height: 32px;
  font-size: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-18__bubble {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.lg-18__ctrl').forEach((ctrl) => {
    const input = ctrl.querySelector('.lg-18__input');
    const bubble = ctrl.querySelector('[data-bubble]');
    const readout = ctrl.querySelector('[data-val]');
    if (!input) return;
    const min = +input.min, max = +input.max;
    const fmt = (n) => (min < 0 && n > 0 ? '+' + n : String(n));
    const sync = () => {
      const v = (input.value - min) / (max - min);
      ctrl.style.setProperty('--v', v);
      const text = fmt(+input.value);
      if (bubble) bubble.textContent = text;
      if (readout) readout.textContent = text;
    };
    input.addEventListener('input', sync);
    sync();
  });
})();
```
