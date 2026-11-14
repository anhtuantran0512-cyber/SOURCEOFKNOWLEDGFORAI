---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/stacked-reveal/"
title: "Stacked Reveal"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A vinyl/record card built from three colored layers that fan out and rotate on hover, like spreading a deck of risograph prints."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Reveal
Source: https://codefronts.com/motion/css-card-hover-effects/stacked-reveal/

A vinyl/record card built from three colored layers that fan out and rotate on hover, like spreading a deck of risograph prints. The offset rotations give a playful, editorial collage feel suited to music, art prints, or creative portfolios.
## HTML
```html
<div class="card-09">
  <article class="card-09__card">
    <div class="card-09__layer card-09__l1"></div>
    <div class="card-09__layer card-09__l2"></div>
    <div class="card-09__layer card-09__l3"></div>
    <div class="card-09__content">
      <span class="card-09__kicker">Vinyl Press · 2025</span>
      <h2 class="card-09__title">Paper<br>Cities</h2>
      <p class="card-09__desc">Limited run pressing. Three layers of risograph artwork fan out across the gatefold sleeve.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;600&display=swap');

.card-09,
.card-09 *,
.card-09 *::before,
.card-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-09 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #ebe4d8;
  background-image: repeating-linear-gradient(45deg, rgba(0,0,0,0.02) 0 12px, transparent 12px 24px);
  font-family: 'Archivo', sans-serif;
  padding: 2rem;
}

.card-09__card {
  --card-09-shift: 14px;
  position: relative;
  width: 320px;
  height: 410px;
  cursor: pointer;
}

.card-09__layer {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease;
}

.card-09__layer.card-09__l1 {
  background: #d94f30;
  transform: translate(0, 0) rotate(0deg);
  z-index: 1;
}

.card-09__layer.card-09__l2 {
  background: #f2b138;
  z-index: 2;
}

.card-09__layer.card-09__l3 {
  background: #1a1a1a;
  z-index: 3;
  box-shadow: 0 18px 40px rgba(0,0,0,0.25);
}

.card-09__card:hover .card-09__l1 {
  transform: translate(calc(var(--card-09-shift) * -2), calc(var(--card-09-shift) * 1.4)) rotate(-6deg);
}

.card-09__card:hover .card-09__l2 {
  transform: translate(calc(var(--card-09-shift) * 1.6), calc(var(--card-09-shift) * -0.6)) rotate(5deg);
}

.card-09__card:hover .card-09__l3 {
  transform: translateY(-6px);
  box-shadow: 0 30px 60px rgba(0,0,0,0.35);
}

.card-09__content {
  position: relative;
  z-index: 4;
  height: 100%;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f4efe6;
  pointer-events: none;
}

.card-09__kicker {
  font-size: 0.7rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #f2b138;
}

.card-09__title {
  font-family: 'Archivo Black', sans-serif;
  font-size: 2.6rem;
  line-height: 0.95;
  text-transform: uppercase;
}

.card-09__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #c9c2b6;
}

@media (prefers-reduced-motion: reduce) {
  .card-09__layer {
    transition: none !important;
  }
}
```
