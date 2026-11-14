---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-icon-reveal-center-hover/"
title: "CSS Image Icon Reveal Center Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Thumbnail grid where the image darkens and an action icon (play, magnify, link) scales in at the exact centre on hover using transform origin."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Icon Reveal Center Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-icon-reveal-center-hover/

Thumbnail grid where the image darkens and an action icon (play, magnify, link) scales in at the exact centre on hover using transform origin.
## HTML
```html
<div class="ih-19">
  <div class="ih-19__grid">
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--1"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🎬</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">▶</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Intro Reel 2025</span><span class="ih-19__views">4.2k views</span></div>
    </div>
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--2"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🌿</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">🔍</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Jungle Macro</span><span class="ih-19__views">1.8k views</span></div>
    </div>
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--3"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🔮</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">🔗</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Prism Study</span><span class="ih-19__views">9.1k views</span></div>
    </div>
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--4"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🌅</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">▶</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Golden Hour BTS</span><span class="ih-19__views">3.3k views</span></div>
    </div>
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--5"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🌊</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">🔍</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Deep Blue Series</span><span class="ih-19__views">7.6k views</span></div>
    </div>
    <div class="ih-19__card">
      <div class="ih-19__img ih-19__img--6"></div>
      <div class="ih-19__img-content"><span class="ih-19__thumb">🌺</span></div>
      <div class="ih-19__icon-wrap"><div class="ih-19__icon-btn">🔗</div></div>
      <div class="ih-19__strip"><span class="ih-19__title">Bloom Editorial</span><span class="ih-19__views">2.9k views</span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-19,
.ih-19 *,
.ih-19 *::before,
.ih-19 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-19 ::selection {
  background: #818cf8;
  color: #fff;
}

.ih-19 {
  --accent: #818cf8;
  --bg: #07070e;
  --text: #f1f5f9;
  --muted: #475569;
  --duration: 0.38s;
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-19__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
  max-width: 780px;
  width: 100%;
}

.ih-19__card {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  aspect-ratio: 4/3;
  cursor: pointer;
}

.ih-19__img {
  position: absolute;
  inset: 0;
  transition: filter var(--duration) var(--ease),transform var(--duration) var(--ease);
}

.ih-19__img--1 {
  background: linear-gradient(135deg,#0f0c29,#312e81,#4338ca);
}

.ih-19__img--2 {
  background: linear-gradient(135deg,#042f2e,#065f46,#059669);
}

.ih-19__img--3 {
  background: linear-gradient(135deg,#3b0764,#7e22ce,#a855f7);
}

.ih-19__img--4 {
  background: linear-gradient(135deg,#1c1003,#92400e,#d97706);
}

.ih-19__img--5 {
  background: linear-gradient(135deg,#0c1445,#1e3a8a,#2563eb);
}

.ih-19__img--6 {
  background: linear-gradient(135deg,#1a0010,#9d174d,#e11d48);
}

.ih-19__card:hover .ih-19__img {
  filter: brightness(0.4);
  transform: scale(1.06);
}

.ih-19__img-content {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-19__thumb {
  font-size: 40px;
  opacity: 0.4;
  transition: opacity var(--duration) var(--ease), transform var(--duration) var(--ease);
}

.ih-19__card:hover .ih-19__thumb {
  opacity: 0;
  transform: scale(0.7);
}
/* The center icon — scales in from 0 */

.ih-19__icon-wrap {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transform: scale(0.5) rotate(-20deg);
  transition: opacity var(--duration) var(--ease), transform var(--duration) var(--ease);
}

.ih-19__card:hover .ih-19__icon-wrap {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}

.ih-19__icon-btn {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(255,255,255,0.12);
  border: 2px solid rgba(255,255,255,0.25);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  transition: background 0.2s ease, transform 0.2s ease;
}

.ih-19__card:hover .ih-19__icon-btn:hover {
  background: rgba(255,255,255,0.22);
  transform: scale(1.1);
}
/* Bottom strip */

.ih-19__strip {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 8px 10px;
  background: linear-gradient(to top,rgba(0,0,0,0.8),transparent);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ih-19__title {
  font-size: 11px;
  font-weight: 700;
  color: var(--text);
}

.ih-19__views {
  font-size: 10px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .ih-19__img,
    .ih-19__thumb,
    .ih-19__icon-wrap {
    transition: none;
  }

  .ih-19__icon-wrap {
    opacity: 1;
    transform: none;
  }
}
```
