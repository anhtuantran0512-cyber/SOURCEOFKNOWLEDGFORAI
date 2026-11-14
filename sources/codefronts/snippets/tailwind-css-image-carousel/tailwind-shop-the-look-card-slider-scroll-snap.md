---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-shop-the-look-card-slider-scroll-snap/"
title: "Tailwind Shop the Look Multi-Item Card Slider with Scroll Snap"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A horizontal product-card rail: three to four cards on desktop, one-per-view on mobile — the 'complete the look' pattern."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shop the Look Multi-Item Card Slider with Scroll Snap
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-shop-the-look-card-slider-scroll-snap/

A horizontal product-card rail: three to four cards on desktop, one-per-view on mobile — the 'complete the look' pattern. Tailwind ships first-class snap-x snap-mandatory / snap-start utilities, so this is the rare carousel where the port is shorter than the original, not just better located.
## HTML
```html
<section class="tcar-02 w-full min-h-svh grid place-items-center bg-tcar02-bg font-tcar02-sans px-3 py-10" aria-label="Shop the look product rail">
  <div class="w-[min(760px,100%)]">
    <h3 class="text-[15px] font-bold tracking-[0.02em] text-tcar02-ink mx-2 mb-3.5">Complete the look</h3>
    <ul tabindex="0" role="group" aria-label="Recommended products, scrollable" class="list-none flex gap-4 overflow-x-auto px-2 pt-1.5 pb-4 m-0 snap-x snap-mandatory [scroll-padding-left:8px] [scrollbar-width:thin] [scrollbar-color:var(--color-tcar02-track)_transparent] focus-visible:outline-3 focus-visible:outline-tcar02-acc focus-visible:outline-offset-2 focus-visible:rounded-xl">
      <li class="flex-none basis-[clamp(200px,70%,236px)] sm:basis-[calc((100%-32px)/3)] snap-start bg-white border border-tcar02-edge rounded-2xl overflow-hidden shadow-[0_12px_30px_-26px_oklch(0.35_0.06_40/0.7)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_36px_-24px_oklch(0.35_0.06_40/0.6)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="aspect-[5/6] bg-tcar02-ph"><img src="https://picsum.photos/seed/look-1/500/600" width="500" height="600" decoding="async" alt="Oversized wool coat" class="size-full object-cover block"></div>
        <div class="flex items-center justify-between gap-2.5 px-3.5 pt-3 pb-3.5"><span class="text-sm font-semibold text-tcar02-ink">Wool Overcoat</span><span class="text-sm font-bold text-tcar02-acc">$248</span></div>
      </li>
      <li class="flex-none basis-[clamp(200px,70%,236px)] sm:basis-[calc((100%-32px)/3)] snap-start bg-white border border-tcar02-edge rounded-2xl overflow-hidden shadow-[0_12px_30px_-26px_oklch(0.35_0.06_40/0.7)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_36px_-24px_oklch(0.35_0.06_40/0.6)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="aspect-[5/6] bg-tcar02-ph"><img src="https://picsum.photos/seed/look-2/500/600" width="500" height="600" loading="lazy" decoding="async" alt="Ribbed knit scarf" class="size-full object-cover block"></div>
        <div class="flex items-center justify-between gap-2.5 px-3.5 pt-3 pb-3.5"><span class="text-sm font-semibold text-tcar02-ink">Ribbed Scarf</span><span class="text-sm font-bold text-tcar02-acc">$54</span></div>
      </li>
      <li class="flex-none basis-[clamp(200px,70%,236px)] sm:basis-[calc((100%-32px)/3)] snap-start bg-white border border-tcar02-edge rounded-2xl overflow-hidden shadow-[0_12px_30px_-26px_oklch(0.35_0.06_40/0.7)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_36px_-24px_oklch(0.35_0.06_40/0.6)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="aspect-[5/6] bg-tcar02-ph"><img src="https://picsum.photos/seed/look-3/500/600" width="500" height="600" loading="lazy" decoding="async" alt="Leather ankle boots" class="size-full object-cover block"></div>
        <div class="flex items-center justify-between gap-2.5 px-3.5 pt-3 pb-3.5"><span class="text-sm font-semibold text-tcar02-ink">Ankle Boots</span><span class="text-sm font-bold text-tcar02-acc">$189</span></div>
      </li>
      <li class="flex-none basis-[clamp(200px,70%,236px)] sm:basis-[calc((100%-32px)/3)] snap-start bg-white border border-tcar02-edge rounded-2xl overflow-hidden shadow-[0_12px_30px_-26px_oklch(0.35_0.06_40/0.7)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_36px_-24px_oklch(0.35_0.06_40/0.6)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="aspect-[5/6] bg-tcar02-ph"><img src="https://picsum.photos/seed/look-4/500/600" width="500" height="600" loading="lazy" decoding="async" alt="Canvas crossbody bag" class="size-full object-cover block"></div>
        <div class="flex items-center justify-between gap-2.5 px-3.5 pt-3 pb-3.5"><span class="text-sm font-semibold text-tcar02-ink">Crossbody Bag</span><span class="text-sm font-bold text-tcar02-acc">$96</span></div>
      </li>
      <li class="flex-none basis-[clamp(200px,70%,236px)] sm:basis-[calc((100%-32px)/3)] snap-start bg-white border border-tcar02-edge rounded-2xl overflow-hidden shadow-[0_12px_30px_-26px_oklch(0.35_0.06_40/0.7)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_36px_-24px_oklch(0.35_0.06_40/0.6)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="aspect-[5/6] bg-tcar02-ph"><img src="https://picsum.photos/seed/look-5/500/600" width="500" height="600" loading="lazy" decoding="async" alt="Round tortoiseshell sunglasses" class="size-full object-cover block"></div>
        <div class="flex items-center justify-between gap-2.5 px-3.5 pt-3 pb-3.5"><span class="text-sm font-semibold text-tcar02-ink">Sunglasses</span><span class="text-sm font-bold text-tcar02-acc">$72</span></div>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar02-bg: #faf7f5;
  --color-tcar02-bg: oklch(0.98 0.005 50);
  --color-tcar02-edge: #eee3dd;
  --color-tcar02-edge: oklch(0.93 0.01 45);
  --color-tcar02-ph: #efe6e0;
  --color-tcar02-ph: oklch(0.92 0.012 45);
  --color-tcar02-track: #d9cfc9;
  --color-tcar02-track: oklch(0.85 0.015 45);
  --color-tcar02-ink: #2a211d;
  --color-tcar02-ink: oklch(0.26 0.015 45);
  --color-tcar02-acc: #a8442c;
  --color-tcar02-acc: oklch(0.55 0.14 25);
  --font-tcar02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-02 {
  width: 100%;
  min-height: 100svh;
}

.tcar-02 ::selection {
  background: var(--color-tcar02-acc);
  color: #fff;
}
/* Reduced motion also calms the snap scroll itself, which no variant reaches. */

@media (prefers-reduced-motion: reduce) {
  .tcar-02 ul {
    scroll-behavior: auto;
  }
}
```
