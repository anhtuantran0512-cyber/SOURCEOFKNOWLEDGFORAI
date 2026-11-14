---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-image-clip-path-transition-hover/"
title: "CSS Image Clip-Path Transition Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "Geometric shape morphing where images transition between circles, diamonds, and polygons via interpolated clip-path values on hover."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Clip-Path Transition Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-image-clip-path-transition-hover/

Geometric shape morphing where images transition between circles, diamonds, and polygons via interpolated clip-path values on hover.
## HTML
```html
<div class="ih-11">
  <div class="ih-11__grid">
    <div class="ih-11__item">
      <div class="ih-11__frame">
        <div class="ih-11__img ih-11__img--circle"><span class="ih-11__icon">🌕</span></div>
      </div>
      <div class="ih-11__labels">
        <p><span class="ih-11__shape-from">Circle</span><span class="ih-11__arrow">→</span><span class="ih-11__shape-to">Rounded Rect</span></p>
        <p class="ih-11__name">Orbital Shift</p>
      </div>
    </div>
    <div class="ih-11__item">
      <div class="ih-11__frame">
        <div class="ih-11__img ih-11__img--diamond"><span class="ih-11__icon">💎</span></div>
      </div>
      <div class="ih-11__labels">
        <p><span class="ih-11__shape-from">Diamond</span><span class="ih-11__arrow">→</span><span class="ih-11__shape-to">Circle</span></p>
        <p class="ih-11__name">Gem Reveal</p>
      </div>
    </div>
    <div class="ih-11__item">
      <div class="ih-11__frame">
        <div class="ih-11__img ih-11__img--hexagon"><span class="ih-11__icon">⬡</span></div>
      </div>
      <div class="ih-11__labels">
        <p><span class="ih-11__shape-from">Hex</span><span class="ih-11__arrow">→</span><span class="ih-11__shape-to">Wide Hex + Spin</span></p>
        <p class="ih-11__name">Lattice Morph</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-11,
.ih-11 *,
.ih-11 *::before,
.ih-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-11 ::selection {
  background: #e879f9;
  color: #000;
}

.ih-11 {
  --accent: #e879f9;
  --bg: #08080d;
  --text: #f1f5f9;
  --muted: #64748b;
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

.ih-11__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-11__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}
/* clip-path morphs the image shape on hover */

.ih-11__frame {
  width: 100%;
  aspect-ratio: 1;
  position: relative;
  overflow: visible;
}

.ih-11__img {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: clip-path var(--duration) var(--ease), transform var(--duration) var(--ease);
}
/* Starting shapes */

.ih-11__img--circle {
  clip-path: circle(42% at 50% 50%);
  background: radial-gradient(circle,#2d1b69,#4c1d95,#7c3aed);
}

.ih-11__img--diamond {
  clip-path: polygon(50% 0%,100% 50%,50% 100%,0% 50%);
  background: radial-gradient(circle,#042f2e,#065f46,#34d399);
}

.ih-11__img--hexagon {
  clip-path: polygon(50% 0%,100% 25%,100% 75%,50% 100%,0% 75%,0% 25%);
  background: radial-gradient(circle,#1c1917,#92400e,#f59e0b);
}
/* Hover shapes */

.ih-11__item:hover .ih-11__img--circle {
  clip-path: polygon(10% 0%,90% 0%,100% 10%,100% 90%,90% 100%,10% 100%,0% 90%,0% 10%);
  transform: scale(1.05);
}

.ih-11__item:hover .ih-11__img--diamond {
  clip-path: circle(48% at 50% 50%);
  transform: scale(1.05);
}

.ih-11__item:hover .ih-11__img--hexagon {
  clip-path: polygon(25% 0%,75% 0%,100% 50%,75% 100%,25% 100%,0% 50%);
  transform: scale(1.05) rotate(30deg);
}

.ih-11__icon {
  font-size: 44px;
  opacity: 0.5;
}
/* Shape label */

.ih-11__labels {
  text-align: center;
}

.ih-11__shape-from {
  font-size: 10px;
  color: var(--muted);
  letter-spacing: 0.08em;
}

.ih-11__arrow {
  color: var(--accent);
  margin: 0 4px;
}

.ih-11__shape-to {
  font-size: 10px;
  color: var(--accent);
  font-weight: 700;
}

.ih-11__name {
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ih-11__img {
    transition: none;
  }
}
```
