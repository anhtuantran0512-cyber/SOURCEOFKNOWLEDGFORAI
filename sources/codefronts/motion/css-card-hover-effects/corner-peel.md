---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/corner-peel/"
title: "Corner Peel"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A sticker-style promo card whose top-right corner physically peels back to expose a hidden discount underneath, with a soft drop shadow on the lifted flap."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Peel
Source: https://codefronts.com/motion/css-card-hover-effects/corner-peel/

A sticker-style promo card whose top-right corner physically peels back to expose a hidden discount underneath, with a soft drop shadow on the lifted flap. Ideal for coupons, membership perks, or any card with a reward worth "uncovering."
## HTML
```html
<div class="card-12">
  <article class="card-12__card">
    <div class="card-12__secret"><span>-20%</span></div>
    <div class="card-12__flap"></div>
    <div class="card-12__content">
      <span class="card-12__tag">Members Only</span>
      <h2 class="card-12__title">Spring<br>Harvest Box</h2>
      <p class="card-12__desc">Peel the corner to uncover this week's hidden subscriber discount on farm-fresh produce.</p>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@600&family=Nunito+Sans:opsz,[email protected],400;6..12,700&display=swap');

.card-12,
.card-12 *,
.card-12 *::before,
.card-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-12 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #cfe3dd;
  background-image: radial-gradient(circle at 30% 20%, #e2f0eb, #b9d4cb);
  font-family: 'Nunito Sans', sans-serif;
  padding: 2rem;
}

.card-12__card {
  position: relative;
  width: 320px;
  height: 400px;
  border-radius: 14px;
  background: #fffdf7;
  cursor: pointer;
  box-shadow: 0 14px 30px rgba(40, 70, 60, 0.18);
  overflow: hidden;
}

.card-12__content {
  position: relative;
  z-index: 1;
  height: 100%;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #2a3d36;
}

.card-12__tag {
  align-self: flex-start;
  background: #ff7a59;
  color: #fff;
  font-weight: 700;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  padding: 0.35rem 0.8rem;
  border-radius: 999px;
  text-transform: uppercase;
}

.card-12__title {
  font-family: 'Caveat', cursive;
  font-size: 3rem;
  line-height: 0.95;
  color: #1f5c4d;
}

.card-12__desc {
  font-size: 0.9rem;
  line-height: 1.6;
  color: #5a6e66;
}

.card-12__flap {
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 0;
  z-index: 4;
  background: linear-gradient(135deg, #f7efe0, #e7dcc6);
  transform-origin: top right;
  transition: width 0.45s cubic-bezier(0.16,1,0.3,1), height 0.45s cubic-bezier(0.16,1,0.3,1), box-shadow 0.45s ease;
  clip-path: polygon(100% 0, 0 0, 100% 100%);
  box-shadow: none;
}

.card-12__secret {
  position: absolute;
  top: 0;
  right: 0;
  width: 0;
  height: 0;
  z-index: 3;
  background: linear-gradient(135deg, #1f5c4d, #2f8f76);
  clip-path: polygon(100% 0, 0 0, 100% 100%);
  transition: width 0.45s cubic-bezier(0.16,1,0.3,1), height 0.45s cubic-bezier(0.16,1,0.3,1);
  display: grid;
  place-items: center;
}

.card-12__secret span {
  position: absolute;
  top: 14px;
  right: 14px;
  color: #fff;
  font-weight: 700;
  font-size: 0.65rem;
  opacity: 0;
  transition: opacity 0.3s ease 0.2s;
  transform: rotate(45deg);
}

.card-12__card:hover .card-12__secret {
  width: 110px;
  height: 110px;
}

.card-12__card:hover .card-12__secret span {
  opacity: 1;
}

.card-12__card:hover .card-12__flap {
  width: 110px;
  height: 110px;
  box-shadow: -6px 6px 14px rgba(0,0,0,0.25);
}

@media (prefers-reduced-motion: reduce) {
  .card-12__flap,
    .card-12__secret,
    .card-12__secret span {
    transition: none !important;
  }
}
```
