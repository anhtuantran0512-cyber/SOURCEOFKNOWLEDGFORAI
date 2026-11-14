---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-glitch-flicker-loader/"
title: "CSS Glitch Flicker Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three cyberpunk CSS loaders — a glitching text title with RGB channel split, a CRT scan-line box, and a matrix binary rain column — evoking terminal hacking…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitch Flicker Loader
Source: https://codefronts.com/motion/css-loader-designs/css-glitch-flicker-loader/

Three cyberpunk CSS loaders — a glitching text title with RGB channel split, a CRT scan-line box, and a matrix binary rain column — evoking terminal hacking and retro sci-fi aesthetics.
## HTML
```html
<div class="ld-07">
  <div class="ld-07__stage">
    <div class="ld-07__cell">
      <div class="ld-07__text" data-text="LOADING">LOADING</div>
      <span class="ld-07__label">Glitch Text</span>
    </div>
    <div class="ld-07__cell">
      <div class="ld-07__scan"></div>
      <span class="ld-07__label">Scan Line</span>
    </div>
    <div class="ld-07__cell">
      <div class="ld-07__matrix">
        <div class="ld-07__col"><span>1</span><span>0</span><span>1</span><span>0</span><span>1</span><span>0</span></div>
        <div class="ld-07__col"><span>0</span><span>1</span><span>0</span><span>1</span><span>0</span><span>1</span></div>
        <div class="ld-07__col"><span>1</span><span>1</span><span>0</span><span>0</span><span>1</span><span>0</span></div>
        <div class="ld-07__col"><span>0</span><span>0</span><span>1</span><span>1</span><span>0</span><span>1</span></div>
      </div>
```
## CSS
```css
.ld-07,
.ld-07 *,
.ld-07 *::before,
.ld-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-07 {
  --bg: #080808;
  --c1: #00ff41;
  --c2: #ff003c;
  --c3: #00d4ff;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Courier New',monospace;
}

.ld-07__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-07__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-07__label {
  color: rgba(255,255,255,.3);
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
}
/* Glitch text */

.ld-07__text {
  font-size: 28px;
  font-weight: 700;
  color: var(--c1);
  letter-spacing: 4px;
  position: relative;
  text-shadow: 0 0 10px var(--c1);
  animation: ld-07-flicker 3s step-end infinite;
}

.ld-07__text::before {
  content: attr(data-text);
  position: absolute;
  left: 0;
  top: 0;
  color: var(--c2);
  animation: ld-07-glitch-r 2.5s step-end infinite;
  clip-path: polygon(0 20%,100% 20%,100% 40%,0 40%);
}

.ld-07__text::after {
  content: attr(data-text);
  position: absolute;
  left: 0;
  top: 0;
  color: var(--c3);
  animation: ld-07-glitch-b 2s step-end infinite;
  clip-path: polygon(0 60%,100% 60%,100% 80%,0 80%);
}

@keyframes ld-07-flicker {
  0%,
    100% {
    opacity: 1;
  }

  92% {
    opacity: 1;
  }

  93% {
    opacity: 0;
  }

  94% {
    opacity: 1;
  }

  96% {
    opacity: 0;
  }

  97% {
    opacity: 1;
  }
}

@keyframes ld-07-glitch-r {
  0% {
    transform: translateX(0);
  }

  15% {
    transform: translateX(-3px);
  }

  16% {
    transform: translateX(3px);
  }

  17% {
    transform: translateX(0);
  }

  85% {
    transform: translateX(0);
  }

  86% {
    transform: translateX(2px);
  }

  87% {
    transform: translateX(-2px);
  }

  88% {
    transform: translateX(0);
  }
}

@keyframes ld-07-glitch-b {
  0% {
    transform: translateX(0);
  }

  10% {
    transform: translateX(2px);
  }

  11% {
    transform: translateX(-2px);
  }

  12% {
    transform: translateX(0);
  }

  75% {
    transform: translateX(0);
  }

  76% {
    transform: translateX(-3px);
  }

  77% {
    transform: translateX(3px);
  }

  78% {
    transform: translateX(0);
  }
}
/* Scan line loader */

.ld-07__scan {
  width: 80px;
  height: 80px;
  background: #111;
  border: 1px solid var(--c1);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0,255,65,.2);
}

.ld-07__scan::before {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--c1);
  box-shadow: 0 0 8px var(--c1);
  animation: ld-07-scan 1.5s linear infinite;
  opacity: .8;
}

.ld-07__scan::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(0deg,transparent,transparent 3px,rgba(0,255,65,.03) 3px,rgba(0,255,65,.03) 4px);
}

@keyframes ld-07-scan {
  0% {
    top: 0;
  }

  100% {
    top: 100%;
  }
}
/* Binary rain letters */

.ld-07__matrix {
  width: 80px;
  height: 80px;
  overflow: hidden;
  background: #050505;
  border: 1px solid rgba(0,255,65,.2);
  border-radius: 4px;
  display: flex;
  gap: 1px;
  padding: 2px;
}

.ld-07__col {
  display: flex;
  flex-direction: column;
  gap: 1px;
  animation: ld-07-matrix-col 1.5s linear infinite;
}

.ld-07__col:nth-child(2) {
  animation-delay: .3s;
}

.ld-07__col:nth-child(3) {
  animation-delay: .6s;
}

.ld-07__col:nth-child(4) {
  animation-delay: .9s;
}

.ld-07__col span {
  font-size: 9px;
  color: var(--c1);
  opacity: .15;
  display: block;
  line-height: 12px;
  text-align: center;
  animation: ld-07-digit 2s step-end infinite;
}

.ld-07__col span:nth-child(1) {
  animation-delay: 0s;
}

.ld-07__col span:nth-child(2) {
  animation-delay: .2s;
  opacity: .4;
}

.ld-07__col span:nth-child(3) {
  animation-delay: .4s;
  opacity: .7;
}

.ld-07__col span:nth-child(4) {
  animation-delay: .6s;
  opacity: 1;
  color: #fff;
  text-shadow: 0 0 4px var(--c1);
}

.ld-07__col span:nth-child(5) {
  animation-delay: .8s;
  opacity: .4;
}

.ld-07__col span:nth-child(6) {
  animation-delay: 1s;
  opacity: .1;
}

@keyframes ld-07-matrix-col {
  0% {
    transform: translateY(-20px);
  }

  100% {
    transform: translateY(20px);
  }
}

@keyframes ld-07-digit {
  0%,
    100% {
    content: '0';
  }

  25% {
    content: '1';
  }

  50% {
    content: '0';
  }

  75% {
    content: '1';
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-07__text,
    .ld-07__text::before,
    .ld-07__text::after,
    .ld-07__scan::before,
    .ld-07__col {
    animation: none;
  }
}
```
