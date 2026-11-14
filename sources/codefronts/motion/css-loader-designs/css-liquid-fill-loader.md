---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-liquid-fill-loader/"
title: "CSS Liquid Fill Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four liquid-fill CSS loaders — a flask with wave, a liquid circle with sloshing, a vertical tube, and an animated battery indicator — using height and…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Fill Loader
Source: https://codefronts.com/motion/css-loader-designs/css-liquid-fill-loader/

Four liquid-fill CSS loaders — a flask with wave, a liquid circle with sloshing, a vertical tube, and an animated battery indicator — using height and transform animations to simulate fluid.
## HTML
```html
<div class="ld-10">
  <div class="ld-10__stage">
    <div class="ld-10__cell"><div class="ld-10__flask"><div class="ld-10__flask-fill"></div><div class="ld-10__flask-wave"></div></div>
```
## CSS
```css
.ld-10,
.ld-10 *,
.ld-10 *::before,
.ld-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-10 {
  --bg: #071330;
  --c1: #0ea5e9;
  --c2: #6366f1;
  --c3: #10b981;
  --c4: #f59e0b;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-10__stage {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: flex-end;
}

.ld-10__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.ld-10__label {
  color: rgba(255,255,255,.4);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Flask fill */

.ld-10__flask {
  width: 50px;
  height: 80px;
  border: 2px solid var(--c1);
  border-radius: 4px 4px 12px 12px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 16px rgba(14,165,233,.2);
}

.ld-10__flask-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top,var(--c1),rgba(14,165,233,.4));
  animation: ld-10-fill 3s ease-in-out infinite;
}

.ld-10__flask-wave {
  position: absolute;
  bottom: 0;
  left: -100%;
  width: 300%;
  height: 30px;
  background: radial-gradient(ellipse at 50% 100%,rgba(14,165,233,.6) 0%,transparent 70%);
  animation: ld-10-wave 1.5s linear infinite;
}

@keyframes ld-10-fill {
  0% {
    height: 10%;
  }

  50% {
    height: 80%;
  }

  100% {
    height: 10%;
  }
}

@keyframes ld-10-wave {
  to {
    transform: translateX(33%);
  }
}
/* Circle liquid */

.ld-10__circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 3px solid var(--c2);
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(99,102,241,.2);
}

.ld-10__circle-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: linear-gradient(to top,var(--c2),rgba(99,102,241,.3));
  animation: ld-10-wave-x 1.2s ease-in-out infinite alternate;
}

.ld-10__circle::before {
  content: '60%';
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  z-index: 1;
}

@keyframes ld-10-wave-x {
  0% {
    transform: translateX(-5px) skewX(-3deg);
  }

  100% {
    transform: translateX(5px) skewX(3deg);
  }
}
/* Tube */

.ld-10__tube {
  width: 24px;
  height: 100px;
  border: 2px solid var(--c3);
  border-radius: 12px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 12px rgba(16,185,129,.15);
}

.ld-10__tube-fill {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top,var(--c3),rgba(16,185,129,.3));
  animation: ld-10-tube 2.5s ease-in-out infinite;
}

@keyframes ld-10-tube {
  0%,
    100% {
    height: 15%;
  }

  50% {
    height: 85%;
  }
}
/* Battery */

.ld-10__battery {
  width: 80px;
  height: 44px;
  border: 2px solid var(--c4);
  border-radius: 6px;
  position: relative;
  overflow: hidden;
}

.ld-10__battery::before {
  content: '';
  position: absolute;
  right: -8px;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 16px;
  background: var(--c4);
  border-radius: 0 3px 3px 0;
}

.ld-10__battery-fill {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  background: linear-gradient(90deg,var(--c4),rgba(245,158,11,.5));
  animation: ld-10-battery 3s ease-in-out infinite;
  border-radius: 4px;
}

@keyframes ld-10-battery {
  0% {
    width: 5%;
  }

  60% {
    width: 85%;
  }

  100% {
    width: 5%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-10__flask-fill,
    .ld-10__flask-wave,
    .ld-10__circle-fill,
    .ld-10__tube-fill,
    .ld-10__battery-fill {
    animation: none;
  }
}
```
