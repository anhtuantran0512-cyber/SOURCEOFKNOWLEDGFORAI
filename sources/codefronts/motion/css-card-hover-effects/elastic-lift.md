---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/elastic-lift/"
title: "Elastic Lift"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A coffee brand card that springs upward on hover with a bouncy, overshooting cubic-bezier curve and a warm ember glow rising from below."
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Elastic Lift
Source: https://codefronts.com/motion/css-card-hover-effects/elastic-lift/

A coffee brand card that springs upward on hover with a bouncy, overshooting cubic-bezier curve and a warm ember glow rising from below. The elastic timing makes the lift feel physical and tactile rather than a flat translate — ideal for product or menu cards where you want a friendly, energetic response.
## HTML
```html
<div class="card-07">
  <article class="card-07__card">
    <div class="card-07__inner">
      <span class="card-07__tag">Seasonal Roast</span>
      <div>
        <div class="card-07__num">04</div>
      </div>
      <div>
        <h2 class="card-07__title">Ember Drip<br>Coffee Co.</h2>
        <p class="card-07__desc">Slow-roasted single origin beans with notes of burnt caramel and stone fruit.</p>
      </div>
    </div>
    <span class="card-07__dot"></span>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,[email protected],400;9..144,600;9..144,900&family=Spline+Sans+Mono:wght@400;500&display=swap');

.card-07,
.card-07 *,
.card-07 *::before,
.card-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-07 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 20% 20%, #ffe7c2 0%, transparent 45%), radial-gradient(circle at 80% 80%, #ffc9d4 0%, transparent 45%), #f4ede4;
  font-family: 'Spline Sans Mono', monospace;
  padding: 2rem;
}

.card-07__card {
  --card-07-bounce: cubic-bezier(0.34, 1.8, 0.4, 1);
  position: relative;
  width: 320px;
  height: 420px;
  border-radius: 28px;
  background: linear-gradient(160deg, #1c1410 0%, #3a2618 100%);
  color: #f4ede4;
  cursor: pointer;
  overflow: hidden;
  transform-origin: bottom center;
  transition: transform 0.55s var(--card-07-bounce), box-shadow 0.55s ease;
  box-shadow: 0 10px 25px rgba(60, 30, 10, 0.25);
  will-change: transform;
}

.card-07__card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 120%, #ff8a3c 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.5s ease;
}

.card-07__card:hover {
  transform: translateY(-26px) scale(1.04);
  box-shadow: 0 40px 60px rgba(60, 30, 10, 0.4);
}

.card-07__card:hover::before {
  opacity: 0.55;
}

.card-07__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem 2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-07__tag {
  font-size: 0.72rem;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: #ffb27a;
}

.card-07__num {
  font-family: 'Fraunces', serif;
  font-size: 5.5rem;
  font-weight: 900;
  line-height: 0.85;
  transition: transform 0.55s var(--card-07-bounce);
}

.card-07__card:hover .card-07__num {
  transform: translateY(-6px);
}

.card-07__title {
  font-family: 'Fraunces', serif;
  font-size: 1.9rem;
  font-weight: 600;
  line-height: 1.1;
}

.card-07__desc {
  font-size: 0.85rem;
  line-height: 1.6;
  color: #cdb9a6;
  max-width: 90%;
}

.card-07__dot {
  position: absolute;
  bottom: 1.8rem;
  right: 1.8rem;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #ff8a3c;
  box-shadow: 0 0 0 0 rgba(255, 138, 60, 0.6);
  transition: box-shadow 0.5s ease;
}

.card-07__card:hover .card-07__dot {
  box-shadow: 0 0 0 10px rgba(255, 138, 60, 0);
}

@media (prefers-reduced-motion: reduce) {
  .card-07__card,
    .card-07__num,
    .card-07__dot {
    transition: none !important;
  }
}
```
