---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/grain-texture/"
title: "Grain Texture"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A vintage film card where animated SVG noise grain breathes faster and stronger on hover over a sepia, vignetted frame."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grain Texture
Source: https://codefronts.com/motion/css-card-hover-effects/grain-texture/

A vintage film card where animated SVG noise grain breathes faster and stronger on hover over a sepia, vignetted frame. Suited to photography, film, archival, and any brand chasing an analog, celluloid mood.
## HTML
```html
<div class="card-26">
  <article class="card-26__card">
    <div class="card-26__overlay"></div>
    <div class="card-26__inner">
      <span class="card-26__meta">SUPER 8 · 1974</span>
      <h2 class="card-26__title">Golden<br>Hour Reel</h2>
      <p class="card-26__desc">A scanned film transfer. Hover and the grain breathes, like light running through celluloid.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant:wght@500;600&family=Fragment+Mono&display=swap');

.card-26,
.card-26 *,
.card-26 *::before,
.card-26 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-26 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #16130f;
  font-family: 'Fragment Mono', monospace;
  padding: 2rem;
}

.card-26__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 8px;
  cursor: pointer;
  overflow: hidden;
  background: linear-gradient(160deg, #3a2e22, #1b140d);
  box-shadow: 0 20px 45px rgba(0,0,0,0.5);
}

.card-26__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 35%, rgba(210,170,110,0.35), transparent 60%), linear-gradient(160deg, #5a4732, #241a10);
}

.card-26__overlay {
  position: absolute;
  inset: -50%;
  z-index: 2;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.12;
  mix-blend-mode: overlay;
  pointer-events: none;
  transition: opacity 0.5s ease;
  animation: card-26-move 0.6s steps(4) infinite;
}

.card-26__card:hover .card-26__overlay {
  opacity: 0.42;
  animation-duration: 0.25s;
}

@keyframes card-26-move {
  0% {
    transform: translate(0,0);
  }

  25% {
    transform: translate(-8%, 5%);
  }

  50% {
    transform: translate(6%, -8%);
  }

  75% {
    transform: translate(-5%, -4%);
  }

  100% {
    transform: translate(7%, 6%);
  }
}

.card-26__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 3;
  box-shadow: inset 0 0 90px rgba(0,0,0,0.7);
  pointer-events: none;
}

.card-26__inner {
  position: relative;
  z-index: 4;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f0e2cc;
}

.card-26__meta {
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  color: #c9a877;
}

.card-26__title {
  font-family: 'Cormorant', serif;
  font-weight: 600;
  font-size: 3rem;
  line-height: 0.95;
  font-style: italic;
}

.card-26__desc {
  font-size: 0.82rem;
  line-height: 1.65;
  color: #c4b39a;
}

@media (prefers-reduced-motion: reduce) {
  .card-26__overlay {
    animation: none !important;
  }
}
```
