---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-glowing-neon-border-image-hover/"
title: "CSS Glowing Neon Border Image Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Gaming-card style hover where vibrant box-shadow glows activate around the card border, driven by per-card CSS custom properties."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glowing Neon Border Image Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-glowing-neon-border-image-hover/

Gaming-card style hover where vibrant box-shadow glows activate around the card border, driven by per-card CSS custom properties.
## HTML
```html
<div class="ih-10">
  <div class="ih-10__grid">
    <div class="ih-10__card ih-10__card--1">
      <div class="ih-10__img ih-10__img--1"><span class="ih-10__icon">⚡</span></div>
      <div class="ih-10__body">
        <p class="ih-10__title">Cipher X9 GPU</p>
        <p class="ih-10__sub">24GB GDDR7 · Ray Tracing</p>
        <p class="ih-10__score">★ 98 / 100 Performance</p>
      </div>
    </div>
    <div class="ih-10__card ih-10__card--2">
      <div class="ih-10__img ih-10__img--2"><span class="ih-10__icon">🖥️</span></div>
      <div class="ih-10__body">
        <p class="ih-10__title">Horizon 4K OLED</p>
        <p class="ih-10__sub">240Hz · 1ms GTG · HDR</p>
        <p class="ih-10__score">★ 96 / 100 Visuals</p>
      </div>
    </div>
    <div class="ih-10__card ih-10__card--3">
      <div class="ih-10__img ih-10__img--3"><span class="ih-10__icon">⌨️</span></div>
      <div class="ih-10__body">
        <p class="ih-10__title">Spectra 75% MK</p>
        <p class="ih-10__sub">Optical · Per-key RGB</p>
        <p class="ih-10__score">★ 94 / 100 Feel</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-10,
.ih-10 *,
.ih-10 *::before,
.ih-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-10 ::selection {
  background: #f0abfc;
  color: #000;
}

.ih-10 {
  --c1: #f0abfc;
  --c2: #22d3ee;
  --c3: #86efac;
  --bg: #030308;
  --text: #f1f5f9;
  --muted: #64748b;
  --duration: 0.4s;
  --ease: cubic-bezier(0.25,0.46,0.45,0.94);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-10__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}
/* The glow uses box-shadow — much cheaper than drop-shadow on GPU */

.ih-10__card {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,0.06);
  transition: box-shadow var(--duration) var(--ease), border-color var(--duration) var(--ease);
}

.ih-10__card--1:hover {
  box-shadow: 0 0 0 1px var(--c1),0 0 20px var(--c1),0 0 60px rgba(240,171,252,0.25);
  border-color: var(--c1);
}

.ih-10__card--2:hover {
  box-shadow: 0 0 0 1px var(--c2),0 0 20px var(--c2),0 0 60px rgba(34,211,238,0.25);
  border-color: var(--c2);
}

.ih-10__card--3:hover {
  box-shadow: 0 0 0 1px var(--c3),0 0 20px var(--c3),0 0 60px rgba(134,239,172,0.25);
  border-color: var(--c3);
}

.ih-10__img {
  aspect-ratio: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease);
}

.ih-10__img--1 {
  background: linear-gradient(135deg,#150824,#3b0764,#6b21a8);
}

.ih-10__img--2 {
  background: linear-gradient(135deg,#041e2b,#0c4a6e,#0369a1);
}

.ih-10__img--3 {
  background: linear-gradient(135deg,#052013,#064e3b,#065f46);
}

.ih-10__card:hover .ih-10__img {
  transform: scale(1.04);
}
/* Animated corner accents */

.ih-10__img::before,
.ih-10__img::after {
  content: '';
  position: absolute;
  width: 16px;
  height: 16px;
  opacity: 0;
  transition: opacity var(--duration) var(--ease);
}

.ih-10__img::before {
  top: 8px;
  left: 8px;
  border-top: 2px solid currentColor;
  border-left: 2px solid currentColor;
}

.ih-10__img::after {
  bottom: 8px;
  right: 8px;
  border-bottom: 2px solid currentColor;
  border-right: 2px solid currentColor;
}

.ih-10__card--1 .ih-10__img {
  color: var(--c1);
}

.ih-10__card--2 .ih-10__img {
  color: var(--c2);
}

.ih-10__card--3 .ih-10__img {
  color: var(--c3);
}

.ih-10__card:hover .ih-10__img::before,
.ih-10__card:hover .ih-10__img::after {
  opacity: 1;
}

.ih-10__icon {
  font-size: 52px;
  opacity: 0.4;
  transition: opacity var(--duration) var(--ease);
}

.ih-10__card:hover .ih-10__icon {
  opacity: 0.2;
}

.ih-10__body {
  padding: 14px 16px;
  background: rgba(0,0,0,0.3);
}

.ih-10__title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
}

.ih-10__sub {
  font-size: 11px;
  color: var(--muted);
  margin-top: 3px;
}

.ih-10__score {
  font-size: 12px;
  font-weight: 800;
  margin-top: 8px;
  background: linear-gradient(90deg,var(--c1),var(--c2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.ih-10__card--2 .ih-10__score {
  background: linear-gradient(90deg,var(--c2),var(--c3));
  -webkit-background-clip: text;
  background-clip: text;
}

.ih-10__card--3 .ih-10__score {
  background: linear-gradient(90deg,var(--c3),var(--c1));
  -webkit-background-clip: text;
  background-clip: text;
}

@media (prefers-reduced-motion: reduce) {
  .ih-10__card,
    .ih-10__img,
    .ih-10__icon,
    .ih-10__img::before,
    .ih-10__img::after {
    transition: none;
  }
}
```
