---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/interactive-or-click-to-expand-ripple-static-effects/"
title: "Interactive Water Ripple Background"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Touch the surface and it answers."
has_js: "true"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Water Ripple Background
Source: https://codefronts.com/motion/css-background-animations/interactive-or-click-to-expand-ripple-static-effects/

Touch the surface and it answers. Each pointer press spawns a self-destructing ripple element — three expanding rings with staggered delays and a refraction wobble — over a caustics layer built from animated turbulence. The JavaScript is nine lines and removes its own DOM nodes on animationend, so an hour of clicking leaves the node count exactly where it started.
## HTML
```html
<section class="bga-16" id="bga-16-root" aria-label="Interactive water ripple background demo">
  <svg class="bga-16__defs" aria-hidden="true" focusable="false">
    <filter id="bga-16-water" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="2" seed="7" result="bga-16-n">
        <animate attributeName="seed" values="7;19;7" dur="22s" repeatCount="indefinite"/>
      </feTurbulence>
      <feDisplacementMap in="SourceGraphic" in2="bga-16-n" scale="44" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="bga-16__deep" aria-hidden="true">
    <img class="bga-16__photo" src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1800&auto=format&fit=crop" alt="" width="1800" height="1200" loading="lazy" decoding="async">
  </div>
  <div class="bga-16__caustics" aria-hidden="true"></div>
  <div class="bga-16__sheen" aria-hidden="true"></div>

  <div class="bga-16__stage">
    <div class="bga-16__card">
      <p class="bga-16__eyebrow">Direct manipulation · 16</p>
      <h1 class="bga-16__title">Press anywhere.<br>The surface remembers.</h1>
      <p class="bga-16__sub">Each press spawns one element that removes itself on <code>animationend</code>. Drag to draw a wake — ripples are throttled by distance, not by time.</p>
      <div class="bga-16__meta">
        <span><b id="bga-16-count">0</b>ripples spawned</span>
        <span><b id="bga-16-live">0</b>currently alive</span>
      </div>
      <p class="bga-16__spec">pointerdown + pointermove · self-cleaning nodes · feDisplacementMap caustics</p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-16,
.bga-16 *,
.bga-16 *::before,
.bga-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-16-deep: oklch(0.28 0.09 232);
  --bga-16-shal: oklch(0.62 0.13 200);
  --bga-16-foam: oklch(0.93 0.06 195);
  background: var(--bga-16-deep);
  color: oklch(0.98 0.008 210);
  cursor: crosshair;
  touch-action: manipulation;
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-16__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.bga-16__deep {
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 90% at 50% 12%,oklch(0.5 0.12 210),oklch(0.22 0.08 244) 74%);
}

.bga-16__photo {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  opacity: .46;
  mix-blend-mode: luminosity;
}

.bga-16__caustics {
  position: absolute;
  inset: -8%;
  opacity: .5;
  mix-blend-mode: screen;
  filter: url(#bga-16-water) blur(1px);
  background: repeating-radial-gradient(circle at 32% 28%,transparent 0 26px,color-mix(in oklab,var(--bga-16-foam) 26%,transparent) 26px 29px), repeating-radial-gradient(circle at 74% 66%,transparent 0 34px,color-mix(in oklab,var(--bga-16-shal) 34%,transparent) 34px 37px);
  animation: bga-16-swim 40s linear infinite;
}

@keyframes bga-16-swim {
  to {
    translate: -3% 2%;
    scale: 1.05;
  }
}

.bga-16__sheen {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: screen;
  opacity: .4;
  background: linear-gradient(104deg,transparent 38%,oklch(0.95 0.04 200/.3) 50%,transparent 62%);
  background-size: 280% 100%;
  animation: bga-16-sheen 15s linear infinite;
}

@keyframes bga-16-sheen {
  from {
    background-position: 130% 0;
  }

  to {
    background-position: -130% 0;
  }
}

.bga-16__ripple {
  position: absolute;
  width: 0;
  height: 0;
  pointer-events: none;
  z-index: 3;
}

.bga-16__ripple::before,
.bga-16__ripple::after,
.bga-16__ripple > i {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  width: var(--bga-16-r,420px);
  aspect-ratio: 1;
  translate: -50% -50%;
  border-radius: 50%;
  border: 3px solid oklch(0.96 0.05 195/.85);
  animation: bga-16-ring 1.5s cubic-bezier(.16,1,.3,1) forwards;
}

.bga-16__ripple::after {
  animation-delay: .13s;
  border-color: oklch(0.9 0.08 205/.6);
}

.bga-16__ripple > i {
  animation-delay: .27s;
  border-color: oklch(0.85 0.1 215/.45);
}

@keyframes bga-16-ring {
  from {
    scale: 0;
    opacity: .9;
    border-width: 3px;
  }

  to {
    scale: 1;
    opacity: 0;
    border-width: .5px;
  }
}

.bga-16__stage {
  position: relative;
  z-index: 4;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
  pointer-events: none;
}

.bga-16__card {
  width: min(100%,660px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 24px;
  background: oklch(0.2 0.06 235/.42);
  border: 1px solid oklch(1 0 0/.18);
  backdrop-filter: blur(20px) saturate(1.4);
  -webkit-backdrop-filter: blur(20px) saturate(1.4);
  box-shadow: 0 44px 100px -54px oklch(0 0 0/.9),inset 0 1px 0 oklch(1 0 0/.22);
}

.bga-16__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.9 0.1 195);
}

.bga-16__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 620;
  line-height: 1.04;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-16__sub {
  max-width: 48ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.95 0.01 210/.8);
  text-wrap: pretty;
}

.bga-16__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.12);
}

.bga-16__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
}

.bga-16__meta span {
  display: flex;
  align-items: baseline;
  gap: 7px;
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(1 0 0/.6);
  padding: 9px 15px;
  border-radius: 12px;
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.13);
}

.bga-16__meta b {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 17px;
  letter-spacing: -.02em;
  color: oklch(0.95 0.07 195);
}

.bga-16__spec {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.42);
}

@media (prefers-reduced-motion: reduce) {
  .bga-16__caustics,
    .bga-16__sheen {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('bga-16-root');
  if (!root) return;
  const cnt = document.getElementById('bga-16-count');
  const liveEl = document.getElementById('bga-16-live');
  let total = 0, alive = 0, last = null;

  const spawn = (x, y, size) => {
    const d = document.createElement('span');
    d.className = 'bga-16__ripple';
    d.style.left = x + 'px';
    d.style.top = y + 'px';
    d.style.setProperty('--bga-16-r', size + 'px');
    d.append(document.createElement('i'));
    alive++; total++;
    if (cnt) cnt.textContent = String(total);
    if (liveEl) liveEl.textContent = String(alive);
    d.addEventListener('animationend', () => {
      d.remove(); alive = Math.max(0, alive - 1);
      if (liveEl) liveEl.textContent = String(alive);
    }, { once: true });
    root.append(d);
  };

  const at = (e) => {
    const r = root.getBoundingClientRect();
    return { x: e.clientX - r.left, y: e.clientY - r.top };
  };

  root.addEventListener('pointerdown', (e) => {
    const p = at(e); last = p;
    spawn(p.x, p.y, 460);
  });

  root.addEventListener('pointermove', (e) => {
    if (e.buttons !== 1) { last = null; return; }
    const p = at(e);
    if (!last) { last = p; return; }
    const dx = p.x - last.x, dy = p.y - last.y;
    if (dx * dx + dy * dy < 5200) return;
    last = p;
    spawn(p.x, p.y, 230);
  }, { passive: true });

  root.addEventListener('pointerup', () => { last = null; });
})();
```
