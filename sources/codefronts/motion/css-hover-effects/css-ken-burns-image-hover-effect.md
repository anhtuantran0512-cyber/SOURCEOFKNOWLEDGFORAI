---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-ken-burns-image-hover-effect/"
title: "CSS Ken Burns Image Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Documentary-style slow zoom and pan animations on images, triggered by hover — six directional Ken Burns presets."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Ken Burns Image Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-ken-burns-image-hover-effect/

Documentary-style slow zoom and pan animations on images, triggered by hover — six directional Ken Burns presets.
## HTML
```html
<div class="hv-23">
  <p class="hv-23__label">Ken Burns Hover — 6 Presets</p>
  <div class="hv-23__grid">

    <div class="hv-23__card hv-23__card--zoom-in">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb1/400/260" alt="zoom-in" />
      <span class="hv-23__tag">Zoom In</span>
    </div>

    <div class="hv-23__card hv-23__card--zoom-out">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb2/400/260" alt="zoom-out" />
      <span class="hv-23__tag">Zoom Out</span>
    </div>

    <div class="hv-23__card hv-23__card--pan-right">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb3/400/260" alt="pan right" />
      <span class="hv-23__tag">Pan Right</span>
    </div>

    <div class="hv-23__card hv-23__card--pan-left">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb4/400/260" alt="pan left" />
      <span class="hv-23__tag">Pan Left</span>
    </div>

    <div class="hv-23__card hv-23__card--drift-up">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb5/400/260" alt="drift up" />
      <span class="hv-23__tag">Drift Up</span>
    </div>

    <div class="hv-23__card hv-23__card--drift-diagonal">
      <img class="hv-23__img" src="https://picsum.photos/seed/kb6/400/260" alt="diagonal" />
      <span class="hv-23__tag">Diagonal</span>
    </div>

  </div>
</div>
```
## CSS
```css
.hv-23,
.hv-23 *,
.hv-23 *::before,
.hv-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-23 {
  --kb-duration: 6s;
  --kb-ease: cubic-bezier(.25,.46,.45,.94);
  font-family: system-ui, sans-serif;
  padding: 2rem;
  background: #0d0d0d;
  min-height: 100vh;
}

.hv-23__label {
  text-align: center;
  color: #888;
  font-size: .78rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-bottom: 2rem;
}

.hv-23__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
  max-width: 820px;
  margin: 0 auto;
}

.hv-23__card {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  cursor: pointer;
  aspect-ratio: 3/2;
  box-shadow: 0 4px 20px rgba(0,0,0,.5);
}

.hv-23__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  animation-duration: var(--kb-duration);
  animation-timing-function: var(--kb-ease);
  animation-fill-mode: both;
  animation-play-state: paused;
  will-change: transform;
}

.hv-23__card:hover .hv-23__img {
  animation-play-state: running;
}

.hv-23__tag {
  position: absolute;
  bottom: .6rem;
  left: .6rem;
  background: rgba(0,0,0,.65);
  color: #fff;
  font-size: .7rem;
  letter-spacing: .08em;
  padding: .25rem .55rem;
  border-radius: 4px;
  backdrop-filter: blur(4px);
  pointer-events: none;
}
/* ── Keyframes ── */

@keyframes hv-23-zoom-in {
  from {
    transform: scale(1) translate(0, 0);
  }

  to {
    transform: scale(1.18) translate(-2%, -2%);
  }
}

@keyframes hv-23-zoom-out {
  from {
    transform: scale(1.2) translate(-3%, -3%);
  }

  to {
    transform: scale(1) translate(0, 0);
  }
}

@keyframes hv-23-pan-right {
  from {
    transform: scale(1.14) translate(-5%, 0);
  }

  to {
    transform: scale(1.14) translate(5%, 0);
  }
}

@keyframes hv-23-pan-left {
  from {
    transform: scale(1.14) translate(5%, 0);
  }

  to {
    transform: scale(1.14) translate(-5%, 0);
  }
}

@keyframes hv-23-drift-up {
  from {
    transform: scale(1.14) translate(0, 5%);
  }

  to {
    transform: scale(1.14) translate(0, -5%);
  }
}

@keyframes hv-23-diagonal {
  from {
    transform: scale(1) translate(0, 0);
  }

  to {
    transform: scale(1.2) translate(-4%, -4%);
  }
}
/* ── Per-card assignments ── */

.hv-23__card--zoom-in .hv-23__img {
  animation-name: hv-23-zoom-in;
}

.hv-23__card--zoom-out .hv-23__img {
  animation-name: hv-23-zoom-out;
}

.hv-23__card--pan-right .hv-23__img {
  animation-name: hv-23-pan-right;
}

.hv-23__card--pan-left .hv-23__img {
  animation-name: hv-23-pan-left;
}

.hv-23__card--drift-up .hv-23__img {
  animation-name: hv-23-drift-up;
}

.hv-23__card--drift-diagonal .hv-23__img {
  animation-name: hv-23-diagonal;
}

@media (max-width: 600px) {
  .hv-23__grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-23__img {
    animation: none !important;
  }
}
```
