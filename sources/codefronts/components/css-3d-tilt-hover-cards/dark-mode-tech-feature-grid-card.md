---
source: "codefronts"
url: "https://codefronts.com/components/css-3d-tilt-hover-cards/dark-mode-tech-feature-grid-card/"
title: "Dark Mode Tech Feature Grid Card"
section: "components"
category: "css-3d-tilt-hover-cards"
category_name: "CSS 3D Tilt Hover Cards"
description: "The Vercel/Supabase-style feature grid: three near-black cards with a mouse-following border highlight — a radial light that lives IN the border ring and…"
has_js: "true"
---

Here's a working CSS 3D Tilt Hover Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Tech Feature Grid Card
Source: https://codefronts.com/components/css-3d-tilt-hover-cards/dark-mode-tech-feature-grid-card/

The Vercel/Supabase-style feature grid: three near-black cards with a mouse-following border highlight — a radial light that lives IN the border ring and travels along it as the cursor crosses the grid — plus a whisper of tilt (±5°). The technique is one ::before layer and two custom properties per card.
## HTML
```html
<section class="thc-06" aria-label="Dark tech feature grid tilt cards demo">
  <div class="thc-06__grid">
    <article class="thc-06__card" tabindex="0">
      <div class="thc-06__icon" aria-hidden="true"></div>
      <h3 class="thc-06__title">Edge Functions</h3>
      <p class="thc-06__body">Deploy globally in milliseconds. Zero cold starts, zero config.</p>
    </article>
    <article class="thc-06__card" tabindex="0">
      <div class="thc-06__icon" aria-hidden="true"></div>
      <h3 class="thc-06__title">Realtime Sync</h3>
      <p class="thc-06__body">Postgres changes stream to every client over WebSockets.</p>
    </article>
    <article class="thc-06__card" tabindex="0">
      <div class="thc-06__icon" aria-hidden="true"></div>
      <h3 class="thc-06__title">Row-Level Auth</h3>
      <p class="thc-06__body">Policies live next to your data. Security by default.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.thc-06,
.thc-06 *,
.thc-06 *::before,
.thc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.thc-06 {
  --edge: oklch(0.72 0.15 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: oklch(0.13 0.008 260);
}

.thc-06 .thc-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
  gap: 16px;
  width: min(720px,100%);
}

.thc-06 .thc-06__card {
  position: relative;
  padding: 24px 22px;
  border-radius: 16px;
  background: oklch(0.17 0.01 260);
  border: 1px solid rgba(255,255,255,.07);
  overflow: hidden;
  transform: perspective(1200px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));
  transition: transform .5s ease;
}

.thc-06 .thc-06__card.is-live {
  transition: transform .09s linear;
}

.thc-06 .thc-06__card:focus-visible {
  outline: 2px solid var(--edge);
  outline-offset: 3px;
}

.thc-06 .thc-06__card::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 1px;
  background: radial-gradient(220px circle at var(--px,-999px) var(--py,-999px),var(--edge),transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  pointer-events: none;
}

.thc-06 .thc-06__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(340px circle at var(--px,-999px) var(--py,-999px),color-mix(in oklab,var(--edge) 10%,transparent),transparent 70%);
  pointer-events: none;
}

.thc-06 .thc-06__icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(140deg,color-mix(in oklab,var(--edge) 45%,oklch(0.2 0.01 260)),oklch(0.22 0.02 260));
  border: 1px solid color-mix(in oklab,var(--edge) 35%,transparent);
}

.thc-06 .thc-06__title {
  margin-top: 16px;
  font-size: 15.5px;
  font-weight: 600;
  color: oklch(0.93 0.005 260);
}

.thc-06 .thc-06__body {
  margin-top: 7px;
  font-size: 13px;
  line-height: 1.55;
  color: oklch(0.62 0.01 260);
}

@media (prefers-reduced-motion: reduce) {
  .thc-06 .thc-06__card {
    transition: none;
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const grid = document.querySelector('.thc-06 .thc-06__grid');
  if (!grid) return;
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const cards = [...grid.querySelectorAll('.thc-06__card')];
  const MAX = 5; // dev-tool aesthetics: whisper, don't wobble
  grid.addEventListener('pointermove', (e) => {
    // One listener updates EVERY card, so the glow flows across gaps
    // and lights a neighbour's edge before the pointer arrives.
    cards.forEach((card) => {
      const r = card.getBoundingClientRect();
      const x = e.clientX - r.left, y = e.clientY - r.top;
      card.style.setProperty('--px', x.toFixed(1) + 'px');
      card.style.setProperty('--py', y.toFixed(1) + 'px');
      const inside = x >= 0 && x <= r.width && y >= 0 && y <= r.height;
      card.classList.toggle('is-live', inside);
      card.style.setProperty('--rx', inside ? ((0.5 - y / r.height) * MAX).toFixed(2) + 'deg' : '0deg');
      card.style.setProperty('--ry', inside ? ((x / r.width - 0.5) * MAX).toFixed(2) + 'deg' : '0deg');
    });
  });
  grid.addEventListener('pointerleave', () => {
    cards.forEach((card) => {
      card.classList.remove('is-live');
      card.style.setProperty('--px', '-999px');
      card.style.setProperty('--py', '-999px');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
