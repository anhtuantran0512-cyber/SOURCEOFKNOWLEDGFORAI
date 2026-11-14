---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-dot-chase-loader/"
title: "CSS Dot Chase Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four dot-based CSS loaders — a staggered bounce chase row, a spinning orbit ring, a hexagonal trail pulse, and animated wave bars — all driven by staggered…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Dot Chase Loader
Source: https://codefronts.com/motion/css-loader-designs/css-dot-chase-loader/

Four dot-based CSS loaders — a staggered bounce chase row, a spinning orbit ring, a hexagonal trail pulse, and animated wave bars — all driven by staggered animation-delay.
## HTML
```html
<div class="ld-02">
  <div class="ld-02__stage">
    <div class="ld-02__cell"><div class="ld-02__chase"><span></span><span></span><span></span><span></span><span></span></div><span class="ld-02__label">Dot Chase</span></div>
    <div class="ld-02__cell"><div class="ld-02__orbit"><span></span><span></span><span></span><span></span></div><span class="ld-02__label">Orbit Dots</span></div>
    <div class="ld-02__cell"><div class="ld-02__trail"><span></span><span></span><span></span><span></span><span></span><span></span></div><span class="ld-02__label">Trailing Dots</span></div>
    <div class="ld-02__cell"><div class="ld-02__flock"><span></span><span></span><span></span><span></span><span></span></div><span class="ld-02__label">Wave Bars</span></div>
  </div>
```
## CSS
```css
.ld-02,
.ld-02 *,
.ld-02 *::before,
.ld-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-02 {
  --bg: #0d1117;
  --c1: #f7c948;
  --c2: #f27121;
  --c3: #e94057;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-02__stage {
  display: flex;
  gap: 56px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-02__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-02__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Dot Chase */

.ld-02__chase {
  display: flex;
  gap: 8px;
  align-items: center;
}

.ld-02__chase span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--c1);
  animation: ld-02-chase 1.2s ease-in-out infinite;
}

.ld-02__chase span:nth-child(1) {
  animation-delay: 0s;
}

.ld-02__chase span:nth-child(2) {
  animation-delay: .15s;
  background: var(--c2);
}

.ld-02__chase span:nth-child(3) {
  animation-delay: .3s;
  background: var(--c3);
}

.ld-02__chase span:nth-child(4) {
  animation-delay: .45s;
  background: var(--c1);
}

.ld-02__chase span:nth-child(5) {
  animation-delay: .6s;
  background: var(--c2);
}

@keyframes ld-02-chase {
  0%,
    80%,
    100% {
    transform: scale(.6);
    opacity: .4;
  }

  40% {
    transform: scale(1.1);
    opacity: 1;
  }
}
/* Orbit dots */

.ld-02__orbit {
  width: 60px;
  height: 60px;
  position: relative;
  animation: ld-02-spin 1.5s linear infinite;
}

.ld-02__orbit span {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--c1);
}

.ld-02__orbit span:nth-child(1) {
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}

.ld-02__orbit span:nth-child(2) {
  top: 50%;
  right: 0;
  transform: translateY(-50%);
  background: var(--c2);
}

.ld-02__orbit span:nth-child(3) {
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  background: var(--c3);
}

.ld-02__orbit span:nth-child(4) {
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  background: var(--c1);
}

@keyframes ld-02-spin {
  to {
    transform: rotate(360deg);
  }
}
/* Trailing dots */

.ld-02__trail {
  width: 60px;
  height: 60px;
  position: relative;
}

.ld-02__trail span {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  animation: ld-02-trail 1.2s ease-in-out infinite;
}

.ld-02__trail span:nth-child(1) {
  background: var(--c1);
  animation-delay: 0s;
  top: 4px;
  left: 26px;
}

.ld-02__trail span:nth-child(2) {
  background: var(--c2);
  animation-delay: .1s;
  top: 10px;
  right: 4px;
}

.ld-02__trail span:nth-child(3) {
  background: var(--c3);
  animation-delay: .2s;
  bottom: 10px;
  right: 4px;
}

.ld-02__trail span:nth-child(4) {
  background: var(--c1);
  animation-delay: .3s;
  bottom: 4px;
  left: 26px;
}

.ld-02__trail span:nth-child(5) {
  background: var(--c2);
  animation-delay: .4s;
  bottom: 10px;
  left: 4px;
}

.ld-02__trail span:nth-child(6) {
  background: var(--c3);
  animation-delay: .5s;
  top: 10px;
  left: 4px;
}

@keyframes ld-02-trail {
  0%,
    100% {
    transform: scale(.4);
    opacity: .3;
  }

  50% {
    transform: scale(1);
    opacity: 1;
  }
}
/* Flocking dots */

.ld-02__flock {
  display: flex;
  gap: 6px;
  align-items: flex-end;
  height: 40px;
}

.ld-02__flock span {
  width: 10px;
  border-radius: 5px;
  background: var(--c2);
  animation: ld-02-flock 1s ease-in-out infinite;
}

.ld-02__flock span:nth-child(1) {
  height: 10px;
  animation-delay: 0s;
}

.ld-02__flock span:nth-child(2) {
  height: 20px;
  animation-delay: .1s;
  background: var(--c3);
}

.ld-02__flock span:nth-child(3) {
  height: 30px;
  animation-delay: .2s;
  background: var(--c1);
}

.ld-02__flock span:nth-child(4) {
  height: 20px;
  animation-delay: .3s;
  background: var(--c3);
}

.ld-02__flock span:nth-child(5) {
  height: 10px;
  animation-delay: .4s;
}

@keyframes ld-02-flock {
  0%,
    100% {
    transform: scaleY(.5);
    opacity: .5;
  }

  50% {
    transform: scaleY(1.3);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-02__chase span,
    .ld-02__orbit,
    .ld-02__trail span,
    .ld-02__flock span {
    animation: none;
  }
}
```
