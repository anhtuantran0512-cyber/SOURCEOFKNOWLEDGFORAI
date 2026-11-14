---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/spiral-tower/"
title: "Spiral Tower"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "Cards arranged in a continuously rotating 3D helix around a central axis; hover pauses the spin."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spiral Tower
Source: https://codefronts.com/components/css-stacked-cards/spiral-tower/

Cards arranged in a continuously rotating 3D helix around a central axis; hover pauses the spin. Hypnotic and bold. Perfect for hero showcases, featured collections, or attention-grabbing displays.
## HTML
```html
<div class="scd-36">
  <div class="scd-36__stage">
    <div class="scd-36__spiral">
      <div class="scd-36__card">01</div>
      <div class="scd-36__card">02</div>
      <div class="scd-36__card">03</div>
      <div class="scd-36__card">04</div>
      <div class="scd-36__card">05</div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Major+Mono+Display&family=Jost:wght@400;500&display=swap');

.scd-36,
.scd-36 *,
.scd-36 *::before,
.scd-36 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-36 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 50%,#1e0a2e,#080410);
  font-family: 'Jost', sans-serif;
}

.scd-36__stage {
  perspective: 1200px;
  width: 240px;
  height: 400px;
}

.scd-36__spiral {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  animation: scd-36-spin 14s linear infinite;
}

@keyframes scd-36-spin {
  to {
    transform: rotateY(360deg);
  }
}

.scd-36__stage:hover .scd-36__spiral {
  animation-play-state: paused;
}

.scd-36__card {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 120px;
  height: 160px;
  margin: -80px -60px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-family: 'Major Mono Display', monospace;
  font-size: 1.4rem;
  box-shadow: 0 0 30px rgba(180,100,255,.25);
}

.scd-36__card:nth-child(1) {
  transform: rotateY(0deg) translateZ(150px) translateY(-120px);
  background: linear-gradient(150deg,#ee0979,#ff6a00);
}

.scd-36__card:nth-child(2) {
  transform: rotateY(72deg) translateZ(150px) translateY(-60px);
  background: linear-gradient(150deg,#7f00ff,#e100ff);
}

.scd-36__card:nth-child(3) {
  transform: rotateY(144deg) translateZ(150px) translateY(0px);
  background: linear-gradient(150deg,#00c6ff,#0072ff);
}

.scd-36__card:nth-child(4) {
  transform: rotateY(216deg) translateZ(150px) translateY(60px);
  background: linear-gradient(150deg,#11998e,#38ef7d);
}

.scd-36__card:nth-child(5) {
  transform: rotateY(288deg) translateZ(150px) translateY(120px);
  background: linear-gradient(150deg,#f7971e,#ffd200);
  color: #623;
}

@media (prefers-reduced-motion: reduce) {
  .scd-36__spiral {
    animation: none !important;
    transition: none !important;
  }
}
```
