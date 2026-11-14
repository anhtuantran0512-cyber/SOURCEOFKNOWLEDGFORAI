---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/rotate3d-and-the-transform-matrix/"
title: "Rotate3d and the Transform Matrix"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "rotate3d(x, y, z, angle) rotates around an arbitrary axis vector, which rotateX, rotateY and rotateZ cannot express between them."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate3d and the Transform Matrix
Source: https://codefronts.com/design-styles/css-3d/rotate3d-and-the-transform-matrix/

rotate3d(x, y, z, angle) rotates around an arbitrary axis vector, which rotateX, rotateY and rotateZ cannot express between them. Four wireframe plates turn around four different vectors with the vector drawn on each, and the readout names the fact that all of it compiles down to one matrix3d().
## HTML
```html
<section class="d3-11" aria-labelledby="d3-11-title">
  <h2 class="d3-11__sr" id="d3-11-title">Rotate3d and the transform matrix</h2>

  <div class="d3-11__theme">
    <input class="d3-11__theme-input" type="checkbox" id="d3-11-theme">
    <label class="d3-11__theme-label" for="d3-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-11__stage">
    <div class="d3-11__viewport">
      <div class="d3-11__panel">
        <span class="d3-11__kicker">Season pass &middot; 2027</span>
        <strong class="d3-11__title">Rotating around an arbitrary axis</strong>
        <p class="d3-11__copy">Three separate rotations run one after another. <code>rotate3d(x, y, z, angle)</code> runs once, around a vector you choose &mdash; so the badge tumbles on its true diagonal instead of stepping through three axes.</p>
        <dl class="d3-11__read">
          <div><dt>axis</dt><dd>1, 1, 0.35</dd></div>
          <div><dt>angle</dt><dd>360deg</dd></div>
          <div><dt>matrix</dt><dd>4 &times; 4</dd></div>
        </dl>
        <ul class="d3-11__legend">
          <li><span class="d3-11__key d3-11__key--x"></span>X 1.0</li>
          <li><span class="d3-11__key d3-11__key--y"></span>Y 1.0</li>
          <li><span class="d3-11__key d3-11__key--z"></span>Z 0.35</li>
        </ul>
      </div>

      <div class="d3-11__scene">
        <div class="d3-11__rig">
          <div class="d3-11__badge">
            <span class="d3-11__holo" aria-hidden="true"></span>
            <span class="d3-11__mark">VX</span>
            <span class="d3-11__name">Vector Pass</span>
            <span class="d3-11__serial">No. 0117 / 5000</span>
          </div>
          <span class="d3-11__vector" aria-hidden="true"></span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-11 {
  --d3-11-bg: #17151c;
  --d3-11-surf: #201d28;
  --d3-11-line: #35303f;
  --d3-11-ink: #f2eff7;
  --d3-11-mut: #a49cb4;
  --d3-11-acc: #a26bff;
  --d3-11-acc: oklch(70% 0.19 296);
  --d3-11-acc2: #4de0d4;
  --d3-11-acc2: oklch(84% 0.13 186);
  --d3-11-spin: 14s;
  --d3-11-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(48rem 26rem at 84% -8%, color-mix(in oklab, var(--d3-11-acc) 26%, transparent), transparent 62%), radial-gradient(40rem 22rem at -4% 100%, color-mix(in oklab, var(--d3-11-acc2) 18%, transparent), transparent 60%), var(--d3-11-bg);
  color: var(--d3-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-11 *,
.d3-11 *::before,
.d3-11 *::after {
  box-sizing: border-box;
}

.d3-11__sr {
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

.d3-11:has(.d3-11__theme-input:checked) {
  --d3-11-bg: #f4f2f8;
  --d3-11-surf: #ffffff;
  --d3-11-line: #ded8e8;
  --d3-11-ink: #15121b;
  --d3-11-mut: #625a70;
  --d3-11-acc: #6a29d6;
  --d3-11-acc: oklch(48% 0.22 296);
  --d3-11-acc2: #007f77;
  --d3-11-acc2: oklch(52% 0.1 186);
}

@media (prefers-color-scheme: light) {
  .d3-11:has(.d3-11__theme-input:checked) {
    --d3-11-bg: #f4f2f8;
    --d3-11-surf: #ffffff;
    --d3-11-line: #ded8e8;
    --d3-11-ink: #15121b;
    --d3-11-mut: #625a70;
    --d3-11-acc: #6a29d6;
    --d3-11-acc: oklch(48% 0.22 296);
    --d3-11-acc2: #007f77;
    --d3-11-acc2: oklch(52% 0.1 186);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-11:has(.d3-11__theme-input:checked) {
    --d3-11-bg: #f4f2f8;
    --d3-11-surf: #ffffff;
    --d3-11-line: #ded8e8;
    --d3-11-ink: #15121b;
    --d3-11-mut: #625a70;
    --d3-11-acc: #6a29d6;
    --d3-11-acc: oklch(48% 0.22 296);
    --d3-11-acc2: #007f77;
    --d3-11-acc2: oklch(52% 0.1 186);
  }
}

.d3-11__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-11__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-11-line);
  border-radius: 14px;
  background: var(--d3-11-surf);
  color: var(--d3-11-ink);
  cursor: pointer;
}

.d3-11__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-11__theme-input:focus-visible + .d3-11__theme-label {
  outline: 2px solid var(--d3-11-acc);
  outline-offset: 3px;
}

.d3-11__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-11__viewport {
  inline-size: 100%;
  max-inline-size: 62rem;
  overflow: hidden;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  align-items: center;
  gap: clamp(1rem, 3.5vw, 2rem);
  padding: clamp(1rem, 3.5vw, 2rem);
  border: 1px solid var(--d3-11-line);
  border-radius: 26px;
  background: color-mix(in oklab, var(--d3-11-surf) 76%, transparent);
  box-shadow: 0 40px 90px -50px #000;
}

.d3-11__panel {
  display: grid;
  gap: 0.55rem;
}

.d3-11__kicker {
  font: 700 0.64rem/1.4 var(--d3-11-font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--d3-11-acc2);
}

.d3-11__title {
  font: 700 clamp(1.25rem, 4vw, 2rem)/1.08 system-ui, sans-serif;
  letter-spacing: -0.02em;
}

.d3-11__copy {
  margin: 0;
  font: 500 clamp(0.75rem, 2vw, 0.85rem)/1.55 system-ui, sans-serif;
  color: var(--d3-11-mut);
  text-wrap: pretty;
}

.d3-11__copy code {
  font: 600 0.95em/1 var(--d3-11-font-display);
  color: var(--d3-11-acc);
}

.d3-11__read {
  margin: 0.2rem 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.d3-11__read div {
  padding: 0.45rem 0.7rem;
  border: 1px solid var(--d3-11-line);
  border-radius: 12px;
  background: color-mix(in oklab, var(--d3-11-surf) 70%, transparent);
}

.d3-11__read dt {
  font: 700 0.58rem/1.4 var(--d3-11-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--d3-11-mut);
}

.d3-11__read dd {
  margin: 0;
  font: 600 0.85rem/1.2 var(--d3-11-font-display);
  color: var(--d3-11-ink);
}

.d3-11__legend {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  font: 500 0.7rem/1.2 var(--d3-11-font-display);
  color: var(--d3-11-mut);
}

.d3-11__legend li {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.d3-11__key {
  inline-size: 0.65rem;
  block-size: 0.65rem;
  border-radius: 999px;
}

.d3-11__key--x {
  background: var(--d3-11-acc);
}

.d3-11__key--y {
  background: var(--d3-11-acc2);
}

.d3-11__key--z {
  background: color-mix(in oklab, var(--d3-11-acc) 50%, var(--d3-11-acc2));
}

.d3-11__scene {
  perspective: 1000px;
  perspective-origin: 50% 45%;
  block-size: clamp(15rem, 40vw, 20rem);
  display: grid;
  place-items: center;
}

.d3-11__rig {
  position: relative;
  transform-style: preserve-3d;
  display: grid;
  place-items: center;
}

.d3-11__badge {
  position: relative;
  inline-size: clamp(9rem, 26vw, 12rem);
  aspect-ratio: 0.78;
  padding: clamp(0.8rem, 2.4vw, 1.1rem);
  display: grid;
  align-content: end;
  gap: 0.15rem;
  overflow: hidden;
  border-radius: 18px;
  color: #fff;
  background: linear-gradient(150deg, #2a1c48, #120f1c 60%);
  border: 1px solid color-mix(in oklab, var(--d3-11-acc) 45%, transparent);
  box-shadow: 0 30px 60px -26px #000, inset 0 1px 0 rgba(255, 255, 255, 0.14);
  animation: d3-11-tumble var(--d3-11-spin) linear infinite;
}

@keyframes d3-11-tumble {
  from {
    transform: rotate3d(1, 1, 0.35, 0deg);
  }

  to {
    transform: rotate3d(1, 1, 0.35, 360deg);
  }
}

.d3-11__holo {
  position: absolute;
  inset: -30% -10%;
  background: conic-gradient(from 200deg, transparent, color-mix(in oklab, var(--d3-11-acc) 70%, transparent), color-mix(in oklab, var(--d3-11-acc2) 65%, transparent), transparent 70%);
  opacity: 0.5;
}

.d3-11__mark {
  position: absolute;
  inset-block-start: clamp(0.8rem, 2.4vw, 1.1rem);
  inset-inline-start: clamp(0.8rem, 2.4vw, 1.1rem);
  font: 800 clamp(1.4rem, 4.5vw, 2rem)/1 system-ui, sans-serif;
  letter-spacing: -0.04em;
}

.d3-11__name {
  position: relative;
  font: 700 clamp(0.85rem, 2.4vw, 1rem)/1.1 system-ui, sans-serif;
}

.d3-11__serial {
  position: relative;
  font: 500 0.64rem/1.2 var(--d3-11-font-display);
  color: rgba(255, 255, 255, 0.7);
}

.d3-11__vector {
  position: absolute;
  inline-size: 132%;
  block-size: 2px;
  border-radius: 2px;
  background: linear-gradient(90deg, transparent, var(--d3-11-acc2), transparent);
  transform: rotateZ(-38deg) translateZ(-1px);
  opacity: 0.8;
}

@media (prefers-reduced-motion: reduce) {
  .d3-11__badge {
    animation: none;
    transform: rotate3d(1, 1, 0.35, 42deg);
  }
}
```
