---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-ripple-button-hover-effect/"
title: "CSS Ripple Button Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five ripple and pulse hover effects on buttons — center-out ring, double ripple, contained wave, border-pulse, and glow-ring expansion — all using…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ripple Button Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-ripple-button-hover-effect/

Five ripple and pulse hover effects on buttons — center-out ring, double ripple, contained wave, border-pulse, and glow-ring expansion — all using pseudo-element scale animations and opacity keyframes to simulate a water-droplet impact.
## HTML
```html
<div class="hv-12">
  <div class="hv-12__stack">
    <div class="hv-12__row">
      <button class="hv-12__btn hv-12__btn--ring">Center Ripple</button>
      <span class="hv-12__label">scale + opacity keyframe</span>
    </div>
    <div class="hv-12__row">
      <button class="hv-12__btn hv-12__btn--double">Double Ring</button>
      <span class="hv-12__label">staggered dual ripple</span>
    </div>
    <div class="hv-12__row">
      <button class="hv-12__btn hv-12__btn--wave">Contained Wave</button>
      <span class="hv-12__label">overflow-clipped wave</span>
    </div>
    <div class="hv-12__row">
      <button class="hv-12__btn hv-12__btn--pulse">Border Pulse</button>
      <span class="hv-12__label">outline-offset ping</span>
    </div>
    <div class="hv-12__row">
      <button class="hv-12__btn hv-12__btn--glow">Glow Ring</button>
      <span class="hv-12__label">box-shadow expand</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-12,
.hv-12 *,
.hv-12 *::before,
.hv-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-12 ::selection {
  background: #be185d;
  color: #fff;
}

.hv-12 {
  --bg: #0f0008;
  --text: #fce7f3;
  --dim: #6b7280;
  --pink: #ec4899;
  --rose: #f43f5e;
  --magenta: #db2777;
  --purple: #a855f7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-12__stack {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: min(640px,100%);
}

.hv-12__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 24px 36px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-12__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  white-space: nowrap;
  flex-shrink: 0;
}
/* shared btn */

.hv-12__btn {
  position: relative;
  padding: 13px 36px;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: .05em;
  cursor: pointer;
  border-radius: 8px;
  border: none;
  flex-shrink: 0;
}
/* 1 — center ripple */

.hv-12__btn--ring {
  background: var(--pink);
  color: #fff;
  overflow: visible;
}

.hv-12__btn--ring::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(255,255,255,.4);
  transform: translate(-50%,-50%) scale(0);
  pointer-events: none;
}

.hv-12__btn--ring:hover::after {
  animation: hv-12-ripple .6s ease-out forwards;
}

@keyframes hv-12-ripple {
  0% {
    transform: translate(-50%,-50%) scale(0);
    opacity: .7;
  }

  100% {
    transform: translate(-50%,-50%) scale(3.5);
    opacity: 0;
  }
}
/* 2 — double ripple */

.hv-12__btn--double {
  background: var(--rose);
  color: #fff;
  overflow: visible;
}

.hv-12__btn--double::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(255,255,255,.3);
  transform: translate(-50%,-50%) scale(0);
  pointer-events: none;
}

.hv-12__btn--double::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: rgba(255,255,255,.2);
  transform: translate(-50%,-50%) scale(0);
  pointer-events: none;
}

.hv-12__btn--double:hover::before {
  animation: hv-12-ripple .7s ease-out forwards;
}

.hv-12__btn--double:hover::after {
  animation: hv-12-ripple .7s ease-out .25s forwards;
}
/* 3 — contained wave */

.hv-12__btn--wave {
  background: transparent;
  border: 2px solid var(--magenta);
  color: var(--magenta);
  overflow: hidden;
}

.hv-12__btn--wave::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(219,39,119,.25);
  transform: translate(-50%,-50%);
  pointer-events: none;
}

.hv-12__btn--wave:hover::before {
  animation: hv-12-wave .6s ease-out forwards;
}

@keyframes hv-12-wave {
  0% {
    width: 0;
    height: 0;
    opacity: .8;
  }

  100% {
    width: 300px;
    height: 300px;
    opacity: 0;
  }
}
/* 4 — border pulse */

.hv-12__btn--pulse {
  background: var(--purple);
  color: #fff;
  outline: 2px solid var(--purple);
  outline-offset: 0;
  transition: outline-offset .4s,outline-color .4s;
}

.hv-12__btn--pulse:hover {
  outline-offset: 10px;
  outline-color: transparent;
}
/* 5 — glow ring */

.hv-12__btn--glow {
  background: transparent;
  border: 2px solid var(--pink);
  color: var(--pink);
  box-shadow: 0 0 0 0 rgba(236,72,153,.4);
  transition: box-shadow .4s cubic-bezier(.4,0,.2,1),color .3s,background .3s;
}

.hv-12__btn--glow:hover {
  box-shadow: 0 0 0 12px rgba(236,72,153,0);
  color: #fff;
  background: var(--pink);
}

@media (max-width: 500px) {
  .hv-12__row {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-12__btn::before,
    .hv-12__btn::after {
    animation: none!important;
  }

  .hv-12__btn--pulse {
    transition: none!important;
  }
}
```
