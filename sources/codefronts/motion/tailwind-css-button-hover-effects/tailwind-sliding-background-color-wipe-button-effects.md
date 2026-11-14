---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-sliding-background-color-wipe-button-effects/"
title: "Tailwind Sliding Background Color Wipe Button Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "The dependable one: a solid colour wipes in and the label colour swaps to stay readable &mdash; the most requested hover in professional product UIs, in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Background Color Wipe Button Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-sliding-background-color-wipe-button-effects/

The dependable one: a solid colour wipes in and the label colour swaps to stay readable &mdash; the most requested hover in professional product UIs, in three directions. The port's whole subtlety is one utility: delay-[120ms] on the label's colour transition.
## HTML
```html
<div class="tbh-12-group w-full min-h-svh flex flex-wrap">
<section class="tbh-12a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh12-sans bg-tbh12a-stage" aria-label="Colour wipe button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh12a-fill px-[38px] py-4 text-base font-bold text-tbh12a-fill bg-transparent transition-colors duration-[250ms] delay-[120ms] before:content-[''] before:absolute before:inset-0 before:z-0 before:bg-tbh12a-fill before:scale-x-0 before:origin-left before:transition-transform before:duration-400 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-tbh12a-onfill hover:before:scale-x-100 focus-visible:text-tbh12a-onfill focus-visible:before:scale-x-100 focus-visible:outline-3 focus-visible:outline-tbh12a-fill focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:before:transition-none">
    <span class="relative z-[1]">Contact sales</span>
  </button>
</section>
<section class="tbh-12b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh12-sans bg-tbh12b-stage" aria-label="Bottom-up fill button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh12b-fill px-[42px] py-[17px] text-base font-extrabold text-tbh12b-fill bg-transparent transition-colors duration-[250ms] delay-[140ms] before:content-[''] before:absolute before:inset-0 before:z-0 before:bg-tbh12b-fill before:scale-y-0 before:origin-bottom before:transition-transform before:duration-[380ms] before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-tbh12b-onfill hover:before:scale-y-100 focus-visible:text-tbh12b-onfill focus-visible:before:scale-y-100 focus-visible:outline-3 focus-visible:outline-tbh12b-fill focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:before:transition-none">
    <span class="relative z-[1]">Get the app</span>
  </button>
</section>
<section class="tbh-12c flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh12-sans bg-tbh12c-stage" aria-label="Center-out fill button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-full border-2 border-tbh12c-fill px-[42px] py-[17px] text-base font-extrabold text-tbh12c-fill bg-transparent transition-colors duration-[250ms] delay-[120ms] before:content-[''] before:absolute before:inset-0 before:z-0 before:bg-tbh12c-fill before:scale-x-0 before:origin-center before:transition-transform before:duration-400 before:ease-[cubic-bezier(.4,0,.2,1)] hover:text-tbh12c-onfill hover:before:scale-x-100 focus-visible:text-tbh12c-onfill focus-visible:before:scale-x-100 focus-visible:outline-3 focus-visible:outline-tbh12c-fill focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:before:transition-none">
    <span class="relative z-[1]">Start trial</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh12a-fill: #3f6ad0;
  --color-tbh12a-fill: oklch(0.55 0.17 255);
  --color-tbh12a-onfill: #ffffff;
  --color-tbh12a-onfill: oklch(1 0 0);
  --color-tbh12a-stage: #eef1f6;
  --color-tbh12a-stage: oklch(0.95 0.008 255);
  --color-tbh12b-fill: #4cb87a;
  --color-tbh12b-fill: oklch(0.6 0.16 150);
  --color-tbh12b-onfill: #04180d;
  --color-tbh12b-onfill: oklch(0.2 0.05 150);
  --color-tbh12b-stage: #0d160f;
  --color-tbh12b-stage: oklch(0.16 0.02 150);
  --color-tbh12c-fill: #d2543c;
  --color-tbh12c-fill: oklch(0.58 0.18 20);
  --color-tbh12c-onfill: #ffffff;
  --color-tbh12c-onfill: oklch(1 0 0);
  --color-tbh12c-stage: #1a0f10;
  --color-tbh12c-stage: oklch(0.18 0.02 20);
  --font-tbh12-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS. Three directions, three origin utilities, one delayed colour swap. */

.tbh-12-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-12a,
.tbh-12b,
.tbh-12c {
  min-height: 100svh;
}
```
