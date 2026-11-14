---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-diagonal-shutter-sweep-button-effect/"
title: "Tailwind Diagonal Shutter Sweep Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A dynamic CTA where a skewed colour panel sweeps across on hover like a diagonal shutter closing over the surface, with the label swapping colour as it passes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Diagonal Shutter Sweep Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-diagonal-shutter-sweep-button-effect/

A dynamic CTA where a skewed colour panel sweeps across on hover like a diagonal shutter closing over the surface, with the label swapping colour as it passes. In v4 the skew and the sweep are separate properties, so the blade's angle is stated once instead of in every state.
## HTML
```html
<div class="tbh-20-group w-full min-h-svh flex flex-wrap">
<section class="tbh-20a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh20-sans bg-tbh20a-stage" aria-label="Diagonal shutter button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-lg border-2 border-tbh20a-blade px-10 py-[17px] text-base font-extrabold tracking-[0.03em] text-tbh20a-blade bg-tbh20a-panel transition-colors duration-300 delay-[120ms] before:content-[''] before:absolute before:-top-[20%] before:-left-[20%] before:w-[140%] before:h-[140%] before:z-0 before:bg-tbh20a-blade before:skew-x-[-20deg] before:scale-x-0 before:origin-center before:transition-[scale] before:duration-[450ms] before:ease-[cubic-bezier(.5,0,.2,1)] hover:text-tbh20a-onblade hover:before:scale-x-100 focus-visible:text-tbh20a-onblade focus-visible:before:scale-x-100 focus-visible:outline-3 focus-visible:outline-tbh20a-blade focus-visible:outline-offset-4 motion-reduce:transition-colors motion-reduce:delay-0 motion-reduce:before:transition-none">
    <span class="relative z-[1]">View gallery</span>
  </button>
</section>
<section class="tbh-20b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh20-sans bg-tbh20b-stage" aria-label="Twin shutter button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer rounded-lg border-2 border-tbh20b-blade px-[42px] py-[17px] text-base font-extrabold text-tbh20b-blade bg-transparent transition-colors duration-300 delay-[140ms] before:content-[''] before:absolute before:-top-[30%] before:-left-[20%] before:h-[160%] before:w-[70%] before:z-0 before:bg-tbh20b-blade before:skew-x-[-18deg] before:scale-x-0 before:origin-left before:transition-[scale] before:duration-400 before:ease-[cubic-bezier(.5,0,.2,1)] after:content-[''] after:absolute after:-top-[30%] after:-right-[20%] after:h-[160%] after:w-[70%] after:z-0 after:bg-tbh20b-blade after:skew-x-[-18deg] after:scale-x-0 after:origin-right after:transition-[scale] after:duration-400 after:ease-[cubic-bezier(.5,0,.2,1)] hover:text-tbh20b-onblade hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:text-tbh20b-onblade focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 focus-visible:outline-3 focus-visible:outline-tbh20b-blade focus-visible:outline-offset-4 motion-reduce:transition-colors motion-reduce:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span class="relative z-[1]">Book demo</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh20a-blade: #171717;
  --color-tbh20a-blade: oklch(0.18 0 0);
  --color-tbh20a-onblade: #ffffff;
  --color-tbh20a-onblade: oklch(1 0 0);
  --color-tbh20a-panel: #f7f5f0;
  --color-tbh20a-panel: oklch(0.97 0.006 90);
  --color-tbh20a-stage: #e9e6dd;
  --color-tbh20a-stage: oklch(0.92 0.01 90);
  --color-tbh20b-blade: #3f6ad0;
  --color-tbh20b-blade: oklch(0.55 0.17 255);
  --color-tbh20b-onblade: #ffffff;
  --color-tbh20b-onblade: oklch(1 0 0);
  --color-tbh20b-stage: #0b1220;
  --color-tbh20b-stage: oklch(0.14 0.02 255);
  --font-tbh20-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: the skew is a persistent utility and only the scale animates. */

.tbh-20-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-20a,
.tbh-20b {
  min-height: 100svh;
}
```
