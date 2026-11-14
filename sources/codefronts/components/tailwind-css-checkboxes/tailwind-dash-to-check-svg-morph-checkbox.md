---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-dash-to-check-svg-morph-checkbox/"
title: "Tailwind CSS Dash-to-Check SVG Morph Checkbox"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A pending dash retracts as a checkmark draws in — two SVG paths trading stroke-dashoffset with a 120ms stagger, while the whole glyph tilts -rotate-8."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dash-to-Check SVG Morph Checkbox
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-dash-to-check-svg-morph-checkbox/

A pending dash retracts as a checkmark draws in — two SVG paths trading stroke-dashoffset with a 120ms stagger, while the whole glyph tilts -rotate-8. New: a status label on the right swaps Pending → Approved, so the row states its meaning in words.
## HTML
```html
<section class="tcb-24 w-full min-h-svh grid place-items-center bg-tcb24-bg px-5 py-14 font-tcb24-sans text-tcb24-ink selection:bg-tcb24-acc selection:text-white" aria-label="Dash to check morph checkboxes">
  <div class="w-full max-w-[26rem] rounded-2xl border border-tcb24-line bg-white px-4 py-2.5">
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-lg border-2 border-tcb24-box bg-white text-tcb24-dash transition-colors duration-300 peer-checked:border-tcb24-acc peer-checked:bg-tcb24-acc peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb24-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-5 transition-[rotate] duration-400 group-has-checked:-rotate-8"><path d="M6 12H18" class="transition-[stroke-dashoffset] duration-300 [stroke-dasharray:12] [stroke-dashoffset:0] group-has-checked:[stroke-dashoffset:12] motion-reduce:transition-none"/><path d="M5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] delay-120 duration-400 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span class="flex-1 text-[15px]">Review approved</span><span aria-hidden="true" class="font-tcb24-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb24-mut after:content-['Pending'] group-has-checked:text-tcb24-acc group-has-checked:after:content-['Approved']"></span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-lg border-2 border-tcb24-box bg-white text-tcb24-dash transition-colors duration-300 peer-checked:border-tcb24-acc peer-checked:bg-tcb24-acc peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb24-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-5 transition-[rotate] duration-400 group-has-checked:-rotate-8"><path d="M6 12H18" class="transition-[stroke-dashoffset] duration-300 [stroke-dasharray:12] [stroke-dashoffset:0] group-has-checked:[stroke-dashoffset:12] motion-reduce:transition-none"/><path d="M5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] delay-120 duration-400 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span class="flex-1 text-[15px]">Awaiting sign-off</span><span aria-hidden="true" class="font-tcb24-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb24-mut after:content-['Pending'] group-has-checked:text-tcb24-acc group-has-checked:after:content-['Approved']"></span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-7 flex-none place-items-center rounded-lg border-2 border-tcb24-box bg-white text-tcb24-dash transition-colors duration-300 peer-checked:border-tcb24-acc peer-checked:bg-tcb24-acc peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb24-acc motion-reduce:transition-none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="size-5 transition-[rotate] duration-400 group-has-checked:-rotate-8"><path d="M6 12H18" class="transition-[stroke-dashoffset] duration-300 [stroke-dasharray:12] [stroke-dashoffset:0] group-has-checked:[stroke-dashoffset:12] motion-reduce:transition-none"/><path d="M5 12.5 10 18 20 6" class="transition-[stroke-dashoffset] delay-120 duration-400 ease-[cubic-bezier(.6,.1,.3,1)] [stroke-dasharray:24] [stroke-dashoffset:24] group-has-checked:[stroke-dashoffset:0] motion-reduce:transition-none"/></svg></span><span class="flex-1 text-[15px]">Pending checks</span><span aria-hidden="true" class="font-tcb24-mono text-[11px] font-semibold uppercase tracking-[0.08em] text-tcb24-mut after:content-['Pending'] group-has-checked:text-tcb24-acc group-has-checked:after:content-['Approved']"></span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb24-bg: #eef2f8;
  --color-tcb24-bg: oklch(0.96 0.01 255);
  --color-tcb24-ink: #2c3540;
  --color-tcb24-ink: oklch(0.32 0.02 250);
  --color-tcb24-mut: #5e6a7c;
  --color-tcb24-mut: oklch(0.5 0.03 255);
  --color-tcb24-line: #dde5f0;
  --color-tcb24-line: oklch(0.92 0.013 255);
  --color-tcb24-box: #8e9db4;
  --color-tcb24-box: oklch(0.7 0.035 255);
  --color-tcb24-dash: #6b7890;
  --color-tcb24-dash: oklch(0.57 0.035 255);
  --color-tcb24-acc: #1f6fc0;
  --color-tcb24-acc: oklch(0.53 0.15 250);
  --font-tcb24-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tcb24-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-24 {
  width: 100%;
  min-height: 100svh;
}
```
