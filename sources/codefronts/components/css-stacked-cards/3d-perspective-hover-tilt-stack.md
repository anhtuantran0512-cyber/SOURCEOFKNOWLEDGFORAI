---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/3d-perspective-hover-tilt-stack/"
title: "3D Perspective Hover Tilt Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A holographic-trading-card-style 3D deck with layered parallax, iridescent conic-gradient border sweep, cursor-tracked specular glare, and Pokemon-holo-card…"
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Perspective Hover Tilt Stack
Source: https://codefronts.com/components/css-stacked-cards/3d-perspective-hover-tilt-stack/

A holographic-trading-card-style 3D deck with layered parallax, iridescent conic-gradient border sweep, cursor-tracked specular glare, and Pokemon-holo-card color-dodge sheen. Uses cutting-edge CSS Houdini @property for GPU-composited typed-value transitions, color-mix(in oklch) for perceptually-uniform accent blending, and mask-composite:exclude for the animated iridescent border. The whole stack tilts toward the cursor in real time with five distinct parallax layers moving at different depths.
## HTML
```html
<section class="scd-06" aria-label="Holographic 3D perspective tilt card stack">
  <div class="scd-06__scene">
    <div class="scd-06__deck" id="scd-06-deck" tabindex="0" role="button" aria-label="Interactive holographic card deck. Move pointer to tilt.">
      <div class="scd-06__card scd-06__card--back" aria-hidden="true">
        <span class="scd-06__cardnum">03</span>
      </div>
      <div class="scd-06__card scd-06__card--mid" aria-hidden="true">
        <span class="scd-06__cardnum">02</span>
      </div>
      <div class="scd-06__card scd-06__card--front">
        <div class="scd-06__layer scd-06__layer--bg" aria-hidden="true"></div>
        <div class="scd-06__layer scd-06__layer--holo" aria-hidden="true"></div>
        <div class="scd-06__layer scd-06__layer--content">
          <p class="scd-06__eyebrow">Holographic · 01</p>
          <h3 class="scd-06__title">Depth Pass</h3>
          <p class="scd-06__desc">Move your pointer to tilt the deck. Layered parallax, iridescent sweep, real specular glare.</p>
        </div>
        <div class="scd-06__layer scd-06__layer--glare" aria-hidden="true"></div>
        <div class="scd-06__layer scd-06__layer--border" aria-hidden="true"></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@property --scd-06-tilt-x {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}

@property --scd-06-tilt-y {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: true;
}

@property --scd-06-mx {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --scd-06-my {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --scd-06-holo-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.scd-06,
.scd-06 *,
.scd-06 *::before,
.scd-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-06 {
  --accent: oklch(0.72 0.18 320);
  --accent-b: oklch(0.68 0.20 200);
  --accent-c: oklch(0.75 0.19 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(circle at 20% 30%,color-mix(in oklch,var(--accent) 22%,transparent),transparent 60%),radial-gradient(circle at 80% 70%,color-mix(in oklch,var(--accent-b) 22%,transparent),transparent 60%),radial-gradient(circle at 50% 100%,#0a0b14,#04050a);
}

.scd-06__scene {
  perspective: 1200px;
  perspective-origin: center 40%;
  width: min(340px,100%);
  height: 460px;
  position: relative;
}

.scd-06__deck {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transform: rotateX(var(--scd-06-tilt-x)) rotateY(var(--scd-06-tilt-y));
  transition: --scd-06-tilt-x .4s cubic-bezier(.22,1,.36,1),--scd-06-tilt-y .4s cubic-bezier(.22,1,.36,1);
  cursor: grab;
}

.scd-06__card {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  background: linear-gradient(160deg,#1a1c2e,#0f1120);
  border: 1px solid color-mix(in oklch,var(--accent) 25%,#2a2d48);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.9),0 0 0 1px color-mix(in oklch,var(--accent) 15%,transparent) inset;
}

.scd-06__card--back {
  transform: translateZ(-100px) translateY(20px) scale(.92);
  filter: brightness(.5);
}

.scd-06__card--mid {
  transform: translateZ(-50px) translateY(10px) scale(.96);
  filter: brightness(.72);
}

.scd-06__cardnum {
  position: absolute;
  top: 20px;
  right: 22px;
  font-weight: 800;
  color: color-mix(in oklch,var(--accent) 40%,#4a5080);
  font-size: 14px;
  letter-spacing: .05em;
}

.scd-06__card--front {
  transform: translateZ(0);
  overflow: hidden;
  filter: brightness(1);
  background: linear-gradient(155deg,color-mix(in oklch,var(--accent) 12%,#1a1c2e) 0%,#0f1120 100%);
}

.scd-06__layer {
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
}

.scd-06__layer--bg {
  transform: translateZ(4px);
  background: radial-gradient(circle at 30% 30%,color-mix(in oklch,var(--accent) 35%,transparent),transparent 50%),radial-gradient(circle at 70% 70%,color-mix(in oklch,var(--accent-b) 35%,transparent),transparent 50%);
  filter: blur(20px);
  opacity: .85;
}

.scd-06__layer--holo {
  transform: translateZ(6px);
  background: conic-gradient(from var(--scd-06-holo-angle) at var(--scd-06-mx) var(--scd-06-my),color-mix(in oklch,var(--accent) 70%,transparent),color-mix(in oklch,var(--accent-b) 70%,transparent),color-mix(in oklch,var(--accent-c) 70%,transparent),color-mix(in oklch,var(--accent) 70%,transparent));
  mix-blend-mode: color-dodge;
  opacity: .32;
  animation: scd-06-holo-spin 8s linear infinite;
}

.scd-06__layer--content {
  padding: 32px 30px;
  transform: translateZ(30px);
  color: #fff;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 8px;
  height: 100%;
}

.scd-06__eyebrow {
  font-size: 11px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 700;
}

.scd-06__title {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.05;
  color: color-mix(in oklch,var(--accent) 20%,#ffffff);
}

.scd-06__desc {
  font-size: 14px;
  line-height: 1.5;
  color: color-mix(in oklch,var(--accent) 8%,#c3c7de);
  max-width: 26ch;
}

.scd-06__layer--glare {
  transform: translateZ(35px);
  background: radial-gradient(200px circle at var(--scd-06-mx) var(--scd-06-my),rgba(255,255,255,.35),transparent 55%);
  mix-blend-mode: overlay;
  opacity: 0;
  transition: opacity .3s;
}

.scd-06__deck:hover .scd-06__layer--glare,
.scd-06__deck:focus-visible .scd-06__layer--glare {
  opacity: 1;
}

.scd-06__layer--border {
  transform: translateZ(38px);
  padding: 2px;
  background: conic-gradient(from var(--scd-06-holo-angle),var(--accent),var(--accent-b),var(--accent-c),var(--accent));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: .7;
  transition: opacity .3s;
}

.scd-06__deck:hover .scd-06__layer--border,
.scd-06__deck:focus-visible .scd-06__layer--border {
  opacity: 1;
}

.scd-06__deck:hover,
.scd-06__deck:focus-visible {
  cursor: grabbing;
}

@keyframes scd-06-holo-spin {
  from {
    --scd-06-holo-angle: 0deg;
  }

  to {
    --scd-06-holo-angle: 360deg;
  }
}

.scd-06__deck:focus-visible {
  outline: none;
  --scd-06-tilt-x: 10deg;
  --scd-06-tilt-y: -12deg;
}

.scd-06__scene:has(.scd-06__deck:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 12px;
  border-radius: 26px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-06__deck {
    transition: none;
  }

  .scd-06__layer--holo {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-06');
  if (!root) return;
  const deck = root.querySelector('#scd-06-deck');
  const MAX_DEG = 14;
  const supportsHover = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!supportsHover || reduceMotion) return;
  let raf = 0;
  const setTilt = (rx, ry, mx, my) => {
    deck.style.setProperty('--scd-06-tilt-x', rx + 'deg');
    deck.style.setProperty('--scd-06-tilt-y', ry + 'deg');
    deck.style.setProperty('--scd-06-mx', mx + '%');
    deck.style.setProperty('--scd-06-my', my + '%');
  };
  deck.addEventListener('pointermove', (e) => {
    if (raf) cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      const r = deck.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      const ry = ((px - 0.5) * 2 * MAX_DEG).toFixed(2);
      const rx = ((0.5 - py) * 2 * MAX_DEG).toFixed(2);
      setTilt(rx, ry, (px * 100).toFixed(1), (py * 100).toFixed(1));
    });
  });
  deck.addEventListener('pointerleave', () => {
    if (raf) cancelAnimationFrame(raf);
    setTilt(0, 0, 50, 50);
  });
})();
```
