---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/prismatic-sweep/"
title: "Prismatic Sweep"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "An optics/art card where a soft rainbow light bar sweeps diagonally across the surface in screen blend mode, like light refracting through glass."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Prismatic Sweep
Source: https://codefronts.com/motion/css-card-hover-effects/prismatic-sweep/

An optics/art card where a soft rainbow light bar sweeps diagonally across the surface in screen blend mode, like light refracting through glass. Ideal for art installations, science, premium tech, and visually rich landing cards.
## HTML
```html
<div class="card-31">
  <article class="card-31__card">
    <div class="card-31__sweep"></div>
    <div class="card-31__lines"></div>
    <div class="card-31__inner">
      <span class="card-31__eyebrow">Optics Lab</span>
      <h2 class="card-31__title">Refraction<br>No. 9</h2>
      <p class="card-31__desc">A coated-glass installation. Light enters white and leaves as a spectrum sweeping the wall.</p>
      <div class="card-31__meta">
        <span><b>540nm</b>peak</span>
        <span><b>1.52</b>index</span>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Geist+Mono:wght@400;500&display=swap');

.card-31,
.card-31 *,
.card-31 *::before,
.card-31 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-31 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #06060c;
  font-family: 'Sora', sans-serif;
  padding: 2rem;
}

.card-31__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 20px;
  cursor: pointer;
  overflow: hidden;
  background: linear-gradient(160deg, #14141f, #0a0a12);
  border: 1px solid rgba(255,255,255,0.07);
}

.card-31__sweep {
  position: absolute;
  top: -60%;
  left: -120%;
  width: 60%;
  height: 220%;
  z-index: 1;
  transform: rotate(22deg);
  background: linear-gradient(
      90deg,
      transparent,
      rgba(255,0,128,0.5),
      rgba(255,200,0,0.5),
      rgba(0,255,170,0.5),
      rgba(0,170,255,0.5),
      rgba(180,80,255,0.5),
      transparent
    );
  filter: blur(8px);
  mix-blend-mode: screen;
  transition: left 0.7s cubic-bezier(0.4,0,0.2,1);
}

.card-31__card:hover .card-31__sweep {
  left: 160%;
}

.card-31__lines {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: repeating-linear-gradient(
      115deg,
      transparent 0 40px,
      rgba(255,255,255,0.015) 40px 41px
    );
}

.card-31__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #eef0f7;
}

.card-31__eyebrow {
  font-family: 'Geist Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #8b8fa6;
}

.card-31__title {
  font-weight: 800;
  font-size: 2.5rem;
  line-height: 1;
}

.card-31__desc {
  font-size: 0.86rem;
  line-height: 1.6;
  color: #a3a7bd;
}

.card-31__meta {
  display: flex;
  gap: 1.4rem;
  font-family: 'Geist Mono', monospace;
  font-size: 0.74rem;
  color: #7c8197;
}

.card-31__meta span b {
  display: block;
  color: #eef0f7;
  font-size: 1.1rem;
}

@media (prefers-reduced-motion: reduce) {
  .card-31__sweep {
    transition: none !important;
  }
}
```
