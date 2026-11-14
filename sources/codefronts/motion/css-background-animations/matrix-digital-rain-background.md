---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/matrix-digital-rain-background/"
title: "Matrix Digital Rain Effect"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Digital rain done right: a bright leading glyph, a decaying trail behind it, per-column speeds, occasional glyph mutation mid-fall, and a frame budget that…"
has_js: "true"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Matrix Digital Rain Effect
Source: https://codefronts.com/motion/css-background-animations/matrix-digital-rain-background/

Digital rain done right: a bright leading glyph, a decaying trail behind it, per-column speeds, occasional glyph mutation mid-fall, and a frame budget that holds at 4K. It runs at a deliberate 24fps — the film frame rate the effect is remembered from — which also cuts its CPU cost by more than half compared to a 60fps loop nobody can perceive as smoother.
## HTML
```html
<section class="bga-20" id="bga-20-root" aria-label="Matrix digital rain background demo">
  <canvas class="bga-20__c" id="bga-20-canvas" aria-hidden="true"></canvas>
  <div class="bga-20__vig" aria-hidden="true"></div>

  <div class="bga-20__stage">
    <div class="bga-20__panel">
      <p class="bga-20__eyebrow">24 fps by choice · 20</p>
      <h1 class="bga-20__title">Bright head.<br>Decaying tail.</h1>
      <p class="bga-20__sub">The head/tail luminance split is what makes digital rain read as rain. Everything else — glyph set, colour, speed — is set dressing.</p>
      <div class="bga-20__readout">
        <span><i></i>columns <b id="bga-20-cols">—</b></span>
        <span><i></i>fps cap <b>24</b></span>
        <span><i></i>off-screen <b>paused</b></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-20,
.bga-20 *,
.bga-20 *::before,
.bga-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-20 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-20-bg: oklch(0.13 0.03 158);
  --bga-20-ph: oklch(0.86 0.2 152);
  background: var(--bga-20-bg);
  color: var(--bga-20-ph);
  font-family: ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  -webkit-font-smoothing: antialiased;
}

.bga-20__c {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
}

.bga-20__vig {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(110% 88% at 50% 46%,transparent 34%,oklch(0.07 0.02 158/.92) 100%);
}

.bga-20__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-20__panel {
  width: min(100%,640px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,46px);
  background: oklch(0.1 0.025 158/.7);
  border: 1px solid color-mix(in oklab,var(--bga-20-ph) 26%,transparent);
  box-shadow: 0 0 60px -20px color-mix(in oklab,var(--bga-20-ph) 40%,transparent),0 40px 90px -50px oklch(0 0 0/.95);
}

.bga-20__eyebrow {
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--bga-20-ph) 70%,transparent);
}

.bga-20__title {
  font-size: clamp(28px,5.6vw,56px);
  font-weight: 700;
  line-height: 1.02;
  letter-spacing: -.03em;
  text-wrap: balance;
  text-shadow: 0 0 28px color-mix(in oklab,var(--bga-20-ph) 55%,transparent);
}

.bga-20__sub {
  max-width: 48ch;
  font-family: ui-sans-serif,system-ui,-apple-system,sans-serif;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: color-mix(in oklab,var(--bga-20-ph) 78%,transparent);
  text-wrap: pretty;
}

.bga-20__readout {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 4px;
}

.bga-20__readout span {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: 8px 13px;
  color: color-mix(in oklab,var(--bga-20-ph) 66%,transparent);
  background: oklch(1 0 0/.04);
  border: 1px solid color-mix(in oklab,var(--bga-20-ph) 18%,transparent);
}

.bga-20__readout i {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--bga-20-ph);
  box-shadow: 0 0 8px var(--bga-20-ph);
}

.bga-20__readout b {
  color: var(--bga-20-ph);
  font-size: 12.5px;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bga-20-root');
  const cv = document.getElementById('bga-20-canvas');
  if (!root || !cv) return;
  const ctx = cv.getContext('2d');
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const GLYPHS = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ0123456789';
  const FPS = 24, STEP = 1000 / FPS;
  const CELL = 18;
  let w = 0, h = 0, dpr = 1, cols = 0, drops = [], glyph = [], raf = 0, live = false, last = 0;

  const pick = () => GLYPHS[(Math.random() * GLYPHS.length) | 0];

  const size = () => {
    const r = root.getBoundingClientRect();
    w = r.width; h = r.height;
    dpr = Math.min(devicePixelRatio || 1, 2);
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.font = (CELL - 2) + 'px ui-monospace, Menlo, monospace';
    ctx.textBaseline = 'top';
    cols = Math.ceil(w / CELL);
    drops = Array.from({ length: cols }, () => ({
      y: -Math.random() * h,
      v: CELL * (0.55 + Math.random() * 0.9),
      prev: pick()
    }));
    glyph = Array.from({ length: cols }, pick);
    ctx.fillStyle = '#080d0a';
    ctx.fillRect(0, 0, w, h);
    const out = document.getElementById('bga-20-cols');
    if (out) out.textContent = String(cols);
  };

  const draw = () => {
    ctx.fillStyle = 'rgba(8,13,10,0.17)';
    ctx.fillRect(0, 0, w, h);
    for (let i = 0; i < cols; i++) {
      const d = drops[i];
      const x = i * CELL;
      if (Math.random() < 0.22) { d.prev = glyph[i]; glyph[i] = pick(); }
      ctx.shadowBlur = 14;
      ctx.shadowColor = '#3dffa4';
      ctx.fillStyle = '#e6fff2';
      ctx.fillText(glyph[i], x, d.y);
      ctx.shadowBlur = 0;
      ctx.fillStyle = 'rgba(61,255,164,0.82)';
      ctx.fillText(d.prev, x, d.y - CELL);
      d.y += d.v;
      if (d.y > h + Math.random() * 240) { d.y = -Math.random() * 160; d.v = CELL * (0.55 + Math.random() * 0.9); }
    }
  };

  const frame = (now) => {
    if (now - last >= STEP) { last = now; draw(); }
    if (live) raf = requestAnimationFrame(frame);
  };

  const start = () => { if (!live && !calm) { live = true; raf = requestAnimationFrame(frame); } };
  const stop = () => { live = false; cancelAnimationFrame(raf); };

  size();
  if (calm) { for (let i = 0; i < 26; i++) draw(); }
  else new IntersectionObserver((es) => es.forEach(e => e.isIntersecting ? start() : stop()), { threshold: 0 }).observe(root);

  let t;
  addEventListener('resize', () => { clearTimeout(t); t = setTimeout(() => { size(); if (calm) for (let i = 0; i < 26; i++) draw(); }, 180); });
})();
```
