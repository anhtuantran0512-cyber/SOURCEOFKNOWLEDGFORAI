---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-slide-doors-closing-panel-button-effect/"
title: "Tailwind Slide Doors Closing Panel Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A CTA where two coloured panels slide in from the left and right to meet in the exact centre on hover &mdash; like closing doors &mdash; restyling the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide Doors Closing Panel Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-slide-doors-closing-panel-button-effect/

A CTA where two coloured panels slide in from the left and right to meet in the exact centre on hover &mdash; like closing doors &mdash; restyling the surface as they seal. The inward counterpart to entry 19's outward split, and the pair is worth reading together.
## HTML
```html
<div class="tbh-25-group w-full min-h-svh flex flex-wrap">
<section class="tbh-25a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh25-sans bg-tbh25a-stage" aria-label="Slide doors button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh25a-door px-[42px] py-[17px] text-base font-extrabold text-tbh25a-door bg-white transition-colors duration-[250ms] delay-[180ms] before:content-[''] before:absolute before:top-0 before:left-0 before:w-1/2 before:h-full before:z-0 before:bg-tbh25a-door before:-translate-x-[101%] before:transition-[translate] before:duration-[350ms] before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[''] after:absolute after:top-0 after:right-0 after:w-1/2 after:h-full after:z-0 after:bg-tbh25a-door after:translate-x-[101%] after:transition-[translate] after:duration-[350ms] after:ease-[cubic-bezier(.4,0,.2,1)] hover:text-tbh25a-ondoor hover:before:translate-x-0 hover:after:translate-x-0 focus-visible:text-tbh25a-ondoor focus-visible:before:translate-x-0 focus-visible:after:translate-x-0 focus-visible:outline-3 focus-visible:outline-tbh25a-door focus-visible:outline-offset-[3px] motion-reduce:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span class="relative z-[1]">Open account</span>
  </button>
</section>
<section class="tbh-25b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh25-sans bg-tbh25b-stage" aria-label="Vertical shutter doors button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-[10px] border-2 border-tbh25b-door px-11 py-[18px] text-base font-extrabold text-tbh25b-door bg-white transition-colors duration-[250ms] delay-[180ms] before:content-[''] before:absolute before:left-0 before:top-0 before:w-full before:h-1/2 before:z-0 before:bg-tbh25b-door before:-translate-y-[101%] before:transition-[translate] before:duration-[350ms] before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[''] after:absolute after:left-0 after:bottom-0 after:w-full after:h-1/2 after:z-0 after:bg-tbh25b-door after:translate-y-[101%] after:transition-[translate] after:duration-[350ms] after:ease-[cubic-bezier(.4,0,.2,1)] hover:text-tbh25b-ondoor hover:before:translate-y-0 hover:after:translate-y-0 focus-visible:text-tbh25b-ondoor focus-visible:before:translate-y-0 focus-visible:after:translate-y-0 focus-visible:outline-3 focus-visible:outline-tbh25b-door focus-visible:outline-offset-[3px] motion-reduce:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span class="relative z-[1]">Reveal offer</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh25a-door: #7a4fc0;
  --color-tbh25a-door: oklch(0.55 0.15 300);
  --color-tbh25a-ondoor: #ffffff;
  --color-tbh25a-ondoor: oklch(1 0 0);
  --color-tbh25a-stage: #f2eef8;
  --color-tbh25a-stage: oklch(0.95 0.015 300);
  --color-tbh25b-door: #3d94a4;
  --color-tbh25b-door: oklch(0.58 0.16 200);
  --color-tbh25b-ondoor: #03181c;
  --color-tbh25b-ondoor: oklch(0.2 0.03 200);
  --color-tbh25b-stage: #e6f2f4;
  --color-tbh25b-stage: oklch(0.95 0.015 200);
  --font-tbh25-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: two half-panels and one translate each. */

.tbh-25-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-25a,
.tbh-25b {
  min-height: 100svh;
}
```
