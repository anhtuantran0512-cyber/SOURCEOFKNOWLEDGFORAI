---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-subtle-shake-hover-effect/"
title: "CSS Subtle Shake Hover Effect"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The quiet end of the spectrum: filter chips with a 1px micro-jitter that makes them feel alive under the cursor, and an icon dock whose tools tilt ±2° with a…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Subtle Shake Hover Effect
Source: https://codefronts.com/motion/css-shake-animation/css-subtle-shake-hover-effect/

The quiet end of the spectrum: filter chips with a 1px micro-jitter that makes them feel alive under the cursor, and an icon dock whose tools tilt ±2° with a soft lift — both calibrated so users register 'responsive', not 'animation'.
## HTML
```html
<div class="shk-13-group">
<link href="https://fonts.googleapis.com/css2?family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-13a" aria-label="Filter chips with subtle hover jitter">
  <div class="shk-13a__stage">
    <p class="shk-13a__title">Browse the archive</p>
    <div class="shk-13a__row" role="list">
      <button class="shk-13a__chip" type="button" role="listitem">Editorial</button>
      <button class="shk-13a__chip" type="button" role="listitem">Brand systems</button>
      <button class="shk-13a__chip is-hot" type="button" role="listitem">Motion ✦</button>
      <button class="shk-13a__chip" type="button" role="listitem">Type specimens</button>
      <button class="shk-13a__chip" type="button" role="listitem">3D & spatial</button>
      <button class="shk-13a__chip" type="button" role="listitem">Archive '24</button>
    </div>
    <p class="shk-13a__hint" aria-hidden="true">hover slowly across the row — a .5px ping-pong you feel more than see</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-13b" aria-label="Icon dock with gentle tilt on hover">
  <div class="shk-13b__stage">
    <div class="shk-13b__dock">
      <button class="shk-13b__tool" type="button" aria-label="Pen tool"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle></svg></button>
      <button class="shk-13b__tool" type="button" aria-label="Shapes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="1"></rect><circle cx="17" cy="17" r="4"></circle><path d="M13 3l4 8h-8l4-8z" transform="translate(4 0)"></path></svg></button>
      <button class="shk-13b__tool" type="button" aria-label="Text"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4 7 4 4 20 4 20 7"></polyline><line x1="9" y1="20" x2="15" y2="20"></line><line x1="12" y1="4" x2="12" y2="20"></line></svg></button>
      <button class="shk-13b__tool" type="button" aria-label="Layers"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></button>
      <button class="shk-13b__tool" type="button" aria-label="Comment"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></button>
    </div>
    <p class="shk-13b__hint" aria-hidden="true">hover a tool — ±2° tilt, 2px lift, shadow deepens: “picked up”, not “vibrating”</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-13-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-13-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-13a,
.shk-13a *,
.shk-13a *::before,
.shk-13a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-13a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#fbfaf7,#f0efe9);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-13a__stage {
  text-align: center;
  max-width: 560px;
}

.shk-13a__title {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.015em;
  color: #22201b;
}

.shk-13a__row {
  margin-top: 22px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.shk-13a__chip {
  padding: 10px 18px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  color: #22201b;
  background: #fff;
  border: 1.5px solid rgba(34,32,27,.16);
  border-radius: 999px;
  cursor: pointer;
  transition: border-color .2s,background .2s,color .2s;
}

.shk-13a__chip:hover {
  border-color: #22201b;
  animation: shk-13a-jitter .28s steps(2,jump-none) infinite;
}

.shk-13a__chip:active {
  background: #22201b;
  color: #fbfaf7;
}

.shk-13a__chip.is-hot {
  background: oklch(0.85 0.12 95);
  border-color: oklch(0.6 0.12 95);
}

.shk-13a__hint {
  margin-top: 24px;
  font-size: 12px;
  color: rgba(34,32,27,.45);
}

@keyframes shk-13a-jitter {
  0% {
    translate: -.5px .5px;
  }

  100% {
    translate: .5px -.5px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-13a__chip:hover {
    animation: none;
  }
}

.shk-13b,
.shk-13b *,
.shk-13b *::before,
.shk-13b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-13b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 110% at 50% 0%,#191c24,#0e1015);
}

.shk-13b__stage {
  text-align: center;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-13b__dock {
  display: flex;
  gap: 10px;
  padding: 12px;
  border-radius: 20px;
  background: rgba(255,255,255,.055);
  border: 1px solid rgba(170,190,225,.15);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.06);
}

.shk-13b__tool {
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 14px;
  background: rgba(255,255,255,.06);
  color: #d9e2f2;
  cursor: pointer;
  transition: background .2s,translate .18s,box-shadow .18s;
}

.shk-13b__tool svg {
  width: 23px;
  height: 23px;
}

.shk-13b__tool:hover {
  background: rgba(255,255,255,.12);
  translate: 0 -3px;
  box-shadow: 0 10px 18px -8px rgba(0,0,0,.7);
  animation: shk-13b-tilt .9s ease-in-out .05s infinite;
}

.shk-13b__tool:active {
  translate: 0 0;
  animation: none;
}

.shk-13b__tool:focus-visible {
  outline: 2px solid #d9e2f2;
  outline-offset: 3px;
}

.shk-13b__hint {
  margin-top: 24px;
  font-size: 12px;
  color: rgba(217,226,242,.4);
}

@keyframes shk-13b-tilt {
  0%,
    100% {
    rotate: 0deg;
  }

  30% {
    rotate: 2deg;
  }

  70% {
    rotate: -2deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-13b__tool:hover {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a two-frame .5px ping-pong (steps(2, jump-none)) at ~3.5Hz. On 2× displays the browser maps .5px to one device pixel: shimmer, not shake. */

/* No JavaScript — the transition owns the lift (translate + shadow), the animation owns the slow ±2° tilt, and starting the tilt .05s late lets the “pickup” read before the wobble begins. */
```
