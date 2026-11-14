---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/3d-tilt/"
title: "3D Tilt"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A product card that tilts in 3D toward the cursor with a moving specular glare and layered depth on the text, using translateZ for true parallax."
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Tilt
Source: https://codefronts.com/motion/css-card-hover-effects/3d-tilt/

A product card that tilts in 3D toward the cursor with a moving specular glare and layered depth on the text, using translateZ for true parallax. Perfect for sneaker drops, gadgets, and hero product features that reward close inspection.
## HTML
```html
<div class="card-17">
  <article class="card-17__card" data-card-17="root">
    <div class="card-17__glare"></div>
    <div class="card-17__inner">
      <span class="card-17__chip">Limited Drop</span>
      <h2 class="card-17__title">Nimbus<br>Hi-Tops</h2>
      <p class="card-17__desc">Float-foam midsole and an iridescent upper that shifts as it turns in the light.</p>
      <span class="card-17__price">$189</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Clash+Display:wght@600;700&family=Space+Grotesk:wght@400;500&display=swap');

@import url('https://fonts.cdnfonts.com/css/clash-display');

.card-17,
.card-17 *,
.card-17 *::before,
.card-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-17 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 70% 30%, #2a1f4d, #0d0a1a 70%);
  font-family: 'Space Grotesk', sans-serif;
  padding: 2rem;
  perspective: 1100px;
}

.card-17__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 24px;
  cursor: pointer;
  transform-style: preserve-3d;
  transition: transform 0.12s ease-out, box-shadow 0.4s ease;
  background: linear-gradient(150deg, #3a2b6e, #18122e);
  box-shadow: 0 25px 50px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.08);
}

.card-17__glare {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(
      circle at var(--card-17-gx, 50%) var(--card-17-gy, 50%),
      rgba(255,255,255,0.28),
      transparent 45%
    );
  opacity: 0;
  transition: opacity 0.3s ease;
  pointer-events: none;
  z-index: 5;
}

.card-17__card:hover .card-17__glare {
  opacity: 1;
}

.card-17__inner {
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #ede9ff;
  transform: translateZ(0);
}

.card-17__chip {
  align-self: flex-start;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 0.4rem 0.9rem;
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 999px;
  transform: translateZ(60px);
  color: #c5b8ff;
}

.card-17__title {
  font-family: 'Clash Display', 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 2.8rem;
  line-height: 0.95;
  transform: translateZ(80px);
}

.card-17__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #b3a9d6;
  transform: translateZ(40px);
}

.card-17__price {
  font-family: 'Clash Display', 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 1.6rem;
  transform: translateZ(70px);
  color: #9d7bff;
}

@media (prefers-reduced-motion: reduce) {
  .card-17__card,
    .card-17__glare {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-17');
  if (!root) return;
  const c = root.querySelector('[data-card-17="root"]');
  if (!c) return;
  c.addEventListener('mousemove', (e) => {
    const r = c.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    c.style.transform = `rotateY(${(px - 0.5) * 20}deg) rotateX(${(0.5 - py) * 20}deg)`;
    c.style.setProperty('--card-17-gx', `${px * 100}%`);
    c.style.setProperty('--card-17-gy', `${py * 100}%`);
  });
  c.addEventListener('mouseleave', () => {
    c.style.transform = 'rotateY(0) rotateX(0)';
  });
})();
```
