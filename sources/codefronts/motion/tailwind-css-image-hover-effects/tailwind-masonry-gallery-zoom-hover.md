---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-masonry-gallery-zoom-hover/"
title: "Tailwind Masonry Gallery Zoom Hover"
section: "motion"
category: "tailwind-css-image-hover-effects"
category_name: "Tailwind CSS Image Hover Effects"
description: "Column-based masonry where the responsive column count is the whole layout: columns-2 sm:columns-3 plus break-inside-avoid on each item."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Masonry Gallery Zoom Hover
Source: https://codefronts.com/motion/tailwind-css-image-hover-effects/tailwind-masonry-gallery-zoom-hover/

Column-based masonry where the responsive column count is the whole layout: columns-2 sm:columns-3 plus break-inside-avoid on each item. The CSS version needs a media query to change column count; here it is one breakpoint prefix, which is the kind of edit this port makes trivial.
## HTML
```html
<section class="tih-18 w-full min-h-svh bg-tih18-bg font-tih18-sans px-6 py-8" aria-label="Masonry gallery zoom hover demo">
  <div class="columns-2 sm:columns-3 gap-3 w-full max-w-195 mx-auto">
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[5/7] bg-[image:url('https://picsum.photos/seed/masonry-a/600/840'),linear-gradient(150deg,oklch(0.17_0.07_310),oklch(0.35_0.18_298),oklch(0.55_0.24_295))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Cosmos</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-square bg-[image:url('https://picsum.photos/seed/masonry-b/600/600'),linear-gradient(150deg,oklch(0.2_0.04_190),oklch(0.42_0.09_165),oklch(0.7_0.15_163))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Flora</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[3/2] bg-[image:url('https://picsum.photos/seed/masonry-c/600/400'),linear-gradient(150deg,oklch(0.18_0.03_60),oklch(0.45_0.11_60),oklch(0.78_0.16_72))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Desert</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-square bg-[image:url('https://picsum.photos/seed/masonry-d/600/600'),linear-gradient(150deg,oklch(0.17_0.08_265),oklch(0.33_0.14_262),oklch(0.62_0.19_260))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Ocean</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[5/7] bg-[image:url('https://picsum.photos/seed/masonry-e/600/840'),linear-gradient(150deg,oklch(0.16_0.06_350),oklch(0.4_0.18_5),oklch(0.65_0.22_15))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Bloom</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[3/2] bg-[image:url('https://picsum.photos/seed/masonry-f/600/400'),linear-gradient(150deg,oklch(0.19_0.03_230),oklch(0.32_0.06_240),oklch(0.6_0.12_215))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Ice</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[3/2] bg-[image:url('https://picsum.photos/seed/masonry-g/600/400'),linear-gradient(150deg,oklch(0.17_0.07_285),oklch(0.31_0.14_280),oklch(0.5_0.2_275))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Mystic</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-[5/7] bg-[image:url('https://picsum.photos/seed/masonry-h/600/840'),linear-gradient(150deg,oklch(0.2_0.05_150),oklch(0.35_0.09_150),oklch(0.8_0.16_145))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Forest</span></figcaption>
    </figure>
    <figure class="group relative block mb-3 break-inside-avoid overflow-hidden rounded-[10px]">
      <div class="aspect-square bg-[image:url('https://picsum.photos/seed/masonry-i/600/600'),linear-gradient(150deg,oklch(0.17_0.07_310),oklch(0.35_0.18_298),oklch(0.55_0.24_295))] bg-cover bg-center transition-transform duration-400 ease-tih18 group-hover:scale-108 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <figcaption class="absolute inset-0 flex items-end p-2.5 bg-linear-[to_top,oklch(0_0_0/0.7),transparent_60%] opacity-0 transition-opacity duration-400 ease-tih18 group-hover:opacity-100 motion-reduce:transition-none motion-reduce:opacity-100"><span class="px-1.5 py-0.5 rounded text-[10px] font-bold text-white bg-[oklch(0.6_0.22_15/0.7)]">Stars</span></figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tih18-bg: #08080c;
  --color-tih18-bg: oklch(0.12 0.008 285);
  --color-tih18-text: #f1f5f9;
  --color-tih18-text: oklch(0.96 0.005 250);
  --color-tih18-muted: #64748b;
  --color-tih18-muted: oklch(0.58 0.035 255);
  --color-tih18-acc: #f43f5e;
  --color-tih18-acc: oklch(0.6 0.22 15);
  --font-tih18-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tih18: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is correctly sized before the browser build compiles. */

.tih-18 {
  width: 100%;
  min-height: 100svh;
}

.tih-18 ::selection {
  background: oklch(0.6 0.22 15);
  color: #fff;
}
```
