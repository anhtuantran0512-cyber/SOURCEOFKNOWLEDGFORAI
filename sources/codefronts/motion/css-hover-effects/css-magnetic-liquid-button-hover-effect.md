---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-magnetic-liquid-button-hover-effect/"
title: "CSS Magnetic Liquid Button Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four button hover effects with fluid, organic transitions — liquid fill bubble, morphing border-radius blob, surface tension ripple, and stretched rubber —…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Magnetic Liquid Button Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-magnetic-liquid-button-hover-effect/

Four button hover effects with fluid, organic transitions — liquid fill bubble, morphing border-radius blob, surface tension ripple, and stretched rubber — using border-radius animation and pseudo-element scale transforms for a tactile, material-feeling interaction.
## HTML
```html
<div class="hv-07">
  <div class="hv-07__grid">
    <div class="hv-07__cell">
      <button class="hv-07__btn hv-07__btn--fill">
        <span>Liquid Fill</span>
      </button>
      <span class="hv-07__label">scale-Y fill</span>
    </div>
    <div class="hv-07__cell">
      <button class="hv-07__btn hv-07__btn--blob">
        <span>Blob Morph</span>
      </button>
      <span class="hv-07__label">border-radius keyframe</span>
    </div>
    <div class="hv-07__cell">
      <button class="hv-07__btn hv-07__btn--tension">
        <span>Surface Tension</span>
      </button>
      <span class="hv-07__label">ellipse clip-path burst</span>
    </div>
    <div class="hv-07__cell">
      <button class="hv-07__btn hv-07__btn--rubber">
        <span>Rubber Stretch</span>
      </button>
      <span class="hv-07__label">squash-and-stretch</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-07,
.hv-07 *,
.hv-07 *::before,
.hv-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-07 ::selection {
  background: #10b981;
  color: #fff;
}

.hv-07 {
  --bg: #030d09;
  --text: #d1fae5;
  --dim: #374151;
  --green: #10b981;
  --teal: #0d9488;
  --emerald: #059669;
  --mint: #6ee7b7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-07__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 48px;
  max-width: 720px;
  width: 100%;
}

.hv-07__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 48px 32px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 14px;
}

.hv-07__label {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared btn base */

.hv-07__btn {
  position: relative;
  overflow: hidden;
  padding: 14px 36px;
  border: 2px solid var(--green);
  background: transparent;
  color: var(--green);
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: .06em;
  border-radius: 8px;
  cursor: pointer;
  transition: color .35s;
}

.hv-07__btn span {
  position: relative;
  z-index: 1;
}

.hv-07__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
}
/* 1 — liquid fill */

.hv-07__btn--fill::before {
  background: var(--green);
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-07__btn--fill:hover::before {
  transform: scaleY(1);
}

.hv-07__btn--fill:hover {
  color: #fff;
}
/* 2 — blob morph */

.hv-07__btn--blob {
  border-color: var(--teal);
  color: var(--teal);
  border-radius: 8px;
  transition: border-radius .5s cubic-bezier(.4,0,.2,1),color .35s,background .35s;
}

.hv-07__btn--blob::before {
  background: var(--teal);
  border-radius: 8px;
  transform: scale(0);
  transition: transform .35s cubic-bezier(.4,0,.2,1),border-radius .5s;
}

.hv-07__btn--blob:hover {
  color: #fff;
  border-radius: 60% 40% 70% 30% / 40% 70% 30% 60%;
}

.hv-07__btn--blob:hover::before {
  transform: scale(1);
  border-radius: 60% 40% 70% 30% / 40% 70% 30% 60%;
}
/* 3 — surface tension (expanding emerald droplet from button center).
       The original used negative percentage margins (margin:-100% 0 0
       -100%) to center the ::after, but percentage margins resolve
       against the PARENT'S WIDTH on BOTH axes (not against the
       element's own size, and NOT against parent's height for
       top/bottom margins). On a wide button, margin-top:-100%
       overshoots by ~200px upward, pushing the entire droplet above
       the visible button area where overflow:hidden clips it to
       nothing.

       Fix: use transform translate(-50%, -50%) for the centering
       (translate-% uses the ELEMENT's own dimensions) and combine the
       scale in the same transform. The animated value is the scale
       inside the transform, so we declare the centered translate +
       scaled-to-zero state, and the :hover handler bumps the scale
       portion to 1 while the centering translate stays the same. */

.hv-07__btn--tension {
  border-color: var(--emerald);
  color: var(--emerald);
}

.hv-07__btn--tension::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200%;
  height: 200%;
  background: var(--emerald);
  border-radius: 50%;
  transform: translate(-50%,-50%) scale(0);
  transition: transform .5s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.hv-07__btn--tension:hover::after {
  transform: translate(-50%,-50%) scale(1);
}

.hv-07__btn--tension:hover {
  color: #fff;
}
/* 4 — rubber stretch */

.hv-07__btn--rubber {
  border-color: var(--mint);
  color: var(--mint);
  transition: transform .2s cubic-bezier(.4,0,.2,1),color .35s,background .35s,border-color .35s;
}

.hv-07__btn--rubber::before {
  background: var(--mint);
  transform: scaleY(0);
  transform-origin: bottom;
  transition: transform .35s;
}

.hv-07__btn--rubber:hover {
  transform: scaleX(1.06) scaleY(0.93);
  color: #000;
}

.hv-07__btn--rubber:hover::before {
  transform: scaleY(1);
}

.hv-07__btn--rubber:active {
  transform: scaleX(0.97) scaleY(1.04);
}

@media (max-width: 520px) {
  .hv-07__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-07__btn,
    .hv-07__btn::before,
    .hv-07__btn::after {
    transition: none!important;
    animation: none!important;
  }
}
```
