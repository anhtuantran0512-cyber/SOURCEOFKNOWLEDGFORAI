---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/media-player-album-art-hover-card/"
title: "Media Player Album Art Hover Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "A streaming-app album card driven by a requestAnimationFrame spring: instead of CSS transitions, the tilt is lerped every frame toward the pointer, so it…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media Player Album Art Hover Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/media-player-album-art-hover-card/

A streaming-app album card driven by a requestAnimationFrame spring: instead of CSS transitions, the tilt is lerped every frame toward the pointer, so it overshoots and settles like a physical object. On hover the play button and track controls surface from under the artwork at translateZ(50px).
## HTML
```html
<section class="thc-07" aria-label="Album art media player tilt card demo">
  <article class="thc-07__card" tabindex="0" aria-label="Midnight Static by Velvet Antenna">
    <div class="thc-07__art" aria-hidden="true"><img src="https://picsum.photos/seed/midnight-static/520/520" alt="" loading="lazy"><div class="thc-07__vinyl"></div></div>
    <div class="thc-07__tray">
      <button class="thc-07__play" type="button" aria-label="Play Midnight Static"><span class="thc-07__tri" aria-hidden="true"></span></button>
      <div class="thc-07__meta">
        <h3 class="thc-07__track">Midnight Static</h3>
        <p class="thc-07__artist">Velvet Antenna</p>
      </div>
      <button class="thc-07__like" type="button" aria-label="Like this track">&#9825;</button>
    </div>
  </article>
</section>
```
## CSS
```css
.thc-07,
.thc-07 *,
.thc-07 *::before,
.thc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-07 {
  --acc: oklch(0.75 0.16 340);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(90% 100% at 50% 110%,oklch(0.26 0.08 340 / .8),transparent 60%),oklch(0.14 0.015 300);
}

.thc-07 .thc-07__card {
  position: relative;
  width: min(280px,100%);
  border-radius: 20px;
  background: oklch(0.2 0.02 320);
  border: 1px solid rgba(255,255,255,.1);
  padding: 14px;
  transform: perspective(1000px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transform-style: preserve-3d;
  box-shadow: 0 30px 60px -28px rgba(0,0,0,.85);
  cursor: pointer;
}

.thc-07 .thc-07__card:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 4px;
}

.thc-07 .thc-07__art {
  position: relative;
  width: 100%;
  aspect-ratio: 1;
  border-radius: 14px;
  overflow: hidden;
  background: radial-gradient(70% 70% at 30% 25%,oklch(0.6 0.19 340),transparent 65%),radial-gradient(60% 60% at 75% 75%,oklch(0.45 0.15 280),transparent 65%),oklch(0.22 0.05 320);
  transform: translateZ(20px);
}

.thc-07 .thc-07__art img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thc-07 .thc-07__vinyl {
  position: absolute;
  right: -30%;
  top: 50%;
  width: 88%;
  aspect-ratio: 1;
  translate: 0 -50%;
  border-radius: 50%;
  background: repeating-radial-gradient(circle,oklch(0.16 0.01 300) 0 2px,oklch(0.2 0.015 300) 2px 4px);
  border: 14px solid transparent;
  transition: right .5s cubic-bezier(.2,.9,.3,1.2);
}

.thc-07 .thc-07__vinyl::after {
  content: "";
  position: absolute;
  inset: 36%;
  border-radius: 50%;
  background: var(--acc);
}

.thc-07 .thc-07__card.is-live .thc-07__vinyl {
  right: -16%;
}

.thc-07 .thc-07__tray {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 4px 4px;
  transform: translateZ(50px);
  opacity: .85;
  transition: opacity .3s ease;
}

.thc-07 .thc-07__card.is-live .thc-07__tray {
  opacity: 1;
}

.thc-07 .thc-07__play {
  width: 44px;
  height: 44px;
  flex-shrink: 0;
  border: none;
  border-radius: 50%;
  background: var(--acc);
  display: grid;
  place-items: center;
  cursor: pointer;
  box-shadow: 0 10px 22px -8px color-mix(in oklab,var(--acc) 80%,transparent);
  transition: transform .25s ease;
}

.thc-07 .thc-07__play:hover {
  transform: scale(1.08);
}

.thc-07 .thc-07__play:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.thc-07 .thc-07__tri {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 8px 0 8px 13px;
  border-color: transparent transparent transparent oklch(0.15 0.02 320);
  margin-left: 3px;
}

.thc-07 .thc-07__meta {
  flex: 1;
  min-width: 0;
}

.thc-07 .thc-07__track {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.thc-07 .thc-07__artist {
  font-size: 12px;
  color: rgba(255,255,255,.55);
  margin-top: 2px;
}

.thc-07 .thc-07__like {
  border: none;
  background: none;
  font-size: 20px;
  color: rgba(255,255,255,.6);
  cursor: pointer;
  transition: color .2s ease;
}

.thc-07 .thc-07__like:hover {
  color: var(--acc);
}

.thc-07 .thc-07__like:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .thc-07 .thc-07__vinyl {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('.thc-07 .thc-07__card');
  if (!card) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const MAX = 12, EASE = 0.12; // EASE is the spring: 0.08 heavy, 0.2 snappy
  let tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
  const tick = () => {
    cx += (tx - cx) * EASE;
    cy += (ty - cy) * EASE;
    card.style.setProperty('--rx', cx.toFixed(3) + 'deg');
    card.style.setProperty('--ry', cy.toFixed(3) + 'deg');
    // Self-suspend when settled — idle cost drops to zero.
    raf = (Math.abs(tx - cx) > 0.01 || Math.abs(ty - cy) > 0.01)
      ? requestAnimationFrame(tick) : null;
  };
  const wake = () => { if (!raf) raf = requestAnimationFrame(tick); };
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    tx = (0.5 - (e.clientY - r.top) / r.height) * MAX;
    ty = ((e.clientX - r.left) / r.width - 0.5) * MAX;
    card.classList.add('is-live');
    wake();
  });
  card.addEventListener('pointerleave', () => {
    tx = 0; ty = 0;                 // spring home along the same physics
    card.classList.remove('is-live');
    wake();
  });
})();
```
