---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/image-zoom-with-content-reveal-slide-up/"
title: "Image Zoom with Content Reveal / Slide-Up"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A clean e-commerce product card showing only the image and a small badge at rest."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Zoom with Content Reveal / Slide-Up
Source: https://codefronts.com/motion/css-card-hover-effects/image-zoom-with-content-reveal-slide-up/

A clean e-commerce product card showing only the image and a small badge at rest. On hover, the image scales up smoothly inside an overflow:hidden frame while a frosted detail panel — name, price, description, and a "View Product" CTA — slides up from a peeking strip at the bottom. A dependable workhorse for shop grids, blog post cards, and directory listings.
## HTML
```html
<div class="card-03">
  <article class="card-03__card">
    <div class="card-03__media"><div class="card-03__img"></div></div>
    <span class="card-03__badge">New In</span>
    <div class="card-03__panel">
      <div class="card-03__top">
        <div>
          <h2 class="card-03__name">Terra Vase</h2>
          <p class="card-03__sub">Hand-thrown stoneware</p>
        </div>
        <span class="card-03__price">$68</span>
      </div>
      <p class="card-03__desc">Matte terracotta with a subtle asymmetric lip. Each piece is wheel-thrown and one of a kind.</p>
      <span class="card-03__cta">View Product</span>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,[email protected],500;9..144,600&family=Manrope:wght@400;500;700&display=swap');

.card-03,
.card-03 *,
.card-03 *::before,
.card-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-03 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #f4f1ec;
  font-family: 'Manrope', sans-serif;
  padding: 2rem;
}

.card-03__card {
  position: relative;
  width: 330px;
  height: 440px;
  border-radius: 18px;
  cursor: pointer;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 14px 36px rgba(60,50,40,0.12);
}
/* image area — clips the zoom */

.card-03__media {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.card-03__img {
  position: absolute;
  inset: 0;
  transform: scale(1);
  transition: transform 0.7s cubic-bezier(0.16,1,0.3,1);
  background: radial-gradient(circle at 35% 30%, #ffe2c2 0 30%, transparent 31%), linear-gradient(150deg, #e8956b, #b6452f 70%);
}

.card-03__img::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 42%;
  width: 150px;
  height: 150px;
  transform: translate(-50%,-50%);
  border-radius: 50% 50% 48% 52% / 60% 58% 42% 40%;
  background: linear-gradient(160deg, #6b3526, #3a1a12);
  box-shadow: 0 20px 40px rgba(0,0,0,0.25);
}

.card-03__card:hover .card-03__img {
  transform: scale(1.12);
}
/* top tag pinned over image */

.card-03__badge {
  position: absolute;
  top: 1.2rem;
  left: 1.2rem;
  z-index: 3;
  background: #1a1a1a;
  color: #fff;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.4rem 0.8rem;
  border-radius: 999px;
}
/* sliding panel from bottom */

.card-03__panel {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 4;
  background: rgba(255,255,255,0.96);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  padding: 1.4rem 1.5rem 1.6rem;
  transform: translateY(calc(100% - 84px));
  transition: transform 0.55s cubic-bezier(0.16,1,0.3,1);
}

.card-03__card:hover .card-03__panel {
  transform: translateY(0);
}

.card-03__top {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.card-03__name {
  font-family: 'Fraunces', serif;
  font-weight: 600;
  font-size: 1.5rem;
  color: #2a2018;
}

.card-03__price {
  font-weight: 700;
  font-size: 1.25rem;
  color: #b6452f;
}

.card-03__sub {
  font-size: 0.8rem;
  color: #8a7d70;
  margin-top: 0.15rem;
}

.card-03__desc {
  font-size: 0.84rem;
  line-height: 1.55;
  color: #6a5e52;
  margin: 0.9rem 0 1rem;
}

.card-03__cta {
  display: block;
  text-align: center;
  background: #1a1a1a;
  color: #fff;
  font-weight: 600;
  font-size: 0.88rem;
  padding: 0.8rem;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .card-03__img,
    .card-03__panel {
    transition: none !important;
  }
}
```
