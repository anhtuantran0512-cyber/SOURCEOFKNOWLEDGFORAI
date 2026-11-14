---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-grayscale-to-color-image-hover/"
title: "CSS Grayscale to Color Image Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Team-bio technique where images start in desaturated grayscale and animate to full colour with a slight saturation boost on hover."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grayscale to Color Image Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-grayscale-to-color-image-hover/

Team-bio technique where images start in desaturated grayscale and animate to full colour with a slight saturation boost on hover.
## HTML
```html
<div class="ih-06">
  <div class="ih-06__grid">
    <div class="ih-06__card">
      <div class="ih-06__img ih-06__img--1"><span class="ih-06__emoji">👩‍💻</span></div>
      <div class="ih-06__info">
        <p class="ih-06__name">Aria Chen</p>
        <p class="ih-06__role">Lead Engineer</p>
      </div>
    </div>
    <div class="ih-06__card">
      <div class="ih-06__img ih-06__img--2"><span class="ih-06__emoji">👨‍🎨</span></div>
      <div class="ih-06__info">
        <p class="ih-06__name">Marcus Webb</p>
        <p class="ih-06__role">Creative Director</p>
      </div>
    </div>
    <div class="ih-06__card">
      <div class="ih-06__img ih-06__img--3"><span class="ih-06__emoji">👩‍🔬</span></div>
      <div class="ih-06__info">
        <p class="ih-06__name">Priya Nair</p>
        <p class="ih-06__role">Research Scientist</p>
      </div>
    </div>
    <div class="ih-06__card">
      <div class="ih-06__img ih-06__img--4"><span class="ih-06__emoji">👨‍💼</span></div>
      <div class="ih-06__info">
        <p class="ih-06__name">Leo Santos</p>
        <p class="ih-06__role">Product Strategist</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-06,
.ih-06 *,
.ih-06 *::before,
.ih-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-06 ::selection {
  background: #22d3ee;
  color: #000;
}

.ih-06 {
  --accent: #22d3ee;
  --bg: #09090f;
  --text: #f1f5f9;
  --muted: #475569;
  --duration: 0.55s;
  --ease: cubic-bezier(0.25,0.46,0.45,0.94);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-06__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 14px;
  max-width: 780px;
  width: 100%;
}

.ih-06__card {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  aspect-ratio: 3/4;
}
/* filter:grayscale() + saturate() is the key technique — hardware accelerated */

.ih-06__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  filter: grayscale(1) brightness(0.75) saturate(0);
  transition: filter var(--duration) var(--ease), transform var(--duration) var(--ease);
}

.ih-06__card:hover .ih-06__img {
  filter: grayscale(0) brightness(1) saturate(1.2);
  transform: scale(1.04);
}

.ih-06__img--1 {
  background: linear-gradient(135deg,#1e3a5f,#1e40af,#3b82f6,#93c5fd);
}

.ih-06__img--2 {
  background: linear-gradient(135deg,#431407,#9a3412,#ef4444,#fca5a5);
}

.ih-06__img--3 {
  background: linear-gradient(135deg,#064e3b,#065f46,#10b981,#6ee7b7);
}

.ih-06__img--4 {
  background: linear-gradient(135deg,#3b0764,#7e22ce,#a855f7,#e9d5ff);
}

.ih-06__emoji {
  font-size: 52px;
  opacity: 0.6;
  filter: grayscale(1);
  transition: filter var(--duration) var(--ease);
}

.ih-06__card:hover .ih-06__emoji {
  filter: grayscale(0);
}

.ih-06__info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 12px;
  background: linear-gradient(to top,rgba(0,0,0,0.8),transparent);
}

.ih-06__name {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
}

.ih-06__role {
  font-size: 10px;
  color: var(--muted);
  margin-top: 2px;
  transition: color var(--duration) var(--ease);
}

.ih-06__card:hover .ih-06__role {
  color: var(--accent);
}
/* Coloured border reveal on hover */

.ih-06__card::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 10px;
  border: 2px solid transparent;
  transition: border-color var(--duration) var(--ease);
  pointer-events: none;
}

.ih-06__card:hover::after {
  border-color: rgba(34,211,238,0.4);
}

@media (prefers-reduced-motion: reduce) {
  .ih-06__img,
    .ih-06__emoji,
    .ih-06__role,
    .ih-06__card::after {
    transition: none;
  }

  .ih-06__img {
    filter: none;
  }
}
```
