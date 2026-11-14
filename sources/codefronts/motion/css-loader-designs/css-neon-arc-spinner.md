---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-neon-arc-spinner/"
title: "CSS Neon Arc Spinner"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Five glowing neon CSS spinners — a single neon ring, double counter-rotating neon, multi-arc intersecting glow, neon orbiting dot, and a conic comet — styled…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Arc Spinner
Source: https://codefronts.com/motion/css-loader-designs/css-neon-arc-spinner/

Five glowing neon CSS spinners — a single neon ring, double counter-rotating neon, multi-arc intersecting glow, neon orbiting dot, and a conic comet — styled for dark cyberpunk UIs.
## HTML
```html
<div class="ld-11">
  <div class="ld-11__stage">
    <div class="ld-11__cell"><div class="ld-11__neon"></div><span class="ld-11__label">Neon Ring</span></div>
    <div class="ld-11__cell"><div class="ld-11__double-neon"><span></span><span></span></div><span class="ld-11__label">Double Neon</span></div>
    <div class="ld-11__cell"><div class="ld-11__arcs"><span></span><span></span><span></span></div><span class="ld-11__label">Neon Arcs</span></div>
    <div class="ld-11__cell"><div class="ld-11__orbit-neon"><i></i></div><span class="ld-11__label">Neon Orbit</span></div>
    <div class="ld-11__cell"><div class="ld-11__comet-neon"></div><span class="ld-11__label">Neon Comet</span></div>
  </div>
```
## CSS
```css
.ld-11,
.ld-11 *,
.ld-11 *::before,
.ld-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-11 {
  --bg: #06000f;
  --c1: #bf00ff;
  --c2: #00f5ff;
  --c3: #ff6600;
  --c4: #39ff14;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-11__stage {
  display: flex;
  gap: 60px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-11__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-11__label {
  color: rgba(255,255,255,.35);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Neon ring */

.ld-11__neon {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  border: 3px solid transparent;
  border-top-color: var(--c1);
  box-shadow: 0 0 12px var(--c1),inset 0 0 12px rgba(191,0,255,.1);
  animation: ld-11-spin 1s linear infinite;
}

@keyframes ld-11-spin {
  to {
    transform: rotate(360deg);
  }
}
/* Double neon */

.ld-11__double-neon {
  width: 70px;
  height: 70px;
  position: relative;
}

.ld-11__double-neon span {
  position: absolute;
  border-radius: 50%;
  border: 3px solid transparent;
  animation: ld-11-spin linear infinite;
}

.ld-11__double-neon span:nth-child(1) {
  inset: 0;
  border-top-color: var(--c2);
  box-shadow: 0 0 14px var(--c2);
  animation-duration: 1s;
}

.ld-11__double-neon span:nth-child(2) {
  inset: 10px;
  border-bottom-color: var(--c1);
  box-shadow: 0 0 10px var(--c1);
  animation-duration: 1.5s;
  animation-direction: reverse;
}
/* Neon arc segments */

.ld-11__arcs {
  width: 70px;
  height: 70px;
  position: relative;
}

.ld-11__arcs span {
  position: absolute;
  border-radius: 50%;
  border: 3px solid transparent;
  animation: ld-11-spin linear infinite;
}

.ld-11__arcs span:nth-child(1) {
  inset: 0;
  border-top-color: var(--c3);
  box-shadow: 0 0 12px var(--c3);
  animation-duration: .8s;
}

.ld-11__arcs span:nth-child(2) {
  inset: 0;
  border-right-color: var(--c3);
  box-shadow: 0 0 12px var(--c3);
  animation-duration: .8s;
}

.ld-11__arcs span:nth-child(3) {
  inset: 16px;
  border-bottom-color: var(--c4);
  box-shadow: 0 0 10px var(--c4);
  animation-duration: 1.2s;
  animation-direction: reverse;
}
/* Neon orbit */

.ld-11__orbit-neon {
  width: 70px;
  height: 70px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-11__orbit-neon::before {
  content: '';
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--c1);
  box-shadow: 0 0 15px var(--c1),0 0 30px var(--c1);
  animation: ld-11-spin 1.2s linear infinite;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  transform-origin: 35px 35px;
}

.ld-11__orbit-neon::after {
  content: '';
  position: absolute;
  width: 64px;
  height: 64px;
  border-radius: 50%;
  border: 1px solid rgba(191,0,255,.2);
  box-shadow: 0 0 8px rgba(191,0,255,.15);
}

.ld-11__orbit-neon i {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--c2);
  box-shadow: 0 0 10px var(--c2);
}
/* Comet neon */

.ld-11__comet-neon {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(transparent 60%,var(--c4));
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 4px),#000 0);
  animation: ld-11-spin 1.2s linear infinite;
  filter: drop-shadow(0 0 6px var(--c4));
}

@media (prefers-reduced-motion: reduce) {
  .ld-11__neon,
    .ld-11__double-neon span,
    .ld-11__arcs span,
    .ld-11__orbit-neon::before,
    .ld-11__comet-neon {
    animation: none;
  }
}
```
