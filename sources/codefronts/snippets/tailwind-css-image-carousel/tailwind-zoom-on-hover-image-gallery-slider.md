---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-zoom-on-hover-image-gallery-slider/"
title: "Tailwind Zoom-on-Hover Image Gallery Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A scroll-snap rail where hovering any tile scales the photograph up inside its fixed frame."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Zoom-on-Hover Image Gallery Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-zoom-on-hover-image-gallery-slider/

A scroll-snap rail where hovering any tile scales the photograph up inside its fixed frame. The frame clips the overflow, so the picture grows and the layout does not move — the most reusable three-utility idea in the collection.
## HTML
```html
<section class="tcar-21 w-full min-h-svh grid place-items-center bg-tcar21-bg font-tcar21-sans px-3 py-10" aria-label="Dish gallery">
  <ul tabindex="0" role="group" aria-label="Dishes, scrollable" class="list-none flex gap-4 w-[min(760px,100%)] overflow-x-auto p-3 m-0 snap-x snap-mandatory [scroll-padding:12px] [scrollbar-width:thin] [scrollbar-color:var(--color-tcar21-track)_transparent] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-2 focus-visible:rounded-2xl">
    <li class="flex-none basis-[clamp(180px,60%,220px)] snap-start">
      <a href="#" class="group relative block aspect-square rounded-2xl overflow-hidden no-underline bg-tcar21-ph shadow-[0_14px_30px_-22px_oklch(0.4_0.15_10/0.6)] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-[3px]">
        <img src="https://picsum.photos/seed/zoom-1/600/600" width="600" height="600" decoding="async" alt="Ramen bowl" class="size-full object-cover block transition-[scale] duration-[550ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:scale-[1.18] group-focus-within:scale-[1.18] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        <span class="absolute inset-x-0 bottom-0 px-3.5 pt-8 pb-3 text-white text-sm font-bold bg-[linear-gradient(transparent,oklch(0.22_0.08_10/0.88))] opacity-0 translate-y-1.5 transition-[opacity,translate] duration-350 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Tonkotsu Ramen</span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(180px,60%,220px)] snap-start">
      <a href="#" class="group relative block aspect-square rounded-2xl overflow-hidden no-underline bg-tcar21-ph shadow-[0_14px_30px_-22px_oklch(0.4_0.15_10/0.6)] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-[3px]">
        <img src="https://picsum.photos/seed/zoom-2/600/600" width="600" height="600" loading="lazy" decoding="async" alt="Stack of pancakes" class="size-full object-cover block transition-[scale] duration-[550ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:scale-[1.18] group-focus-within:scale-[1.18] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        <span class="absolute inset-x-0 bottom-0 px-3.5 pt-8 pb-3 text-white text-sm font-bold bg-[linear-gradient(transparent,oklch(0.22_0.08_10/0.88))] opacity-0 translate-y-1.5 transition-[opacity,translate] duration-350 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Buttermilk Stack</span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(180px,60%,220px)] snap-start">
      <a href="#" class="group relative block aspect-square rounded-2xl overflow-hidden no-underline bg-tcar21-ph shadow-[0_14px_30px_-22px_oklch(0.4_0.15_10/0.6)] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-[3px]">
        <img src="https://picsum.photos/seed/zoom-3/600/600" width="600" height="600" loading="lazy" decoding="async" alt="Poke bowl" class="size-full object-cover block transition-[scale] duration-[550ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:scale-[1.18] group-focus-within:scale-[1.18] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        <span class="absolute inset-x-0 bottom-0 px-3.5 pt-8 pb-3 text-white text-sm font-bold bg-[linear-gradient(transparent,oklch(0.22_0.08_10/0.88))] opacity-0 translate-y-1.5 transition-[opacity,translate] duration-350 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Ahi Poke Bowl</span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(180px,60%,220px)] snap-start">
      <a href="#" class="group relative block aspect-square rounded-2xl overflow-hidden no-underline bg-tcar21-ph shadow-[0_14px_30px_-22px_oklch(0.4_0.15_10/0.6)] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-[3px]">
        <img src="https://picsum.photos/seed/zoom-4/600/600" width="600" height="600" loading="lazy" decoding="async" alt="Berry tart" class="size-full object-cover block transition-[scale] duration-[550ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:scale-[1.18] group-focus-within:scale-[1.18] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        <span class="absolute inset-x-0 bottom-0 px-3.5 pt-8 pb-3 text-white text-sm font-bold bg-[linear-gradient(transparent,oklch(0.22_0.08_10/0.88))] opacity-0 translate-y-1.5 transition-[opacity,translate] duration-350 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Berry Tart</span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(180px,60%,220px)] snap-start">
      <a href="#" class="group relative block aspect-square rounded-2xl overflow-hidden no-underline bg-tcar21-ph shadow-[0_14px_30px_-22px_oklch(0.4_0.15_10/0.6)] focus-visible:outline-3 focus-visible:outline-tcar21-acc focus-visible:outline-offset-[3px]">
        <img src="https://picsum.photos/seed/zoom-5/600/600" width="600" height="600" loading="lazy" decoding="async" alt="Espresso" class="size-full object-cover block transition-[scale] duration-[550ms] ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:scale-[1.18] group-focus-within:scale-[1.18] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
        <span class="absolute inset-x-0 bottom-0 px-3.5 pt-8 pb-3 text-white text-sm font-bold bg-[linear-gradient(transparent,oklch(0.22_0.08_10/0.88))] opacity-0 translate-y-1.5 transition-[opacity,translate] duration-350 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none motion-reduce:opacity-100 motion-reduce:translate-y-0">Double Espresso</span>
      </a>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar21-bg: #fbf5f2;
  --color-tcar21-bg: oklch(0.97 0.008 30);
  --color-tcar21-ph: #eeddd7;
  --color-tcar21-ph: oklch(0.91 0.02 30);
  --color-tcar21-track: #e6cdc6;
  --color-tcar21-track: oklch(0.87 0.03 30);
  --color-tcar21-acc: #c3113c;
  --color-tcar21-acc: oklch(0.52 0.2 15);
  --font-tcar21-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-21 {
  width: 100%;
  min-height: 100svh;
}

.tcar-21 ::selection {
  background: var(--color-tcar21-acc);
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .tcar-21 ul {
    scroll-behavior: auto;
  }
}
```
