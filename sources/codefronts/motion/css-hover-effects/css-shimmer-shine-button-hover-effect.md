---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-shimmer-shine-button-hover-effect/"
title: "CSS Shimmer Shine Button Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five light-streak and shimmer button effects — diagonal gloss swipe, radial spotlight, frosted edge shimmer, holographic foil, and full-button shimmer wash —…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shimmer Shine Button Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-shimmer-shine-button-hover-effect/

Five light-streak and shimmer button effects — diagonal gloss swipe, radial spotlight, frosted edge shimmer, holographic foil, and full-button shimmer wash — using pseudo-element gradients animated on hover to simulate a reflective material surface.
## HTML
```html
<div class="hv-09">
  <div class="hv-09__stack">
    <div class="hv-09__row">
      <button class="hv-09__btn hv-09__btn--diagonal">Diagonal Gloss</button>
      <span class="hv-09__label">translateX streak</span>
    </div>
    <div class="hv-09__row">
      <button class="hv-09__btn hv-09__btn--radial">Radial Spotlight</button>
      <span class="hv-09__label">radial-gradient reveal</span>
    </div>
    <div class="hv-09__row">
      <button class="hv-09__btn hv-09__btn--frost">Frosted Edge</button>
      <span class="hv-09__label">edge-shimmer effect</span>
    </div>
    <div class="hv-09__row">
      <button class="hv-09__btn hv-09__btn--holo">Holographic Foil</button>
      <span class="hv-09__label">conic-gradient holo</span>
    </div>
    <div class="hv-09__row">
      <button class="hv-09__btn hv-09__btn--wash">Shimmer Wash</button>
      <span class="hv-09__label">full-button wave</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-09,
.hv-09 *,
.hv-09 *::before,
.hv-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-09 ::selection {
  background: #6366f1;
  color: #fff;
}

.hv-09 {
  --bg: #07070f;
  --text: #e0e0ff;
  --dim: #4b5563;
  --indigo: #6366f1;
  --violet: #8b5cf6;
  --blue: #3b82f6;
  --sky: #0ea5e9;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-09__stack {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: min(640px,100%);
}

.hv-09__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 24px 36px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-09__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
  white-space: nowrap;
  flex-shrink: 0;
}
/* shared btn */

.hv-09__btn {
  position: relative;
  overflow: hidden;
  padding: 13px 36px;
  border: none;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: .05em;
  cursor: pointer;
  border-radius: 8px;
  flex-shrink: 0;
}

.hv-09__btn::before {
  content: '';
  position: absolute;
  pointer-events: none;
}
/* 1 — diagonal gloss */

.hv-09__btn--diagonal {
  background: var(--indigo);
  color: #fff;
}

.hv-09__btn--diagonal::before {
  top: 0;
  left: -75%;
  width: 75%;
  height: 100%;
  background: linear-gradient(105deg,transparent 0%,rgba(255,255,255,.7) 50%,transparent 100%);
  transition: left .7s cubic-bezier(.4,0,.2,1);
}

.hv-09__btn--diagonal:hover::before {
  left: 125%;
}
/* 2 — radial spotlight */

.hv-09__btn--radial {
  background: var(--violet);
  color: #fff;
}

.hv-09__btn--radial::before {
  inset: 0;
  background: radial-gradient(circle at 50% 50%,rgba(255,255,255,.5) 0%,transparent 65%);
  opacity: 0;
  transition: opacity .4s;
}

.hv-09__btn--radial:hover::before {
  opacity: 1;
}
/* 3 — frosted edge */

.hv-09__btn--frost {
  background: transparent;
  color: var(--blue);
  border: 2px solid var(--blue);
  transition: background .4s ease,color .4s ease,box-shadow .4s ease;
}

.hv-09__btn--frost::before {
  top: 0;
  left: 0;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg,rgba(59,130,246,.55),transparent);
  transform: translateX(-100%);
  transition: transform .5s ease;
}

.hv-09__btn--frost:hover {
  box-shadow: 0 0 24px rgba(59,130,246,.35);
}

.hv-09__btn--frost:hover::before {
  transform: translateX(0);
}

.hv-09__btn--frost::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 60%;
  height: 100%;
  background: linear-gradient(270deg,rgba(59,130,246,.55),transparent);
  transform: translateX(100%);
  transition: transform .5s ease;
  pointer-events: none;
}

.hv-09__btn--frost:hover::after {
  transform: translateX(0);
}
/* 4 — holographic foil */

.hv-09__btn--holo {
  background: conic-gradient(from 0deg,#6366f1,#8b5cf6,#ec4899,#f59e0b,#10b981,#06b6d4,#6366f1);
  background-size: 200% 200%;
  background-position: 0% 50%;
  color: #fff;
  transition: background-position .6s,filter .4s;
}

.hv-09__btn--holo:hover {
  background-position: 100% 50%;
  filter: brightness(1.2) saturate(1.3);
}
/* 5 — shimmer wash */

.hv-09__btn--wash {
  background: linear-gradient(135deg,var(--sky),var(--indigo));
  color: #fff;
}

.hv-09__btn--wash::before {
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
      90deg,
      transparent 0%,
      rgba(255,255,255,.6) 50%,
      transparent 100%
    );
}

.hv-09__btn--wash:hover::before {
  animation: hv-09-wash .9s ease-in-out forwards;
}

@keyframes hv-09-wash {
  0% {
    left: -100%;
  }

  100% {
    left: 100%;
  }
}

@media (max-width: 500px) {
  .hv-09__row {
    flex-direction: column;
    align-items: flex-start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-09__btn::before,
    .hv-09__btn::after {
    transition: none!important;
    animation: none!important;
  }
}
```
