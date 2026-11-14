---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-morph-shape-silhouette-button-effects/"
title: "Tailwind Morph Shape Silhouette Button Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "Three silhouette morphs: sharp corners rounding into a pill, a pill snapping to an asymmetric notch, and a circular icon button expanding into a labelled bar."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Morph Shape Silhouette Button Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-morph-shape-silhouette-button-effects/

Three silhouette morphs: sharp corners rounding into a pill, a pill snapping to an asymmetric notch, and a circular icon button expanding into a labelled bar. The third is the one worth copying &mdash; a floating action button that earns its label on hover.
## HTML
```html
<div class="tbh-30-group w-full min-h-svh flex flex-wrap">
<section class="tbh-30a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh30-sans bg-tbh30a-stage" aria-label="Morph shape button">
  <button type="button" class="cursor-pointer border-0 rounded px-[38px] py-4 text-base font-extrabold text-white bg-tbh30a-acc shadow-[0_10px_22px_-12px_color-mix(in_oklab,var(--color-tbh30a-acc)_70%,transparent)] transition-[border-radius,translate,scale,background-color] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:rounded-[30px] hover:-translate-y-0.5 hover:bg-[color-mix(in_oklab,var(--color-tbh30a-acc)_88%,black)] focus-visible:rounded-[30px] focus-visible:-translate-y-0.5 active:translate-y-0 active:scale-[.98] focus-visible:outline-3 focus-visible:outline-tbh30a-acc focus-visible:outline-offset-4 motion-reduce:transition-[border-radius,background-color] motion-reduce:duration-[250ms] motion-reduce:hover:translate-y-0">
    Send message
  </button>
</section>
<section class="tbh-30b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh30-sans bg-tbh30b-stage" aria-label="Pill to notched button">
  <button type="button" class="cursor-pointer border-0 rounded-[30px] px-10 py-4 text-base font-extrabold text-white bg-tbh30b-acc shadow-[0_12px_24px_-12px_var(--color-tbh30b-acc)] transition-[border-radius,translate,scale] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:[border-radius:16px_4px_16px_4px] hover:-translate-y-0.5 focus-visible:[border-radius:16px_4px_16px_4px] focus-visible:-translate-y-0.5 active:translate-y-0 active:scale-[.98] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:transition-[border-radius] motion-reduce:duration-[250ms] motion-reduce:hover:translate-y-0">
    Reserve seat
  </button>
</section>
<section class="tbh-30c flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh30-sans bg-tbh30c-stage" aria-label="Circle to bar button">
  <button type="button" class="group/btn relative grid place-items-center overflow-hidden h-14 w-14 cursor-pointer border-0 rounded-[28px] text-base font-extrabold text-white bg-tbh30c-acc shadow-[0_12px_24px_-12px_var(--color-tbh30c-acc)] transition-[width,border-radius] duration-[450ms] ease-[cubic-bezier(.4,0,.2,1)] hover:w-[170px] hover:rounded-[14px] focus-visible:w-[170px] focus-visible:rounded-[14px] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:transition-none">
    <span aria-hidden="true" class="text-2xl leading-none transition-opacity duration-200 group-hover/btn:opacity-0 group-hover/btn:duration-150 group-focus-visible/btn:opacity-0">&#65291;</span>
    <span class="absolute whitespace-nowrap opacity-0 transition-opacity duration-200 group-hover/btn:opacity-100 group-hover/btn:delay-[250ms] group-focus-visible/btn:opacity-100 group-focus-visible/btn:delay-[250ms]">Add item</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh30a-acc: #3d8fb8;
  --color-tbh30a-acc: oklch(0.58 0.17 210);
  --color-tbh30a-stage: #f4f6f8;
  --color-tbh30a-stage: oklch(0.97 0.005 220);
  --color-tbh30b-acc: #d4664a;
  --color-tbh30b-acc: oklch(0.6 0.16 25);
  --color-tbh30b-stage: #1a1010;
  --color-tbh30b-stage: oklch(0.18 0.02 25);
  --color-tbh30c-acc: #4aab72;
  --color-tbh30c-acc: oklch(0.62 0.16 150);
  --color-tbh30c-stage: #0c160f;
  --color-tbh30c-stage: oklch(0.15 0.02 150);
  --font-tbh30-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: three radius targets and one width expansion. */

.tbh-30-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-30a,
.tbh-30b,
.tbh-30c {
  min-height: 100svh;
}
```
