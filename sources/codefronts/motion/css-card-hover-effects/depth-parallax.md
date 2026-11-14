---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/depth-parallax/"
title: "Depth Parallax"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A landscape/travel card with stacked depth layers (mountains, sun, foreground hills) that shift independently as the cursor moves, creating real 3D depth."
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Depth Parallax
Source: https://codefronts.com/motion/css-card-hover-effects/depth-parallax/

A landscape/travel card with stacked depth layers (mountains, sun, foreground hills) that shift independently as the cursor moves, creating real 3D depth. Best for travel, outdoor, and immersive storytelling cards where motion conveys place.
## HTML
```html
<div class="card-15">
  <article class="card-15__card" data-card-15="root">
    <div class="card-15__layer card-15__far"  data-depth="8"></div>
    <div class="card-15__layer card-15__sun"  data-depth="16"><div class="card-15__orb"></div></div>
    <div class="card-15__layer card-15__near" data-depth="28"></div>
    <div class="card-15__content" data-depth="40">
      <span class="card-15__kicker">Field Notes</span>
      <h2 class="card-15__title">Valley of<br>Long Light</h2>
      <p class="card-15__desc">A guided dawn trek through layered ridgelines. Move your cursor to feel the depth.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],500;12..96,800&family=Inter+Tight:wght@400;600&display=swap');

.card-15,
.card-15 *,
.card-15 *::before,
.card-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-15 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0b1d2a;
  font-family: 'Inter Tight', sans-serif;
  padding: 2rem;
  perspective: 1000px;
}

.card-15__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 22px;
  cursor: pointer;
  overflow: hidden;
  transform-style: preserve-3d;
  transition: transform 0.2s ease-out, box-shadow 0.4s ease;
  background: linear-gradient(180deg, #2c6e8f 0%, #0b1d2a 100%);
  box-shadow: 0 20px 50px rgba(0,0,0,0.45);
}

.card-15__layer {
  position: absolute;
  inset: 0;
  transition: transform 0.2s ease-out;
  will-change: transform;
}

.card-15__far {
  background: radial-gradient(circle at 20% 70%, #1b4a63 0 28%, transparent 29%), radial-gradient(circle at 70% 75%, #1b4a63 0 32%, transparent 33%);
  opacity: 0.9;
}

.card-15__sun {
  display: grid;
  place-items: center;
}

.card-15__sun .card-15__orb {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  background: radial-gradient(circle, #ffd56b, #ff8c42);
  box-shadow: 0 0 60px rgba(255,170,80,0.6);
  margin-top: -60px;
}

.card-15__near {
  background: radial-gradient(ellipse 120% 60% at 30% 110%, #06222e 60%, transparent 61%), radial-gradient(ellipse 120% 50% at 80% 115%, #04161e 60%, transparent 61%);
}

.card-15__content {
  position: absolute;
  inset: 0;
  z-index: 5;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  color: #eaf4fa;
  transition: transform 0.2s ease-out;
}

.card-15__kicker {
  font-size: 0.72rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #ffd56b;
}

.card-15__title {
  font-family: 'Bricolage Grotesque', sans-serif;
  font-weight: 800;
  font-size: 2.6rem;
  line-height: 0.95;
  margin: 0.4rem 0 0.6rem;
}

.card-15__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #b9d0dd;
}

@media (prefers-reduced-motion: reduce) {
  .card-15__card,
    .card-15__layer,
    .card-15__content {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-15');
  if (!root) return;
  const card = root.querySelector('[data-card-15="root"]');
  if (!card) return;
  const layers = card.querySelectorAll('[data-depth]');
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = `rotateY(${x * 10}deg) rotateX(${-y * 10}deg)`;
    layers.forEach((l) => {
      const d = parseFloat(l.dataset.depth);
      l.style.transform = `translate(${-x * d}px, ${-y * d}px)`;
    });
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateY(0) rotateX(0)';
    layers.forEach((l) => (l.style.transform = 'translate(0,0)'));
  });
})();
```
