---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-star-rating-logo-cloud/"
title: "Tailwind CSS Hero Section with Star Rating & Logo Cloud"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A Mediterranean social-proof hero — a review pill with avatar stack and stars above an olive serif headline, aubergine CTA, and an as featured in wordmark…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hero Section with Star Rating & Logo Cloud
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-star-rating-logo-cloud/

A Mediterranean social-proof hero — a review pill with avatar stack and stars above an olive serif headline, aubergine CTA, and an as featured in wordmark row set in distinct typefaces. Every proof point is real text, not an image.
## HTML
```html
<section class="ths-07 grid w-full min-h-svh place-items-center bg-ths07-bg bg-[radial-gradient(70%_60%_at_50%_0%,var(--color-ths07-glow),transparent_70%)] px-5 py-16 font-ths07-sans text-ths07-plum sm:px-14" aria-label="Hero with social proof">
  <div class="w-full max-w-[46rem] text-center">
    <div class="inline-flex items-center gap-3 rounded-full border border-ths07-line bg-white py-1.5 pr-4 pl-1.5 shadow-[0_6px_20px_-12px_rgb(107_30_74/0.4)]">
      <span class="flex -space-x-2" aria-hidden="true">
        <span class="grid size-7 place-items-center rounded-full bg-ths07-olive text-[10px] font-bold text-white ring-2 ring-white">LM</span>
        <span class="grid size-7 place-items-center rounded-full bg-ths07-wine text-[10px] font-bold text-white ring-2 ring-white">AR</span>
        <span class="grid size-7 place-items-center rounded-full bg-ths07-gold text-[10px] font-bold text-white ring-2 ring-white">JP</span>
      </span>
      <span role="img" aria-label="Rated 4.9 out of 5" class="text-sm tracking-[0.06em] text-ths07-gold">★★★★★</span>
      <span class="text-[13px] font-medium text-ths07-mut">4.9 from 12,400 reviews</span>
    </div>
    <h1 class="mt-7 font-ths07-serif text-[clamp(36px,5.8vw,64px)] leading-[1.05] font-semibold tracking-[-0.01em] text-balance text-ths07-olive">Recipes from <em class="text-ths07-wine">real grandmothers,</em> measured for real kitchens.</h1>
    <p class="mx-auto mt-5 max-w-[30rem] text-[17px] leading-relaxed text-pretty text-ths07-mut">Saved by 500,000 home cooks who never want to scroll past life stories again.</p>
    <div class="mt-8 flex flex-wrap justify-center gap-3">
      <a href="#start" class="inline-flex min-h-12 items-center rounded-md bg-ths07-wine px-7 text-sm font-bold tracking-[0.04em] text-ths07-bg transition hover:bg-ths07-deep focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths07-wine motion-reduce:transition-none">Open the cookbook</a>
      <a href="#sample" class="inline-flex min-h-12 items-center rounded-md border border-ths07-line bg-white/60 px-6 text-sm font-semibold text-ths07-plum transition hover:border-ths07-wine focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths07-wine">See a sample recipe</a>
    </div>
    <div class="mt-12 border-t border-ths07-line pt-6">
      <p class="text-[11px] font-semibold tracking-[0.2em] text-ths07-mut uppercase">As featured in</p>
      <ul class="mt-4 flex flex-wrap items-center justify-center gap-x-9 gap-y-3 text-ths07-mut" aria-label="Featured by">
        <li class="font-ths07-display text-xl font-bold">The Times</li>
        <li class="text-sm font-extrabold tracking-[0.3em]">BON APPÉTIT</li>
        <li class="font-ths07-serif text-2xl font-bold italic">Eater</li>
        <li class="font-ths07-display text-lg font-bold italic">The Guardian</li>
        <li class="text-sm font-semibold tracking-[0.12em] uppercase">Saveur</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths07-bg: #faf3e3;
  --color-ths07-bg: oklch(0.965 0.022 87.2);
  --color-ths07-glow: #f5e6c6;
  --color-ths07-glow: oklch(0.929 0.045 85.9);
  --color-ths07-line: #e2c89a;
  --color-ths07-line: oklch(0.844 0.067 81.7);
  --color-ths07-plum: #3a2845;
  --color-ths07-plum: oklch(0.311 0.056 311.9);
  --color-ths07-olive: #3a4f2a;
  --color-ths07-olive: oklch(0.4 0.064 132.8);
  --color-ths07-wine: #6b1e4a;
  --color-ths07-wine: oklch(0.373 0.119 349.2);
  --color-ths07-deep: #4a1232;
  --color-ths07-deep: oklch(0.289 0.092 349.2);
  --color-ths07-gold: #b07f1c;
  --color-ths07-gold: oklch(0.63 0.122 79.3);
  --color-ths07-mut: #5f5646;
  --color-ths07-mut: oklch(0.457 0.028 82);
  --font-ths07-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths07-display: 'Playfair Display', Georgia, serif;
  --font-ths07-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-07 {
  width: 100%;
  min-height: 100svh;
}
```
