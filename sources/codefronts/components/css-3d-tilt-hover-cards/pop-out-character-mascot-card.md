---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/pop-out-character-mascot-card/"
title: "Pop-Out Character Mascot Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "The scroll-stopping agency trick: a mascot cutout whose head rises OUTSIDE the card's top edge, floating at translateZ(70px) while the card tilts beneath it."
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pop-Out Character Mascot Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/pop-out-character-mascot-card/

The scroll-stopping agency trick: a mascot cutout whose head rises OUTSIDE the card's top edge, floating at translateZ(70px) while the card tilts beneath it. The illusion needs exactly two decisions — overflow:visible on the card, and a cutout that overlaps the border — and it makes any character IP feel alive.
## HTML
```html
<section class="thc-05" aria-label="Pop-out mascot tilt card demo">
  <article class="thc-05__card" tabindex="0" aria-label="Blobby, studio mascot">
    <div class="thc-05__face" aria-hidden="true"></div>
    <div class="thc-05__mascot" aria-hidden="true"><span class="thc-05__eye thc-05__eye--l"></span><span class="thc-05__eye thc-05__eye--r"></span></div>
    <div class="thc-05__plate">
      <h3 class="thc-05__name">Blobby</h3>
      <p class="thc-05__sub">Chief Vibe Officer &middot; est. 2019</p>
    </div>
  </article>
</section>
```
## CSS
```css
.thc-05,
.thc-05 *,
.thc-05 *::before,
.thc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-05 {
  --skin: oklch(0.72 0.19 145);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 110px 24px 48px;
  background: radial-gradient(80% 90% at 80% 10%,oklch(0.3 0.09 145 / .7),transparent 60%),radial-gradient(70% 80% at 10% 90%,oklch(0.28 0.07 250 / .7),transparent 60%),oklch(0.16 0.02 200);
}

.thc-05 .thc-05__card {
  position: relative;
  width: min(290px,100%);
  height: 250px;
  border-radius: 22px;
  overflow: visible;
  transform: perspective(1000px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.2,.9,.3,1.15);
  cursor: pointer;
}

.thc-05 .thc-05__card.is-live {
  transition: transform .08s linear;
}

.thc-05 .thc-05__card:focus-visible {
  outline: 3px solid var(--skin);
  outline-offset: 6px;
}

.thc-05 .thc-05__face {
  position: absolute;
  inset: 0;
  border-radius: 22px;
  overflow: hidden;
  background: linear-gradient(170deg,oklch(0.28 0.06 150),oklch(0.2 0.04 200));
  border: 1px solid rgba(255,255,255,.12);
  box-shadow: 0 30px 60px -26px rgba(0,0,0,.8);
}

.thc-05 .thc-05__face::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(120% 60% at 50% 0%,oklch(0.5 0.12 150 / .35),transparent 60%);
}

.thc-05 .thc-05__mascot {
  position: absolute;
  top: -72px;
  left: 50%;
  width: 150px;
  height: 170px;
  translate: -50% 0;
  transform: translateZ(45px);
  transition: transform .6s cubic-bezier(.2,.9,.3,1.3);
  background: radial-gradient(60% 55% at 50% 32%,color-mix(in oklab,var(--skin) 90%,white) 0 58%,transparent 59%),radial-gradient(75% 48% at 50% 78%,var(--skin) 0 60%,transparent 61%);
  filter: drop-shadow(0 22px 18px rgba(0,0,0,.5));
}

.thc-05 .thc-05__card.is-live .thc-05__mascot {
  transform: translateZ(70px) scale(1.06);
}

.thc-05 .thc-05__eye {
  position: absolute;
  top: 44px;
  width: 13px;
  height: 18px;
  border-radius: 50%;
  background: oklch(0.2 0.02 200);
}

.thc-05 .thc-05__eye--l {
  left: 53px;
}

.thc-05 .thc-05__eye--r {
  right: 53px;
}

.thc-05 .thc-05__plate {
  position: absolute;
  left: 20px;
  right: 20px;
  bottom: 20px;
  transform: translateZ(30px);
}

.thc-05 .thc-05__name {
  font-size: 24px;
  font-weight: 800;
  color: #fff;
}

.thc-05 .thc-05__sub {
  font-size: 12.5px;
  color: rgba(255,255,255,.6);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-05 .thc-05__card,
    .thc-05__mascot {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-05 .thc-05__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 13;
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.classList.add('is-live'); // lifts the mascot to translateZ(70px)
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
