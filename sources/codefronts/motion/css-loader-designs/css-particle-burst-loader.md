---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-particle-burst-loader/"
title: "CSS Particle Burst Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three particle CSS loaders — a radial burst with eight directional particles, floating ascending particles, and a 12-arm pulsing starburst — creating…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Particle Burst Loader
Source: https://codefronts.com/motion/css-loader-designs/css-particle-burst-loader/

Three particle CSS loaders — a radial burst with eight directional particles, floating ascending particles, and a 12-arm pulsing starburst — creating energetic, attention-grabbing loading states.
## HTML
```html
<div class="ld-20">
  <div class="ld-20__stage">
    <div class="ld-20__cell">
      <div class="ld-20__burst">
        <span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>
        <div class="ld-20__burst-core"></div>
      </div>
```
## CSS
```css
.ld-20,
.ld-20 *,
.ld-20 *::before,
.ld-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-20 {
  --bg: #0a0012;
  --c1: #e040fb;
  --c2: #7c4dff;
  --c3: #40c4ff;
  --c4: #64ffda;
  --c5: #ff6d00;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-20__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-20__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-20__label {
  color: rgba(255,255,255,.3);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Radial burst */

.ld-20__burst {
  width: 80px;
  height: 80px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-20__burst span {
  position: absolute;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  animation: ld-20-burst 1.5s ease-in-out infinite;
}

.ld-20__burst span:nth-child(1) {
  background: var(--c1);
  animation-delay: 0s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(2) {
  background: var(--c2);
  animation-delay: .1s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(3) {
  background: var(--c3);
  animation-delay: .2s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(4) {
  background: var(--c4);
  animation-delay: .3s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(5) {
  background: var(--c5);
  animation-delay: .4s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(6) {
  background: var(--c1);
  animation-delay: .5s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(7) {
  background: var(--c2);
  animation-delay: .6s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

.ld-20__burst span:nth-child(8) {
  background: var(--c3);
  animation-delay: .7s;
  transform-origin: 40px 40px;
  top: 37px;
  left: 37px;
}

@keyframes ld-20-burst {
  0% {
    transform: rotate(calc(var(--r,0)*45deg)) translateY(0);
    opacity: 1;
    width: 6px;
    height: 6px;
  }

  80% {
    opacity: .6;
  }

  100% {
    transform: rotate(calc(var(--r,0)*45deg)) translateY(-34px);
    opacity: 0;
    width: 3px;
    height: 3px;
  }
}

.ld-20__burst span:nth-child(1) {
  --r: 0;
}

.ld-20__burst span:nth-child(2) {
  --r: 1;
}

.ld-20__burst span:nth-child(3) {
  --r: 2;
}

.ld-20__burst span:nth-child(4) {
  --r: 3;
}

.ld-20__burst span:nth-child(5) {
  --r: 4;
}

.ld-20__burst span:nth-child(6) {
  --r: 5;
}

.ld-20__burst span:nth-child(7) {
  --r: 6;
}

.ld-20__burst span:nth-child(8) {
  --r: 7;
}

.ld-20__burst-core {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--c1);
  box-shadow: 0 0 12px var(--c1),0 0 24px rgba(224,64,251,.4);
  animation: ld-20-core 1.5s ease-in-out infinite;
}

@keyframes ld-20-core {
  0%,
    100% {
    transform: scale(.8);
    opacity: .7;
  }

  50% {
    transform: scale(1.2);
    opacity: 1;
  }
}
/* Floating particles */

.ld-20__float {
  width: 80px;
  height: 80px;
  position: relative;
}

.ld-20__float span {
  position: absolute;
  border-radius: 50%;
  animation: ld-20-float linear infinite;
}

.ld-20__float span:nth-child(1) {
  width: 8px;
  height: 8px;
  background: var(--c1);
  left: 10px;
  top: 60px;
  animation-duration: 2s;
  animation-delay: 0s;
}

.ld-20__float span:nth-child(2) {
  width: 5px;
  height: 5px;
  background: var(--c3);
  left: 35px;
  top: 65px;
  animation-duration: 2.5s;
  animation-delay: .3s;
}

.ld-20__float span:nth-child(3) {
  width: 7px;
  height: 7px;
  background: var(--c4);
  left: 55px;
  top: 62px;
  animation-duration: 1.8s;
  animation-delay: .6s;
}

.ld-20__float span:nth-child(4) {
  width: 4px;
  height: 4px;
  background: var(--c2);
  left: 20px;
  top: 70px;
  animation-duration: 2.2s;
  animation-delay: .9s;
}

.ld-20__float span:nth-child(5) {
  width: 6px;
  height: 6px;
  background: var(--c5);
  left: 45px;
  top: 68px;
  animation-duration: 1.6s;
  animation-delay: 1.2s;
}

@keyframes ld-20-float {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }

  100% {
    transform: translateY(-80px) scale(0);
    opacity: 0;
  }
}
/* Starburst */

.ld-20__star {
  width: 80px;
  height: 80px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-20__star-arm {
  position: absolute;
  width: 3px;
  height: 30px;
  border-radius: 2px;
  transform-origin: 50% 100%;
  bottom: 50%;
  left: calc(50% - 1.5px);
  animation: ld-20-star-arm 2s ease-in-out infinite;
}

.ld-20__star-arm:nth-child(1) {
  transform: rotate(0deg);
  background: var(--c1);
  animation-delay: 0s;
}

.ld-20__star-arm:nth-child(2) {
  transform: rotate(30deg);
  background: var(--c2);
  animation-delay: .17s;
}

.ld-20__star-arm:nth-child(3) {
  transform: rotate(60deg);
  background: var(--c3);
  animation-delay: .33s;
}

.ld-20__star-arm:nth-child(4) {
  transform: rotate(90deg);
  background: var(--c4);
  animation-delay: .5s;
}

.ld-20__star-arm:nth-child(5) {
  transform: rotate(120deg);
  background: var(--c5);
  animation-delay: .67s;
}

.ld-20__star-arm:nth-child(6) {
  transform: rotate(150deg);
  background: var(--c1);
  animation-delay: .83s;
}

.ld-20__star-arm:nth-child(7) {
  transform: rotate(180deg);
  background: var(--c2);
  animation-delay: 1s;
}

.ld-20__star-arm:nth-child(8) {
  transform: rotate(210deg);
  background: var(--c3);
  animation-delay: 1.17s;
}

.ld-20__star-arm:nth-child(9) {
  transform: rotate(240deg);
  background: var(--c4);
  animation-delay: 1.33s;
}

.ld-20__star-arm:nth-child(10) {
  transform: rotate(270deg);
  background: var(--c5);
  animation-delay: 1.5s;
}

.ld-20__star-arm:nth-child(11) {
  transform: rotate(300deg);
  background: var(--c1);
  animation-delay: 1.67s;
}

.ld-20__star-arm:nth-child(12) {
  transform: rotate(330deg);
  background: var(--c2);
  animation-delay: 1.83s;
}

@keyframes ld-20-star-arm {
  0%,
    100% {
    opacity: .2;
    height: 14px;
  }

  50% {
    opacity: 1;
    height: 30px;
    box-shadow: 0 -6px 8px currentColor;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-20__burst span,
    .ld-20__burst-core,
    .ld-20__float span,
    .ld-20__star-arm {
    animation: none;
  }
}
```
