---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-spotlight-card-hover-effect/"
title: "CSS Spotlight Card Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four spotlight and lighting hover effects on cards — radial gradient center spotlight, corner-origin light sweep, edge scanline, and vignette-lift — using…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Spotlight Card Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-spotlight-card-hover-effect/

Four spotlight and lighting hover effects on cards — radial gradient center spotlight, corner-origin light sweep, edge scanline, and vignette-lift — using CSS radial-gradient pseudo-elements to simulate a focused light source illuminating the card face on hover.
## HTML
```html
<div class="hv-16">
  <div class="hv-16__grid">
    <div class="hv-16__card hv-16__card--center">
      <div class="hv-16__content">
        <div class="hv-16__icon">◎</div>
        <h3 class="hv-16__title">Center Spot</h3>
        <p class="hv-16__text">Radial gradient fades in from the center on hover.</p>
      </div>
    </div>
    <div class="hv-16__card hv-16__card--corner">
      <div class="hv-16__content">
        <div class="hv-16__icon">◤</div>
        <h3 class="hv-16__title">Corner Light</h3>
        <p class="hv-16__text">Conic light sweep from the top-left corner lamp.</p>
      </div>
    </div>
    <div class="hv-16__card hv-16__card--scan">
      <div class="hv-16__content">
        <div class="hv-16__icon">▤</div>
        <h3 class="hv-16__title">Edge Scan</h3>
        <p class="hv-16__text">Bright scan band sweeps top to bottom on hover.</p>
      </div>
    </div>
    <div class="hv-16__card hv-16__card--vignette">
      <div class="hv-16__content">
        <div class="hv-16__icon">◉</div>
        <h3 class="hv-16__title">Vignette Lift</h3>
        <p class="hv-16__text">Dark vignette fades out revealing the full card face.</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-16,
.hv-16 *,
.hv-16 *::before,
.hv-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-16 ::selection {
  background: #0f766e;
  color: #fff;
}

.hv-16 {
  --bg: #020c0b;
  --text: #ccfbf1;
  --dim: #6b7280;
  --teal: #14b8a6;
  --green: #10b981;
  --cyan: #06b6d4;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-16__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 32px;
  max-width: 720px;
  width: 100%;
}
/* shared card */

.hv-16__card {
  position: relative;
  overflow: hidden;
  min-height: 220px;
  border-radius: 16px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.1);
  cursor: pointer;
  transition: border-color .4s,transform .4s;
}

.hv-16__card:hover {
  border-color: rgba(20,184,166,.3);
  transform: translateY(-4px);
}

.hv-16__card::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  transition: opacity .4s;
}

.hv-16__content {
  position: relative;
  z-index: 1;
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hv-16__icon {
  font-size: 1.8rem;
  color: var(--teal);
}

.hv-16__title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
}

.hv-16__text {
  font-size: .85rem;
  color: var(--dim);
  line-height: 1.5;
}
/* 1 — center spotlight */

.hv-16__card--center::before {
  background: radial-gradient(circle at 50% 50%,rgba(20,184,166,.18) 0%,transparent 65%);
  opacity: 0;
}

.hv-16__card--center:hover::before {
  opacity: 1;
}
/* 2 — corner sweep */

.hv-16__card--corner::before {
  background: conic-gradient(from 225deg at 0% 0%,rgba(6,182,212,.25),transparent 40%);
  opacity: 0;
}

.hv-16__card--corner:hover::before {
  opacity: 1;
}
/* 3 — scan band */

.hv-16__card--scan::before {
  background: linear-gradient(180deg,transparent 0%,rgba(20,184,166,.15) 40%,rgba(20,184,166,.15) 60%,transparent 100%);
  opacity: 0;
  transform: translateY(-100%);
  transition: opacity .3s,transform .5s cubic-bezier(.4,0,.2,1);
}

.hv-16__card--scan:hover::before {
  opacity: 1;
  transform: translateY(60%);
}
/* 4 — vignette lift */

.hv-16__card--vignette::before {
  background: radial-gradient(ellipse at center,transparent 40%,rgba(0,0,0,.7) 100%);
  opacity: 1;
  transition: opacity .4s;
}

.hv-16__card--vignette:hover::before {
  opacity: 0;
}

@media (max-width: 520px) {
  .hv-16__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-16__card,
    .hv-16__card::before {
    transition: none!important;
  }
}
```
