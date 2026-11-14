---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/glassmorphism-loader-spinner/"
title: "Glassmorphism Loader Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A frosted-glass circle with backdrop-filter blur floats over animated colour blobs, with two nested arcs spinning at different speeds to create a layered…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Loader Spinner
Source: https://codefronts.com/motion/css-spinner-designs/glassmorphism-loader-spinner/

A frosted-glass circle with backdrop-filter blur floats over animated colour blobs, with two nested arcs spinning at different speeds to create a layered glassmorphic loading indicator.
## HTML
```html
<div class="sp-17">
  <div class="sp-17__blobs">
    <div class="sp-17__blob"></div>
    <div class="sp-17__blob"></div>
    <div class="sp-17__blob"></div>
  </div>
  <div class="sp-17__glass">
    <div class="sp-17__arc"></div>
    <div class="sp-17__arc-inner"></div>
  </div>
</div>
```
## CSS
```css
.sp-17,
.sp-17 *,
.sp-17 *::before,
.sp-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-17 {
  --bg: #1a0533;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
  overflow: hidden;
}

.sp-17__blobs {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.sp-17__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
  animation: sp-17-float 6s ease-in-out infinite;
}

.sp-17__blob:nth-child(1) {
  width: 200px;
  height: 200px;
  background: #7c3aed;
  top: -80px;
  left: -60px;
  animation-delay: 0s;
}

.sp-17__blob:nth-child(2) {
  width: 180px;
  height: 180px;
  background: #ec4899;
  bottom: -60px;
  right: -40px;
  animation-delay: -2s;
}

.sp-17__blob:nth-child(3) {
  width: 160px;
  height: 160px;
  background: #3b82f6;
  top: 20%;
  right: 10%;
  animation-delay: -4s;
}

.sp-17__glass {
  position: relative;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.2);
  box-shadow: 0 8px 32px rgba(0,0,0,0.3),inset 0 1px 0 rgba(255,255,255,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
}

.sp-17__arc {
  position: absolute;
  inset: 8px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: rgba(255,255,255,0.9);
  border-right-color: rgba(255,255,255,0.4);
  animation: sp-17-spin 1.1s linear infinite;
}

.sp-17__arc-inner {
  position: absolute;
  inset: 20px;
  border-radius: 50%;
  border: 2px solid transparent;
  border-bottom-color: rgba(255,255,255,0.7);
  animation: sp-17-spin 0.8s linear infinite reverse;
}

@keyframes sp-17-spin {
  to {
    transform: rotate(360deg);
  }
}

@keyframes sp-17-float {
  0%,
    100% {
    transform: translateY(0) scale(1);
  }

  50% {
    transform: translateY(-20px) scale(1.05);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-17__arc,
    .sp-17__arc-inner,
    .sp-17__blob {
    animation: none;
  }
}
```
