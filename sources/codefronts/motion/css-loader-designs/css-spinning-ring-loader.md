---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-spinning-ring-loader/"
title: "CSS Spinning Ring Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Six ring-based CSS spinners — classic, double, triple nested, dashed, gradient conic, and pulse ring — demonstrating the full spectrum of border and…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Spinning Ring Loader
Source: https://codefronts.com/motion/css-loader-designs/css-spinning-ring-loader/

Six ring-based CSS spinners — classic, double, triple nested, dashed, gradient conic, and pulse ring — demonstrating the full spectrum of border and conic-gradient spin techniques.
## HTML
```html
<div class="ld-01">
  <div class="ld-01__stage">
    <div class="ld-01__cell"><div class="ld-01__ring"></div><span class="ld-01__label">Classic Ring</span></div>
    <div class="ld-01__cell"><div class="ld-01__double"></div><span class="ld-01__label">Double Ring</span></div>
    <div class="ld-01__cell"><div class="ld-01__triple"><span></span><span></span><span></span></div><span class="ld-01__label">Triple Ring</span></div>
    <div class="ld-01__cell"><div class="ld-01__dashed"></div><span class="ld-01__label">Dashed Ring</span></div>
    <div class="ld-01__cell"><div class="ld-01__gradient"></div><span class="ld-01__label">Gradient Ring</span></div>
    <div class="ld-01__cell"><div class="ld-01__pulse-ring"></div><span class="ld-01__label">Pulse Ring</span></div>
  </div>
```
## CSS
```css
.ld-01,
.ld-01 *,
.ld-01 *::before,
.ld-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-01 {
  --bg: #0a0a0f;
  --accent: #6c63ff;
  --accent2: #ff6584;
  --accent3: #43e97b;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-01__stage {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
}

.ld-01__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.ld-01__label {
  color: rgba(255,255,255,.5);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Classic Ring */

.ld-01__ring {
  width: 56px;
  height: 56px;
  border: 4px solid rgba(108,99,255,.2);
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: ld-01-spin 1s linear infinite;
}

@keyframes ld-01-spin {
  to {
    transform: rotate(360deg);
  }
}
/* Double Ring */

.ld-01__double {
  width: 56px;
  height: 56px;
  border: 4px solid transparent;
  border-top-color: var(--accent);
  border-bottom-color: var(--accent2);
  border-radius: 50%;
  animation: ld-01-spin 1.2s linear infinite;
}
/* Triple Ring */

.ld-01__triple {
  width: 60px;
  height: 60px;
  position: relative;
}

.ld-01__triple span {
  position: absolute;
  border-radius: 50%;
  border: 3px solid transparent;
  animation: ld-01-spin linear infinite;
}

.ld-01__triple span:nth-child(1) {
  inset: 0;
  border-top-color: var(--accent);
  animation-duration: .9s;
}

.ld-01__triple span:nth-child(2) {
  inset: 8px;
  border-top-color: var(--accent2);
  animation-duration: 1.3s;
  animation-direction: reverse;
}

.ld-01__triple span:nth-child(3) {
  inset: 16px;
  border-top-color: var(--accent3);
  animation-duration: 1.7s;
}
/* Dashed Ring */

.ld-01__dashed {
  width: 56px;
  height: 56px;
  border: 4px dashed var(--accent);
  border-radius: 50%;
  animation: ld-01-spin 2s linear infinite;
  opacity: .8;
}
/* Gradient Ring */

.ld-01__gradient {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: conic-gradient(var(--accent),var(--accent2),var(--accent3),var(--accent));
  animation: ld-01-spin 1s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 6px),#000 0);
}
/* Pulsing Ring */

.ld-01__pulse-ring {
  width: 56px;
  height: 56px;
  border: 4px solid var(--accent);
  border-radius: 50%;
  animation: ld-01-pulse-ring 1.5s ease-out infinite;
}

@keyframes ld-01-pulse-ring {
  0% {
    transform: scale(.8);
    opacity: 1;
  }

  100% {
    transform: scale(1.5);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-01__ring,
    .ld-01__double,
    .ld-01__triple span,
    .ld-01__dashed,
    .ld-01__gradient,
    .ld-01__pulse-ring {
    animation: none;
  }
}
```
