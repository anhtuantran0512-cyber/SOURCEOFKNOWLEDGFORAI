---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-card-slide-up-caption-on-hover/"
title: "CSS Card Slide Up Caption on Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "A caption panel anchored at the bottom that slides up into view from below the image frame, revealing metadata and a category pill."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Card Slide Up Caption on Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-card-slide-up-caption-on-hover/

A caption panel anchored at the bottom that slides up into view from below the image frame, revealing metadata and a category pill.
## HTML
```html
<div class="ih-05">
  <div class="ih-05__grid">
    <div class="ih-05__card">
      <div class="ih-05__img ih-05__img--1"><span class="ih-05__icon">🎵</span></div>
      <div class="ih-05__caption">
        <div class="ih-05__peek"><span class="ih-05__dot"></span>Synthwave</div>
        <p class="ih-05__title">Neon Highways</p>
        <p class="ih-05__meta">A 12-track journey through retro-futuristic soundscapes and pulsing basslines</p>
        <span class="ih-05__pill">New Album</span>
      </div>
    </div>
    <div class="ih-05__card">
      <div class="ih-05__img ih-05__img--2"><span class="ih-05__icon">🌊</span></div>
      <div class="ih-05__caption">
        <div class="ih-05__peek"><span class="ih-05__dot"></span>Ambient</div>
        <p class="ih-05__title">Ocean Mind</p>
        <p class="ih-05__meta">Meditative binaural compositions recorded at the Faroe Islands coastline</p>
        <span class="ih-05__pill">EP Release</span>
      </div>
    </div>
    <div class="ih-05__card">
      <div class="ih-05__img ih-05__img--3"><span class="ih-05__icon">🔮</span></div>
      <div class="ih-05__caption">
        <div class="ih-05__peek"><span class="ih-05__dot"></span>Electronic</div>
        <p class="ih-05__title">Violet Frequencies</p>
        <p class="ih-05__meta">Experimental club music blending modular synthesis and jazz improvisation</p>
        <span class="ih-05__pill">Single</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-05,
.ih-05 *,
.ih-05 *::before,
.ih-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-05 ::selection {
  background: #f472b6;
  color: #000;
}

.ih-05 {
  --accent: #f472b6;
  --accent2: #818cf8;
  --bg: #0a0a10;
  --card: #141420;
  --text: #f1f5f9;
  --muted: #64748b;
  --duration: 0.4s;
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-05__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-05__card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  aspect-ratio: 4/5;
  cursor: pointer;
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.05);
}

.ih-05__img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease);
}

.ih-05__img--1 {
  background: linear-gradient(150deg,#0d0d1a 0%,#1e1b4b 60%,#312e81 100%);
}

.ih-05__img--2 {
  background: linear-gradient(150deg,#042f2e 0%,#0f766e 60%,#2dd4bf 100%);
}

.ih-05__img--3 {
  background: linear-gradient(150deg,#1a0626 0%,#6b21a8 60%,#c084fc 100%);
}

.ih-05__card:hover .ih-05__img {
  transform: scale(1.06) translateY(-4px);
}

.ih-05__icon {
  font-size: 56px;
  opacity: 0.35;
  transition: opacity var(--duration) var(--ease);
}

.ih-05__card:hover .ih-05__icon {
  opacity: 0.12;
}
/* The caption panel slides up from the bottom */

.ih-05__caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.7) 60%, transparent 100%);
  padding: 40px 16px 16px;
  transform: translateY(calc(100% - 44px));
  transition: transform var(--duration) var(--ease);
}

.ih-05__card:hover .ih-05__caption {
  transform: translateY(0);
}

.ih-05__peek {
  font-size: 12px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.ih-05__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--accent);
  flex-shrink: 0;
}

.ih-05__title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.ih-05__meta {
  font-size: 11px;
  color: var(--muted);
  line-height: 1.5;
}

.ih-05__pill {
  display: inline-block;
  margin-top: 8px;
  padding: 3px 8px;
  border-radius: 20px;
  background: rgba(244,114,182,0.15);
  border: 1px solid rgba(244,114,182,0.3);
  font-size: 10px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.06em;
}

@media (prefers-reduced-motion: reduce) {
  .ih-05__img,
    .ih-05__icon,
    .ih-05__caption {
    transition: none;
  }

  .ih-05__caption {
    transform: none;
  }
}
```
