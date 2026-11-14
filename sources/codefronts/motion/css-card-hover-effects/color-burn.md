---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/color-burn/"
title: "Color Burn"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A BBQ/food card that starts desaturated and dim, then ignites with a color-burn blend-mode fire layer and drifting embers on hover."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Color Burn
Source: https://codefronts.com/motion/css-card-hover-effects/color-burn/

A BBQ/food card that starts desaturated and dim, then ignites with a color-burn blend-mode fire layer and drifting embers on hover. Perfect for food, fitness, automotive, and any brand with heat and intensity in its story.
## HTML
```html
<div class="card-30">
  <article class="card-30__card">
    <div class="card-30__base"></div>
    <div class="card-30__layer"></div>
    <div class="card-30__embers"></div>
    <div class="card-30__inner">
      <span class="card-30__tag">BBQ · Texas Style</span>
      <h2 class="card-30__title">Low &amp;<br>Slow</h2>
      <p class="card-30__desc">Sixteen hours over post oak. Hover to bring the coals back to life.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;800&family=Barlow:wght@400;500&display=swap');

.card-30,
.card-30 *,
.card-30 *::before,
.card-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-30 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #100804;
  font-family: 'Barlow', sans-serif;
  padding: 2rem;
}

.card-30__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 14px;
  cursor: pointer;
  overflow: hidden;
  background: #1a1a1a;
  filter: grayscale(0.8) brightness(0.7);
  transition: filter 0.6s ease, box-shadow 0.6s ease;
}

.card-30__card:hover {
  filter: grayscale(0) brightness(1);
  box-shadow: 0 0 60px rgba(255,90,20,0.4);
}

.card-30__base {
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg, #4a4a52, #1c1c20);
}

.card-30__layer {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: radial-gradient(circle at 50% 100%, #ff7a18, #ff2d00 40%, #8a0e00 70%, transparent 90%);
  mix-blend-mode: color-burn;
  opacity: 0;
  transform: translateY(20%);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.card-30__card:hover .card-30__layer {
  opacity: 1;
  transform: translateY(0);
}

.card-30__embers {
  position: absolute;
  inset: 0;
  z-index: 2;
  background-image: radial-gradient(#ffcf6b 1px, transparent 1.5px), radial-gradient(#ff8a3c 1px, transparent 1.5px);
  background-size: 60px 60px, 90px 90px;
  background-position: 0 0, 30px 40px;
  opacity: 0;
  transition: opacity 0.6s ease 0.1s;
  mix-blend-mode: screen;
}

.card-30__card:hover .card-30__embers {
  opacity: 0.7;
}

.card-30__inner {
  position: relative;
  z-index: 3;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #f3ece4;
}

.card-30__tag {
  font-size: 0.72rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #ffb27a;
}

.card-30__title {
  font-family: 'Big Shoulders Display', sans-serif;
  font-weight: 800;
  font-size: 3.6rem;
  line-height: 0.82;
  text-transform: uppercase;
}

.card-30__desc {
  font-size: 0.86rem;
  line-height: 1.6;
  color: #d8cabc;
}

@media (prefers-reduced-motion: reduce) {
  .card-30__card,
    .card-30__layer,
    .card-30__embers {
    transition: none !important;
  }
}
```
