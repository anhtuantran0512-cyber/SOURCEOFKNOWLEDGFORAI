---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/retro-tv-static-noise-loader/"
title: "Retro TV Static Noise Loader"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A miniature CRT television screen filled with flickering monochrome pixel tiles simulates analog static noise, complete with scanline overlay and vignette…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro TV Static Noise Loader
Source: https://codefronts.com/motion/css-spinner-designs/retro-tv-static-noise-loader/

A miniature CRT television screen filled with flickering monochrome pixel tiles simulates analog static noise, complete with scanline overlay and vignette darkening.
## HTML
```html
<div class="sp-21">
  <div class="sp-21__tv">
    <div class="sp-21__static">
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
      <div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div><div class="sp-21__pixel"></div>
    </div>
    <div class="sp-21__scanline"></div>
    <div class="sp-21__glow"></div>
  </div>
</div>
```
## CSS
```css
.sp-21,
.sp-21 *,
.sp-21 *::before,
.sp-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-21 {
  --bg: #0a0a0a;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-21__tv {
  position: relative;
  width: 120px;
  height: 90px;
  background: #111;
  border-radius: 8px;
  border: 3px solid #333;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0,0,0,0.8),inset 0 0 10px rgba(0,0,0,0.5);
}

.sp-21__static {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-template-rows: repeat(9,1fr);
  gap: 0;
}

.sp-21__pixel {
  background: #fff;
  animation: sp-21-flicker 0.08s steps(1) infinite;
}

.sp-21__pixel:nth-child(4n+1) {
  animation-delay: 0s;
  opacity: 0.9;
}

.sp-21__pixel:nth-child(4n+2) {
  animation-delay: 0.02s;
  opacity: 0.4;
}

.sp-21__pixel:nth-child(4n+3) {
  animation-delay: 0.04s;
  opacity: 0.7;
}

.sp-21__pixel:nth-child(4n) {
  animation-delay: 0.06s;
  opacity: 0.2;
}

.sp-21__pixel:nth-child(7n) {
  animation-duration: 0.12s;
}

.sp-21__pixel:nth-child(11n) {
  animation-duration: 0.06s;
}

.sp-21__pixel:nth-child(3n) {
  background: #888;
}

.sp-21__scanline {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      to bottom,
      transparent 0px,
      transparent 3px,
      rgba(0,0,0,0.3) 3px,
      rgba(0,0,0,0.3) 4px
    );
  pointer-events: none;
}

.sp-21__glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse,transparent 40%,rgba(0,0,0,0.5) 100%);
  pointer-events: none;
}

@keyframes sp-21-flicker {
  0%,
    100% {
    opacity: var(--o,0.9);
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-21__pixel {
    animation: none;
  }
}
```
