---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/retro-cyberpunk-grid-synthwave-horizon/"
title: "Synthwave 3D Retro Grid"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The outrun horizon: a real 3D floor built with perspective and rotateX, scrolling toward you forever, under a slit-scanned neon sun and a chrome horizon glow."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Synthwave 3D Retro Grid
Source: https://codefronts.com/motion/css-background-animations/retro-cyberpunk-grid-synthwave-horizon/

The outrun horizon: a real 3D floor built with perspective and rotateX, scrolling toward you forever, under a slit-scanned neon sun and a chrome horizon glow. The infinite scroll is a single trick — translate the grid by exactly one cell in Z-space — and because the plane is genuinely rotated in 3D, the perspective convergence is correct rather than faked with a skew.
## HTML
```html
<section class="bga-21" aria-label="Synthwave 3D retro grid background demo">
  <div class="bga-21__sky" aria-hidden="true"></div>
  <div class="bga-21__stars" aria-hidden="true"></div>
  <div class="bga-21__sun" aria-hidden="true"></div>
  <div class="bga-21__haze" aria-hidden="true"></div>

  <div class="bga-21__scene" aria-hidden="true">
    <div class="bga-21__floor"></div>
  </div>
  <div class="bga-21__horizon" aria-hidden="true"></div>

  <div class="bga-21__stage">
    <div class="bga-21__copy">
      <p class="bga-21__eyebrow">Perspective · rotateX(78deg) · 21</p>
      <h1 class="bga-21__title">OUTRUN</h1>
      <p class="bga-21__sub">A genuinely 3D plane, not a skew. The velocity gradient from near to far comes free with the projection — that is the part your eye reads as speed.</p>
      <div class="bga-21__gauges">
        <span>perspective <b>340px</b></span>
        <span>cell <b>60px</b></span>
        <span>loop <b>1.4s</b></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-21,
.bga-21 *,
.bga-21 *::before,
.bga-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-21-line: oklch(0.78 0.22 330);
  --bga-21-glow: oklch(0.72 0.2 300);
  --bga-21-hot: oklch(0.86 0.2 60);
  background: oklch(0.1 0.04 292);
  color: oklch(0.98 0.02 320);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-21__sky {
  position: absolute;
  inset: 0 0 42% 0;
  background: linear-gradient(180deg,oklch(0.1 0.05 292) 0%,oklch(0.2 0.1 300) 44%,oklch(0.4 0.16 330) 78%,oklch(0.56 0.2 350) 100%);
}

.bga-21__stars {
  position: absolute;
  inset: 0 0 52% 0;
  opacity: .6;
  background-image: radial-gradient(oklch(1 0 0/.85) .9px,transparent 1.1px),radial-gradient(oklch(0.9 0.06 320/.6) .7px,transparent 1px);
  background-size: 130px 130px,77px 77px;
  background-position: 0 0,38px 52px;
  animation: bga-21-tw 6s ease-in-out infinite alternate;
}

@keyframes bga-21-tw {
  from {
    opacity: .35;
  }

  to {
    opacity: .75;
  }
}

.bga-21__sun {
  position: absolute;
  left: 50%;
  bottom: 41%;
  translate: -50% 0;
  width: min(46vmin,380px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: linear-gradient(180deg,var(--bga-21-hot) 0%,oklch(0.78 0.22 30) 42%,oklch(0.62 0.25 8) 74%,oklch(0.52 0.24 340) 100%);
  -webkit-mask-image: linear-gradient(oklch(0 0 0) 0 46%,transparent 46%),repeating-linear-gradient(oklch(0 0 0) 0 9px,transparent 9px 15px);
  mask-image: linear-gradient(oklch(0 0 0) 0 46%,transparent 46%),repeating-linear-gradient(oklch(0 0 0) 0 9px,transparent 9px 15px);
  -webkit-mask-composite: source-over;
  mask-composite: add;
  filter: drop-shadow(0 0 70px color-mix(in oklab,var(--bga-21-hot) 55%,transparent));
  animation: bga-21-pulse 7s ease-in-out infinite alternate;
}

@keyframes bga-21-pulse {
  to {
    filter: drop-shadow(0 0 110px color-mix(in oklab,var(--bga-21-hot) 75%,transparent));
  }
}

.bga-21__haze {
  position: absolute;
  inset: 0 0 30% 0;
  pointer-events: none;
  mix-blend-mode: screen;
  opacity: .5;
  background: radial-gradient(70% 40% at 50% 100%,color-mix(in oklab,var(--bga-21-glow) 55%,transparent),transparent 72%);
}

.bga-21__scene {
  position: absolute;
  inset-inline: -30%;
  inset-block-end: 0;
  height: 44%;
  perspective: 340px;
  perspective-origin: 50% 0%;
  -webkit-mask-image: linear-gradient(transparent,oklch(0 0 0) 16%);
  mask-image: linear-gradient(transparent,oklch(0 0 0) 16%);
}

.bga-21__floor {
  position: absolute;
  inset: 0;
  transform: rotateX(78deg);
  transform-origin: 50% 0%;
  background-color: oklch(0.12 0.05 300);
  background-image: linear-gradient(color-mix(in oklab,var(--bga-21-line) 90%,transparent) 2px,transparent 2px), linear-gradient(90deg,color-mix(in oklab,var(--bga-21-line) 90%,transparent) 2px,transparent 2px);
  background-size: 60px 60px;
  animation: bga-21-run 1.4s linear infinite;
}

@keyframes bga-21-run {
  to {
    background-position: 0 60px;
  }
}

.bga-21__horizon {
  position: absolute;
  inset-inline: 0;
  bottom: 43.4%;
  height: 2px;
  background: linear-gradient(90deg,transparent,var(--bga-21-hot),oklch(1 0 0),var(--bga-21-line),transparent);
  box-shadow: 0 0 26px 5px color-mix(in oklab,var(--bga-21-line) 55%,transparent);
}

.bga-21__stage {
  position: relative;
  z-index: 5;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px) clamp(22px,5vw,68px) 46vh;
}

.bga-21__copy {
  width: min(100%,660px);
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
}

.bga-21__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: oklch(0.9 0.12 320);
}

.bga-21__title {
  font-size: clamp(44px,13vw,142px);
  font-weight: 800;
  letter-spacing: .06em;
  line-height: .9;
  background: linear-gradient(180deg,oklch(0.99 0.03 90) 0 42%,var(--bga-21-hot) 52%,oklch(0.66 0.25 350) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 0 26px color-mix(in oklab,var(--bga-21-line) 55%,transparent));
}

.bga-21__sub {
  max-width: 48ch;
  font-size: clamp(13px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.95 0.02 320/.8);
  text-wrap: pretty;
  text-shadow: 0 1px 18px oklch(0.1 0.04 300/.9);
}

.bga-21__gauges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 6px;
}

.bga-21__gauges span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 13px;
  color: oklch(1 0 0/.7);
  background: oklch(0.2 0.06 300/.45);
  border: 1px solid color-mix(in oklab,var(--bga-21-line) 34%,transparent);
}

.bga-21__gauges b {
  color: oklch(0.94 0.1 330);
}

@media (prefers-reduced-motion: reduce) {
  .bga-21__floor,
    .bga-21__sun,
    .bga-21__stars {
    animation: none;
  }
}
```
