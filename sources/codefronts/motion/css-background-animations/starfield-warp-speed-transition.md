---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/starfield-warp-speed-transition/"
title: "Starfield Warp Speed Transition"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "A real perspective starfield — stars live in 3D and are projected to the screen, so they streak outward with correct parallax instead of sliding on a flat…"
has_js: "true"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Starfield Warp Speed Transition
Source: https://codefronts.com/motion/css-background-animations/starfield-warp-speed-transition/

A real perspective starfield — stars live in 3D and are projected to the screen, so they streak outward with correct parallax instead of sliding on a flat plane. Press Engage and the warp factor eases from 1 to 22 over a second and a half, stretching every star into a light trail: the classic hyperspace page transition, in about fifty lines with no library.
## HTML
```html
<section class="bga-11" id="bga-11-root" aria-label="Starfield warp speed background demo">
  <canvas class="bga-11__c" id="bga-11-canvas" aria-hidden="true"></canvas>
  <div class="bga-11__blur" id="bga-11-blur" aria-hidden="true"></div>
  <div class="bga-11__vig" aria-hidden="true"></div>

  <div class="bga-11__stage">
    <div class="bga-11__hud">
      <p class="bga-11__eyebrow">Perspective projection · 11</p>
      <h1 class="bga-11__title">Hyperspace is one<br>perspective divide.</h1>
      <p class="bga-11__sub">Stars are 3D points. Divide x and y by z, draw a line from last frame's projection to this one, and the streak length becomes a free function of speed.</p>
      <div class="bga-11__row">
        <button class="bga-11__btn" id="bga-11-go" type="button">Engage warp</button>
        <div class="bga-11__gauge" aria-hidden="true">
          <span class="bga-11__gaugeLabel">Factor</span>
          <b id="bga-11-factor">1.0</b>
          <i class="bga-11__bar"><em id="bga-11-fill"></em></i>
        </div>
      </div>
      <p class="bga-11__spec">z-recycling · previous-to-current line trails · eased scalar warp · rAF paused off-screen</p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-11,
.bga-11 *,
.bga-11 *::before,
.bga-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-11-bg: oklch(0.11 0.02 268);
  --bga-11-acc: oklch(0.82 0.16 250);
  background: var(--bga-11-bg);
  color: oklch(0.97 0.01 250);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-11__c {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
}

.bga-11__blur {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0;
  mix-blend-mode: screen;
  background: radial-gradient(60% 60% at 50% 50%,transparent 20%,color-mix(in oklab,var(--bga-11-acc) 26%,transparent) 74%,transparent 100%);
  transition: opacity .5s linear;
}

.bga-11__vig {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(120% 100% at 50% 50%,transparent 42%,oklch(0.06 0.015 268/.9) 100%);
}

.bga-11__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-11__hud {
  width: min(100%,700px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 18px;
  background: oklch(0.1 0.02 268/.55);
  border: 1px solid color-mix(in oklab,var(--bga-11-acc) 24%,transparent);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 0 0 1px oklch(0 0 0/.4),0 44px 100px -50px oklch(0 0 0/.95);
}

.bga-11__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--bga-11-acc);
}

.bga-11__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 640;
  line-height: 1.04;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-11__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.92 0.01 250/.76);
  text-wrap: pretty;
}

.bga-11__row {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: center;
  margin-top: 4px;
}

.bga-11__btn {
  min-height: 48px;
  padding: 0 26px;
  border: 0;
  border-radius: 99px;
  cursor: pointer;
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 660;
  letter-spacing: -.01em;
  color: oklch(0.14 0.03 260);
  background: linear-gradient(oklch(0.95 0.06 240),oklch(0.82 0.15 250));
  box-shadow: 0 0 34px -6px color-mix(in oklab,var(--bga-11-acc) 70%,transparent);
  transition: transform .35s cubic-bezier(.16,1,.3,1),box-shadow .35s,filter .2s;
}

.bga-11__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 52px -4px color-mix(in oklab,var(--bga-11-acc) 85%,transparent);
}

.bga-11__btn:active {
  transform: translateY(0) scale(.98);
}

.bga-11__btn:focus-visible {
  outline: 3px solid oklch(0.99 0 0);
  outline-offset: 3px;
}

.bga-11__btn[disabled] {
  filter: grayscale(.5) brightness(.8);
  cursor: progress;
}

.bga-11__gauge {
  display: grid;
  grid-template-columns: auto auto;
  gap: 2px 10px;
  align-items: center;
  padding: 9px 15px;
  border-radius: 12px;
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.12);
}

.bga-11__gaugeLabel {
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(1 0 0/.5);
}

.bga-11__gauge b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 17px;
  color: var(--bga-11-acc);
  text-align: right;
}

.bga-11__bar {
  grid-column: 1/-1;
  display: block;
  width: 150px;
  height: 5px;
  border-radius: 99px;
  background: oklch(1 0 0/.12);
  overflow: hidden;
}

.bga-11__bar em {
  display: block;
  width: 4%;
  height: 100%;
  border-radius: 99px;
  background: var(--bga-11-acc);
  transition: width .1s linear;
}

.bga-11__spec {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.4);
  text-wrap: balance;
  max-width: 60ch;
}

@media (prefers-reduced-motion: reduce) {
  .bga-11__btn {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bga-11-root');
  const cv = document.getElementById('bga-11-canvas');
  const btn = document.getElementById('bga-11-go');
  const out = document.getElementById('bga-11-factor');
  const fill = document.getElementById('bga-11-fill');
  const blur = document.getElementById('bga-11-blur');
  if (!root || !cv) return;
  const ctx = cv.getContext('2d');
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const MAX = 22, FOV = 128;
  let w = 0, h = 0, dpr = 1, stars = [], raf = 0, live = false;
  let speed = 1, warpUntil = 0;

  const seed = (s) => {
    s.x = (Math.random() - .5) * 2400;
    s.y = (Math.random() - .5) * 2400;
    s.z = Math.random() * 1200 + 40;
    s.px = null;
    return s;
  };

  const size = () => {
    const r = root.getBoundingClientRect();
    w = r.width; h = r.height;
    dpr = Math.min(devicePixelRatio || 1, 2);
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const n = Math.min(620, Math.max(160, Math.round(w * h / 2600)));
    stars = Array.from({ length: n }, () => seed({}));
  };

  const frame = (now) => {
    if (warpUntil) {
      const t = Math.min(1, 1 - (warpUntil - now) / 1500);
      const e = t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      speed = 1 + (MAX - 1) * (t < 1 ? e : 0);
      if (t >= 1) { warpUntil = 0; speed = 1; }
      if (out) out.textContent = speed.toFixed(1);
      if (fill) fill.style.width = (speed / MAX * 100).toFixed(1) + '%';
      if (blur) blur.style.opacity = String(Math.min(.85, (speed - 1) / MAX));
    }
    ctx.fillStyle = '#0b0d16';
    ctx.fillRect(0, 0, w, h);
    ctx.beginPath();
    const cx = w / 2, cy = h / 2;
    for (const s of stars) {
      const k0 = FOV / s.z;
      const x0 = s.x * k0 + cx, y0 = s.y * k0 + cy;
      s.z -= speed * 2.4;
      if (s.z < 6) { seed(s); continue; }
      const k = FOV / s.z;
      const x = s.x * k + cx, y = s.y * k + cy;
      if (x < -60 || x > w + 60 || y < -60 || y > h + 60) { seed(s); continue; }
      ctx.moveTo(x0, y0); ctx.lineTo(x, y);
    }
    ctx.strokeStyle = 'rgba(214,232,255,0.9)';
    ctx.lineWidth = Math.min(2.2, .7 + speed * .07);
    ctx.lineCap = 'round';
    ctx.stroke();
    if (live) raf = requestAnimationFrame(frame);
  };

  const start = () => { if (!live && !calm) { live = true; raf = requestAnimationFrame(frame); } };
  const stop = () => { live = false; cancelAnimationFrame(raf); };

  size();
  if (calm) { speed = 14; frame(performance.now()); speed = 1; }
  else new IntersectionObserver((es) => es.forEach(e => e.isIntersecting ? start() : stop()), { threshold: 0 }).observe(root);

  let t;
  addEventListener('resize', () => { clearTimeout(t); t = setTimeout(() => { size(); if (calm) frame(performance.now()); }, 160); });

  if (btn) btn.addEventListener('click', () => {
    if (calm) {
      speed = 16; frame(performance.now()); speed = 1;
      if (out) out.textContent = '16.0';
      if (fill) fill.style.width = '73%';
      return;
    }
    btn.disabled = true;
    warpUntil = performance.now() + 1500;
    setTimeout(() => {
      btn.disabled = false;
      if (out) out.textContent = '1.0';
      if (fill) fill.style.width = '4%';
      if (blur) blur.style.opacity = '0';
    }, 1600);
  });
})();
```
