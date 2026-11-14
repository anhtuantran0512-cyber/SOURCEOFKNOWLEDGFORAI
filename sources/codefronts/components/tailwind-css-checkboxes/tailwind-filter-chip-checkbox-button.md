---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-filter-chip-checkbox-button/"
title: "Tailwind Filter Chip Checkbox — Style Checkbox as Button"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The e-commerce facet bar in a single class list per chip: has-checked:bg-tcb02-acc repaints the whole <label>, a leading tick unfolds, and a pure-CSS counter…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Filter Chip Checkbox — Style Checkbox as Button
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-filter-chip-checkbox-button/

The e-commerce facet bar in a single class list per chip: has-checked:bg-tcb02-acc repaints the whole <label>, a leading tick unfolds, and a pure-CSS counter tallies the active filters live — has-checked:[counter-increment:tcb02] plus after:content-[counter(tcb02)]. Zero JavaScript.
## HTML
```html
<section class="tcb-02 w-full min-h-svh grid place-items-center bg-tcb02-bg px-5 py-14 font-tcb02-sans text-tcb02-ink selection:bg-tcb02-acc selection:text-white" aria-label="Filter tag pills">
  <fieldset class="flex w-full max-w-[30rem] flex-wrap gap-2.5 [counter-reset:tcb02]">
    <legend class="mb-3.5 text-xs font-bold uppercase tracking-[0.12em] text-tcb02-mut">Filter by category</legend>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only" checked><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Design</label>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only"><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Engineering</label>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only" checked><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Marketing</label>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only"><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Remote</label>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only"><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Full-time</label>
    <label class="group inline-flex min-h-11 cursor-pointer select-none items-center rounded-full border-[1.5px] border-tcb02-line bg-white px-4 text-sm font-semibold transition-colors duration-200 hover:border-tcb02-acc has-checked:border-tcb02-acc has-checked:bg-tcb02-acc has-checked:text-white has-checked:[counter-increment:tcb02] has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb02-acc motion-reduce:transition-none"><input type="checkbox" class="sr-only" checked><span aria-hidden="true" class="inline-flex w-0 scale-50 overflow-hidden opacity-0 transition-all duration-200 group-has-checked:mr-1.5 group-has-checked:w-3.5 group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 flex-none"><path d="M20 6 9 17l-5-5"/></svg></span>Contract</label>
    <p aria-hidden="true" class="mt-3 flex basis-full items-center gap-2 text-[13px] font-semibold text-tcb02-mut after:grid after:h-6 after:min-w-6 after:place-items-center after:rounded-full after:bg-tcb02-ink after:px-2 after:text-xs after:text-white after:content-[counter(tcb02)]">Active filters</p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb02-bg: #f4f6f5;
  --color-tcb02-bg: oklch(0.97 0.004 160);
  --color-tcb02-ink: #2f3538;
  --color-tcb02-ink: oklch(0.32 0.01 220);
  --color-tcb02-mut: #5f6763;
  --color-tcb02-mut: oklch(0.5 0.01 160);
  --color-tcb02-line: #d6dcd9;
  --color-tcb02-line: oklch(0.89 0.008 160);
  --color-tcb02-acc: #1f7a57;
  --color-tcb02-acc: oklch(0.5 0.11 160);
  --font-tcb02-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-02 {
  width: 100%;
  min-height: 100svh;
}
```
