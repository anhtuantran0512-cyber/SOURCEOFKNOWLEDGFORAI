---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-3d-tilt-card-hover-effect/"
title: "CSS 3D Tilt Card Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four card hover effects with perspective-based 3D depth — static tilt corner, perspective flip-axis, floating lift with shadow depth, and layered parallax…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Tilt Card Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-3d-tilt-card-hover-effect/

Four card hover effects with perspective-based 3D depth — static tilt corner, perspective flip-axis, floating lift with shadow depth, and layered parallax layers — using CSS perspective, rotateX/Y transforms, and transform-style: preserve-3d.
## HTML
```html
<div class="hv-13">
  <div class="hv-13__grid">
    <div class="hv-13__scene">
      <div class="hv-13__card hv-13__card--tilt">
        <div class="hv-13__card-body">
          <div class="hv-13__icon">◈</div>
          <h3 class="hv-13__title">Static Tilt</h3>
          <p class="hv-13__text">Perspective rotateX + rotateY on hover</p>
        </div>
      </div>
    </div>
    <div class="hv-13__scene">
      <div class="hv-13__card hv-13__card--flip">
        <div class="hv-13__card-body">
          <div class="hv-13__icon">⬡</div>
          <h3 class="hv-13__title">Axis Flip</h3>
          <p class="hv-13__text">rotateY 180° perspective reveal</p>
        </div>
      </div>
    </div>
    <div class="hv-13__scene hv-13__scene--lift">
      <div class="hv-13__card hv-13__card--lift">
        <div class="hv-13__card-body">
          <div class="hv-13__icon">▲</div>
          <h3 class="hv-13__title">Float Lift</h3>
          <p class="hv-13__text">translateY + shadow depth</p>
        </div>
      </div>
    </div>
    <div class="hv-13__scene">
      <div class="hv-13__card hv-13__card--layers">
        <div class="hv-13__layer hv-13__layer--bg"></div>
        <div class="hv-13__layer hv-13__layer--mid">
          <div class="hv-13__icon">◉</div>
        </div>
        <div class="hv-13__layer hv-13__layer--top">
          <h3 class="hv-13__title">Parallax</h3>
          <p class="hv-13__text">translateZ layered depth</p>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-13,
.hv-13 *,
.hv-13 *::before,
.hv-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-13 ::selection {
  background: #0284c7;
  color: #fff;
}

.hv-13 {
  --bg: #020810;
  --text: #bae6fd;
  --dim: #475569;
  --blue: #0ea5e9;
  --sky: #38bdf8;
  --indigo: #6366f1;
  --teal: #14b8a6;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-13__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 40px;
  max-width: 760px;
  width: 100%;
}

.hv-13__scene {
  perspective: 800px;
}

.hv-13__card {
  width: 100%;
  min-height: 220px;
  border-radius: 16px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.1);
  transition: transform .4s cubic-bezier(.4,0,.2,1),box-shadow .4s;
  transform-style: preserve-3d;
  cursor: pointer;
}

.hv-13__card-body {
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hv-13__icon {
  font-size: 2rem;
  color: var(--blue);
}

.hv-13__title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
}

.hv-13__text {
  font-size: .85rem;
  color: var(--dim);
  line-height: 1.5;
}
/* 1 — static tilt */

.hv-13__card--tilt:hover {
  transform: rotateX(8deg) rotateY(-8deg);
  box-shadow: 8px 12px 40px rgba(14,165,233,.3);
}
/* 2 — axis flip */

.hv-13__card--flip {
  border-color: rgba(99,102,241,.3);
}

.hv-13__card--flip .hv-13__icon {
  color: var(--indigo);
}

.hv-13__card--flip:hover {
  transform: rotateX(-6deg) rotateY(10deg);
  box-shadow: -10px 8px 40px rgba(99,102,241,.3);
  border-color: rgba(99,102,241,.6);
}
/* 3 — float lift */

.hv-13__card--lift {
  border-color: rgba(20,184,166,.3);
  box-shadow: 0 4px 20px rgba(0,0,0,.4);
  transition: transform .4s cubic-bezier(.4,0,.2,1),box-shadow .4s;
}

.hv-13__card--lift .hv-13__icon {
  color: var(--teal);
}

.hv-13__card--lift:hover {
  transform: translateY(-14px);
  box-shadow: 0 28px 60px rgba(0,0,0,.5),0 0 30px rgba(20,184,166,.2);
}
/* 4 — parallax layers */

.hv-13__card--layers {
  position: relative;
  min-height: 220px;
  overflow: visible;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
  border-color: rgba(56,189,248,.3);
}

.hv-13__card--layers:hover {
  transform: rotateX(6deg) rotateY(-6deg);
}

.hv-13__layer {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-13__layer--bg {
  background: linear-gradient(135deg,rgba(14,165,233,.1),rgba(56,189,248,.05));
}

.hv-13__layer--mid {
  display: flex;
  align-items: flex-start;
  padding: 32px;
}

.hv-13__layer--mid .hv-13__icon {
  color: var(--sky);
  font-size: 2.5rem;
}

.hv-13__card--layers:hover .hv-13__layer--mid {
  transform: translateZ(20px) translateY(-6px);
}

.hv-13__layer--top {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 28px;
  gap: 8px;
}

.hv-13__card--layers:hover .hv-13__layer--top {
  transform: translateZ(35px) translateY(-4px);
}

@media (max-width: 520px) {
  .hv-13__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-13__card,
    .hv-13__layer {
    transition: none!important;
  }
}
```
