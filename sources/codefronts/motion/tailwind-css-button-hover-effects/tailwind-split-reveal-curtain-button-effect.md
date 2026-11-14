---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-split-reveal-curtain-button-effect/"
title: "Tailwind Split Reveal Curtain Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A theatrical CTA: on hover the surface splits into halves that slide apart, revealing a contrasting label behind &mdash; an outward curtain."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Split Reveal Curtain Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-split-reveal-curtain-button-effect/

A theatrical CTA: on hover the surface splits into halves that slide apart, revealing a contrasting label behind &mdash; an outward curtain. Both front halves are one data-front attribute clipped twice, so the front copy can never disagree with itself.
## HTML
```html
<div class="tbh-19-group w-full min-h-svh flex flex-wrap">
<section class="tbh-19a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh19-sans bg-tbh19a-stage" aria-label="Split reveal button">
  <button type="button" data-front="Hover me" class="relative overflow-hidden cursor-pointer border-0 rounded-xl px-11 py-[18px] text-base font-extrabold text-tbh19a-backink bg-tbh19a-back focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 before:content-[attr(data-front)] before:absolute before:inset-0 before:grid before:place-items-center before:text-white before:bg-tbh19a-front before:z-[1] before:[clip-path:inset(0_0_calc(50%-1px)_0)] before:transition-[translate] before:duration-400 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-front)] after:absolute after:inset-0 after:grid after:place-items-center after:text-white after:bg-tbh19a-front after:z-[1] after:[clip-path:inset(calc(50%-1px)_0_0_0)] after:transition-[translate] after:duration-400 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-y-full hover:after:translate-y-full focus-visible:before:-translate-y-full focus-visible:after:translate-y-full motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span class="relative z-0">Let's go &rarr;</span>
  </button>
</section>
<section class="tbh-19b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh19-sans bg-tbh19b-stage" aria-label="Vertical split reveal button">
  <button type="button" data-front="Reveal" class="relative overflow-hidden cursor-pointer border-0 rounded-xl px-[46px] py-[18px] text-base font-extrabold text-tbh19b-backink bg-tbh19b-back focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 before:content-[attr(data-front)] before:absolute before:inset-0 before:grid before:place-items-center before:text-white before:bg-tbh19b-front before:z-[1] before:[clip-path:inset(0_calc(50%-1px)_0_0)] before:transition-[translate] before:duration-400 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[attr(data-front)] after:absolute after:inset-0 after:grid after:place-items-center after:text-white after:bg-tbh19b-front after:z-[1] after:[clip-path:inset(0_0_0_calc(50%-1px))] after:transition-[translate] after:duration-400 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:-translate-x-full hover:after:translate-x-full focus-visible:before:-translate-x-full focus-visible:after:translate-x-full motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span class="relative z-0">Unlock &#10022;</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh19a-front: #6a4fc4;
  --color-tbh19a-front: oklch(0.5 0.16 285);
  --color-tbh19a-back: #74dba0;
  --color-tbh19a-back: oklch(0.82 0.17 145);
  --color-tbh19a-backink: #04140b;
  --color-tbh19a-backink: oklch(0.2 0.05 145);
  --color-tbh19a-stage: #0d0b1a;
  --color-tbh19a-stage: oklch(0.15 0.03 285);
  --color-tbh19b-front: #b8503a;
  --color-tbh19b-front: oklch(0.52 0.16 25);
  --color-tbh19b-back: #dcae4e;
  --color-tbh19b-back: oklch(0.8 0.15 85);
  --color-tbh19b-backink: #1a1206;
  --color-tbh19b-backink: oklch(0.22 0.04 85);
  --color-tbh19b-stage: #160b0a;
  --color-tbh19b-stage: oklch(0.17 0.02 25);
  --font-tbh19-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: two clipped attr() halves and one translate each. */

.tbh-19-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-19a,
.tbh-19b {
  min-height: 100svh;
}
```
