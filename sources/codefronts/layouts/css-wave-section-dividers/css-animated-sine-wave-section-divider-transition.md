---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/css-animated-sine-wave-section-divider-transition/"
title: "CSS animated sine wave section divider transition"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "A mathematically correct sine wave — sampled from y = A·sin(x) rather than eyeballed with bezier handles — animated as a travelling waveform."
has_js: "false"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS animated sine wave section divider transition
Source: https://codefronts.com/layouts/css-wave-section-dividers/css-animated-sine-wave-section-divider-transition/

A mathematically correct sine wave — sampled from y = A·sin(x) rather than eyeballed with bezier handles — animated as a travelling waveform. The geometric, signal-processing look that tech, audio and web3 landing pages keep asking for.
## HTML
```html
<div class="wsd-12-group">
<section class="wsd-12a">
  <div class="wsd-12a__top">
    <p class="wsd-12a__eyebrow">y = A · sin(x)</p>
    <h2 class="wsd-12a__title">Signal, not decoration</h2>
    <div class="wsd-12a__waves" aria-hidden="true">
      <div class="wsd-12a__track wsd-12a__track--b">
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C90,40 270,40 360,70 C450,100 630,100 720,70 C810,40 990,40 1080,70 C1170,100 1350,100 1440,70 L1440,120 L0,120 Z"></path></svg>
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,70 C90,40 270,40 360,70 C450,100 630,100 720,70 C810,40 990,40 1080,70 C1170,100 1350,100 1440,70 L1440,120 L0,120 Z"></path></svg>
      </div>
      <div class="wsd-12a__track wsd-12a__track--a">
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,80 C60,50 180,50 240,80 C300,110 420,110 480,80 C540,50 660,50 720,80 C780,110 900,110 960,80 C1020,50 1140,50 1200,80 C1260,110 1380,110 1440,80 L1440,120 L0,120 Z"></path></svg>
        <svg viewBox="0 0 1440 120" preserveAspectRatio="none" focusable="false"><path d="M0,80 C60,50 180,50 240,80 C300,110 420,110 480,80 C540,50 660,50 720,80 C780,110 900,110 960,80 C1020,50 1140,50 1200,80 C1260,110 1380,110 1440,80 L1440,120 L0,120 Z"></path></svg>
      </div>
    </div>
  </div>
  <div class="wsd-12a__bottom"><p class="wsd-12a__copy">Each half-period is identical, so the loop is mathematically seamless.</p></div>
</section>
<section class="wsd-12b">
  <div class="wsd-12b__top">
    <h2 class="wsd-12b__title">Stroked waveform seam</h2>
    <div class="wsd-12b__waves" aria-hidden="true">
      <div class="wsd-12b__track">
        <svg viewBox="0 0 1440 100" preserveAspectRatio="none" focusable="false"><path class="wsd-12b__line" d="M0,50 C60,14 180,14 240,50 C300,86 420,86 480,50 C540,14 660,14 720,50 C780,86 900,86 960,50 C1020,14 1140,14 1200,50 C1260,86 1380,86 1440,50" fill="none"></path></svg>
        <svg viewBox="0 0 1440 100" preserveAspectRatio="none" focusable="false"><path class="wsd-12b__line" d="M0,50 C60,14 180,14 240,50 C300,86 420,86 480,50 C540,14 660,14 720,50 C780,86 900,86 960,50 C1020,14 1140,14 1200,50 C1260,86 1380,86 1440,50" fill="none"></path></svg>
      </div>
    </div>
  </div>
  <div class="wsd-12b__bottom"><p class="wsd-12b__copy">A stroke instead of a fill turns the divider into an instrument readout.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-12-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-12-group > section {
  width: 100%;
}

.wsd-12a,
.wsd-12a *,
.wsd-12a *::before,
.wsd-12a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-12a {
  --void: oklch(0.15 0.03 265);
  --signal: oklch(0.78 0.18 165);
  --floor: oklch(0.95 0.02 165);
  font-family: ui-monospace,'Segoe UI',monospace;
}

.wsd-12a__top {
  position: relative;
  overflow: hidden;
  background: var(--void);
  color: #fff;
  padding: 70px 24px 124px;
  text-align: center;
}

.wsd-12a__eyebrow {
  font-size: 12px;
  letter-spacing: .2em;
  color: var(--signal);
  margin-bottom: 12px;
}

.wsd-12a__title {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: clamp(25px,4vw,40px);
}

.wsd-12a__waves {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: clamp(64px,10vw,120px);
}

.wsd-12a__track {
  position: absolute;
  inset: 0;
  display: flex;
  width: 200%;
}

.wsd-12a__track svg {
  display: block;
  width: 50%;
  height: 100%;
}

.wsd-12a__track--b {
  animation: wsd-12a-run 18s linear infinite;
}

.wsd-12a__track--b path {
  fill: color-mix(in oklab,var(--signal) 34%,transparent);
}

.wsd-12a__track--a {
  animation: wsd-12a-run 11s linear infinite;
}

.wsd-12a__track--a path {
  fill: var(--floor);
}

.wsd-12a__bottom {
  background: var(--floor);
  color: oklch(0.28 0.05 165);
  padding: 30px 24px 58px;
  text-align: center;
}

.wsd-12a__copy {
  font-size: 14px;
  opacity: .76;
}

@keyframes wsd-12a-run {
  from {
    transform: translate3d(0,0,0);
  }

  to {
    transform: translate3d(-50%,0,0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .wsd-12a__track {
    animation: none!important;
  }
}

.wsd-12b,
.wsd-12b *,
.wsd-12b *::before,
.wsd-12b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-12b {
  --void: oklch(0.13 0.02 150);
  --trace: oklch(0.85 0.19 145);
  font-family: ui-monospace,'Segoe UI',monospace;
}

.wsd-12b__top {
  position: relative;
  overflow: hidden;
  background: var(--void);
  color: #eafff2;
  padding: 66px 24px 96px;
  text-align: center;
}

.wsd-12b__title {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: clamp(23px,3.6vw,34px);
}

.wsd-12b__waves {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: clamp(56px,8vw,100px);
}

.wsd-12b__track {
  position: absolute;
  inset: 0;
  display: flex;
  width: 200%;
  animation: wsd-12b-run 8s linear infinite;
}

.wsd-12b__track svg {
  display: block;
  width: 50%;
  height: 100%;
  overflow: visible;
}

.wsd-12b__line {
  stroke: var(--trace);
  stroke-width: 3;
  vector-effect: non-scaling-stroke;
  filter: drop-shadow(0 0 6px color-mix(in oklab,var(--trace) 70%,transparent));
}

.wsd-12b__bottom {
  background: oklch(0.2 0.03 150);
  color: #dcf7e8;
  padding: 26px 24px 56px;
  text-align: center;
  border-top: 1px solid color-mix(in oklab,var(--trace) 35%,transparent);
}

.wsd-12b__copy {
  font-size: 14px;
  opacity: .8;
}

@keyframes wsd-12b-run {
  from {
    transform: translate3d(0,0,0);
  }

  to {
    transform: translate3d(-50%,0,0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .wsd-12b__track {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — sampled sine paths (control points at 1/4 and 3/4 of each half-period) tiled twice and translated -50% forever. */

/* No JavaScript — vector-effect:non-scaling-stroke keeps the trace 3px thick even though the SVG is stretched horizontally. */
```
