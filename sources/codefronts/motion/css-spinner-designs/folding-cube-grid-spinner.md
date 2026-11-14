---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/folding-cube-grid-spinner/"
title: "Folding Cube Grid Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A 3×3 grid of teal cubes each flip through two 90° rotation axes in sequence with staggered delays, creating a cascading wave of 3D folding tiles."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Folding Cube Grid Spinner
Source: https://codefronts.com/motion/css-spinner-designs/folding-cube-grid-spinner/

A 3×3 grid of teal cubes each flip through two 90° rotation axes in sequence with staggered delays, creating a cascading wave of 3D folding tiles.
## HTML
```html
<div class="sp-11">
  <div class="sp-11__grid">
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
    <div class="sp-11__cube"></div>
  </div>
</div>
```
## CSS
```css
.sp-11,
.sp-11 *,
.sp-11 *::before,
.sp-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-11 {
  --bg: #0a0a0a;
  --c: #64ffda;
  --glow: rgba(100,255,218,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-11__grid {
  display: grid;
  grid-template-columns: repeat(3,22px);
  grid-template-rows: repeat(3,22px);
  gap: 4px;
}

.sp-11__cube {
  width: 22px;
  height: 22px;
  background: var(--c);
  box-shadow: 0 0 8px var(--glow);
  border-radius: 2px;
  animation: sp-11-fold 1.8s ease-in-out infinite;
}

.sp-11__cube:nth-child(1) {
  animation-delay: 0s;
}

.sp-11__cube:nth-child(2) {
  animation-delay: 0.1s;
}

.sp-11__cube:nth-child(3) {
  animation-delay: 0.2s;
}

.sp-11__cube:nth-child(4) {
  animation-delay: 0.3s;
}

.sp-11__cube:nth-child(5) {
  animation-delay: 0.4s;
}

.sp-11__cube:nth-child(6) {
  animation-delay: 0.5s;
}

.sp-11__cube:nth-child(7) {
  animation-delay: 0.6s;
}

.sp-11__cube:nth-child(8) {
  animation-delay: 0.7s;
}

.sp-11__cube:nth-child(9) {
  animation-delay: 0.8s;
}

@keyframes sp-11-fold {
  0%,
    100% {
    transform: perspective(60px) rotateX(0deg) rotateY(0deg);
    opacity: 1;
  }

  33% {
    transform: perspective(60px) rotateX(-90deg) rotateY(0deg);
    opacity: 0.4;
  }

  66% {
    transform: perspective(60px) rotateX(-90deg) rotateY(90deg);
    opacity: 0.4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-11__cube {
    animation: none;
  }
}
```
