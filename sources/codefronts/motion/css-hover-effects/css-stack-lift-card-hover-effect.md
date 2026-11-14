---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-stack-lift-card-hover-effect/"
title: "CSS Stack Lift Card Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four stacked card hover effects — single card lift with shadow bloom, layered deck fan-out, cascading z-lift, and magnetic group hover — using translateY,…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stack Lift Card Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-stack-lift-card-hover-effect/

Four stacked card hover effects — single card lift with shadow bloom, layered deck fan-out, cascading z-lift, and magnetic group hover — using translateY, box-shadow, and sibling selectors to create physical depth when hovering a stack of UI cards.
## HTML
```html
<div class="hv-18">
  <div class="hv-18__demos">
    <div class="hv-18__demo">
      <div class="hv-18__single">
        <div class="hv-18__card hv-18__card--single">
          <div class="hv-18__icon">◈</div>
          <h3 class="hv-18__title">Lift Me</h3>
          <p class="hv-18__text">Single card rise and shadow bloom.</p>
        </div>
      </div>
      <span class="hv-18__label">shadow bloom lift</span>
    </div>
    <div class="hv-18__demo">
      <div class="hv-18__deck">
        <div class="hv-18__card hv-18__card--deck hv-18__card--d1">
          <div class="hv-18__icon">★</div>
          <h3 class="hv-18__title">Fan Out</h3>
        </div>
        <div class="hv-18__card hv-18__card--deck hv-18__card--d2"></div>
        <div class="hv-18__card hv-18__card--deck hv-18__card--d3"></div>
      </div>
      <span class="hv-18__label">sibling fan-out</span>
    </div>
    <div class="hv-18__demo">
      <div class="hv-18__cascade">
        <div class="hv-18__card hv-18__card--cas hv-18__card--c1">
          <span class="hv-18__num">01</span>
        </div>
        <div class="hv-18__card hv-18__card--cas hv-18__card--c2">
          <span class="hv-18__num">02</span>
        </div>
        <div class="hv-18__card hv-18__card--cas hv-18__card--c3">
          <span class="hv-18__num">03</span>
        </div>
      </div>
      <span class="hv-18__label">cascade z-lift</span>
    </div>
    <div class="hv-18__demo">
      <div class="hv-18__group">
        <div class="hv-18__card hv-18__card--grp">A</div>
        <div class="hv-18__card hv-18__card--grp">B</div>
        <div class="hv-18__card hv-18__card--grp">C</div>
      </div>
      <span class="hv-18__label">group isolation</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-18,
.hv-18 *,
.hv-18 *::before,
.hv-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-18 ::selection {
  background: #0f766e;
  color: #fff;
}

.hv-18 {
  --bg: #020c08;
  --text: #d1fae5;
  --dim: #6b7280;
  --green: #10b981;
  --teal: #14b8a6;
  --emerald: #059669;
  --sage: #6ee7b7;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-18__demos {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 40px;
  max-width: 760px;
  width: 100%;
}

.hv-18__demo {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  padding: 40px 24px;
  background: rgba(255,255,255,.025);
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 16px;
}

.hv-18__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}
/* shared card */

.hv-18__card {
  border-radius: 12px;
  cursor: pointer;
}

.hv-18__icon {
  font-size: 1.6rem;
  color: var(--green);
}

.hv-18__title {
  font-size: .95rem;
  font-weight: 700;
  color: var(--text);
}

.hv-18__text {
  font-size: .8rem;
  color: var(--dim);
  line-height: 1.4;
}

.hv-18__num {
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--text);
}
/* 1 — single lift */

.hv-18__single {
  padding-bottom: 24px;
}

.hv-18__card--single {
  padding: 24px;
  width: 200px;
  background: rgba(16,185,129,.12);
  border: 1px solid rgba(16,185,129,.25);
  display: flex;
  flex-direction: column;
  gap: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,.3);
  transition: transform .35s cubic-bezier(.4,0,.2,1),box-shadow .35s;
}

.hv-18__card--single:hover {
  transform: translateY(-14px);
  box-shadow: 0 28px 56px rgba(0,0,0,.5),0 0 24px rgba(16,185,129,.2);
}
/* 2 — deck fan-out */

.hv-18__deck {
  position: relative;
  width: 180px;
  height: 160px;
}

.hv-18__card--deck {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border: 1px solid rgba(255,255,255,.1);
  transition: transform .4s cubic-bezier(.4,0,.2,1);
}

.hv-18__card--d1 {
  background: rgba(16,185,129,.2);
  z-index: 3;
}

.hv-18__card--d2 {
  background: rgba(5,150,105,.15);
  z-index: 2;
  transform: translateY(8px);
}

.hv-18__card--d3 {
  background: rgba(4,120,87,.1);
  z-index: 1;
  transform: translateY(16px);
}

.hv-18__deck:hover .hv-18__card--d1 {
  transform: translateY(-12px);
}

.hv-18__deck:hover .hv-18__card--d2 {
  transform: translateY(4px);
}

.hv-18__deck:hover .hv-18__card--d3 {
  transform: translateY(20px);
}
/* 3 — cascade */

.hv-18__cascade {
  display: flex;
  gap: 10px;
  align-items: flex-end;
}

.hv-18__card--cas {
  width: 60px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255,255,255,.1);
  transition: transform .35s cubic-bezier(.4,0,.2,1),box-shadow .35s;
}

.hv-18__card--c1 {
  background: rgba(20,184,166,.2);
  height: 80px;
}

.hv-18__card--c2 {
  background: rgba(16,185,129,.2);
  height: 100px;
}

.hv-18__card--c3 {
  background: rgba(5,150,105,.2);
  height: 120px;
}

.hv-18__card--c1:hover {
  transform: translateY(-10px);
  box-shadow: 0 12px 30px rgba(0,0,0,.4);
}

.hv-18__card--c2:hover {
  transform: translateY(-14px);
  box-shadow: 0 16px 36px rgba(0,0,0,.4);
}

.hv-18__card--c3:hover {
  transform: translateY(-18px);
  box-shadow: 0 20px 40px rgba(0,0,0,.4);
}
/* 4 — group hover isolation */

.hv-18__group {
  display: flex;
  gap: 10px;
}

.hv-18__card--grp {
  width: 56px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  border-radius: 10px;
  background: rgba(16,185,129,.2);
  border: 1px solid rgba(16,185,129,.3);
  transition: transform .3s,opacity .3s,box-shadow .3s;
}

.hv-18__group:hover .hv-18__card--grp {
  opacity: .35;
  transform: scale(0.95);
}

.hv-18__group:hover .hv-18__card--grp:hover {
  opacity: 1;
  transform: translateY(-10px);
  box-shadow: 0 16px 36px rgba(0,0,0,.4);
}

@media (max-width: 520px) {
  .hv-18__demos {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-18__card {
    transition: none!important;
  }
}
```
