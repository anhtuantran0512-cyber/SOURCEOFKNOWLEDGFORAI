---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-card-with-hover-refraction/"
title: "Tailwind Liquid Glass Card with Hover Refraction"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "The premium product card, ported so the whole material is legible in one class list: backdrop-blur-[18px] backdrop-saturate-180 is the frost, bg-white/12…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Card with Hover Refraction
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-card-with-hover-refraction/

The premium product card, ported so the whole material is legible in one class list: backdrop-blur-[18px] backdrop-saturate-180 is the frost, bg-white/12 plus border-white/35 plus an inset hairline shadow is the thickness, and a before: radial gloss reads two custom properties the pointer handler writes. The 3D tilt is an arbitrary [transform:rotateX(var(--ry))_rotateY(var(--rx))], so the JS never touches a style beyond four variables.
## HTML
```html
<section class="lgt-01 grid w-full min-h-svh place-items-center p-15 font-lgt01-sans [perspective:1100px] bg-[image:url('https://picsum.photos/seed/lgcard/1200/900')] bg-cover bg-center bg-fixed" aria-label="Tailwind liquid glass card with hover refraction">
  <article id="lgt-01-card" tabindex="0" class="group relative isolate w-[min(340px,90vw)] cursor-pointer overflow-hidden rounded-[26px] border border-white/35 bg-white/12 p-6.5 pb-5.5 text-white backdrop-blur-[18px] backdrop-saturate-180 shadow-[0_30px_60px_-30px_rgba(0,0,0,.65),inset_0_1px_0_rgba(255,255,255,.5)] transition-[transform,box-shadow] duration-500 ease-lgt01 [transform-style:preserve-3d] [transform:rotateX(var(--ry,0deg))_rotateY(var(--rx,0deg))] hover:shadow-[0_40px_80px_-28px_rgba(0,0,0,.7),inset_0_1px_0_rgba(255,255,255,.6)] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-white/90 focus-visible:shadow-[0_40px_80px_-28px_rgba(0,0,0,.7),inset_0_1px_0_rgba(255,255,255,.6)] motion-reduce:transition-[box-shadow] motion-reduce:duration-200 before:pointer-events-none before:absolute before:inset-0 before:z-2 before:rounded-[inherit] before:transition-opacity before:duration-300 before:[background:radial-gradient(220px_220px_at_var(--mx,30%)_var(--my,20%),rgba(255,255,255,.55),rgba(255,255,255,0)_60%)] before:[opacity:var(--gloss,.5)] after:pointer-events-none after:absolute after:inset-0 after:z-1 after:rounded-[inherit] after:[background:linear-gradient(120deg,transparent_30%,rgba(255,255,255,.18)_46%,transparent_62%)] motion-reduce:after:hidden">
    <span class="relative z-3 inline-block rounded-full border border-white/40 bg-white/22 px-2.75 py-1.25 text-[11px] font-extrabold uppercase tracking-[0.12em]">New</span>
    <h3 class="relative z-3 mt-16 mb-2 text-2xl font-extrabold tracking-[-0.02em]">Aurora Headphones</h3>
    <p class="relative z-3 text-sm leading-relaxed text-white [text-shadow:0_1px_8px_rgba(0,0,0,.45)]">Spatial audio, 40-hour battery, and a machined-glass shell that catches the light like the UI around it.</p>
    <div class="relative z-3 mt-5 flex items-center justify-between">
      <span class="text-[22px] font-extrabold">$299</span>
      <span class="rounded-full bg-white/90 px-4 py-2 text-sm font-semibold text-lgt01-deep">View &rarr;</span>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-lgt01-deep: #1a1330;
  --color-lgt01-deep: oklch(0.26 0.07 300);
  --font-lgt01-sans: 'Manrope', system-ui, sans-serif;
  --ease-lgt01: cubic-bezier(0.2, 0.9, 0.2, 1);
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('#lgt-01-card');
  if (!card) return;
  const MAX_TILT = 8;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const onMove = e => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
    card.style.setProperty('--my', (py * 100).toFixed(1) + '%');
    card.style.setProperty('--gloss', '.85');
    if (reduce) return;
    card.style.setProperty('--rx', ((px - .5) * MAX_TILT * 2).toFixed(2) + 'deg');
    card.style.setProperty('--ry', (-(py - .5) * MAX_TILT * 2).toFixed(2) + 'deg');
  };
  const onLeave = () => {
    card.style.setProperty('--gloss', '.5');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  };
  card.addEventListener('pointermove', onMove);
  card.addEventListener('pointerleave', onLeave);
  card.cleanup = () => { card.removeEventListener('pointermove', onMove); card.removeEventListener('pointerleave', onLeave); };
})();
```
