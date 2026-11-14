---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-border-draw-hover-effect/"
title: "CSS Border Draw Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six button and card border-draw hover effects — clockwise stroke, corner flash, double-rail slide, snake crawl, dashed grow, and gradient border sweep — all…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Border Draw Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-border-draw-hover-effect/

Six button and card border-draw hover effects — clockwise stroke, corner flash, double-rail slide, snake crawl, dashed grow, and gradient border sweep — all achieved by animating pseudo-element dimensions or SVG-style techniques without JavaScript.
## HTML
```html
<div class="hv-08">
  <div class="hv-08__grid">
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--cw">Clockwise Draw</button>
      <span class="hv-08__label">clockwise stroke</span>
    </div>
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--corner">Corner Flash</button>
      <span class="hv-08__label">corner flash</span>
    </div>
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--rail">Double Rail</button>
      <span class="hv-08__label">dual-rail slide</span>
    </div>
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--dashed">Dashed Grow</button>
      <span class="hv-08__label">dashed border scale</span>
    </div>
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--grad">Gradient Sweep</button>
      <span class="hv-08__label">conic border sweep</span>
    </div>
    <div class="hv-08__cell">
      <button class="hv-08__btn hv-08__btn--inset">Inset Reveal</button>
      <span class="hv-08__label">box-shadow inset</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-08,
.hv-08 *,
.hv-08 *::before,
.hv-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-08 ::selection {
  background: #f59e0b;
  color: #000;
}

.hv-08 {
  --bg: #0c0a03;
  --text: #fef3c7;
  --dim: #6b7280;
  --amber: #f59e0b;
  --orange: #f97316;
  --red: #ef4444;
  --yellow: #fde047;
  --gold: #b45309;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-08__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 36px;
  max-width: 860px;
  width: 100%;
}

.hv-08__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 40px 20px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-08__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared btn base */

.hv-08__btn {
  position: relative;
  overflow: hidden;
  padding: 13px 32px;
  background: transparent;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: .05em;
  cursor: pointer;
}
/* 1 — clockwise draw */

.hv-08__btn--cw {
  color: var(--amber);
  border: none;
}

.hv-08__btn--cw::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 2px;
  background: var(--amber);
  transition: width .2s linear;
}

.hv-08__btn--cw::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--amber);
  transition: width .2s linear .4s;
}

.hv-08__btn--cw:hover::before {
  width: 100%;
  transition: width .2s linear;
}

.hv-08__btn--cw:hover::after {
  width: 100%;
  transition: width .2s linear .2s;
}
/* border sides via box-shadow on hover for left/right of CW */

.hv-08__btn--cw {
  box-shadow: inset 2px 0 0 transparent, inset -2px 0 0 transparent;
  transition: box-shadow .001s linear .39s,color .3s;
}

.hv-08__btn--cw:hover {
  color: var(--text);
  box-shadow: inset 2px 0 0 var(--amber), inset -2px 0 0 var(--amber);
  transition: box-shadow .2s linear .2s, color .3s;
}
/* 2 — corner flash (L-shaped pseudos grow on hover to form full border).
       Two problems with the original: (a) the shared .hv-08__btn rule
       sets overflow:hidden, which clipped the L-corner pseudo-elements
       (positioned at top/left/bottom/right: -2px — slightly OUTSIDE the
       button box). Result: invisible default state, no growth on hover.
       (b) The background-image: linear-gradient stack was meant as a
       border-box transparent-center trick but was incomplete (no
       background-origin pairing), so it just painted the page bg
       over everything including the corner indicators.

       Fix: override overflow to visible on this variant only (other
       variants still need overflow:hidden for their clip effects),
       and drop the broken background-image stack entirely — the
       transparent button is already transparent without it. */

.hv-08__btn--corner {
  color: var(--orange);
  overflow: visible;
  transition: color .3s;
}

.hv-08__btn--corner::before,
.hv-08__btn--corner::after {
  content: '';
  position: absolute;
  width: 12px;
  height: 12px;
  border-color: var(--orange);
  border-style: solid;
  transition: width .25s,height .25s;
}

.hv-08__btn--corner::before {
  top: -2px;
  left: -2px;
  border-width: 2px 0 0 2px;
}

.hv-08__btn--corner::after {
  bottom: -2px;
  right: -2px;
  border-width: 0 2px 2px 0;
}

.hv-08__btn--corner:hover::before,
.hv-08__btn--corner:hover::after {
  width: calc(100% + 4px);
  height: calc(100% + 4px);
}
/* 3 — double rail */

.hv-08__btn--rail {
  color: var(--red);
  border: none;
}

.hv-08__btn--rail::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 2px;
  background: var(--red);
  transition: left .35s cubic-bezier(.4,0,.2,1);
}

.hv-08__btn--rail::after {
  content: '';
  position: absolute;
  bottom: 0;
  right: -100%;
  width: 100%;
  height: 2px;
  background: var(--red);
  transition: right .35s cubic-bezier(.4,0,.2,1);
}

.hv-08__btn--rail:hover::before {
  left: 0;
}

.hv-08__btn--rail:hover::after {
  right: 0;
}

.hv-08__btn--rail:hover {
  color: var(--text);
}
/* 4 — dashed grow */

.hv-08__btn--dashed {
  color: var(--yellow);
  border: 2px dashed transparent;
  transition: border-color .3s,color .3s,padding .3s;
}

.hv-08__btn--dashed:hover {
  border-color: var(--yellow);
  padding: 13px 40px;
  color: var(--text);
}
/* 5 — gradient border sweep (conic gradient rotates around a 2px ring,
       button's bg covers the center so only the 2px edge shows the
       spinning gradient).

       Original implementation rotated the entire ::before pseudo-
       element via @keyframes transform: rotate(360deg). That works
       on SQUARE elements but the button is a wide rectangle
       (~189x43), so rotating the rectangle itself swings its
       corners through a huge arc — producing the "gradient wedge
       flapping in the background" effect the user reported.

       Fix: don't rotate the element. Instead use @property to
       register a custom property --angle as angle, then animate
       --angle inside the conic-gradient's "from angle" parameter.
       The ELEMENT stays put; only the gradient's start-angle
       rotates within the rectangle, producing a clean circular
       sweep visible only as a 2px ring (since ::after covers the
       center). @property support: Chrome 85+, Safari 16.4+,
       Firefox 128+ (~92% global). Older browsers see a static
       gradient — still looks intentional, just doesn't spin.

       Also fixed previously: overflow:visible override (shared
       .hv-08__btn sets overflow:hidden which clipped the gradient's
       2px overhang), and isolation:isolate to trap the pseudo-
       elements' negative z-index within the button's stacking
       context. */

@property --hv-08-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.hv-08__btn--grad {
  color: var(--text);
  border: none;
  background: transparent;
  overflow: visible;
  isolation: isolate;
}

.hv-08__btn--grad::before {
  content: '';
  position: absolute;
  inset: -2px;
  --hv-08-angle: 0deg;
  background: conic-gradient(from var(--hv-08-angle),transparent 0%,var(--amber) 30%,var(--orange) 50%,transparent 70%);
  border-radius: 4px;
  opacity: 0;
  transition: opacity .3s;
  z-index: -1;
}

.hv-08__btn--grad::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--bg);
  border-radius: 2px;
  z-index: -1;
}

.hv-08__btn--grad:hover::before {
  opacity: 1;
  animation: hv-08-spin 1.5s linear infinite;
}

@keyframes hv-08-spin {
  to {
    --hv-08-angle: 360deg;
  }
}
/* 6 — inset reveal */

.hv-08__btn--inset {
  color: var(--gold);
  border: none;
  box-shadow: inset 0 0 0 0 var(--amber);
  transition: box-shadow .4s cubic-bezier(.4,0,.2,1),color .4s;
}

.hv-08__btn--inset:hover {
  color: #000;
  box-shadow: inset 0 0 0 60px var(--amber);
}

@media (max-width: 640px) {
  .hv-08__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .hv-08__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-08__btn,
    .hv-08__btn::before,
    .hv-08__btn::after {
    transition: none!important;
    animation: none!important;
  }
}
```
