---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/tilt-on-hover/"
title: "Tilt on Hover"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A card stack that tilts toward whichever corner your cursor enters from — hover the top-left and it banks up-left; sweep to the bottom-right and it follows."
has_js: "true"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tilt on Hover
Source: https://codefronts.com/components/css-stacked-cards/tilt-on-hover/

A card stack that tilts toward whichever corner your cursor enters from — hover the top-left and it banks up-left; sweep to the bottom-right and it follows. A lightweight, tactile feedback loop with a soft sheen that tracks the pointer.
## HTML
```html
<section class="scd-24" aria-label="Quadrant tilt card stack">
  <div class="scd-24__scene">
    <div class="scd-24__stack" id="scd-24-stack" tabindex="0">
      <div class="scd-24__card" style="--i:2"></div>
      <div class="scd-24__card" style="--i:1"></div>
      <div class="scd-24__card scd-24__card--top" style="--i:0"><p class="scd-24__k">Interactive</p><h3>Tilt me</h3><p class="scd-24__d">Enter from any corner — the deck banks toward you.</p><span class="scd-24__sheen"></span></div>
    </div>
  </div>
</section>
```
## CSS
```css
.scd-24,
.scd-24 *,
.scd-24 *::before,
.scd-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-24 {
  --accent: oklch(0.72 0.15 190);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(circle at 50% 40%,#10222a,#080d12);
}

.scd-24__scene {
  perspective: 900px;
  width: min(300px,90vw);
}

.scd-24__stack {
  position: relative;
  height: 220px;
  transform-style: preserve-3d;
  transform: rotateX(calc(var(--ty,0) * 1deg)) rotateY(calc(var(--tx,0) * 1deg));
  transition: transform .4s ease;
  outline: none;
}

.scd-24__card {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: #132831;
  border: 1px solid #1e3b46;
  transform: translate(calc(var(--i) * 8px),calc(var(--i) * 8px)) translateZ(calc(var(--i) * -20px));
  box-shadow: 0 22px 44px -26px rgba(0,0,0,.85);
}

.scd-24__card--top {
  padding: 28px;
  color: #eaf6f8;
  overflow: hidden;
  background: linear-gradient(150deg,#153039,#0e2028);
}

.scd-24__k {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.scd-24__card--top h3 {
  font-size: 30px;
  font-weight: 800;
  margin: 10px 0 8px;
  letter-spacing: -.02em;
}

.scd-24__d {
  font-size: 14px;
  line-height: 1.55;
  color: #a9c6cd;
  max-width: 26ch;
}

.scd-24__sheen {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(200px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.22),transparent 60%);
  opacity: 0;
  transition: opacity .3s;
}

.scd-24__stack:hover .scd-24__sheen,
.scd-24__stack:focus-visible .scd-24__sheen {
  opacity: 1;
}

.scd-24__scene:has(.scd-24__stack:focus-visible) .scd-24__stack {
  transform: rotateX(7deg) rotateY(-9deg);
}

@media (prefers-reduced-motion: reduce) {
  .scd-24__stack {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.scd-24');
  const stack = root.querySelector('#scd-24-stack');
  const sheen = root.querySelector('.scd-24__sheen');
  const MAX = 12;
  stack.addEventListener('pointermove', e => {
    const r = stack.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    const qx = px < .5 ? -1 : 1, qy = py < .5 ? 1 : -1;
    stack.style.setProperty('--tx', (qx * MAX).toString());
    stack.style.setProperty('--ty', (qy * MAX).toString());
    sheen.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    sheen.style.setProperty('--my', (py * 100).toFixed(1) + '%');
  });
  stack.addEventListener('pointerleave', () => { stack.style.setProperty('--tx', 0); stack.style.setProperty('--ty', 0); });
})();
```
