---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-3d-press-button-hover-effect/"
title: "CSS 3D Press Button Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Six physically satisfying 3D button press effects — layered shadow stack, extrude push-down, isometric depth, embossed groove, beveled edge, and neumorphic…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Press Button Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-3d-press-button-hover-effect/

Six physically satisfying 3D button press effects — layered shadow stack, extrude push-down, isometric depth, embossed groove, beveled edge, and neumorphic press — each simulating real depth through box-shadow and transform: translateY on hover.
## HTML
```html
<div class="hv-11">
  <div class="hv-11__grid">
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--stack">Push Down</button>
      <span class="hv-11__label">shadow shrink press</span>
    </div>
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--extrude">Extrude</button>
      <span class="hv-11__label">stacked shadow layers</span>
    </div>
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--iso">Isometric</button>
      <span class="hv-11__label">angled depth edge</span>
    </div>
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--emboss">Embossed</button>
      <span class="hv-11__label">groove press</span>
    </div>
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--bevel">Beveled</button>
      <span class="hv-11__label">inset bevel edges</span>
    </div>
    <div class="hv-11__cell">
      <button class="hv-11__btn hv-11__btn--neu">Neumorphic</button>
      <span class="hv-11__label">concave surface</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-11,
.hv-11 *,
.hv-11 *::before,
.hv-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-11 ::selection {
  background: #1d4ed8;
  color: #fff;
}

.hv-11 {
  --bg: #0b0f1a;
  --text: #e2e8f0;
  --dim: #475569;
  --blue: #3b82f6;
  --navy: #1d4ed8;
  --slate: #64748b;
  --neu: #e2e8f0;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-11__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 36px;
  max-width: 840px;
  width: 100%;
}

.hv-11__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 48px 20px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 12px;
}

.hv-11__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared btn */

.hv-11__btn {
  padding: 13px 32px;
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: .05em;
  cursor: pointer;
  border: none;
  border-radius: 8px;
  transition: transform .12s,box-shadow .12s;
}
/* 1 — classic push-down */

.hv-11__btn--stack {
  background: var(--blue);
  color: #fff;
  box-shadow: 0 6px 0 var(--navy);
  transform: translateY(0);
}

.hv-11__btn--stack:hover {
  transform: translateY(3px);
  box-shadow: 0 3px 0 var(--navy);
}

.hv-11__btn--stack:active {
  transform: translateY(6px);
  box-shadow: 0 0 0 var(--navy);
}
/* 2 — extrude stack (visible side-wall layers via 1px striations) */

.hv-11__btn--extrude {
  background: #f59e0b;
  color: #000;
  box-shadow: 0 2px 0 #b45309, 0 4px 0 #9a3412, 0 6px 0 #7c2d12, 0 8px 0 #5a1a08, 0 10px 0 #3d1004, 0 14px 18px rgba(0,0,0,.55);
  transform: translateY(0);
}

.hv-11__btn--extrude:hover {
  transform: translateY(8px);
  box-shadow: 0 1px 0 #b45309, 0 2px 0 #9a3412, 0 3px 6px rgba(0,0,0,.5);
}
/* 3 — isometric */

.hv-11__btn--iso {
  background: #10b981;
  color: #fff;
  box-shadow: 4px 4px 0 #065f46,5px 5px 0 #064e3b;
  transform: translate(0,0);
  transition: transform .12s,box-shadow .12s;
}

.hv-11__btn--iso:hover {
  transform: translate(4px,4px);
  box-shadow: 0 0 0 #065f46;
}
/* 4 — embossed groove (deeply recessed engraving, no platform shadow) */

.hv-11__btn--emboss {
  background: #1f2937;
  color: #9ca3af;
  text-shadow: 0 -1px 0 #000,0 1px 0 rgba(255,255,255,.08);
  box-shadow: inset 0 3px 6px rgba(0,0,0,.7), inset 0 -2px 4px rgba(0,0,0,.5), inset 0 1px 0 rgba(255,255,255,.06), inset 0 -1px 0 rgba(255,255,255,.03);
}

.hv-11__btn--emboss:hover {
  color: #e5e7eb;
  box-shadow: inset 0 4px 10px rgba(0,0,0,.9), inset 0 -3px 6px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.04);
}
/* 5 — beveled (strong dual-edge chamfer, clearly visible top/bottom bevels) */

.hv-11__btn--bevel {
  background: linear-gradient(180deg,#8b5cf6 0%,#7c3aed 50%,#5b21b6 100%);
  color: #fff;
  text-shadow: 0 -1px 0 rgba(0,0,0,.4);
  box-shadow: inset 0 3px 0 rgba(255,255,255,.4), inset 3px 0 0 rgba(255,255,255,.15), inset -3px 0 0 rgba(0,0,0,.25), inset 0 -4px 0 rgba(0,0,0,.45), 0 4px 0 #3c1a78, 0 6px 8px rgba(0,0,0,.4);
}

.hv-11__btn--bevel:hover {
  transform: translateY(2px);
  background: linear-gradient(180deg,#7c3aed 0%,#6d28d9 50%,#4c1d95 100%);
  box-shadow: inset 0 2px 0 rgba(255,255,255,.25), inset 2px 0 0 rgba(255,255,255,.1), inset -2px 0 0 rgba(0,0,0,.3), inset 0 -3px 0 rgba(0,0,0,.5), 0 2px 0 #3c1a78, 0 3px 4px rgba(0,0,0,.4);
}
/* 6 — neumorphic */

.hv-11__btn--neu {
  background: #e2e8f0;
  color: #334155;
  box-shadow: 5px 5px 10px #b8bec9, -5px -5px 10px #ffffff;
}

.hv-11__btn--neu:hover {
  box-shadow: inset 4px 4px 8px #b8bec9, inset -4px -4px 8px #ffffff;
}

@media (max-width: 640px) {
  .hv-11__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .hv-11__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-11__btn {
    transition: none!important;
  }
}
```
