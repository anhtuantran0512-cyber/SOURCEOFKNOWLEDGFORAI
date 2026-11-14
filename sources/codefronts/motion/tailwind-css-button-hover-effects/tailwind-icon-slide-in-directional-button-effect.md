---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-icon-slide-in-directional-button-effect/"
title: "Tailwind Icon Slide In Directional Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A directional CTA where the label nudges aside and an arrow slides in from outside the edge on hover &mdash; a purposeful 'forward' cue for Next and Continue…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Slide In Directional Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-icon-slide-in-directional-button-effect/

A directional CTA where the label nudges aside and an arrow slides in from outside the edge on hover &mdash; a purposeful 'forward' cue for Next and Continue actions. The icon animates width from 0, which is the one honest way to make it claim space without the label jumping.
## HTML
```html
<div class="tbh-31-group w-full min-h-svh flex flex-wrap">
<section class="tbh-31a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh31-sans bg-tbh31a-stage" aria-label="Icon slide in button">
  <button type="button" class="group/btn inline-flex items-center justify-center overflow-hidden cursor-pointer border-0 rounded-[10px] px-[34px] py-4 text-base font-extrabold text-white bg-tbh31a-acc focus-visible:outline-3 focus-visible:outline-tbh31a-acc focus-visible:outline-offset-4">
    <span class="transition-[translate] duration-300 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:-translate-x-1 group-focus-visible/btn:-translate-x-1 motion-reduce:transition-none">Continue</span>
    <span aria-hidden="true" class="w-0 ml-0 overflow-hidden text-lg opacity-0 -translate-x-1.5 transition-[width,margin,translate,opacity] duration-300 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:w-[18px] group-hover/btn:ml-2 group-hover/btn:opacity-100 group-hover/btn:translate-x-0 group-focus-visible/btn:w-[18px] group-focus-visible/btn:ml-2 group-focus-visible/btn:opacity-100 group-focus-visible/btn:translate-x-0 motion-reduce:transition-[opacity]">&rarr;</span>
  </button>
</section>
<section class="tbh-31b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh31-sans bg-tbh31b-stage" aria-label="Icon swap button">
  <button type="button" class="group/btn inline-flex items-center justify-center overflow-hidden cursor-pointer border-0 rounded-[10px] px-[34px] py-4 text-base font-extrabold text-white bg-tbh31b-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span aria-hidden="true" class="w-0 mr-0 overflow-hidden text-lg opacity-0 translate-x-1.5 transition-[width,margin,translate,opacity] duration-300 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:w-[18px] group-hover/btn:mr-2 group-hover/btn:opacity-100 group-hover/btn:translate-x-0 group-focus-visible/btn:w-[18px] group-focus-visible/btn:mr-2 group-focus-visible/btn:opacity-100 group-focus-visible/btn:translate-x-0 motion-reduce:transition-[opacity]">&darr;</span>
    <span class="transition-[translate] duration-300 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:translate-x-1 group-focus-visible/btn:translate-x-1 motion-reduce:transition-none">Save file</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh31a-acc: #6154c8;
  --color-tbh31a-acc: oklch(0.55 0.17 275);
  --color-tbh31a-stage: #eef0f6;
  --color-tbh31a-stage: oklch(0.95 0.008 275);
  --color-tbh31b-acc: #3d94a0;
  --color-tbh31b-acc: oklch(0.58 0.15 200);
  --color-tbh31b-stage: #0a1618;
  --color-tbh31b-stage: oklch(0.15 0.02 200);
  --font-tbh31-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: a zero-width icon growing into a flex row. */

.tbh-31-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-31a,
.tbh-31b {
  min-height: 100svh;
}
```
