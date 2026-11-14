---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/particle-scatter-burst-spinner/"
title: "Particle Scatter Burst Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Eight coloured particles radiate outward from a central white core, fading and shrinking to nothing at the edge of their orbit while the whole assembly…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Particle Scatter Burst Spinner
Source: https://codefronts.com/motion/css-spinner-designs/particle-scatter-burst-spinner/

Eight coloured particles radiate outward from a central white core, fading and shrinking to nothing at the edge of their orbit while the whole assembly rotates slowly.
## HTML
```html
<div class="sp-20">
  <div class="sp-20__burst">
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__particle"></div>
    <div class="sp-20__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-20,
.sp-20 *,
.sp-20 *::before,
.sp-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-20 {
  --bg: #08050f;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-20__burst {
  position: relative;
  width: 100px;
  height: 100px;
  animation: sp-20-rotate 3s linear infinite;
}

.sp-20__particle {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin: -4px 0 0 -4px;
  animation: sp-20-scatter 1.5s ease-out infinite;
}

.sp-20__particle:nth-child(1) {
  background: #ff6b6b;
  animation-delay: 0s;
  transform: rotate(0deg);
}

.sp-20__particle:nth-child(2) {
  background: #ffd93d;
  animation-delay: 0.1s;
  transform: rotate(45deg);
}

.sp-20__particle:nth-child(3) {
  background: #6bcb77;
  animation-delay: 0.2s;
  transform: rotate(90deg);
}

.sp-20__particle:nth-child(4) {
  background: #4d96ff;
  animation-delay: 0.3s;
  transform: rotate(135deg);
}

.sp-20__particle:nth-child(5) {
  background: #ff6b6b;
  animation-delay: 0.4s;
  transform: rotate(180deg);
}

.sp-20__particle:nth-child(6) {
  background: #ffd93d;
  animation-delay: 0.5s;
  transform: rotate(225deg);
}

.sp-20__particle:nth-child(7) {
  background: #6bcb77;
  animation-delay: 0.6s;
  transform: rotate(270deg);
}

.sp-20__particle:nth-child(8) {
  background: #4d96ff;
  animation-delay: 0.7s;
  transform: rotate(315deg);
}

@keyframes sp-20-scatter {
  0% {
    transform: var(--r,rotate(0deg)) translateX(0) scale(1);
    opacity: 1;
  }

  60% {
    opacity: 0.8;
  }

  100% {
    transform: var(--r,rotate(0deg)) translateX(42px) scale(0);
    opacity: 0;
  }
}

.sp-20__particle:nth-child(1) {
  --r: rotate(0deg);
}

.sp-20__particle:nth-child(2) {
  --r: rotate(45deg);
}

.sp-20__particle:nth-child(3) {
  --r: rotate(90deg);
}

.sp-20__particle:nth-child(4) {
  --r: rotate(135deg);
}

.sp-20__particle:nth-child(5) {
  --r: rotate(180deg);
}

.sp-20__particle:nth-child(6) {
  --r: rotate(225deg);
}

.sp-20__particle:nth-child(7) {
  --r: rotate(270deg);
}

.sp-20__particle:nth-child(8) {
  --r: rotate(315deg);
}

@keyframes sp-20-rotate {
  to {
    transform: rotate(360deg);
  }
}

.sp-20__core {
  position: absolute;
  inset: 40px;
  border-radius: 50%;
  background: white;
  box-shadow: 0 0 12px white;
  animation: sp-20-pulse 1.5s ease-in-out infinite;
}

@keyframes sp-20-pulse {
  0%,
    100% {
    transform: scale(0.8);
    opacity: 0.6;
  }

  50% {
    transform: scale(1.2);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-20__particle,
    .sp-20__burst,
    .sp-20__core {
    animation: none;
  }
}
```
