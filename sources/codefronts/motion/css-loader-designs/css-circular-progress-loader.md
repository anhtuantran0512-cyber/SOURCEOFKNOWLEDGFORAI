---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-circular-progress-loader/"
title: "CSS Circular Progress Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four SVG-based circular progress loaders — a stroke-dashoffset arc, segmented arcs, a gauge semicircle, and radial concentric rings — covering all common…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Circular Progress Loader
Source: https://codefronts.com/motion/css-loader-designs/css-circular-progress-loader/

Four SVG-based circular progress loaders — a stroke-dashoffset arc, segmented arcs, a gauge semicircle, and radial concentric rings — covering all common circular-indicator design patterns.
## HTML
```html
<div class="ld-09">
  <div class="ld-09__stage">
    <div class="ld-09__cell">
      <div class="ld-09__svg-wrap">
        <svg viewBox="0 0 90 90"><circle class="ld-09__track" cx="45" cy="45" r="36"/><circle class="ld-09__prog" cx="45" cy="45" r="36"/></svg>
        <div class="ld-09__pct">78%</div>
      </div>
```
## CSS
```css
.ld-09,
.ld-09 *,
.ld-09 *::before,
.ld-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-09 {
  --bg: #0f172a;
  --c1: #818cf8;
  --c2: #34d399;
  --c3: #fb923c;
  --c4: #f472b6;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-09__stage {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-09__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.ld-09__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* SVG Circle progress */

.ld-09__svg-wrap {
  position: relative;
  width: 90px;
  height: 90px;
}

.ld-09__svg-wrap svg {
  width: 90px;
  height: 90px;
  transform: rotate(-90deg);
}

.ld-09__track {
  fill: none;
  stroke: rgba(255,255,255,.07);
  stroke-width: 6;
}

.ld-09__prog {
  fill: none;
  stroke: var(--c1);
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 226;
  animation: ld-09-dash 2s ease-in-out infinite;
}

@keyframes ld-09-dash {
  0% {
    stroke-dashoffset: 226;
    opacity: .6;
  }

  50% {
    stroke-dashoffset: 50;
    opacity: 1;
  }

  100% {
    stroke-dashoffset: 226;
    opacity: .6;
  }
}

.ld-09__pct {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  font-weight: 700;
  color: var(--c1);
}
/* Segmented ring */

.ld-09__seg-ring {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  position: relative;
}

.ld-09__seg-ring svg {
  width: 90px;
  height: 90px;
}

.ld-09__seg-arc {
  fill: none;
  stroke-width: 6;
  stroke-linecap: round;
}

.ld-09__seg-arc:nth-child(1) {
  stroke: var(--c2);
  stroke-dasharray: 40 226;
  stroke-dashoffset: 0;
  animation: ld-09-seg1 3s linear infinite;
}

.ld-09__seg-arc:nth-child(2) {
  stroke: var(--c3);
  stroke-dasharray: 40 226;
  stroke-dashoffset: -60;
  animation: ld-09-seg2 3s linear infinite;
}

.ld-09__seg-arc:nth-child(3) {
  stroke: var(--c4);
  stroke-dasharray: 40 226;
  stroke-dashoffset: -120;
  animation: ld-09-seg3 3s linear infinite;
}

@keyframes ld-09-seg1 {
  to {
    stroke-dashoffset: -226;
  }
}

@keyframes ld-09-seg2 {
  to {
    stroke-dashoffset: -286;
  }
}

@keyframes ld-09-seg3 {
  to {
    stroke-dashoffset: -346;
  }
}
/* Gauge */

.ld-09__gauge {
  width: 100px;
  height: 55px;
  position: relative;
  overflow: hidden;
}

.ld-09__gauge svg {
  width: 100px;
  height: 100px;
  transform: translateY(10px);
}

.ld-09__gauge-track {
  fill: none;
  stroke: rgba(255,255,255,.07);
  stroke-width: 8;
  stroke-dasharray: 125;
  stroke-dashoffset: -62.5;
}

.ld-09__gauge-fill {
  fill: none;
  stroke: var(--c3);
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: 125;
  stroke-dashoffset: -62.5;
  animation: ld-09-gauge 2.5s ease-in-out infinite;
}

@keyframes ld-09-gauge {
  0% {
    stroke-dashoffset: 0;
  }

  50% {
    stroke-dashoffset: -62.5;
  }

  100% {
    stroke-dashoffset: 0;
  }
}
/* Radial multi */

.ld-09__radial {
  width: 90px;
  height: 90px;
  position: relative;
}

.ld-09__radial svg {
  width: 90px;
  height: 90px;
  transform: rotate(-90deg);
}

.ld-09__r-track {
  fill: none;
  stroke: rgba(255,255,255,.05);
  stroke-linecap: round;
}

.ld-09__r-fill {
  fill: none;
  stroke-linecap: round;
  animation: ld-09-rdash 2s ease-in-out infinite;
}

.ld-09__r-fill:nth-child(2) {
  stroke: var(--c1);
  stroke-width: 5;
  stroke-dasharray: 200;
  animation-delay: 0s;
}

.ld-09__r-fill:nth-child(4) {
  stroke: var(--c2);
  stroke-width: 5;
  stroke-dasharray: 160;
  animation-delay: .3s;
}

.ld-09__r-fill:nth-child(6) {
  stroke: var(--c3);
  stroke-width: 5;
  stroke-dasharray: 120;
  animation-delay: .6s;
}

@keyframes ld-09-rdash {
  0% {
    stroke-dashoffset: 200;
    opacity: .5;
  }

  60% {
    stroke-dashoffset: 40;
    opacity: 1;
  }

  100% {
    stroke-dashoffset: 200;
    opacity: .5;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-09__prog,
    .ld-09__seg-arc,
    .ld-09__gauge-fill,
    .ld-09__r-fill {
    animation: none;
  }
}
```
