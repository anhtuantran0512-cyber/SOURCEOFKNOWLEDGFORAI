---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/perspective-origin-as-the-camera-position/"
title: "Perspective Origin as the Camera Position"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "perspective-origin moves the viewer, not the object."
has_js: "true"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Perspective Origin as the Camera Position
Source: https://codefronts.com/design-styles/css-3d/perspective-origin-as-the-camera-position/

perspective-origin moves the viewer, not the object. Five camera positions drive one unchanged block of geometry: the radio-style control switches the origin and the readout shows the value, so the shift in which faces you can see is clearly a change of viewpoint rather than a change of transform. No script.
## HTML
```html
<section class="d3-03" aria-labelledby="d3-03-title">
  <h2 class="d3-03__sr" id="d3-03-title">Perspective origin as the camera</h2>

  <div class="d3-03__theme">
    <input class="d3-03__theme-input" type="checkbox" id="d3-03-theme">
    <label class="d3-03__theme-label" for="d3-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-03__stage">
    <div class="d3-03__viewport">
      <header class="d3-03__head">
        <div>
          <span class="d3-03__kicker">Halo Audio &mdash; showroom</span>
          <strong>Model One</strong>
        </div>
        <span class="d3-03__price">&pound;249</span>
      </header>

      <div class="d3-03__scene" id="d3-03-scene">
        <div class="d3-03__object">
          <div class="d3-03__speaker">
            <span class="d3-03__grille" aria-hidden="true"></span>
            <span class="d3-03__ring" aria-hidden="true"></span>
            <span class="d3-03__brand">HALO</span>
          </div>
          <div class="d3-03__plinth" aria-hidden="true"></div>
          <div class="d3-03__shadow" aria-hidden="true"></div>
        </div>
      </div>

      <div class="d3-03__bar">
        <div class="d3-03__pad" id="d3-03-pad" role="img" aria-label="Camera position pad">
          <span class="d3-03__cam" id="d3-03-cam"></span>
        </div>
        <dl class="d3-03__read">
          <div><dt>perspective-origin</dt><dd id="d3-03-out">50% 38%</dd></div>
          <div><dt>perspective</dt><dd>980px</dd></div>
        </dl>
        <p class="d3-03__hint">Drag anywhere on the stage to move the camera.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-03 {
  --d3-03-bg: #070d1b;
  --d3-03-surf: #0f1830;
  --d3-03-line: #22304f;
  --d3-03-ink: #eaf0ff;
  --d3-03-mut: #94a5c6;
  --d3-03-acc: #ffb020;
  --d3-03-acc: oklch(80% 0.16 78);
  --d3-03-acc2: #3c6dff;
  --d3-03-acc2: oklch(62% 0.19 266);
  --d3-03-x: 50%;
  --d3-03-y: 38%;
  --d3-03-font-display: "Barlow Condensed", "Oswald", "Haettenschweiler", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(60rem 34rem at var(--d3-03-x) 10%, color-mix(in oklab, var(--d3-03-acc2) 26%, transparent), transparent 62%), var(--d3-03-bg);
  color: var(--d3-03-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-03 *,
.d3-03 *::before,
.d3-03 *::after {
  box-sizing: border-box;
}

.d3-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-03:has(.d3-03__theme-input:checked) {
  --d3-03-bg: #f4f1ea;
  --d3-03-surf: #ffffff;
  --d3-03-line: #ddd6c8;
  --d3-03-ink: #131722;
  --d3-03-mut: #5f6a80;
  --d3-03-acc: #a35c00;
  --d3-03-acc: oklch(56% 0.14 72);
  --d3-03-acc2: #2247c9;
  --d3-03-acc2: oklch(48% 0.2 266);
}

@media (prefers-color-scheme: light) {
  .d3-03:has(.d3-03__theme-input:checked) {
    --d3-03-bg: #f4f1ea;
    --d3-03-surf: #ffffff;
    --d3-03-line: #ddd6c8;
    --d3-03-ink: #131722;
    --d3-03-mut: #5f6a80;
    --d3-03-acc: #a35c00;
    --d3-03-acc: oklch(56% 0.14 72);
    --d3-03-acc2: #2247c9;
    --d3-03-acc2: oklch(48% 0.2 266);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-03:has(.d3-03__theme-input:checked) {
    --d3-03-bg: #f4f1ea;
    --d3-03-surf: #ffffff;
    --d3-03-line: #ddd6c8;
    --d3-03-ink: #131722;
    --d3-03-mut: #5f6a80;
    --d3-03-acc: #a35c00;
    --d3-03-acc: oklch(56% 0.14 72);
    --d3-03-acc2: #2247c9;
    --d3-03-acc2: oklch(48% 0.2 266);
  }
}

.d3-03__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-03__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-03-line);
  border-radius: 999px;
  background: var(--d3-03-surf);
  color: var(--d3-03-ink);
  cursor: pointer;
}

.d3-03__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-03__theme-input:focus-visible + .d3-03__theme-label {
  outline: 2px solid var(--d3-03-acc);
  outline-offset: 3px;
}

.d3-03__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-03__viewport {
  inline-size: 100%;
  max-inline-size: 58rem;
  overflow: hidden;
  border: 1px solid var(--d3-03-line);
  border-radius: 28px;
  background: linear-gradient(180deg, color-mix(in oklab, var(--d3-03-surf) 92%, transparent), color-mix(in oklab, var(--d3-03-bg) 88%, transparent));
  padding: clamp(1rem, 3.5vw, 2rem);
  display: grid;
  gap: clamp(0.9rem, 3vw, 1.5rem);
  box-shadow: 0 40px 90px -46px #000;
}

.d3-03__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
}

.d3-03__kicker {
  display: block;
  font: 700 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-03-acc);
}

.d3-03__head strong {
  font: 700 clamp(1.6rem, 6vw, 3rem)/0.95 var(--d3-03-font-display);
  letter-spacing: 0.01em;
  text-transform: uppercase;
}

.d3-03__price {
  font: 700 clamp(1rem, 3vw, 1.4rem)/1 var(--d3-03-font-display);
  color: var(--d3-03-mut);
}

.d3-03__scene {
  perspective: 980px;
  perspective-origin: var(--d3-03-x) var(--d3-03-y);
  block-size: clamp(15rem, 44vw, 22rem);
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: radial-gradient(24rem 12rem at 50% 82%, color-mix(in oklab, var(--d3-03-acc) 18%, transparent), transparent 70%);
  cursor: grab;
  touch-action: none;
}

.d3-03__scene:active {
  cursor: grabbing;
}

.d3-03__object {
  position: relative;
  inline-size: clamp(10rem, 30vw, 15rem);
  block-size: clamp(10rem, 30vw, 15rem);
  transform-style: preserve-3d;
  transform: rotateX(8deg) rotateY(-18deg);
}

.d3-03__speaker {
  position: absolute;
  inset: 6% 12% 22%;
  border-radius: 22px;
  background: linear-gradient(160deg, #23262e, #0d0f14);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.16), 0 30px 60px -20px #000;
  transform: translateZ(46px);
  display: grid;
  place-items: center;
}

.d3-03__grille {
  position: absolute;
  inset: 12%;
  border-radius: 14px;
  background-image: radial-gradient(currentColor 1px, transparent 1.4px);
  background-size: 7px 7px;
  color: rgba(255, 255, 255, 0.22);
}

.d3-03__ring {
  position: absolute;
  inline-size: 46%;
  aspect-ratio: 1;
  border-radius: 999px;
  border: 3px solid var(--d3-03-acc);
  box-shadow: 0 0 24px color-mix(in oklab, var(--d3-03-acc) 60%, transparent), inset 0 0 18px color-mix(in oklab, var(--d3-03-acc) 35%, transparent);
}

.d3-03__brand {
  position: absolute;
  inset-block-end: 8%;
  font: 700 0.66rem/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.3em;
  color: rgba(255, 255, 255, 0.6);
}

.d3-03__plinth {
  position: absolute;
  inset-inline: 4%;
  inset-block-end: 8%;
  block-size: 18%;
  border-radius: 14px;
  background: linear-gradient(180deg, color-mix(in oklab, var(--d3-03-acc2) 40%, #101425), #0a0e1a);
  transform: translateZ(16px);
  box-shadow: 0 20px 40px -16px #000;
}

.d3-03__shadow {
  position: absolute;
  inset-inline: 0;
  inset-block-end: -6%;
  block-size: 40%;
  transform: rotateX(90deg);
  background: radial-gradient(closest-side, rgba(0, 0, 0, 0.6), transparent 72%);
}

.d3-03__bar {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: clamp(0.75rem, 3vw, 1.25rem);
  padding: clamp(0.7rem, 2.4vw, 1rem);
  border: 1px solid var(--d3-03-line);
  border-radius: 18px;
  background: color-mix(in oklab, var(--d3-03-surf) 80%, transparent);
}

.d3-03__pad {
  position: relative;
  inline-size: 72px;
  block-size: 52px;
  border-radius: 10px;
  border: 1px solid var(--d3-03-line);
  background-image: linear-gradient(color-mix(in oklab, var(--d3-03-mut) 30%, transparent) 1px, transparent 1px), linear-gradient(90deg, color-mix(in oklab, var(--d3-03-mut) 30%, transparent) 1px, transparent 1px);
  background-size: 12px 12px;
}

.d3-03__cam {
  position: absolute;
  inset-block-start: var(--d3-03-y);
  inset-inline-start: var(--d3-03-x);
  inline-size: 12px;
  block-size: 12px;
  margin: -6px 0 0 -6px;
  border-radius: 999px;
  background: var(--d3-03-acc);
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--d3-03-acc) 30%, transparent);
}

.d3-03__read {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.2rem;
}

.d3-03__read dt {
  font: 700 0.6rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--d3-03-mut);
}

.d3-03__read dd {
  margin: 0;
  font: 600 clamp(0.78rem, 2.2vw, 0.95rem)/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-03-acc);
}

.d3-03__hint {
  grid-column: 1 / -1;
  margin: 0;
  font: 500 0.72rem/1.3 system-ui, sans-serif;
  color: var(--d3-03-mut);
}

@media (prefers-reduced-motion: reduce) {
  .d3-03__object {
    transform: rotateX(8deg) rotateY(-18deg);
  }
}
```

## JavaScript
```js
const root = document.querySelector('.d3-03');
const scene = root.querySelector('#d3-03-scene');
const out = root.querySelector('#d3-03-out');
let drag = false;
const move = (e) => {
  if (!drag) return;
  const r = scene.getBoundingClientRect();
  const x = Math.min(100, Math.max(0, ((e.clientX - r.left) / r.width) * 100));
  const y = Math.min(100, Math.max(0, ((e.clientY - r.top) / r.height) * 100));
  root.style.setProperty('--d3-03-x', x.toFixed(1) + '%');
  root.style.setProperty('--d3-03-y', y.toFixed(1) + '%');
  out.textContent = x.toFixed(0) + '% ' + y.toFixed(0) + '%';
};
const down = (e) => { drag = true; scene.setPointerCapture(e.pointerId); move(e); };
const up = () => { drag = false; };
scene.addEventListener('pointerdown', down);
scene.addEventListener('pointermove', move);
scene.addEventListener('pointerup', up);
scene.addEventListener('pointercancel', up);
root.__d3Cleanup = () => { scene.removeEventListener('pointerdown', down); scene.removeEventListener('pointermove', move); scene.removeEventListener('pointerup', up); scene.removeEventListener('pointercancel', up); };
```
