---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/topographic-contour-line-flow/"
title: "Topographic Contour Line Flow"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Elevation lines that slowly reshape themselves, like a survey map redrawing itself."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Topographic Contour Line Flow
Source: https://codefronts.com/motion/css-background-animations/topographic-contour-line-flow/

Elevation lines that slowly reshape themselves, like a survey map redrawing itself. A stack of hard-stop repeating-radial-gradient rings is pushed through an SVG feDisplacementMap driven by fractal turbulence — the rings stop being circles and become a landscape. SMIL animates the noise seed inside the SVG, so the terrain flows continuously with no JavaScript at all.
## HTML
```html
<section class="bga-05" aria-label="Animated topographic contour line background demo">
  <svg class="bga-05__defs" aria-hidden="true" focusable="false">
    <filter id="bga-05-warp" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.004 0.009" numOctaves="3" seed="4" result="bga-05-n">
        <animate attributeName="seed" values="4;26;4" dur="38s" repeatCount="indefinite"/>
      </feTurbulence>
      <feDisplacementMap in="SourceGraphic" in2="bga-05-n" scale="180" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </svg>

  <div class="bga-05__terrain" aria-hidden="true"></div>
  <div class="bga-05__ridge" aria-hidden="true"></div>

  <div class="bga-05__stage">
    <div class="bga-05__panel">
      <div class="bga-05__ticks" aria-hidden="true"><span></span><span></span><span></span></div>
      <p class="bga-05__eyebrow">Survey · 05 · 51.5072° N</p>
      <h1 class="bga-05__title">Contour lines that keep surveying.</h1>
      <p class="bga-05__sub">Hard-stop repeating gradients displaced by animated fractal noise. The rings are perfect circles until the filter decides otherwise.</p>
      <dl class="bga-05__legend">
        <div><dt>Interval</dt><dd>22 px</dd></div>
        <div><dt>Displacement</dt><dd>scale 180</dd></div>
        <div><dt>Period</dt><dd>38 s</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-05,
.bga-05 *,
.bga-05 *::before,
.bga-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-05-bg: oklch(0.965 0.012 120);
  --bga-05-line: oklch(0.55 0.055 150);
  --bga-05-acc: oklch(0.58 0.14 40);
  --bga-05-ink: oklch(0.24 0.02 150);
  background: var(--bga-05-bg);
  color: var(--bga-05-ink);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-05__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.bga-05__terrain,
.bga-05__ridge {
  position: absolute;
  inset: -18%;
  filter: url(#bga-05-warp);
  -webkit-mask-image: radial-gradient(115% 100% at 50% 50%,oklch(0 0 0) 42%,transparent 100%);
  mask-image: radial-gradient(115% 100% at 50% 50%,oklch(0 0 0) 42%,transparent 100%);
}

.bga-05__terrain {
  background-image: repeating-radial-gradient(circle at 28% 36%,transparent 0 21px,color-mix(in oklab,var(--bga-05-line) 42%,transparent) 21px 22.6px), repeating-radial-gradient(circle at 76% 68%,transparent 0 27px,color-mix(in oklab,var(--bga-05-line) 30%,transparent) 27px 28.5px);
}

.bga-05__ridge {
  translate: 6px 6px;
  opacity: .5;
  background-image: repeating-radial-gradient(circle at 28% 36%,transparent 0 21px,color-mix(in oklab,var(--bga-05-acc) 46%,transparent) 21px 22px);
}

.bga-05__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-05__panel {
  width: min(100%,660px);
  display: grid;
  gap: 16px;
  padding: clamp(26px,3.6vw,46px);
  border-radius: 4px;
  background: oklch(1 0 0/.72);
  border: 1px solid color-mix(in oklab,var(--bga-05-line) 32%,transparent);
  backdrop-filter: blur(6px) saturate(1.1);
  -webkit-backdrop-filter: blur(6px) saturate(1.1);
  box-shadow: 0 30px 70px -40px oklch(0.3 0.05 150/.6);
}

.bga-05__ticks {
  display: flex;
  gap: 5px;
}

.bga-05__ticks span {
  width: 26px;
  height: 3px;
  background: var(--bga-05-acc);
  opacity: .85;
}

.bga-05__ticks span:nth-child(2) {
  width: 14px;
  opacity: .5;
}

.bga-05__ticks span:nth-child(3) {
  width: 7px;
  opacity: .3;
}

.bga-05__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--bga-05-ink) 60%,transparent);
}

.bga-05__title {
  font-size: clamp(27px,5.2vw,50px);
  font-weight: 600;
  line-height: 1.05;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.bga-05__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: color-mix(in oklab,var(--bga-05-ink) 75%,transparent);
  text-wrap: pretty;
}

.bga-05__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 6px;
  padding-top: 16px;
  border-top: 1px dashed color-mix(in oklab,var(--bga-05-line) 40%,transparent);
}

.bga-05__legend div {
  display: grid;
  gap: 3px;
  min-width: 104px;
}

.bga-05__legend dt {
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--bga-05-ink) 52%,transparent);
}

.bga-05__legend dd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 14px;
  font-weight: 600;
  color: var(--bga-05-acc);
}

@media (prefers-reduced-motion: reduce) {
  .bga-05__terrain,
    .bga-05__ridge {
    filter: none;
    opacity: .55;
  }
}
```
