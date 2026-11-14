---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/glassmorphism-checkbox-tailwind-backdrop-blur/"
title: "Glassmorphism Checkbox in Tailwind CSS — backdrop-blur Frosted Glass"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Frosted-glass checkboxes on a panel that actually has something to blur: two soft colour orbs drift behind backdrop-blur-xl backdrop-saturate-150."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Checkbox in Tailwind CSS — backdrop-blur Frosted Glass
Source: https://codefronts.com/components/tailwind-css-checkboxes/glassmorphism-checkbox-tailwind-backdrop-blur/

Frosted-glass checkboxes on a panel that actually has something to blur: two soft colour orbs drift behind backdrop-blur-xl backdrop-saturate-150. Browsers without backdrop-filter get an opaque tinted panel via supports-[backdrop-filter:blur(1px)]:, so the white text never lands on a bright gradient.
## HTML
```html
<section class="tcb-11 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-linear-135 from-tcb11-a via-tcb11-b via-55% to-tcb11-c px-5 py-14 font-tcb11-sans text-white selection:bg-white/60 selection:text-tcb11-deep" aria-label="Glassmorphism checkboxes">
  <span aria-hidden="true" class="absolute left-[calc(50%-11rem)] top-[calc(50%-8rem)] -z-10 size-48 rounded-full bg-tcb11-orb1 blur-2xl"></span>
  <span aria-hidden="true" class="absolute left-[calc(50%+3rem)] top-[calc(50%+1rem)] -z-10 size-40 rounded-full bg-tcb11-orb2 blur-2xl"></span>
  <div class="flex w-full max-w-[25rem] flex-col gap-1.5 rounded-3xl border border-white/35 bg-tcb11-solid p-4 shadow-tcb11-panel supports-[backdrop-filter:blur(1px)]:bg-white/15 supports-[backdrop-filter:blur(1px)]:backdrop-blur-xl supports-[backdrop-filter:blur(1px)]:backdrop-saturate-150">
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3 transition-colors hover:bg-white/10"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-[1.5px] border-white/60 bg-white/20 text-tcb11-deep shadow-tcb11-bevel backdrop-blur-sm transition-colors duration-250 peer-checked:border-white/90 peer-checked:bg-white/70 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium [text-shadow:0_1px_2px_rgb(40_10_70/0.35)]">Ambient sounds</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3 transition-colors hover:bg-white/10"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-[1.5px] border-white/60 bg-white/20 text-tcb11-deep shadow-tcb11-bevel backdrop-blur-sm transition-colors duration-250 peer-checked:border-white/90 peer-checked:bg-white/70 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium [text-shadow:0_1px_2px_rgb(40_10_70/0.35)]">Auto-brightness</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 rounded-xl px-3 transition-colors hover:bg-white/10"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-[1.5px] border-white/60 bg-white/20 text-tcb11-deep shadow-tcb11-bevel backdrop-blur-sm transition-colors duration-250 peer-checked:border-white/90 peer-checked:bg-white/70 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-white motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium [text-shadow:0_1px_2px_rgb(40_10_70/0.35)]">Reduce transparency</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb11-a: #a55ee8;
  --color-tcb11-a: oklch(0.62 0.2 300);
  --color-tcb11-b: #3aa6d8;
  --color-tcb11-b: oklch(0.66 0.13 230);
  --color-tcb11-c: #f07d4f;
  --color-tcb11-c: oklch(0.7 0.16 45);
  --color-tcb11-orb1: #ff5fa2;
  --color-tcb11-orb1: oklch(0.7 0.2 355);
  --color-tcb11-orb2: #5bf0d0;
  --color-tcb11-orb2: oklch(0.86 0.13 175);
  --color-tcb11-solid: #5b3c9e;
  --color-tcb11-solid: oklch(0.43 0.15 295);
  --color-tcb11-deep: #4a2394;
  --color-tcb11-deep: oklch(0.38 0.17 293);
  --font-tcb11-sans: 'DM Sans', system-ui, sans-serif;
  --shadow-tcb11-panel: 0 20px 50px -24px rgb(30 10 60 / 0.55);
  --shadow-tcb11-bevel: inset 0 1px 2px rgb(255 255 255 / 0.6), inset 0 -2px 4px rgb(80 40 120 / 0.2);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-11 {
  width: 100%;
  min-height: 100svh;
}
```
