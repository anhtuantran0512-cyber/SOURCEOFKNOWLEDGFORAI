---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-split-transition-hover/"
title: "Tailwind Image Split Transition Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "The card slices in half and an action strip wipes open in the gap."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Image Split Transition Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-image-split-transition-hover/

The card slices in half and an action strip wipes open in the gap. Two layers carry identical artwork and complementary clip-path polygons; the strip animates inset(100%_0_100%_0) to inset(0), so it opens from the centre line outward rather than fading in.
## HTML
```html
<section class="tih-14 w-full min-h-svh grid place-items-center bg-tih14-bg font-tih14-sans px-6 py-10" aria-label="Image split transition hover demo">
  <div class="grid w-full max-w-195 gap-5 grid-cols-1 sm:grid-cols-3">
    <article class="group relative aspect-[3/4] rounded-[14px] overflow-hidden">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-canvas/600/800'),linear-gradient(135deg,oklch(0.17_0.07_310),oklch(0.35_0.18_298),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_0,100%_0,100%_50.5%,0_50.5%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_-6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-canvas/600/800'),linear-gradient(135deg,oklch(0.17_0.07_310),oklch(0.35_0.18_298),oklch(0.55_0.24_295))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_49.5%,100%_49.5%,100%_100%,0_100%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <span class="absolute top-3 left-3 z-2 text-[22px] font-black leading-none text-[oklch(1_0_0/0.12)]" aria-hidden="true">01</span>
      <div class="absolute inset-x-0 top-1/2 z-3 -translate-y-1/2 flex items-center justify-between px-4 py-3 bg-tih14-bg opacity-0 [clip-path:inset(100%_0_100%_0)] transition-[clip-path,opacity] duration-500 ease-tih14 group-hover:opacity-100 group-hover:[clip-path:inset(0)] focus-within:opacity-100 focus-within:[clip-path:inset(0)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:[clip-path:inset(0)]">
        <p class="text-xs font-bold text-tih14-text">Digital Canvas</p>
        <a href="#digital-canvas" class="px-2.5 py-1 rounded-full text-[10px] font-bold text-white bg-tih14-acc no-underline focus-visible:outline-2 focus-visible:outline-tih14-text focus-visible:outline-offset-2">View</a>
      </div>
    </article>
    <article class="group relative aspect-[3/4] rounded-[14px] overflow-hidden">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-growth/600/800'),linear-gradient(135deg,oklch(0.25_0.05_180),oklch(0.42_0.09_165),oklch(0.7_0.15_163))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_0,100%_0,100%_50.5%,0_50.5%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_-6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-growth/600/800'),linear-gradient(135deg,oklch(0.25_0.05_180),oklch(0.42_0.09_165),oklch(0.7_0.15_163))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_49.5%,100%_49.5%,100%_100%,0_100%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <span class="absolute top-3 left-3 z-2 text-[22px] font-black leading-none text-[oklch(1_0_0/0.12)]" aria-hidden="true">02</span>
      <div class="absolute inset-x-0 top-1/2 z-3 -translate-y-1/2 flex items-center justify-between px-4 py-3 bg-tih14-bg opacity-0 [clip-path:inset(100%_0_100%_0)] transition-[clip-path,opacity] duration-500 ease-tih14 group-hover:opacity-100 group-hover:[clip-path:inset(0)] focus-within:opacity-100 focus-within:[clip-path:inset(0)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:[clip-path:inset(0)]">
        <p class="text-xs font-bold text-tih14-text">Growth Series</p>
        <a href="#growth-series" class="px-2.5 py-1 rounded-full text-[10px] font-bold text-white bg-tih14-acc no-underline focus-visible:outline-2 focus-visible:outline-tih14-text focus-visible:outline-offset-2">View</a>
      </div>
    </article>
    <article class="group relative aspect-[3/4] rounded-[14px] overflow-hidden">
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-power/600/800'),linear-gradient(135deg,oklch(0.18_0.03_60),oklch(0.45_0.11_60),oklch(0.78_0.16_72))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_0,100%_0,100%_50.5%,0_50.5%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_-6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <div class="absolute inset-0 grid place-items-center bg-[image:url('https://picsum.photos/seed/tih14-power/600/800'),linear-gradient(135deg,oklch(0.18_0.03_60),oklch(0.45_0.11_60),oklch(0.78_0.16_72))] bg-cover bg-center bg-no-repeat [clip-path:polygon(0_49.5%,100%_49.5%,100%_100%,0_100%)] will-change-transform transition-[translate] duration-500 ease-tih14 group-hover:[translate:0_6%] motion-reduce:transition-none motion-reduce:group-hover:[translate:0_0]">
      </div>
      <span class="absolute top-3 left-3 z-2 text-[22px] font-black leading-none text-[oklch(1_0_0/0.12)]" aria-hidden="true">03</span>
      <div class="absolute inset-x-0 top-1/2 z-3 -translate-y-1/2 flex items-center justify-between px-4 py-3 bg-tih14-bg opacity-0 [clip-path:inset(100%_0_100%_0)] transition-[clip-path,opacity] duration-500 ease-tih14 group-hover:opacity-100 group-hover:[clip-path:inset(0)] focus-within:opacity-100 focus-within:[clip-path:inset(0)] motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:[clip-path:inset(0)]">
        <p class="text-xs font-bold text-tih14-text">Power Study</p>
        <a href="#power-study" class="px-2.5 py-1 rounded-full text-[10px] font-bold text-white bg-tih14-acc no-underline focus-visible:outline-2 focus-visible:outline-tih14-text focus-visible:outline-offset-2">View</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih14-bg: #070710;
  --color-tih14-bg: oklch(0.11 0.012 285);
  --color-tih14-text: #f1f5f9;
  --color-tih14-text: oklch(0.96 0.005 250);
  --color-tih14-muted: #475569;
  --color-tih14-muted: oklch(0.52 0.03 255);
  --color-tih14-acc: #fb7185;
  --color-tih14-acc: oklch(0.7 0.17 15);
  --font-tih14-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih14: cubic-bezier(0.34, 1.56, 0.64, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-14 {
  width: 100%;
  min-height: 100svh;
}

.tih-14 ::selection {
  background: oklch(0.7 0.17 15);
  color: #000;
}
```
