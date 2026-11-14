---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/cyberpunk-segmented-ring-spinner/"
title: "Cyberpunk Segmented Ring Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A yellow dashed outer ring and a magenta inner arc spin in opposite directions around a rotating wireframe diamond core, channelling the segmented HUD…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Segmented Ring Spinner
Source: https://codefronts.com/motion/css-spinner-designs/cyberpunk-segmented-ring-spinner/

A yellow dashed outer ring and a magenta inner arc spin in opposite directions around a rotating wireframe diamond core, channelling the segmented HUD aesthetics of cyberpunk UIs.
## HTML
```html
<div class="sp-18">
  <div class="sp-18__wrap">
    <div class="sp-18__ring-outer"></div>
    <div class="sp-18__ring-outer-2"></div>
    <div class="sp-18__ring-inner"></div>
    <div class="sp-18__ring-inner-2"></div>
    <div class="sp-18__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-18,
.sp-18 *,
.sp-18 *::before,
.sp-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-18 {
  --bg: #020409;
  --c1: #f7ff00;
  --c2: #ff0080;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-18__wrap {
  position: relative;
  width: 88px;
  height: 88px;
}

.sp-18__ring-outer {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px dashed var(--c1);
  border-dash-offset: 0;
  opacity: 0.9;
  box-shadow: 0 0 8px var(--c1),inset 0 0 8px rgba(247,255,0,0.1);
  animation: sp-18-cw 1.6s linear infinite;
  clip-path: polygon(50% 0%,100% 0%,100% 100%,50% 100%);
}

.sp-18__ring-outer-2 {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px dashed var(--c1);
  opacity: 0.5;
  animation: sp-18-cw 1.6s linear infinite;
  animation-delay: -0.8s;
  clip-path: polygon(0% 0%,50% 0%,50% 100%,0% 100%);
}

.sp-18__ring-inner {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  border: 2px solid var(--c2);
  border-right-color: transparent;
  border-bottom-color: transparent;
  box-shadow: 0 0 8px var(--c2);
  animation: sp-18-ccw 0.9s linear infinite;
}

.sp-18__ring-inner-2 {
  position: absolute;
  inset: 14px;
  border-radius: 50%;
  border: 2px solid var(--c2);
  border-left-color: transparent;
  border-top-color: transparent;
  opacity: 0.4;
  animation: sp-18-ccw 0.9s linear infinite;
  animation-delay: -0.45s;
}

.sp-18__core {
  position: absolute;
  inset: 32px;
  background: transparent;
  border: 1px solid var(--c1);
  transform: rotate(45deg);
  animation: sp-18-cw 2s linear infinite;
  box-shadow: 0 0 6px var(--c1);
}

@keyframes sp-18-cw {
  to {
    transform: rotate(360deg);
  }
}

@keyframes sp-18-ccw {
  to {
    transform: rotate(-360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-18__ring-outer,
    .sp-18__ring-outer-2,
    .sp-18__ring-inner,
    .sp-18__ring-inner-2,
    .sp-18__core {
    animation: none;
  }
}
```
