---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-glitch-slice-button-hover-effect/"
title: "Tailwind Glitch Slice Button Hover Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A digital-distortion CTA: on hover the button splits into horizontal bands that jump out of alignment before snapping back &mdash; a sharp data-corruption…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Glitch Slice Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-glitch-slice-button-hover-effect/

A digital-distortion CTA: on hover the button splits into horizontal bands that jump out of alignment before snapping back &mdash; a sharp data-corruption glitch. Two attr(data-text) copies do all the work, and the real label underneath never moves.
## HTML
```html
<div class="tbh-17-group w-full min-h-svh flex flex-wrap">
<section class="tbh-17a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh17-mono bg-tbh17a-stage" aria-label="Glitch slice button">
  <button type="button" data-text="Play now" class="relative cursor-pointer rounded-md border border-tbh17a-cyan px-10 py-4 text-base font-extrabold uppercase tracking-[0.14em] text-tbh17a-ink bg-tbh17a-panel focus-visible:outline-3 focus-visible:outline-tbh17a-cyan focus-visible:outline-offset-4 before:content-[attr(data-text)] before:absolute before:inset-0 before:grid before:place-items-center before:font-[inherit] before:tracking-[0.14em] before:text-tbh17a-cyan before:bg-tbh17a-panel before:pointer-events-none before:[clip-path:inset(0_0_55%_0)] after:content-[attr(data-text)] after:absolute after:inset-0 after:grid after:place-items-center after:font-[inherit] after:tracking-[0.14em] after:text-tbh17a-mag after:bg-tbh17a-panel after:pointer-events-none after:[clip-path:inset(55%_0_0_0)] hover:before:animate-tbh17a-a hover:after:animate-tbh17a-b focus-visible:before:animate-tbh17a-a focus-visible:after:animate-tbh17a-b motion-reduce:hover:before:animate-none motion-reduce:hover:after:animate-none">
    <span class="relative z-[1]">Play now</span>
  </button>
</section>
<section class="tbh-17b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh17-mono bg-tbh17b-stage" aria-label="Skew glitch button">
  <button type="button" data-text="Deploy" class="relative cursor-pointer rounded-md border border-tbh17b-pink px-[42px] py-4 text-base font-extrabold uppercase tracking-[0.16em] text-white bg-tbh17b-panel focus-visible:outline-3 focus-visible:outline-tbh17b-pink focus-visible:outline-offset-4 before:content-[attr(data-text)] before:absolute before:inset-0 before:grid before:place-items-center before:font-[inherit] before:tracking-[0.16em] before:text-tbh17b-blue before:bg-tbh17b-panel before:opacity-0 before:pointer-events-none before:[clip-path:inset(0_0_70%_0)] hover:before:opacity-85 hover:before:animate-tbh17b-tear focus-visible:before:opacity-85 focus-visible:before:animate-tbh17b-tear motion-reduce:hover:before:animate-none motion-reduce:hover:before:opacity-0">
    <span class="relative z-[1]">Deploy</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh17a-stage: #0a0a12;
  --color-tbh17a-stage: oklch(0.13 0.02 285);
  --color-tbh17a-panel: #0f1226;
  --color-tbh17a-panel: oklch(0.18 0.04 275);
  --color-tbh17a-cyan: #22e3ff;
  --color-tbh17a-cyan: oklch(0.85 0.15 210);
  --color-tbh17a-mag: #ff2bd6;
  --color-tbh17a-mag: oklch(0.7 0.28 330);
  --color-tbh17a-ink: #eafcff;
  --color-tbh17a-ink: oklch(0.97 0.02 210);
  --color-tbh17b-stage: #100810;
  --color-tbh17b-stage: oklch(0.14 0.02 330);
  --color-tbh17b-panel: #1a0e1a;
  --color-tbh17b-panel: oklch(0.19 0.03 330);
  --color-tbh17b-pink: #ff4dd2;
  --color-tbh17b-pink: oklch(0.72 0.26 330);
  --color-tbh17b-blue: #4dd2ff;
  --color-tbh17b-blue: oklch(0.82 0.14 215);
  --font-tbh17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbh17a-a: tbh17a-a 0.4s steps(3) infinite;
  --animate-tbh17a-b: tbh17a-b 0.4s steps(3) infinite;
  --animate-tbh17b-tear: tbh17b-tear 0.35s steps(2) infinite;
}
/* Stays CSS: three jitter keyframes, written against the discrete translate property so
   they never collide with a translate-* utility on the same pseudo-element. */

@keyframes tbh17a-a {
  0% {
    translate: 0 0;
  }

  33% {
    translate: -5px 0;
  }

  66% {
    translate: 4px 0;
  }

  100% {
    translate: 0 0;
  }
}

@keyframes tbh17a-b {
  0% {
    translate: 0 0;
  }

  33% {
    translate: 5px 0;
  }

  66% {
    translate: -4px 0;
  }

  100% {
    translate: 0 0;
  }
}

@keyframes tbh17b-tear {
  0% {
    transform: skewX(0);
    translate: 0 0;
    clip-path: inset(0 0 70% 0);
  }

  50% {
    transform: skewX(-14deg);
    translate: -4px 0;
    clip-path: inset(40% 0 20% 0);
  }

  100% {
    transform: skewX(0);
    translate: 0 0;
    clip-path: inset(0 0 70% 0);
  }
}

.tbh-17-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-17a,
.tbh-17b {
  min-height: 100svh;
}
```
