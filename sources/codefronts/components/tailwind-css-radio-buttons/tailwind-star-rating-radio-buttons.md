---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-star-rating-radio-buttons/"
title: "Tailwind Star Rating Radio Buttons"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A five-star rating built the right way: five radios in logical 1→5 order, cumulative fill, a hover preview and a staggered pop when the rating lands — plus a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Star Rating Radio Buttons
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-star-rating-radio-buttons/

A five-star rating built the right way: five radios in logical 1→5 order, cumulative fill, a hover preview and a staggered pop when the rating lands — plus a live caption ("Great") for the score. The cumulative logic is one arbitrary variant, group-has-[~label_input:checked]/star:: every star before the checked one lights up.
## HTML
```html
<section class="trb-11 w-full min-h-svh grid place-items-center bg-trb11-bg px-6 py-14 font-trb11-sans text-trb11-ink" aria-label="Star rating radio group demo">
  <fieldset class="group/rate grid justify-items-center gap-4 rounded-3xl bg-white px-8 py-7 shadow-trb11-card ring-1 ring-trb11-line">
    <legend class="sr-only">Rate your experience</legend>
    <p aria-hidden="true" class="text-center text-[22px] font-extrabold tracking-[-0.02em]">Rate your experience</p>
    <div class="group/stars flex gap-1">
      <label class="group/star relative grid size-[52px] cursor-pointer place-items-center rounded-xl has-focus-visible:outline-3 has-focus-visible:outline-trb11-star"><input type="radio" name="trb-11" value="1" class="sr-only"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[38px] fill-transparent stroke-trb11-off stroke-[1.6] transition-[fill,stroke,scale] duration-250 [--d:0ms] group-has-checked/star:animate-trb11-pop group-has-checked/star:fill-trb11-star group-has-checked/star:stroke-trb11-star group-has-[~label_input:checked]/star:animate-trb11-pop group-has-[~label_input:checked]/star:fill-trb11-star group-has-[~label_input:checked]/star:stroke-trb11-star group-hover/stars:fill-transparent! group-hover/stars:stroke-trb11-off! [label:hover_&]:scale-110 [label:hover_&]:fill-trb11-star/55! [label:hover_&]:stroke-trb11-star! [label:has(~label:hover)_&]:fill-trb11-star/55! [label:has(~label:hover)_&]:stroke-trb11-star! motion-reduce:animate-none! motion-reduce:scale-100!"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="sr-only">1 of 5 stars</span></label>
      <label class="group/star relative grid size-[52px] cursor-pointer place-items-center rounded-xl has-focus-visible:outline-3 has-focus-visible:outline-trb11-star"><input type="radio" name="trb-11" value="2" class="sr-only"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[38px] fill-transparent stroke-trb11-off stroke-[1.6] transition-[fill,stroke,scale] duration-250 [--d:60ms] group-has-checked/star:animate-trb11-pop group-has-checked/star:fill-trb11-star group-has-checked/star:stroke-trb11-star group-has-[~label_input:checked]/star:animate-trb11-pop group-has-[~label_input:checked]/star:fill-trb11-star group-has-[~label_input:checked]/star:stroke-trb11-star group-hover/stars:fill-transparent! group-hover/stars:stroke-trb11-off! [label:hover_&]:scale-110 [label:hover_&]:fill-trb11-star/55! [label:hover_&]:stroke-trb11-star! [label:has(~label:hover)_&]:fill-trb11-star/55! [label:has(~label:hover)_&]:stroke-trb11-star! motion-reduce:animate-none! motion-reduce:scale-100!"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="sr-only">2 of 5 stars</span></label>
      <label class="group/star relative grid size-[52px] cursor-pointer place-items-center rounded-xl has-focus-visible:outline-3 has-focus-visible:outline-trb11-star"><input type="radio" name="trb-11" value="3" class="sr-only"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[38px] fill-transparent stroke-trb11-off stroke-[1.6] transition-[fill,stroke,scale] duration-250 [--d:120ms] group-has-checked/star:animate-trb11-pop group-has-checked/star:fill-trb11-star group-has-checked/star:stroke-trb11-star group-has-[~label_input:checked]/star:animate-trb11-pop group-has-[~label_input:checked]/star:fill-trb11-star group-has-[~label_input:checked]/star:stroke-trb11-star group-hover/stars:fill-transparent! group-hover/stars:stroke-trb11-off! [label:hover_&]:scale-110 [label:hover_&]:fill-trb11-star/55! [label:hover_&]:stroke-trb11-star! [label:has(~label:hover)_&]:fill-trb11-star/55! [label:has(~label:hover)_&]:stroke-trb11-star! motion-reduce:animate-none! motion-reduce:scale-100!"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="sr-only">3 of 5 stars</span></label>
      <label class="group/star relative grid size-[52px] cursor-pointer place-items-center rounded-xl has-focus-visible:outline-3 has-focus-visible:outline-trb11-star"><input type="radio" name="trb-11" value="4" class="sr-only" checked><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[38px] fill-transparent stroke-trb11-off stroke-[1.6] transition-[fill,stroke,scale] duration-250 [--d:180ms] group-has-checked/star:animate-trb11-pop group-has-checked/star:fill-trb11-star group-has-checked/star:stroke-trb11-star group-has-[~label_input:checked]/star:animate-trb11-pop group-has-[~label_input:checked]/star:fill-trb11-star group-has-[~label_input:checked]/star:stroke-trb11-star group-hover/stars:fill-transparent! group-hover/stars:stroke-trb11-off! [label:hover_&]:scale-110 [label:hover_&]:fill-trb11-star/55! [label:hover_&]:stroke-trb11-star! [label:has(~label:hover)_&]:fill-trb11-star/55! [label:has(~label:hover)_&]:stroke-trb11-star! motion-reduce:animate-none! motion-reduce:scale-100!"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="sr-only">4 of 5 stars</span></label>
      <label class="group/star relative grid size-[52px] cursor-pointer place-items-center rounded-xl has-focus-visible:outline-3 has-focus-visible:outline-trb11-star"><input type="radio" name="trb-11" value="5" class="sr-only"><svg viewBox="0 0 24 24" aria-hidden="true" class="size-[38px] fill-transparent stroke-trb11-off stroke-[1.6] transition-[fill,stroke,scale] duration-250 [--d:240ms] group-has-checked/star:animate-trb11-pop group-has-checked/star:fill-trb11-star group-has-checked/star:stroke-trb11-star group-has-[~label_input:checked]/star:animate-trb11-pop group-has-[~label_input:checked]/star:fill-trb11-star group-has-[~label_input:checked]/star:stroke-trb11-star group-hover/stars:fill-transparent! group-hover/stars:stroke-trb11-off! [label:hover_&]:scale-110 [label:hover_&]:fill-trb11-star/55! [label:hover_&]:stroke-trb11-star! [label:has(~label:hover)_&]:fill-trb11-star/55! [label:has(~label:hover)_&]:stroke-trb11-star! motion-reduce:animate-none! motion-reduce:scale-100!"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z"/></svg><span class="sr-only">5 of 5 stars</span></label>
    </div>
    <p aria-hidden="true" class="min-h-7 text-center text-lg font-bold text-trb11-ink">
      <span class="hidden group-has-[[value='1']:checked]/rate:inline">Poor</span><span class="hidden group-has-[[value='2']:checked]/rate:inline">Fair</span><span class="hidden group-has-[[value='3']:checked]/rate:inline">Good</span><span class="hidden group-has-[[value='4']:checked]/rate:inline">Great</span><span class="hidden group-has-[[value='5']:checked]/rate:inline">Loved it</span>
    </p>
    <p class="text-[13px] text-trb11-mut">Hover to preview · click or use arrow keys to rate</p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb11-bg: #fdf9f0;
  --color-trb11-bg: oklch(0.982 0.012 85);
  --color-trb11-ink: #292317;
  --color-trb11-ink: oklch(0.26 0.02 80);
  --color-trb11-mut: #6f6446;
  --color-trb11-mut: oklch(0.5 0.04 85);
  --color-trb11-line: #efe6d0;
  --color-trb11-line: oklch(0.925 0.025 85);
  --color-trb11-off: #b8ab88;
  --color-trb11-off: oklch(0.74 0.045 88);
  --color-trb11-star: #f2b320;
  --color-trb11-star: oklch(0.8 0.16 80);
  --shadow-trb11-card: 0 18px 44px -24px oklch(0.4 0.06 80 / 0.35);
  --font-trb11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* inline: the pop token reads each star's own --d delay. */

@theme inline {
  --animate-trb11-pop: trb11-pop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) var(--d, 0ms) backwards;
}

@keyframes trb11-pop {
  0% {
    scale: 0.6;
  }

  60% {
    scale: 1.25;
  }

  100% {
    scale: 1;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-11 {
  width: 100%;
  min-height: 100svh;
}
```
