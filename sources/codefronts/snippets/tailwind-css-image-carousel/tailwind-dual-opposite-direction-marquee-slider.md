---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-dual-opposite-direction-marquee-slider/"
title: "Tailwind Dual Opposite-Direction Marquee Slider"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "Two image tracks gliding in opposite directions — the top row drifts left while the bottom drifts right."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dual Opposite-Direction Marquee Slider
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-dual-opposite-direction-marquee-slider/

Two image tracks gliding in opposite directions — the top row drifts left while the bottom drifts right. One keyframe, two @theme animation tokens, and the second one differs from the first by a single word: reverse.
## HTML
```html
<section class="tcar-15 w-full min-h-svh grid place-items-center bg-tcar15-bg font-tcar15-sans py-10" aria-label="Moodboard marquee">
  <div class="group tcar15-band w-full flex flex-col gap-4 overflow-hidden [mask-image:linear-gradient(90deg,transparent,#000_8%,#000_92%,transparent)]">
    <ul class="list-none flex gap-4 w-max m-0 p-0 animate-tcar15-run group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none motion-reduce:flex-wrap motion-reduce:justify-center motion-reduce:w-auto">
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-1/300/220" width="300" height="220" decoding="async" alt="Studio still life" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-2/300/220" width="300" height="220" decoding="async" alt="Architectural detail" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-3/300/220" width="300" height="220" decoding="async" alt="Textile close-up" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-4/300/220" width="300" height="220" decoding="async" alt="Product on plinth" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-1/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-2/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-3/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-4/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
    </ul>
    <ul class="list-none flex gap-4 w-max m-0 p-0 animate-tcar15-back group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none motion-reduce:flex-wrap motion-reduce:justify-center motion-reduce:w-auto">
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-5/300/220" width="300" height="220" decoding="async" alt="Gradient backdrop" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-6/300/220" width="300" height="220" decoding="async" alt="Ceramic vessels" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-7/300/220" width="300" height="220" decoding="async" alt="Folded paper" class="size-full object-cover block"></li>
      <li class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-8/300/220" width="300" height="220" decoding="async" alt="Woven basket" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-5/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-6/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-7/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
      <li aria-hidden="true" class="flex-none w-[210px] aspect-[15/11] rounded-xl overflow-hidden bg-tcar15-tile"><img src="https://picsum.photos/seed/du-8/300/220" width="300" height="220" loading="lazy" decoding="async" alt="" class="size-full object-cover block"></li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar15-bg: #14121a;
  --color-tcar15-bg: oklch(0.19 0.015 300);
  --color-tcar15-tile: #221f2b;
  --color-tcar15-tile: oklch(0.25 0.018 300);
  --color-tcar15-acc: #f43f5e;
  --color-tcar15-acc: oklch(0.65 0.21 15);
  --font-tcar15-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tcar15-run: tcar15-run 30s linear infinite;
  --animate-tcar15-back: tcar15-run 30s linear infinite reverse;
}

@keyframes tcar15-run {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

.tcar-15 {
  width: 100%;
  min-height: 100svh;
}

.tcar-15 ::selection {
  background: var(--color-tcar15-acc);
  color: #fff;
}
/* Safari < 15.4 mask prefix. */

.tcar15-band {
  -webkit-mask: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}
```
