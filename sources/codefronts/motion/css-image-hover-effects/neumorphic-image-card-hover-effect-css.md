---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/neumorphic-image-card-hover-effect-css/"
title: "Neumorphic Image Card Hover Effect CSS"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Soft-UI cards that shift from an extruded dual-shadow state to an inset \"pressed\" shadow on hover, mimicking tactile depth."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Image Card Hover Effect CSS
Source: https://codefronts.com/motion/css-image-hover-effects/neumorphic-image-card-hover-effect-css/

Soft-UI cards that shift from an extruded dual-shadow state to an inset "pressed" shadow on hover, mimicking tactile depth.
## HTML
```html
<div class="ih-08">
  <div class="ih-08__grid">
    <div class="ih-08__card">
      <div class="ih-08__img-frame">
        <div class="ih-08__img ih-08__img--1"><span class="ih-08__icon">🎮</span></div>
      </div>
      <div class="ih-08__body">
        <p class="ih-08__title">Phantom Controller</p>
        <p class="ih-08__sub">Haptic · Wireless · 40h</p>
        <div class="ih-08__foot">
          <span class="ih-08__price">$89</span>
          <button class="ih-08__btn">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="ih-08__card">
      <div class="ih-08__img-frame">
        <div class="ih-08__img ih-08__img--2"><span class="ih-08__icon">🎧</span></div>
      </div>
      <div class="ih-08__body">
        <p class="ih-08__title">AquaTone Studio</p>
        <p class="ih-08__sub">ANC · Hi-Res · 60h</p>
        <div class="ih-08__foot">
          <span class="ih-08__price">$229</span>
          <button class="ih-08__btn">Add to Cart</button>
        </div>
      </div>
    </div>
    <div class="ih-08__card">
      <div class="ih-08__img-frame">
        <div class="ih-08__img ih-08__img--3"><span class="ih-08__icon">💻</span></div>
      </div>
      <div class="ih-08__body">
        <p class="ih-08__title">NovaPad Ultra</p>
        <p class="ih-08__sub">OLED · 12-core · 18h</p>
        <div class="ih-08__foot">
          <span class="ih-08__price">$1,299</span>
          <button class="ih-08__btn">Add to Cart</button>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-08,
.ih-08 *,
.ih-08 *::before,
.ih-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-08 ::selection {
  background: #6366f1;
  color: #fff;
}

.ih-08 {
  --nm-bg: #1e1e2a;
  --nm-light: rgba(255,255,255,0.05);
  --nm-dark: rgba(0,0,0,0.45);
  --accent: #6366f1;
  --accent2: #22d3ee;
  --text: #e2e8f0;
  --muted: #64748b;
  --duration: 0.4s;
  --ease: cubic-bezier(0.25,0.46,0.45,0.94);
  font-family: system-ui,sans-serif;
  background: var(--nm-bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-08__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 24px;
  max-width: 780px;
  width: 100%;
}
/* Neumorphic base: dual shadow (light top-left, dark bottom-right) */

.ih-08__card {
  background: var(--nm-bg);
  border-radius: 20px;
  padding: 12px;
  cursor: pointer;
  box-shadow: 6px 6px 16px var(--nm-dark), -4px -4px 12px var(--nm-light);
  transition: box-shadow var(--duration) var(--ease), transform var(--duration) var(--ease);
}
/* Hover: inset shadow = pressed state */

.ih-08__card:hover {
  box-shadow: inset 4px 4px 10px var(--nm-dark), inset -3px -3px 8px var(--nm-light);
  transform: scale(0.98);
}

.ih-08__img-frame {
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 1;
  position: relative;
  box-shadow: inset 2px 2px 6px var(--nm-dark),inset -1px -1px 4px var(--nm-light);
}

.ih-08__img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease);
}

.ih-08__img--1 {
  background: linear-gradient(135deg,#1e1b4b,#312e81,#4338ca);
}

.ih-08__img--2 {
  background: linear-gradient(135deg,#0c4a6e,#075985,#38bdf8);
}

.ih-08__img--3 {
  background: linear-gradient(135deg,#3b0764,#6b21a8,#a855f7);
}

.ih-08__card:hover .ih-08__img {
  transform: scale(1.04);
}

.ih-08__icon {
  font-size: 48px;
  opacity: 0.45;
}

.ih-08__body {
  padding: 12px 4px 4px;
}

.ih-08__title {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 3px;
}

.ih-08__sub {
  font-size: 11px;
  color: var(--muted);
}

.ih-08__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 10px;
}

.ih-08__price {
  font-size: 15px;
  font-weight: 700;
  color: var(--accent);
}
/* Neumorphic pill button */

.ih-08__btn {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 10px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 0.06em;
  background: var(--nm-bg);
  box-shadow: 3px 3px 8px var(--nm-dark), -2px -2px 6px var(--nm-light);
  transition: box-shadow 0.2s ease;
  border: none;
  cursor: pointer;
}

.ih-08__btn:hover {
  box-shadow: inset 2px 2px 6px var(--nm-dark),inset -1px -1px 4px var(--nm-light);
}

@media (prefers-reduced-motion: reduce) {
  .ih-08__card,
    .ih-08__img {
    transition: none;
  }
}
```
