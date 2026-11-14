---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-color-overlay-tint-on-hover/"
title: "CSS Image Color Overlay Tint on Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Brand-tint hover where a per-card accent colour washes over a neutral image using mix-blend-mode to preserve the underlying texture."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Color Overlay Tint on Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-color-overlay-tint-on-hover/

Brand-tint hover where a per-card accent colour washes over a neutral image using mix-blend-mode to preserve the underlying texture.
## HTML
```html
<div class="ih-07">
  <div class="ih-07__grid">
    <div class="ih-07__card">
      <div class="ih-07__img ih-07__img--1"><span class="ih-07__icon">🏗️</span></div>
      <div class="ih-07__tint"></div>
      <span class="ih-07__corner-tag">Brand A</span>
      <div class="ih-07__label"><p class="ih-07__name">Ember Orange Tint</p></div>
    </div>
    <div class="ih-07__card">
      <div class="ih-07__img ih-07__img--2"><span class="ih-07__icon">💡</span></div>
      <div class="ih-07__tint"></div>
      <span class="ih-07__corner-tag">Brand B</span>
      <div class="ih-07__label"><p class="ih-07__name">Pacific Blue Tint</p></div>
    </div>
    <div class="ih-07__card">
      <div class="ih-07__img ih-07__img--3"><span class="ih-07__icon">🔮</span></div>
      <div class="ih-07__tint"></div>
      <span class="ih-07__corner-tag">Brand C</span>
      <div class="ih-07__label"><p class="ih-07__name">Deep Violet Tint</p></div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-07,
.ih-07 *,
.ih-07 *::before,
.ih-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-07 ::selection {
  background: #f97316;
  color: #000;
}

.ih-07 {
  --bg: #0d0d0f;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --duration: 0.38s;
  --ease: cubic-bezier(0.25,0.46,0.45,0.94);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-07__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-07__card {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  aspect-ratio: 1;
  cursor: pointer;
}

.ih-07__img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease);
}

.ih-07__img--1 {
  background-image: url('https://picsum.photos/seed/landscape-orange/600/600'), linear-gradient(135deg,#111827,#1f2937,#374151);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-07__img--2 {
  background-image: url('https://picsum.photos/seed/landscape-blue/600/600'), linear-gradient(135deg,#0c0c0c,#1c1c1e,#2c2c2e);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-07__img--3 {
  background-image: url('https://picsum.photos/seed/landscape-violet/600/600'), linear-gradient(135deg,#0f0f14,#1a1a24,#252535);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.ih-07__card:hover .ih-07__img {
  transform: scale(1.06);
}

.ih-07__icon {
  font-size: 56px;
  opacity: 0.5;
  transition: opacity var(--duration) var(--ease);
}

.ih-07__card:hover .ih-07__icon {
  opacity: 0.2;
}
/* The tint overlay uses a CSS custom property for the brand colour per card */

.ih-07__tint {
  position: absolute;
  inset: 0;
  background: var(--tint-color);
  opacity: 0;
  transition: opacity var(--duration) var(--ease);
  mix-blend-mode: color;
  /* blend mode keeps underlying texture visible */
}

.ih-07__card:hover .ih-07__tint {
  opacity: 0.7;
}
/* Dark overlay under the text (separate from tint so blend mode doesn't affect it) */

.ih-07__label {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.ih-07__name {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  opacity: 0;
  transform: scale(0.9);
  transition: opacity var(--duration) var(--ease),transform var(--duration) var(--ease);
}

.ih-07__card:hover .ih-07__name {
  opacity: 1;
  transform: none;
}

.ih-07__card:first-child {
  --tint-color: #f97316;
}
/* orange */

.ih-07__card:nth-child(2) {
  --tint-color: #3b82f6;
}
/* blue */

.ih-07__card:nth-child(3) {
  --tint-color: #8b5cf6;
}
/* violet */

.ih-07__corner-tag {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 6px;
  padding: 3px 8px;
  font-size: 10px;
  font-weight: 600;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .ih-07__img,
    .ih-07__tint,
    .ih-07__icon,
    .ih-07__name {
    transition: none;
  }

  .ih-07__tint {
    opacity: 0.5;
  }

  .ih-07__name {
    opacity: 1;
    transform: none;
  }
}
```
