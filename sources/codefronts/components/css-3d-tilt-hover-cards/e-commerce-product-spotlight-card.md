---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/e-commerce-product-spotlight-card/"
title: "E-Commerce Product Spotlight Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A premium product card where the sneaker cutout floats 50px in front of the card face, the Add-to-Cart button rides even higher, and a radial glare chases…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Product Spotlight Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/e-commerce-product-spotlight-card/

A premium product card where the sneaker cutout floats 50px in front of the card face, the Add-to-Cart button rides even higher, and a radial glare chases the cursor. The depth stack — background, product, copy, CTA — is the exact pattern D2C stores use to make a $189 product feel worth it before a single scroll.
## HTML
```html
<section class="thc-01" aria-label="E-commerce product spotlight tilt card demo">
  <article class="thc-01__card" tabindex="0" aria-label="Aurora Runner sneaker, 189 dollars">
    <span class="thc-01__badge" aria-hidden="true">NEW DROP</span>
    <div class="thc-01__product" aria-hidden="true"></div>
    <h3 class="thc-01__name">Aurora Runner</h3>
    <p class="thc-01__meta">Limited colourway &middot; <strong>$189</strong></p>
    <button class="thc-01__cta" type="button">Add to Cart</button>
    <div class="thc-01__glare" aria-hidden="true"></div>
  </article>
</section>
```
## CSS
```css
.thc-01,
.thc-01 *,
.thc-01 *::before,
.thc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-01 {
  --ink: oklch(0.93 0.01 260);
  --accent: oklch(0.72 0.17 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(80% 90% at 15% 10%,oklch(0.28 0.06 290 / .9),transparent 60%),radial-gradient(70% 80% at 90% 95%,oklch(0.25 0.07 40 / .8),transparent 60%),oklch(0.15 0.02 280);
}

.thc-01 .thc-01__card {
  position: relative;
  width: min(300px,100%);
  padding: 28px 26px 26px;
  border-radius: 22px;
  background: linear-gradient(160deg,oklch(0.24 0.03 285),oklch(0.18 0.025 280));
  border: 1px solid rgba(255,255,255,.1);
  transform: perspective(1100px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.2,.9,.3,1.15);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.8);
  cursor: pointer;
}

.thc-01 .thc-01__card.is-live {
  transition: transform .08s linear;
}

.thc-01 .thc-01__card:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

.thc-01 .thc-01__badge {
  position: absolute;
  top: 18px;
  left: 22px;
  font: 700 10px/1 'Segoe UI',sans-serif;
  letter-spacing: .12em;
  color: var(--accent);
  border: 1px solid color-mix(in oklab,var(--accent) 50%,transparent);
  border-radius: 999px;
  padding: 6px 10px;
  transform: translateZ(35px);
}

.thc-01 .thc-01__product {
  width: 82%;
  aspect-ratio: 4/3;
  margin: 26px auto 8px;
  border-radius: 16px;
  background: radial-gradient(70% 90% at 35% 30%,oklch(0.75 0.16 40),oklch(0.55 0.19 25) 55%,oklch(0.35 0.1 300) 100%);
  transform: translateZ(50px) rotate(-6deg);
  filter: drop-shadow(0 24px 22px rgba(0,0,0,.55));
  transition: transform .6s cubic-bezier(.2,.9,.3,1.15);
}

.thc-01 .thc-01__card.is-live .thc-01__product {
  transform: translateZ(62px) rotate(-8deg);
}

.thc-01 .thc-01__name {
  font-size: 20px;
  font-weight: 700;
  color: var(--ink);
  transform: translateZ(25px);
}

.thc-01 .thc-01__meta {
  font-size: 13px;
  color: oklch(0.7 0.02 270);
  margin-top: 4px;
  transform: translateZ(25px);
}

.thc-01 .thc-01__meta strong {
  color: var(--ink);
}

.thc-01 .thc-01__cta {
  margin-top: 16px;
  width: 100%;
  height: 44px;
  border: none;
  border-radius: 12px;
  font: 600 14px 'Segoe UI',sans-serif;
  color: oklch(0.15 0.02 280);
  background: linear-gradient(120deg,oklch(0.78 0.15 45),oklch(0.7 0.18 30));
  transform: translateZ(60px);
  cursor: pointer;
  box-shadow: 0 14px 26px -12px oklch(0.6 0.18 35 / .7);
}

.thc-01 .thc-01__cta:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.thc-01 .thc-01__glare {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: radial-gradient(260px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.22),transparent 65%);
  opacity: 0;
  transition: opacity .4s ease;
  transform: translateZ(70px);
}

.thc-01 .thc-01__card.is-live .thc-01__glare {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .thc-01 .thc-01__card,
    .thc-01 .thc-01__product {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-01 .thc-01__card');
  if (!card) return;
  // Touch + motion guards: static (fully styled) card for everyone else.
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 14; // degrees of tilt at the card's edge
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;   // 0 → 1 across the card
    const py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    card.classList.add('is-live');
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');           // re-arm the slow spring transition
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
