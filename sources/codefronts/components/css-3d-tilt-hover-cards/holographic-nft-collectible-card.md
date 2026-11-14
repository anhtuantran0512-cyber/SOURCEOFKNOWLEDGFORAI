---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/holographic-nft-collectible-card/"
title: "Holographic NFT Collectible Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A trading-card-grade holo effect: a conic rainbow foil swings across the artwork as the cursor moves, blended with color-dodge over a deep-space gradient,…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic NFT Collectible Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/holographic-nft-collectible-card/

A trading-card-grade holo effect: a conic rainbow foil swings across the artwork as the cursor moves, blended with color-dodge over a deep-space gradient, inside a heavy ±20° tilt. This is the pattern behind every viral 'Pokémon card CSS' demo — rebuilt with oklch stops so the foil never muddies.
## HTML
```html
<section class="thc-04" aria-label="Holographic NFT collectible tilt card demo">
  <article class="thc-04__card" tabindex="0" aria-label="Nebula Drifter number 042, legendary rarity">
    <div class="thc-04__art" aria-hidden="true"><img src="https://picsum.photos/seed/nebula-drifter/540/756" alt="" loading="lazy"></div>
    <div class="thc-04__foil" aria-hidden="true"></div>
    <div class="thc-04__spec" aria-hidden="true"></div>
    <div class="thc-04__plate">
      <h3 class="thc-04__name">Nebula Drifter</h3>
      <p class="thc-04__rank">#042 &middot; LEGENDARY</p>
    </div>
  </article>
</section>
```
## CSS
```css
.thc-04,
.thc-04 *,
.thc-04 *::before,
.thc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-04 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 50% -10%,oklch(0.22 0.06 300 / .9),transparent 60%),oklch(0.12 0.02 290);
}

.thc-04 .thc-04__card {
  position: relative;
  width: min(270px,100%);
  aspect-ratio: 5/7;
  border-radius: 18px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.18);
  transform: perspective(900px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .65s cubic-bezier(.2,.9,.3,1.2);
  box-shadow: 0 34px 70px -28px rgba(0,0,0,.9);
  cursor: pointer;
}

.thc-04 .thc-04__card.is-live {
  transition: transform .07s linear;
}

.thc-04 .thc-04__card:focus-visible {
  outline: 3px solid oklch(0.75 0.15 200);
  outline-offset: 4px;
}

.thc-04 .thc-04__art img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: saturate(1.15) contrast(1.05);
}

.thc-04 .thc-04__art {
  position: absolute;
  inset: 0;
  background: radial-gradient(65% 50% at 30% 30%,oklch(0.55 0.2 310),transparent 60%),radial-gradient(55% 45% at 75% 65%,oklch(0.5 0.19 230),transparent 60%),radial-gradient(40% 35% at 55% 20%,oklch(0.7 0.15 60 / .7),transparent 60%),oklch(0.18 0.05 290);
}

.thc-04 .thc-04__foil {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: color-dodge;
  opacity: 0;
  transition: opacity .5s ease;
  background: conic-gradient(from 90deg,oklch(0.7 0.2 20),oklch(0.75 0.19 90),oklch(0.72 0.2 160),oklch(0.7 0.2 230),oklch(0.68 0.21 300),oklch(0.7 0.2 20));
  background-size: 220% 220%;
  background-position: var(--mx,50%) var(--my,50%);
  filter: saturate(1.4) brightness(.85);
}

.thc-04 .thc-04__spec {
  position: absolute;
  inset: -40%;
  pointer-events: none;
  opacity: 0;
  transition: opacity .5s ease;
  background: linear-gradient(115deg,transparent 42%,rgba(255,255,255,.65) 50%,transparent 58%);
  background-size: 250% 250%;
  background-position: var(--mx,50%) var(--my,50%);
  mix-blend-mode: overlay;
}

.thc-04 .thc-04__card.is-live .thc-04__foil {
  opacity: .85;
}

.thc-04 .thc-04__card.is-live .thc-04__spec {
  opacity: 1;
}

.thc-04 .thc-04__plate {
  position: absolute;
  left: 14px;
  right: 14px;
  bottom: 14px;
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(10,8,20,.55);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.15);
  transform: translateZ(40px);
}

.thc-04 .thc-04__name {
  font-size: 17px;
  font-weight: 700;
  color: #fff;
}

.thc-04 .thc-04__rank {
  font: 600 10px 'Segoe UI',sans-serif;
  letter-spacing: .14em;
  color: oklch(0.78 0.14 90);
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-04 .thc-04__card {
    transition: none;
  }

  .thc-04__foil,
    .thc-04__spec {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-04 .thc-04__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 20; // collectibles earn drama
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    // Foil travels OPPOSITE the pointer — like light raking across real holo foil.
    card.style.setProperty('--mx', ((1 - px) * 100).toFixed(1) + '%');
    card.style.setProperty('--my', ((1 - py) * 100).toFixed(1) + '%');
    card.classList.add('is-live');
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
