---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-testimonial-card-carousel-star-ratings/"
title: "Tailwind Testimonial Card Carousel with Star Ratings"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A swipeable rail of review cards — star rating, quote, avatar — snapping one per view on mobile and two-up wide."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Testimonial Card Carousel with Star Ratings
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-testimonial-card-carousel-star-ratings/

A swipeable rail of review cards — star rating, quote, avatar — snapping one per view on mobile and two-up wide. The half-star rating is a masked bar rather than five glyphs, which means a 4.5 needs no extra image and no icon font.
## HTML
```html
<section class="tcar-06 w-full min-h-svh grid place-items-center bg-tcar06-bg font-tcar06-sans px-3 py-10" aria-label="Customer testimonials">
  <ul tabindex="0" role="group" aria-label="Customer reviews, scrollable" class="list-none flex gap-[18px] w-[min(760px,100%)] overflow-x-auto p-2.5 m-0 snap-x snap-mandatory [scroll-padding:10px] [scrollbar-width:thin] [scrollbar-color:var(--color-tcar06-track)_transparent] focus-visible:outline-3 focus-visible:outline-tcar06-acc focus-visible:outline-offset-2 focus-visible:rounded-2xl">
    <li class="flex-none basis-[clamp(240px,82%,320px)] sm:basis-[calc((100%-18px)/2)] snap-center bg-white border border-tcar06-edge rounded-[18px] px-[22px] py-6 shadow-[0_16px_34px_-28px_oklch(0.3_0.08_290/0.7)] transition-[translate] duration-250 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Rated 5 out of 5" class="relative w-28 h-[18px] bg-tcar06-startrack tcar06-stars"><span style="width:100%" class="absolute inset-y-0 left-0 block bg-tcar06-star"></span></div>
      <p class="mt-4 mb-5 text-[15px] leading-[1.55] text-tcar06-ink text-pretty">&ldquo;Swapped our slider library for this and shaved 40&nbsp;KB off the bundle. Scroll feel is better than what we replaced.&rdquo;</p>
      <div class="flex items-center gap-3"><img src="https://picsum.photos/seed/ava-1/96/96" width="96" height="96" loading="lazy" decoding="async" alt="" class="size-11 rounded-full object-cover flex-none bg-tcar06-edge"><span><b class="block text-sm text-tcar06-ink">Priya N.</b><small class="block text-xs text-tcar06-mute mt-px">Front-end Lead, UK</small></span></div>
    </li>
    <li class="flex-none basis-[clamp(240px,82%,320px)] sm:basis-[calc((100%-18px)/2)] snap-center bg-white border border-tcar06-edge rounded-[18px] px-[22px] py-6 shadow-[0_16px_34px_-28px_oklch(0.3_0.08_290/0.7)] transition-[translate] duration-250 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Rated 4.5 out of 5" class="relative w-28 h-[18px] bg-tcar06-startrack tcar06-stars"><span style="width:90%" class="absolute inset-y-0 left-0 block bg-tcar06-star"></span></div>
      <p class="mt-4 mb-5 text-[15px] leading-[1.55] text-tcar06-ink text-pretty">&ldquo;Perfect CLS score after switching to the aspect-ratio pattern here. Copy-paste took ten minutes.&rdquo;</p>
      <div class="flex items-center gap-3"><img src="https://picsum.photos/seed/ava-2/96/96" width="96" height="96" loading="lazy" decoding="async" alt="" class="size-11 rounded-full object-cover flex-none bg-tcar06-edge"><span><b class="block text-sm text-tcar06-ink">Marcus T.</b><small class="block text-xs text-tcar06-mute mt-px">Web Dev, US</small></span></div>
    </li>
    <li class="flex-none basis-[clamp(240px,82%,320px)] sm:basis-[calc((100%-18px)/2)] snap-center bg-white border border-tcar06-edge rounded-[18px] px-[22px] py-6 shadow-[0_16px_34px_-28px_oklch(0.3_0.08_290/0.7)] transition-[translate] duration-250 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Rated 5 out of 5" class="relative w-28 h-[18px] bg-tcar06-startrack tcar06-stars"><span style="width:100%" class="absolute inset-y-0 left-0 block bg-tcar06-star"></span></div>
      <p class="mt-4 mb-5 text-[15px] leading-[1.55] text-tcar06-ink text-pretty">&ldquo;Finally a carousel my keyboard users can actually operate. Focus ring and arrow keys just work.&rdquo;</p>
      <div class="flex items-center gap-3"><img src="https://picsum.photos/seed/ava-3/96/96" width="96" height="96" loading="lazy" decoding="async" alt="" class="size-11 rounded-full object-cover flex-none bg-tcar06-edge"><span><b class="block text-sm text-tcar06-ink">Alira K.</b><small class="block text-xs text-tcar06-mute mt-px">UX Engineer, AU</small></span></div>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar06-bg: #f5f4f9;
  --color-tcar06-bg: oklch(0.96 0.006 290);
  --color-tcar06-edge: #e9e7f1;
  --color-tcar06-edge: oklch(0.92 0.01 290);
  --color-tcar06-track: #d5d2e2;
  --color-tcar06-track: oklch(0.86 0.015 290);
  --color-tcar06-startrack: #e4e2ee;
  --color-tcar06-startrack: oklch(0.91 0.012 290);
  --color-tcar06-star: #d98b00;
  --color-tcar06-star: oklch(0.72 0.15 75);
  --color-tcar06-ink: #33303d;
  --color-tcar06-ink: oklch(0.32 0.015 290);
  --color-tcar06-mute: #6f6a80;
  --color-tcar06-mute: oklch(0.55 0.02 290);
  --color-tcar06-acc: #6d54c7;
  --color-tcar06-acc: oklch(0.52 0.16 290);
  --font-tcar06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tcar-06 {
  width: 100%;
  min-height: 100svh;
}

.tcar-06 ::selection {
  background: var(--color-tcar06-acc);
  color: #fff;
}
/* The star mask: a data-URI repeat, too long and too structural to live in a class list. */

.tcar06-stars {
  -webkit-mask: repeat-x left/22.4px 18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 6.3 6.9.9-5 4.8 1.2 6.9L12 17.7 5.9 20.9 7.1 14 2.1 9.2 9 8.3z'/%3E%3C/svg%3E");
  mask: repeat-x left/22.4px 18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 6.3 6.9.9-5 4.8 1.2 6.9L12 17.7 5.9 20.9 7.1 14 2.1 9.2 9 8.3z'/%3E%3C/svg%3E");
}

@media (prefers-reduced-motion: reduce) {
  .tcar-06 ul {
    scroll-behavior: auto;
  }
}
```
