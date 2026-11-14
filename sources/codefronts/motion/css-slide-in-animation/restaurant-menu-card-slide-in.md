---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/restaurant-menu-card-slide-in/"
title: "Restaurant Menu Card Slide-In"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A warm-cream restaurant menu section where dish cards cascade in from below, each showing a plate photo, item name, description, price, and dietary tags —…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Restaurant Menu Card Slide-In
Source: https://codefronts.com/motion/css-slide-in-animation/restaurant-menu-card-slide-in/

A warm-cream restaurant menu section where dish cards cascade in from below, each showing a plate photo, item name, description, price, and dietary tags — the layout used by Toast, OpenTable, and modern restaurant marketing sites.
## HTML
```html
<div class="sl-01">
  <div class="sl-01__inner">
    <p class="sl-01__kicker">Chef's selection</p>
    <h2 class="sl-01__title">Dinner menu</h2>
    <p class="sl-01__sub">Sourced within 50 miles · Wine pairings on request</p>
    <div class="sl-01__grid">
      <article class="sl-01__dish">
        <div class="sl-01__plate">🥩</div>
        <div class="sl-01__body">
          <h3>Grass-fed Filet Mignon</h3>
          <p>8oz center-cut, roasted heirloom root veg, red wine jus</p>
          <div class="sl-01__meta"><span class="sl-01__tag sl-01__tag--gf">GF</span><span class="sl-01__price">$42</span></div>
        </div>
      </article>
      <article class="sl-01__dish">
        <div class="sl-01__plate">🐟</div>
        <div class="sl-01__body">
          <h3>Pan-seared Halibut</h3>
          <p>Wild Alaskan, saffron risotto, lemon-caper butter</p>
          <div class="sl-01__meta"><span class="sl-01__tag sl-01__tag--gf">GF</span><span class="sl-01__price">$38</span></div>
        </div>
      </article>
      <article class="sl-01__dish">
        <div class="sl-01__plate">🍝</div>
        <div class="sl-01__body">
          <h3>Handmade Pappardelle</h3>
          <p>Slow-braised beef ragù, aged pecorino, gremolata</p>
          <div class="sl-01__meta"><span class="sl-01__tag sl-01__tag--v">V</span><span class="sl-01__price">$28</span></div>
        </div>
      </article>
      <article class="sl-01__dish">
        <div class="sl-01__plate">🥗</div>
        <div class="sl-01__body">
          <h3>Roasted Beet Carpaccio</h3>
          <p>Whipped goat cheese, candied walnuts, aged balsamic</p>
          <div class="sl-01__meta"><span class="sl-01__tag sl-01__tag--vg">VG</span><span class="sl-01__tag sl-01__tag--gf">GF</span><span class="sl-01__price">$18</span></div>
        </div>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-01 {
  --bg: #f5ead0;
  --card: #fbf5e4;
  --accent: #c8552a;
  --ink: #2a1810;
  --sub: #7a5b3e;
  --olive: #658d5c;
  --line: rgba(42,24,16,.10);
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 32px;
  background: radial-gradient(80% 60% at 20% 0%, rgba(200,85,42,.06) 0%, transparent 55%), var(--bg);
  color: var(--ink);
}

.sl-01 *,
.sl-01 *::before,
.sl-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-01 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-01__inner {
  width: 100%;
  max-width: 820px;
}

.sl-01__kicker {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: .85rem;
  font-weight: 400;
  font-style: italic;
  letter-spacing: .02em;
  color: var(--accent);
  margin-bottom: 6px;
  text-align: center;
}

.sl-01__title {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(2rem,4.4vw,3rem);
  font-weight: 800;
  letter-spacing: -.015em;
  line-height: 1;
  margin-bottom: 10px;
  text-align: center;
}

.sl-01__sub {
  font-size: .88rem;
  color: var(--sub);
  text-align: center;
  margin-bottom: 32px;
  letter-spacing: .02em;
}

.sl-01__grid {
  display: grid;
  grid-template-columns: repeat(2,1fr);
  gap: 14px;
}

.sl-01__dish {
  display: flex;
  gap: 14px;
  padding: 18px 20px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--card);
  box-shadow: 0 8px 20px -12px rgba(42,24,16,.2);
  opacity: 0;
  transform: translateY(40px);
  animation: sl-01-dish .7s cubic-bezier(.22,1,.36,1) forwards;
}

.sl-01__dish:nth-child(1) {
  animation-delay: .1s;
}

.sl-01__dish:nth-child(2) {
  animation-delay: .25s;
}

.sl-01__dish:nth-child(3) {
  animation-delay: .4s;
}

.sl-01__dish:nth-child(4) {
  animation-delay: .55s;
}

.sl-01__plate {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  flex-shrink: 0;
  background: linear-gradient(135deg,#ede0c0,#d9c99b);
  font-size: 22px;
  box-shadow: inset 0 -2px 4px rgba(42,24,16,.1),inset 0 2px 4px rgba(255,255,255,.6);
}

.sl-01__body {
  flex: 1;
  min-width: 0;
}

.sl-01__body h3 {
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.005em;
  margin-bottom: 4px;
}

.sl-01__body p {
  font-size: .82rem;
  color: var(--sub);
  line-height: 1.45;
  margin-bottom: 8px;
}

.sl-01__meta {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.sl-01__tag {
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(101,141,92,.15);
  color: var(--olive);
}

.sl-01__tag--v {
  background: rgba(200,85,42,.15);
  color: var(--accent);
}

.sl-01__tag--vg {
  background: rgba(101,141,92,.15);
  color: var(--olive);
}

.sl-01__tag--gf {
  background: rgba(122,91,62,.12);
  color: var(--sub);
}

.sl-01__price {
  margin-left: auto;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
}

@keyframes sl-01-dish {
  from {
    opacity: 0;
    transform: translateY(40px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-01__dish {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 600px) {
  .sl-01__grid {
    grid-template-columns: 1fr;
  }
}
```
