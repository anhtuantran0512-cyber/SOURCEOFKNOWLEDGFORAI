---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-vertical-image-carousel-scroll-snap/"
title: "Tailwind Vertical Image Carousel with Y-Axis Scroll Snap"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A carousel that scrolls up and down instead of left to right — sidebar widgets, story feeds, creative portfolios."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Image Carousel with Y-Axis Scroll Snap
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-vertical-image-carousel-scroll-snap/

A carousel that scrolls up and down instead of left to right — sidebar widgets, story feeds, creative portfolios. Tailwind ships snap-y as readily as snap-x, so the only genuinely vertical concern is giving the scroller a height and stopping its scroll from chaining to the page.
## HTML
```html
<section class="tcar-12 w-full min-h-svh grid place-items-center bg-tcar12-bg font-tcar12-sans px-5 py-10" aria-label="Vertical image carousel">
  <ul tabindex="0" role="group" aria-label="Gallery, scroll up and down" class="tcar12-scroller list-none w-[min(340px,100%)] h-[min(560px,80svh)] overflow-y-auto m-0 p-0 rounded-[20px] snap-y snap-mandatory [overscroll-behavior:contain] [scrollbar-width:none] shadow-[0_30px_60px_-34px_oklch(0_0_0/0.9)] focus-visible:outline-3 focus-visible:outline-tcar12-acc focus-visible:outline-offset-[3px]">
    <li class="relative h-full snap-start overflow-hidden"><img src="https://picsum.photos/seed/vert-1/700/900" width="700" height="900" decoding="async" alt="Desert dunes at sunset" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-10 pb-5 text-[15px] font-semibold text-white bg-[linear-gradient(transparent,oklch(0.15_0.01_170/0.9))]">Sahara, Morocco</span></li>
    <li class="relative h-full snap-start overflow-hidden"><img src="https://picsum.photos/seed/vert-2/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Glacier lagoon" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-10 pb-5 text-[15px] font-semibold text-white bg-[linear-gradient(transparent,oklch(0.15_0.01_170/0.9))]">J&ouml;kuls&aacute;rl&oacute;n, Iceland</span></li>
    <li class="relative h-full snap-start overflow-hidden"><img src="https://picsum.photos/seed/vert-3/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Terraced rice fields" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-10 pb-5 text-[15px] font-semibold text-white bg-[linear-gradient(transparent,oklch(0.15_0.01_170/0.9))]">Bali, Indonesia</span></li>
    <li class="relative h-full snap-start overflow-hidden"><img src="https://picsum.photos/seed/vert-4/700/900" width="700" height="900" loading="lazy" decoding="async" alt="Autumn forest path" class="size-full object-cover block"><span class="absolute inset-x-0 bottom-0 px-5 pt-10 pb-5 text-[15px] font-semibold text-white bg-[linear-gradient(transparent,oklch(0.15_0.01_170/0.9))]">Kyoto, Japan</span></li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar12-bg: #0e1513;
  --color-tcar12-bg: oklch(0.18 0.015 170);
  --color-tcar12-acc: #2dd4bf;
  --color-tcar12-acc: oklch(0.78 0.13 180);
  --font-tcar12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-12 {
  width: 100%;
  min-height: 100svh;
}

.tcar-12 ::selection {
  background: var(--color-tcar12-acc);
  color: #062120;
}

.tcar12-scroller::-webkit-scrollbar {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .tcar12-scroller {
    scroll-behavior: auto;
  }
}
```
