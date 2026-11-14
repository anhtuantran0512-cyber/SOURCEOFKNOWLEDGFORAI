---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-bouncing-balls-loader/"
title: "CSS Bouncing Balls Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four kinetic ball-physics loaders — a staggered bounce row, elastic scale pulses, rolling balls with rotation, and a squash-and-stretch ball with shadow —…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Bouncing Balls Loader
Source: https://codefronts.com/motion/css-loader-designs/css-bouncing-balls-loader/

Four kinetic ball-physics loaders — a staggered bounce row, elastic scale pulses, rolling balls with rotation, and a squash-and-stretch ball with shadow — each using pure CSS animation.
## HTML
```html
<div class="ld-05">
  <div class="ld-05__stage">
    <div class="ld-05__cell"><div class="ld-05__simple"><span></span><span></span><span></span><span></span></div><span class="ld-05__label">Bounce Row</span></div>
    <div class="ld-05__cell"><div class="ld-05__elastic"><span></span><span></span><span></span></div><span class="ld-05__label">Elastic Pulse</span></div>
    <div class="ld-05__cell"><div class="ld-05__roll"><span></span><span></span><span></span></div><span class="ld-05__label">Rolling Balls</span></div>
    <div class="ld-05__cell"><div class="ld-05__squash"><div class="ld-05__squash-ball"></div><div class="ld-05__squash-shadow"></div></div>
```
## CSS
```css
.ld-05,
.ld-05 *,
.ld-05 *::before,
.ld-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-05 {
  --bg: #1a0a2e;
  --c1: #ff6b6b;
  --c2: #ffd93d;
  --c3: #6bcb77;
  --c4: #4d96ff;
  --c5: #c77dff;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-05__stage {
  display: flex;
  gap: 64px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-05__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-05__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Simple bounce */

.ld-05__simple {
  display: flex;
  gap: 8px;
  align-items: flex-end;
  height: 50px;
}

.ld-05__simple span {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--c1);
  animation: ld-05-simple-bounce 0.8s ease-in-out infinite alternate;
}

.ld-05__simple span:nth-child(1) {
  animation-delay: 0s;
}

.ld-05__simple span:nth-child(2) {
  animation-delay: .15s;
  background: var(--c2);
}

.ld-05__simple span:nth-child(3) {
  animation-delay: .3s;
  background: var(--c3);
}

.ld-05__simple span:nth-child(4) {
  animation-delay: .45s;
  background: var(--c4);
}

@keyframes ld-05-simple-bounce {
  0% {
    transform: translateY(0) scaleX(1);
  }

  100% {
    transform: translateY(-30px) scaleX(.85);
  }
}
/* Elastic */

.ld-05__elastic {
  display: flex;
  gap: 10px;
  align-items: center;
  height: 50px;
}

.ld-05__elastic span {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--c4);
  animation: ld-05-elastic 1.2s cubic-bezier(.68,-.55,.27,1.55) infinite;
}

.ld-05__elastic span:nth-child(1) {
  animation-delay: 0s;
}

.ld-05__elastic span:nth-child(2) {
  animation-delay: .15s;
  background: var(--c5);
}

.ld-05__elastic span:nth-child(3) {
  animation-delay: .3s;
  background: var(--c1);
}

@keyframes ld-05-elastic {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.6);
    opacity: .5;
  }
}
/* Rolling */

.ld-05__roll {
  width: 100px;
  height: 30px;
  position: relative;
  overflow: hidden;
}

.ld-05__roll span {
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  top: 7px;
  background: var(--c2);
  animation: ld-05-roll 1.5s linear infinite;
}

.ld-05__roll span:nth-child(1) {
  animation-delay: 0s;
}

.ld-05__roll span:nth-child(2) {
  animation-delay: .5s;
  background: var(--c3);
}

.ld-05__roll span:nth-child(3) {
  animation-delay: 1s;
  background: var(--c5);
}

@keyframes ld-05-roll {
  0% {
    left: -16px;
    transform: rotate(0);
  }

  100% {
    left: 100%;
    transform: rotate(720deg);
  }
}
/* Shadow squash */

.ld-05__squash {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  height: 60px;
  justify-content: flex-end;
}

.ld-05__squash-ball {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--c1);
  animation: ld-05-squash-ball 0.8s ease-in-out infinite alternate;
}

.ld-05__squash-shadow {
  width: 20px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255,107,107,.3);
  animation: ld-05-squash-shadow 0.8s ease-in-out infinite alternate;
}

@keyframes ld-05-squash-ball {
  0% {
    transform: translateY(0) scaleY(1);
  }

  100% {
    transform: translateY(-28px) scaleY(.9);
  }
}

@keyframes ld-05-squash-shadow {
  0% {
    transform: scaleX(1);
    opacity: .4;
  }

  100% {
    transform: scaleX(.5);
    opacity: .1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-05__simple span,
    .ld-05__elastic span,
    .ld-05__roll span,
    .ld-05__squash-ball,
    .ld-05__squash-shadow {
    animation: none;
  }
}
```
