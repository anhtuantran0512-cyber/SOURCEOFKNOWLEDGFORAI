---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-text-glitch-hover-effect/"
title: "CSS Text Glitch Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four text glitch hover effects — RGB channel split, scanline flicker, noise slice, and VHS chromatic aberration — each triggered by hovering the element and…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Glitch Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-text-glitch-hover-effect/

Four text glitch hover effects — RGB channel split, scanline flicker, noise slice, and VHS chromatic aberration — each triggered by hovering the element and driven entirely by CSS keyframes on pseudo-elements using clip-path and color-mix.
## HTML
```html
<div class="hv-02">
  <div class="hv-02__grid">
    <div class="hv-02__cell">
      <span class="hv-02__glitch hv-02__glitch--rgb" data-text="GLITCH">GLITCH</span>
      <span class="hv-02__label">RGB Channel Split</span>
    </div>
    <div class="hv-02__cell">
      <span class="hv-02__glitch hv-02__glitch--scan" data-text="SCANLINE">SCANLINE</span>
      <span class="hv-02__label">Scanline Flicker</span>
    </div>
    <div class="hv-02__cell">
      <span class="hv-02__glitch hv-02__glitch--slice" data-text="NOISE">NOISE</span>
      <span class="hv-02__label">Noise Slice</span>
    </div>
    <div class="hv-02__cell">
      <span class="hv-02__glitch hv-02__glitch--vhs" data-text="VHS">VHS</span>
      <span class="hv-02__label">VHS Chromatic</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-02,
.hv-02 *,
.hv-02 *::before,
.hv-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-02 ::selection {
  background: #ff003c;
  color: #fff;
}

.hv-02 {
  --bg: #080810;
  --text: #f0f0f0;
  --dim: #444;
  --red: #ff003c;
  --blue: #00e5ff;
  --green: #39ff14;
  --yellow: #ffe600;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-02__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 48px;
  max-width: 800px;
  width: 100%;
}

.hv-02__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  padding: 60px 32px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-02__label {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared glitch base */

.hv-02__glitch {
  font-size: clamp(2rem,6vw,3.5rem);
  font-weight: 900;
  color: var(--text);
  letter-spacing: .08em;
  position: relative;
  cursor: default;
  display: inline-block;
}

.hv-02__glitch::before,
.hv-02__glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
/* 1 — RGB channel split */

.hv-02__glitch--rgb::before {
  color: var(--red);
  left: 2px;
}

.hv-02__glitch--rgb::after {
  color: var(--blue);
  left: -2px;
}

.hv-02__glitch--rgb:hover::before {
  animation: hv-02-rgb-b .4s steps(2) infinite;
}

.hv-02__glitch--rgb:hover::after {
  animation: hv-02-rgb-a .4s steps(2) infinite .1s;
}

@keyframes hv-02-rgb-b {
  0% {
    clip-path: inset(0 0 95% 0);
    transform: translateX(-3px);
  }

  20% {
    clip-path: inset(30% 0 50% 0);
    transform: translateX(3px);
  }

  40% {
    clip-path: inset(60% 0 20% 0);
    transform: translateX(-2px);
  }

  60% {
    clip-path: inset(10% 0 75% 0);
    transform: translateX(4px);
  }

  80% {
    clip-path: inset(80% 0 5% 0);
    transform: translateX(-3px);
  }

  100% {
    clip-path: inset(45% 0 40% 0);
    transform: translateX(2px);
  }
}

@keyframes hv-02-rgb-a {
  0% {
    clip-path: inset(50% 0 30% 0);
    transform: translateX(3px);
  }

  25% {
    clip-path: inset(5% 0 80% 0);
    transform: translateX(-4px);
  }

  50% {
    clip-path: inset(70% 0 15% 0);
    transform: translateX(2px);
  }

  75% {
    clip-path: inset(20% 0 60% 0);
    transform: translateX(-3px);
  }

  100% {
    clip-path: inset(40% 0 45% 0);
    transform: translateX(3px);
  }
}
/* 2 — scanline flicker */

.hv-02__glitch--scan {
  color: var(--green);
}

.hv-02__glitch--scan::before {
  background: repeating-linear-gradient(
      0deg,transparent,transparent 2px,rgba(0,0,0,.4) 2px,rgba(0,0,0,.4) 4px
    );
  background-size: 100% 4px;
  mix-blend-mode: multiply;
  opacity: 0;
  transition: opacity .2s;
}

.hv-02__glitch--scan::after {
  color: var(--green);
  left: 2px;
  opacity: 0;
  transition: opacity .2s;
}

.hv-02__glitch--scan:hover::before {
  opacity: 1;
  animation: hv-02-scan-roll .8s linear infinite;
}

.hv-02__glitch--scan:hover::after {
  opacity: .7;
  animation: hv-02-rgb-b .3s steps(3) infinite;
}

@keyframes hv-02-scan-roll {
  0% {
    background-position-y: 0;
  }

  100% {
    background-position-y: 100px;
  }
}
/* 3 — noise slice */

.hv-02__glitch--slice {
  color: var(--yellow);
}

.hv-02__glitch--slice::before {
  color: var(--red);
  clip-path: inset(0 0 100% 0);
}

.hv-02__glitch--slice::after {
  color: var(--blue);
  clip-path: inset(100% 0 0 0);
}

.hv-02__glitch--slice:hover::before {
  animation: hv-02-slice-t .5s steps(4) infinite;
}

.hv-02__glitch--slice:hover::after {
  animation: hv-02-slice-b .5s steps(4) infinite .15s;
}

@keyframes hv-02-slice-t {
  0% {
    clip-path: inset(0 0 85% 0);
    transform: translateX(6px) skewX(-2deg);
  }

  33% {
    clip-path: inset(25% 0 55% 0);
    transform: translateX(-5px);
  }

  66% {
    clip-path: inset(60% 0 10% 0);
    transform: translateX(4px) skewX(1deg);
  }

  100% {
    clip-path: inset(10% 0 75% 0);
    transform: translateX(-6px);
  }
}

@keyframes hv-02-slice-b {
  0% {
    clip-path: inset(80% 0 0 0);
    transform: translateX(-4px);
  }

  33% {
    clip-path: inset(50% 0 20% 0);
    transform: translateX(6px);
  }

  66% {
    clip-path: inset(15% 0 70% 0);
    transform: translateX(-3px) skewX(2deg);
  }

  100% {
    clip-path: inset(65% 0 5% 0);
    transform: translateX(5px);
  }
}
/* 4 — VHS chromatic */

.hv-02__glitch--vhs {
  color: #fff;
}

.hv-02__glitch--vhs::before {
  color: var(--red);
  mix-blend-mode: screen;
  transform: translateX(0);
}

.hv-02__glitch--vhs::after {
  color: var(--blue);
  mix-blend-mode: screen;
  transform: translateX(0);
}

.hv-02__glitch--vhs:hover::before {
  animation: hv-02-vhs-r .6s steps(3) infinite;
}

.hv-02__glitch--vhs:hover::after {
  animation: hv-02-vhs-b .6s steps(3) infinite .2s;
}

@keyframes hv-02-vhs-r {
  0% {
    transform: translateX(-6px);
    clip-path: inset(20% 0 60% 0);
  }

  50% {
    transform: translateX(4px);
    clip-path: inset(55% 0 10% 0);
  }

  100% {
    transform: translateX(-5px);
    clip-path: inset(5% 0 80% 0);
  }
}

@keyframes hv-02-vhs-b {
  0% {
    transform: translateX(6px);
    clip-path: inset(40% 0 30% 0);
  }

  50% {
    transform: translateX(-4px);
    clip-path: inset(10% 0 65% 0);
  }

  100% {
    transform: translateX(5px);
    clip-path: inset(70% 0 5% 0);
  }
}

@media (max-width: 520px) {
  .hv-02__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-02__glitch::before,
    .hv-02__glitch::after {
    animation: none!important;
    opacity: 0!important;
  }
}
```
