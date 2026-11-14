---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/masonry-grid-gallery/"
title: "Masonry Grid Gallery"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A Pinterest-style gallery skeleton in three CSS columns: tiles of varying heights (200, 350, 280px…) each washed with a different pastel oklch tint, so the…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Masonry Grid Gallery
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/masonry-grid-gallery/

A Pinterest-style gallery skeleton in three CSS columns: tiles of varying heights (200, 350, 280px…) each washed with a different pastel oklch tint, so the loading wall already feels like a curated moodboard. Demonstrates how skeletons handle non-uniform content — the case simple grids can't fake.
## HTML
```html
<section class="ssc-13" aria-label="Masonry gallery skeleton demo">
  <div class="ssc-13__wall" role="status" aria-busy="true">
    <span class="ssc-sr">Loading gallery…</span>
    <div class="ssc-13__cols" aria-hidden="true">
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 350);height:200px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 220);height:350px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 130);height:280px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 60);height:240px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 290);height:180px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 180);height:320px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 20);height:220px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 250);height:260px"></div>
      <div class="ssc-sk ssc-13__tile" style="--h:oklch(0.7 0.12 100);height:190px"></div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-13,
.ssc-13 *,
.ssc-13 *::before,
.ssc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-13 {
  --base: oklch(0.93 0.008 280);
  --sk-shine: rgba(255,255,255,.75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.975 0.005 280),oklch(0.95 0.01 290));
}

.ssc-13 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: color-mix(in oklab,var(--h,gray) 14%,var(--base));
  border-radius: 14px;
}

.ssc-13 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-13-shimmer 1.9s ease-in-out infinite;
}

@keyframes ssc-13-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-13 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-13 .ssc-13__wall {
  position: relative;
  width: min(560px,100%);
}

.ssc-13 .ssc-13__cols {
  columns: 3;
  column-gap: 14px;
}

.ssc-13 .ssc-13__tile {
  width: 100%;
  break-inside: avoid;
  margin-bottom: 14px;
  box-shadow: 0 10px 26px -20px oklch(0.4 0.05 285 / .6);
}

.ssc-13 .ssc-13__tile:nth-child(3n)::after {
  animation-delay: .15s;
}

.ssc-13 .ssc-13__tile:nth-child(3n+2)::after {
  animation-delay: .3s;
}

@media (max-width: 520px) {
  .ssc-13__cols {
    columns: 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ssc-13 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS columns + break-inside:avoid build the waterfall; per-tile color-mix washes make it a moodboard. */
```
