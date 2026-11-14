---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-hover-zoom-in-card/"
title: "Tailwind Image Hover Zoom In Card"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The classic contained zoom, ported to one variant: overflow-hidden on the card and group-hover:scale-112 on the image, so the scale is clipped at the card…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Hover Zoom In Card
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-hover-zoom-in-card/

The classic contained zoom, ported to one variant: overflow-hidden on the card and group-hover:scale-112 on the image, so the scale is clipped at the card boundary and the grid never shifts. The hover state lives on the element that moves &mdash; not in a .card:hover .img rule several screens away.
## HTML
```html
<section class="tih-01 w-full min-h-svh grid place-items-center bg-tih01-bg font-tih01-sans px-6 py-10" aria-label="Image hover zoom-in card demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article class="group overflow-hidden rounded-2xl bg-tih01-card border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-450 ease-tih01 hover:shadow-[0_20px_60px_oklch(0.5_0.25_295/0.25)] hover:border-[oklch(0.55_0.22_295/0.35)] motion-reduce:transition-none">
      <div class="relative overflow-hidden aspect-[4/3]">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih01-observatory/800/600'),linear-gradient(135deg,oklch(0.19_0.11_300),oklch(0.35_0.2_295)_50%,oklch(0.6_0.12_220))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih01 group-hover:scale-112 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="p-4">
        <p class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih01-acc2">Explore</p>
        <h3 class="mb-1 text-sm font-semibold text-tih01-text"><a href="#deep-space" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih01-acc focus-visible:outline-offset-3">Deep Space Observatory</a></h3>
        <p class="text-xs text-tih01-muted">12 min read &middot; Cosmos</p>
      </div>
    </article>
    <article class="group overflow-hidden rounded-2xl bg-tih01-card border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-450 ease-tih01 hover:shadow-[0_20px_60px_oklch(0.5_0.25_295/0.25)] hover:border-[oklch(0.55_0.22_295/0.35)] motion-reduce:transition-none">
      <div class="relative overflow-hidden aspect-[4/3]">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih01-forest/800/600'),linear-gradient(135deg,oklch(0.18_0.05_250),oklch(0.34_0.07_250)_50%,oklch(0.42_0.11_160))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih01 group-hover:scale-112 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="p-4">
        <p class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih01-acc2">Nature</p>
        <h3 class="mb-1 text-sm font-semibold text-tih01-text"><a href="#forest-canopy" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih01-acc focus-visible:outline-offset-3">Ancient Forest Canopy</a></h3>
        <p class="text-xs text-tih01-muted">8 min read &middot; Biology</p>
      </div>
    </article>
    <article class="group overflow-hidden rounded-2xl bg-tih01-card border border-[oklch(1_0_0/0.06)] transition-[box-shadow,border-color] duration-450 ease-tih01 hover:shadow-[0_20px_60px_oklch(0.5_0.25_295/0.25)] hover:border-[oklch(0.55_0.22_295/0.35)] motion-reduce:transition-none">
      <div class="relative overflow-hidden aspect-[4/3]">
        <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih01-crystal/800/600'),linear-gradient(135deg,oklch(0.17_0.07_330),oklch(0.42_0.2_305)_50%,oklch(0.52_0.22_355))] bg-cover bg-center bg-no-repeat transition-transform duration-450 ease-tih01 group-hover:scale-112 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        </div>
      </div>
      <div class="p-4">
        <p class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih01-acc2">Design</p>
        <h3 class="mb-1 text-sm font-semibold text-tih01-text"><a href="#crystal" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih01-acc focus-visible:outline-offset-3">Crystal Formations</a></h3>
        <p class="text-xs text-tih01-muted">5 min read &middot; Art</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih01-bg: #0f0f13;
  --color-tih01-bg: oklch(0.16 0.008 285);
  --color-tih01-card: #1a1a24;
  --color-tih01-card: oklch(0.21 0.015 285);
  --color-tih01-text: #e2e8f0;
  --color-tih01-text: oklch(0.92 0.01 250);
  --color-tih01-muted: #94a3b8;
  --color-tih01-muted: oklch(0.7 0.03 250);
  --color-tih01-acc: #7c3aed;
  --color-tih01-acc: oklch(0.55 0.24 295);
  --color-tih01-acc2: #06b6d4;
  --color-tih01-acc2: oklch(0.71 0.14 205);
  --font-tih01-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih01: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-01 {
  width: 100%;
  min-height: 100svh;
}
/* Scoped selection colour and the Safari rounded-corner-with-transform shim:
   neither has a variant form. */

.tih-01 ::selection {
  background: oklch(0.55 0.24 295);
  color: #fff;
}

.tih-01 .group > div {
  -webkit-mask-image: -webkit-radial-gradient(white, black);
}
```
