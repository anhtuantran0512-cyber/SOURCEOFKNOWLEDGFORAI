---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/heartbeat-pulse-loader/"
title: "Heartbeat Pulse Loader"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A vivid red core pulses with a cardiac double-beat rhythm while three concentric ripple rings expand outward and fade, mimicking a real heartbeat waveform."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Heartbeat Pulse Loader
Source: https://codefronts.com/motion/css-spinner-designs/heartbeat-pulse-loader/

A vivid red core pulses with a cardiac double-beat rhythm while three concentric ripple rings expand outward and fade, mimicking a real heartbeat waveform.
## HTML
```html
<div class="sp-05">
  <div class="sp-05__stack">
    <div class="sp-05__ring"></div>
    <div class="sp-05__ring"></div>
    <div class="sp-05__ring"></div>
    <div class="sp-05__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-05,
.sp-05 *,
.sp-05 *::before,
.sp-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-05 {
  --bg: #0f0a0a;
  --c: #ff1744;
  --glow: rgba(255,23,68,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-05__stack {
  position: relative;
  width: 72px;
  height: 72px;
}

.sp-05__ring {
  position: absolute;
  border-radius: 50%;
  border: 2px solid var(--c);
  opacity: 0;
  animation: sp-05-ripple 1.8s ease-out infinite;
}

.sp-05__ring:nth-child(1) {
  inset: 0;
  animation-delay: 0s;
}

.sp-05__ring:nth-child(2) {
  inset: 0;
  animation-delay: 0.6s;
}

.sp-05__ring:nth-child(3) {
  inset: 0;
  animation-delay: 1.2s;
}

.sp-05__core {
  position: absolute;
  inset: 22px;
  border-radius: 50%;
  background: var(--c);
  box-shadow: 0 0 16px var(--glow),0 0 32px var(--glow);
  animation: sp-05-beat 1.8s ease-in-out infinite;
}

@keyframes sp-05-ripple {
  0% {
    transform: scale(0.3);
    opacity: 0.9;
  }

  100% {
    transform: scale(1.6);
    opacity: 0;
  }
}

@keyframes sp-05-beat {
  0%,
    100% {
    transform: scale(1);
  }

  15% {
    transform: scale(1.25);
  }

  30% {
    transform: scale(0.95);
  }

  45% {
    transform: scale(1.1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-05__ring,
    .sp-05__core {
    animation: none;
    opacity: 1;
  }
}
```
