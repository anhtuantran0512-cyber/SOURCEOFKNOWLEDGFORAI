---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-neon-glow-text-hover-effect/"
title: "CSS Neon Glow Text Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six neon-sign-inspired text hover effects — classic tube glow, pulsing flicker, color-cycle sweep, multi-layer bloom, retro arcade, and icy frost glow —…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Glow Text Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-neon-glow-text-hover-effect/

Six neon-sign-inspired text hover effects — classic tube glow, pulsing flicker, color-cycle sweep, multi-layer bloom, retro arcade, and icy frost glow — using layered text-shadow transitions to simulate electroluminescent lighting.
## HTML
```html
<div class="hv-06">
  <div class="hv-06__stack">
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--classic">NEON</span>
      <span class="hv-06__label">classic tube glow</span>
    </div>
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--flicker">FLICKER</span>
      <span class="hv-06__label">pulsing flicker</span>
    </div>
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--cycle">SPECTRUM</span>
      <span class="hv-06__label">hue-rotate cycle</span>
    </div>
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--bloom">BLOOM</span>
      <span class="hv-06__label">multi-layer bloom</span>
    </div>
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--arcade">HI-SCORE</span>
      <span class="hv-06__label">retro arcade</span>
    </div>
    <div class="hv-06__row">
      <span class="hv-06__neon hv-06__neon--frost">ICE</span>
      <span class="hv-06__label">icy frost glow</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-06,
.hv-06 *,
.hv-06 *::before,
.hv-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-06 ::selection {
  background: #ff00de;
  color: #fff;
}

.hv-06 {
  --bg: #020204;
  --dim: #3a3a4a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-06__stack {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: min(700px,100%);
}

.hv-06__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 32px 40px;
  background: rgba(255,255,255,.02);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 12px;
  gap: 20px;
}

.hv-06__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  white-space: nowrap;
  flex-shrink: 0;
}
/* shared neon base */

.hv-06__neon {
  font-size: clamp(1.6rem,4vw,2.4rem);
  font-weight: 700;
  letter-spacing: .15em;
  cursor: default;
  display: inline-block;
}
/* 1 — classic */

.hv-06__neon--classic {
  color: #ff00de;
  text-shadow: 0 0 4px #ff00de44;
  transition: text-shadow .4s,color .4s;
}

.hv-06__neon--classic:hover {
  color: #fff;
  text-shadow: 0 0 4px #fff, 0 0 16px #ff00de, 0 0 40px #ff00de, 0 0 80px #ff00de;
}
/* 2 — flicker */

.hv-06__neon--flicker {
  color: #39ff14;
  transition: text-shadow .3s;
}

.hv-06__neon--flicker:hover {
  color: #fff;
  text-shadow: 0 0 4px #fff,0 0 18px #39ff14,0 0 50px #39ff14;
  animation: hv-06-flicker 2s linear infinite;
}

@keyframes hv-06-flicker {
  0%,
    19%,
    21%,
    23%,
    25%,
    54%,
    56%,
    100% {
    text-shadow: 0 0 4px #fff,0 0 18px #39ff14,0 0 50px #39ff14;
    color: #fff;
  }

  20%,
    24%,
    55% {
    text-shadow: none;
    color: #39ff14;
  }
}
/* 3 — hue-rotate cycle */

.hv-06__neon--cycle {
  color: #ff4400;
  text-shadow: 0 0 4px #ff440033;
  transition: text-shadow .4s,filter .4s;
}

.hv-06__neon--cycle:hover {
  color: #fff;
  text-shadow: 0 0 6px #fff,0 0 20px #ff4400,0 0 60px #ff4400;
  animation: hv-06-huerot 3s linear infinite;
}

@keyframes hv-06-huerot {
  0% {
    filter: hue-rotate(0deg);
  }

  100% {
    filter: hue-rotate(360deg);
  }
}
/* 4 — multi-layer bloom */

.hv-06__neon--bloom {
  color: #7c3aed;
  text-shadow: 0 0 4px #7c3aed44;
  transition: text-shadow .5s cubic-bezier(.4,0,.2,1),color .5s;
}

.hv-06__neon--bloom:hover {
  color: #fff;
  text-shadow: 0 0 2px #fff, 0 0 8px #a78bfa, 0 0 20px #7c3aed, 0 0 50px #6d28d9, 0 0 100px #5b21b6, 0 0 180px #4c1d95;
}
/* 5 — retro arcade */

.hv-06__neon--arcade {
  color: #ffee00;
  font-family: monospace;
  text-shadow: 0 0 4px #ffee0044;
  transition: text-shadow .25s steps(2),color .25s;
}

.hv-06__neon--arcade:hover {
  color: #fff;
  text-shadow: 2px 2px 0 #ff6600, 0 0 10px #ffee00, 0 0 30px #ffee00, 0 0 60px #ff6600;
}
/* 6 — frost */

.hv-06__neon--frost {
  color: #a5f3fc;
  text-shadow: 0 0 4px #a5f3fc44;
  transition: text-shadow .5s,color .5s,letter-spacing .5s;
}

.hv-06__neon--frost:hover {
  color: #fff;
  letter-spacing: .25em;
  text-shadow: 0 0 4px #fff, 0 0 16px #a5f3fc, 0 0 40px #0ea5e9, 0 0 80px #0369a1;
}

@media (max-width: 520px) {
  .hv-06__row {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-06__neon {
    transition: none!important;
    animation: none!important;
  }
}
```
