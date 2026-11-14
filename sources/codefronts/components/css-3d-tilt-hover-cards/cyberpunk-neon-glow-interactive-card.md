---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/cyberpunk-neon-glow-interactive-card/"
title: "Cyberpunk Neon Glow Interactive Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "An event-promo card whose neon reacts physically: the magenta/cyan box-shadow's offset is computed FROM the tilt — light the card banks away from throws a…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Glow Interactive Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/cyberpunk-neon-glow-interactive-card/

An event-promo card whose neon reacts physically: the magenta/cyan box-shadow's offset is computed FROM the tilt — light the card banks away from throws a longer glow on the opposite side, like a sign swinging in front of a wall. A scanline overlay and flickering border finish the Night City read.
## HTML
```html
<section class="thc-09" aria-label="Cyberpunk neon glow tilt card demo">
  <article class="thc-09__card" tabindex="0" aria-label="Neon District live event, October 31, Sector 7 warehouse">
    <div class="thc-09__scan" aria-hidden="true"></div>
    <p class="thc-09__kicker">LIVE // 10.31</p>
    <h3 class="thc-09__title">NEON<br>DISTRICT</h3>
    <p class="thc-09__sub">Sector 7 Warehouse &middot; Doors 23:00</p>
    <button class="thc-09__cta" type="button">Claim Access</button>
  </article>
</section>
```
## CSS
```css
.thc-09,
.thc-09 *,
.thc-09 *::before,
.thc-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-09 {
  --pink: oklch(0.68 0.26 350);
  --cyan: oklch(0.78 0.15 200);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 32px;
  background: radial-gradient(100% 100% at 50% 120%,oklch(0.2 0.07 330 / .7),transparent 60%),oklch(0.11 0.015 300);
}

.thc-09 .thc-09__card {
  position: relative;
  width: min(300px,100%);
  padding: 30px 28px;
  border-radius: 14px;
  overflow: hidden;
  background: linear-gradient(165deg,oklch(0.17 0.03 320),oklch(0.13 0.02 300));
  border: 1.5px solid var(--pink);
  transform: perspective(1000px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transition: transform .55s cubic-bezier(.2,.9,.3,1.15),box-shadow .55s ease;
  box-shadow: var(--gx,0px) var(--gy,10px) 34px -6px color-mix(in oklab,var(--pink) 55%,transparent),calc(var(--gx,0px) * -1) calc(var(--gy,10px) * -1) 34px -6px color-mix(in oklab,var(--cyan) 45%,transparent);
  animation: thc-09-flicker 4.5s steps(1) infinite;
  cursor: pointer;
}

.thc-09 .thc-09__card.is-live {
  transition: transform .08s linear,box-shadow .08s linear;
}

.thc-09 .thc-09__card:focus-visible {
  outline: 3px solid var(--cyan);
  outline-offset: 5px;
}

@keyframes thc-09-flicker {
  0%,
    100% {
    border-color: var(--pink);
  }

  7% {
    border-color: color-mix(in oklab,var(--pink) 55%,transparent);
  }

  8% {
    border-color: var(--pink);
  }

  54% {
    border-color: color-mix(in oklab,var(--pink) 70%,transparent);
  }

  56% {
    border-color: var(--pink);
  }
}

.thc-09 .thc-09__scan {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,rgba(255,255,255,.055) 0 1px,transparent 1px 3px);
  animation: thc-09-drift 9s linear infinite;
}

@keyframes thc-09-drift {
  100% {
    transform: translateY(3px);
  }
}

.thc-09 .thc-09__kicker {
  font: 700 11px ui-monospace,'Cascadia Code',monospace;
  letter-spacing: .22em;
  color: var(--cyan);
}

.thc-09 .thc-09__title {
  margin-top: 14px;
  font-size: 40px;
  line-height: .95;
  font-weight: 900;
  letter-spacing: .02em;
  color: #fff;
  text-shadow: 0 0 18px color-mix(in oklab,var(--pink) 70%,transparent);
}

.thc-09 .thc-09__sub {
  margin-top: 12px;
  font-size: 12.5px;
  color: rgba(255,255,255,.6);
}

.thc-09 .thc-09__cta {
  margin-top: 24px;
  width: 100%;
  height: 42px;
  border-radius: 8px;
  font: 700 12px ui-monospace,monospace;
  letter-spacing: .14em;
  color: var(--pink);
  background: transparent;
  border: 1.5px solid var(--pink);
  cursor: pointer;
  transition: background .2s ease,color .2s ease;
}

.thc-09 .thc-09__cta:hover {
  background: var(--pink);
  color: oklch(0.12 0.02 300);
}

.thc-09 .thc-09__cta:focus-visible {
  outline: 3px solid var(--cyan);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-09 .thc-09__card {
    transition: none;
    animation: none;
  }

  .thc-09__scan {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-09 .thc-09__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 12, GLOW = 1.6; // px of shadow throw per degree of tilt
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    const rx = (0.5 - (e.clientY - r.top) / r.height) * MAX;
    const ry = ((e.clientX - r.left) / r.width - 0.5) * MAX;
    card.style.setProperty('--rx', rx.toFixed(2) + 'deg');
    card.style.setProperty('--ry', ry.toFixed(2) + 'deg');
    // Glow throws OPPOSITE the bank — a sign swinging in front of a wall.
    card.style.setProperty('--gx', (-ry * GLOW).toFixed(1) + 'px');
    card.style.setProperty('--gy', (rx * GLOW).toFixed(1) + 'px');
    card.classList.add('is-live');
  });
  card.addEventListener('pointerleave', () => {
    card.classList.remove('is-live');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
    card.style.setProperty('--gx', '0px');
    card.style.setProperty('--gy', '10px');
  });
})();
```
