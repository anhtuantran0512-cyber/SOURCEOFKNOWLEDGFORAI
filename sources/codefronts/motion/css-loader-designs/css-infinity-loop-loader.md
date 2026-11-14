---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-infinity-loop-loader/"
title: "CSS Infinity Loop Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three infinity and loop CSS loaders — a lemniscate dot path, an SVG animateMotion tracer, and a Möbius counter-spin — creating hypnotic continuous-flow…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Infinity Loop Loader
Source: https://codefronts.com/motion/css-loader-designs/css-infinity-loop-loader/

Three infinity and loop CSS loaders — a lemniscate dot path, an SVG animateMotion tracer, and a Möbius counter-spin — creating hypnotic continuous-flow loading indicators.
## HTML
```html
<div class="ld-18">
  <div class="ld-18__stage">
    <div class="ld-18__cell">
      <div class="ld-18__lemniscate">
        <div class="ld-18__lem-track">
          <div class="ld-18__lem-dot"></div>
          <div class="ld-18__lem-dot"></div>
          <div class="ld-18__lem-dot"></div>
        </div>
```
## CSS
```css
.ld-18,
.ld-18 *,
.ld-18 *::before,
.ld-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-18 {
  --bg: #05050a;
  --c1: #00e5ff;
  --c2: #ff1744;
  --c3: #76ff03;
  --c4: #ffea00;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-18__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-18__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-18__label {
  color: rgba(255,255,255,.3);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Figure-8 / Infinity */

.ld-18__infinity {
  width: 100px;
  height: 50px;
  position: relative;
}

.ld-18__infinity svg {
  width: 100px;
  height: 50px;
}

.ld-18__inf-path {
  fill: none;
  stroke: rgba(0,229,255,.15);
  stroke-width: 3;
}

.ld-18__inf-dot {
  animation: ld-18-inf-move 2s linear infinite;
}

@keyframes ld-18-inf-move {
  0% {
    offset-distance: 0%;
  }

  100% {
    offset-distance: 100%;
  }
}
/* Lemniscate dot tracker */

.ld-18__lemniscate {
  width: 110px;
  height: 55px;
  position: relative;
}

.ld-18__lem-track {
  position: absolute;
  inset: 0;
}

.ld-18__lem-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--c1);
  box-shadow: 0 0 10px var(--c1);
  position: absolute;
  animation: ld-18-lem 2.4s ease-in-out infinite;
}

.ld-18__lem-dot:nth-child(1) {
  animation-delay: 0s;
}

.ld-18__lem-dot:nth-child(2) {
  animation-delay: .8s;
  background: var(--c2);
  box-shadow: 0 0 10px var(--c2);
}

.ld-18__lem-dot:nth-child(3) {
  animation-delay: 1.6s;
  background: var(--c3);
  box-shadow: 0 0 10px var(--c3);
}

@keyframes ld-18-lem {
  0% {
    top: 22px;
    left: 50px;
  }

  12.5% {
    top: 2px;
    left: 80px;
  }

  25% {
    top: 22px;
    left: 100px;
  }

  37.5% {
    top: 42px;
    left: 80px;
  }

  50% {
    top: 22px;
    left: 50px;
  }

  62.5% {
    top: 2px;
    left: 20px;
  }

  75% {
    top: 22px;
    left: 0px;
  }

  87.5% {
    top: 42px;
    left: 20px;
  }

  100% {
    top: 22px;
    left: 50px;
  }
}
/* Möbius strip illusion */

.ld-18__mobius {
  width: 90px;
  height: 45px;
  position: relative;
}

.ld-18__mobius::before,
.ld-18__mobius::after {
  content: '';
  position: absolute;
  border-radius: 50px;
  border: 4px solid transparent;
}

.ld-18__mobius::before {
  width: 40px;
  height: 40px;
  top: 0;
  left: 0;
  border-top-color: var(--c4);
  border-left-color: var(--c4);
  animation: ld-18-mob1 2s ease-in-out infinite;
}

.ld-18__mobius::after {
  width: 40px;
  height: 40px;
  top: 0;
  right: 0;
  border-bottom-color: var(--c2);
  border-right-color: var(--c2);
  animation: ld-18-mob2 2s ease-in-out infinite;
}

@keyframes ld-18-mob1 {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}

@keyframes ld-18-mob2 {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(-360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-18__inf-dot,
    .ld-18__lem-dot,
    .ld-18__mobius::before,
    .ld-18__mobius::after {
    animation: none;
  }
}
```
