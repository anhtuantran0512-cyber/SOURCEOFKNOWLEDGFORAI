---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-staircase-step-loader/"
title: "CSS Staircase Step Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three step-progression CSS loaders — a cascading staircase bar chart, a 3×3 pulsing grid, and a multi-bar equaliser — representing data loading, task…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Staircase Step Loader
Source: https://codefronts.com/motion/css-loader-designs/css-staircase-step-loader/

Three step-progression CSS loaders — a cascading staircase bar chart, a 3×3 pulsing grid, and a multi-bar equaliser — representing data loading, task processing, and multi-step upload flows.
## HTML
```html
<div class="ld-17">
  <div class="ld-17__stage">
    <div class="ld-17__cell"><div class="ld-17__stairs"><div class="ld-17__step"></div><div class="ld-17__step"></div><div class="ld-17__step"></div><div class="ld-17__step"></div><div class="ld-17__step"></div></div>
```
## CSS
```css
.ld-17,
.ld-17 *,
.ld-17 *::before,
.ld-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-17 {
  --bg: #0f1923;
  --c1: #f0db4f;
  --c2: #e8834a;
  --c3: #4ecdc4;
  --c4: #ff6b6b;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-17__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-17__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-17__label {
  color: rgba(255,255,255,.35);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Staircase ascending */

.ld-17__stairs {
  display: flex;
  gap: 4px;
  align-items: flex-end;
  height: 60px;
}

.ld-17__step {
  width: 12px;
  border-radius: 2px 2px 0 0;
  animation: ld-17-step 1.4s ease-in-out infinite;
}

.ld-17__step:nth-child(1) {
  height: 10px;
  background: var(--c1);
  animation-delay: 0s;
}

.ld-17__step:nth-child(2) {
  height: 20px;
  background: var(--c2);
  animation-delay: .15s;
}

.ld-17__step:nth-child(3) {
  height: 32px;
  background: var(--c3);
  animation-delay: .3s;
}

.ld-17__step:nth-child(4) {
  height: 44px;
  background: var(--c4);
  animation-delay: .45s;
}

.ld-17__step:nth-child(5) {
  height: 56px;
  background: var(--c1);
  animation-delay: .6s;
}

@keyframes ld-17-step {
  0%,
    100% {
    opacity: .3;
    transform: scaleY(.8);
  }

  50% {
    opacity: 1;
    transform: scaleY(1);
  }
}
/* Tetris-style blocks */

.ld-17__tetris {
  width: 60px;
  height: 60px;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 3px;
}

.ld-17__block {
  border-radius: 3px;
  background: rgba(255,255,255,.06);
  animation: ld-17-block 2.1s ease-in-out infinite;
}

.ld-17__block:nth-child(1) {
  animation-delay: 0s;
  background: rgba(240,219,79,.12);
}

.ld-17__block:nth-child(2) {
  animation-delay: .14s;
}

.ld-17__block:nth-child(3) {
  animation-delay: .28s;
  background: rgba(78,205,196,.12);
}

.ld-17__block:nth-child(4) {
  animation-delay: .42s;
}

.ld-17__block:nth-child(5) {
  animation-delay: .56s;
  background: rgba(255,107,107,.12);
}

.ld-17__block:nth-child(6) {
  animation-delay: .70s;
}

.ld-17__block:nth-child(7) {
  animation-delay: .84s;
  background: rgba(240,219,79,.12);
}

.ld-17__block:nth-child(8) {
  animation-delay: .98s;
}

.ld-17__block:nth-child(9) {
  animation-delay: 1.12s;
  background: rgba(78,205,196,.12);
}

@keyframes ld-17-block {
  0%,
    100% {
    opacity: .15;
  }

  50% {
    opacity: 1;
    transform: scale(1.05);
  }
}
/* Equalizer */

.ld-17__eq {
  display: flex;
  gap: 5px;
  align-items: center;
  height: 60px;
}

.ld-17__eq-bar {
  width: 10px;
  border-radius: 5px;
  background: var(--c3);
  animation: ld-17-eq 1s ease-in-out infinite;
}

.ld-17__eq-bar:nth-child(1) {
  animation-delay: 0s;
}

.ld-17__eq-bar:nth-child(2) {
  animation-delay: .1s;
  background: var(--c4);
}

.ld-17__eq-bar:nth-child(3) {
  animation-delay: .2s;
}

.ld-17__eq-bar:nth-child(4) {
  animation-delay: .3s;
  background: var(--c1);
}

.ld-17__eq-bar:nth-child(5) {
  animation-delay: .4s;
}

@keyframes ld-17-eq {
  0% {
    height: 8px;
  }

  25% {
    height: 40px;
  }

  50% {
    height: 20px;
  }

  75% {
    height: 55px;
  }

  100% {
    height: 8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-17__step,
    .ld-17__block,
    .ld-17__eq-bar {
    animation: none;
  }
}
```
