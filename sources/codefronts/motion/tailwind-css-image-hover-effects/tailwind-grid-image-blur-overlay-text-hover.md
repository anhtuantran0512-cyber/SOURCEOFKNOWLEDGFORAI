---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-grid-image-blur-overlay-text-hover/"
title: "Tailwind Grid Image Blur Overlay Text Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Blur the image through the overlay rather than blurring the image: group-hover:backdrop-blur-lg plus group-hover:backdrop-brightness-60, which is the port's…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Grid Image Blur Overlay Text Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-grid-image-blur-overlay-text-hover/

Blur the image through the overlay rather than blurring the image: group-hover:backdrop-blur-lg plus group-hover:backdrop-brightness-60, which is the port's cleanest single win &mdash; Tailwind ships composable backdrop-filter utilities, so a two-function filter stack that was one hand-written declaration is now two named utilities that read like the intent.
## HTML
```html
<section class="tih-04 w-full min-h-svh grid place-items-center bg-tih04-bg font-tih04-sans px-6 py-10" aria-label="Backdrop blur overlay text hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-[14px] aspect-[3/4]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih04-canvas/600/800'),linear-gradient(135deg,oklch(0.17_0.07_285),oklch(0.34_0.12_285),oklch(0.28_0.06_290))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih04 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 flex flex-col justify-end p-5 bg-transparent backdrop-blur-none backdrop-brightness-100 transition-[backdrop-filter,background-color] duration-400 ease-tih04 group-hover:bg-[oklch(0_0_0/0.15)] group-hover:backdrop-blur-lg group-hover:backdrop-brightness-60 motion-reduce:transition-none motion-reduce:bg-[oklch(0_0_0/0.15)] motion-reduce:backdrop-blur-lg motion-reduce:backdrop-brightness-60">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih04-acc opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Editorial</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih04-text opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#infinite-canvas" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih04-acc focus-visible:outline-offset-3">The Infinite Canvas</a></h3>
        <p style="--i:2" class="mt-1.25 text-[11px] text-tih04-muted opacity-0 translate-y-3.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Exploring the boundaries of digital art in 2026</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[14px] aspect-[3/4]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih04-ocean/600/800'),linear-gradient(135deg,oklch(0.3_0.07_165),oklch(0.42_0.09_165),oklch(0.85_0.13_165))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih04 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 flex flex-col justify-end p-5 bg-transparent backdrop-blur-none backdrop-brightness-100 transition-[backdrop-filter,background-color] duration-400 ease-tih04 group-hover:bg-[oklch(0_0_0/0.15)] group-hover:backdrop-blur-lg group-hover:backdrop-brightness-60 motion-reduce:transition-none motion-reduce:bg-[oklch(0_0_0/0.15)] motion-reduce:backdrop-blur-lg motion-reduce:backdrop-brightness-60">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih04-acc opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Nature</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih04-text opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#bioluminescent" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih04-acc focus-visible:outline-offset-3">Bioluminescent Depths</a></h3>
        <p style="--i:2" class="mt-1.25 text-[11px] text-tih04-muted opacity-0 translate-y-3.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Life thriving in the ocean's twilight zone</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-[14px] aspect-[3/4]">
      <div class="absolute inset-0 bg-[image:url('https://picsum.photos/seed/tih04-neon/600/800'),linear-gradient(135deg,oklch(0.16_0.06_350),oklch(0.35_0.15_350),oklch(0.75_0.2_330))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih04 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="absolute inset-0 flex flex-col justify-end p-5 bg-transparent backdrop-blur-none backdrop-brightness-100 transition-[backdrop-filter,background-color] duration-400 ease-tih04 group-hover:bg-[oklch(0_0_0/0.15)] group-hover:backdrop-blur-lg group-hover:backdrop-brightness-60 motion-reduce:transition-none motion-reduce:bg-[oklch(0_0_0/0.15)] motion-reduce:backdrop-blur-lg motion-reduce:backdrop-brightness-60">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.12em] uppercase text-tih04-acc opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Culture</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih04-text opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#neon-flux" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih04-acc focus-visible:outline-offset-3">Neon Flux Collection</a></h3>
        <p style="--i:2" class="mt-1.25 text-[11px] text-tih04-muted opacity-0 translate-y-3.5 transition-[opacity,translate] duration-400 ease-tih04 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*60ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Street art meets future-forward design aesthetics</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih04-bg: #080810;
  --color-tih04-bg: oklch(0.12 0.012 285);
  --color-tih04-text: #f1f5f9;
  --color-tih04-text: oklch(0.96 0.005 250);
  --color-tih04-muted: #94a3b8;
  --color-tih04-muted: oklch(0.7 0.03 250);
  --color-tih04-acc: #8b5cf6;
  --color-tih04-acc: oklch(0.62 0.21 295);
  --font-tih04-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih04: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-04 {
  width: 100%;
  min-height: 100svh;
}

.tih-04 ::selection {
  background: oklch(0.62 0.21 295);
  color: #fff;
}
```
