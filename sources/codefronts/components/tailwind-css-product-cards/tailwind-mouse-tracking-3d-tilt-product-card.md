---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-mouse-tracking-3d-tilt-product-card/"
title: "Tailwind Mouse-Tracking 3D Tilt Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The VanillaTilt look with no library: a pointer handler writes four custom properties and every visual reads them through arbitrary utilities."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mouse-Tracking 3D Tilt Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-mouse-tracking-3d-tilt-product-card/

The VanillaTilt look with no library: a pointer handler writes four custom properties and every visual reads them through arbitrary utilities. The card rotates toward the cursor, a specular glare tracks the pointer in mix-blend-mode: screen, and the whole thing no-ops on touch and under reduced motion — a rare case where the JS is genuinely just a data source.
## HTML
```html
<section class="tpc-04 w-full min-h-svh grid place-items-center bg-tpc04-bg font-tpc04-sans px-5 py-14 [perspective:900px]" aria-label="Mouse-tracking 3D tilt product card demo">
  <article class="group relative w-80 max-w-full rounded-[20px] overflow-hidden border border-tpc04-edge bg-linear-[160deg,var(--color-tpc04-card),var(--color-tpc04-card2)] shadow-[0_30px_60px_-30px_oklch(0.1_0.02_285/0.8)] transform-3d [transform:rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,box-shadow] duration-400 ease-out motion-reduce:[transform:none] motion-reduce:transition-none">
    <span aria-hidden="true" class="pointer-events-none absolute inset-0 z-3 opacity-0 transition-opacity duration-300 bg-[radial-gradient(320px_320px_at_var(--mx,50%)_var(--my,50%),oklch(1_0_0/0.22),transparent_60%)] mix-blend-screen group-hover:opacity-100 motion-reduce:hidden"></span>
    <div role="img" aria-label="Product photo: Nova 75 mechanical keyboard" class="aspect-[16/11] bg-linear-[135deg,var(--color-tpc04-ph),var(--color-tpc04-ph2)] bg-[url('https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&h=560&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="px-5.5 pt-5 pb-5.5">
      <p class="font-tpc04-mono text-[11px] tracking-[0.2em] uppercase text-tpc04-acc">Nova Labs</p>
      <h3 class="mt-1.5 text-[18px] font-semibold leading-[1.3] text-tpc04-ink text-pretty">Nova 75 Mechanical Keyboard</h3>
      <div class="mt-4 flex items-center justify-between gap-3">
        <p class="text-[20px] font-bold text-tpc04-hi tabular-nums">$219</p>
        <button type="button" class="min-h-11 h-11 px-5.5 rounded-xl border-0 bg-tpc04-acc text-tpc04-onacc text-sm font-bold cursor-pointer shadow-[0_0_22px_-6px_var(--color-tpc04-acc)] transition-[filter,scale] duration-200 hover:brightness-110 active:scale-97 focus-visible:outline-3 focus-visible:outline-tpc04-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Buy Now</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc04-bg: #0a0810;
  --color-tpc04-bg: oklch(0.14 0.02 290);
  --color-tpc04-card: #1b1730;
  --color-tpc04-card: oklch(0.24 0.04 290);
  --color-tpc04-card2: #12101d;
  --color-tpc04-card2: oklch(0.18 0.03 290);
  --color-tpc04-edge: #332c4d;
  --color-tpc04-edge: oklch(0.32 0.04 290);
  --color-tpc04-ph: #2a2440;
  --color-tpc04-ph: oklch(0.3 0.04 290);
  --color-tpc04-ph2: #1a1730;
  --color-tpc04-ph2: oklch(0.23 0.04 290);
  --color-tpc04-ink: #f2f0fb;
  --color-tpc04-ink: oklch(0.95 0.01 290);
  --color-tpc04-hi: #ffffff;
  --color-tpc04-hi: oklch(1 0 0);
  --color-tpc04-acc: #a68cf5;
  --color-tpc04-acc: oklch(0.72 0.17 285);
  --color-tpc04-onacc: #0a0616;
  --color-tpc04-onacc: oklch(0.14 0.03 290);
  --color-tpc04-ring: #c7b6ff;
  --color-tpc04-ring: oklch(0.82 0.1 285);
  --font-tpc04-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpc04-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Registered angles: an unregistered custom property is a string to the animation
   engine, so the card would snap back to rest instead of easing. @property is a
   rule, not a utility — this cannot move into the markup. */

@property --rx {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

@property --ry {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

.tpc-04 {
  width: 100%;
  min-height: 100svh;
}

.tpc-04 ::selection {
  background: var(--color-tpc04-acc);
  color: #0a0616;
}
/* The touch guard, in CSS as well as in the script: a (hover:none) device fires
   pointermove on drag, and a card nobody asked to tilt should not tilt. */

@media (hover: none) {
  .tpc-04 article {
    transform: none !important;
    transition: none;
  }

  .tpc-04 article > span[aria-hidden] {
    display: none;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.tpc-04 > article').forEach(function (card) {
    if (card.dataset.bound) return; card.dataset.bound = '1';
    if (matchMedia('(hover:none)').matches || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
    var MAX = 12; // max tilt in degrees
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect();
      var px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--ry', ((px - 0.5) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--rx', ((0.5 - py) * 2 * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
      card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    });
    card.addEventListener('pointerleave', function () {
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
