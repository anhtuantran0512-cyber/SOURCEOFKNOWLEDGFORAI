---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-todo-list-checkbox-strikethrough/"
title: "Tailwind CSS To-Do List Checkbox with Animated Strikethrough"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "The to-do list done properly: ticking a task draws a strike across its label with after:scale-x-0 → group-has-checked:after:scale-x-100, and a zero-JS header…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS To-Do List Checkbox with Animated Strikethrough
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-todo-list-checkbox-strikethrough/

The to-do list done properly: ticking a task draws a strike across its label with after:scale-x-0 → group-has-checked:after:scale-x-100, and a zero-JS header counter reports "2 of 4 done" using CSS counters. Done items stay readable at 4.6:1 instead of fading to 2.3:1.
## HTML
```html
<section class="tcb-20 w-full min-h-svh grid place-items-center bg-tcb20-bg px-5 py-14 font-tcb20-sans text-tcb20-ink selection:bg-tcb20-acc selection:text-white" aria-label="To-do list with strikethrough">
  <div class="w-full max-w-[26rem] rounded-2xl border border-tcb20-line bg-white px-4 pb-3 pt-4 [counter-reset:tcb20]">
    <h2 class="px-2 pb-1 text-lg font-bold tracking-[-0.01em]">Launch week</h2>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 px-2 has-checked:[counter-increment:tcb20]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb20-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb20-acc peer-checked:bg-tcb20-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb20-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="relative text-[15px] transition-colors duration-300 after:absolute after:left-0 after:top-[52%] after:h-0.5 after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform after:duration-350 after:ease-[cubic-bezier(.5,.1,.2,1)] after:content-[''] group-has-checked:text-tcb20-done group-has-checked:after:scale-x-100 motion-reduce:after:transition-none">Write the launch email</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 px-2 has-checked:[counter-increment:tcb20]"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb20-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb20-acc peer-checked:bg-tcb20-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb20-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="relative text-[15px] transition-colors duration-300 after:absolute after:left-0 after:top-[52%] after:h-0.5 after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform after:duration-350 after:ease-[cubic-bezier(.5,.1,.2,1)] after:content-[''] group-has-checked:text-tcb20-done group-has-checked:after:scale-x-100 motion-reduce:after:transition-none">Review pull requests</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 px-2 has-checked:[counter-increment:tcb20]"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb20-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb20-acc peer-checked:bg-tcb20-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb20-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="relative text-[15px] transition-colors duration-300 after:absolute after:left-0 after:top-[52%] after:h-0.5 after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform after:duration-350 after:ease-[cubic-bezier(.5,.1,.2,1)] after:content-[''] group-has-checked:text-tcb20-done group-has-checked:after:scale-x-100 motion-reduce:after:transition-none">Book the venue</span></label>
    <label class="group flex min-h-12 cursor-pointer items-center gap-3.5 px-2 has-checked:[counter-increment:tcb20]"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[22px] flex-none place-items-center rounded-md border-2 border-tcb20-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb20-acc peer-checked:bg-tcb20-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb20-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="relative text-[15px] transition-colors duration-300 after:absolute after:left-0 after:top-[52%] after:h-0.5 after:w-full after:origin-left after:scale-x-0 after:bg-current after:transition-transform after:duration-350 after:ease-[cubic-bezier(.5,.1,.2,1)] after:content-[''] group-has-checked:text-tcb20-done group-has-checked:after:scale-x-100 motion-reduce:after:transition-none">Update the changelog</span></label>
    <p aria-hidden="true" class="mt-2 border-t border-tcb20-line px-2 pt-3 text-[13px] font-semibold text-tcb20-mut before:text-tcb20-acc before:content-[counter(tcb20)]"> of 4 done</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb20-bg: #f3f6f4;
  --color-tcb20-bg: oklch(0.97 0.005 155);
  --color-tcb20-ink: #2c3a33;
  --color-tcb20-ink: oklch(0.33 0.02 160);
  --color-tcb20-mut: #5b675f;
  --color-tcb20-mut: oklch(0.49 0.015 155);
  --color-tcb20-done: #62786c;
  --color-tcb20-done: oklch(0.54 0.03 160);
  --color-tcb20-line: #e1e8e3;
  --color-tcb20-line: oklch(0.92 0.008 155);
  --color-tcb20-box: #9aaca1;
  --color-tcb20-box: oklch(0.72 0.02 155);
  --color-tcb20-acc: #1f8a4c;
  --color-tcb20-acc: oklch(0.55 0.14 152);
  --font-tcb20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-20 {
  width: 100%;
  min-height: 100svh;
}
```
