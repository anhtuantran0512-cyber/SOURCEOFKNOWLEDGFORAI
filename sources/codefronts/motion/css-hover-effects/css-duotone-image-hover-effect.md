---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-duotone-image-hover-effect/"
title: "CSS Duotone Image Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Four duotone image hover transitions — grayscale to full color restore, monochrome to brand duotone, hue rotation shift, and saturation fade-in — using CSS…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Duotone Image Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-duotone-image-hover-effect/

Four duotone image hover transitions — grayscale to full color restore, monochrome to brand duotone, hue rotation shift, and saturation fade-in — using CSS filter chains and pseudo-element blending to apply and remove two-tone color grades on hover.
## HTML
```html
<div class="hv-21">
  <div class="hv-21__grid">
    <div class="hv-21__cell">
      <div class="hv-21__wrap hv-21__wrap--restore">
        <div class="hv-21__img hv-21__swatch--a"></div>
      </div>
      <span class="hv-21__label">grayscale → color restore</span>
    </div>
    <div class="hv-21__cell">
      <div class="hv-21__wrap hv-21__wrap--duo">
        <div class="hv-21__img hv-21__swatch--b"></div>
        <div class="hv-21__duo-overlay"></div>
      </div>
      <span class="hv-21__label">duotone → natural</span>
    </div>
    <div class="hv-21__cell">
      <div class="hv-21__wrap hv-21__wrap--hue">
        <div class="hv-21__img hv-21__swatch--c"></div>
      </div>
      <span class="hv-21__label">hue-rotate grade</span>
    </div>
    <div class="hv-21__cell">
      <div class="hv-21__wrap hv-21__wrap--sat">
        <div class="hv-21__img hv-21__swatch--d"></div>
      </div>
      <span class="hv-21__label">desaturate fade-in</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-21,
.hv-21 *,
.hv-21 *::before,
.hv-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-21 ::selection {
  background: #9333ea;
  color: #fff;
}

.hv-21 {
  --bg: #080608;
  --dim: #6b7280;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-21__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 32px;
  max-width: 720px;
  width: 100%;
}

.hv-21__cell {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hv-21__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.hv-21__wrap {
  aspect-ratio: 16/9;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  position: relative;
  isolation: isolate;
}

.hv-21__img {
  width: 100%;
  height: 100%;
}
/* layered pseudo-images so duotone/grayscale/hue-rotate are visually meaningful */

.hv-21__swatch--a {
  background: radial-gradient(circle at 28% 32%,#fef9c3 0%,transparent 14%), radial-gradient(circle at 70% 65%,#dc2626 0%,transparent 22%), repeating-linear-gradient(45deg,transparent 0 16px,rgba(255,255,255,.08) 16px 17px), repeating-linear-gradient(-45deg,transparent 0 24px,rgba(0,0,0,.14) 24px 25px), linear-gradient(135deg,#1e3a5f,#2563eb,#7dd3fc,#1e40af);
}

.hv-21__swatch--b {
  background: radial-gradient(circle at 32% 30%,#fde047 0%,transparent 16%), radial-gradient(circle at 68% 68%,#10b981 0%,transparent 22%), repeating-linear-gradient(30deg,transparent 0 18px,rgba(255,255,255,.1) 18px 19px), repeating-linear-gradient(-60deg,transparent 0 28px,rgba(0,0,0,.14) 28px 29px), linear-gradient(135deg,#4a1942,#7c3aed,#ddd6fe,#6d28d9);
}

.hv-21__swatch--c {
  background: radial-gradient(circle at 25% 30%,#fef3c7 0%,transparent 15%), radial-gradient(circle at 72% 70%,#dc2626 0%,transparent 22%), repeating-linear-gradient(60deg,transparent 0 20px,rgba(255,255,255,.1) 20px 21px), repeating-linear-gradient(-30deg,transparent 0 30px,rgba(0,0,0,.14) 30px 31px), linear-gradient(135deg,#14532d,#16a34a,#bbf7d0,#15803d);
}

.hv-21__swatch--d {
  background: radial-gradient(circle at 30% 35%,#fef9c3 0%,transparent 14%), radial-gradient(circle at 70% 68%,#1e40af 0%,transparent 22%), repeating-linear-gradient(75deg,transparent 0 18px,rgba(255,255,255,.1) 18px 19px), repeating-linear-gradient(-15deg,transparent 0 28px,rgba(0,0,0,.14) 28px 29px), linear-gradient(135deg,#7c2d12,#ea580c,#fdba74,#c2410c);
}
/* 1 — grayscale restore */

.hv-21__wrap--restore .hv-21__img {
  filter: grayscale(1) contrast(1.1);
  transition: filter .5s cubic-bezier(.4,0,.2,1);
}

.hv-21__wrap--restore:hover .hv-21__img {
  filter: none;
}
/* 2 — duotone overlay fade */

.hv-21__duo-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,#1e003c,#ff6b00);
  mix-blend-mode: color;
  opacity: 1;
  transition: opacity .5s cubic-bezier(.4,0,.2,1);
}

.hv-21__wrap--duo .hv-21__img {
  filter: contrast(1.1);
}

.hv-21__wrap--duo:hover .hv-21__duo-overlay {
  opacity: 0;
}
/* 3 — hue rotate */

.hv-21__wrap--hue .hv-21__img {
  filter: hue-rotate(0deg) saturate(1);
  transition: filter .6s cubic-bezier(.4,0,.2,1);
}

.hv-21__wrap--hue:hover .hv-21__img {
  filter: hue-rotate(160deg) saturate(1.5);
}
/* 4 — desaturate reveal */

.hv-21__wrap--sat .hv-21__img {
  filter: grayscale(1);
  transition: filter .5s cubic-bezier(.4,0,.2,1);
}

.hv-21__wrap--sat:hover .hv-21__img {
  filter: grayscale(0) saturate(1.2);
}

@media (max-width: 520px) {
  .hv-21__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-21__img,
    .hv-21__duo-overlay {
    transition: none!important;
  }
}
```
