---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-cube-flip-3d-loader/"
title: "CSS Cube Flip 3D Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three three-dimensional CSS loaders — a six-face spinning cube, a folding grid of four squares, and a nested wireframe box — using CSS 3D transforms and…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Cube Flip 3D Loader
Source: https://codefronts.com/motion/css-loader-designs/css-cube-flip-3d-loader/

Three three-dimensional CSS loaders — a six-face spinning cube, a folding grid of four squares, and a nested wireframe box — using CSS 3D transforms and preserve-3d for depth.
## HTML
```html
<div class="ld-12">
  <div class="ld-12__stage">
    <div class="ld-12__cell">
      <div style="perspective:200px">
        <div class="ld-12__cube" style="position:relative">
          <div class="ld-12__face ld-12__face--front"></div>
          <div class="ld-12__face ld-12__face--back"></div>
          <div class="ld-12__face ld-12__face--left"></div>
          <div class="ld-12__face ld-12__face--right"></div>
          <div class="ld-12__face ld-12__face--top"></div>
          <div class="ld-12__face ld-12__face--bottom"></div>
        </div>
```
## CSS
```css
.ld-12,
.ld-12 *,
.ld-12 *::before,
.ld-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-12 {
  --bg: #12151e;
  --c1: #ff9f43;
  --c2: #ee5a24;
  --c3: #a29bfe;
  --c4: #6c5ce7;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
  perspective: 600px;
}

.ld-12__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-12__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-12__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Flip cube */

.ld-12__cube {
  width: 50px;
  height: 50px;
  transform-style: preserve-3d;
  animation: ld-12-cube-flip 2s ease-in-out infinite;
}

.ld-12__face {
  position: absolute;
  width: 50px;
  height: 50px;
  border: 2px solid var(--c1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-12__face--front {
  transform: translateZ(25px);
  background: rgba(255,159,67,.15);
}

.ld-12__face--back {
  transform: rotateY(180deg) translateZ(25px);
  background: rgba(255,159,67,.1);
}

.ld-12__face--left {
  transform: rotateY(-90deg) translateZ(25px);
  background: rgba(238,90,36,.1);
}

.ld-12__face--right {
  transform: rotateY(90deg) translateZ(25px);
  background: rgba(238,90,36,.15);
}

.ld-12__face--top {
  transform: rotateX(90deg) translateZ(25px);
  background: rgba(255,159,67,.05);
}

.ld-12__face--bottom {
  transform: rotateX(-90deg) translateZ(25px);
  background: rgba(238,90,36,.05);
}

@keyframes ld-12-cube-flip {
  0% {
    transform: rotateX(0) rotateY(0);
  }

  33% {
    transform: rotateX(90deg) rotateY(0);
  }

  66% {
    transform: rotateX(90deg) rotateY(90deg);
  }

  100% {
    transform: rotateX(180deg) rotateY(90deg);
  }
}
/* Folding squares */

.ld-12__fold {
  width: 40px;
  height: 40px;
  position: relative;
}

.ld-12__fold span {
  position: absolute;
  width: 18px;
  height: 18px;
  background: var(--c3);
  animation: ld-12-fold 2.4s ease-in-out infinite;
}

.ld-12__fold span:nth-child(1) {
  top: 0;
  left: 0;
  transform-origin: bottom right;
  animation-delay: 0s;
}

.ld-12__fold span:nth-child(2) {
  top: 0;
  right: 0;
  transform-origin: bottom left;
  animation-delay: .3s;
  background: rgba(162,155,254,.7);
}

.ld-12__fold span:nth-child(3) {
  bottom: 0;
  right: 0;
  transform-origin: top left;
  animation-delay: .6s;
  background: rgba(162,155,254,.5);
}

.ld-12__fold span:nth-child(4) {
  bottom: 0;
  left: 0;
  transform-origin: top right;
  animation-delay: .9s;
  background: rgba(162,155,254,.3);
}

@keyframes ld-12-fold {
  0%,
    10%,
    100% {
    transform: perspective(140px) rotateX(0) rotateY(0);
  }

  50% {
    transform: perspective(140px) rotateX(-180deg) rotateY(0);
  }
}
/* Rotating box */

.ld-12__box {
  width: 50px;
  height: 50px;
  border: 3px solid var(--c4);
  position: relative;
  animation: ld-12-box-spin 3s linear infinite;
  transform-style: preserve-3d;
}

.ld-12__box::before,
.ld-12__box::after {
  content: '';
  position: absolute;
  border: 3px solid rgba(108,92,231,.4);
}

.ld-12__box::before {
  inset: -12px;
  transform: rotateY(45deg);
  border-color: rgba(108,92,231,.3);
}

.ld-12__box::after {
  inset: -6px;
  transform: rotateX(45deg);
  border-color: rgba(108,92,231,.2);
}

@keyframes ld-12-box-spin {
  to {
    transform: rotateX(360deg) rotateY(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-12__cube,
    .ld-12__fold span,
    .ld-12__box {
    animation: none;
  }
}
```
