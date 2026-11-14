---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-gradient-conic-spinner/"
title: "CSS Gradient Conic Spinner"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Six conic-gradient CSS spinners — rainbow sweep, sunset arc, dual-sweep, thick gradient arc, nested concentric conics, and a glowing comet — demonstrating…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Conic Spinner
Source: https://codefronts.com/motion/css-loader-designs/css-gradient-conic-spinner/

Six conic-gradient CSS spinners — rainbow sweep, sunset arc, dual-sweep, thick gradient arc, nested concentric conics, and a glowing comet — demonstrating the full expressive range of conic-gradient masking.
## HTML
```html
<div class="ld-19">
  <div class="ld-19__stage">
    <div class="ld-19__cell"><div class="ld-19__rainbow"></div><span class="ld-19__label">Rainbow Conic</span></div>
    <div class="ld-19__cell"><div class="ld-19__sunset"></div><span class="ld-19__label">Sunset Arc</span></div>
    <div class="ld-19__cell"><div class="ld-19__dual-sweep"></div><span class="ld-19__label">Dual Sweep</span></div>
    <div class="ld-19__cell"><div class="ld-19__thick"></div><span class="ld-19__label">Thick Arc</span></div>
    <div class="ld-19__cell"><div class="ld-19__nested"><span></span><span></span><span></span></div><span class="ld-19__label">Nested Conic</span></div>
    <div class="ld-19__cell"><div class="ld-19__glow"></div><span class="ld-19__label">Glow Conic</span></div>
  </div>
```
## CSS
```css
.ld-19,
.ld-19 *,
.ld-19 *::before,
.ld-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-19 {
  --bg: #0a0a0a;
  --c1: #ff6b6b;
  --c2: #ffd93d;
  --c3: #6bcb77;
  --c4: #4d96ff;
  --c5: #c77dff;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-19__stage {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-19__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

.ld-19__label {
  color: rgba(255,255,255,.35);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Rainbow conic */

.ld-19__rainbow {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(var(--c1),var(--c2),var(--c3),var(--c4),var(--c5),var(--c1));
  animation: ld-19-spin 1s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 6px),#000 0);
}

@keyframes ld-19-spin {
  to {
    transform: rotate(360deg);
  }
}
/* Sunset conic */

.ld-19__sunset {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(transparent 30%,#ff6b6b,#ffd93d,transparent 70%);
  animation: ld-19-spin 1.5s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 5px),#000 0);
}
/* Dual-sweep */

.ld-19__dual-sweep {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(var(--c4) 0deg,transparent 120deg,var(--c5) 180deg,transparent 300deg,var(--c4) 360deg);
  animation: ld-19-spin 1.2s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 5px),#000 0);
}
/* Thick gradient arc */

.ld-19__thick {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(transparent 20%,var(--c3),#4d96ff,transparent 80%);
  animation: ld-19-spin 2s ease-in-out infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 10px),#000 0);
}
/* Nested conic */

.ld-19__nested {
  width: 70px;
  height: 70px;
  position: relative;
}

.ld-19__nested span {
  position: absolute;
  border-radius: 50%;
  background: conic-gradient(transparent 70%,currentColor);
  animation: ld-19-spin linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 4px),#000 0);
}

.ld-19__nested span:nth-child(1) {
  inset: 0;
  color: var(--c1);
  animation-duration: 1s;
}

.ld-19__nested span:nth-child(2) {
  inset: 10px;
  color: var(--c3);
  animation-duration: 1.5s;
  animation-direction: reverse;
}

.ld-19__nested span:nth-child(3) {
  inset: 20px;
  color: var(--c4);
  animation-duration: 2s;
}
/* Glow conic */

.ld-19__glow {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: conic-gradient(transparent 40%,var(--c5),white,var(--c5),transparent 60%);
  animation: ld-19-spin 1.5s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 6px),#000 0);
  filter: drop-shadow(0 0 6px var(--c5));
}

@media (prefers-reduced-motion: reduce) {
  .ld-19__rainbow,
    .ld-19__sunset,
    .ld-19__dual-sweep,
    .ld-19__thick,
    .ld-19__nested span,
    .ld-19__glow {
    animation: none;
  }
}
```
