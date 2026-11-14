---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/material-ripple-checkbox-tailwind/"
title: "Material Ripple Checkbox in Tailwind CSS — State Layer & Wave"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Material-style checkboxes with the halo done right: a 40px circular state layer sits behind the box, tints on hover and focus, and emits a ripple…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Ripple Checkbox in Tailwind CSS — State Layer & Wave
Source: https://codefronts.com/components/tailwind-css-checkboxes/material-ripple-checkbox-tailwind/

Material-style checkboxes with the halo done right: a 40px circular state layer sits behind the box, tints on hover and focus, and emits a ripple (group-has-checked:animate-tcb18-ripple) that escapes the box instead of being clipped inside it.
## HTML
```html
<section class="tcb-18 w-full min-h-svh grid place-items-center bg-tcb18-bg px-5 py-14 font-tcb18-sans text-tcb18-ink selection:bg-tcb18-acc selection:text-white" aria-label="Ripple wave checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb18-line bg-white px-3 py-2">
    <label class="group flex min-h-14 cursor-pointer items-center gap-2 pr-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-10 flex-none place-items-center rounded-full transition-colors group-hover:bg-tcb18-acc/8 group-has-focus-visible:bg-tcb18-acc/12 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb18-acc"><span class="absolute inset-0 scale-0 rounded-full bg-tcb18-acc opacity-0 group-has-checked:animate-tcb18-ripple motion-reduce:hidden"></span><span class="relative grid size-5 place-items-center rounded-[4px] border-2 border-tcb18-box bg-white text-white transition-colors duration-200 group-has-checked:border-tcb18-acc group-has-checked:bg-tcb18-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="text-[15px]">Sync across devices</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-2 pr-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-10 flex-none place-items-center rounded-full transition-colors group-hover:bg-tcb18-acc/8 group-has-focus-visible:bg-tcb18-acc/12 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb18-acc"><span class="absolute inset-0 scale-0 rounded-full bg-tcb18-acc opacity-0 group-has-checked:animate-tcb18-ripple motion-reduce:hidden"></span><span class="relative grid size-5 place-items-center rounded-[4px] border-2 border-tcb18-box bg-white text-white transition-colors duration-200 group-has-checked:border-tcb18-acc group-has-checked:bg-tcb18-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="text-[15px]">Offline downloads</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-2 pr-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-10 flex-none place-items-center rounded-full transition-colors group-hover:bg-tcb18-acc/8 group-has-focus-visible:bg-tcb18-acc/12 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb18-acc"><span class="absolute inset-0 scale-0 rounded-full bg-tcb18-acc opacity-0 group-has-checked:animate-tcb18-ripple motion-reduce:hidden"></span><span class="relative grid size-5 place-items-center rounded-[4px] border-2 border-tcb18-box bg-white text-white transition-colors duration-200 group-has-checked:border-tcb18-acc group-has-checked:bg-tcb18-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3.5 scale-50 opacity-0 transition duration-200 ease-[cubic-bezier(.2,.9,.3,1.2)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span></span><span class="text-[15px]">Background refresh</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb18-bg: #f4f5fa;
  --color-tcb18-bg: oklch(0.97 0.006 275);
  --color-tcb18-ink: #2c3040;
  --color-tcb18-ink: oklch(0.3 0.025 275);
  --color-tcb18-line: #e5e7f0;
  --color-tcb18-line: oklch(0.925 0.01 275);
  --color-tcb18-box: #6f7690;
  --color-tcb18-box: oklch(0.56 0.04 275);
  --color-tcb18-acc: #4c5fd5;
  --color-tcb18-acc: oklch(0.54 0.18 270);
  --font-tcb18-sans: 'DM Sans', system-ui, sans-serif;
  --animate-tcb18-ripple: tcb18-ripple 0.55s ease-out;

  @keyframes tcb18-ripple {
    from {
      scale: 0.4;
      opacity: 0.3;
    }

    to {
      scale: 1.25;
      opacity: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-18 {
  width: 100%;
  min-height: 100svh;
}
```
