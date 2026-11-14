---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/3d-overlapping-stacked-cards-isometric-view/"
title: "3D Overlapping Stacked Cards (Isometric View)"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "Three pricing tiers floated in a true isometric plane using perspective, rotateX, and rotateZ, each lifted on its own translateZ layer."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Overlapping Stacked Cards (Isometric View)
Source: https://codefronts.com/components/css-stacked-cards/3d-overlapping-stacked-cards-isometric-view/

Three pricing tiers floated in a true isometric plane using perspective, rotateX, and rotateZ, each lifted on its own translateZ layer. Hover eases the tilt and slides the upper tiers apart so all three prices stay readable. Suited to SaaS pricing pages, product mockups, and high-tech feature highlights.
## HTML
```html
<div class="scd-31">
  <div class="scd-31__stage">
    <div class="scd-31__stack">
      <div class="scd-31__plane scd-31__plane--p3"><span class="scd-31__tier">SCALE</span><span class="scd-31__feat">Unlimited seats &middot; SSO &middot; SLA</span><span class="scd-31__price">$79<small>/mo</small></span></div>
      <div class="scd-31__plane scd-31__plane--p2"><span class="scd-31__tier">GROWTH</span><span class="scd-31__feat">10 seats &middot; analytics &middot; API</span><span class="scd-31__price">$29<small>/mo</small></span></div>
      <div class="scd-31__plane scd-31__plane--p1"><span class="scd-31__tier">STARTER</span><span class="scd-31__feat">1 seat &middot; core features</span><span class="scd-31__price">$9<small>/mo</small></span></div>
    </div>
    <span class="scd-31__hint">HOVER TO COMPARE PLANS</span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=DM+Mono:wght@400&display=swap');

.scd-31,
.scd-31 *,
.scd-31 *::before,
.scd-31 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-31 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 30%,#191d2e,#0a0c14);
  font-family: 'DM Mono', monospace;
}

.scd-31__stage {
  perspective: 1400px;
  width: 340px;
  height: 420px;
  position: relative;
}

.scd-31__stack {
  position: relative;
  width: 100%;
  height: 100%;
  transform: rotateX(52deg) rotateZ(-34deg);
  transform-style: preserve-3d;
  transition: transform .7s cubic-bezier(.3,.9,.3,1);
}

.scd-31__stage:hover .scd-31__stack {
  transform: rotateX(46deg) rotateZ(-28deg);
}

.scd-31__plane {
  position: absolute;
  left: 50px;
  top: 120px;
  width: 240px;
  height: 150px;
  border-radius: 18px;
  padding: 22px;
  transform-style: preserve-3d;
  box-shadow: 0 36px 60px rgba(0,0,0,.55);
  transition: transform .65s cubic-bezier(.3,.9,.3,1);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.scd-31__tier {
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 700;
  font-size: 1.15rem;
  letter-spacing: .04em;
}

.scd-31__feat {
  font-size: .72rem;
  opacity: .85;
  line-height: 1.6;
}

.scd-31__price {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1;
}

.scd-31__price small {
  font-size: .85rem;
  opacity: .7;
}

.scd-31__plane--p1 {
  background: linear-gradient(135deg,#3a4cf0,#6d7cff);
  color: #fff;
}

.scd-31__plane--p2 {
  background: linear-gradient(135deg,#f0466b,#ff7aa0);
  color: #fff;
}

.scd-31__plane--p3 {
  background: linear-gradient(135deg,#11b894,#46f0c4);
  color: #03241c;
}

.scd-31__plane--p3 {
  transform: translateZ(12px) translate(0,0);
}

.scd-31__plane--p2 {
  transform: translateZ(24px) translate(0,0);
}

.scd-31__plane--p1 {
  transform: translateZ(36px) translate(0,0);
}

.scd-31__stage:hover .scd-31__plane--p1 {
  transform: translateZ(36px) translate(-150px,-150px);
}

.scd-31__stage:hover .scd-31__plane--p2 {
  transform: translateZ(24px) translate(0,0);
}

.scd-31__stage:hover .scd-31__plane--p3 {
  transform: translateZ(12px) translate(150px,150px);
}

.scd-31__hint {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  color: #5b6480;
  font-size: .72rem;
  letter-spacing: .18em;
  transition: opacity .4s;
}

.scd-31__stage:hover .scd-31__hint {
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .scd-31__stack,
    .scd-31__plane,
    .scd-31__hint {
    transition: none !important;
  }
}
```
