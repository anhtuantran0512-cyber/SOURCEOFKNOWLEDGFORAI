---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-stagger-fill-equaliser-button-effect/"
title: "Tailwind Stagger Fill Equaliser Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A rhythmic CTA where several bars rise one after another on hover &mdash; an equaliser sweeping across the button."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stagger Fill Equaliser Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-stagger-fill-equaliser-button-effect/

A rhythmic CTA where several bars rise one after another on hover &mdash; an equaliser sweeping across the button. The stagger used to need four :nth-child rules; here each bar carries its own delay-*, which is both shorter and impossible to misread.
## HTML
```html
<div class="tbh-33-group w-full min-h-svh flex flex-wrap">
<section class="tbh-33a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh33-sans bg-tbh33a-stage" aria-label="Stagger fill button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh33a-bar px-11 py-[17px] text-base font-extrabold text-tbh33a-bar bg-transparent transition-colors duration-[250ms] delay-[160ms] hover:text-tbh33a-onbar focus-visible:text-tbh33a-onbar focus-visible:outline-3 focus-visible:outline-tbh33a-bar focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute inset-0 z-0 flex">
      <i class="flex-1 bg-tbh33a-bar scale-y-0 origin-bottom transition-[scale] duration-300 ease-out delay-0 group-hover/btn:scale-y-100 group-focus-visible/btn:scale-y-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33a-bar scale-y-0 origin-bottom transition-[scale] duration-300 ease-out delay-[50ms] group-hover/btn:scale-y-100 group-focus-visible/btn:scale-y-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33a-bar scale-y-0 origin-bottom transition-[scale] duration-300 ease-out delay-100 group-hover/btn:scale-y-100 group-focus-visible/btn:scale-y-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33a-bar scale-y-0 origin-bottom transition-[scale] duration-300 ease-out delay-150 group-hover/btn:scale-y-100 group-focus-visible/btn:scale-y-100 motion-reduce:transition-none"></i>
    </span>
    <span class="relative z-[1]">Play set</span>
  </button>
</section>
<section class="tbh-33b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh33-sans bg-tbh33b-stage" aria-label="Horizontal blinds fill button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh33b-bar px-[46px] py-[18px] text-base font-extrabold text-tbh33b-bar bg-transparent transition-colors duration-[250ms] delay-[180ms] hover:text-tbh33b-onbar focus-visible:text-tbh33b-onbar focus-visible:outline-3 focus-visible:outline-tbh33b-bar focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute inset-0 z-0 flex flex-col">
      <i class="flex-1 bg-tbh33b-bar scale-x-0 origin-left transition-[scale] duration-[320ms] ease-out delay-0 group-hover/btn:scale-x-100 group-focus-visible/btn:scale-x-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33b-bar scale-x-0 origin-right transition-[scale] duration-[320ms] ease-out delay-[60ms] group-hover/btn:scale-x-100 group-focus-visible/btn:scale-x-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33b-bar scale-x-0 origin-left transition-[scale] duration-[320ms] ease-out delay-[120ms] group-hover/btn:scale-x-100 group-focus-visible/btn:scale-x-100 motion-reduce:transition-none"></i>
      <i class="flex-1 bg-tbh33b-bar scale-x-0 origin-right transition-[scale] duration-[320ms] ease-out delay-[180ms] group-hover/btn:scale-x-100 group-focus-visible/btn:scale-x-100 motion-reduce:transition-none"></i>
    </span>
    <span class="relative z-[1]">Reveal</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh33a-bar: #63d98f;
  --color-tbh33a-bar: oklch(0.8 0.19 145);
  --color-tbh33a-onbar: #04170d;
  --color-tbh33a-onbar: oklch(0.2 0.05 145);
  --color-tbh33a-stage: #0a120c;
  --color-tbh33a-stage: oklch(0.14 0.015 145);
  --color-tbh33b-bar: #7a6ce0;
  --color-tbh33b-bar: oklch(0.62 0.17 280);
  --color-tbh33b-onbar: #ffffff;
  --color-tbh33b-onbar: oklch(1 0 0);
  --color-tbh33b-stage: #0d0a1a;
  --color-tbh33b-stage: oklch(0.14 0.025 280);
  --font-tbh33-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: the four :nth-child delay rules became four delay-* utilities. */

.tbh-33-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-33a,
.tbh-33b {
  min-height: 100svh;
}
```
