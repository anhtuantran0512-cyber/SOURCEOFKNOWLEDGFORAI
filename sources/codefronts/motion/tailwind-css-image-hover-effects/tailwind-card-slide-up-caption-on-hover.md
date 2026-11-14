---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-card-slide-up-caption-on-hover/"
title: "Tailwind Card Slide Up Caption on Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "A caption panel parked below the frame with a 44px strip still showing, so the card advertises itself before anyone hovers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Card Slide Up Caption on Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-card-slide-up-caption-on-hover/

A caption panel parked below the frame with a 44px strip still showing, so the card advertises itself before anyone hovers. The resting offset is [translate:0_calc(100%-44px)] &mdash; an arbitrary translate, because the value is tied to the peek height, not to the spacing scale.
## HTML
```html
<section class="tih-05 w-full min-h-svh grid place-items-center bg-tih05-bg font-tih05-sans px-6 py-10" aria-label="Slide up caption on hover demo">
  <div class="grid w-full max-w-195 gap-4 grid-cols-1 sm:grid-cols-3">
    <article class="group relative overflow-hidden rounded-xl aspect-[4/5] bg-tih05-card border border-[oklch(1_0_0/0.05)]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih05-synthwave/640/800'),linear-gradient(150deg,oklch(0.16_0.03_285),oklch(0.27_0.11_285)_60%,oklch(0.35_0.14_282))] bg-cover bg-center bg-no-repeat transition-[scale,translate] duration-400 ease-tih05 group-hover:scale-106 group-hover:-translate-y-1 motion-reduce:transition-none motion-reduce:group-hover:scale-100 motion-reduce:group-hover:translate-y-0">
      </div>
      <div class="absolute inset-x-0 bottom-0 pt-10 px-4 pb-4 bg-linear-[to_top,oklch(0_0_0/0.92),oklch(0_0_0/0.7)_60%,transparent] [translate:0_calc(100%-44px)] transition-[translate] duration-400 ease-tih05 group-hover:translate-y-0 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:translate-y-0">
        <p class="flex items-center gap-1.5 mb-2.5 text-xs font-semibold text-tih05-text"><span class="w-1.5 h-1.5 rounded-full bg-tih05-acc shrink-0" aria-hidden="true"></span>Synthwave</p>
        <h3 class="mb-1.5 text-sm font-bold text-tih05-text"><a href="#neon-highways" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih05-acc focus-visible:outline-offset-3">Neon Highways</a></h3>
        <p class="text-[11px] leading-[1.5] text-tih05-muted">A 12-track journey through retro-futuristic soundscapes and pulsing basslines</p>
        <span class="inline-block mt-2 px-2 py-0.75 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih05-acc bg-[oklch(0.72_0.16_350/0.15)] border border-[oklch(0.72_0.16_350/0.3)]">New Album</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-xl aspect-[4/5] bg-tih05-card border border-[oklch(1_0_0/0.05)]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih05-ambient/640/800'),linear-gradient(150deg,oklch(0.2_0.04_190),oklch(0.46_0.09_185)_60%,oklch(0.78_0.11_185))] bg-cover bg-center bg-no-repeat transition-[scale,translate] duration-400 ease-tih05 group-hover:scale-106 group-hover:-translate-y-1 motion-reduce:transition-none motion-reduce:group-hover:scale-100 motion-reduce:group-hover:translate-y-0">
      </div>
      <div class="absolute inset-x-0 bottom-0 pt-10 px-4 pb-4 bg-linear-[to_top,oklch(0_0_0/0.92),oklch(0_0_0/0.7)_60%,transparent] [translate:0_calc(100%-44px)] transition-[translate] duration-400 ease-tih05 group-hover:translate-y-0 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:translate-y-0">
        <p class="flex items-center gap-1.5 mb-2.5 text-xs font-semibold text-tih05-text"><span class="w-1.5 h-1.5 rounded-full bg-tih05-acc shrink-0" aria-hidden="true"></span>Ambient</p>
        <h3 class="mb-1.5 text-sm font-bold text-tih05-text"><a href="#ocean-mind" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih05-acc focus-visible:outline-offset-3">Ocean Mind</a></h3>
        <p class="text-[11px] leading-[1.5] text-tih05-muted">Meditative binaural compositions recorded at the Faroe Islands coastline</p>
        <span class="inline-block mt-2 px-2 py-0.75 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih05-acc bg-[oklch(0.72_0.16_350/0.15)] border border-[oklch(0.72_0.16_350/0.3)]">EP Release</span>
      </div>
    </article>
    <article class="group relative overflow-hidden rounded-xl aspect-[4/5] bg-tih05-card border border-[oklch(1_0_0/0.05)]">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih05-electronic/640/800'),linear-gradient(150deg,oklch(0.17_0.08_310),oklch(0.42_0.2_305)_60%,oklch(0.72_0.16_305))] bg-cover bg-center bg-no-repeat transition-[scale,translate] duration-400 ease-tih05 group-hover:scale-106 group-hover:-translate-y-1 motion-reduce:transition-none motion-reduce:group-hover:scale-100 motion-reduce:group-hover:translate-y-0">
      </div>
      <div class="absolute inset-x-0 bottom-0 pt-10 px-4 pb-4 bg-linear-[to_top,oklch(0_0_0/0.92),oklch(0_0_0/0.7)_60%,transparent] [translate:0_calc(100%-44px)] transition-[translate] duration-400 ease-tih05 group-hover:translate-y-0 focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:translate-y-0">
        <p class="flex items-center gap-1.5 mb-2.5 text-xs font-semibold text-tih05-text"><span class="w-1.5 h-1.5 rounded-full bg-tih05-acc shrink-0" aria-hidden="true"></span>Electronic</p>
        <h3 class="mb-1.5 text-sm font-bold text-tih05-text"><a href="#violet-frequencies" class="no-underline text-inherit rounded focus-visible:outline-2 focus-visible:outline-tih05-acc focus-visible:outline-offset-3">Violet Frequencies</a></h3>
        <p class="text-[11px] leading-[1.5] text-tih05-muted">Experimental club music blending modular synthesis and jazz improvisation</p>
        <span class="inline-block mt-2 px-2 py-0.75 rounded-full text-[10px] font-bold tracking-[0.06em] text-tih05-acc bg-[oklch(0.72_0.16_350/0.15)] border border-[oklch(0.72_0.16_350/0.3)]">Single</span>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih05-bg: #0a0a10;
  --color-tih05-bg: oklch(0.13 0.01 285);
  --color-tih05-card: #141420;
  --color-tih05-card: oklch(0.18 0.015 285);
  --color-tih05-text: #f1f5f9;
  --color-tih05-text: oklch(0.96 0.005 250);
  --color-tih05-muted: #64748b;
  --color-tih05-muted: oklch(0.55 0.035 255);
  --color-tih05-acc: #f472b6;
  --color-tih05-acc: oklch(0.72 0.16 350);
  --font-tih05-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih05: cubic-bezier(0.16, 1, 0.3, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-05 {
  width: 100%;
  min-height: 100svh;
}

.tih-05 ::selection {
  background: oklch(0.72 0.16 350);
  color: #000;
}
```
