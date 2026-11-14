---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/3d-tilt-parallax-card-effects/"
title: "3D Tilt & Parallax Card Effects"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A premium portfolio card that follows the cursor's orientation in real 3D, with the background, badge, title, and description each pushed onto separate…"
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Tilt & Parallax Card Effects
Source: https://codefronts.com/motion/css-card-hover-effects/3d-tilt-parallax-card-effects/

A premium portfolio card that follows the cursor's orientation in real 3D, with the background, badge, title, and description each pushed onto separate Z-axis depth planes so they shift at different rates as you move. A specular glare tracks the pointer across the surface, making the whole card feel like a physical, light-catching object — ideal for featured work, showcase grids, and hero web-app cards.
## HTML
```html
<div class="card-01">
  <article class="card-01__card" data-card-01="root">
    <div class="card-01__bg"      data-depth="10"></div>
    <span class="card-01__tag"    data-depth="34">Featured Work</span>
    <div class="card-01__emblem"  data-depth="46">◈</div>
    <h2 class="card-01__title"    data-depth="60">Aether<br>Studio</h2>
    <p class="card-01__desc"      data-depth="40">An award-winning interactive site. Background, type, and badge each ride their own depth plane.</p>
    <div class="card-01__glare"></div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,[email protected],500;9..144,900&family=Inter+Tight:wght@400;500;600&display=swap');

.card-01,
.card-01 *,
.card-01 *::before,
.card-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-01 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 30% 20%, #1f2347, #090a18 65%);
  font-family: 'Inter Tight', sans-serif;
  padding: 2rem;
  perspective: 1300px;
}

.card-01__card {
  position: relative;
  width: 340px;
  height: 460px;
  border-radius: 26px;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.15s ease-out, box-shadow 0.5s ease;
  box-shadow: 0 30px 60px rgba(0,0,0,0.5);
  background: #0e1024;
  border: 1px solid rgba(255,255,255,0.08);
}

.card-01__card > * {
  position: absolute;
  transition: transform 0.15s ease-out;
  will-change: transform;
}
/* split background — far layer */

.card-01__bg {
  inset: 0;
  border-radius: 26px;
  overflow: hidden;
  background: radial-gradient(circle at 30% 25%, #ff7a59 0 18%, transparent 19%), radial-gradient(circle at 75% 70%, #5b8cff 0 24%, transparent 25%), linear-gradient(160deg, #2a2f63, #11132c);
}

.card-01__bg::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 40%, transparent, rgba(9,10,24,0.6));
}
/* floating glare */

.card-01__glare {
  inset: 0;
  border-radius: 26px;
  background: radial-gradient(circle at var(--card-01-gx,50%) var(--card-01-gy,50%), rgba(255,255,255,0.22), transparent 45%);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 6;
  pointer-events: none;
}

.card-01__card:hover .card-01__glare {
  opacity: 1;
}

.card-01__tag {
  top: 2rem;
  left: 2rem;
  z-index: 5;
  font-size: 0.7rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #ffd6c4;
}

.card-01__emblem {
  top: 2rem;
  right: 2rem;
  z-index: 5;
  width: 46px;
  height: 46px;
  border-radius: 14px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.25);
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 700;
  backdrop-filter: blur(4px);
}

.card-01__title {
  left: 2rem;
  bottom: 5.4rem;
  z-index: 5;
  font-family: 'Fraunces', serif;
  font-weight: 900;
  font-size: 3rem;
  line-height: 0.9;
  color: #fff;
}

.card-01__desc {
  left: 2rem;
  right: 2rem;
  bottom: 2rem;
  z-index: 5;
  font-size: 0.85rem;
  line-height: 1.55;
  color: #c4c8e6;
}

@media (prefers-reduced-motion: reduce) {
  .card-01__card,
    .card-01__card > *,
    .card-01__glare {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-01');
  if (!root) return;
  const card = root.querySelector('[data-card-01="root"]');
  if (!card) return;
  const layers = card.querySelectorAll('[data-depth]');
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    card.style.transform =
      `rotateY(${(px - 0.5) * 18}deg) rotateX(${(0.5 - py) * 18}deg)`;
    layers.forEach((l) => {
      const d = parseFloat(l.dataset.depth);
      l.style.transform =
        `translateZ(${d}px) translate(${(0.5 - px) * d * 0.6}px, ${(0.5 - py) * d * 0.6}px)`;
    });
    card.style.setProperty('--card-01-gx', `${px * 100}%`);
    card.style.setProperty('--card-01-gy', `${py * 100}%`);
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateY(0) rotateX(0)';
    layers.forEach((l) => {
      const d = parseFloat(l.dataset.depth);
      l.style.transform = `translateZ(${d}px)`;
    });
  });
})();
```
