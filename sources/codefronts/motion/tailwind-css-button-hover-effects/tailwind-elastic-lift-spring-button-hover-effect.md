---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-elastic-lift-spring-button-hover-effect/"
title: "Tailwind Elastic Lift Spring Button Hover Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A bouncy, delightful CTA that springs up on hover &mdash; it lifts, squashes slightly and overshoots before settling."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elastic Lift Spring Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-elastic-lift-spring-button-hover-effect/

A bouncy, delightful CTA that springs up on hover &mdash; it lifts, squashes slightly and overshoots before settling. The squash is the part most implementations skip, and in v4 it is one utility (hover:scale-x-[1.04] hover:scale-y-[.96]) that no longer has to repeat the lift.
## HTML
```html
<div class="tbh-21-group w-full min-h-svh flex flex-wrap">
<section class="tbh-21a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh21-sans bg-tbh21a-stage" aria-label="Elastic lift button">
  <button type="button" class="cursor-pointer border-0 rounded-[14px] px-[42px] py-[18px] text-[17px] font-extrabold text-white bg-tbh21a-acc shadow-[0_8px_16px_-8px_color-mix(in_oklab,var(--color-tbh21a-acc)_70%,transparent)] transition-[translate,scale,box-shadow] duration-[450ms] ease-[cubic-bezier(.68,-.6,.32,1.6)] hover:-translate-y-1.5 hover:scale-x-[1.04] hover:scale-y-[.96] hover:shadow-[0_22px_30px_-12px_color-mix(in_oklab,var(--color-tbh21a-acc)_65%,transparent)] focus-visible:-translate-y-1.5 focus-visible:scale-x-[1.04] focus-visible:scale-y-[.96] active:-translate-y-px active:scale-[.97] active:duration-[120ms] focus-visible:outline-3 focus-visible:outline-tbh21a-acc focus-visible:outline-offset-4 motion-reduce:transition-[box-shadow] motion-reduce:duration-200 motion-reduce:hover:-translate-y-[3px] motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
    Join the fun
  </button>
</section>
<section class="tbh-21b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh21-sans bg-tbh21b-stage" aria-label="Wobble tilt button">
  <button type="button" class="cursor-pointer border-0 rounded-[14px] px-[42px] py-[18px] text-[17px] font-extrabold text-white bg-tbh21b-acc shadow-[0_10px_20px_-10px_var(--color-tbh21b-acc)] transition-[scale] duration-200 hover:animate-tbh21b-wob focus-visible:animate-tbh21b-wob active:scale-[.96] focus-visible:outline-3 focus-visible:outline-tbh21b-acc focus-visible:outline-offset-4 motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:scale-[1.03]">
    Say cheese
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh21a-acc: #ef8347;
  --color-tbh21a-acc: oklch(0.68 0.19 40);
  --color-tbh21a-stage: #fff5ec;
  --color-tbh21a-stage: oklch(0.97 0.02 60);
  --color-tbh21b-acc: #d966c4;
  --color-tbh21b-acc: oklch(0.66 0.18 320);
  --color-tbh21b-stage: #fbeffa;
  --color-tbh21b-stage: oklch(0.96 0.02 320);
  --font-tbh21-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh21b-wob: tbh21b-wob 0.5s cubic-bezier(.36,.07,.19,.97);
}
/* Stays CSS: the one-shot wobble. It writes rotate and scale as discrete properties, so it
   composes with the button's own active:scale utility instead of overwriting it. */

@keyframes tbh21b-wob {
  0% {
    rotate: 0deg;
    scale: 1;
  }

  25% {
    rotate: -4deg;
    scale: 1.05;
  }

  50% {
    rotate: 3deg;
    scale: 1.03;
  }

  75% {
    rotate: -2deg;
    scale: 1.02;
  }

  100% {
    rotate: 0deg;
    scale: 1;
  }
}

.tbh-21-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-21a,
.tbh-21b {
  min-height: 100svh;
}
```
