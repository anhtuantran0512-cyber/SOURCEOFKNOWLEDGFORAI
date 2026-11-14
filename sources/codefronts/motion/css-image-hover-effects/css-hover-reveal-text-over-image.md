---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-hover-reveal-text-over-image/"
title: "CSS Hover Reveal Text Over Image"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Portfolio-grid technique where a title and description fade and slide in over an image on mouseover via layered opacity and translateY transitions."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hover Reveal Text Over Image
Source: https://codefronts.com/motion/css-image-hover-effects/css-hover-reveal-text-over-image/

Portfolio-grid technique where a title and description fade and slide in over an image on mouseover via layered opacity and translateY transitions.
## HTML
```html
<div class="ih-02">
  <div class="ih-02__grid">
    <div class="ih-02__card">
      <div class="ih-02__img ih-02__img--1">
        <span class="ih-02__emoji">🌌</span>
      </div>
      <span class="ih-02__badge">Portfolio</span>
      <div class="ih-02__overlay">
        <p class="ih-02__tag">Astrophotography</p>
        <p class="ih-02__name">Nebula Series Vol. 3</p>
        <p class="ih-02__sub">Shot over 14 nights in the Chilean Atacama desert</p>
      </div>
    </div>
    <div class="ih-02__card">
      <div class="ih-02__img ih-02__img--2">
        <span class="ih-02__emoji">🏙️</span>
      </div>
      <span class="ih-02__badge">Architecture</span>
      <div class="ih-02__overlay">
        <p class="ih-02__tag">Urban Design</p>
        <p class="ih-02__name">Midnight Cityscapes</p>
        <p class="ih-02__sub">Long exposure study of downtown light trails</p>
      </div>
    </div>
    <div class="ih-02__card">
      <div class="ih-02__img ih-02__img--3">
        <span class="ih-02__emoji">🔮</span>
      </div>
      <span class="ih-02__badge">Abstract</span>
      <div class="ih-02__overlay">
        <p class="ih-02__tag">Digital Art</p>
        <p class="ih-02__name">Prism Light Study</p>
        <p class="ih-02__sub">Generative colour diffraction experiments</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-02,
.ih-02 *,
.ih-02 *::before,
.ih-02 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-02 ::selection {
  background: #06b6d4;
  color: #000;
}

.ih-02 {
  --accent: #06b6d4;
  --accent2: #a78bfa;
  --bg: #09090f;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --duration: 0.4s;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  font-family: 'Inter', system-ui, sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-02__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-02__card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 3/4;
  cursor: pointer;
}
/* Gradient placeholder images */

.ih-02__img {
  width: 100%;
  height: 100%;
  transition: transform var(--duration) var(--ease);
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-02__img--1 {
  background: linear-gradient(160deg,#0f0c29,#302b63,#24243e);
}

.ih-02__img--2 {
  background: linear-gradient(160deg,#0f2027,#203a43,#2c5364);
}

.ih-02__img--3 {
  background: linear-gradient(160deg,#1a0533,#4a044e,#2d1b69);
}

.ih-02__card:hover .ih-02__img {
  transform: scale(1.08);
}

.ih-02__emoji {
  font-size: 56px;
  opacity: 0.35;
  transition: opacity var(--duration) var(--ease);
}

.ih-02__card:hover .ih-02__emoji {
  opacity: 0.1;
}
/* The overlay fades in and text slides up */

.ih-02__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.3) 50%, transparent 100%);
  opacity: 0;
  transition: opacity var(--duration) var(--ease);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 20px 16px;
}

.ih-02__card:hover .ih-02__overlay {
  opacity: 1;
}

.ih-02__tag {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
  transform: translateY(12px);
  transition: transform var(--duration) var(--ease);
}

.ih-02__card:hover .ih-02__tag {
  transform: translateY(0);
}

.ih-02__name {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.3;
  transform: translateY(16px);
  transition: transform calc(var(--duration) * 1.1) var(--ease);
}

.ih-02__card:hover .ih-02__name {
  transform: translateY(0);
}

.ih-02__sub {
  font-size: 12px;
  color: var(--muted);
  margin-top: 4px;
  transform: translateY(20px);
  opacity: 0;
  transition: transform calc(var(--duration) * 1.2) var(--ease), opacity calc(var(--duration) * 1.2) var(--ease);
}

.ih-02__card:hover .ih-02__sub {
  transform: translateY(0);
  opacity: 1;
}
/* Static label when not hovered (accessibility) */

.ih-02__badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 6px;
  padding: 4px 8px;
  font-size: 10px;
  color: var(--muted);
  font-weight: 600;
  letter-spacing: 0.05em;
}

@media (prefers-reduced-motion: reduce) {
  .ih-02__img,
    .ih-02__overlay,
    .ih-02__tag,
    .ih-02__name,
    .ih-02__sub,
    .ih-02__emoji {
    transition: none;
  }

  .ih-02__overlay {
    opacity: 1;
  }

  .ih-02__tag,
    .ih-02__name,
    .ih-02__sub {
    transform: none;
    opacity: 1;
  }
}
```
