---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/neumorphism-checkbox-tailwind-soft-ui/"
title: "Neumorphism Checkbox in Tailwind CSS — Soft UI"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Soft-UI boxes that look extruded when off and pressed-in when on: the two states are two shadow tokens, shadow-tcb12-out and peer-checked:shadow-tcb12-in."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphism Checkbox in Tailwind CSS — Soft UI
Source: https://codefronts.com/components/tailwind-css-checkboxes/neumorphism-checkbox-tailwind-soft-ui/

Soft-UI boxes that look extruded when off and pressed-in when on: the two states are two shadow tokens, shadow-tcb12-out and peer-checked:shadow-tcb12-in. Checked labels darken and a thin accent edge keeps the state legible — neumorphism's usual weakness.
## HTML
```html
<section class="tcb-12 w-full min-h-svh grid place-items-center bg-tcb12-surface px-5 py-14 font-tcb12-sans text-tcb12-mut selection:bg-tcb12-acc selection:text-white" aria-label="Neumorphic checkboxes">
  <div class="flex w-full max-w-[25rem] flex-col gap-1.5 rounded-[22px] bg-tcb12-surface p-5 shadow-tcb12-panel">
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2.5"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[30px] flex-none place-items-center rounded-[9px] bg-tcb12-surface text-tcb12-acc shadow-tcb12-out transition-shadow duration-300 peer-checked:shadow-tcb12-in peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb12-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 scale-50 opacity-0 transition duration-250 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-semibold transition-colors group-has-checked:text-tcb12-ink">Silent mode</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2.5"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[30px] flex-none place-items-center rounded-[9px] bg-tcb12-surface text-tcb12-acc shadow-tcb12-out transition-shadow duration-300 peer-checked:shadow-tcb12-in peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb12-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 scale-50 opacity-0 transition duration-250 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-semibold transition-colors group-has-checked:text-tcb12-ink">Haptic feedback</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2.5"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[30px] flex-none place-items-center rounded-[9px] bg-tcb12-surface text-tcb12-acc shadow-tcb12-out transition-shadow duration-300 peer-checked:shadow-tcb12-in peer-focus-visible:outline-3 peer-focus-visible:outline-offset-4 peer-focus-visible:outline-tcb12-acc motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-4 scale-50 opacity-0 transition duration-250 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-semibold transition-colors group-has-checked:text-tcb12-ink">Battery saver</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb12-surface: #e6e9ef;
  --color-tcb12-surface: oklch(0.93 0.008 265);
  --color-tcb12-ink: #2b3040;
  --color-tcb12-ink: oklch(0.3 0.03 270);
  --color-tcb12-mut: #555c6a;
  --color-tcb12-mut: oklch(0.47 0.02 265);
  --color-tcb12-acc: #4a5fd6;
  --color-tcb12-acc: oklch(0.55 0.17 268);
  --font-tcb12-sans: 'Manrope', system-ui, sans-serif;
  --shadow-tcb12-panel: 9px 9px 20px #c4c9d3, -9px -9px 20px #ffffff;
  --shadow-tcb12-out: 4px 4px 8px #c4c9d3, -4px -4px 8px #ffffff;
  --shadow-tcb12-in: inset 4px 4px 8px #c4c9d3, inset -4px -4px 8px #ffffff, 0 0 0 1px rgb(74 95 214 / 0.35);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-12 {
  width: 100%;
  min-height: 100svh;
}
```
