---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-3d-flip-card-button-hover-effect/"
title: "Tailwind 3D Flip Card Button Hover Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A CTA that flips like a physical card: on hover it rotates 180&deg; in 3D to reveal a styled back face with a different label and colour."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Flip Card Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-3d-flip-card-button-hover-effect/

A CTA that flips like a physical card: on hover it rotates 180&deg; in 3D to reveal a styled back face with a different label and colour. Three properties have to be exactly right &mdash; perspective, transform-style and backface-visibility &mdash; and the port puts all three where you can see them.
## HTML
```html
<div class="tbh-23-group w-full min-h-svh flex flex-wrap">
<section class="tbh-23a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh23-sans bg-tbh23a-stage [perspective:900px]" aria-label="3D flip button">
  <button type="button" aria-label="Follow" class="group/btn w-[200px] h-[58px] p-0 cursor-pointer border-0 rounded-xl bg-transparent text-base font-extrabold text-white focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span class="relative block w-full h-full transform-3d transition-[rotate] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover/btn:[rotate:y_180deg] group-focus-visible/btn:[rotate:y_180deg] motion-reduce:transition-none">
      <span class="absolute inset-0 grid place-items-center rounded-xl bg-tbh23a-facea [backface-visibility:hidden]">Follow</span>
      <span aria-hidden="true" class="absolute inset-0 grid place-items-center rounded-xl bg-tbh23a-faceb [backface-visibility:hidden] [rotate:y_180deg]">Following &check;</span>
    </span>
  </button>
</section>
<section class="tbh-23b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh23-sans bg-tbh23b-stage [perspective:700px]" aria-label="3D roll button">
  <button type="button" aria-label="Download" class="group/btn w-[190px] h-[58px] p-0 cursor-pointer border-0 rounded-xl bg-transparent text-base font-extrabold text-white focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span class="relative block w-full h-full transform-3d transition-[rotate] duration-500 ease-[cubic-bezier(.4,0,.2,1)] group-hover/btn:[rotate:x_180deg] group-focus-visible/btn:[rotate:x_180deg] motion-reduce:transition-none">
      <span class="absolute inset-0 grid place-items-center rounded-xl bg-tbh23b-facea [backface-visibility:hidden]">Download</span>
      <span aria-hidden="true" class="absolute inset-0 grid place-items-center rounded-xl bg-tbh23b-faceb [backface-visibility:hidden] [rotate:x_180deg]">Saved &darr;</span>
    </span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh23a-facea: #5470c4;
  --color-tbh23a-facea: oklch(0.55 0.16 265);
  --color-tbh23a-faceb: #4aa878;
  --color-tbh23a-faceb: oklch(0.6 0.15 155);
  --color-tbh23a-stage: #101018;
  --color-tbh23a-stage: oklch(0.15 0.01 285);
  --color-tbh23b-facea: #3e93b8;
  --color-tbh23b-facea: oklch(0.56 0.16 210);
  --color-tbh23b-faceb: #52b07f;
  --color-tbh23b-faceb: oklch(0.62 0.15 145);
  --color-tbh23b-stage: #0a1418;
  --color-tbh23b-stage: oklch(0.14 0.02 210);
  --font-tbh23-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Stays CSS: Safari's prefixed backface-visibility, which has no utility form. */

.tbh-23a span span,
.tbh-23b span span {
  -webkit-backface-visibility: hidden;
}

.tbh-23-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-23a,
.tbh-23b {
  min-height: 100svh;
}
```
