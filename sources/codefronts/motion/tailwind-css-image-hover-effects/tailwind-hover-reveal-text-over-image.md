---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-hover-reveal-text-over-image/"
title: "Tailwind Hover Reveal Text Over Image"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The portfolio-grid reveal: a gradient overlay fades in and its three text lines slide up in sequence."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hover Reveal Text Over Image
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-hover-reveal-text-over-image/

The portfolio-grid reveal: a gradient overlay fades in and its three text lines slide up in sequence. The CSS version staggers with duration multipliers; the port staggers with the per-item index pattern &mdash; each line carries style="--i:1" and one shared utility reads it, so the cascade tempo is a single number.
## HTML
```html
<section class="tih-02 w-full min-h-svh grid place-items-center bg-tih02-bg font-tih02-sans px-6 py-10" aria-label="Hover reveal text over image demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-xl aspect-[3/4]">
      <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih02-nebula/600/800'),linear-gradient(160deg,oklch(0.17_0.07_285),oklch(0.34_0.12_285),oklch(0.28_0.06_290))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih02 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <span class="absolute top-3 left-3 z-2 px-2 py-1 rounded-md text-[10px] font-semibold tracking-[0.05em] text-tih02-muted bg-[oklch(0_0_0/0.5)] backdrop-blur-md border border-[oklch(1_0_0/0.1)]">Portfolio</span>
      <div class="absolute inset-0 z-1 flex flex-col justify-end p-4 pointer-events-none bg-linear-[to_top,oklch(0_0_0/0.85),oklch(0_0_0/0.3)_50%,transparent] opacity-0 transition-opacity duration-400 ease-tih02 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.1em] uppercase text-tih02-acc opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Astrophotography</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih02-text opacity-0 translate-y-4 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#nebula" class="pointer-events-auto no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih02-acc focus-visible:outline-offset-3">Nebula Series Vol. 3</a></h3>
        <p style="--i:2" class="mt-1 text-xs text-tih02-muted opacity-0 translate-y-5 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Shot over 14 nights in the Chilean Atacama desert</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-xl aspect-[3/4]">
      <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih02-city/600/800'),linear-gradient(160deg,oklch(0.2_0.03_220),oklch(0.32_0.04_215),oklch(0.42_0.05_235))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih02 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <span class="absolute top-3 left-3 z-2 px-2 py-1 rounded-md text-[10px] font-semibold tracking-[0.05em] text-tih02-muted bg-[oklch(0_0_0/0.5)] backdrop-blur-md border border-[oklch(1_0_0/0.1)]">Architecture</span>
      <div class="absolute inset-0 z-1 flex flex-col justify-end p-4 pointer-events-none bg-linear-[to_top,oklch(0_0_0/0.85),oklch(0_0_0/0.3)_50%,transparent] opacity-0 transition-opacity duration-400 ease-tih02 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.1em] uppercase text-tih02-acc opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Urban Design</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih02-text opacity-0 translate-y-4 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#cityscapes" class="pointer-events-auto no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih02-acc focus-visible:outline-offset-3">Midnight Cityscapes</a></h3>
        <p style="--i:2" class="mt-1 text-xs text-tih02-muted opacity-0 translate-y-5 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Long exposure study of downtown light trails</p>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-xl aspect-[3/4]">
      <div class="grid place-items-center w-full h-full bg-[image:url('https://picsum.photos/seed/tih02-prism/600/800'),linear-gradient(160deg,oklch(0.17_0.09_320),oklch(0.29_0.15_325),oklch(0.32_0.12_290))] bg-cover bg-center bg-no-repeat transition-transform duration-400 ease-tih02 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      </div>
      <span class="absolute top-3 left-3 z-2 px-2 py-1 rounded-md text-[10px] font-semibold tracking-[0.05em] text-tih02-muted bg-[oklch(0_0_0/0.5)] backdrop-blur-md border border-[oklch(1_0_0/0.1)]">Abstract</span>
      <div class="absolute inset-0 z-1 flex flex-col justify-end p-4 pointer-events-none bg-linear-[to_top,oklch(0_0_0/0.85),oklch(0_0_0/0.3)_50%,transparent] opacity-0 transition-opacity duration-400 ease-tih02 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100">
        <p style="--i:0" class="mb-1.5 text-[10px] font-bold tracking-[0.1em] uppercase text-tih02-acc opacity-0 translate-y-3 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Digital Art</p>
        <h3 style="--i:1" class="text-[15px] font-bold leading-[1.3] text-tih02-text opacity-0 translate-y-4 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0"><a href="#prism" class="pointer-events-auto no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih02-acc focus-visible:outline-offset-3">Prism Light Study</a></h3>
        <p style="--i:2" class="mt-1 text-xs text-tih02-muted opacity-0 translate-y-5 transition-[opacity,translate] duration-400 ease-tih02 group-hover:opacity-100 group-hover:translate-y-0 group-hover:[transition-delay:calc(var(--i)*70ms)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Generative colour diffraction experiments</p>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih02-bg: #09090f;
  --color-tih02-bg: oklch(0.13 0.008 285);
  --color-tih02-text: #f1f5f9;
  --color-tih02-text: oklch(0.96 0.005 250);
  --color-tih02-muted: #94a3b8;
  --color-tih02-muted: oklch(0.7 0.03 250);
  --color-tih02-acc: #06b6d4;
  --color-tih02-acc: oklch(0.71 0.14 205);
  --font-tih02-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih02: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-02 {
  width: 100%;
  min-height: 100svh;
}

.tih-02 ::selection {
  background: oklch(0.71 0.14 205);
  color: #000;
}
```
