---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-accordion-expanding-image-panel-carousel/"
title: "Tailwind Accordion Expanding Image Panel Carousel"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A row of tall panels where hovering or focusing one expands it wide while the others shrink to slivers."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion Expanding Image Panel Carousel
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-accordion-expanding-image-panel-carousel/

A row of tall panels where hovering or focusing one expands it wide while the others shrink to slivers. The only demo in the collection that deliberately animates a layout property — flex-grow — because there is no transform that produces this push-and-pull.
## HTML
```html
<section class="tcar-19 w-full min-h-svh grid place-items-center bg-tcar19-bg font-tcar19-sans px-5 py-10" aria-label="Expanding image panels">
  <ul class="list-none flex gap-2.5 w-[min(820px,100%)] h-[min(440px,70svh)] m-0 p-0">
    <li class="group grow basis-0 min-w-0 transition-[flex-grow] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:grow-[5] focus-within:grow-[5] motion-reduce:transition-none">
      <a href="#" class="relative block h-full rounded-[14px] overflow-hidden no-underline bg-tcar19-tile focus-visible:outline-3 focus-visible:outline-tcar19-acc focus-visible:outline-offset-2">
        <img src="https://picsum.photos/seed/acc-1/700/900" width="700" height="900" decoding="async" alt="Modernist villa" class="size-full object-cover block brightness-[0.72] transition-[filter] duration-500 group-hover:brightness-100 group-focus-within:brightness-100 motion-reduce:transition-none">
        <span class="absolute left-4 bottom-4 right-4 text-white whitespace-nowrap opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 delay-100 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none"><b class="block text-lg font-tcar19-serif">Villa Sereno</b><small class="block text-[12.5px] text-tcar19-cap mt-0.5">Coastal retreat</small></span>
      </a>
    </li>
    <li class="group grow basis-0 min-w-0 transition-[flex-grow] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:grow-[5] focus-within:grow-[5] motion-reduce:transition-none">
      <a href="#" class="relative block h-full rounded-[14px] overflow-hidden no-underline bg-tcar19-tile focus-visible:outline-3 focus-visible:outline-tcar19-acc focus-visible:outline-offset-2">
        <img src="https://picsum.photos/seed/acc-2/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Loft interior" class="size-full object-cover block brightness-[0.72] transition-[filter] duration-500 group-hover:brightness-100 group-focus-within:brightness-100 motion-reduce:transition-none">
        <span class="absolute left-4 bottom-4 right-4 text-white whitespace-nowrap opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 delay-100 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none"><b class="block text-lg font-tcar19-serif">Union Loft</b><small class="block text-[12.5px] text-tcar19-cap mt-0.5">City living</small></span>
      </a>
    </li>
    <li class="group grow basis-0 min-w-0 transition-[flex-grow] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:grow-[5] focus-within:grow-[5] motion-reduce:transition-none">
      <a href="#" class="relative block h-full rounded-[14px] overflow-hidden no-underline bg-tcar19-tile focus-visible:outline-3 focus-visible:outline-tcar19-acc focus-visible:outline-offset-2">
        <img src="https://picsum.photos/seed/acc-3/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Cabin in the woods" class="size-full object-cover block brightness-[0.72] transition-[filter] duration-500 group-hover:brightness-100 group-focus-within:brightness-100 motion-reduce:transition-none">
        <span class="absolute left-4 bottom-4 right-4 text-white whitespace-nowrap opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 delay-100 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none"><b class="block text-lg font-tcar19-serif">Pine Cabin</b><small class="block text-[12.5px] text-tcar19-cap mt-0.5">Forest escape</small></span>
      </a>
    </li>
    <li class="group grow basis-0 min-w-0 transition-[flex-grow] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:grow-[5] focus-within:grow-[5] motion-reduce:transition-none">
      <a href="#" class="relative block h-full rounded-[14px] overflow-hidden no-underline bg-tcar19-tile focus-visible:outline-3 focus-visible:outline-tcar19-acc focus-visible:outline-offset-2">
        <img src="https://picsum.photos/seed/acc-4/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Desert house" class="size-full object-cover block brightness-[0.72] transition-[filter] duration-500 group-hover:brightness-100 group-focus-within:brightness-100 motion-reduce:transition-none">
        <span class="absolute left-4 bottom-4 right-4 text-white whitespace-nowrap opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 delay-100 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none"><b class="block text-lg font-tcar19-serif">Dune House</b><small class="block text-[12.5px] text-tcar19-cap mt-0.5">Desert calm</small></span>
      </a>
    </li>
    <li class="group grow basis-0 min-w-0 transition-[flex-grow] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:grow-[5] focus-within:grow-[5] motion-reduce:transition-none">
      <a href="#" class="relative block h-full rounded-[14px] overflow-hidden no-underline bg-tcar19-tile focus-visible:outline-3 focus-visible:outline-tcar19-acc focus-visible:outline-offset-2">
        <img src="https://picsum.photos/seed/acc-5/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Lakeside home" class="size-full object-cover block brightness-[0.72] transition-[filter] duration-500 group-hover:brightness-100 group-focus-within:brightness-100 motion-reduce:transition-none">
        <span class="absolute left-4 bottom-4 right-4 text-white whitespace-nowrap opacity-0 translate-y-2.5 transition-[opacity,translate] duration-400 delay-100 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none"><b class="block text-lg font-tcar19-serif">Still Water</b><small class="block text-[12.5px] text-tcar19-cap mt-0.5">Lakeside</small></span>
      </a>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar19-bg: #17140f;
  --color-tcar19-bg: oklch(0.19 0.012 75);
  --color-tcar19-tile: #221d16;
  --color-tcar19-tile: oklch(0.24 0.015 75);
  --color-tcar19-cap: #f0dcb4;
  --color-tcar19-cap: oklch(0.89 0.06 85);
  --color-tcar19-acc: #d97706;
  --color-tcar19-acc: oklch(0.67 0.16 60);
  --font-tcar19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tcar19-serif: 'Newsreader', Georgia, serif;
}

.tcar-19 {
  width: 100%;
  min-height: 100svh;
}

.tcar-19 ::selection {
  background: var(--color-tcar19-acc);
  color: #1a1208;
}
```
