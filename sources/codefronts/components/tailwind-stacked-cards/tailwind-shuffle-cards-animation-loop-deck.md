---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-shuffle-cards-animation-loop-deck/"
title: "Tailwind Shuffle Cards Animation Loop Deck"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A deck riffling itself, offset per card by a negative animation-delay so the loop never syncs."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shuffle Cards Animation Loop Deck
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-shuffle-cards-animation-loop-deck/

A deck riffling itself, offset per card by a negative animation-delay so the loop never syncs. Hover and it stops dead and fans out to be read &mdash; group-hover:[animation-play-state:paused] plus a static fan transform. The reduced-motion path is the interesting one: it does not slow the loop down, it removes it and ships the fanned deck as the resting state.
## HTML
```html
<section class="stk-17 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk17-sans bg-stk17-bg" aria-label="Shuffling card deck">
  <div class="has-focus-visible:outline-3 has-focus-visible:outline-stk17-ring has-focus-visible:outline-offset-[12px] has-focus-visible:rounded-[22px]">
    <div class="group relative w-37.5 h-50 outline-none" tabindex="0" role="img" aria-label="A deck of four suit cards, riffling. Hover or focus to pause and fan them out.">
      <div class="absolute inset-0 grid place-items-center rounded-2xl bg-stk17-c1 text-[52px] text-white shadow-[0_16px_32px_-16px_rgba(0,0,0,0.8)] animate-stk17-riffle [animation-delay:calc(var(--i)*-0.4s)] group-hover:[animation-play-state:paused] group-hover:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] group-focus-visible:[animation-play-state:paused] group-focus-visible:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] motion-reduce:animate-none motion-reduce:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))]" style="--i:0" aria-hidden="true">&diams;</div>
      <div class="absolute inset-0 grid place-items-center rounded-2xl bg-stk17-c2 text-[52px] text-white shadow-[0_16px_32px_-16px_rgba(0,0,0,0.8)] animate-stk17-riffle [animation-delay:calc(var(--i)*-0.4s)] group-hover:[animation-play-state:paused] group-hover:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] group-focus-visible:[animation-play-state:paused] group-focus-visible:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] motion-reduce:animate-none motion-reduce:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))]" style="--i:1" aria-hidden="true">&clubs;</div>
      <div class="absolute inset-0 grid place-items-center rounded-2xl bg-stk17-c3 text-[52px] text-white shadow-[0_16px_32px_-16px_rgba(0,0,0,0.8)] animate-stk17-riffle [animation-delay:calc(var(--i)*-0.4s)] group-hover:[animation-play-state:paused] group-hover:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] group-focus-visible:[animation-play-state:paused] group-focus-visible:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] motion-reduce:animate-none motion-reduce:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))]" style="--i:2" aria-hidden="true">&hearts;</div>
      <div class="absolute inset-0 grid place-items-center rounded-2xl bg-stk17-c4 text-[52px] text-white shadow-[0_16px_32px_-16px_rgba(0,0,0,0.8)] animate-stk17-riffle [animation-delay:calc(var(--i)*-0.4s)] group-hover:[animation-play-state:paused] group-hover:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] group-focus-visible:[animation-play-state:paused] group-focus-visible:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))] motion-reduce:animate-none motion-reduce:[transform:translateX(calc((var(--i)-1.5)*54px))_rotate(calc((var(--i)-1.5)*6deg))]" style="--i:3" aria-hidden="true">&spades;</div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk17-bg: #131620;
  --color-stk17-bg: oklch(0.21 0.018 275);
  --color-stk17-ring: #45ab7c;
  --color-stk17-ring: oklch(0.66 0.15 150);
  --color-stk17-c1: #cf5f4b;
  --color-stk17-c1: oklch(0.62 0.16 20);
  --color-stk17-c2: #45ab7c;
  --color-stk17-c2: oklch(0.64 0.15 150);
  --color-stk17-c3: #4d8ade;
  --color-stk17-c3: oklch(0.62 0.16 250);
  --color-stk17-c4: #9b6ed6;
  --color-stk17-c4: oklch(0.62 0.16 300);
  --font-stk17-sans: 'Archivo', system-ui, sans-serif;
  --animate-stk17-riffle: stk-17-riffle 1.6s ease-in-out infinite;
}
/* The riffle path itself. z-index is not interpolated inside keyframes — it
   steps at each stop, which is exactly what a shuffle wants. */

@keyframes stk-17-riffle {
  0%,
    100% {
    transform: translateX(0) rotate(0);
    z-index: 2;
  }

  25% {
    transform: translateX(70px) rotate(10deg);
    z-index: 5;
  }

  50% {
    transform: translateX(0) rotate(0);
    z-index: 2;
  }

  75% {
    transform: translateX(-70px) rotate(-10deg);
    z-index: 1;
  }
}
```
