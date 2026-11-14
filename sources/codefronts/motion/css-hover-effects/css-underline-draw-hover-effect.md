---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-underline-draw-hover-effect/"
title: "CSS Underline Draw Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six scoped link and heading hover styles that animate underlines from invisible to visible — left-to-right draw, center-out expand, two-tone dual-line,…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Underline Draw Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-underline-draw-hover-effect/

Six scoped link and heading hover styles that animate underlines from invisible to visible — left-to-right draw, center-out expand, two-tone dual-line, offset thick bar, dotted border, and gradient sweep — all driven by CSS custom properties and pseudo-element transforms.
## HTML
```html
<div class="hv-01">
  <div class="hv-01__grid">
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--ltr" href="#">Left-to-Right Draw</a>
      <span class="hv-01__label">scaleX · left origin</span>
    </div>
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--center" href="#">Center Expand</a>
      <span class="hv-01__label">scaleX · center origin</span>
    </div>
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--dual" href="#">Dual Line Sweep</a>
      <span class="hv-01__label">::before + ::after toward center</span>
    </div>
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--thick" href="#">Thick Bar Slide</a>
      <span class="hv-01__label">offset bold underbar</span>
    </div>
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--dot" href="#">Dotted Border Grow</a>
      <span class="hv-01__label">border-bottom + scaleX</span>
    </div>
    <div class="hv-01__cell">
      <a class="hv-01__link hv-01__link--grad" href="#">Gradient Sweep</a>
      <span class="hv-01__label">background-size animation</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-01,
.hv-01 *,
.hv-01 *::before,
.hv-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-01 ::selection {
  background: #f72585;
  color: #fff;
}

.hv-01 {
  --bg: #0a0a0f;
  --text: #e8e6f0;
  --dim: #666;
  --accent: #f72585;
  --cyan: #4cc9f0;
  --gold: #ffd60a;
  --green: #06d6a0;
  --orange: #fb5607;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-01__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 40px 60px;
  max-width: 900px;
  width: 100%;
}

.hv-01__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 40px 24px;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-01__label {
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--dim);
  text-align: center;
}
/* shared link base */

.hv-01__link {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text);
  text-decoration: none;
  position: relative;
  display: inline-block;
  padding-bottom: 4px;
}
/* 1 — left-to-right draw */

.hv-01__link--ltr::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.hv-01__link--ltr:hover::after {
  transform: scaleX(1);
}
/* 2 — center expand */

.hv-01__link--center::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2px;
  background: var(--cyan);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-01__link--center:hover::after {
  transform: scaleX(1);
}
/* 3 — dual line sweep */

.hv-01__link--dual::before,
.hv-01__link--dual::after {
  content: '';
  position: absolute;
  left: 0;
  width: 100%;
  height: 2px;
  background: var(--gold);
  transform: scaleX(0);
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-01__link--dual::before {
  bottom: 6px;
  transform-origin: right;
}

.hv-01__link--dual::after {
  bottom: 0;
  transform-origin: left;
}

.hv-01__link--dual:hover::before,
.hv-01__link--dual:hover::after {
  transform: scaleX(1);
}
/* 4 — thick offset bar (highlighter effect).
       The :hover swaps text to var(--bg) so it reads as dark text on
       a bright green highlight. For the bar to land BEHIND the text
       but ABOVE the cell background, the link itself must create a
       stacking context — otherwise z-index:-1 on the ::after escapes
       the link and lands behind the cell's translucent fill, hiding
       the entire highlight. isolation:isolate creates that local
       stacking context without affecting the link's positioning.
       Bar height bumped from 6px to a fuller block so it visually
       reads as a highlighter rather than a thin underline; bottom
       offset adjusted so the bar covers the full text height. */

.hv-01__link--thick {
  isolation: isolate;
}

.hv-01__link--thick::after {
  content: '';
  position: absolute;
  left: -6px;
  bottom: 0;
  width: calc(100% + 12px);
  height: 100%;
  background: var(--green);
  border-radius: 3px;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .35s cubic-bezier(.22,1,.36,1);
  z-index: -1;
  opacity: .85;
}

.hv-01__link--thick:hover::after {
  transform: scaleX(1);
}

.hv-01__link--thick:hover {
  color: var(--bg);
}
/* 5 — dotted border grow */

.hv-01__link--dot::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  border-bottom: 2px dotted var(--orange);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .4s ease;
}

.hv-01__link--dot:hover::after {
  transform: scaleX(1);
}

.hv-01__link--dot:hover {
  color: var(--orange);
}
/* 6 — gradient background-size sweep */

.hv-01__link--grad {
  background-image: linear-gradient(90deg,var(--accent),var(--cyan));
  background-repeat: no-repeat;
  background-size: 0% 2px;
  background-position: left bottom;
  transition: background-size .4s cubic-bezier(.4,0,.2,1),color .3s;
}

.hv-01__link--grad:hover {
  background-size: 100% 2px;
  color: var(--accent);
}

@media (max-width: 680px) {
  .hv-01__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 440px) {
  .hv-01__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-01__link::before,
    .hv-01__link::after {
    transition: none!important;
  }

  .hv-01__link--grad {
    transition: none!important;
  }
}
```
