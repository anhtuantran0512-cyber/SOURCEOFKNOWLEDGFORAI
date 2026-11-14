---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/infinity-loop-stroke-spinner/"
title: "Infinity Loop Stroke Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "An SVG infinity symbol (∞) animates its stroke drawing from start to end and back using stroke-dasharray and stroke-dashoffset, with a glowing lime-green…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinity Loop Stroke Spinner
Source: https://codefronts.com/motion/css-spinner-designs/infinity-loop-stroke-spinner/

An SVG infinity symbol (∞) animates its stroke drawing from start to end and back using stroke-dasharray and stroke-dashoffset, with a glowing lime-green line on a dark field.
## HTML
```html
<div class="sp-14">
  <svg class="sp-14__svg" viewBox="-10 -10 120 60">
    <path class="sp-14__track" d="M50,20 C50,4 72,4 72,20 C72,36 94,36 94,20 C94,4 72,4 72,20 C72,36 50,36 50,20 C50,4 28,4 28,20 C28,36 6,36 6,20 C6,4 28,4 28,20 C28,36 50,36 50,20"/>
    <path class="sp-14__path" d="M50,20 C50,4 72,4 72,20 C72,36 94,36 94,20 C94,4 72,4 72,20 C72,36 50,36 50,20 C50,4 28,4 28,20 C28,36 6,36 6,20 C6,4 28,4 28,20 C28,36 50,36 50,20"/>
  </svg>
</div>
```
## CSS
```css
.sp-14,
.sp-14 *,
.sp-14 *::before,
.sp-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-14 {
  --bg: #04080f;
  --c: #76ff03;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-14__svg {
  width: 120px;
  height: 60px;
  overflow: visible;
  filter: drop-shadow(0 0 6px var(--c)) drop-shadow(0 0 12px rgba(118,255,3,0.3));
}

.sp-14__path {
  fill: none;
  stroke: var(--c);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-dasharray: 300;
  stroke-dashoffset: 300;
  animation: sp-14-draw 2s ease-in-out infinite;
}

.sp-14__track {
  fill: none;
  stroke: rgba(118,255,3,0.1);
  stroke-width: 3;
  stroke-linecap: round;
}

@keyframes sp-14-draw {
  0% {
    stroke-dashoffset: 300;
    opacity: 1;
  }

  50% {
    stroke-dashoffset: 0;
    opacity: 1;
  }

  100% {
    stroke-dashoffset: -300;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-14__path {
    animation: none;
    stroke-dashoffset: 0;
  }
}
```
