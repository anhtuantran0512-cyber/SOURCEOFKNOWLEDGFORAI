---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/mouse-tracking-refraction-hero/"
title: "Mouse-Tracking Refraction Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "A large hero card with a real Liquid Glass lens bubble that follows the cursor across the surface, magnifying and refracting the headline and mesh background…"
has_js: "true"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mouse-Tracking Refraction Hero
Source: https://codefronts.com/layouts/css-hero-sections/mouse-tracking-refraction-hero/

A large hero card with a real Liquid Glass lens bubble that follows the cursor across the surface, magnifying and refracting the headline and mesh background beneath it in real time. Move away and the lens drifts back to centre with an easing spring — the show-off centerpiece for a frontend portfolio.
## HTML
```html
<section class="hs-31" aria-label="Mouse-tracking refraction hero demo" id="hs-31">
  <div class="hs-31__inner">
    <p class="hs-31__kicker">Frontend that feels physical</p>
    <h2 class="hs-31__title">Liquid<br>Glass</h2>
    <p class="hs-31__sub">Move — or tap and drag on touch — the lens refracts everything beneath it.</p>
  </div>
  <span class="hs-31__lens" id="hs-31-lens" aria-hidden="true"></span>
</section>
```
## CSS
```css
.hs-31,
.hs-31 * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hs-31 {
  --r: 96px;
  --mx: 200px;
  --my: 200px;
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  cursor: crosshair;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 60deg at 30% 30%,#f59e0b,#ef4444,#8b5cf6,#06b6d4,#f59e0b);
  background-size: 200% 200%;
  animation: hs-31-bg 16s ease-in-out infinite;
}

@keyframes hs-31-bg {
  50% {
    background-position: 100% 100%;
  }
}

.hs-31__inner {
  position: absolute;
  inset: 0;
  display: grid;
  align-content: center;
  padding: 0 40px;
  color: #fff;
}

.hs-31__kicker {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  opacity: .9;
}

.hs-31__title {
  font-size: clamp(52px,13vw,110px);
  font-weight: 900;
  line-height: .9;
  letter-spacing: -.04em;
  margin: 10px 0;
  text-shadow: 0 4px 24px rgba(0,0,0,.28);
}

.hs-31__sub {
  font-size: 15px;
  max-width: 34ch;
  opacity: .92;
}

.hs-31__lens {
  position: absolute;
  top: 0;
  left: 0;
  width: calc(var(--r)*2);
  height: calc(var(--r)*2);
  border-radius: 50%;
  transform: translate(calc(var(--mx) - var(--r)),calc(var(--my) - var(--r)));
  pointer-events: none;
  isolation: isolate;
  background: radial-gradient(circle at 35% 30%,rgba(255,255,255,.32),rgba(255,255,255,.05) 55%,transparent 72%);
  border: 2px solid rgba(255,255,255,.7);
  box-shadow: inset 0 3px 12px rgba(255,255,255,.55),inset 0 -12px 26px rgba(0,0,0,.28),0 14px 40px -8px rgba(0,0,0,.55);
  backdrop-filter: blur(12px) saturate(210%) contrast(1.08);
  -webkit-backdrop-filter: blur(12px) saturate(210%) contrast(1.08);
}

@media (prefers-reduced-motion: reduce) {
  .hs-31 {
    animation: none;
    cursor: auto;
  }

  .hs-31__lens {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const hero = document.querySelector('#hs-31');
  const lens = document.querySelector('#hs-31-lens');
  if (!hero || !lens) return;
  // Touch detection — on touch devices the demo runs an ambient orbit so
  // mobile users see a live lens without needing to drag (many won't
  // discover the drag affordance on first paint). Any real pointer input
  // cancels the orbit.
  const hasCoarsePointer = matchMedia('(pointer: coarse)').matches;
  let tx = 0, ty = 0, x = 0, y = 0, raf, ambientRaf, ambientStartedAt = 0;
  const centerFromRect = (b) => {
    tx = b.width/2; ty = b.height/2;
    if (!x && !y) { x = tx; y = ty; }
    lens.style.setProperty('--mx', x + 'px');
    lens.style.setProperty('--my', y + 'px');
  };
  const initFromLayout = () => {
    const b = hero.getBoundingClientRect();
    if (b.width < 32 || b.height < 32) {
      // Layout hasn't settled yet — try again next frame. Guards against
      // iframe-init timing where the hero renders after the script runs.
      requestAnimationFrame(initFromLayout);
      return;
    }
    centerFromRect(b);
    if (hasCoarsePointer) startAmbient();
  };
  const startAmbient = () => {
    if (ambientRaf) return;
    const orbit = (t) => {
      if (!ambientStartedAt) ambientStartedAt = t;
      const elapsed = (t - ambientStartedAt) / 1000;
      const b = hero.getBoundingClientRect();
      const cx = b.width/2, cy = b.height/2;
      // Slow figure-eight so users see the lens moving over headline + background
      const rx = Math.min(cx, b.width * 0.28);
      const ry = Math.min(cy, b.height * 0.22);
      tx = cx + Math.cos(elapsed * 0.7) * rx;
      ty = cy + Math.sin(elapsed * 1.4) * ry;
      x = tx; y = ty;
      lens.style.setProperty('--mx', x + 'px');
      lens.style.setProperty('--my', y + 'px');
      ambientRaf = requestAnimationFrame(orbit);
    };
    ambientRaf = requestAnimationFrame(orbit);
  };
  const stopAmbient = () => {
    if (!ambientRaf) return;
    cancelAnimationFrame(ambientRaf);
    ambientRaf = null; ambientStartedAt = 0;
  };
  hero.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'touch' && !e.isPrimary) return;
    stopAmbient();
    const b = hero.getBoundingClientRect();
    tx = e.clientX - b.left;
    ty = e.clientY - b.top;
    if (!raf) loop();
  });
  hero.addEventListener('pointerleave', () => {
    const b = hero.getBoundingClientRect();
    tx = b.width/2;
    ty = b.height/2;
    if (!raf) loop();
    // If we're on touch and user finished, restart ambient
    if (hasCoarsePointer) setTimeout(startAmbient, 800);
  });
  function loop(){
    x += (tx - x) * 0.14;
    y += (ty - y) * 0.14;
    lens.style.setProperty('--mx', x + 'px');
    lens.style.setProperty('--my', y + 'px');
    if (Math.abs(tx-x) > 0.5 || Math.abs(ty-y) > 0.5) raf = requestAnimationFrame(loop);
    else raf = null;
  }
  window.addEventListener('resize', () => {
    const b = hero.getBoundingClientRect();
    if (b.width < 32 || b.height < 32) return;
    if (Math.hypot(tx - b.width/2, ty - b.height/2) < 8) {
      tx = b.width/2; ty = b.height/2;
      if (!raf) loop();
    }
  }, { passive: true });
  initFromLayout();
})();
```
