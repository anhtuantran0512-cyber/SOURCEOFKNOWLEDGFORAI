---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-glassmorphism-overlay-on-image-hover/"
title: "Tailwind Glassmorphism Overlay on Image Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A frosted panel parked below the frame that rises into the card on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glassmorphism Overlay on Image Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-glassmorphism-overlay-on-image-hover/

A frosted panel parked below the frame that rises into the card on hover. Two backdrop utilities do the glass (backdrop-blur-xl backdrop-saturate-150), one arbitrary translate parks it, and the resting title fades out as the panel arrives &mdash; so the card never shows two competing labels mid-transition.
## HTML
```html
<section class="tih-09 w-full min-h-svh grid place-items-center bg-tih09-bg font-tih09-sans px-6 py-10" aria-label="Glassmorphism overlay on image hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-2xl aspect-[3/4]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih09-spring/600/800'),linear-gradient(145deg,oklch(0.16_0.07_310),oklch(0.28_0.13_290),oklch(0.4_0.19_295),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih09 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-4 bg-linear-[to_top,oklch(0_0_0/0.7),transparent]">
        <p class="text-[13px] font-semibold text-tih09-text transition-opacity duration-450 ease-tih09 group-hover:opacity-0 motion-reduce:transition-none motion-reduce:opacity-0">Spring Collection</p>
      </div>
      <div class="absolute inset-x-3 bottom-3 p-4 rounded-xl bg-[oklch(1_0_0/0.08)] backdrop-blur-xl backdrop-saturate-150 border border-[oklch(1_0_0/0.15)] opacity-0 [translate:0_calc(100%+16px)] transition-[translate,opacity] duration-450 ease-tih09 group-hover:translate-y-0 group-hover:opacity-100 focus-within:translate-y-0 focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
        <p class="mb-1.5 text-[9px] font-bold tracking-[0.12em] uppercase text-tih09-acc">Collection</p>
        <h3 class="mb-1 text-sm font-bold text-tih09-text">Spring Bloom 2026</h3>
        <p class="text-[11px] leading-[1.5] text-[oklch(0.96_0.005_250/0.7)]">Ethereal violet pieces inspired by cherry blossom season</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[10px] text-tih09-muted">24 pieces</span>
          <a href="#spring-bloom" class="text-[10px] font-bold tracking-[0.06em] text-tih09-acc no-underline rounded focus-visible:outline-2 focus-visible:outline-tih09-acc focus-visible:outline-offset-3">Explore &rarr;</a>
        </div>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-2xl aspect-[3/4]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih09-forest/600/800'),linear-gradient(145deg,oklch(0.2_0.05_165),oklch(0.35_0.09_163),oklch(0.55_0.13_163),oklch(0.8_0.14_163))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih09 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-4 bg-linear-[to_top,oklch(0_0_0/0.7),transparent]">
        <p class="text-[13px] font-semibold text-tih09-text transition-opacity duration-450 ease-tih09 group-hover:opacity-0 motion-reduce:transition-none motion-reduce:opacity-0">Earth Tones</p>
      </div>
      <div class="absolute inset-x-3 bottom-3 p-4 rounded-xl bg-[oklch(1_0_0/0.08)] backdrop-blur-xl backdrop-saturate-150 border border-[oklch(1_0_0/0.15)] opacity-0 [translate:0_calc(100%+16px)] transition-[translate,opacity] duration-450 ease-tih09 group-hover:translate-y-0 group-hover:opacity-100 focus-within:translate-y-0 focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
        <p class="mb-1.5 text-[9px] font-bold tracking-[0.12em] uppercase text-tih09-acc">Sustainable</p>
        <h3 class="mb-1 text-sm font-bold text-tih09-text">Forest Origins</h3>
        <p class="text-[11px] leading-[1.5] text-[oklch(0.96_0.005_250/0.7)]">Organic cotton pieces dyed with natural plant extracts</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[10px] text-tih09-muted">18 pieces</span>
          <a href="#forest-origins" class="text-[10px] font-bold tracking-[0.06em] text-tih09-acc no-underline rounded focus-visible:outline-2 focus-visible:outline-tih09-acc focus-visible:outline-offset-3">Explore &rarr;</a>
        </div>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-2xl aspect-[3/4]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih09-azure/600/800'),linear-gradient(145deg,oklch(0.17_0.08_265),oklch(0.32_0.14_262),oklch(0.45_0.2_260),oklch(0.72_0.14_255))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih09 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <div class="absolute inset-x-0 bottom-0 p-4 bg-linear-[to_top,oklch(0_0_0/0.7),transparent]">
        <p class="text-[13px] font-semibold text-tih09-text transition-opacity duration-450 ease-tih09 group-hover:opacity-0 motion-reduce:transition-none motion-reduce:opacity-0">Azure Line</p>
      </div>
      <div class="absolute inset-x-3 bottom-3 p-4 rounded-xl bg-[oklch(1_0_0/0.08)] backdrop-blur-xl backdrop-saturate-150 border border-[oklch(1_0_0/0.15)] opacity-0 [translate:0_calc(100%+16px)] transition-[translate,opacity] duration-450 ease-tih09 group-hover:translate-y-0 group-hover:opacity-100 focus-within:translate-y-0 focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
        <p class="mb-1.5 text-[9px] font-bold tracking-[0.12em] uppercase text-tih09-acc">Limited</p>
        <h3 class="mb-1 text-sm font-bold text-tih09-text">Azure Coast</h3>
        <p class="text-[11px] leading-[1.5] text-[oklch(0.96_0.005_250/0.7)]">Mediterranean-inspired linen pieces for summer living</p>
        <div class="flex items-center justify-between mt-2.5">
          <span class="text-[10px] text-tih09-muted">12 pieces</span>
          <a href="#azure-coast" class="text-[10px] font-bold tracking-[0.06em] text-tih09-acc no-underline rounded focus-visible:outline-2 focus-visible:outline-tih09-acc focus-visible:outline-offset-3">Explore &rarr;</a>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih09-bg: #060611;
  --color-tih09-bg: oklch(0.11 0.015 285);
  --color-tih09-text: #f1f5f9;
  --color-tih09-text: oklch(0.96 0.005 250);
  --color-tih09-muted: #94a3b8;
  --color-tih09-muted: oklch(0.7 0.03 250);
  --color-tih09-acc: #8b5cf6;
  --color-tih09-acc: oklch(0.62 0.21 295);
  --font-tih09-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih09: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-09 {
  width: 100%;
  min-height: 100svh;
}

.tih-09 ::selection {
  background: oklch(0.62 0.21 295 / 0.8);
  color: #fff;
}
```
