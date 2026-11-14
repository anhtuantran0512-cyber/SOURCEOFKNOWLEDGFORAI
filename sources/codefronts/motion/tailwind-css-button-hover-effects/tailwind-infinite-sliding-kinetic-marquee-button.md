---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-infinite-sliding-kinetic-marquee-button/"
title: "Tailwind Infinite Sliding Kinetic Marquee Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A kinetic editorial CTA that trades a static label for a continuously scrolling marquee on hover &mdash; the phrase repeats and slides endlessly across the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Infinite Sliding Kinetic Marquee Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-infinite-sliding-kinetic-marquee-button/

A kinetic editorial CTA that trades a static label for a continuously scrolling marquee on hover &mdash; the phrase repeats and slides endlessly across the pill. The port's real work is accessibility: the scrolling copies are aria-hidden decoration and the accessible name comes from aria-label, so what a screen reader hears never moves.
## HTML
```html
<div class="tbh-07-group w-full min-h-svh flex flex-wrap">
<section class="tbh-07a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh07-sans bg-tbh07a-stage" aria-label="Kinetic marquee button">
  <button type="button" aria-label="Book tickets" class="group/btn relative overflow-hidden w-[230px] h-[60px] cursor-pointer border-0 rounded-full text-base font-extrabold tracking-[0.04em] text-white bg-tbh07a-acc focus-visible:outline-3 focus-visible:outline-tbh07a-acc focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute inset-0 grid place-items-center transition-opacity duration-200 group-hover/btn:opacity-0 group-focus-visible/btn:opacity-0 motion-reduce:group-hover/btn:opacity-100 motion-reduce:group-focus-visible/btn:opacity-100">Book tickets</span>
    <span aria-hidden="true" class="absolute inset-0 flex items-center gap-[34px] pl-[34px] whitespace-nowrap opacity-0 transition-opacity duration-200 group-hover/btn:opacity-100 group-hover/btn:animate-tbh07a-scroll group-focus-visible/btn:opacity-100 group-focus-visible/btn:animate-tbh07a-scroll motion-reduce:group-hover/btn:animate-none motion-reduce:group-hover/btn:opacity-0 motion-reduce:group-focus-visible/btn:animate-none motion-reduce:group-focus-visible/btn:opacity-0">
      <span>Book tickets</span><span>Book tickets</span><span>Book tickets</span><span>Book tickets</span>
    </span>
  </button>
</section>
<section class="tbh-07b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh07-sans bg-tbh07b-stage" aria-label="Vertical marquee button">
  <button type="button" aria-label="Shop the drop" class="group/btn relative overflow-hidden w-[220px] h-[58px] cursor-pointer border-0 rounded-xl text-base font-extrabold text-white bg-tbh07b-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute inset-0 flex flex-col group-hover/btn:animate-tbh07b-roll group-focus-visible/btn:animate-tbh07b-roll motion-reduce:group-hover/btn:animate-none motion-reduce:group-focus-visible/btn:animate-none">
      <span class="grid place-items-center h-[58px] flex-none">Shop the drop</span>
      <span class="grid place-items-center h-[58px] flex-none">Shop the drop</span>
    </span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh07a-acc: #c8344a;
  --color-tbh07a-acc: oklch(0.55 0.2 15);
  --color-tbh07a-stage: #faf7f2;
  --color-tbh07a-stage: oklch(0.97 0.008 80);
  --color-tbh07b-acc: #6e5ad8;
  --color-tbh07b-acc: oklch(0.55 0.18 285);
  --color-tbh07b-stage: #0e0b1a;
  --color-tbh07b-stage: oklch(0.15 0.03 285);
  --font-tbh07-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh07a-scroll: tbh07a-scroll 6s linear infinite;
  --animate-tbh07b-roll: tbh07b-roll 1.6s linear infinite;
}
/* Stays CSS: the two loop keyframes. Both write the discrete translate property, so they
   cannot collide with a translate-* utility added to the same track later. */

@keyframes tbh07a-scroll {
  from {
    translate: 0 0;
  }

  to {
    translate: -50% 0;
  }
}

@keyframes tbh07b-roll {
  from {
    translate: 0 0;
  }

  to {
    translate: 0 -58px;
  }
}

.tbh-07-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-07a,
.tbh-07b {
  min-height: 100svh;
}
```
