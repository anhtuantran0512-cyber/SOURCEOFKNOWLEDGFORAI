---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/aurora-gradient-orb-spinner/"
title: "Aurora Gradient Orb Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A softly glowing orb pulses with shifting aurora borealis colours — layered radial gradients rotate independently with hue-shift filters — while a single…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Gradient Orb Spinner
Source: https://codefronts.com/motion/css-spinner-designs/aurora-gradient-orb-spinner/

A softly glowing orb pulses with shifting aurora borealis colours — layered radial gradients rotate independently with hue-shift filters — while a single orbital ring traces a luminous dot around the perimeter.
## HTML
```html
<div class="sp-25">
  <div class="sp-25__orb">
    <div class="sp-25__layer"></div>
    <div class="sp-25__layer"></div>
    <div class="sp-25__layer"></div>
    <div class="sp-25__ring"></div>
  </div>
</div>
```
## CSS
```css
.sp-25,
.sp-25 *,
.sp-25 *::before,
.sp-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-25 {
  --bg: #020d12;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-25__orb {
  position: relative;
  width: 100px;
  height: 100px;
}

.sp-25__layer {
  position: absolute;
  inset: 0;
  border-radius: 50%;
}

.sp-25__layer:nth-child(1) {
  background: radial-gradient(circle at 30% 40%,#00e5ff,transparent 60%), radial-gradient(circle at 70% 60%,#69f0ae,transparent 60%);
  filter: blur(4px);
  animation: sp-25-aurora1 4s ease-in-out infinite;
}

.sp-25__layer:nth-child(2) {
  background: radial-gradient(circle at 60% 30%,#7c4dff,transparent 55%), radial-gradient(circle at 40% 70%,#40c4ff,transparent 55%);
  filter: blur(6px);
  animation: sp-25-aurora2 5s ease-in-out infinite;
  animation-delay: -2s;
  mix-blend-mode: screen;
}

.sp-25__layer:nth-child(3) {
  background: radial-gradient(circle at 50% 50%,rgba(255,255,255,0.15),transparent 50%);
  animation: sp-25-pulse 3s ease-in-out infinite;
}

.sp-25__ring {
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.2);
  animation: sp-25-spin 8s linear infinite;
}

.sp-25__ring::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 50%;
  width: 6px;
  height: 6px;
  margin-left: -3px;
  border-radius: 50%;
  background: rgba(255,255,255,0.8);
  box-shadow: 0 0 6px white;
}

@keyframes sp-25-aurora1 {
  0%,
    100% {
    transform: rotate(0deg) scale(1);
    filter: blur(4px) hue-rotate(0deg);
  }

  33% {
    transform: rotate(120deg) scale(1.1);
    filter: blur(5px) hue-rotate(60deg);
  }

  66% {
    transform: rotate(240deg) scale(0.95);
    filter: blur(3px) hue-rotate(120deg);
  }
}

@keyframes sp-25-aurora2 {
  0%,
    100% {
    transform: rotate(0deg) scale(1.05);
  }

  50% {
    transform: rotate(-180deg) scale(0.95);
  }
}

@keyframes sp-25-pulse {
  0%,
    100% {
    opacity: 0.4;
  }

  50% {
    opacity: 0.9;
  }
}

@keyframes sp-25-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-25__layer,
    .sp-25__ring {
    animation: none;
  }
}
```
