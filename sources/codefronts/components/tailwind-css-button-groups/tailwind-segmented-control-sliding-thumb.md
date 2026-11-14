---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-segmented-control-sliding-thumb/"
title: "Tailwind Segmented Control with Sliding Thumb (iOS Style)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "The most-searched button-group pattern: an iOS-style segmented control whose thumb springs between options."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Segmented Control with Sliding Thumb (iOS Style)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-segmented-control-sliding-thumb/

The most-searched button-group pattern: an iOS-style segmented control whose thumb springs between options. Radios carry state and keyboard support; the thumb slides with group-has-[#tbg05-3:checked]/seg:translate-x-[200%] on a spring curve written with v4's ease-[linear(…)]. Each segment shows a sub-value, and the whole control is pure Tailwind.
## HTML
```html
<section class="tbg-05 w-full min-h-svh grid place-items-center bg-tbg05-bg bg-linear-135 from-tbg05-bg via-tbg05-bg2 to-tbg05-bg3 px-5 py-14 font-tbg05-sans text-tbg05-ink" aria-label="iOS style segmented control demo">
  <div class="grid w-full max-w-[32rem] gap-3">
    <p id="tbg05-label" class="ml-1 text-xs font-bold uppercase tracking-[0.14em] text-tbg05-acc">Timeframe</p>
    <div role="radiogroup" aria-labelledby="tbg05-label" class="group/seg relative grid grid-cols-4 rounded-2xl border border-tbg05-line bg-white p-1.5 shadow-tbg05-lift">
      <label class="relative z-1 grid min-h-14 cursor-pointer place-content-center justify-items-center rounded-xl text-[15px] font-semibold text-tbg05-mut transition-colors duration-250 hover:text-tbg05-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg05-acc"><input type="radio" name="tbg05" id="tbg05-1" class="sr-only" checked>Day<span class="text-[11px] font-medium opacity-75">+2.4%</span></label>
      <label class="relative z-1 grid min-h-14 cursor-pointer place-content-center justify-items-center rounded-xl text-[15px] font-semibold text-tbg05-mut transition-colors duration-250 hover:text-tbg05-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg05-acc"><input type="radio" name="tbg05" id="tbg05-2" class="sr-only">Week<span class="text-[11px] font-medium opacity-75">+6.1%</span></label>
      <label class="relative z-1 grid min-h-14 cursor-pointer place-content-center justify-items-center rounded-xl text-[15px] font-semibold text-tbg05-mut transition-colors duration-250 hover:text-tbg05-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg05-acc"><input type="radio" name="tbg05" id="tbg05-3" class="sr-only">Month<span class="text-[11px] font-medium opacity-75">−1.8%</span></label>
      <label class="relative z-1 grid min-h-14 cursor-pointer place-content-center justify-items-center rounded-xl text-[15px] font-semibold text-tbg05-mut transition-colors duration-250 hover:text-tbg05-ink has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-tbg05-acc"><input type="radio" name="tbg05" id="tbg05-4" class="sr-only">Year<span class="text-[11px] font-medium opacity-75">+31%</span></label>
      <span aria-hidden="true" class="pointer-events-none absolute top-1.5 bottom-1.5 left-1.5 z-0 w-[calc((100%-0.75rem)/4)] rounded-xl bg-tbg05-acc shadow-[0_6px_16px_-6px_var(--color-tbg05-acc)] transition-transform duration-500 ease-tbg05-spring group-has-[#tbg05-2:checked]/seg:translate-x-full group-has-[#tbg05-3:checked]/seg:translate-x-[200%] group-has-[#tbg05-4:checked]/seg:translate-x-[300%] motion-reduce:transition-none"></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg05-bg: #f5f2ff;
  --color-tbg05-bg2: #efeaff;
  --color-tbg05-bg3: #e7dfff;
  --color-tbg05-line: #e6def9;
  --color-tbg05-ink: #24173f;
  --color-tbg05-mut: #5b4b86;
  --color-tbg05-mut: oklch(0.45 0.09 290);
  --color-tbg05-acc: #6a3fe0;
  --color-tbg05-acc: oklch(0.52 0.22 288);
  --shadow-tbg05-lift: 0 18px 44px -30px rgb(60 20 120 / 0.6);
  --ease-tbg05-spring: linear(0, 0.18 7%, 0.6 18%, 0.96 30%, 1.08 40%, 1.06 48%, 1 60%, 0.99 75%, 1);
  --font-tbg05-sans: 'Onest', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-05 {
  width: 100%;
  min-height: 100svh;
}
```
