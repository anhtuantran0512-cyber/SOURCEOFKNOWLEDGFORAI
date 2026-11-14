---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/css-shining-light-glare-image-hover/"
title: "CSS Shining Light Glare Image Hover"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "A linear-gradient sheen sweeps across the image on hover using a translateX-driven pseudo-element, simulating a light reflection glare."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shining Light Glare Image Hover
Source: https://codefronts.com/motion/css-image-hover-effects/css-shining-light-glare-image-hover/

A linear-gradient sheen sweeps across the image on hover using a translateX-driven pseudo-element, simulating a light reflection glare.
## HTML
```html
<div class="ih-13">
  <div class="ih-13__grid">
    <div class="ih-13__card">
      <div class="ih-13__img ih-13__img--1"><span class="ih-13__icon">🏆</span></div>
      <div class="ih-13__body">
        <p class="ih-13__tag">Premium</p>
        <p class="ih-13__title">Gold Tier Membership</p>
        <p class="ih-13__stars">★★★★★</p>
        <p class="ih-13__price">$49 / mo</p>
      </div>
    </div>
    <div class="ih-13__card">
      <div class="ih-13__img ih-13__img--2"><span class="ih-13__icon">💳</span></div>
      <div class="ih-13__body">
        <p class="ih-13__tag">Exclusive</p>
        <p class="ih-13__title">Platinum Credit Card</p>
        <p class="ih-13__stars">★★★★★</p>
        <p class="ih-13__price">0% APR 18mo</p>
      </div>
    </div>
    <div class="ih-13__card">
      <div class="ih-13__img ih-13__img--3"><span class="ih-13__icon">💎</span></div>
      <div class="ih-13__body">
        <p class="ih-13__tag">Diamond</p>
        <p class="ih-13__title">Crystal Pro Bundle</p>
        <p class="ih-13__stars">★★★★★</p>
        <p class="ih-13__price">$299 / yr</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-13,
.ih-13 *,
.ih-13 *::before,
.ih-13 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-13 ::selection {
  background: #fbbf24;
  color: #000;
}

.ih-13 {
  --accent: #fbbf24;
  --bg: #0a0906;
  --text: #f1f5f9;
  --muted: #78716c;
  --duration: 0.6s;
  --ease: cubic-bezier(0.4,0,0.2,1);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-13__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
  max-width: 780px;
  width: 100%;
}

.ih-13__card {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,0.06);
  transition: border-color var(--duration) var(--ease), box-shadow var(--duration) var(--ease);
}

.ih-13__card:hover {
  border-color: rgba(251,191,36,0.3);
  box-shadow: 0 8px 40px rgba(251,191,36,0.12);
}

.ih-13__img {
  aspect-ratio: 4/3;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}

.ih-13__img--1 {
  background: linear-gradient(135deg,#1c1003,#451a03,#92400e,#fbbf24);
}

.ih-13__img--2 {
  background: linear-gradient(135deg,#0d0d0d,#1f1f1f,#404040,#a3a3a3);
}

.ih-13__img--3 {
  background: linear-gradient(135deg,#1a0a24,#4c1d95,#7c3aed,#c4b5fd);
}

.ih-13__icon {
  font-size: 48px;
  opacity: 0.45;
  position: relative;
  z-index: 1;
}
/* The glare: a rotated linear-gradient pseudo-element that slides across */

.ih-13__img::after {
  content: '';
  position: absolute;
  inset: -50%;
  width: 40%;
  height: 200%;
  background: linear-gradient(
      105deg,
      transparent 40%,
      rgba(255,255,255,0.08) 45%,
      rgba(255,255,255,0.22) 50%,
      rgba(255,255,255,0.08) 55%,
      transparent 60%
    );
  transform: translateX(-200%) skewX(-10deg);
  transition: transform var(--duration) cubic-bezier(0.4,0,0.2,1);
}

.ih-13__card:hover .ih-13__img::after {
  transform: translateX(300%) skewX(-10deg);
}

.ih-13__body {
  padding: 14px 16px;
  background: rgba(0,0,0,0.4);
}

.ih-13__tag {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 5px;
}

.ih-13__title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
}

.ih-13__price {
  font-size: 16px;
  font-weight: 800;
  color: var(--accent);
  margin-top: 6px;
}

.ih-13__stars {
  font-size: 11px;
  color: var(--accent);
  margin-top: 2px;
  letter-spacing: -1px;
}

@media (prefers-reduced-motion: reduce) {
  .ih-13__img::after,
    .ih-13__card {
    transition: none;
  }

  .ih-13__img::after {
    display: none;
  }
}
```
