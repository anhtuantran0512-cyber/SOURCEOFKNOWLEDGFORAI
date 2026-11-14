---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/dot-chase-orbit-spinner/"
title: "Dot Chase Orbit Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Four multi-coloured dots orbit a shared centre, each fading in and out with staggered delays to create a chasing, comet-like orbital trail effect."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dot Chase Orbit Spinner
Source: https://codefronts.com/motion/css-spinner-designs/dot-chase-orbit-spinner/

Four multi-coloured dots orbit a shared centre, each fading in and out with staggered delays to create a chasing, comet-like orbital trail effect.
## HTML
```html
<div class="sp-03">
  <div class="sp-03__orbit">
    <div class="sp-03__trail"></div>
    <div class="sp-03__dot"></div>
    <div class="sp-03__dot"></div>
    <div class="sp-03__dot"></div>
    <div class="sp-03__dot"></div>
  </div>
</div>
```
## CSS
```css
.sp-03,
.sp-03 *,
.sp-03 *::before,
.sp-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-03 {
  --bg: #0b1120;
  --d1: #f9a825;
  --d2: #ff6b35;
  --d3: #e91e8c;
  --d4: #7c4dff;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-03__orbit {
  position: relative;
  width: 72px;
  height: 72px;
  animation: sp-03-spin 1.4s linear infinite;
}

.sp-03__dot {
  position: absolute;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform-origin: 0 0;
}

.sp-03__dot:nth-child(1) {
  background: var(--d1);
  box-shadow: 0 0 8px var(--d1);
  transform: rotate(0deg) translateX(28px) translateY(-6px);
  animation: sp-03-fade 1.4s linear infinite;
  animation-delay: 0s;
}

.sp-03__dot:nth-child(2) {
  background: var(--d2);
  box-shadow: 0 0 8px var(--d2);
  transform: rotate(90deg) translateX(28px) translateY(-6px);
  animation: sp-03-fade 1.4s linear infinite;
  animation-delay: -0.35s;
}

.sp-03__dot:nth-child(3) {
  background: var(--d3);
  box-shadow: 0 0 8px var(--d3);
  transform: rotate(180deg) translateX(28px) translateY(-6px);
  animation: sp-03-fade 1.4s linear infinite;
  animation-delay: -0.7s;
}

.sp-03__dot:nth-child(4) {
  background: var(--d4);
  box-shadow: 0 0 8px var(--d4);
  transform: rotate(270deg) translateX(28px) translateY(-6px);
  animation: sp-03-fade 1.4s linear infinite;
  animation-delay: -1.05s;
}

.sp-03__trail {
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.06);
}

@keyframes sp-03-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes sp-03-fade {
  0%,
    100% {
    opacity: 1;
    transform-origin: 0 0;
  }

  50% {
    opacity: 0.25;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-03__orbit,
    .sp-03__dot {
    animation: none;
  }
}
```
