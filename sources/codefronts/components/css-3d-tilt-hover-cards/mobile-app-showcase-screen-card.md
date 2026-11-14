---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/mobile-app-showcase-screen-card/"
title: "Mobile App Showcase Screen Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "An app-landing-page hero card: a CSS-drawn phone hovers at a resting 3D angle inside the card, straightening toward the viewer as the cursor approaches…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile App Showcase Screen Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/mobile-app-showcase-screen-card/

An app-landing-page hero card: a CSS-drawn phone hovers at a resting 3D angle inside the card, straightening toward the viewer as the cursor approaches centre, while a rating pill and a downloads badge orbit at translateZ(70px) and a specular streak sweeps the screen glass. High perspective depth, floating chrome — the App Store screenshot, weaponized.
## HTML
```html
<section class="thc-13" aria-label="Mobile app showcase tilt card demo">
  <article class="thc-13__card" tabindex="0" aria-label="Tidepool app: 4.9 stars, 2 million downloads">
    <div class="thc-13__copy">
      <h3 class="thc-13__name">Tidepool</h3>
      <p class="thc-13__pitch">Sleep sounds, tuned to your night.</p>
    </div>
    <div class="thc-13__stage" aria-hidden="true">
      <div class="thc-13__phone">
        <span class="thc-13__notch"></span>
        <div class="thc-13__screen"><i></i><i></i><i></i></div>
      </div>
      <span class="thc-13__badge thc-13__badge--rating">&#9733; 4.9</span>
      <span class="thc-13__badge thc-13__badge--dl">2M+ downloads</span>
    </div>
  </article>
</section>
```
## CSS
```css
.thc-13,
.thc-13 *,
.thc-13 *::before,
.thc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-13 {
  --acc: oklch(0.72 0.13 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 100% at 20% 0%,oklch(0.26 0.06 240 / .9),transparent 60%),oklch(0.15 0.02 250);
}

.thc-13 .thc-13__card {
  position: relative;
  width: min(320px,100%);
  padding: 26px 26px 0;
  border-radius: 24px;
  overflow: hidden;
  background: linear-gradient(170deg,oklch(0.22 0.04 235),oklch(0.16 0.025 250));
  border: 1px solid rgba(255,255,255,.1);
  transform: perspective(1400px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  transition: transform .6s cubic-bezier(.2,.9,.3,1.1);
  box-shadow: 0 32px 64px -28px rgba(0,0,0,.85);
  cursor: pointer;
}

.thc-13 .thc-13__card.is-live {
  transition: transform .08s linear;
}

.thc-13 .thc-13__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 4px;
}

.thc-13 .thc-13__name {
  font-size: 22px;
  font-weight: 800;
  color: #fff;
  transform: translateZ(30px);
}

.thc-13 .thc-13__pitch {
  font-size: 13px;
  color: rgba(255,255,255,.6);
  margin-top: 4px;
  transform: translateZ(30px);
}

.thc-13 .thc-13__stage {
  position: relative;
  height: 260px;
  margin-top: 18px;
  transform-style: preserve-3d;
}

.thc-13 .thc-13__phone {
  position: absolute;
  left: 50%;
  bottom: -40px;
  width: 150px;
  height: 300px;
  margin-left: -75px;
  border-radius: 28px;
  padding: 9px;
  background: oklch(0.25 0.02 250);
  border: 1px solid rgba(255,255,255,.18);
  transform: translateZ(40px) rotateY(calc(-18deg + var(--ry,0deg) * 1.4)) rotateX(calc(8deg + var(--rx,0deg) * .6));
  transition: transform .6s cubic-bezier(.2,.9,.3,1.1);
  box-shadow: 24px 30px 50px -20px rgba(0,0,0,.7);
}

.thc-13 .thc-13__card.is-live .thc-13__phone {
  transition: transform .08s linear;
}

.thc-13 .thc-13__notch {
  position: absolute;
  top: 16px;
  left: 50%;
  translate: -50% 0;
  width: 44px;
  height: 9px;
  border-radius: 999px;
  background: oklch(0.12 0.01 250);
  z-index: 2;
}

.thc-13 .thc-13__screen {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  overflow: hidden;
  background: linear-gradient(190deg,oklch(0.45 0.12 230),oklch(0.22 0.06 260));
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 34px 10px 10px;
}

.thc-13 .thc-13__screen i {
  display: block;
  border-radius: 8px;
  background: rgba(255,255,255,.14);
}

.thc-13 .thc-13__screen i:nth-child(1) {
  height: 42%;
}

.thc-13 .thc-13__screen i:nth-child(2) {
  height: 16%;
  background: rgba(255,255,255,.22);
}

.thc-13 .thc-13__screen i:nth-child(3) {
  height: 16%;
}

.thc-13 .thc-13__screen::after {
  content: "";
  position: absolute;
  inset: -60%;
  background: linear-gradient(115deg,transparent 44%,rgba(255,255,255,.28) 50%,transparent 56%);
  transform: translateX(-70%);
  transition: transform .9s ease;
}

.thc-13 .thc-13__card.is-live .thc-13__screen::after {
  transform: translateX(55%);
}

.thc-13 .thc-13__badge {
  position: absolute;
  font: 700 11px 'Segoe UI',sans-serif;
  color: #fff;
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.2);
  border-radius: 999px;
  padding: 8px 13px;
  transform: translateZ(70px);
}

.thc-13 .thc-13__badge--rating {
  top: 22px;
  left: 8px;
  animation: thc-13-bob 3.4s ease-in-out infinite;
}

.thc-13 .thc-13__badge--dl {
  top: 110px;
  right: 0;
  animation: thc-13-bob 3.4s ease-in-out -1.7s infinite;
}

@keyframes thc-13-bob {
  50% {
    margin-top: -7px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .thc-13 .thc-13__card,
    .thc-13__phone,
    .thc-13__screen::after {
    transition: none;
  }

  .thc-13__badge {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-13 .thc-13__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 9; // the phone amplifies this 1.4x via its calc() pose
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
    card.classList.add('is-live'); // also fires the specular sweep across the glass
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
