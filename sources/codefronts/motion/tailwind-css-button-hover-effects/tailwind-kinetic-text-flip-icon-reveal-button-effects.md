---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-kinetic-text-flip-icon-reveal-button-effects/"
title: "Tailwind Kinetic Text Flip & Icon Reveal Button Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A snappy micro-interaction: on hover the label slides up and out while a second line or icon slides up to replace it, inside a clipped window &mdash; the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Kinetic Text Flip & Icon Reveal Button Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-kinetic-text-flip-icon-reveal-button-effects/

A snappy micro-interaction: on hover the label slides up and out while a second line or icon slides up to replace it, inside a clipped window &mdash; the 'Add to cart &rarr; Added &check;' pattern. The port's discipline is accessibility: the second row is aria-hidden, so the accessible name never changes under the user.
## HTML
```html
<div class="tbh-14-group w-full min-h-svh flex flex-wrap">
<section class="tbh-14a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh14-sans bg-tbh14a-stage" aria-label="Text flip reveal button">
  <button type="button" class="group/btn overflow-hidden h-14 min-w-[180px] cursor-pointer border-0 rounded-xl p-0 text-base font-extrabold text-white bg-tbh14a-acc focus-visible:outline-3 focus-visible:outline-tbh14a-acc focus-visible:outline-offset-[3px]">
    <span class="flex flex-col w-full transition-[translate] duration-400 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:-translate-y-1/2 group-focus-visible/btn:-translate-y-1/2 motion-reduce:transition-none">
      <span class="flex items-center justify-center h-14 w-full px-10">Add to cart</span>
      <span aria-hidden="true" class="flex items-center justify-center h-14 w-full px-10 bg-tbh14a-deep">Added&nbsp;&check;</span>
    </span>
  </button>
</section>
<section class="tbh-14b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh14-sans bg-tbh14b-stage" aria-label="Label to icon button">
  <button type="button" aria-label="Next step" class="group/btn overflow-hidden h-14 w-[180px] cursor-pointer border-0 rounded-full text-base font-extrabold text-white bg-tbh14b-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[3px]">
    <span class="flex flex-col transition-[translate] duration-[380ms] ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:-translate-y-[56px] group-focus-visible/btn:-translate-y-[56px] motion-reduce:transition-none">
      <span class="flex items-center justify-center h-14 text-base">Next step</span>
      <span aria-hidden="true" class="flex items-center justify-center h-14 text-xl">&rarr;</span>
    </span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh14a-acc: #4a9e6e;
  --color-tbh14a-acc: oklch(0.58 0.15 155);
  --color-tbh14a-deep: #3d8a5e;
  --color-tbh14a-deep: oklch(0.5 0.15 155);
  --color-tbh14a-stage: #0f1512;
  --color-tbh14a-stage: oklch(0.17 0.015 155);
  --color-tbh14b-acc: #6155db;
  --color-tbh14b-acc: oklch(0.56 0.17 275);
  --color-tbh14b-stage: #0d0b1a;
  --color-tbh14b-stage: oklch(0.15 0.03 275);
  --font-tbh14-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: a clipped window, a flex column and one translate per design. */

.tbh-14-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-14a,
.tbh-14b {
  min-height: 100svh;
}
```
