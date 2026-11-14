---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/magnetic-float/"
title: "Magnetic Float"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A music/interactive card with a glowing orb that leans toward the cursor as if caught in a magnetic field, over a tech grid backdrop."
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magnetic Float
Source: https://codefronts.com/motion/css-card-hover-effects/magnetic-float/

A music/interactive card with a glowing orb that leans toward the cursor as if caught in a magnetic field, over a tech grid backdrop. Ideal for interactive demos, audio apps, and playful CTAs that invite the pointer in.
## HTML
```html
<div class="card-23">
  <article class="card-23__card" data-card-23="root">
    <div class="card-23__grid"></div>
    <div class="card-23__orb" data-card-23="orb">PLAY ▶</div>
    <div class="card-23__inner">
      <span class="card-23__eyebrow">Interactive Demo</span>
      <h2 class="card-23__title">Gravity<br>Synth</h2>
      <p class="card-23__desc">Drag your cursor near the orb — it leans toward you like it's caught in your field.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;900&family=Manrope:wght@400;500;700&display=swap');

.card-23,
.card-23 *,
.card-23 *::before,
.card-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-23 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #06060a;
  font-family: 'Manrope', sans-serif;
  padding: 2rem;
}

.card-23__card {
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 26px;
  background: radial-gradient(circle at 50% 0%, #1c2540, #0a0d1a);
  cursor: pointer;
  overflow: hidden;
  border: 1px solid rgba(120,160,255,0.12);
}

.card-23__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(120,160,255,0.06) 1px, transparent 1px), linear-gradient(90deg, rgba(120,160,255,0.06) 1px, transparent 1px);
  background-size: 28px 28px;
}

.card-23__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e9eefc;
}

.card-23__eyebrow {
  font-size: 0.72rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #6f8bd6;
}

.card-23__title {
  font-family: 'Unbounded', sans-serif;
  font-weight: 700;
  font-size: 2.1rem;
  line-height: 1.05;
}

.card-23__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #93a0c4;
}

.card-23__orb {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 110px;
  height: 110px;
  margin: -55px 0 0 -55px;
  border-radius: 50%;
  background: linear-gradient(145deg, #6a8cff, #b46aff);
  display: grid;
  place-items: center;
  color: #fff;
  font-weight: 700;
  font-size: 0.95rem;
  letter-spacing: 0.05em;
  z-index: 3;
  box-shadow: 0 0 40px rgba(120,140,255,0.5);
  transition: transform 0.18s ease-out, box-shadow 0.3s ease;
  will-change: transform;
}

.card-23__card:hover .card-23__orb {
  box-shadow: 0 0 60px rgba(140,120,255,0.7);
}

@media (prefers-reduced-motion: reduce) {
  .card-23__orb {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-23');
  if (!root) return;
  const card = root.querySelector('[data-card-23="root"]');
  const orb = root.querySelector('[data-card-23="orb"]');
  if (!card || !orb) return;
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    const cx = r.left + r.width / 2;
    const cy = r.top + r.height / 2;
    const dx = (e.clientX - cx) * 0.4;
    const dy = (e.clientY - cy) * 0.4;
    orb.style.transform = `translate(${dx}px, ${dy}px) scale(1.05)`;
  });
  card.addEventListener('mouseleave', () => {
    orb.style.transform = 'translate(0,0) scale(1)';
  });
})();
```
