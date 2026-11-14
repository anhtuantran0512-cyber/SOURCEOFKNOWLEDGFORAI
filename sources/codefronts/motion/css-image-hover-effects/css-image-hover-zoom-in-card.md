---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-hover-zoom-in-card/"
title: "CSS Image Hover Zoom In Card"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "The classic card micro-interaction where the image scales up inside its clipped container boundary without shifting the surrounding grid."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Hover Zoom In Card
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-hover-zoom-in-card/

The classic card micro-interaction where the image scales up inside its clipped container boundary without shifting the surrounding grid.
## HTML
```html
<div class="ih-01">
  <div class="ih-01__grid">
    <div class="ih-01__card">
      <div class="ih-01__img-wrap">
        <div class="ih-01__img ih-01__img--1">
          <div class="ih-01__img-inner"><span class="ih-01__img-icon">🔭</span></div>
        </div>
      </div>
      <div class="ih-01__body">
        <p class="ih-01__cat">Explore</p>
        <p class="ih-01__title">Deep Space Observatory</p>
        <p class="ih-01__meta">12 min read · Cosmos</p>
      </div>
    </div>
    <div class="ih-01__card">
      <div class="ih-01__img-wrap">
        <div class="ih-01__img ih-01__img--2">
          <div class="ih-01__img-inner"><span class="ih-01__img-icon">🌿</span></div>
        </div>
      </div>
      <div class="ih-01__body">
        <p class="ih-01__cat">Nature</p>
        <p class="ih-01__title">Ancient Forest Canopy</p>
        <p class="ih-01__meta">8 min read · Biology</p>
      </div>
    </div>
    <div class="ih-01__card">
      <div class="ih-01__img-wrap">
        <div class="ih-01__img ih-01__img--3">
          <div class="ih-01__img-inner"><span class="ih-01__img-icon">💎</span></div>
        </div>
      </div>
      <div class="ih-01__body">
        <p class="ih-01__cat">Design</p>
        <p class="ih-01__title">Crystal Formations</p>
        <p class="ih-01__meta">5 min read · Art</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-01,
.ih-01 *,
.ih-01 *::before,
.ih-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-01 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ih-01 {
  --accent: #7c3aed;
  --accent2: #06b6d4;
  --bg: #0f0f13;
  --card-bg: #1a1a24;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --radius: 16px;
  --zoom: 1.12;
  --duration: 0.45s;
  --ease: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  font-family: 'Inter', system-ui, sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-01__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}
/* The key trick: overflow:hidden on card clips the zooming image */

.ih-01__card {
  background: var(--card-bg);
  border-radius: var(--radius);
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.06);
  transition: box-shadow var(--duration) var(--ease), border-color var(--duration) var(--ease);
  cursor: pointer;
}

.ih-01__card:hover {
  box-shadow: 0 20px 60px rgba(124,58,237,0.25);
  border-color: rgba(124,58,237,0.35);
}

.ih-01__img-wrap {
  overflow: hidden;
  aspect-ratio: 4/3;
  position: relative;
}
/* The image itself scales — overflow:hidden on parent does the crop */

.ih-01__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration) var(--ease);
  display: block;
  background: linear-gradient(135deg, #1e1e2e, #2d1b69);
}

.ih-01__card:hover .ih-01__img {
  transform: scale(var(--zoom));
}
/* Decorative gradient placeholder images */

.ih-01__img--1 {
  background: linear-gradient(135deg, #1a0533 0%, #4c1d95 50%, #0891b2 100%);
}

.ih-01__img--2 {
  background: linear-gradient(135deg, #0c1a2e 0%, #1e3a5f 50%, #065f46 100%);
}

.ih-01__img--3 {
  background: linear-gradient(135deg, #1a0a1e 0%, #6b21a8 50%, #be185d 100%);
}

.ih-01__img-inner {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-01__img-icon {
  font-size: 48px;
  opacity: 0.4;
  transition: transform var(--duration) var(--ease), opacity var(--duration) var(--ease);
}

.ih-01__card:hover .ih-01__img-icon {
  transform: scale(0.88);
  opacity: 0.25;
}

.ih-01__body {
  padding: 16px;
}

.ih-01__cat {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 6px;
}

.ih-01__title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 4px;
}

.ih-01__meta {
  font-size: 12px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .ih-01__img,
    .ih-01__img-icon,
    .ih-01__card {
    transition: none;
  }
}
```
