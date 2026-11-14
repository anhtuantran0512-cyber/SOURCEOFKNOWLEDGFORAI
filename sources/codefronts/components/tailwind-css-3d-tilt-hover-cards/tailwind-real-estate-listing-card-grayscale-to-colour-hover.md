---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-real-estate-listing-card-grayscale-to-colour-hover/"
title: "Tailwind Real Estate Listing Card with Grayscale-to-Colour Hover"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "A luxury listing built on absence: white space, one hairline rule, Instrument Serif numerals — and a photo that lives in grayscale until hover develops the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Real Estate Listing Card with Grayscale-to-Colour Hover
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-real-estate-listing-card-grayscale-to-colour-hover/

A luxury listing built on absence: white space, one hairline rule, Instrument Serif numerals — and a photo that lives in grayscale until hover develops the colour over 700ms while the card tilts a fluid ±7°. The port fixes the structure: the card is no longer one giant link, so a real Save toggle can sit on the photo, and the address is a stretched link.
## HTML
```html
<section class="ttc-11 w-full min-h-svh grid place-items-center bg-ttc11-bg px-6 py-14 font-ttc11-sans text-ttc11-ink" aria-label="Real estate listing card with grayscale-to-colour hover demo">
  <div class="grid w-full justify-items-center gap-8">
    <article data-ttc11-card class="group/card relative w-full max-w-[20rem] overflow-hidden border border-ttc11-line bg-white shadow-[0_20px_50px_-34px_var(--color-ttc11-shadow)] [transform:perspective(1200px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))] transition-[transform,box-shadow] duration-750 ease-[cubic-bezier(0.2,0.8,0.2,1)] data-live:duration-100 data-live:ease-linear data-live:shadow-[0_34px_64px_-30px_var(--color-ttc11-shadow)] motion-reduce:transition-none has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-6 has-[a:focus-visible]:outline-ttc11-ink">
      <div aria-hidden="true" class="aspect-[4/3] overflow-hidden bg-ttc11-line">
        <img class="size-full object-cover grayscale contrast-105 transition-[filter] duration-700 ease-out group-data-live/card:grayscale-0 group-data-live/card:contrast-100 group-has-[a:focus-visible]/card:grayscale-0 pointer-coarse:grayscale-0 motion-reduce:transition-none" src="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?q=80&w=640&auto=format&fit=crop" alt="" loading="lazy">
      </div>
      <button data-save type="button" aria-pressed="false" aria-label="Save 142 Cliffside Terrace" class="group/save absolute top-3 right-3 z-20 grid size-11 cursor-pointer place-items-center rounded-full bg-white/90 text-ttc11-ink shadow-sm backdrop-blur-sm transition-colors hover:bg-white aria-pressed:text-ttc11-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttc11-ink">
        <svg aria-hidden="true" viewBox="0 0 24 24" class="size-[18px] fill-none group-aria-pressed/save:fill-current" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 20s-7.5-4.6-7.5-10.1A4.4 4.4 0 0 1 12 7.3a4.4 4.4 0 0 1 7.5 2.6C19.5 15.4 12 20 12 20z"/></svg>
      </button>
      <div class="px-6 pt-5 pb-6">
        <div class="flex items-baseline justify-between gap-3">
          <p class="font-ttc11-serif text-[32px] leading-none tracking-[-0.01em] lining-nums">$2,450,000</p>
          <span class="text-[10px] font-bold tracking-[0.2em] text-ttc11-mut">FOR SALE</span>
        </div>
        <h3 class="mt-2 text-[13.5px] font-medium text-ttc11-mut"><a href="#" class="no-underline text-inherit outline-none after:absolute after:inset-0 after:z-10 after:content-[''] hover:text-ttc11-ink">142 Cliffside Terrace, Byron Bay</a></h3>
        <dl class="mt-5 grid grid-cols-4 border-t border-ttc11-line pt-4 text-center">
          <div><dt class="text-[9.5px] font-semibold tracking-[0.16em] text-ttc11-mut">BEDS</dt><dd class="mt-1 text-sm font-semibold">4</dd></div>
          <div><dt class="text-[9.5px] font-semibold tracking-[0.16em] text-ttc11-mut">BATHS</dt><dd class="mt-1 text-sm font-semibold">3</dd></div>
          <div><dt class="text-[9.5px] font-semibold tracking-[0.16em] text-ttc11-mut">AREA</dt><dd class="mt-1 text-sm font-semibold">380 m²</dd></div>
          <div><dt class="text-[9.5px] font-semibold tracking-[0.16em] text-ttc11-mut">VIEW</dt><dd class="mt-1 text-sm font-semibold">Ocean</dd></div>
        </dl>
      </div>
    </article>
    <p aria-hidden="true" class="rounded-full border border-ttc11-line bg-white px-3.5 py-2 font-ttc11-mono text-[11.5px] text-ttc11-mut">grayscale → group-data-live/card:grayscale-0 · stretched link</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc11-bg: #f4f3ef;
  --color-ttc11-bg: oklch(0.965 0.004 90);
  --color-ttc11-line: #e6e4de;
  --color-ttc11-line: oklch(0.915 0.006 90);
  --color-ttc11-ink: #1f1b17;
  --color-ttc11-ink: oklch(0.22 0.01 60);
  --color-ttc11-mut: #625a52;
  --color-ttc11-mut: oklch(0.47 0.015 60);
  --color-ttc11-acc: #c2413a;
  --color-ttc11-acc: oklch(0.56 0.17 27);
  --color-ttc11-shadow: #3d34297f;
  --color-ttc11-shadow: oklch(0.3 0.02 60 / 0.5);
  --font-ttc11-serif: 'Instrument Serif', Georgia, serif;
  --font-ttc11-sans: 'Manrope', system-ui, sans-serif;
  --font-ttc11-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-11 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc11-card]').forEach((card) => {
    if (card.dataset.wired) return;
    card.dataset.wired = '1';
    const save = card.querySelector('[data-save]');
    save.addEventListener('click', () => {
      save.setAttribute('aria-pressed', String(save.getAttribute('aria-pressed') !== 'true'));
    });
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 7; // fluid but unhurried: match the brand's pace
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
      card.setAttribute('data-live', ''); // develops the photo from grayscale to colour
    });
    card.addEventListener('pointerleave', () => {
      card.removeAttribute('data-live');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });
})();
```
