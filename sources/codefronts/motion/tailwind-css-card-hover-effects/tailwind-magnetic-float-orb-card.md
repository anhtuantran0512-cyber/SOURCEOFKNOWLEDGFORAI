---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-magnetic-float-orb-card/"
title: "Tailwind Magnetic Float Orb Card with Pointer Attraction"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A glowing play-orb that leans toward the cursor as if caught in a magnetic field, over a faint tech grid."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Magnetic Float Orb Card with Pointer Attraction
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-magnetic-float-orb-card/

A glowing play-orb that leans toward the cursor as if caught in a magnetic field, over a faint tech grid. The pull is 20 lines of JS writing one transform; everything visible &mdash; grid, glow, spring reset &mdash; is utilities.
## HTML
```html
<section class="tch-23 w-full min-h-svh grid place-items-center bg-tch23-bg font-tch23-sans p-8">
  <article data-tch23="root" class="group relative w-[340px] h-[440px] rounded-[26px] overflow-hidden cursor-pointer bg-[radial-gradient(circle_at_50%_0%,#1c2540,#0a0d1a)] border border-tch23-acc/12">
    <div class="absolute inset-0 bg-[linear-gradient(rgb(120_160_255/0.06)_1px,transparent_1px),linear-gradient(90deg,rgb(120_160_255/0.06)_1px,transparent_1px)] bg-[length:28px_28px]"></div>
    <div data-tch23="orb" class="absolute top-1/2 left-1/2 z-3 grid place-items-center size-[110px] -mt-[55px] -ml-[55px] rounded-full bg-[linear-gradient(145deg,#6a8cff,#b46aff)] text-white font-bold text-[0.95rem] tracking-[0.05em] shadow-[0_0_40px_rgb(120_140_255/0.5)] will-change-transform transition-[transform,box-shadow] duration-200 ease-[cubic-bezier(0.34,1.56,0.64,1)] group-hover:shadow-[0_0_60px_rgb(140_120_255/0.7)] motion-reduce:transition-none">PLAY ▶</div>
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch23-ink pointer-events-none">
      <span class="text-[0.72rem] tracking-[0.22em] uppercase text-tch23-mut">Interactive Demo</span>
      <h2 class="font-tch23-display font-bold text-[2.1rem] leading-[1.05]">Gravity<br>Synth</h2>
      <p class="text-[0.85rem] leading-[1.6] text-tch23-body">Move your cursor near the orb — it leans toward you like it's caught in your field.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch23-bg: #06060a;
  --color-tch23-bg: oklch(0.09 0.004 285);
  --color-tch23-ink: #e9eefc;
  --color-tch23-ink: oklch(0.94 0.01 265);
  --color-tch23-body: #93a0c4;
  --color-tch23-body: oklch(0.68 0.04 265);
  --color-tch23-mut: #6f8bd6;
  --color-tch23-mut: oklch(0.62 0.12 265);
  --color-tch23-acc: #78a0ff;
  --color-tch23-acc: oklch(0.72 0.15 265);
  --font-tch23-sans: 'Manrope', system-ui, sans-serif;
  --font-tch23-display: 'Unbounded', system-ui, sans-serif;
}

.tch-23 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-23');
  if (!root) return;
  const card = root.querySelector('[data-tch23="root"]');
  const orb = root.querySelector('[data-tch23="orb"]');
  if (!card || !orb) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let frame = 0;
  card.addEventListener('mousemove', (e) => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = card.getBoundingClientRect();
      const dx = (e.clientX - (r.left + r.width / 2)) * 0.4;
      const dy = (e.clientY - (r.top + r.height / 2)) * 0.4;
      orb.style.transform = 'translate(' + (dx) + 'px, ' + (dy) + 'px) scale(1.05)';
    });
  });
  card.addEventListener('mouseleave', () => {
    orb.style.transform = 'translate(0,0) scale(1)';
  });
})();
```
