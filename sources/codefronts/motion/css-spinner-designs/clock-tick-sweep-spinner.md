---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/clock-tick-sweep-spinner/"
title: "Clock Tick Sweep Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A precise gold second-hand sweeps in discrete tick steps around a minimal dark clock face with 12 hour markers, using CSS steps() timing to simulate…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clock Tick Sweep Spinner
Source: https://codefronts.com/motion/css-spinner-designs/clock-tick-sweep-spinner/

A precise gold second-hand sweeps in discrete tick steps around a minimal dark clock face with 12 hour markers, using CSS steps() timing to simulate mechanical tick motion.
## HTML
```html
<div class="sp-13">
  <div class="sp-13__clock">
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__tick"></div>
    <div class="sp-13__hand"></div>
    <div class="sp-13__center"></div>
  </div>
</div>
```
## CSS
```css
.sp-13,
.sp-13 *,
.sp-13 *::before,
.sp-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-13 {
  --bg: #0d0d0d;
  --face: #111;
  --ring: #e8e0d0;
  --hand: #f5c518;
  --tick: rgba(232,224,208,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-13__clock {
  position: relative;
  width: 80px;
  height: 80px;
  background: var(--face);
  border-radius: 50%;
  border: 2px solid var(--ring);
  box-shadow: 0 0 0 1px rgba(232,224,208,0.1),inset 0 0 16px rgba(0,0,0,0.5);
}

.sp-13__tick {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 2px;
  height: 6px;
  margin-left: -1px;
  background: var(--tick);
  transform-origin: bottom center;
  border-radius: 1px;
}

.sp-13__tick:nth-child(1) {
  transform: translateY(-100%) translateY(-27px) rotate(0deg);
}

.sp-13__tick:nth-child(2) {
  transform: translateY(-100%) translateY(-27px) rotate(30deg);
}

.sp-13__tick:nth-child(3) {
  transform: translateY(-100%) translateY(-27px) rotate(60deg);
}

.sp-13__tick:nth-child(4) {
  transform: translateY(-100%) translateY(-27px) rotate(90deg);
}

.sp-13__tick:nth-child(5) {
  transform: translateY(-100%) translateY(-27px) rotate(120deg);
}

.sp-13__tick:nth-child(6) {
  transform: translateY(-100%) translateY(-27px) rotate(150deg);
}

.sp-13__tick:nth-child(7) {
  transform: translateY(-100%) translateY(-27px) rotate(180deg);
}

.sp-13__tick:nth-child(8) {
  transform: translateY(-100%) translateY(-27px) rotate(210deg);
}

.sp-13__tick:nth-child(9) {
  transform: translateY(-100%) translateY(-27px) rotate(240deg);
}

.sp-13__tick:nth-child(10) {
  transform: translateY(-100%) translateY(-27px) rotate(270deg);
}

.sp-13__tick:nth-child(11) {
  transform: translateY(-100%) translateY(-27px) rotate(300deg);
}

.sp-13__tick:nth-child(12) {
  transform: translateY(-100%) translateY(-27px) rotate(330deg);
}

.sp-13__hand {
  position: absolute;
  bottom: 50%;
  left: 50%;
  width: 2px;
  height: 26px;
  margin-left: -1px;
  background: var(--hand);
  border-radius: 2px 2px 0 0;
  transform-origin: bottom center;
  box-shadow: 0 0 4px var(--hand);
  animation: sp-13-tick 1s steps(60,end) infinite;
}

.sp-13__center {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--hand);
  transform: translate(-50%,-50%);
  box-shadow: 0 0 4px var(--hand);
}

@keyframes sp-13-tick {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-13__hand {
    animation: none;
  }
}
```
