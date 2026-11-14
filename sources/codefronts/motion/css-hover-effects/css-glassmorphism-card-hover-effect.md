---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-glassmorphism-card-hover-effect/"
title: "CSS Glassmorphism Card Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four glassmorphism card hover effects — frosted clarity increase, edge glow border, blur-depth stack, and reflective tinted glass — using backdrop-filter,…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Card Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-glassmorphism-card-hover-effect/

Four glassmorphism card hover effects — frosted clarity increase, edge glow border, blur-depth stack, and reflective tinted glass — using backdrop-filter, border transparency transitions, and box-shadow layers to simulate frosted glass UI on hover.
## HTML
```html
<div class="hv-15">
  <div class="hv-15__bg">
    <div class="hv-15__orb hv-15__orb--1"></div>
    <div class="hv-15__orb hv-15__orb--2"></div>
    <div class="hv-15__orb hv-15__orb--3"></div>
  </div>
  <div class="hv-15__grid">
    <div class="hv-15__card hv-15__card--clarity">
      <div class="hv-15__icon">✦</div>
      <h3 class="hv-15__title">Frosted Clarity</h3>
      <p class="hv-15__text">Blur depth increases on hover, making the panel appear to thicken.</p>
    </div>
    <div class="hv-15__card hv-15__card--glow">
      <div class="hv-15__icon">◉</div>
      <h3 class="hv-15__title">Edge Glow</h3>
      <p class="hv-15__text">Border lights up with accent color and a matching halo shadow.</p>
    </div>
    <div class="hv-15__card hv-15__card--depth">
      <div class="hv-15__icon">⬡</div>
      <h3 class="hv-15__title">Depth Stack</h3>
      <p class="hv-15__text">Layered glass panels separate on hover revealing depth.</p>
    </div>
    <div class="hv-15__card hv-15__card--reflect">
      <div class="hv-15__icon">◈</div>
      <h3 class="hv-15__title">Reflection</h3>
      <p class="hv-15__text">Specular highlight sweeps across the glass surface on hover.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-15,
.hv-15 *,
.hv-15 *::before,
.hv-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-15 ::selection {
  background: #7c3aed;
  color: #fff;
}

.hv-15 {
  --bg: #080514;
  --text: #e2d9f3;
  --dim: #9ca3af;
  --purple: #7c3aed;
  --pink: #ec4899;
  --cyan: #06b6d4;
  --white: rgba(255,255,255,.9);
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  position: relative;
  overflow: hidden;
}

.hv-15__bg {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.hv-15__orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: .45;
}

.hv-15__orb--1 {
  width: 400px;
  height: 400px;
  background: #7c3aed;
  top: -100px;
  left: -100px;
}

.hv-15__orb--2 {
  width: 350px;
  height: 350px;
  background: #ec4899;
  bottom: -80px;
  right: -60px;
}

.hv-15__orb--3 {
  width: 280px;
  height: 280px;
  background: #06b6d4;
  top: 30%;
  left: 40%;
}

.hv-15__grid {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 28px;
  max-width: 720px;
  width: 100%;
}
/* shared card */

.hv-15__card {
  padding: 32px;
  border-radius: 20px;
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,.12);
  display: flex;
  flex-direction: column;
  gap: 14px;
  cursor: pointer;
  transition: background .4s,border-color .4s,box-shadow .4s,transform .4s;
}

.hv-15__icon {
  font-size: 1.8rem;
  color: var(--text);
}

.hv-15__title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
}

.hv-15__text {
  font-size: .85rem;
  color: var(--dim);
  line-height: 1.5;
}
/* 1 — clarity increase */

.hv-15__card--clarity:hover {
  background: rgba(255,255,255,.14);
  -webkit-backdrop-filter: blur(24px);
  backdrop-filter: blur(24px);
  border-color: rgba(255,255,255,.25);
  transform: translateY(-4px);
}
/* 2 — edge glow */

.hv-15__card--glow {
  --glow: rgba(124,58,237,0);
  box-shadow: 0 0 0 0 var(--glow);
}

.hv-15__card--glow:hover {
  border-color: rgba(124,58,237,.6);
  box-shadow: 0 0 0 1px rgba(124,58,237,.3),0 0 24px rgba(124,58,237,.4),inset 0 0 24px rgba(124,58,237,.05);
  background: rgba(124,58,237,.08);
}
/* 3 — depth stack via box-shadow layers */

.hv-15__card--depth {
  box-shadow: 0 4px 20px rgba(0,0,0,.2);
}

.hv-15__card--depth:hover {
  transform: translateY(-8px);
  box-shadow: 0 2px 8px rgba(0,0,0,.2), 0 16px 40px rgba(0,0,0,.4), 0 32px 60px rgba(0,0,0,.2);
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.2);
}
/* 4 — reflective sweep */

.hv-15__card--reflect {
  position: relative;
  overflow: hidden;
}

.hv-15__card--reflect::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -60%;
  width: 40%;
  height: 200%;
  background: linear-gradient(105deg,transparent,rgba(255,255,255,.12),transparent);
  transform: skewX(-20deg);
  transition: left .5s cubic-bezier(.4,0,.2,1);
  pointer-events: none;
}

.hv-15__card--reflect:hover::before {
  left: 120%;
}

.hv-15__card--reflect:hover {
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.2);
}

@media (max-width: 520px) {
  .hv-15__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-15__card {
    transition: none!important;
  }

  .hv-15__card--reflect::before {
    transition: none!important;
  }
}
```
