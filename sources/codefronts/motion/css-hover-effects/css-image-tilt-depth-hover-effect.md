---
source: "codefronts"
url: "https://codefronts.com/motion/css-hover-effects/css-image-tilt-depth-hover-effect/"
title: "CSS Image Tilt Depth Hover Effect"
section: "motion"
category: "css-hover-effects"
category_name: "CSS Hover Effects"
description: "Cards that tilt in 3-D perspective with floating depth layers and dynamic drop-shadows, entirely in CSS."
has_js: "false"
---

Here's a working CSS Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Image Tilt Depth Hover Effect
Source: https://codefronts.com/motion/css-hover-effects/css-image-tilt-depth-hover-effect/

Cards that tilt in 3-D perspective with floating depth layers and dynamic drop-shadows, entirely in CSS.
## HTML
```html
<div class="hv-24">
  <p class="hv-24__label">Image Tilt Depth — 4 Variants</p>
  <div class="hv-24__grid">

    <div class="hv-24__card hv-24__card--portrait">
      <div class="hv-24__inner">
        <img class="hv-24__img" src="https://picsum.photos/seed/tilt1/300/400" alt="" />
        <div class="hv-24__shine"></div>
        <div class="hv-24__caption">Portrait Tilt</div>
      </div>
    </div>

    <div class="hv-24__card hv-24__card--landscape">
      <div class="hv-24__inner">
        <img class="hv-24__img" src="https://picsum.photos/seed/tilt2/400/260" alt="" />
        <div class="hv-24__shine"></div>
        <div class="hv-24__caption">Landscape Tilt</div>
      </div>
    </div>

    <div class="hv-24__card hv-24__card--deep">
      <div class="hv-24__inner">
        <img class="hv-24__img" src="https://picsum.photos/seed/tilt3/300/400" alt="" />
        <div class="hv-24__shine"></div>
        <div class="hv-24__caption">Deep Perspective</div>
      </div>
    </div>

    <div class="hv-24__card hv-24__card--flat">
      <div class="hv-24__inner">
        <img class="hv-24__img" src="https://picsum.photos/seed/tilt4/400/260" alt="" />
        <div class="hv-24__shine"></div>
        <div class="hv-24__caption">Flat Hover Lift</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.hv-24,
.hv-24 *,
.hv-24 *::before,
.hv-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.hv-24 {
  font-family: system-ui, sans-serif;
  background: #0e0e12;
  padding: 2.5rem 2rem;
  min-height: 100vh;
}

.hv-24__label {
  text-align: center;
  color: #666;
  font-size: .75rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.hv-24__grid {
  display: grid;
  grid-template-columns: repeat(2, auto);
  gap: 2.5rem;
  justify-content: center;
  align-items: start;
}
/* ── Card shell — holds perspective ── */

.hv-24__card {
  perspective: 700px;
  cursor: pointer;
}
/* ── Inner — rotates in 3-D ── */

.hv-24__inner {
  position: relative;
  border-radius: 12px;
  transform-style: preserve-3d;
  transition: transform .45s cubic-bezier(.23,1,.32,1), box-shadow .45s cubic-bezier(.23,1,.32,1);
  box-shadow: 0 8px 30px rgba(0,0,0,.55);
  overflow: hidden;
  /* clip image but we accept safari caveat */
}

.hv-24__card--portrait .hv-24__inner {
  width: 220px;
  aspect-ratio: 3/4;
}

.hv-24__card--landscape .hv-24__inner {
  width: 320px;
  aspect-ratio: 16/9;
}

.hv-24__card--deep .hv-24__inner {
  width: 220px;
  aspect-ratio: 3/4;
}

.hv-24__card--flat .hv-24__inner {
  width: 320px;
  aspect-ratio: 16/9;
}
/* per-variant tilt angles */

.hv-24__card--portrait:hover .hv-24__inner {
  transform: rotateY(12deg) rotateX(-6deg);
  box-shadow: -14px 18px 50px rgba(0,0,0,.7);
}

.hv-24__card--landscape:hover .hv-24__inner {
  transform: rotateX(10deg) rotateY(-5deg);
  box-shadow: 0 -14px 40px rgba(0,0,0,.6);
}

.hv-24__card--deep:hover .hv-24__inner {
  transform: rotateY(-16deg) rotateX(8deg);
  box-shadow: 20px 14px 60px rgba(0,0,0,.8);
}

.hv-24__card--flat:hover .hv-24__inner {
  transform: rotateX(5deg) rotateY(5deg) translateZ(12px);
  box-shadow: -8px 20px 50px rgba(0,0,0,.65);
}

.hv-24__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
/* ── Specular shine overlay ── */

.hv-24__shine {
  position: absolute;
  inset: 0;
  background: conic-gradient(from 135deg at 50% 0%,
      rgba(255,255,255,.18) 0deg,
      transparent 80deg);
  opacity: 0;
  transition: opacity .4s;
  pointer-events: none;
  border-radius: inherit;
}

.hv-24__card:hover .hv-24__shine {
  opacity: 1;
}
/* ── Caption ── */

.hv-24__caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: .65rem .9rem;
  background: linear-gradient(transparent, rgba(0,0,0,.75));
  color: #fff;
  font-size: .78rem;
  letter-spacing: .06em;
  transform: translateY(4px);
  opacity: 0;
  transition: opacity .35s, transform .35s;
  pointer-events: none;
}

.hv-24__card:hover .hv-24__caption {
  opacity: 1;
  transform: translateY(0);
}

@media (max-width: 560px) {
  .hv-24__grid {
    grid-template-columns: 1fr;
  }

  .hv-24__card--portrait .hv-24__inner,
    .hv-24__card--deep .hv-24__inner {
    width: 100%;
  }

  .hv-24__card--landscape .hv-24__inner,
    .hv-24__card--flat .hv-24__inner {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hv-24__inner {
    transition: none !important;
  }

  .hv-24__shine,
    .hv-24__caption {
    transition: none !important;
  }
}
```
