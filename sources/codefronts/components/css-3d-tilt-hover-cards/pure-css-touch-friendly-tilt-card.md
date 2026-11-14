---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/pure-css-touch-friendly-tilt-card/"
title: "Pure CSS Touch-Friendly Tilt Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "Zero JavaScript, zero listeners: a 3×3 grid of invisible hover zones overlays the card, and :has() maps whichever zone the cursor occupies to a predefined…"
has_js: "false"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Touch-Friendly Tilt Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/pure-css-touch-friendly-tilt-card/

Zero JavaScript, zero listeners: a 3×3 grid of invisible hover zones overlays the card, and :has() maps whichever zone the cursor occupies to a predefined tilt pose — nine discrete poses that eased transitions blend into motion that feels continuous. The accessible, dependency-free fallback every tilt collection needs.
## HTML
```html
<section class="thc-15" aria-label="Pure CSS no-JavaScript tilt card demo">
  <article class="thc-15__card" tabindex="0" aria-label="CSS-only tilt card, no JavaScript required">
    <i class="thc-15__z"></i><i class="thc-15__z"></i><i class="thc-15__z"></i>
    <i class="thc-15__z"></i><i class="thc-15__z"></i><i class="thc-15__z"></i>
    <i class="thc-15__z"></i><i class="thc-15__z"></i><i class="thc-15__z"></i>
    <div class="thc-15__glare" aria-hidden="true"></div>
    <div class="thc-15__content">
      <p class="thc-15__kicker">0 KB OF JAVASCRIPT</p>
      <h3 class="thc-15__title">Pure CSS Tilt</h3>
      <p class="thc-15__body">Nine invisible hover zones + :has() = a tilt card with no listeners, no library, no main-thread work.</p>
    </div>
    <a class="thc-15__cta" href="#">Read the technique</a>
  </article>
</section>
```
## CSS
```css
.thc-15,
.thc-15 *,
.thc-15 *::before,
.thc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-15 {
  --acc: oklch(0.78 0.15 85);
  --tx: 10deg;
  --ty: 10deg;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(80% 90% at 25% 15%,oklch(0.26 0.05 85 / .8),transparent 60%),oklch(0.15 0.015 280);
}

.thc-15 .thc-15__card {
  position: relative;
  width: min(310px,100%);
  aspect-ratio: 31/24;
  border-radius: 20px;
  background: linear-gradient(165deg,oklch(0.22 0.03 85),oklch(0.16 0.02 280));
  border: 1px solid rgba(255,255,255,.12);
  display: grid;
  grid-template: repeat(3,1fr)/repeat(3,1fr);
  transform: perspective(1000px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .35s ease;
  box-shadow: 0 28px 58px -28px rgba(0,0,0,.8);
}

.thc-15 .thc-15__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 4px;
}
/* Zones sit ABOVE the content overlay so hover always reaches a zone.
   Content is pointer-events:none by default so the zone <i>'s underneath
   stay hoverable through the visual content; the CTA re-enables pointer
   events on itself so it remains clickable. Without this, moving the
   cursor over the title / kicker / body would block zone :hover and the
   card would freeze mid-tilt. */

.thc-15 .thc-15__z {
  z-index: 3;
}

.thc-15 .thc-15__glare {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: radial-gradient(240px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.17),transparent 62%);
  opacity: 0;
  transition: opacity .35s ease,background-position .35s ease;
  z-index: 1;
}

.thc-15 .thc-15__card:hover .thc-15__glare {
  opacity: 1;
}

.thc-15 .thc-15__content {
  position: absolute;
  inset: 0;
  padding: 30px 28px;
  display: flex;
  flex-direction: column;
  transform: translateZ(30px);
  pointer-events: none;
  z-index: 2;
}

.thc-15 .thc-15__kicker {
  font: 700 10px ui-monospace,monospace;
  letter-spacing: .2em;
  color: var(--acc);
}

.thc-15 .thc-15__title {
  margin-top: 12px;
  font-size: 28px;
  font-weight: 800;
  color: #fff;
}

.thc-15 .thc-15__body {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(255,255,255,.65);
  text-wrap: pretty;
}

.thc-15 .thc-15__cta {
  position: absolute;
  left: 28px;
  bottom: 28px;
  z-index: 4;
  font: 600 13px 'Segoe UI',sans-serif;
  color: oklch(0.15 0.015 280);
  background: var(--acc);
  text-decoration: none;
  border-radius: 999px;
  padding: 10px 18px;
  transform: translateZ(45px);
}

.thc-15 .thc-15__cta:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}
/* 3x3 pose map — row 1 */

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(1):hover) {
  --rx: var(--tx);
  --ry: calc(var(--ty) * -1);
  --mx: 16%;
  --my: 16%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(2):hover) {
  --rx: var(--tx);
  --ry: 0deg;
  --mx: 50%;
  --my: 16%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(3):hover) {
  --rx: var(--tx);
  --ry: var(--ty);
  --mx: 84%;
  --my: 16%;
}
/* row 2 */

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(4):hover) {
  --rx: 0deg;
  --ry: calc(var(--ty) * -1);
  --mx: 16%;
  --my: 50%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(5):hover) {
  --rx: 0deg;
  --ry: 0deg;
  --mx: 50%;
  --my: 50%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(6):hover) {
  --rx: 0deg;
  --ry: var(--ty);
  --mx: 84%;
  --my: 50%;
}
/* row 3 */

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(7):hover) {
  --rx: calc(var(--tx) * -1);
  --ry: calc(var(--ty) * -1);
  --mx: 16%;
  --my: 84%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(8):hover) {
  --rx: calc(var(--tx) * -1);
  --ry: 0deg;
  --mx: 50%;
  --my: 84%;
}

.thc-15 .thc-15__card:has(.thc-15__z:nth-child(9):hover) {
  --rx: calc(var(--tx) * -1);
  --ry: var(--ty);
  --mx: 84%;
  --my: 84%;
}

.thc-15 .thc-15__card:focus-within {
  --rx: 2deg;
  --ry: 0deg;
}

@media (hover: none) {
  .thc-15 .thc-15__card {
    transform: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .thc-15 .thc-15__card,
    .thc-15__glare {
    transition: none;
  }

  .thc-15 .thc-15__card:has(.thc-15__z:hover) {
    --rx: 0deg;
    --ry: 0deg;
  }
}
```

## JavaScript
```js
/* No JavaScript — nine invisible hover zones + :has() map the cursor to predefined tilt poses; eased transitions blend the steps into motion. */
```
