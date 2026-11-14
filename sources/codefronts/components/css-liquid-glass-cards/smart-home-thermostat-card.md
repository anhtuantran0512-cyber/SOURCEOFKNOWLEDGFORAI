---
source: "codefronts"
url: "https://codefronts.com/components/css-liquid-glass-cards/smart-home-thermostat-card/"
title: "Smart Home Thermostat Card"
section: "components"
category: "css-liquid-glass-cards"
category_name: "CSS Liquid Glass Cards"
description: "A radial thermostat controller where the central temperature dial is a dense Liquid Glass lens that distorts a temperature grid drawn behind it — drag around…"
has_js: "true"
---

Here's a working CSS Liquid Glass Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Smart Home Thermostat Card
Source: https://codefronts.com/components/css-liquid-glass-cards/smart-home-thermostat-card/

A radial thermostat controller where the central temperature dial is a dense Liquid Glass lens that distorts a temperature grid drawn behind it — drag around the ring to set the target and the lens magnifies and warps the gridlines beneath the big degree readout. A conic progress arc tracks the setpoint around the dial.
## HTML
```html
<section class="lg-19" aria-label="Liquid glass smart home thermostat card demo">
  <svg class="lg-19__defs" aria-hidden="true" width="0" height="0"><filter id="lg-19-warp"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="2" seed="8" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
  <article class="lg-19__card">
    <div class="lg-19__top"><span class="lg-19__room">Living Room</span><span class="lg-19__mode">Heating</span></div>
    <div class="lg-19__dial" id="lg-19-dial" role="slider" tabindex="0" aria-label="Target temperature" aria-valuemin="15" aria-valuemax="28" aria-valuenow="21" aria-valuetext="21 degrees Celsius" style="--pct:.46">
      <div class="lg-19__grid" aria-hidden="true"></div>
      <div class="lg-19__arc" aria-hidden="true"></div>
      <div class="lg-19__lens"><strong class="lg-19__temp" id="lg-19-temp">21</strong><span class="lg-19__unit">°C</span></div>
    </div>
    <p class="lg-19__hint">Drag the ring or use arrow keys</p>
  </article>
</section>
```
## CSS
```css
.lg-19,
.lg-19 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --pct {
  syntax: '<number>';
  inherits: true;
  initial-value: 0.46;
}

.lg-19 {
  width: 100%;
  --accent: oklch(0.72 0.19 45);
  display: grid;
  place-items: center;
  min-height: 100vh;
  padding: 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(120% 120% at 50% 10%,#1e293b,#020617 70%);
}

.lg-19__card {
  width: min(300px,100%);
  padding: 22px;
  border-radius: 26px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 9%,transparent);
  border: 1px solid rgba(255,255,255,.3);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 30px 62px -30px rgba(0,0,0,.8);
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
}

.lg-19__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 18px;
}

.lg-19__room {
  font-size: 14px;
  font-weight: 800;
}

.lg-19__mode {
  font-size: 11px;
  font-weight: 700;
  color: #ffd8b0;
  padding: 3px 9px;
  border-radius: 999px;
  background: color-mix(in oklab,var(--accent) 45%,transparent);
}

.lg-19__dial {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto;
  border-radius: 50%;
  cursor: grab;
  touch-action: none;
  overflow: hidden;
  isolation: isolate;
  background: #0a1120;
  border: 1px solid rgba(255,255,255,.18);
}

.lg-19__dial:active {
  cursor: grabbing;
}

.lg-19__dial:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

.lg-19__grid {
  position: absolute;
  inset: 0;
  background: linear-gradient(rgba(255,255,255,.14) 1px,transparent 1px) 0 0/100% 18px,linear-gradient(90deg,rgba(255,255,255,.14) 1px,transparent 1px) 0 0/18px 100%;
}

.lg-19__arc {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(from 220deg,var(--accent) calc(var(--pct)*280deg),transparent 0);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 14px),#000 calc(100% - 13px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 14px),#000 calc(100% - 13px));
  filter: drop-shadow(0 0 8px var(--accent));
}

.lg-19__lens {
  position: absolute;
  inset: 26px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  isolation: isolate;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: inset 0 2px 10px rgba(255,255,255,.4),inset 0 -8px 18px rgba(0,0,0,.3),0 8px 20px -8px rgba(0,0,0,.6);
  backdrop-filter: blur(3px) saturate(150%);
  -webkit-backdrop-filter: blur(3px) saturate(150%);
  filter: url(#lg-19-warp);
}

.lg-19__temp {
  font-size: 52px;
  font-weight: 300;
  letter-spacing: -.03em;
  line-height: 1;
}

.lg-19__unit {
  position: absolute;
  top: 52px;
  right: 52px;
  font-size: 16px;
  font-weight: 600;
  color: rgba(255,255,255,.8);
}

.lg-19__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(255,255,255,.6);
  margin-top: 18px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-19__lens {
    filter: none;
  }
}
```

## JavaScript
```js
(() => {
  const dial = document.querySelector('#lg-19-dial');
  const out = document.querySelector('#lg-19-temp');
  if (!dial) return;
  const MIN = 15, MAX = 28;
  // Arc: conic-gradient(from 220deg) sweeps 280deg clockwise. That leaves an
  // 80deg dead zone at the top (140deg..220deg measured from 12 o'clock CW).
  // The MIN end sits at 220deg (bottom-left) and MAX at 140deg (top-right).
  // Clicking/dragging through the top gap must NOT flip MIN↔MAX — instead we
  // clamp to whichever end the pointer is closest to.
  const SWEEP = 280;                  // active dial travel
  const START = 220;                  // 12 o'clock is 0, arc starts here (CW)
  let t = 21;
  const render = () => {
    const pct = (t - MIN) / (MAX - MIN);
    dial.style.setProperty('--pct', pct.toFixed(3));
    out.textContent = t;
    dial.setAttribute('aria-valuenow', t);
    dial.setAttribute('aria-valuetext', t + ' degrees Celsius');
  };
  const fromEvent = (e) => {
    const r = dial.getBoundingClientRect();
    const cx = r.left + r.width/2, cy = r.top + r.height/2;
    // 0 at 12 o'clock, increasing CW
    let ang = Math.atan2(e.clientY - cy, e.clientX - cx) * 180/Math.PI + 90;
    if (ang < 0) ang += 360;
    // Distance CW from START (0 = MIN end, SWEEP = MAX end)
    let a = ang - START;
    if (a < 0) a += 360;
    let pct;
    if (a <= SWEEP) {
      // Inside the active arc — normal mapping
      pct = a / SWEEP;
    } else {
      // In the top gap — snap to nearest end instead of wrapping around.
      // Distance to MAX end (a === SWEEP) vs to MIN end (a === 360, i.e. 0).
      const distToMax = a - SWEEP;
      const distToMin = 360 - a;
      pct = distToMax < distToMin ? 1 : 0;
    }
    const next = Math.round(MIN + pct * (MAX - MIN));
    if (next === t) return;
    t = next;
    render();
  };
  let dragging = false;
  dial.addEventListener('pointerdown', (e) => {
    dragging = true;
    dial.setPointerCapture(e.pointerId);
    fromEvent(e);
  });
  dial.addEventListener('pointermove', (e) => { if (dragging) fromEvent(e); });
  const release = (e) => {
    if (!dragging) return;
    dragging = false;
    try { dial.releasePointerCapture(e.pointerId); } catch(_) {}
  };
  dial.addEventListener('pointerup', release);
  dial.addEventListener('pointercancel', release);
  dial.addEventListener('lostpointercapture', () => { dragging = false; });
  dial.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowUp' || e.key === 'ArrowRight') { t = Math.min(MAX, t+1); e.preventDefault(); render(); }
    if (e.key === 'ArrowDown' || e.key === 'ArrowLeft') { t = Math.max(MIN, t-1); e.preventDefault(); render(); }
    if (e.key === 'Home') { t = MIN; e.preventDefault(); render(); }
    if (e.key === 'End') { t = MAX; e.preventDefault(); render(); }
  });
  render();
})();
```
