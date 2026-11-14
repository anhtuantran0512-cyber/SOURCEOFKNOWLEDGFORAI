---
source: "codefronts"
url: "https://codefronts.com/navigation/css-circular-menus/tactile-dial/"
title: "Rotary Control Dial Interface"
section: "navigation"
category: "css-circular-menus"
category_name: "CSS Circular Menus"
description: "A hi-fi–grade rotary knob: drag around it, scroll over it, or use arrow keys, and a conic-gradient arc sweeps to show the value while the tick marks light up…"
has_js: "true"
---

Here's a working CSS Circular Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotary Control Dial Interface
Source: https://codefronts.com/navigation/css-circular-menus/tactile-dial/

A hi-fi–grade rotary knob: drag around it, scroll over it, or use arrow keys, and a conic-gradient arc sweeps to show the value while the tick marks light up behind it. Under the hood it's a proper ARIA slider, so it reports its value to assistive tech just like a native range input.
## HTML
```html
<section class="ccm-08" aria-label="Rotary dial control demo">
  <div class="ccm-08__stage">
    <div class="ccm-08__deck">
      <div class="ccm-08__ticks" aria-hidden="true"></div>
      <div class="ccm-08__knob" role="slider" tabindex="0" aria-label="Volume" aria-valuemin="0" aria-valuemax="100" aria-valuenow="62" aria-valuetext="62 percent">
        <span class="ccm-08__cap"><i class="ccm-08__pip"></i></span>
      </div>
      <p class="ccm-08__readout"><output class="ccm-08__val">62</output><span>%</span></p>
      <p class="ccm-08__label">volume</p>
    </div>
    <p class="ccm-08__hint">Drag around the knob · scroll · or arrow keys</p>
  </div>
</section>
```
## CSS
```css
.ccm-08,
.ccm-08 *,
.ccm-08 *::before,
.ccm-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccm-08 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg,oklch(0.23 0.015 160),oklch(0.17 0.012 170));
  --brand: oklch(0.75 0.17 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: oklch(0.9 0.01 150);
}

.ccm-08__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  border-radius: 20px;
  background: linear-gradient(180deg,oklch(0.23 0.015 160),oklch(0.17 0.012 170));
  overflow: hidden;
}

.ccm-08__deck {
  position: relative;
  width: 240px;
  height: 240px;
  display: grid;
  place-items: center;
}

.ccm-08__ticks {
  position: absolute;
  inset: 0;
}

.ccm-08__ticks i {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 2px;
  height: 9px;
  margin-left: -1px;
  border-radius: 2px;
  background: oklch(0.45 0.02 160);
  transform: rotate(var(--t)) translateY(-116px);
  transition: background .2s;
}

.ccm-08__ticks i.is-lit {
  background: var(--brand);
  box-shadow: 0 0 8px oklch(0.75 0.17 145 / .7);
}

.ccm-08__knob {
  position: relative;
  width: 176px;
  height: 176px;
  border-radius: 50%;
  cursor: grab;
  touch-action: none;
  background: conic-gradient(from 225deg,var(--brand) calc(var(--val,62) * 270deg / 100),oklch(0.32 0.015 160 / .6) calc(var(--val,62) * 270deg / 100) 270deg,transparent 270deg);
  display: grid;
  place-items: center;
  -webkit-user-select: none;
  user-select: none;
}

.ccm-08__knob:active {
  cursor: grabbing;
}

.ccm-08__knob:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 6px;
}

.ccm-08__cap {
  position: relative;
  width: 148px;
  height: 148px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 28%,oklch(0.36 0.015 160),oklch(0.24 0.012 165) 70%);
  box-shadow: 0 14px 30px -10px oklch(0 0 0 / .7),inset 0 1px 0 oklch(1 0 0 / .14),inset 0 -6px 14px oklch(0 0 0 / .4);
  rotate: calc(135deg + var(--val,62) * 2.7deg + 90deg);
}

.ccm-08__pip {
  position: absolute;
  left: 50%;
  top: 12px;
  width: 10px;
  height: 10px;
  margin-left: -5px;
  border-radius: 50%;
  background: var(--brand);
  box-shadow: 0 0 12px oklch(0.75 0.17 145 / .9);
}

.ccm-08__readout {
  position: absolute;
  bottom: -8px;
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-variant-numeric: tabular-nums;
}

.ccm-08__val {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ccm-08__readout span {
  font-size: 14px;
  color: oklch(0.6 0.03 155);
}

.ccm-08__label {
  position: absolute;
  top: -4px;
  font-size: 11px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: oklch(0.6 0.03 155);
}

.ccm-08__hint {
  font-size: 13px;
  color: oklch(0.6 0.03 155);
}

@media (prefers-reduced-motion: reduce) {
  .ccm-08 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ccm-08');
  const knob = root.querySelector('.ccm-08__knob');
  const out = root.querySelector('.ccm-08__val');
  const ticks = root.querySelector('.ccm-08__ticks');
  for (let t = 0; t <= 27; t++) {
    const i = document.createElement('i');
    i.style.setProperty('--t', (135 + t * 10 + 90) + 'deg');
    ticks.append(i);
  }
  const tickEls = [...ticks.children];
  let val = 62;
  const setVal = (v) => {
    val = Math.max(0, Math.min(100, Math.round(v)));
    knob.style.setProperty('--val', val);
    knob.setAttribute('aria-valuenow', val);
    knob.setAttribute('aria-valuetext', val + ' percent');
    out.textContent = val;
    tickEls.forEach((el, k) => el.classList.toggle('is-lit', k / 27 * 100 <= val));
  };
  const fromPointer = (e) => {
    const r = knob.getBoundingClientRect();
    const dx = e.clientX - (r.left + r.width / 2);
    const dy = e.clientY - (r.top + r.height / 2);
    let deg = Math.atan2(dy, dx) * 180 / Math.PI; // -180..180, 0 = 3 o'clock
    deg = (deg - 135 + 360) % 360;                // 0 at sweep start
    if (deg > 270) deg = deg < 315 ? 270 : 0;     // snap the dead zone to nearest end
    setVal(deg / 270 * 100);
  };
  knob.addEventListener('pointerdown', (e) => {
    knob.setPointerCapture(e.pointerId); fromPointer(e);
    const move = (ev) => fromPointer(ev);
    knob.addEventListener('pointermove', move);
    knob.addEventListener('pointerup', () => knob.removeEventListener('pointermove', move), { once: true });
  });
  knob.addEventListener('wheel', (e) => { e.preventDefault(); setVal(val + (e.deltaY < 0 ? 2 : -2)); }, { passive: false });
  knob.addEventListener('keydown', (e) => {
    const map = { ArrowUp: 1, ArrowRight: 1, ArrowDown: -1, ArrowLeft: -1 };
    if (e.key in map) { e.preventDefault(); setVal(val + map[e.key]); }
    if (e.key === 'Home') setVal(0);
    if (e.key === 'End') setVal(100);
  });
  setVal(62);
})();
```
