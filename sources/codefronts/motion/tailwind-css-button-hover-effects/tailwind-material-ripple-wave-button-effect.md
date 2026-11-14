---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-material-ripple-wave-button-effect/"
title: "Tailwind Material Ripple Wave Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A Material-style ripple: on hover a circular wave expands from the centre and fades as it grows, like a drop hitting water."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Ripple Wave Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-material-ripple-wave-button-effect/

A Material-style ripple: on hover a circular wave expands from the centre and fades as it grows, like a drop hitting water. No pointer tracking, so unlike entry 01 this one needs no JavaScript at all &mdash; and design B turns the same two properties into a repeating sonar echo.
## HTML
```html
<div class="tbh-28-group w-full min-h-svh flex flex-wrap">
<section class="tbh-28a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh28-sans bg-tbh28a-stage" aria-label="Ripple wave button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer border-0 rounded-full px-11 py-[17px] text-base font-extrabold text-white bg-tbh28a-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[3px] before:content-[''] before:absolute before:left-1/2 before:top-1/2 before:-ml-[60px] before:-mt-[60px] before:w-[120px] before:h-[120px] before:z-0 before:rounded-full before:bg-white/40 before:scale-0 before:opacity-100 before:transition-[scale,opacity] before:duration-600 before:ease-out hover:before:scale-[4] hover:before:opacity-0 focus-visible:before:scale-[4] focus-visible:before:opacity-0 motion-reduce:before:transition-opacity motion-reduce:hover:before:scale-0 motion-reduce:hover:before:opacity-30">
    <span class="relative z-[1]">Continue</span>
  </button>
</section>
<section class="tbh-28b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh28-sans bg-tbh28b-stage" aria-label="Echo ripple button">
  <button type="button" class="relative cursor-pointer border-0 rounded-full px-11 py-[17px] text-base font-extrabold text-white bg-tbh28b-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:rounded-full before:border-2 before:border-tbh28b-acc before:opacity-0 before:pointer-events-none after:content-[''] after:absolute after:inset-0 after:rounded-full after:border-2 after:border-tbh28b-acc after:opacity-0 after:pointer-events-none hover:before:animate-tbh28b-echo hover:after:animate-tbh28b-echo hover:after:[animation-delay:.7s] focus-visible:before:animate-tbh28b-echo focus-visible:after:animate-tbh28b-echo focus-visible:after:[animation-delay:.7s] motion-reduce:hover:before:animate-none motion-reduce:hover:after:animate-none">
    <span class="relative z-[1]">Ping</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh28a-acc: #3d93a8;
  --color-tbh28a-acc: oklch(0.58 0.16 200);
  --color-tbh28a-stage: #081418;
  --color-tbh28a-stage: oklch(0.14 0.02 200);
  --color-tbh28b-acc: #5c7ce0;
  --color-tbh28b-acc: oklch(0.6 0.17 260);
  --color-tbh28b-stage: #0a0c1a;
  --color-tbh28b-stage: oklch(0.13 0.02 265);
  --font-tbh28-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh28b-echo: tbh28b-echo 1.4s ease-out infinite;
}
/* Stays CSS: the echo keyframe. Design A needs none — a transition does the ripple, and it
   resets on pointer-out for free. */

@keyframes tbh28b-echo {
  0% {
    opacity: 0.7;
    scale: 1;
  }

  100% {
    opacity: 0;
    scale: 1.5;
  }
}

.tbh-28-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-28a,
.tbh-28b {
  min-height: 100svh;
}
```
