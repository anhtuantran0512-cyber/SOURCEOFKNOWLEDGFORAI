---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/holographic-shimmer/"
title: "Holographic Shimmer"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A collectible trading-card treatment with a color-dodge foil sweep, sparkle grain, and a subtle 3D tilt, mimicking light catching a holographic surface."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic Shimmer
Source: https://codefronts.com/motion/css-card-hover-effects/holographic-shimmer/

A collectible trading-card treatment with a color-dodge foil sweep, sparkle grain, and a subtle 3D tilt, mimicking light catching a holographic surface. Perfect for NFT/collectible, gaming, or limited-edition product cards that need a "rare item" feel.
## HTML
```html
<div class="card-10">
  <article class="card-10__card">
    <div class="card-10__foil"></div>
    <div class="card-10__grain"></div>
    <div class="card-10__inner">
      <span class="card-10__rank">// MYTHIC · 001/250</span>
      <div class="card-10__emblem"></div>
      <div>
        <h2 class="card-10__title">Prism Warden</h2>
        <p class="card-10__desc">A foil-stamped collector card that catches light across the full spectrum.</p>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800&family=Rajdhani:wght@400;600&display=swap');

.card-10,
.card-10 *,
.card-10 *::before,
.card-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-10 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0a0a12;
  font-family: 'Rajdhani', sans-serif;
  padding: 2rem;
  perspective: 1200px;
}

.card-10__card {
  position: relative;
  width: 320px;
  height: 450px;
  border-radius: 18px;
  background: linear-gradient(135deg, #14142a, #0c0c1a);
  cursor: pointer;
  overflow: hidden;
  transform-style: preserve-3d;
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  box-shadow: 0 12px 30px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.08);
}

.card-10__card:hover {
  transform: rotateX(6deg) rotateY(-6deg);
  box-shadow: 0 30px 60px rgba(120, 80, 255, 0.3);
}

.card-10__foil {
  position: absolute;
  inset: 0;
  background: linear-gradient(
      115deg,
      transparent 20%,
      rgba(255, 0, 200, 0.35) 35%,
      rgba(0, 255, 220, 0.35) 45%,
      rgba(255, 230, 0, 0.35) 55%,
      transparent 70%
    );
  background-size: 250% 250%;
  background-position: 0% 0%;
  mix-blend-mode: color-dodge;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.card-10__card:hover .card-10__foil {
  opacity: 1;
  animation: card-10-sweep 2.5s linear infinite;
}

@keyframes card-10-sweep {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 200% 200%;
  }
}

.card-10__grain {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.4) 0.5px, transparent 0.6px);
  background-size: 7px 7px;
  opacity: 0;
  mix-blend-mode: overlay;
  transition: opacity 0.4s ease;
}

.card-10__card:hover .card-10__grain {
  opacity: 0.5;
}

.card-10__inner {
  position: relative;
  z-index: 3;
  height: 100%;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e6e9ff;
  transform: translateZ(40px);
}

.card-10__rank {
  font-family: 'Orbitron', sans-serif;
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  color: #6cf;
}

.card-10__emblem {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: conic-gradient(#ff00c8, #00ffdc, #ffe600, #ff00c8);
  margin: 0 auto;
  filter: blur(0.5px);
  box-shadow: 0 0 30px rgba(120, 80, 255, 0.5);
}

.card-10__title {
  font-family: 'Orbitron', sans-serif;
  font-weight: 800;
  font-size: 1.7rem;
  text-align: center;
  letter-spacing: 0.05em;
}

.card-10__desc {
  font-size: 0.95rem;
  line-height: 1.4;
  color: #aab;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .card-10__foil {
    animation: none !important;
  }
}
```
