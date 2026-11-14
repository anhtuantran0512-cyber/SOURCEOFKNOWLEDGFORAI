---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/parent-blur-sibling-de-emphasis-focus-states/"
title: "Parent Blur / Sibling De-emphasis (Focus States)"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A pricing grid where hovering one card scales it up and brings it forward, while modern :has() and :not(:hover) selectors automatically blur and dim every…"
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parent Blur / Sibling De-emphasis (Focus States)
Source: https://codefronts.com/motion/css-card-hover-effects/parent-blur-sibling-de-emphasis-focus-states/

A pricing grid where hovering one card scales it up and brings it forward, while modern :has() and :not(:hover) selectors automatically blur and dim every neighboring card — pulling all attention to the chosen option with zero JavaScript. Best for pricing tables, minimalist galleries, and any multi-column layout where guiding focus matters. (Note: this demo intentionally renders three cards, since the effect only reads with siblings present.)
## HTML
```html
<div class="card-05">
  <div class="card-05__grid">
    <article class="card-05__card">
      <span class="card-05__plan">Starter</span>
      <div class="card-05__price">$0<span>/mo</span></div>
      <ul class="card-05__feat">
        <li>1 project</li>
        <li>Community support</li>
        <li>1 GB storage</li>
      </ul>
      <span class="card-05__btn">Get started</span>
    </article>

    <article class="card-05__card card-05__card--featured">
      <span class="card-05__plan card-05__popular">Pro · Popular</span>
      <div class="card-05__price">$24<span>/mo</span></div>
      <ul class="card-05__feat">
        <li>Unlimited projects</li>
        <li>Priority support</li>
        <li>100 GB storage</li>
        <li>Advanced analytics</li>
      </ul>
      <span class="card-05__btn">Start free trial</span>
    </article>

    <article class="card-05__card">
      <span class="card-05__plan">Team</span>
      <div class="card-05__price">$60<span>/mo</span></div>
      <ul class="card-05__feat">
        <li>Everything in Pro</li>
        <li>SSO &amp; roles</li>
        <li>1 TB storage</li>
      </ul>
      <span class="card-05__btn">Contact sales</span>
    </article>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Clash+Display:wght@500;600;700&family=Geist:wght@400;500;600&display=swap');

@import url('https://fonts.cdnfonts.com/css/clash-display');

.card-05,
.card-05 *,
.card-05 *::before,
.card-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-05 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #0d0f14;
  background-image: radial-gradient(circle at 50% 0%, #1a1e29, #0a0b10 70%);
  font-family: 'Geist', sans-serif;
  padding: 2rem;
}

.card-05__grid {
  display: flex;
  gap: 1.4rem;
}

.card-05__card {
  position: relative;
  width: 220px;
  height: 400px;
  border-radius: 20px;
  cursor: pointer;
  padding: 1.8rem;
  background: #14171f;
  border: 1px solid rgba(255,255,255,0.07);
  display: flex;
  flex-direction: column;
  color: #e6e9f0;
  transition: transform 0.4s cubic-bezier(0.16,1,0.3,1), filter 0.4s ease, opacity 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease;
}
/* hovered card pops forward */

.card-05__grid:has(.card-05__card:hover) .card-05__card:hover {
  transform: translateY(-12px) scale(1.05);
  box-shadow: 0 30px 60px rgba(0,0,0,0.5);
  border-color: rgba(122,160,255,0.5);
  z-index: 2;
}
/* every non-hovered sibling dims + blurs */

.card-05__grid:has(.card-05__card:hover) .card-05__card:not(:hover) {
  filter: blur(3px) saturate(0.6);
  opacity: 0.45;
  transform: scale(0.97);
}

.card-05__plan {
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #8a93a8;
}

.card-05__popular {
  color: #7aa0ff;
}

.card-05__price {
  font-family: 'Clash Display', 'Geist', sans-serif;
  font-weight: 600;
  font-size: 2.6rem;
  line-height: 1;
  margin: 0.6rem 0 0.2rem;
}

.card-05__price span {
  font-size: 0.9rem;
  color: #8a93a8;
  font-family: 'Geist';
}

.card-05__feat {
  list-style: none;
  margin: 1.4rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
  font-size: 0.82rem;
  color: #aab2c4;
}

.card-05__feat li::before {
  content: "✓ ";
  color: #7aa0ff;
  font-weight: 700;
}

.card-05__btn {
  margin-top: auto;
  text-align: center;
  font-weight: 600;
  font-size: 0.85rem;
  padding: 0.8rem;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.15);
  color: #e6e9f0;
}

.card-05__card--featured .card-05__btn {
  background: linear-gradient(90deg, #5a7cff, #7a50ff);
  border: none;
  color: #fff;
}

.card-05__card--featured {
  border-color: rgba(122,160,255,0.3);
}

@media (max-width: 760px) {
  .card-05__grid {
    flex-direction: column;
  }

  .card-05__card {
    width: 280px;
    height: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-05__card {
    transition: none !important;
  }
}
```
