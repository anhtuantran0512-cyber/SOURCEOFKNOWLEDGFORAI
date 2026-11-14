---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/liquid-fill-checkbox-tailwind-water-wave/"
title: "Liquid Fill Checkbox Animation in Tailwind CSS — Water Wave"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Water rises into the box on check: an oversized, wavy-topped blob slides up from translate-y-[105%] to group-has-checked:translate-y-0, then keeps sloshing…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Fill Checkbox Animation in Tailwind CSS — Water Wave
Source: https://codefronts.com/components/tailwind-css-checkboxes/liquid-fill-checkbox-tailwind-water-wave/

Water rises into the box on check: an oversized, wavy-topped blob slides up from translate-y-[105%] to group-has-checked:translate-y-0, then keeps sloshing with animate-tcb13-wave. Hovering an empty box now lets the water peek in, previewing the action.
## HTML
```html
<section class="tcb-13 w-full min-h-svh grid place-items-center bg-tcb13-bg px-5 py-14 font-tcb13-sans text-tcb13-ink selection:bg-tcb13-water selection:text-white" aria-label="Liquid fill checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb13-line bg-white px-4 py-2.5">
    <label class="group flex min-h-15 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-7 flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb13-box bg-white text-white transition-colors duration-300 peer-checked:border-tcb13-water peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb13-water"><span class="absolute -left-1/4 bottom-0 h-[130%] w-[150%] translate-y-[105%] rounded-[42%_46%_0_0/14px] bg-tcb13-water transition-transform duration-500 ease-[cubic-bezier(.5,.1,.3,1)] group-hover:translate-y-[78%] group-has-checked:translate-y-0 group-has-checked:animate-tcb13-wave motion-reduce:animate-none motion-reduce:transition-none"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] opacity-0 transition-opacity delay-180 duration-250 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span><span class="block text-[15px] font-medium">Drink water</span><span class="block text-[13px] text-tcb13-mut">2 litres</span></span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-7 flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb13-box bg-white text-white transition-colors duration-300 peer-checked:border-tcb13-water peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb13-water"><span class="absolute -left-1/4 bottom-0 h-[130%] w-[150%] translate-y-[105%] rounded-[42%_46%_0_0/14px] bg-tcb13-water transition-transform duration-500 ease-[cubic-bezier(.5,.1,.3,1)] group-hover:translate-y-[78%] group-has-checked:translate-y-0 group-has-checked:animate-tcb13-wave motion-reduce:animate-none motion-reduce:transition-none"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] opacity-0 transition-opacity delay-180 duration-250 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span><span class="block text-[15px] font-medium">Morning workout</span><span class="block text-[13px] text-tcb13-mut">30 minutes</span></span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-7 flex-none place-items-center overflow-hidden rounded-lg border-2 border-tcb13-box bg-white text-white transition-colors duration-300 peer-checked:border-tcb13-water peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb13-water"><span class="absolute -left-1/4 bottom-0 h-[130%] w-[150%] translate-y-[105%] rounded-[42%_46%_0_0/14px] bg-tcb13-water transition-transform duration-500 ease-[cubic-bezier(.5,.1,.3,1)] group-hover:translate-y-[78%] group-has-checked:translate-y-0 group-has-checked:animate-tcb13-wave motion-reduce:animate-none motion-reduce:transition-none"></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] opacity-0 transition-opacity delay-180 duration-250 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span><span class="block text-[15px] font-medium">Read 20 pages</span><span class="block text-[13px] text-tcb13-mut">Before bed</span></span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb13-bg: #eef4f8;
  --color-tcb13-bg: oklch(0.96 0.008 235);
  --color-tcb13-ink: #2c3a44;
  --color-tcb13-ink: oklch(0.33 0.025 240);
  --color-tcb13-mut: #566873;
  --color-tcb13-mut: oklch(0.49 0.025 235);
  --color-tcb13-line: #dce6ee;
  --color-tcb13-line: oklch(0.92 0.012 240);
  --color-tcb13-box: #8ea6b6;
  --color-tcb13-box: oklch(0.7 0.035 235);
  --color-tcb13-water: #2b86c4;
  --color-tcb13-water: oklch(0.58 0.13 240);
  --font-tcb13-sans: 'Outfit', system-ui, sans-serif;
  --animate-tcb13-wave: tcb13-wave 3s linear infinite;

  @keyframes tcb13-wave {
    0%,
        100% {
      border-radius: 42% 46% 0 0 / 14px;
    }

    50% {
      border-radius: 46% 40% 0 0 / 12px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-13 {
  width: 100%;
  min-height: 100svh;
}
```
