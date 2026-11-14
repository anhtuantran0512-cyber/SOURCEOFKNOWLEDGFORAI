---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/3d-flip-checkbox-tailwind/"
title: "3D Flip Checkbox in Tailwind CSS — perspective & backface-hidden"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Each box is a two-faced card that flips on its Y axis to reveal a filled, ticked back — now using Tailwind v4's native 3D utilities: perspective-[600px],…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Checkbox in Tailwind CSS — perspective & backface-hidden
Source: https://codefronts.com/components/tailwind-css-checkboxes/3d-flip-checkbox-tailwind/

Each box is a two-faced card that flips on its Y axis to reveal a filled, ticked back — now using Tailwind v4's native 3D utilities: perspective-[600px], transform-3d, backface-hidden and rotate-y-180. Reduced-motion users get a cross-fade instead.
## HTML
```html
<section class="tcb-17 w-full min-h-svh grid place-items-center bg-tcb17-bg px-5 py-14 font-tcb17-sans text-tcb17-ink selection:bg-tcb17-acc selection:text-white" aria-label="3D flip checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb17-line bg-white px-4 py-2.5">
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="block size-7 flex-none rounded-lg perspective-[600px] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb17-acc"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.4,.8,.3,1)] transform-3d group-has-checked:rotate-y-180 motion-reduce:transition-none motion-reduce:group-has-checked:rotate-y-0"><span class="absolute inset-0 rounded-lg border-2 border-tcb17-box bg-white backface-hidden transition-[border-color,opacity] group-hover:border-tcb17-acc motion-reduce:group-has-checked:opacity-0"></span><span class="absolute inset-0 grid rotate-y-180 place-items-center rounded-lg bg-tcb17-acc text-white backface-hidden motion-reduce:rotate-y-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-has-checked:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span></span></span><span class="text-[15px]">Task complete</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="block size-7 flex-none rounded-lg perspective-[600px] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb17-acc"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.4,.8,.3,1)] transform-3d group-has-checked:rotate-y-180 motion-reduce:transition-none motion-reduce:group-has-checked:rotate-y-0"><span class="absolute inset-0 rounded-lg border-2 border-tcb17-box bg-white backface-hidden transition-[border-color,opacity] group-hover:border-tcb17-acc motion-reduce:group-has-checked:opacity-0"></span><span class="absolute inset-0 grid rotate-y-180 place-items-center rounded-lg bg-tcb17-acc text-white backface-hidden motion-reduce:rotate-y-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-has-checked:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span></span></span><span class="text-[15px]">Mark as read</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="block size-7 flex-none rounded-lg perspective-[600px] peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb17-acc"><span class="relative block size-full transition-transform duration-500 ease-[cubic-bezier(.4,.8,.3,1)] transform-3d group-has-checked:rotate-y-180 motion-reduce:transition-none motion-reduce:group-has-checked:rotate-y-0"><span class="absolute inset-0 rounded-lg border-2 border-tcb17-box bg-white backface-hidden transition-[border-color,opacity] group-hover:border-tcb17-acc motion-reduce:group-has-checked:opacity-0"></span><span class="absolute inset-0 grid rotate-y-180 place-items-center rounded-lg bg-tcb17-acc text-white backface-hidden motion-reduce:rotate-y-0 motion-reduce:opacity-0 motion-reduce:transition-opacity motion-reduce:group-has-checked:opacity-100"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span></span></span><span class="text-[15px]">Approve request</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb17-bg: #eef5f4;
  --color-tcb17-bg: oklch(0.965 0.008 180);
  --color-tcb17-ink: #2b3a38;
  --color-tcb17-ink: oklch(0.33 0.02 180);
  --color-tcb17-line: #dbe8e6;
  --color-tcb17-line: oklch(0.92 0.012 180);
  --color-tcb17-box: #8fb0ab;
  --color-tcb17-box: oklch(0.72 0.04 180);
  --color-tcb17-acc: #127a70;
  --color-tcb17-acc: oklch(0.5 0.1 180);
  --font-tcb17-sans: 'Instrument Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-17 {
  width: 100%;
  min-height: 100svh;
}
```
