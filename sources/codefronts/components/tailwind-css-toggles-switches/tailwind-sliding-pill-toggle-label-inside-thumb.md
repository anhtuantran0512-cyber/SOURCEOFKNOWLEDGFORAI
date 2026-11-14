---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-sliding-pill-toggle-label-inside-thumb/"
title: "Tailwind Sliding Pill Toggle with Label Inside the Thumb"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The label rides in the thumb: a wide pill whose sliding handle says \"Draft\" or \"Live\", crossfading its word mid-journey while ghost labels in the track show…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sliding Pill Toggle with Label Inside the Thumb
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-sliding-pill-toggle-label-inside-thumb/

The label rides in the thumb: a wide pill whose sliding handle says "Draft" or "Live", crossfading its word mid-journey while ghost labels in the track show where a click will take you. Built for publish switches, where the state word must move with the control.
## HTML
```html
<section class="ttg-20 w-full min-h-svh flex flex-col items-center justify-center gap-6 px-5 py-14 bg-ttg20-bg font-ttg20-sans" aria-label="Sliding pill with travelling label">
  <div class="flex items-center gap-7 px-6 py-5 rounded-2xl bg-white border border-ttg20-edge shadow-[0_14px_32px_-26px_oklch(0.4_0.03_95/0.5)]">
    <span class="flex flex-col gap-0.5">
      <span id="ttg-20-l" class="text-[15px] font-semibold text-ttg20-ink">Article status</span>
      <span class="text-[12.5px] text-ttg20-mute">Live posts appear in the feed immediately</span>
    </span>
    <input type="checkbox" id="ttg-20-sw" role="switch" aria-labelledby="ttg-20-l" class="peer sr-only">
    <label for="ttg-20-sw" aria-hidden="true" class="relative shrink-0 w-41 h-11 rounded-3xl bg-ttg20-track cursor-pointer shadow-[inset_0_2px_5px_oklch(0.5_0.02_95/0.18)] peer-focus-visible:outline-3 peer-focus-visible:outline-ttg20-focus peer-focus-visible:outline-offset-3 peer-checked:[&_.ttg20-ghost-r]:opacity-0 peer-checked:[&_.ttg20-ghost-l]:opacity-100 peer-checked:[&_.ttg20-thumb]:translate-x-[78px] peer-checked:[&_.ttg20-thumb]:bg-ttg20-live peer-checked:[&_.ttg20-draft]:opacity-0 peer-checked:[&_.ttg20-live]:opacity-100">
      <span class="ttg20-ghost-l absolute inset-y-0 left-0 w-1/2 flex items-center justify-center text-[13px] font-bold text-ttg20-ghost opacity-0 transition-opacity duration-[350ms] motion-reduce:transition-none">Draft</span>
      <span class="ttg20-ghost-r absolute inset-y-0 right-0 w-1/2 flex items-center justify-center text-[13px] font-bold text-ttg20-ghost transition-opacity duration-[350ms] motion-reduce:transition-none">Live</span>
      <span class="ttg20-thumb absolute top-1 left-1 block w-[78px] h-9 rounded-[20px] bg-ttg20-draft shadow-[0_3px_8px_oklch(0.3_0.02_265/0.35)] transition-[transform,background-color] duration-[350ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:transition-none">
        <i class="ttg20-draft absolute inset-0 flex items-center justify-center not-italic text-[13.5px] font-extrabold tracking-[0.04em] text-white transition-opacity duration-[350ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:transition-none">Draft</i>
        <i class="ttg20-live absolute inset-0 flex items-center justify-center not-italic text-[13.5px] font-extrabold tracking-[0.04em] text-white opacity-0 transition-opacity duration-[350ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] motion-reduce:transition-none">Live</i>
      </span>
    </label>
  </div>
  <p class="text-[12px] tracking-[0.12em] uppercase text-ttg20-mute">The word travels with the thumb</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg20-bg: #f6f6f2;
  --color-ttg20-bg: oklch(0.97 0.006 95);
  --color-ttg20-edge: #e7e6dd;
  --color-ttg20-edge: oklch(0.93 0.008 95);
  --color-ttg20-track: #eae9e0;
  --color-ttg20-track: oklch(0.93 0.01 95);
  --color-ttg20-ghost: #97958a;
  --color-ttg20-ghost: oklch(0.66 0.012 95);
  --color-ttg20-draft: #545b69;
  --color-ttg20-draft: oklch(0.47 0.02 265);
  --color-ttg20-live: #2f9e63;
  --color-ttg20-live: oklch(0.6 0.15 155);
  --color-ttg20-ink: #383b33;
  --color-ttg20-ink: oklch(0.35 0.012 110);
  --color-ttg20-mute: #8a887c;
  --color-ttg20-mute: oklch(0.62 0.012 95);
  --color-ttg20-focus: #3f63e0;
  --color-ttg20-focus: oklch(0.55 0.19 265);
  --font-ttg20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-20 {
  width: 100%;
  min-height: 100svh;
}
```
