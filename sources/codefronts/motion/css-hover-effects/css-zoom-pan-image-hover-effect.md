---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-zoom-pan-image-hover-effect/"
title: "CSS Zoom Pan Image Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five image hover effects using CSS transforms on a contained image — center zoom, corner-pan zoom, slow drift ken-burns, zoom plus brightness, and clip-path…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Zoom Pan Image Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-zoom-pan-image-hover-effect/

Five image hover effects using CSS transforms on a contained image — center zoom, corner-pan zoom, slow drift ken-burns, zoom plus brightness, and clip-path crop zoom — demonstrating how scale, translate, and clip-path on overflow-hidden containers create cinematic image reveals.
## HTML
```html
<div class="hv-19">
  <div class="hv-19__grid">
    <div class="hv-19__cell">
      <div class="hv-19__wrap">
        <div class="hv-19__img hv-19__img--center hv-19__swatch--blue"></div>
      </div>
      <span class="hv-19__label">center zoom</span>
    </div>
    <div class="hv-19__cell">
      <div class="hv-19__wrap">
        <div class="hv-19__img hv-19__img--pan hv-19__swatch--violet"></div>
      </div>
      <span class="hv-19__label">corner-pan zoom</span>
    </div>
    <div class="hv-19__cell">
      <div class="hv-19__wrap">
        <div class="hv-19__img hv-19__img--drift hv-19__swatch--amber"></div>
      </div>
      <span class="hv-19__label">slow ken-burns drift</span>
    </div>
    <div class="hv-19__cell">
      <div class="hv-19__wrap">
        <div class="hv-19__img hv-19__img--bright hv-19__swatch--emerald"></div>
      </div>
      <span class="hv-19__label">zoom + brightness</span>
    </div>
    <div class="hv-19__cell">
      <div class="hv-19__wrap hv-19__wrap--crop">
        <div class="hv-19__img hv-19__img--crop hv-19__swatch--rose"></div>
      </div>
      <span class="hv-19__label">clip-path crop zoom</span>
    </div>
    <div class="hv-19__cell">
      <div class="hv-19__wrap">
        <div class="hv-19__img hv-19__img--rotate hv-19__swatch--teal"></div>
      </div>
      <span class="hv-19__label">zoom + rotation</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-19,
.hv-19 *,
.hv-19 *::before,
.hv-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-19 ::selection {
  background: #1d4ed8;
  color: #fff;
}

.hv-19 {
  --bg: #08080f;
  --dim: #6b7280;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-19__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 24px;
  max-width: 840px;
  width: 100%;
}

.hv-19__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.hv-19__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.hv-19__wrap {
  width: 100%;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 12px;
  cursor: pointer;
}

.hv-19__img {
  width: 100%;
  height: 100%;
  transition: transform .6s cubic-bezier(.4,0,.2,1),filter .6s,clip-path .6s;
}
/* layered pseudo-images: focal radial + grid pattern + diagonal lines + base color
   gives multiple visual anchors so zoom/pan/rotate are clearly perceptible */

.hv-19__swatch--blue {
  background: radial-gradient(circle at 30% 40%,#fef3c7 0%,transparent 18%), radial-gradient(circle at 70% 70%,#fbbf24 0%,transparent 22%), repeating-linear-gradient(45deg,transparent 0 16px,rgba(255,255,255,.08) 16px 17px), repeating-linear-gradient(-45deg,transparent 0 24px,rgba(0,0,0,.12) 24px 25px), linear-gradient(135deg,#1e40af,#3b82f6,#93c5fd,#1e3a8a);
}

.hv-19__swatch--violet {
  background: radial-gradient(circle at 25% 35%,#fce7f3 0%,transparent 16%), radial-gradient(circle at 65% 60%,#ec4899 0%,transparent 24%), repeating-linear-gradient(60deg,transparent 0 18px,rgba(255,255,255,.1) 18px 19px), repeating-linear-gradient(-30deg,transparent 0 28px,rgba(0,0,0,.15) 28px 29px), linear-gradient(135deg,#5b21b6,#7c3aed,#c4b5fd,#4c1d95);
}

.hv-19__swatch--amber {
  background: radial-gradient(circle at 70% 30%,#fef9c3 0%,#fde047 8%,transparent 20%), radial-gradient(circle at 25% 75%,#dc2626 0%,transparent 18%), repeating-linear-gradient(90deg,transparent 0 22px,rgba(0,0,0,.12) 22px 23px), repeating-linear-gradient(0deg,transparent 0 22px,rgba(255,255,255,.08) 22px 23px), linear-gradient(135deg,#92400e,#f59e0b,#fde68a,#78350f);
}

.hv-19__swatch--emerald {
  background: radial-gradient(circle at 40% 30%,#fef9c3 0%,transparent 14%), radial-gradient(circle at 75% 65%,#a7f3d0 0%,transparent 28%), repeating-linear-gradient(30deg,transparent 0 20px,rgba(255,255,255,.1) 20px 21px), repeating-linear-gradient(-60deg,transparent 0 30px,rgba(0,0,0,.14) 30px 31px), linear-gradient(135deg,#065f46,#10b981,#a7f3d0,#064e3b);
}

.hv-19__swatch--rose {
  background: radial-gradient(circle at 30% 30%,#fef3c7 0%,#fbbf24 10%,transparent 22%), radial-gradient(circle at 70% 70%,#7c1d6f 0%,transparent 20%), repeating-linear-gradient(75deg,transparent 0 18px,rgba(255,255,255,.1) 18px 19px), repeating-linear-gradient(-15deg,transparent 0 26px,rgba(0,0,0,.12) 26px 27px), linear-gradient(135deg,#9f1239,#f43f5e,#fda4af,#881337);
}

.hv-19__swatch--teal {
  background: radial-gradient(circle at 35% 35%,#fef3c7 0%,transparent 15%), radial-gradient(circle at 70% 70%,#0c4a6e 0%,transparent 25%), repeating-linear-gradient(45deg,transparent 0 20px,rgba(255,255,255,.1) 20px 21px), repeating-linear-gradient(-45deg,transparent 0 30px,rgba(0,0,0,.14) 30px 31px), linear-gradient(135deg,#0f766e,#14b8a6,#99f6e4,#0d9488);
}
/* 1 — center zoom */

.hv-19__img--center:hover {
  transform: scale(1.12);
}
/* 2 — corner-pan */

.hv-19__img--pan:hover {
  transform: scale(1.18) translate(-5%,-5%);
}
/* 3 — slow drift */

.hv-19__img--drift {
  transition: transform 1.2s cubic-bezier(.4,0,.2,1);
}

.hv-19__img--drift:hover {
  transform: scale(1.1) translate(3%,2%);
}
/* 4 — zoom + brightness */

.hv-19__img--bright:hover {
  transform: scale(1.1);
  filter: brightness(1.25) saturate(1.2);
}
/* 5 — clip-path crop zoom */

.hv-19__wrap--crop {
  overflow: visible;
}

.hv-19__img--crop {
  clip-path: inset(8% round 12px);
  transition: transform .6s cubic-bezier(.4,0,.2,1),clip-path .6s cubic-bezier(.4,0,.2,1);
}

.hv-19__img--crop:hover {
  transform: scale(1.08);
  clip-path: inset(0% round 12px);
}
/* 6 — zoom + rotate */

.hv-19__img--rotate:hover {
  transform: scale(1.15) rotate(3deg);
}

@media (max-width: 640px) {
  .hv-19__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 400px) {
  .hv-19__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-19__img {
    transition: none!important;
  }
}
```
