---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/dual-counter-rotate-ring-spinner/"
title: "Dual Counter-Rotate Ring Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Two concentric rings spin in opposite directions — outer purple and inner pink — with a pulsing radial core, creating a hypnotic, gyroscopic loading indicator."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dual Counter-Rotate Ring Spinner
Source: https://codefronts.com/motion/css-spinner-designs/dual-counter-rotate-ring-spinner/

Two concentric rings spin in opposite directions — outer purple and inner pink — with a pulsing radial core, creating a hypnotic, gyroscopic loading indicator.
## HTML
```html
<div class="sp-02">
  <div class="sp-02__wrap">
    <div class="sp-02__outer-track"></div>
    <div class="sp-02__outer"></div>
    <div class="sp-02__inner-track"></div>
    <div class="sp-02__inner"></div>
    <div class="sp-02__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-02,
.sp-02 *,
.sp-02 *::before,
.sp-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-02 {
  --bg: #0d0017;
  --outer: #b44fff;
  --inner: #ff4fa3;
  --outer-track: rgba(180,79,255,0.15);
  --inner-track: rgba(255,79,163,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-02__wrap {
  position: relative;
  width: 80px;
  height: 80px;
}

.sp-02__outer-track {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 4px solid var(--outer-track);
}

.sp-02__outer {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 4px solid transparent;
  border-top-color: var(--outer);
  border-bottom-color: var(--outer);
  animation: sp-02-cw 1.2s linear infinite;
  filter: drop-shadow(0 0 6px var(--outer));
}

.sp-02__inner-track {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  border: 3px solid var(--inner-track);
}

.sp-02__inner {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-left-color: var(--inner);
  border-right-color: var(--inner);
  animation: sp-02-ccw 0.9s linear infinite;
  filter: drop-shadow(0 0 6px var(--inner));
}

.sp-02__core {
  position: absolute;
  inset: 32px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(180,79,255,0.6),transparent);
  animation: sp-02-pulse 1.2s ease-in-out infinite;
}

@keyframes sp-02-cw {
  to {
    transform: rotate(360deg);
  }
}

@keyframes sp-02-ccw {
  to {
    transform: rotate(-360deg);
  }
}

@keyframes sp-02-pulse {
  0%,
    100% {
    opacity: 0.4;
    transform: scale(0.8);
  }

  50% {
    opacity: 1;
    transform: scale(1.2);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-02__outer,
    .sp-02__inner,
    .sp-02__core {
    animation: none;
  }
}
```
