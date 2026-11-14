---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-split-transition-hover/"
title: "CSS Image Split Transition Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Avant-garde hover where an image slices horizontally into two moving segments, revealing an action strip in the gap via clip-path."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Split Transition Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-split-transition-hover/

Avant-garde hover where an image slices horizontally into two moving segments, revealing an action strip in the gap via clip-path.
## HTML
```html
<div class="ih-14">
  <div class="ih-14__grid">
    <div class="ih-14__card">
      <div class="ih-14__half ih-14__half--top ih-14__half--1"><span class="ih-14__icon">🎨</span></div>
      <div class="ih-14__half ih-14__half--bot ih-14__half--1"><span class="ih-14__icon">🎨</span></div>
      <span class="ih-14__num">01</span>
      <div class="ih-14__reveal">
        <p class="ih-14__rev-title">Digital Canvas</p>
        <span class="ih-14__rev-cta">View</span>
      </div>
    </div>
    <div class="ih-14__card">
      <div class="ih-14__half ih-14__half--top ih-14__half--2"><span class="ih-14__icon">🌱</span></div>
      <div class="ih-14__half ih-14__half--bot ih-14__half--2"><span class="ih-14__icon">🌱</span></div>
      <span class="ih-14__num">02</span>
      <div class="ih-14__reveal">
        <p class="ih-14__rev-title">Growth Series</p>
        <span class="ih-14__rev-cta">View</span>
      </div>
    </div>
    <div class="ih-14__card">
      <div class="ih-14__half ih-14__half--top ih-14__half--3"><span class="ih-14__icon">⚡</span></div>
      <div class="ih-14__half ih-14__half--bot ih-14__half--3"><span class="ih-14__icon">⚡</span></div>
      <span class="ih-14__num">03</span>
      <div class="ih-14__reveal">
        <p class="ih-14__rev-title">Power Study</p>
        <span class="ih-14__rev-cta">View</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-14,
.ih-14 *,
.ih-14 *::before,
.ih-14 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-14 ::selection {
  background: #fb7185;
  color: #000;
}

.ih-14 {
  --accent: #fb7185;
  --accent2: #38bdf8;
  --bg: #070710;
  --text: #f1f5f9;
  --muted: #475569;
  --duration: 0.5s;
  --ease: cubic-bezier(0.34,1.56,0.64,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-14__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-14__card {
  position: relative;
  aspect-ratio: 3/4;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
}
/* Each card is split into two halves using clip-path */

.ih-14__half {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration) var(--ease), clip-path var(--duration) var(--ease);
  will-change: transform;
}
/* Top half */

.ih-14__half--top {
  clip-path: polygon(0 0,100% 0,100% 50%,0 50%);
}
/* Bottom half */

.ih-14__half--bot {
  clip-path: polygon(0 50%,100% 50%,100% 100%,0 100%);
}
/* On hover: halves slide apart */

.ih-14__card:hover .ih-14__half--top {
  transform: translateY(-6%);
}

.ih-14__card:hover .ih-14__half--bot {
  transform: translateY(6%);
}

.ih-14__half--1 {
  background: linear-gradient(135deg,#1a0533,#4c1d95,#7c3aed);
}

.ih-14__half--2 {
  background: linear-gradient(135deg,#042f2e,#065f46,#10b981);
}

.ih-14__half--3 {
  background: linear-gradient(135deg,#1c1003,#92400e,#f59e0b);
}

.ih-14__icon {
  font-size: 52px;
  opacity: 0.4;
  transition: opacity var(--duration) var(--ease);
}

.ih-14__card:hover .ih-14__icon {
  opacity: 0.1;
}
/* Revealed content in the gap */

.ih-14__reveal {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  padding: 12px 16px;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: space-between;
  opacity: 0;
  clip-path: inset(100% 0 100% 0);
  transition: opacity var(--duration) var(--ease), clip-path var(--duration) var(--ease);
}

.ih-14__card:hover .ih-14__reveal {
  opacity: 1;
  clip-path: inset(0 0 0 0);
}

.ih-14__rev-title {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
}

.ih-14__rev-cta {
  font-size: 10px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 20px;
  background: var(--accent);
  color: #fff;
}
/* Static badge */

.ih-14__num {
  position: absolute;
  top: 12px;
  left: 12px;
  font-size: 22px;
  font-weight: 900;
  color: rgba(255,255,255,0.12);
  line-height: 1;
}

@media (prefers-reduced-motion: reduce) {
  .ih-14__half,
    .ih-14__icon,
    .ih-14__reveal {
    transition: none;
  }

  .ih-14__reveal {
    opacity: 1;
    clip-path: inset(0);
  }

  .ih-14__half--top {
    transform: none;
  }

  .ih-14__half--bot {
    transform: none;
  }
}
```
