---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/breathing-circle-loader/"
title: "Breathing Circle Loader"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A calm azure orb slowly inhales and exhales with a scale pulse while three expanding rings propagate outward in a continuous ripple, creating a meditative…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Breathing Circle Loader
Source: https://codefronts.com/motion/css-spinner-designs/breathing-circle-loader/

A calm azure orb slowly inhales and exhales with a scale pulse while three expanding rings propagate outward in a continuous ripple, creating a meditative loading state.
## HTML
```html
<div class="sp-19">
  <div class="sp-19__wrap">
    <div class="sp-19__ring"></div>
    <div class="sp-19__ring"></div>
    <div class="sp-19__ring"></div>
    <div class="sp-19__core"></div>
  </div>
  <div class="sp-19__label">Loading</div>
</div>
```
## CSS
```css
.sp-19,
.sp-19 *,
.sp-19 *::before,
.sp-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-19 {
  --bg: #03080e;
  --c: #4fc3f7;
  --glow: rgba(79,195,247,0.3);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  min-height: 100vh;
  background: var(--bg);
  font-family: system-ui,sans-serif;
}

.sp-19__wrap {
  position: relative;
  width: 90px;
  height: 90px;
}

.sp-19__ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--c);
  opacity: 0;
  animation: sp-19-breathe-ring 4s ease-in-out infinite;
}

.sp-19__ring:nth-child(1) {
  inset: 0;
}

.sp-19__ring:nth-child(2) {
  inset: 0;
  animation-delay: 1.3s;
}

.sp-19__ring:nth-child(3) {
  inset: 0;
  animation-delay: 2.6s;
}

.sp-19__core {
  position: absolute;
  inset: 20px;
  border-radius: 50%;
  background: radial-gradient(circle,var(--c),rgba(79,195,247,0.3));
  animation: sp-19-breathe-core 4s ease-in-out infinite;
}

.sp-19__label {
  color: rgba(79,195,247,0.7);
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  animation: sp-19-text 4s ease-in-out infinite;
}

@keyframes sp-19-breathe-ring {
  0% {
    transform: scale(0.4);
    opacity: 0.8;
  }

  100% {
    transform: scale(1.8);
    opacity: 0;
  }
}

@keyframes sp-19-breathe-core {
  0%,
    100% {
    transform: scale(0.7);
    box-shadow: 0 0 10px var(--glow);
  }

  50% {
    transform: scale(1.15);
    box-shadow: 0 0 30px var(--glow),0 0 60px var(--glow);
  }
}

@keyframes sp-19-text {
  0%,
    100% {
    opacity: 0.3;
  }

  50% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-19__ring,
    .sp-19__core,
    .sp-19__label {
    animation: none;
    opacity: 1;
  }
}
```
