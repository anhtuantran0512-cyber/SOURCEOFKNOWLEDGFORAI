---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/quad-photo-split/"
title: "Quad Photo Split"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Photography portfolio quad split — charcoal frame with four photo accents (sage / clay / mustard / bone)."
has_js: "false"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Quad Photo Split
Source: https://codefronts.com/layouts/css-split-screen/quad-photo-split/

Photography portfolio quad split — charcoal frame with four photo accents (sage / clay / mustard / bone). Hover any tile to expand it; the others contract. CSS grid with :has() on the wrapper to drive the proportions.
## HTML
```html
<section class="ss-quad" aria-label="Photography portfolio quad">
  <article
    class="ss-quad-tile"
    tabindex="0"
    data-tile="1"
    style="--bg: linear-gradient(135deg, #7a8a6a 0%, #4a5a3a 100%)"
  >
    <span class="ss-quad-num">01</span>
    <h3>Field Notes</h3>
    <p>Coastal Oregon, autumn 2025</p>
  </article>
  <article
    class="ss-quad-tile"
    tabindex="0"
    data-tile="2"
    style="--bg: linear-gradient(135deg, #c45a3c 0%, #8a3818 100%)"
  >
    <span class="ss-quad-num">02</span>
    <h3>Clay Walls</h3>
    <p>Marrakech rooftops at noon</p>
  </article>
  <article
    class="ss-quad-tile"
    tabindex="0"
    data-tile="3"
    style="--bg: linear-gradient(135deg, #e8b04a 0%, #b8842a 100%)"
  >
    <span class="ss-quad-num">03</span>
    <h3>Yellow Hour</h3>
    <p>Tuscan vineyards in late September</p>
  </article>
  <article
    class="ss-quad-tile"
    tabindex="0"
    data-tile="4"
    style="--bg: linear-gradient(135deg, #e0d4c0 0%, #a89880 100%)"
  >
    <span class="ss-quad-num">04</span>
    <h3>Bone &amp; Stone</h3>
    <p>Atacama mineral landscapes</p>
  </article>
</section>
```
## CSS
```css
.ss-quad {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #1a1a1a;
  gap: 2px;
  border-radius: 0;
  overflow: hidden;
  border: 2px solid #1a1a1a;
}

.ss-quad-tile {
  position: relative;
  background: var(--bg);
  padding: 28px 28px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  color: #fff;
  cursor: pointer;
  transition: transform 0.32s ease, box-shadow 0.32s ease;
  isolation: isolate;
  overflow: hidden;
}

.ss-quad-tile::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, transparent 60%, rgba(0,0,0,0.4) 100%);
  pointer-events: none;
  z-index: -1;
}

.ss-quad-tile:hover,
.ss-quad-tile:focus-visible {
  transform: scale(1.02);
  z-index: 2;
  box-shadow: 0 14px 40px rgba(0,0,0,0.5);
  outline: none;
}

.ss-quad:has(.ss-quad-tile:hover) .ss-quad-tile:not(:hover),
.ss-quad:has(.ss-quad-tile:focus-visible) .ss-quad-tile:not(:focus-visible) {
  filter: grayscale(0.7) brightness(0.7);
}

.ss-quad-num {
  font-family: 'Courier New', monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.28em;
  color: rgba(255,255,255,0.6);
}

.ss-quad-tile h3 {
  margin: auto 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(24px, 3.5vw, 40px);
  font-weight: 500;
  line-height: 1;
  letter-spacing: -0.02em;
  font-style: italic;
}

.ss-quad-tile p {
  margin: 0;
  font-size: 13px;
  letter-spacing: 0.04em;
  opacity: 0.9;
}

@media (max-width: 720px) {
  .ss-quad {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4, 1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ss-quad-tile {
    transition: none;
  }
}
```
