---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-liquid-wave-fill-button-hover-effect/"
title: "Tailwind Liquid Wave Fill Button Hover Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A CTA that fills like a glass of water: on hover a coloured liquid rises from the bottom with a scalloped wave crest that sways &mdash; the bottom-up fill,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Wave Fill Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-liquid-wave-fill-button-hover-effect/

A CTA that fills like a glass of water: on hover a coloured liquid rises from the bottom with a scalloped wave crest that sways &mdash; the bottom-up fill, distinct from entry 13's centre-out blob. The crest is a repeating radial-gradient, which is the trick worth stealing from this one.
## HTML
```html
<div class="tbh-15-group w-full min-h-svh flex flex-wrap">
<section class="tbh-15a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh15-sans bg-tbh15a-stage" aria-label="Liquid wave fill button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded-xl border-2 border-tbh15a-liquid px-11 py-[18px] text-base font-extrabold text-tbh15a-liquid bg-transparent transition-colors duration-[350ms] delay-150 hover:text-white focus-visible:text-white focus-visible:outline-3 focus-visible:outline-tbh15a-liquid focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute -left-1/2 top-full w-[200%] h-full z-[1] bg-tbh15a-liquid translate-y-[22px] transition-[translate] duration-[550ms] ease-[cubic-bezier(.4,0,.2,1)] before:content-[''] before:absolute before:left-0 before:bottom-full before:w-full before:h-[22px] before:bg-[radial-gradient(circle_at_25%_0,transparent_12px,var(--color-tbh15a-liquid)_13px)] before:bg-[length:44px_22px] before:bg-repeat-x group-hover/btn:-translate-y-full group-hover/btn:animate-tbh15a-sway group-focus-visible/btn:-translate-y-full group-focus-visible/btn:animate-tbh15a-sway motion-reduce:transition-none motion-reduce:group-hover/btn:animate-none motion-reduce:group-focus-visible/btn:animate-none"></span>
    <span class="relative z-[2]">Download</span>
  </button>
</section>
<section class="tbh-15b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh15-sans bg-tbh15b-stage" aria-label="Tilted flood button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded-full border-2 border-tbh15b-liquid px-[46px] py-[18px] text-base font-extrabold text-tbh15b-liquid bg-transparent transition-colors duration-300 delay-[120ms] hover:text-tbh15b-ink focus-visible:text-tbh15b-ink focus-visible:outline-3 focus-visible:outline-tbh15b-liquid focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute -left-[10%] bottom-0 w-[120%] h-[180%] z-0 origin-top bg-tbh15b-liquid [rotate:6deg] translate-y-[120%] transition-[translate,rotate] duration-500 ease-[cubic-bezier(.5,0,.2,1)] group-hover/btn:[rotate:0deg] group-hover/btn:translate-y-0 group-focus-visible/btn:[rotate:0deg] group-focus-visible/btn:translate-y-0 motion-reduce:duration-[250ms]"></span>
    <span class="relative z-[1]">Install now</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh15a-liquid: #4f86e0;
  --color-tbh15a-liquid: oklch(0.6 0.18 235);
  --color-tbh15a-stage: #0b1020;
  --color-tbh15a-stage: oklch(0.14 0.03 265);
  --color-tbh15b-liquid: #6fd99a;
  --color-tbh15b-liquid: oklch(0.7 0.17 150);
  --color-tbh15b-ink: #04180d;
  --color-tbh15b-ink: oklch(0.2 0.05 150);
  --color-tbh15b-stage: #08160e;
  --color-tbh15b-stage: oklch(0.15 0.02 150);
  --font-tbh15-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh15a-sway: tbh15a-sway 1.6s ease-in-out infinite;
}
/* Stays CSS: the sway keyframe. Ported from the original's margin-left animation to the
   discrete translate property — same motion, no layout work per frame. */

@keyframes tbh15a-sway {
  0%,
    100% {
    translate: 0 -100%;
  }

  50% {
    translate: 22px -100%;
  }
}

.tbh-15-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-15a,
.tbh-15b {
  min-height: 100svh;
}
```
