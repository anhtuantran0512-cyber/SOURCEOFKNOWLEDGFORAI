---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/progress-arc-fill-spinner/"
title: "Progress Arc Fill Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "An SVG circle arc fills from empty to complete on a two-second loop, with a 100% percentage counter label centred inside — suitable as both a loading…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Progress Arc Fill Spinner
Source: https://codefronts.com/motion/css-spinner-designs/progress-arc-fill-spinner/

An SVG circle arc fills from empty to complete on a two-second loop, with a 100% percentage counter label centred inside — suitable as both a loading indicator and a determinate progress ring.
## HTML
```html
<div class="sp-23">
  <svg class="sp-23__svg" viewBox="0 0 90 90">
    <circle class="sp-23__track" cx="45" cy="45" r="40"/>
    <circle class="sp-23__arc" cx="45" cy="45" r="40"/>
    <text class="sp-23__percent" x="45" y="45">100%</text>
  </svg>
</div>
```
## CSS
```css
.sp-23,
.sp-23 *,
.sp-23 *::before,
.sp-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-23 {
  --bg: #050a0f;
  --c: #00e5ff;
  --track: rgba(0,229,255,0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-23__svg {
  width: 90px;
  height: 90px;
  transform: rotate(-90deg);
  filter: drop-shadow(0 0 6px var(--c));
}

.sp-23__track {
  fill: none;
  stroke: var(--track);
  stroke-width: 5;
}

.sp-23__arc {
  fill: none;
  stroke: var(--c);
  stroke-width: 5;
  stroke-linecap: round;
  stroke-dasharray: 251;
  stroke-dashoffset: 251;
  animation: sp-23-fill 2s ease-in-out infinite;
}

.sp-23__percent {
  fill: var(--c);
  font-size: 14px;
  font-family: system-ui,sans-serif;
  font-weight: 600;
  text-anchor: middle;
  dominant-baseline: central;
  transform: rotate(90deg);
  transform-origin: 45px 45px;
  animation: sp-23-count 2s ease-in-out infinite;
  letter-spacing: -0.5px;
}

@keyframes sp-23-fill {
  0% {
    stroke-dashoffset: 251;
    opacity: 1;
  }

  80% {
    stroke-dashoffset: 0;
    opacity: 1;
  }

  100% {
    stroke-dashoffset: 0;
    opacity: 0;
  }
}

@keyframes sp-23-count {
  0% {
    opacity: 1;
  }

  80% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-23__arc {
    animation: none;
    stroke-dashoffset: 100;
  }

  .sp-23__percent {
    animation: none;
  }
}
```
