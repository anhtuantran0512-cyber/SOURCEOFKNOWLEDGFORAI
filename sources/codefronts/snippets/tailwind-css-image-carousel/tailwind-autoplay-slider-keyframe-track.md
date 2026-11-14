---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-autoplay-slider-keyframe-track/"
title: "Tailwind Autoplay Slider with Keyframe Track and Progress Bars"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A hands-off banner that advances itself by translating one track through each slide on a keyframe loop, with progress bars that fill in step."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Autoplay Slider with Keyframe Track and Progress Bars
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-autoplay-slider-keyframe-track/

A hands-off banner that advances itself by translating one track through each slide on a keyframe loop, with progress bars that fill in step. Two animation tokens, three arbitrary delays, and no timer to leak or desync in a background tab.
## HTML
```html
<section class="tcar-20 w-full min-h-svh grid place-items-center bg-tcar20-bg font-tcar20-sans px-5 py-10" aria-label="Auto-rotating banner" aria-roledescription="carousel">
  <div class="group relative w-[min(680px,100%)] rounded-2xl overflow-hidden shadow-[0_26px_50px_-32px_oklch(0_0_0/0.9)]">
    <div class="flex w-[300%] animate-tcar20-slide group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none">
      <div class="w-1/3 aspect-[2/1]"><img src="https://picsum.photos/seed/auto-1/1000/500" width="1000" height="500" fetchpriority="high" decoding="async" alt="Summer sale banner" class="size-full object-cover block"></div>
      <div class="w-1/3 aspect-[2/1]"><img src="https://picsum.photos/seed/auto-2/1000/500" width="1000" height="500" loading="lazy" decoding="async" alt="New arrivals banner" class="size-full object-cover block"></div>
      <div class="w-1/3 aspect-[2/1]"><img src="https://picsum.photos/seed/auto-3/1000/500" width="1000" height="500" loading="lazy" decoding="async" alt="Free shipping banner" class="size-full object-cover block"></div>
    </div>
    <div aria-hidden="true" class="absolute inset-x-3.5 bottom-3.5 flex gap-2 motion-reduce:hidden">
      <span class="relative flex-1 h-1 rounded-full bg-tcar20-track shadow-[0_0_0_1px_oklch(0_0_0/0.28)] overflow-hidden"><span class="absolute inset-0 bg-tcar20-acc origin-left scale-x-0 animate-tcar20-bar group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused]"></span></span>
      <span class="relative flex-1 h-1 rounded-full bg-tcar20-track shadow-[0_0_0_1px_oklch(0_0_0/0.28)] overflow-hidden"><span class="absolute inset-0 bg-tcar20-acc origin-left scale-x-0 animate-tcar20-bar [animation-delay:-10s] group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused]"></span></span>
      <span class="relative flex-1 h-1 rounded-full bg-tcar20-track shadow-[0_0_0_1px_oklch(0_0_0/0.28)] overflow-hidden"><span class="absolute inset-0 bg-tcar20-acc origin-left scale-x-0 animate-tcar20-bar [animation-delay:-5s] group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused]"></span></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar20-bg: #1a0f18;
  --color-tcar20-bg: oklch(0.21 0.035 340);
  --color-tcar20-track: #ffffff;
  --color-tcar20-track: oklch(1 0 0 / 0.4);
  --color-tcar20-acc: #ea4c95;
  --color-tcar20-acc: oklch(0.68 0.2 350);
  --font-tcar20-sans: 'Archivo', system-ui, sans-serif;
  --animate-tcar20-slide: tcar20-slide 15s infinite;
  --animate-tcar20-bar: tcar20-bar 15s infinite;
}

@keyframes tcar20-slide {
  0%,
    28% {
    transform: translateX(0);
  }

  33%,
    61% {
    transform: translateX(-33.3333%);
  }

  66%,
    94% {
    transform: translateX(-66.6666%);
  }

  100% {
    transform: translateX(0);
  }
}

@keyframes tcar20-bar {
  0% {
    transform: scaleX(0);
  }

  28% {
    transform: scaleX(1);
  }

  33%,
    100% {
    transform: scaleX(0);
  }
}

.tcar-20 {
  width: 100%;
  min-height: 100svh;
}

.tcar-20 ::selection {
  background: var(--color-tcar20-acc);
  color: #fff;
}
```
