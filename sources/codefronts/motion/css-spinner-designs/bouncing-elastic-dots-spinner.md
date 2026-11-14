---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/bouncing-elastic-dots-spinner/"
title: "Bouncing Elastic Dots Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Three coloured dots bounce with spring-like squash and stretch physics — compressing horizontally and elongating vertically at peak height — using a…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncing Elastic Dots Spinner
Source: https://codefronts.com/motion/css-spinner-designs/bouncing-elastic-dots-spinner/

Three coloured dots bounce with spring-like squash and stretch physics — compressing horizontally and elongating vertically at peak height — using a multi-step cubic-bezier keyframe.
## HTML
```html
<div class="sp-15">
  <div class="sp-15__row">
    <div class="sp-15__dot"></div>
    <div class="sp-15__dot"></div>
    <div class="sp-15__dot"></div>
  </div>
</div>
```
## CSS
```css
.sp-15,
.sp-15 *,
.sp-15 *::before,
.sp-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-15 {
  --bg: #0e0b1e;
  --c1: #ff6e6c;
  --c2: #cbacf9;
  --c3: #67e8f9;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-15__row {
  display: flex;
  align-items: flex-end;
  gap: 10px;
  height: 70px;
}

.sp-15__dot {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  animation: sp-15-bounce 0.9s cubic-bezier(0.36,0.07,0.19,0.97) infinite;
}

.sp-15__dot:nth-child(1) {
  background: var(--c1);
  box-shadow: 0 0 10px var(--c1);
  animation-delay: 0s;
}

.sp-15__dot:nth-child(2) {
  background: var(--c2);
  box-shadow: 0 0 10px var(--c2);
  animation-delay: 0.15s;
}

.sp-15__dot:nth-child(3) {
  background: var(--c3);
  box-shadow: 0 0 10px var(--c3);
  animation-delay: 0.3s;
}

@keyframes sp-15-bounce {
  0%,
    100% {
    transform: translateY(0) scaleX(1) scaleY(1);
  }

  30% {
    transform: translateY(-40px) scaleX(0.9) scaleY(1.1);
  }

  50% {
    transform: translateY(-48px) scaleX(0.85) scaleY(1.15);
  }

  70% {
    transform: translateY(-40px) scaleX(0.9) scaleY(1.1);
  }

  85% {
    transform: translateY(-4px) scaleX(1.1) scaleY(0.9);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-15__dot {
    animation: none;
  }
}
```
