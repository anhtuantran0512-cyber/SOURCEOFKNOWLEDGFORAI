---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/slide-in-label-checkbox-tailwind/"
title: "Slide-In Label Checkbox in Tailwind CSS — Saved Tag Reveal"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Checking a row slides a SAVED tag in from the left, pushing the label along."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide-In Label Checkbox in Tailwind CSS — Saved Tag Reveal
Source: https://codefronts.com/components/tailwind-css-checkboxes/slide-in-label-checkbox-tailwind/

Checking a row slides a SAVED tag in from the left, pushing the label along. The port rebuilds the mechanics: instead of translating a tag into overlap and patching the gap with margin-right, the tag sits in a grid column that animates grid-cols-[0fr_auto] → grid-cols-[1fr_auto], so the label moves because the layout does.
## HTML
```html
<section class="tcb-28 w-full min-h-svh grid place-items-center bg-tcb28-bg px-5 py-14 font-tcb28-sans text-tcb28-mut selection:bg-tcb28-acc selection:text-white" aria-label="Slide-in label checkboxes">
  <div class="w-full max-w-[26rem] rounded-2xl border border-tcb28-line bg-white px-4 py-2.5">
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb28-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb28-acc peer-checked:bg-tcb28-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb28-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="inline-grid grid-cols-[0fr_auto] items-center transition-[grid-template-columns] duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:grid-cols-[1fr_auto] motion-reduce:transition-none"><span aria-hidden="true" class="min-w-0 overflow-hidden"><span class="mr-2 inline-block -translate-x-full rounded-md bg-tcb28-acc px-2 py-0.5 font-tcb28-mono text-[11px] font-bold uppercase tracking-[0.08em] text-white opacity-0 transition duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:translate-x-0">Saved</span></span><span class="text-[15px] font-medium transition-colors group-has-checked:text-tcb28-ink">Keep in library</span></span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb28-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb28-acc peer-checked:bg-tcb28-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb28-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="inline-grid grid-cols-[0fr_auto] items-center transition-[grid-template-columns] duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:grid-cols-[1fr_auto] motion-reduce:transition-none"><span aria-hidden="true" class="min-w-0 overflow-hidden"><span class="mr-2 inline-block -translate-x-full rounded-md bg-tcb28-acc px-2 py-0.5 font-tcb28-mono text-[11px] font-bold uppercase tracking-[0.08em] text-white opacity-0 transition duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:translate-x-0">Saved</span></span><span class="text-[15px] font-medium transition-colors group-has-checked:text-tcb28-ink">Pin to sidebar</span></span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-6 flex-none place-items-center rounded-[7px] border-2 border-tcb28-box bg-white text-white transition-colors duration-200 peer-checked:border-tcb28-acc peer-checked:bg-tcb28-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb28-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="inline-grid grid-cols-[0fr_auto] items-center transition-[grid-template-columns] duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:grid-cols-[1fr_auto] motion-reduce:transition-none"><span aria-hidden="true" class="min-w-0 overflow-hidden"><span class="mr-2 inline-block -translate-x-full rounded-md bg-tcb28-acc px-2 py-0.5 font-tcb28-mono text-[11px] font-bold uppercase tracking-[0.08em] text-white opacity-0 transition duration-350 ease-[cubic-bezier(.3,.9,.3,1)] group-has-checked:translate-x-0 group-has-checked:opacity-100 motion-reduce:translate-x-0">Saved</span></span><span class="text-[15px] font-medium transition-colors group-has-checked:text-tcb28-ink">Add to watchlist</span></span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb28-bg: #eef5f6;
  --color-tcb28-bg: oklch(0.965 0.008 205);
  --color-tcb28-ink: #1f2f30;
  --color-tcb28-ink: oklch(0.28 0.02 205);
  --color-tcb28-mut: #4c5f61;
  --color-tcb28-mut: oklch(0.46 0.02 205);
  --color-tcb28-line: #daeaeb;
  --color-tcb28-line: oklch(0.92 0.015 205);
  --color-tcb28-box: #8fb0b3;
  --color-tcb28-box: oklch(0.72 0.035 205);
  --color-tcb28-acc: #137580;
  --color-tcb28-acc: oklch(0.5 0.09 205);
  --font-tcb28-sans: 'Manrope', system-ui, sans-serif;
  --font-tcb28-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-28 {
  width: 100%;
  min-height: 100svh;
}
```
