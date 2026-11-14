---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/animated-svg-checkmark-tailwind-stroke-draw/"
title: "Animated SVG Checkmark in Tailwind CSS — stroke-dashoffset Draw"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The checkmark draws itself: an inline SVG path starts fully dashed-out with [stroke-dashoffset:24] and animates to group-has-checked:[stroke-dashoffset:0]."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated SVG Checkmark in Tailwind CSS — stroke-dashoffset Draw
Source: https://codefronts.com/components/tailwind-css-checkboxes/animated-svg-checkmark-tailwind-stroke-draw/

The checkmark draws itself: an inline SVG path starts fully dashed-out with [stroke-dashoffset:24] and animates to group-has-checked:[stroke-dashoffset:0]. Rows become a pipeline with a connecting rail and step captions.
## HTML
```html
<section class="tcb-09 w-full min-h-svh grid place-items-center bg-tcb09-bg px-5 py-14 font-tcb09-sans text-tcb09-ink selection:bg-tcb09-acc selection:text-white" aria-label="Draw-stroke checkmark checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb09-line bg-white px-4 py-3">
    <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-2 before:absolute before:left-[21px] before:top-[calc(50%+17px)] before:h-[calc(100%-34px)] before:w-0.5 before:rounded-full before:bg-tcb09-line before:content-['']"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-[7px] border-2 border-tcb09-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb09-acc peer-checked:bg-tcb09-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb09-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-[18px]"><path d="M4.5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] duration-450 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span><span class="block text-[15px] font-medium">Contract signed</span><span class="block text-[13px] text-tcb09-mut">Legal · step 1</span></span></label>
    <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-2 before:absolute before:left-[21px] before:top-[calc(50%+17px)] before:h-[calc(100%-34px)] before:w-0.5 before:rounded-full before:bg-tcb09-line before:content-['']"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-[7px] border-2 border-tcb09-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb09-acc peer-checked:bg-tcb09-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb09-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-[18px]"><path d="M4.5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] duration-450 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span><span class="block text-[15px] font-medium">Payment received</span><span class="block text-[13px] text-tcb09-mut">Finance · step 2</span></span></label>
    <label class="group relative flex min-h-16 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-[7px] border-2 border-tcb09-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb09-acc peer-checked:bg-tcb09-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb09-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-[18px]"><path d="M4.5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] duration-450 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span><span class="block text-[15px] font-medium">Shipment dispatched</span><span class="block text-[13px] text-tcb09-mut">Ops · step 3</span></span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb09-bg: #f3f6f4;
  --color-tcb09-bg: oklch(0.97 0.005 155);
  --color-tcb09-ink: #2c352f;
  --color-tcb09-ink: oklch(0.31 0.015 155);
  --color-tcb09-mut: #5b675f;
  --color-tcb09-mut: oklch(0.49 0.015 155);
  --color-tcb09-line: #e2e8e4;
  --color-tcb09-line: oklch(0.92 0.008 155);
  --color-tcb09-box: #9aa89f;
  --color-tcb09-box: oklch(0.7 0.018 155);
  --color-tcb09-acc: #1f8a4c;
  --color-tcb09-acc: oklch(0.55 0.14 152);
  --font-tcb09-sans: 'Outfit', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-09 {
  width: 100%;
  min-height: 100svh;
}
```
