---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/glassmorphism-overlay-on-image-hover/"
title: "Glassmorphism Overlay on Image Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "A frosted-glass descriptive card slides up from below the image frame on hover, using backdrop-filter for the blurred panel effect."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Overlay on Image Hover
Source: https://codefronts.com/motion/css-image-hover-effects/glassmorphism-overlay-on-image-hover/

A frosted-glass descriptive card slides up from below the image frame on hover, using backdrop-filter for the blurred panel effect.
## HTML
```html
<div class="ih-09">
  <div class="ih-09__grid">
    <div class="ih-09__card">
      <div class="ih-09__bg ih-09__bg--1"><span class="ih-09__icon">🌸</span></div>
      <div class="ih-09__static"><p class="ih-09__static-name">Spring Collection</p></div>
      <div class="ih-09__glass">
        <p class="ih-09__glass-label">Collection</p>
        <p class="ih-09__glass-title">Spring Bloom 2025</p>
        <p class="ih-09__glass-desc">Ethereal violet pieces inspired by cherry blossom season</p>
        <div class="ih-09__glass-footer">
          <span class="ih-09__glass-stat">24 pieces</span>
          <span class="ih-09__glass-cta">Explore →</span>
        </div>
      </div>
    </div>
    <div class="ih-09__card">
      <div class="ih-09__bg ih-09__bg--2"><span class="ih-09__icon">🍃</span></div>
      <div class="ih-09__static"><p class="ih-09__static-name">Earth Tones</p></div>
      <div class="ih-09__glass">
        <p class="ih-09__glass-label">Sustainable</p>
        <p class="ih-09__glass-title">Forest Origins</p>
        <p class="ih-09__glass-desc">Organic cotton pieces dyed with natural plant extracts</p>
        <div class="ih-09__glass-footer">
          <span class="ih-09__glass-stat">18 pieces</span>
          <span class="ih-09__glass-cta">Explore →</span>
        </div>
      </div>
    </div>
    <div class="ih-09__card">
      <div class="ih-09__bg ih-09__bg--3"><span class="ih-09__icon">🌊</span></div>
      <div class="ih-09__static"><p class="ih-09__static-name">Azure Line</p></div>
      <div class="ih-09__glass">
        <p class="ih-09__glass-label">Limited</p>
        <p class="ih-09__glass-title">Azure Coast</p>
        <p class="ih-09__glass-desc">Mediterranean-inspired linen pieces for summer living</p>
        <div class="ih-09__glass-footer">
          <span class="ih-09__glass-stat">12 pieces</span>
          <span class="ih-09__glass-cta">Explore →</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-09,
.ih-09 *,
.ih-09 *::before,
.ih-09 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-09 ::selection {
  background: rgba(139,92,246,0.8);
  color: #fff;
}

.ih-09 {
  --accent: #8b5cf6;
  --accent2: #34d399;
  --bg: #060611;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --duration: 0.45s;
  --ease: cubic-bezier(0.16,1,0.3,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-09__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-09__card {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  aspect-ratio: 3/4;
  cursor: pointer;
}

.ih-09__bg {
  position: absolute;
  inset: 0;
  transition: transform var(--duration) var(--ease);
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-09__bg--1 {
  background: linear-gradient(145deg,#1a0a2e,#2d1b69,#4c1d95,#7c3aed);
}

.ih-09__bg--2 {
  background: linear-gradient(145deg,#022c22,#065f46,#059669,#34d399);
}

.ih-09__bg--3 {
  background: linear-gradient(145deg,#0c1445,#1e3a8a,#1d4ed8,#60a5fa);
}

.ih-09__card:hover .ih-09__bg {
  transform: scale(1.08);
}

.ih-09__icon {
  font-size: 60px;
  opacity: 0.3;
  transition: opacity var(--duration) var(--ease);
}

.ih-09__card:hover .ih-09__icon {
  opacity: 0.08;
}
/* The glass card: backdrop-filter applies to everything behind it in the stacking context */

.ih-09__glass {
  position: absolute;
  left: 12px;
  right: 12px;
  bottom: 12px;
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(12px) saturate(1.5);
  -webkit-backdrop-filter: blur(12px) saturate(1.5);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  padding: 16px;
  transform: translateY(calc(100% + 16px));
  opacity: 0;
  transition: transform var(--duration) var(--ease), opacity var(--duration) var(--ease);
}

.ih-09__card:hover .ih-09__glass {
  transform: translateY(0);
  opacity: 1;
}

.ih-09__glass-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.ih-09__glass-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.ih-09__glass-desc {
  font-size: 11px;
  color: rgba(241,245,249,0.7);
  line-height: 1.5;
}

.ih-09__glass-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 10px;
}

.ih-09__glass-stat {
  font-size: 10px;
  color: var(--muted);
}

.ih-09__glass-cta {
  font-size: 10px;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.06em;
}
/* Static bottom gradient so card has content even before hover */

.ih-09__static {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 16px;
  background: linear-gradient(to top,rgba(0,0,0,0.7) 0%,transparent 100%);
}

.ih-09__static-name {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  transition: opacity var(--duration) var(--ease);
}

.ih-09__card:hover .ih-09__static-name {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .ih-09__bg,
    .ih-09__icon,
    .ih-09__glass,
    .ih-09__static-name {
    transition: none;
  }

  .ih-09__glass {
    transform: none;
    opacity: 1;
  }
}
```
