---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/greyscale-to-color-saturate-fade/"
title: "Greyscale to Color Saturate Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "Three profile cards transition from filter: saturate(0) brightness(0.7) to full color, creating a greyscale-to-vivid reveal with cascading animation delays."
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Greyscale to Color Saturate Fade
Source: https://codefronts.com/motion/css-fade-in-animation/greyscale-to-color-saturate-fade/

Three profile cards transition from filter: saturate(0) brightness(0.7) to full color, creating a greyscale-to-vivid reveal with cascading animation delays.
## HTML
```html
<div class="fi-13">
  <div class="fi-13__photo">
    <div class="fi-13__dot"></div>
    <div class="fi-13__overlay">
      <div class="fi-13__pname">Alex Chen</div>
      <div class="fi-13__prole">Lead Designer</div>
    </div>
  </div>
  <div class="fi-13__photo">
    <div class="fi-13__dot"></div>
    <div class="fi-13__overlay">
      <div class="fi-13__pname">Mia Torres</div>
      <div class="fi-13__prole">Engineering Lead</div>
    </div>
  </div>
  <div class="fi-13__photo">
    <div class="fi-13__dot"></div>
    <div class="fi-13__overlay">
      <div class="fi-13__pname">Sam Osei</div>
      <div class="fi-13__prole">Product Manager</div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-13 {
  --bg: #111;
  --text: #fafafa;
  font-family: 'Plus Jakarta Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  padding: 40px;
  overflow: hidden;
}

.fi-13 *,
.fi-13 *::before,
.fi-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-13 ::selection {
  background: #888;
  color: #fff;
}
/* Greyscale → color: filter:saturate(0) opacity:0 → saturate(1) opacity:1 */

.fi-13__photo {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  flex: 1;
  min-width: 140px;
  max-width: 170px;
  aspect-ratio: 3/4;
  opacity: 0;
  filter: saturate(0) brightness(.7);
  animation: fi-13-color-in 1s ease-out forwards;
  cursor: pointer;
}

.fi-13__photo:nth-child(1) {
  --d: .1s;
}

.fi-13__photo:nth-child(2) {
  --d: .3s;
}

.fi-13__photo:nth-child(3) {
  --d: .5s;
}

.fi-13__photo {
  animation-delay: var(--d);
}

.fi-13__photo:hover {
  filter: saturate(1.2) brightness(1.05)!important;
  transform: scale(1.03);
  transition: all .3s;
}
/* Colorful gradient "photos" */

.fi-13__photo:nth-child(1) {
  background: linear-gradient(160deg,#f97316,#ec4899,#8b5cf6);
}

.fi-13__photo:nth-child(2) {
  background: linear-gradient(160deg,#06b6d4,#3b82f6,#a855f7);
}

.fi-13__photo:nth-child(3) {
  background: linear-gradient(160deg,#10b981,#14b8a6,#0ea5e9);
}

.fi-13__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,rgba(0,0,0,.7) 0%,transparent 60%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 16px;
}

.fi-13__pname {
  font-size: .85rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 3px;
}

.fi-13__prole {
  font-size: .7rem;
  color: rgba(255,255,255,.6);
}

.fi-13__dot {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #4ade80;
  box-shadow: 0 0 6px #4ade80;
}

@keyframes fi-13-color-in {
  to {
    opacity: 1;
    filter: saturate(1) brightness(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-13 * {
    animation: none!important;
    opacity: 1!important;
    filter: none!important;
  }
}
```
