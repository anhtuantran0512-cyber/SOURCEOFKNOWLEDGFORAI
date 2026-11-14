---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/tailwind-bottom-navigation-bar-expanding-labels/"
title: "Tailwind Bottom Navigation Bar with Expanding Labels"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A mobile nav bar in a soft white pill."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bottom Navigation Bar with Expanding Labels
Source: https://codefronts.com/navigation/tailwind-css-tabs/tailwind-bottom-navigation-bar-expanding-labels/

A mobile nav bar in a soft white pill. The chosen item grows (flex-1 → flex-[2.6]), a pink halo blooms behind its icon and the label slides out beside it. The port fixes the original's unreadable mint label (1.9:1 on white) with a deep-teal label token while the icon keeps the bright mint.
## HTML
```html
<section class="ttb-16 grid min-h-svh w-full place-items-center bg-ttb16-bg px-4 py-14 font-ttb16-sans text-ttb16-ink" aria-label="Bottom navigation bar with expanding labels demo">
  <div class="grid w-full max-w-md justify-items-center gap-8">
    <div role="radiogroup" aria-label="App navigation" class="flex w-full gap-1 rounded-full bg-white p-2 shadow-[0_10px_30px_-10px_rgb(0_0_0/0.18)]">
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-full text-ttb16-idle transition-[flex-grow,color] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb16-hover has-checked:flex-[2.6] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb16-label motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb16" id="ttb16-r1" checked><span class="relative grid flex-none place-items-center"><span aria-hidden="true" class="absolute -top-1 -left-1 size-6 scale-0 rounded-full bg-ttb16-halo transition-transform duration-450 group-has-checked/tab:scale-100"></span><svg aria-hidden="true" class="relative size-6 transition-colors group-has-checked/tab:text-ttb16-mint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8M5 9.5V20h5v-6h4v6h5V9.5"/></svg></span><span class="max-w-0 -translate-x-2 overflow-hidden text-[15px] font-extrabold whitespace-nowrap text-ttb16-label opacity-0 transition-[max-width,opacity,translate] delay-100 duration-450 group-has-checked/tab:max-w-32 group-has-checked/tab:translate-x-0 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Home</span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-full text-ttb16-idle transition-[flex-grow,color] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb16-hover has-checked:flex-[2.6] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb16-label motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb16" id="ttb16-r2"><span class="relative grid flex-none place-items-center"><span aria-hidden="true" class="absolute -top-1 -left-1 size-6 scale-0 rounded-full bg-ttb16-halo transition-transform duration-450 group-has-checked/tab:scale-100"></span><svg aria-hidden="true" class="relative size-6 transition-colors group-has-checked/tab:text-ttb16-mint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 8l7-5 7 5v3H5zM9 11h6v8H9zM3 20h18"/></svg></span><span class="max-w-0 -translate-x-2 overflow-hidden text-[15px] font-extrabold whitespace-nowrap text-ttb16-label opacity-0 transition-[max-width,opacity,translate] delay-100 duration-450 group-has-checked/tab:max-w-32 group-has-checked/tab:translate-x-0 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Strategy</span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-full text-ttb16-idle transition-[flex-grow,color] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb16-hover has-checked:flex-[2.6] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb16-label motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb16" id="ttb16-r3"><span class="relative grid flex-none place-items-center"><span aria-hidden="true" class="absolute -top-1 -left-1 size-6 scale-0 rounded-full bg-ttb16-halo transition-transform duration-450 group-has-checked/tab:scale-100"></span><svg aria-hidden="true" class="relative size-6 transition-colors group-has-checked/tab:text-ttb16-mint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h10v4l-3 5 3 5v4H7v-4l3-5-3-5z"/></svg></span><span class="max-w-0 -translate-x-2 overflow-hidden text-[15px] font-extrabold whitespace-nowrap text-ttb16-label opacity-0 transition-[max-width,opacity,translate] delay-100 duration-450 group-has-checked/tab:max-w-32 group-has-checked/tab:translate-x-0 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Period</span></label>
      <label class="group/tab relative flex min-h-12 flex-1 cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-full text-ttb16-idle transition-[flex-grow,color] duration-450 ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-ttb16-hover has-checked:flex-[2.6] has-focus-visible:outline-2 has-focus-visible:-outline-offset-2 has-focus-visible:outline-ttb16-label motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb16" id="ttb16-r4"><span class="relative grid flex-none place-items-center"><span aria-hidden="true" class="absolute -top-1 -left-1 size-6 scale-0 rounded-full bg-ttb16-halo transition-transform duration-450 group-has-checked/tab:scale-100"></span><svg aria-hidden="true" class="relative size-6 transition-colors group-has-checked/tab:text-ttb16-mint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L4 6v6c0 5 3.5 9.5 8 10 4.5-.5 8-5 8-10V6zM9 12l2 2 4-4"/></svg></span><span class="max-w-0 -translate-x-2 overflow-hidden text-[15px] font-extrabold whitespace-nowrap text-ttb16-label opacity-0 transition-[max-width,opacity,translate] delay-100 duration-450 group-has-checked/tab:max-w-32 group-has-checked/tab:translate-x-0 group-has-checked/tab:opacity-100 motion-reduce:transition-none">Security</span></label>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-ttb16-mono text-[11.5px] text-ttb16-mut">has-checked:flex-[2.6] · halo scale-0 → 100 · label max-w slide</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb16-bg: #eef0f0;
  --color-ttb16-bg: oklch(0.954 0.002 197.1);
  --color-ttb16-ink: #1f2a2a;
  --color-ttb16-ink: oklch(0.275 0.015 196.3);
  --color-ttb16-idle: #8b949a;
  --color-ttb16-idle: oklch(0.661 0.014 236.7);
  --color-ttb16-hover: #6d777c;
  --color-ttb16-hover: oklch(0.563 0.014 229.1);
  --color-ttb16-mint: #2dd4bf;
  --color-ttb16-mint: oklch(0.785 0.133 181.9);
  --color-ttb16-label: #0f766e;
  --color-ttb16-label: oklch(0.511 0.086 186.4);
  --color-ttb16-halo: #fde4ec;
  --color-ttb16-halo: oklch(0.941 0.029 356.3);
  --color-ttb16-mut: #5d686d;
  --color-ttb16-mut: oklch(0.510 0.016 226.8);
  --font-ttb16-sans: 'Nunito', system-ui, sans-serif;
  --font-ttb16-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-16 {
  width: 100%;
  min-height: 100svh;
}
```
