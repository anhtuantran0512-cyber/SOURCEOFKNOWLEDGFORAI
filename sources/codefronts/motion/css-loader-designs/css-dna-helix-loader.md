---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-dna-helix-loader/"
title: "CSS DNA Helix Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three organic helix and spiral CSS loaders — a pulsing DNA ladder with rungs, a glowing helix ring stack, and a spiralling orbit chain — creating bio-tech…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS DNA Helix Loader
Source: https://codefronts.com/motion/css-loader-designs/css-dna-helix-loader/

Three organic helix and spiral CSS loaders — a pulsing DNA ladder with rungs, a glowing helix ring stack, and a spiralling orbit chain — creating bio-tech and data-processing aesthetics.
## HTML
```html
<div class="ld-06">
  <div class="ld-06__stage">
    <div class="ld-06__cell">
      <div class="ld-06__dna">
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
        <div class="ld-06__rung"><span></span><span></span><span></span></div>
      </div>
```
## CSS
```css
.ld-06,
.ld-06 *,
.ld-06 *::before,
.ld-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-06 {
  --bg: #020c1b;
  --c1: #00d2ff;
  --c2: #ff6b9d;
  --c3: #a8ff78;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-06__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-06__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-06__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* DNA Helix */

.ld-06__dna {
  display: flex;
  flex-direction: column;
  gap: 3px;
  align-items: center;
}

.ld-06__rung {
  display: flex;
  gap: 4px;
  align-items: center;
}

.ld-06__rung span {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}

.ld-06__rung span:nth-child(1) {
  background: var(--c1);
}

.ld-06__rung span:nth-child(2) {
  background: rgba(255,255,255,.1);
  flex: 1;
  height: 2px;
  border-radius: 1px;
}

.ld-06__rung span:nth-child(3) {
  background: var(--c2);
}

.ld-06__rung:nth-child(1) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: 0s;
}

.ld-06__rung:nth-child(2) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .1s;
}

.ld-06__rung:nth-child(3) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .2s;
}

.ld-06__rung:nth-child(4) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .3s;
}

.ld-06__rung:nth-child(5) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .4s;
}

.ld-06__rung:nth-child(6) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .5s;
}

.ld-06__rung:nth-child(7) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .6s;
}

.ld-06__rung:nth-child(8) {
  animation: ld-06-dna 1.2s ease-in-out infinite;
  animation-delay: .7s;
}

@keyframes ld-06-dna {
  0%,
    100% {
    transform: scaleX(1);
    opacity: .6;
  }

  50% {
    transform: scaleX(.3);
    opacity: 1;
  }
}
/* Helix ring stack */

.ld-06__helix {
  width: 50px;
  height: 80px;
  position: relative;
}

.ld-06__helix span {
  position: absolute;
  left: 50%;
  border-radius: 50%;
  transform: translateX(-50%);
  animation: ld-06-helix 1.5s ease-in-out infinite;
}

.ld-06__helix span:nth-child(1) {
  width: 40px;
  height: 10px;
  background: var(--c1);
  top: 0;
  animation-delay: 0s;
}

.ld-06__helix span:nth-child(2) {
  width: 30px;
  height: 9px;
  background: var(--c2);
  top: 12px;
  animation-delay: .1s;
}

.ld-06__helix span:nth-child(3) {
  width: 16px;
  height: 8px;
  background: var(--c1);
  top: 23px;
  animation-delay: .2s;
}

.ld-06__helix span:nth-child(4) {
  width: 8px;
  height: 8px;
  background: var(--c3);
  top: 34px;
  animation-delay: .3s;
}

.ld-06__helix span:nth-child(5) {
  width: 16px;
  height: 8px;
  background: var(--c2);
  top: 45px;
  animation-delay: .4s;
}

.ld-06__helix span:nth-child(6) {
  width: 30px;
  height: 9px;
  background: var(--c1);
  top: 56px;
  animation-delay: .5s;
}

.ld-06__helix span:nth-child(7) {
  width: 40px;
  height: 10px;
  background: var(--c2);
  top: 68px;
  animation-delay: .6s;
}

@keyframes ld-06-helix {
  0%,
    100% {
    opacity: .3;
  }

  50% {
    opacity: 1;
    box-shadow: 0 0 12px currentColor;
  }
}
/* Spiral */

.ld-06__spiral {
  width: 60px;
  height: 60px;
  position: relative;
}

.ld-06__spiral span {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  animation: ld-06-spiral 2s linear infinite;
}

.ld-06__spiral span:nth-child(1) {
  background: var(--c1);
  animation-delay: 0s;
}

.ld-06__spiral span:nth-child(2) {
  background: var(--c2);
  animation-delay: -.25s;
}

.ld-06__spiral span:nth-child(3) {
  background: var(--c3);
  animation-delay: -.5s;
}

.ld-06__spiral span:nth-child(4) {
  background: var(--c1);
  animation-delay: -.75s;
}

.ld-06__spiral span:nth-child(5) {
  background: var(--c2);
  animation-delay: -1s;
}

.ld-06__spiral span:nth-child(6) {
  background: var(--c3);
  animation-delay: -1.25s;
}

.ld-06__spiral span:nth-child(7) {
  background: var(--c1);
  animation-delay: -1.5s;
}

.ld-06__spiral span:nth-child(8) {
  background: var(--c2);
  animation-delay: -1.75s;
}

@keyframes ld-06-spiral {
  0% {
    transform: rotate(0deg) translateX(24px) scale(.4);
    opacity: 0;
  }

  20% {
    opacity: 1;
    transform: rotate(72deg) translateX(24px) scale(.7);
  }

  60% {
    transform: rotate(216deg) translateX(24px) scale(1);
  }

  80% {
    opacity: 1;
  }

  100% {
    transform: rotate(360deg) translateX(24px) scale(.4);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-06__rung,
    .ld-06__helix span,
    .ld-06__spiral span {
    animation: none;
  }
}
```
