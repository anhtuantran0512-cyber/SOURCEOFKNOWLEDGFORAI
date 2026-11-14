---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/ripple-pulse-ring-spinner/"
title: "Ripple Pulse Ring Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Four concentric rings expand outward from a solid azure dot in sequence, each fading from full opacity to invisible as it reaches its maximum radius — like…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Pulse Ring Spinner
Source: https://codefronts.com/motion/css-spinner-designs/ripple-pulse-ring-spinner/

Four concentric rings expand outward from a solid azure dot in sequence, each fading from full opacity to invisible as it reaches its maximum radius — like rings in water.
## HTML
```html
<div class="sp-12">
  <div class="sp-12__ripple">
    <div class="sp-12__ring"></div>
    <div class="sp-12__ring"></div>
    <div class="sp-12__ring"></div>
    <div class="sp-12__ring"></div>
    <div class="sp-12__dot"></div>
  </div>
</div>
```
## CSS
```css
.sp-12,
.sp-12 *,
.sp-12 *::before,
.sp-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-12 {
  --bg: #060810;
  --c: #29b6f6;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-12__ripple {
  position: relative;
  width: 80px;
  height: 80px;
}

.sp-12__ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--c);
  opacity: 0;
  animation: sp-12-ripple 2s ease-out infinite;
}

.sp-12__ring:nth-child(1) {
  inset: 0;
  animation-delay: 0s;
}

.sp-12__ring:nth-child(2) {
  inset: 0;
  animation-delay: 0.5s;
}

.sp-12__ring:nth-child(3) {
  inset: 0;
  animation-delay: 1s;
}

.sp-12__ring:nth-child(4) {
  inset: 0;
  animation-delay: 1.5s;
}

.sp-12__dot {
  position: absolute;
  inset: 30px;
  border-radius: 50%;
  background: var(--c);
  box-shadow: 0 0 12px var(--c),0 0 24px rgba(41,182,246,0.4);
}

@keyframes sp-12-ripple {
  0% {
    transform: scale(0.1);
    opacity: 1;
  }

  100% {
    transform: scale(1.8);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-12__ring {
    animation: none;
    opacity: 0.3;
    transform: scale(1);
  }
}
```
