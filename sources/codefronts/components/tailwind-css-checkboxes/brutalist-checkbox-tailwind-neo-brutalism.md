---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/brutalist-checkbox-tailwind-neo-brutalism/"
title: "Brutalist Checkbox in Tailwind CSS — Neo-Brutalism Hard Shadow"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Thick black borders, a 4px offset shadow and a box that physically presses into its shadow on check (group-has-checked:translate-1 shadow-none)."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Checkbox in Tailwind CSS — Neo-Brutalism Hard Shadow
Source: https://codefronts.com/components/tailwind-css-checkboxes/brutalist-checkbox-tailwind-neo-brutalism/

Thick black borders, a 4px offset shadow and a box that physically presses into its shadow on check (group-has-checked:translate-1 shadow-none). New: the checked label gets a yellow marker highlight with box-decoration-clone, so the whole row shouts its state.
## HTML
```html
<section class="tcb-15 w-full min-h-svh grid place-items-center bg-tcb15-bg px-5 py-14 font-tcb15-display text-black selection:bg-black selection:text-tcb15-acc" aria-label="Brutalist checkboxes">
  <div class="w-full max-w-[25rem] border-4 border-black bg-white p-2 shadow-tcb15-panel">
    <p class="border-b-4 border-black px-3 pb-2 pt-1 font-tcb15-mono text-xs font-bold uppercase tracking-[0.14em]">Release checklist</p>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-3"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-7 flex-none place-items-center border-4 border-black bg-white shadow-tcb15-hard transition duration-75 ease-linear group-hover:-translate-0.5 group-hover:shadow-tcb15-lift peer-checked:translate-1 peer-checked:bg-tcb15-acc peer-checked:shadow-none peer-focus-visible:outline-4 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-black motion-reduce:translate-0 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="px-1 text-base tracking-[0.04em] box-decoration-clone group-has-checked:bg-tcb15-acc">SHIP IT</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-3"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-7 flex-none place-items-center border-4 border-black bg-white shadow-tcb15-hard transition duration-75 ease-linear group-hover:-translate-0.5 group-hover:shadow-tcb15-lift peer-checked:translate-1 peer-checked:bg-tcb15-acc peer-checked:shadow-none peer-focus-visible:outline-4 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-black motion-reduce:translate-0 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="px-1 text-base tracking-[0.04em] box-decoration-clone group-has-checked:bg-tcb15-acc">BREAK THINGS</span></label>
    <label class="group flex min-h-15 cursor-pointer items-center gap-4 px-3"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-7 flex-none place-items-center border-4 border-black bg-white shadow-tcb15-hard transition duration-75 ease-linear group-hover:-translate-0.5 group-hover:shadow-tcb15-lift peer-checked:translate-1 peer-checked:bg-tcb15-acc peer-checked:shadow-none peer-focus-visible:outline-4 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-black motion-reduce:translate-0 motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" class="size-4 opacity-0 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="px-1 text-base tracking-[0.04em] box-decoration-clone group-has-checked:bg-tcb15-acc">NO REGRETS</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb15-bg: #e8e6df;
  --color-tcb15-bg: oklch(0.92 0.008 90);
  --color-tcb15-acc: #f7ff37;
  --color-tcb15-acc: oklch(0.96 0.2 110);
  --font-tcb15-display: 'Archivo Black', 'Arial Black', sans-serif;
  --font-tcb15-mono: 'Space Mono', ui-monospace, monospace;
  --shadow-tcb15-panel: 8px 8px 0 #000;
  --shadow-tcb15-hard: 4px 4px 0 #000;
  --shadow-tcb15-lift: 6px 6px 0 #000;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-15 {
  width: 100%;
  min-height: 100svh;
}
```
