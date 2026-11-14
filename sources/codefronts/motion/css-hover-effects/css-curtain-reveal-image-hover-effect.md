---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-curtain-reveal-image-hover-effect/"
title: "CSS Curtain Reveal Image Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Five theatrical curtain-style hover reveals — split curtain open, top-to-bottom drop, blind slats slide, venetian blind open, and radial iris expand — all…"
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Curtain Reveal Image Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-curtain-reveal-image-hover-effect/

Five theatrical curtain-style hover reveals — split curtain open, top-to-bottom drop, blind slats slide, venetian blind open, and radial iris expand — all using clip-path polygon and inset transitions to theatrically reveal hidden image content on hover.
## HTML
```html
<div class="hv-22">
  <div class="hv-22__grid">
    <div class="hv-22__cell">
      <div class="hv-22__wrap hv-22__wrap--split">
        <div class="hv-22__reveal hv-22__swatch--a">
          <span class="hv-22__tag">OPEN</span>
        </div>
      </div>
      <span class="hv-22__label">split curtain</span>
    </div>
    <div class="hv-22__cell">
      <div class="hv-22__wrap hv-22__wrap--drop">
        <div class="hv-22__reveal hv-22__swatch--b">
          <span class="hv-22__tag">DROP</span>
        </div>
        <div class="hv-22__curtain-drop"></div>
      </div>
      <span class="hv-22__label">curtain drop</span>
    </div>
    <div class="hv-22__cell">
      <div class="hv-22__wrap hv-22__wrap--iris">
        <div class="hv-22__reveal hv-22__swatch--c">
          <span class="hv-22__tag">IRIS</span>
        </div>
        <div class="hv-22__iris-mask"></div>
      </div>
      <span class="hv-22__label">iris expand</span>
    </div>
    <div class="hv-22__cell">
      <div class="hv-22__wrap hv-22__wrap--slat">
        <div class="hv-22__reveal hv-22__swatch--d">
          <span class="hv-22__tag">BLIND</span>
        </div>
        <div class="hv-22__slat hv-22__slat--1"></div>
        <div class="hv-22__slat hv-22__slat--2"></div>
        <div class="hv-22__slat hv-22__slat--3"></div>
        <div class="hv-22__slat hv-22__slat--4"></div>
        <div class="hv-22__slat hv-22__slat--5"></div>
      </div>
      <span class="hv-22__label">venetian blind</span>
    </div>
  </div>
</div>
```
## CSS
```css
.hv-22,
.hv-22 *,
.hv-22 *::before,
.hv-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-22 ::selection {
  background: #be185d;
  color: #fff;
}

.hv-22 {
  --bg: #08040c;
  --dim: #6b7280;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
}

.hv-22__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 32px;
  max-width: 720px;
  width: 100%;
}

.hv-22__cell {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hv-22__label {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.hv-22__wrap {
  aspect-ratio: 16/9;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.hv-22__reveal {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hv-22__tag {
  font-size: 1.4rem;
  font-weight: 900;
  letter-spacing: .15em;
  color: #fff;
  opacity: .8;
}
/* swatches */

.hv-22__swatch--a {
  background: linear-gradient(135deg,#0f172a,#1e40af,#3b82f6);
}

.hv-22__swatch--b {
  background: linear-gradient(135deg,#0f172a,#7c3aed,#c084fc);
}

.hv-22__swatch--c {
  background: linear-gradient(135deg,#0f172a,#0f766e,#2dd4bf);
}

.hv-22__swatch--d {
  background: linear-gradient(135deg,#0f172a,#be185d,#f9a8d4);
}
/* 1 — split curtain */

.hv-22__wrap--split::before,
.hv-22__wrap--split::after {
  content: '';
  position: absolute;
  top: 0;
  width: 50%;
  height: 100%;
  background: #1a0a2e;
  z-index: 2;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.hv-22__wrap--split::before {
  left: 0;
}

.hv-22__wrap--split::after {
  right: 0;
}

.hv-22__wrap--split:hover::before {
  transform: translateX(-100%);
}

.hv-22__wrap--split:hover::after {
  transform: translateX(100%);
}
/* 2 — curtain drop */

.hv-22__curtain-drop {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #1a002a;
  transform: scaleY(1);
  transform-origin: top;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
}

.hv-22__wrap--drop:hover .hv-22__curtain-drop {
  transform: scaleY(0);
}
/* 3 — iris expand */

.hv-22__iris-mask {
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #0a001a;
  clip-path: polygon(0 0,100% 0,100% 100%,0 100%,0 0,50% 50%);
  transition: clip-path .5s cubic-bezier(.4,0,.2,1);
}

.hv-22__wrap--iris .hv-22__iris-mask {
  clip-path: circle(75% at 50% 50%);
  background: transparent;
  border: none;
}
/* re-approach: solid overlay with clip-path shrinking to reveal */

.hv-22__wrap--iris::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 2;
  background: #0a001a;
  clip-path: polygon(
      0 0,50% 0,50% 0,50% 0,50% 100%,50% 100%,50% 100%,0 100%,
      0 0,100% 0,100% 50%,100% 50%,100% 50%,100% 100%,50% 100%
    );
  transition: clip-path .5s cubic-bezier(.4,0,.2,1),opacity .5s;
  opacity: 1;
}

.hv-22__iris-mask {
  display: none;
}

.hv-22__wrap--iris::after {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 1;
}
/* simpler iris via circle clip-path on a dark overlay */

.hv-22__wrap--iris::before {
  clip-path: circle(76% at 50% 50%);
  background: transparent;
  box-shadow: 0 0 0 200px #0a001a;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  transform: translate(-50%,-50%);
  clip-path: none;
  transition: box-shadow .5s cubic-bezier(.4,0,.2,1);
}

.hv-22__wrap--iris:hover::before {
  box-shadow: 0 0 0 0 #0a001a;
}
/* 4 — venetian blind slats */

.hv-22__slat {
  position: absolute;
  left: 0;
  width: 100%;
  height: 20%;
  background: #1a0014;
  z-index: 2;
  transform: scaleY(1);
  transform-origin: top;
  transition: transform .3s cubic-bezier(.4,0,.2,1);
}

.hv-22__slat--1 {
  top: 0%;
  transition-delay: 0s;
}

.hv-22__slat--2 {
  top: 20%;
  transition-delay: .05s;
}

.hv-22__slat--3 {
  top: 40%;
  transition-delay: .1s;
}

.hv-22__slat--4 {
  top: 60%;
  transition-delay: .15s;
}

.hv-22__slat--5 {
  top: 80%;
  transition-delay: .2s;
}

.hv-22__wrap--slat:hover .hv-22__slat {
  transform: scaleY(0);
}

@media (max-width: 520px) {
  .hv-22__grid {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-22__wrap::before,
    .hv-22__wrap::after,
    .hv-22__curtain-drop,
    .hv-22__slat {
    transition: none!important;
  }
}
```
