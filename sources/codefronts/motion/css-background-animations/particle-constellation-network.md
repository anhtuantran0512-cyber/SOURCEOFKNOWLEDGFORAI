---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/particle-constellation-network/"
title: "Particle Constellation Network"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The connected-dots network, rewritten as forty lines of dependency-free Canvas 2D instead of a 60KB library."
has_js: "true"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Constellation Network
Source: https://codefronts.com/motion/css-background-animations/particle-constellation-network/

The connected-dots network, rewritten as forty lines of dependency-free Canvas 2D instead of a 60KB library. Particles drift, link to neighbours within a radius, and pull toward the cursor; density scales to the viewport area, the loop is DPR-correct, and it stops itself entirely when the section scrolls out of view or the user asks for reduced motion.
## HTML
```html
<section class="bga-10" id="bga-10-root" aria-label="Particle constellation network background demo">
  <canvas class="bga-10__c" id="bga-10-canvas" aria-hidden="true"></canvas>
  <div class="bga-10__wash" aria-hidden="true"></div>

  <div class="bga-10__stage">
    <div class="bga-10__panel">
      <p class="bga-10__eyebrow">Canvas 2D · 10</p>
      <h1 class="bga-10__title">A network that knows when to stop.</h1>
      <p class="bga-10__sub">Half-matrix pair testing, one batched path per frame, DPR-correct lines, and an IntersectionObserver that kills the loop the moment it leaves the viewport.</p>
      <ul class="bga-10__stats">
        <li><b id="bga-10-n">—</b><span>nodes</span></li>
        <li><b>O(n²)/2</b><span>pair tests</span></li>
        <li><b>1</b><span>stroke call</span></li>
        <li><b>~1.4 KB</b><span>no deps</span></li>
      </ul>
      <p class="bga-10__hint">Move the pointer — nodes lean toward it.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-10,
.bga-10 *,
.bga-10 *::before,
.bga-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-10-bg: oklch(0.15 0.02 256);
  --bga-10-acc: oklch(0.82 0.15 178);
  background: var(--bga-10-bg);
  color: oklch(0.97 0.008 220);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-10__c {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
}

.bga-10__wash {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(80% 62% at 50% 46%,color-mix(in oklab,var(--bga-10-acc) 9%,transparent),transparent 68%), radial-gradient(120% 100% at 50% 50%,transparent 45%,oklch(0.1 0.02 256/.8) 100%);
}

.bga-10__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
  pointer-events: none;
}

.bga-10__panel {
  width: min(100%,700px);
  display: grid;
  gap: 16px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 22px;
  background: oklch(0.13 0.018 256/.62);
  border: 1px solid oklch(1 0 0/.12);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 44px 100px -52px oklch(0 0 0/.95);
}

.bga-10__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--bga-10-acc);
}

.bga-10__title {
  font-size: clamp(26px,5vw,50px);
  font-weight: 640;
  line-height: 1.05;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.bga-10__sub {
  max-width: 52ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.92 0.01 220/.76);
  text-wrap: pretty;
}

.bga-10__stats {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 4px;
}

.bga-10__stats li {
  display: grid;
  gap: 2px;
  min-width: 98px;
  padding: 10px 14px;
  border-radius: 12px;
  background: oklch(1 0 0/.05);
  border: 1px solid oklch(1 0 0/.1);
}

.bga-10__stats b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 17px;
  font-weight: 600;
  color: var(--bga-10-acc);
  letter-spacing: -.02em;
}

.bga-10__stats span {
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: oklch(0.85 0.01 220/.6);
}

.bga-10__hint {
  font-size: 12px;
  color: oklch(0.85 0.01 220/.45);
}

@media (prefers-reduced-motion: reduce) {
  .bga-10__hint {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bga-10-root');
  const cv = document.getElementById('bga-10-canvas');
  if (!root || !cv) return;
  const ctx = cv.getContext('2d');
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const LINK = 132;
  let w = 0, h = 0, dpr = 1, parts = [], raf = 0, live = false;
  const mouse = { x: -9999, y: -9999 };

  const size = () => {
    const r = root.getBoundingClientRect();
    w = r.width; h = r.height;
    dpr = Math.min(devicePixelRatio || 1, 2);
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const n = Math.min(120, Math.max(28, Math.round(w * h / 13000)));
    parts = Array.from({ length: n }, () => ({
      x: Math.random() * w, y: Math.random() * h,
      vx: (Math.random() - .5) * .34, vy: (Math.random() - .5) * .34,
      r: Math.random() * 1.6 + .9
    }));
    const out = document.getElementById('bga-10-n');
    if (out) out.textContent = String(n);
  };

  const frame = () => {
    ctx.clearRect(0, 0, w, h);
    for (const p of parts) {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;
      const dx = mouse.x - p.x, dy = mouse.y - p.y, d2 = dx * dx + dy * dy;
      if (d2 < 26000 && d2 > 1) { p.x += dx / d2 * 22; p.y += dy / d2 * 22; }
    }
    ctx.beginPath();
    for (let i = 0; i < parts.length; i++) {
      for (let j = i + 1; j < parts.length; j++) {
        const dx = parts[i].x - parts[j].x, dy = parts[i].y - parts[j].y;
        const d2 = dx * dx + dy * dy;
        if (d2 < LINK * LINK) {
          ctx.moveTo(parts[i].x, parts[i].y);
          ctx.lineTo(parts[j].x, parts[j].y);
        }
      }
    }
    ctx.strokeStyle = 'rgba(120,220,220,0.16)';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.fillStyle = 'rgba(190,245,240,0.85)';
    for (const p of parts) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();
    }
    if (live) raf = requestAnimationFrame(frame);
  };

  const start = () => { if (!live && !calm) { live = true; raf = requestAnimationFrame(frame); } };
  const stop = () => { live = false; cancelAnimationFrame(raf); };

  size();
  if (calm) { frame(); } else {
    new IntersectionObserver((es) => es.forEach(e => e.isIntersecting ? start() : stop()), { threshold: 0 }).observe(root);
  }

  let t;
  addEventListener('resize', () => { clearTimeout(t); t = setTimeout(() => { size(); if (calm) frame(); }, 160); });
  root.addEventListener('pointermove', (e) => {
    const r = root.getBoundingClientRect();
    mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top;
  }, { passive: true });
  root.addEventListener('pointerleave', () => { mouse.x = mouse.y = -9999; });
})();
```
