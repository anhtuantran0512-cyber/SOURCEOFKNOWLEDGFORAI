---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-grid-image-blur-overlay-text-hover/"
title: "CSS Grid Image Blur Overlay Text Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Visually soft hover where the background image blurs under a dark overlay via backdrop-filter to make typography legible."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Image Blur Overlay Text Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-grid-image-blur-overlay-text-hover/

Visually soft hover where the background image blurs under a dark overlay via backdrop-filter to make typography legible.
## HTML
```html
<div class="ih-04">
  <div class="ih-04__grid">
    <div class="ih-04__card">
      <div class="ih-04__bg ih-04__bg--1"></div>
      <span class="ih-04__emoji">🌌</span>
      <div class="ih-04__overlay">
        <p class="ih-04__cat">Editorial</p>
        <p class="ih-04__title">The Infinite Canvas</p>
        <p class="ih-04__desc">Exploring the boundaries of digital art in 2025</p>
      </div>
    </div>
    <div class="ih-04__card">
      <div class="ih-04__bg ih-04__bg--2"></div>
      <span class="ih-04__emoji">🌿</span>
      <div class="ih-04__overlay">
        <p class="ih-04__cat">Nature</p>
        <p class="ih-04__title">Bioluminescent Depths</p>
        <p class="ih-04__desc">Life thriving in the ocean's twilight zone</p>
      </div>
    </div>
    <div class="ih-04__card">
      <div class="ih-04__bg ih-04__bg--3"></div>
      <span class="ih-04__emoji">✨</span>
      <div class="ih-04__overlay">
        <p class="ih-04__cat">Culture</p>
        <p class="ih-04__title">Neon Flux Collection</p>
        <p class="ih-04__desc">Street art meets future-forward design aesthetics</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-04,
.ih-04 *,
.ih-04 *::before,
.ih-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-04 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.ih-04 {
  --accent: #8b5cf6;
  --bg: #080810;
  --text: #f1f5f9;
  --muted: #94a3b8;
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

.ih-04__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-04__card {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  aspect-ratio: 3/4;
  cursor: pointer;
}

.ih-04__bg {
  position: absolute;
  inset: 0;
  transition: filter var(--duration) var(--ease), transform var(--duration) var(--ease);
}

.ih-04__bg--1 {
  background: linear-gradient(135deg,#0f0c29,#302b63,#24243e);
}

.ih-04__bg--2 {
  background: linear-gradient(135deg,#0a3d2e,#155e43,#6ee7b7);
}

.ih-04__bg--3 {
  background: linear-gradient(135deg,#1a0010,#6b1d4e,#e879f9);
}

.ih-04__emoji {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-60%);
  font-size: 60px;
  opacity: 0.35;
  transition: opacity var(--duration) var(--ease), transform var(--duration) var(--ease);
}
/* backdrop-filter blur on overlay — applied to the ::before pseudo so it blurs the sibling bg */

.ih-04__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0);
  /* We use backdrop-filter on the overlay itself */
  backdrop-filter: blur(0px) brightness(1);
  -webkit-backdrop-filter: blur(0px) brightness(1);
  transition: backdrop-filter var(--duration) var(--ease), -webkit-backdrop-filter var(--duration) var(--ease), background var(--duration) var(--ease);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 20px;
}

.ih-04__card:hover .ih-04__bg {
  transform: scale(1.05);
}

.ih-04__card:hover .ih-04__emoji {
  opacity: 0.08;
  transform: translate(-50%,-60%) scale(1.2);
}

.ih-04__card:hover .ih-04__overlay {
  backdrop-filter: blur(8px) brightness(0.6);
  -webkit-backdrop-filter: blur(8px) brightness(0.6);
  background: rgba(0,0,0,0.15);
}

.ih-04__cat {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity var(--duration) var(--ease), transform var(--duration) var(--ease);
}

.ih-04__title {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.3;
  opacity: 0;
  transform: translateY(12px);
  transition: opacity calc(var(--duration)*1.1) var(--ease), transform calc(var(--duration)*1.1) var(--ease);
}

.ih-04__desc {
  font-size: 11px;
  color: var(--muted);
  margin-top: 5px;
  opacity: 0;
  transform: translateY(14px);
  transition: opacity calc(var(--duration)*1.2) var(--ease), transform calc(var(--duration)*1.2) var(--ease);
}

.ih-04__card:hover .ih-04__cat,
.ih-04__card:hover .ih-04__title,
.ih-04__card:hover .ih-04__desc {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: reduce) {
  .ih-04__bg,
    .ih-04__overlay,
    .ih-04__cat,
    .ih-04__title,
    .ih-04__desc,
    .ih-04__emoji {
    transition: none;
  }

  .ih-04__overlay {
    backdrop-filter: blur(8px) brightness(0.6);
  }

  .ih-04__cat,
    .ih-04__title,
    .ih-04__desc {
    opacity: 1;
    transform: none;
  }
}
```
