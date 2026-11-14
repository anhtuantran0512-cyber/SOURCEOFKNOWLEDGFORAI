---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/3d-transform-perspective-layer-parallax/"
title: "3D Transform Perspective Layer Parallax"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "The canonical perspective-based parallax, rebuilt as a documented reference: a scroll container with perspective: 1px, layers pushed back with translateZ and…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Transform Perspective Layer Parallax
Source: https://codefronts.com/motion/css-parallax-designs/3d-transform-perspective-layer-parallax/

The canonical perspective-based parallax, rebuilt as a documented reference: a scroll container with perspective: 1px, layers pushed back with translateZ and scaled up to compensate, and an annotation panel that names what each declaration is doing. No scroll listener and no scroll-timeline — the depth is a property of the 3D scene itself.
## HTML
```html
<div class="plx-08">
  <div class="plx-08__viewport">
    <div class="plx-08__scene">
      <div class="plx-08__group plx-08__group--back" aria-hidden="true">
        <div class="plx-08__stars"></div>
      </div>
      <div class="plx-08__group plx-08__group--mid" aria-hidden="true">
        <div class="plx-08__mesh"></div>
      </div>
      <div class="plx-08__group plx-08__group--front">
        <div class="plx-08__panel">
          <p class="plx-08__prompt">~/parallax $ cat perspective.css</p>
          <h1 class="plx-08__h1">perspective: 1px</h1>
          <pre class="plx-08__code">.viewport { perspective: 1px; overflow-y: auto; }
.back    { transform: translateZ(-2px) scale(3); }
.front   { transform: translateZ(0); }</pre>
          <p class="plx-08__note">Depth ratio = 1 + |z| / perspective. At z = -2px under a 1px camera the back plane renders at 1/3 size and moves at 1/3 the rate, so it is scaled by 3 to fill the frame again.</p>
        </div>
      </div>
      <section class="plx-08__doc">
        <h2 class="plx-08__h2">Why this still ships</h2>
        <p class="plx-08__p">No listener, no timeline, no feature query. The browser projects a fixed 3D scene and scrolling moves the camera through it — support goes back to 2013, which still matters for long-tail Safari.</p>
        <h2 class="plx-08__h2">What it costs</h2>
        <p class="plx-08__p">The perspective ancestor becomes a containing block. Anything position: fixed inside this scene anchors here, not to the viewport, and sticky children behave unpredictably. Scroll this inner container, not the page.</p>
        <dl class="plx-08__table">
          <div class="plx-08__row"><dt>z = 0</dt><dd>1.0x rate · foreground</dd></div>
          <div class="plx-08__row"><dt>z = -1px</dt><dd>0.5x rate · scale(2)</dd></div>
          <div class="plx-08__row"><dt>z = -2px</dt><dd>0.33x rate · scale(3)</dd></div>
        </dl>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
.plx-08 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "JetBrains Mono", "IBM Plex Mono", ui-monospace, "SFMono-Regular", monospace;
  --bg: #04070a;
  --ink: #b8ffd0;
  --dim: #4f9c72;
  --accent: #7dff9b;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-display);
}

.plx-08 * {
  box-sizing: border-box;
}

.plx-08__viewport {
  block-size: 100svh;
  overflow-x: hidden;
  overflow-y: auto;
  perspective: 1px;
  perspective-origin: 0 0;
  -webkit-overflow-scrolling: touch;
  background: var(--bg);
}

.plx-08__scene {
  position: relative;
  transform-style: preserve-3d;
}

.plx-08__group {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
  pointer-events: none;
}

.plx-08__group--back {
  transform: translateZ(-2px) scale(3);
  transform-origin: 0 0;
}

.plx-08__group--mid {
  transform: translateZ(-1px) scale(2);
  transform-origin: 0 0;
}

.plx-08__group--front {
  position: relative;
  transform: translateZ(0);
  pointer-events: auto;
}

.plx-08__stars {
  block-size: 100svh;
  background-image: radial-gradient(1.5px 1.5px at 12% 22%, #7dff9b 40%, transparent 42%), radial-gradient(1.5px 1.5px at 68% 14%, #3ddc84 40%, transparent 42%), radial-gradient(1.5px 1.5px at 34% 62%, #b8ffd0 40%, transparent 42%), radial-gradient(1.5px 1.5px at 86% 48%, #45a86a 40%, transparent 42%), radial-gradient(1.5px 1.5px at 52% 84%, #7dff9b 40%, transparent 42%), radial-gradient(1.5px 1.5px at 22% 92%, #3ddc84 40%, transparent 42%);
}

.plx-08__mesh {
  block-size: 100svh;
  background-image: linear-gradient(rgba(125,255,155,0.14) 1px, transparent 1px), linear-gradient(90deg, rgba(125,255,155,0.14) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: linear-gradient(to bottom, transparent 12%, #000 58%, transparent 96%);
}

.plx-08__group--front {
  padding: clamp(16px, 4vw, 44px);
  min-block-size: 100svh;
  display: flex;
  align-items: center;
}

.plx-08__panel {
  inline-size: 100%;
  max-inline-size: 46rem;
  min-inline-size: 0;
  padding: clamp(14px, 3vw, 24px);
  border: 1px solid #1d5238;
  background: rgba(4,10,7,0.86);
  position: relative;
}

.plx-08__panel::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(to bottom, rgba(125,255,155,0.05) 0 1px, transparent 1px 3px);
}

.plx-08__prompt {
  margin: 0 0 10px;
  font-size: 11.5px;
  color: var(--dim);
  letter-spacing: 0.04em;
}

.plx-08__h1 {
  margin: 0 0 14px;
  font-size: clamp(22px, 5vw, 40px);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--accent);
}

.plx-08__code {
  margin: 0 0 14px;
  padding: 12px;
  overflow-x: auto;
  border-inline-start: 2px solid var(--accent);
  background: #071310;
  font-size: 12.5px;
  line-height: 1.7;
  color: #c9ffdb;
}

.plx-08__note {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--dim);
  max-inline-size: 34rem;
}

.plx-08__doc {
  position: relative;
  background: var(--bg);
  padding: clamp(22px, 5vw, 56px) clamp(16px, 4vw, 44px) 90px;
  border-top: 1px solid #17402c;
}

.plx-08__h2 {
  margin: 0 0 8px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-08__p {
  margin: 0 0 22px;
  max-inline-size: 42rem;
  font-size: 13px;
  line-height: 1.75;
  color: #86c9a3;
}

.plx-08__table {
  margin: 0;
  display: grid;
  gap: 6px;
  max-inline-size: 30rem;
}

.plx-08__row {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  border-bottom: 1px dashed #1d5238;
  padding-block: 7px;
  min-inline-size: 0;
}

.plx-08__row dt {
  font-size: 12.5px;
  color: var(--accent);
}

.plx-08__row dd {
  margin: 0;
  font-size: 12.5px;
  color: var(--dim);
  text-align: end;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .plx-08__viewport {
    perspective: none;
  }

  .plx-08__group {
    position: relative;
    inset: auto;
    transform: none !important;
  }

  .plx-08__group--back,
    .plx-08__group--mid {
    display: none;
  }
}
```
