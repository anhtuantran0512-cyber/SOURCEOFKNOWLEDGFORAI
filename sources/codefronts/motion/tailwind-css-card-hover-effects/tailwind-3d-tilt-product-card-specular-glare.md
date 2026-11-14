---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-tilt-product-card-specular-glare/"
title: "Tailwind 3D Tilt Product Card with Specular Glare"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The simpler cousin of demo 01: one flat surface that leans toward the cursor, a specular glare that tracks the pointer, and text pushed onto four translateZ…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Product Card with Specular Glare
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-3d-tilt-product-card-specular-glare/

The simpler cousin of demo 01: one flat surface that leans toward the cursor, a specular glare that tracks the pointer, and text pushed onto four translateZ planes so the type floats above the face. Fewer moving parts, and the whole thing is one 20-line handler.
## HTML
```html
<section class="tch-17 w-full min-h-svh grid place-items-center bg-[radial-gradient(circle_at_70%_30%,#2a1f4d,#0d0a1a_70%)] font-tch17-sans p-8 [perspective:1100px]">
  <article data-tch17="root" tabindex="0" class="group relative w-[330px] h-[440px] rounded-3xl cursor-pointer outline-none transform-3d bg-[linear-gradient(150deg,#3a2b6e,#18122e)] border border-white/8 shadow-[0_25px_50px_rgb(0_0_0/0.5)] transition-transform duration-100 ease-out focus-visible:outline-3 focus-visible:outline-tch17-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
    <div class="absolute inset-0 z-5 rounded-[inherit] pointer-events-none opacity-0 transition-opacity duration-300 bg-[radial-gradient(circle_at_var(--tch17-gx,50%)_var(--tch17-gy,50%),rgb(255_255_255/0.28),transparent_45%)] group-hover:opacity-100"></div>
    <div class="h-full p-[2.4rem] flex flex-col justify-between text-tch17-ink">
      <span class="self-start text-[0.7rem] tracking-[0.18em] uppercase px-3.5 py-1.5 border border-white/25 rounded-full text-tch17-mut [transform:translateZ(60px)]">Limited Drop</span>
      <h2 class="font-tch17-display font-bold text-[2.8rem] leading-[0.95] [transform:translateZ(80px)]">Nimbus<br>Hi-Tops</h2>
      <p class="text-[0.85rem] leading-[1.6] text-tch17-body [transform:translateZ(40px)]">Float-foam midsole and an iridescent upper that shifts as it turns in the light.</p>
      <span class="font-tch17-display font-semibold text-[1.6rem] text-tch17-acc [transform:translateZ(70px)]">$189</span>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch17-ink: #ede9ff;
  --color-tch17-ink: oklch(0.94 0.02 285);
  --color-tch17-body: #b3a9d6;
  --color-tch17-body: oklch(0.75 0.05 290);
  --color-tch17-mut: #c5b8ff;
  --color-tch17-mut: oklch(0.82 0.08 290);
  --color-tch17-acc: #9d7bff;
  --color-tch17-acc: oklch(0.68 0.19 290);
  --font-tch17-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tch17-display: 'Syne', system-ui, sans-serif;
}

.tch-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tch-17');
  if (!root) return;
  const card = root.querySelector('[data-tch17="root"]');
  if (!card) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let frame = 0;
  card.addEventListener('mousemove', (e) => {
    if (frame) return;
    frame = requestAnimationFrame(() => {
      frame = 0;
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width;
      const py = (e.clientY - r.top) / r.height;
      card.style.transform = 'rotateY(' + ((px - 0.5) * 20) + 'deg) rotateX(' + ((0.5 - py) * 20) + 'deg)';
      card.style.setProperty('--tch17-gx', '' + (px * 100) + '%');
      card.style.setProperty('--tch17-gy', '' + (py * 100) + '%');
    });
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateY(0deg) rotateX(0deg)';
  });
})();
```
