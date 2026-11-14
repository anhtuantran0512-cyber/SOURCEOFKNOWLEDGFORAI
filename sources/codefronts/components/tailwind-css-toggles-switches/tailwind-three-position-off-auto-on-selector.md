---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-three-position-off-auto-on-selector/"
title: "Tailwind Three-Position Off / Auto / On Selector"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Not every setting is binary: a three-detent selector for Off / Auto / On, where the thumb travels to thirds and the card below explains what the chosen mode…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Three-Position Off / Auto / On Selector
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-three-position-off-auto-on-selector/

Not every setting is binary: a three-detent selector for Off / Auto / On, where the thumb travels to thirds and the card below explains what the chosen mode actually does. Named peers make three positions no harder than two.
## HTML
```html
<section class="ttg-41 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg41-bg font-ttg41-sans" aria-label="Three position selector">
  <div class="w-[min(360px,100%)] flex flex-col gap-5 p-7 rounded-[24px] bg-white border border-ttg41-edge shadow-[0_24px_50px_-36px_oklch(0.4_0.04_265/0.6)]">
    <span class="flex flex-col gap-0.5">
      <b class="text-[16px] font-bold text-ttg41-ink">Cooling</b>
      <span class="text-[12.5px] text-ttg41-mute">Server room &middot; rack B</span>
    </span>
    <div role="radiogroup" aria-label="Cooling mode" class="relative grid grid-cols-3 p-1 rounded-2xl bg-ttg41-track">
      <input type="radio" name="ttg-41" id="ttg-41-off" class="peer/off sr-only">
      <input type="radio" name="ttg-41" id="ttg-41-auto" checked class="peer/auto sr-only">
      <input type="radio" name="ttg-41" id="ttg-41-on" class="peer/on sr-only">
      <span aria-hidden="true" class="absolute top-1 left-1 z-0 w-[calc(33.333%-2.67px)] h-[calc(100%-8px)] rounded-xl bg-white shadow-[0_2px_8px_-2px_oklch(0.4_0.03_265/0.45)] transition-transform duration-[320ms] ease-[cubic-bezier(0.3,1,0.35,1.05)] peer-checked/auto:translate-x-full peer-checked/on:translate-x-[200%] motion-reduce:duration-75"></span>
      <label for="ttg-41-off" class="relative z-10 flex items-center justify-center min-h-11 rounded-xl cursor-pointer text-[13.5px] font-bold text-ttg41-mute transition-colors duration-200 peer-checked/off:text-ttg41-ink peer-focus-visible/off:outline-3 peer-focus-visible/off:outline-ttg41-focus peer-focus-visible/off:outline-offset-2">Off</label>
      <label for="ttg-41-auto" class="relative z-10 flex items-center justify-center min-h-11 rounded-xl cursor-pointer text-[13.5px] font-bold text-ttg41-mute transition-colors duration-200 peer-checked/auto:text-ttg41-auto peer-focus-visible/auto:outline-3 peer-focus-visible/auto:outline-ttg41-focus peer-focus-visible/auto:outline-offset-2">Auto</label>
      <label for="ttg-41-on" class="relative z-10 flex items-center justify-center min-h-11 rounded-xl cursor-pointer text-[13.5px] font-bold text-ttg41-mute transition-colors duration-200 peer-checked/on:text-ttg41-on peer-focus-visible/on:outline-3 peer-focus-visible/on:outline-ttg41-focus peer-focus-visible/on:outline-offset-2">On</label>
      <span aria-hidden="true" class="ttg41-exp absolute -bottom-13 left-0 right-0 h-10 peer-checked/off:[&_.ttg41-o]:opacity-100 peer-checked/auto:[&_.ttg41-a]:opacity-100 peer-checked/on:[&_.ttg41-n]:opacity-100">
        <i class="ttg41-o absolute inset-0 not-italic flex items-center text-[12.5px] leading-snug text-ttg41-mute opacity-0 transition-opacity duration-200">Fans stay off. Rack may exceed 30&deg;C under load.</i>
        <i class="ttg41-a absolute inset-0 not-italic flex items-center text-[12.5px] leading-snug text-ttg41-mute opacity-0 transition-opacity duration-200">Fans spin up above 24&deg;C and stop when the rack settles.</i>
        <i class="ttg41-n absolute inset-0 not-italic flex items-center text-[12.5px] leading-snug text-ttg41-mute opacity-0 transition-opacity duration-200">Fans run continuously at 60%. Louder, coldest, more power.</i>
      </span>
    </div>
    <span class="h-10"></span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg41-bg: #eef0f5;
  --color-ttg41-bg: oklch(0.95 0.006 265);
  --color-ttg41-edge: #e6e8f0;
  --color-ttg41-edge: oklch(0.93 0.006 265);
  --color-ttg41-track: #eceef4;
  --color-ttg41-track: oklch(0.94 0.006 265);
  --color-ttg41-ink: #1f2532;
  --color-ttg41-ink: oklch(0.26 0.015 265);
  --color-ttg41-mute: #767e90;
  --color-ttg41-mute: oklch(0.58 0.018 265);
  --color-ttg41-auto: #2a6fd6;
  --color-ttg41-auto: oklch(0.54 0.17 255);
  --color-ttg41-on: #2f9e63;
  --color-ttg41-on: oklch(0.6 0.15 155);
  --color-ttg41-focus: #3f63e0;
  --color-ttg41-focus: oklch(0.55 0.19 265);
  --font-ttg41-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-41 {
  width: 100%;
  min-height: 100svh;
}
```
