---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-dot-pagination-carousel-target-has/"
title: "Tailwind Dot Pagination Carousel with Target and Has Selectors"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A wide-format gallery with indicator dots that jump to their slide and light up when active."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dot Pagination Carousel with Target and Has Selectors
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-dot-pagination-carousel-target-has/

A wide-format gallery with indicator dots that jump to their slide and light up when active. The dots are anchor links, the highlight is :target read through :has(), and the whole thing is navigation that works with JavaScript disabled.
## HTML
```html
<section class="tcar-16 w-full min-h-svh grid place-items-center bg-tcar16-bg font-tcar16-sans px-5 py-10" aria-label="Destination gallery">
  <div class="group tcar16-frame w-[min(680px,100%)] bg-white rounded-[18px] overflow-hidden shadow-[0_24px_50px_-34px_oklch(0.45_0.1_75/0.5)]">
    <ul tabindex="0" role="group" aria-label="Destinations, swipe or use arrow keys" class="tcar16-scroller list-none flex overflow-x-auto m-0 p-0 snap-x snap-mandatory scroll-smooth [scrollbar-width:none] focus-visible:outline-3 focus-visible:outline-tcar16-acc focus-visible:-outline-offset-[3px]">
      <li id="tcar-16-1" class="relative flex-none basis-full snap-center aspect-video overflow-hidden"><img src="https://picsum.photos/seed/dot-1/1000/560" width="1000" height="560" fetchpriority="high" decoding="async" alt="Amalfi coastline" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-[34px] pb-4 text-white text-lg font-bold bg-[linear-gradient(transparent,oklch(0_0_0/0.7))]">Amalfi Coast</span></li>
      <li id="tcar-16-2" class="relative flex-none basis-full snap-center aspect-video overflow-hidden"><img src="https://picsum.photos/seed/dot-2/1000/560" width="1000" height="560" loading="lazy" decoding="async" alt="Santorini rooftops" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-[34px] pb-4 text-white text-lg font-bold bg-[linear-gradient(transparent,oklch(0_0_0/0.7))]">Santorini</span></li>
      <li id="tcar-16-3" class="relative flex-none basis-full snap-center aspect-video overflow-hidden"><img src="https://picsum.photos/seed/dot-3/1000/560" width="1000" height="560" loading="lazy" decoding="async" alt="Kyoto temple garden" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-[34px] pb-4 text-white text-lg font-bold bg-[linear-gradient(transparent,oklch(0_0_0/0.7))]">Kyoto</span></li>
      <li id="tcar-16-4" class="relative flex-none basis-full snap-center aspect-video overflow-hidden"><img src="https://picsum.photos/seed/dot-4/1000/560" width="1000" height="560" loading="lazy" decoding="async" alt="Patagonia peaks" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-[34px] pb-4 text-white text-lg font-bold bg-[linear-gradient(transparent,oklch(0_0_0/0.7))]">Patagonia</span></li>
    </ul>
    <nav aria-label="Pagination" class="flex justify-center p-1 bg-white">
      <a href="#tcar-16-1" aria-label="Go to slide 1" class="tcar16-dot group/dot size-11 grid place-items-center no-underline"><span class="size-2.5 rounded-full bg-tcar16-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar16-dothover focus-visible:outline-3 focus-visible:outline-tcar16-acc focus-visible:outline-offset-[3px] group-has-[#tcar-16-1:target]:bg-tcar16-acc group-has-[#tcar-16-1:target]:scale-[1.4] motion-reduce:transition-none"></span></a>
      <a href="#tcar-16-2" aria-label="Go to slide 2" class="tcar16-dot group/dot size-11 grid place-items-center no-underline"><span class="size-2.5 rounded-full bg-tcar16-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar16-dothover focus-visible:outline-3 focus-visible:outline-tcar16-acc focus-visible:outline-offset-[3px] group-has-[#tcar-16-2:target]:bg-tcar16-acc group-has-[#tcar-16-2:target]:scale-[1.4] motion-reduce:transition-none"></span></a>
      <a href="#tcar-16-3" aria-label="Go to slide 3" class="tcar16-dot group/dot size-11 grid place-items-center no-underline"><span class="size-2.5 rounded-full bg-tcar16-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar16-dothover focus-visible:outline-3 focus-visible:outline-tcar16-acc focus-visible:outline-offset-[3px] group-has-[#tcar-16-3:target]:bg-tcar16-acc group-has-[#tcar-16-3:target]:scale-[1.4] motion-reduce:transition-none"></span></a>
      <a href="#tcar-16-4" aria-label="Go to slide 4" class="tcar16-dot group/dot size-11 grid place-items-center no-underline"><span class="size-2.5 rounded-full bg-tcar16-dot transition-[scale,background-color] duration-200 group-hover/dot:bg-tcar16-dothover focus-visible:outline-3 focus-visible:outline-tcar16-acc focus-visible:outline-offset-[3px] group-has-[#tcar-16-4:target]:bg-tcar16-acc group-has-[#tcar-16-4:target]:scale-[1.4] motion-reduce:transition-none"></span></a>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar16-bg: #faf6ee;
  --color-tcar16-bg: oklch(0.97 0.012 85);
  --color-tcar16-dot: #dcc9a4;
  --color-tcar16-dot: oklch(0.85 0.045 85);
  --color-tcar16-dothover: #c4a873;
  --color-tcar16-dothover: oklch(0.75 0.07 85);
  --color-tcar16-acc: #b26a00;
  --color-tcar16-acc: oklch(0.6 0.13 70);
  --font-tcar16-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-16 {
  width: 100%;
  min-height: 100svh;
}

.tcar-16 ::selection {
  background: var(--color-tcar16-acc);
  color: #fff;
}

.tcar16-scroller::-webkit-scrollbar {
  display: none;
}
/* First paint: nothing is :target yet, so slide 1 owns the highlight.
   :not(:has(:target)) has no readable variant form — this is the rule that stays CSS. */

.tcar16-frame:not(:has(:target)) .tcar16-dot:first-child > span {
  background: var(--color-tcar16-acc);
  scale: 1.4;
}

@media (prefers-reduced-motion: reduce) {
  .tcar16-scroller {
    scroll-behavior: auto;
  }
}
```
