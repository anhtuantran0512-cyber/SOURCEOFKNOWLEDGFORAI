---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-spiral-tower-rotating-stacked-cards/"
title: "Tailwind Spiral Tower Rotating Stacked Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Five cards on a rotating helix, pausing on hover or focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Spiral Tower Rotating Stacked Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-spiral-tower-rotating-stacked-cards/

Five cards on a rotating helix, pausing on hover or focus. Every card's place on the spiral is one expression over its index &mdash; rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px)) &mdash; so changing the card count is changing one number. The honest part of this entry is what it says about itself: a spinning tower cannot carry primary content, and the demo is marked accordingly.
## HTML
```html
<section class="stk-36 grid w-full min-h-svh place-items-center px-5 py-15 font-stk36-sans bg-stk36-bg [background-image:radial-gradient(circle_at_50%_50%,var(--color-stk36-glow),transparent_70%)]" aria-label="Featured collection">
  <div class="group h-100 w-60 [perspective:1200px]" tabindex="0" role="img" aria-label="Five featured cards rotating on a spiral tower. Hover or focus to pause.">
    <div class="relative size-full [transform-style:preserve-3d] animate-stk36-spin group-hover:[animation-play-state:paused] group-focus-within:[animation-play-state:paused] motion-reduce:animate-none" aria-hidden="true">
      <div class="absolute left-1/2 top-1/2 -ml-15 -mt-20 grid h-40 w-30 place-items-center rounded-2xl font-stk36-display text-[1.4rem] text-white bg-linear-[150deg,var(--color-stk36-a1),var(--color-stk36-a2)] shadow-[0_0_30px_var(--color-stk36-halo)] [transform:rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px))]" style="--i:0">01</div>
      <div class="absolute left-1/2 top-1/2 -ml-15 -mt-20 grid h-40 w-30 place-items-center rounded-2xl font-stk36-display text-[1.4rem] text-white bg-linear-[150deg,var(--color-stk36-b1),var(--color-stk36-b2)] shadow-[0_0_30px_var(--color-stk36-halo)] [transform:rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px))]" style="--i:1">02</div>
      <div class="absolute left-1/2 top-1/2 -ml-15 -mt-20 grid h-40 w-30 place-items-center rounded-2xl font-stk36-display text-[1.4rem] text-white bg-linear-[150deg,var(--color-stk36-c1),var(--color-stk36-c2)] shadow-[0_0_30px_var(--color-stk36-halo)] [transform:rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px))]" style="--i:2">03</div>
      <div class="absolute left-1/2 top-1/2 -ml-15 -mt-20 grid h-40 w-30 place-items-center rounded-2xl font-stk36-display text-[1.4rem] text-white bg-linear-[150deg,var(--color-stk36-d1),var(--color-stk36-d2)] shadow-[0_0_30px_var(--color-stk36-halo)] [transform:rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px))]" style="--i:3">04</div>
      <div class="absolute left-1/2 top-1/2 -ml-15 -mt-20 grid h-40 w-30 place-items-center rounded-2xl font-stk36-display text-[1.4rem] text-stk36-dark bg-linear-[150deg,var(--color-stk36-e1),var(--color-stk36-e2)] shadow-[0_0_30px_var(--color-stk36-halo)] [transform:rotateY(calc(var(--i)*72deg))_translateZ(150px)_translateY(calc((var(--i)-2)*60px))]" style="--i:4">05</div>
    </div>
    <ol class="sr-only">
      <li>01 &mdash; Featured collection card one</li>
      <li>02 &mdash; Featured collection card two</li>
      <li>03 &mdash; Featured collection card three</li>
      <li>04 &mdash; Featured collection card four</li>
      <li>05 &mdash; Featured collection card five</li>
    </ol>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk36-bg: #080410;
  --color-stk36-bg: oklch(0.09 0.020 300);
  --color-stk36-glow: #1e0a2e;
  --color-stk36-glow: oklch(0.20 0.055 300);
  --color-stk36-dark: #4a1a2a;
  --color-stk36-dark: oklch(0.32 0.070 10);
  --color-stk36-halo: rgba(180, 100, 255, 0.25);
  --color-stk36-a1: #ee0979;
  --color-stk36-a2: #ff6a00;
  --color-stk36-b1: #7f00ff;
  --color-stk36-b2: #e100ff;
  --color-stk36-c1: #00c6ff;
  --color-stk36-c2: #0072ff;
  --color-stk36-d1: #11998e;
  --color-stk36-d2: #38ef7d;
  --color-stk36-e1: #f7971e;
  --color-stk36-e2: #ffd200;
  --font-stk36-sans: 'Jost', system-ui, sans-serif;
  --font-stk36-display: 'Major Mono Display', ui-monospace, monospace;
  --animate-stk36-spin: stk-36-spin 14s linear infinite;
}

@keyframes stk-36-spin {
  to {
    transform: rotateY(360deg);
  }
}
```
