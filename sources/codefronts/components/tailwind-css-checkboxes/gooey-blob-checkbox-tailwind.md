---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/gooey-blob-checkbox-tailwind/"
title: "Gooey Blob Checkbox in Tailwind CSS — blur + contrast Filter"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Two blobs merge into a fill like drops of ink: a satellite orbits out and back while the main blob swells, and blur-[4px] contrast-[14] on their parent fuses…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gooey Blob Checkbox in Tailwind CSS — blur + contrast Filter
Source: https://codefronts.com/components/tailwind-css-checkboxes/gooey-blob-checkbox-tailwind/

Two blobs merge into a fill like drops of ink: a satellite orbits out and back while the main blob swells, and blur-[4px] contrast-[14] on their parent fuses them into one sticky shape. The port fixes the effect itself — the contrast trick only works over an opaque backdrop, which the original lacked.
## HTML
```html
<section class="tcb-21 w-full min-h-svh grid place-items-center bg-tcb21-bg px-5 py-14 font-tcb21-sans text-tcb21-ink selection:bg-tcb21-acc selection:text-white" aria-label="Gooey blob checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb21-line bg-white px-4 py-2.5">
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center overflow-hidden rounded-[9px] border-2 border-tcb21-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb21-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb21-acc"><span class="absolute inset-0 bg-white blur-[4px] contrast-[14]"><span class="absolute left-1/2 top-1/2 size-4 -translate-1/2 scale-0 rounded-full bg-tcb21-acc transition-[scale] duration-400 ease-[cubic-bezier(.3,1.2,.4,1)] group-has-checked:scale-[2.6] motion-reduce:transition-none"></span><span class="absolute left-1/2 top-1/2 size-[9px] -translate-1/2 scale-0 rounded-full bg-tcb21-acc group-has-checked:animate-tcb21-orbit group-has-checked:scale-200 motion-reduce:animate-none"></span></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] scale-50 opacity-0 transition delay-120 duration-250 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Blend layers</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center overflow-hidden rounded-[9px] border-2 border-tcb21-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb21-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb21-acc"><span class="absolute inset-0 bg-white blur-[4px] contrast-[14]"><span class="absolute left-1/2 top-1/2 size-4 -translate-1/2 scale-0 rounded-full bg-tcb21-acc transition-[scale] duration-400 ease-[cubic-bezier(.3,1.2,.4,1)] group-has-checked:scale-[2.6] motion-reduce:transition-none"></span><span class="absolute left-1/2 top-1/2 size-[9px] -translate-1/2 scale-0 rounded-full bg-tcb21-acc group-has-checked:animate-tcb21-orbit group-has-checked:scale-200 motion-reduce:animate-none"></span></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] scale-50 opacity-0 transition delay-120 duration-250 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Merge branches</span></label>
    <label class="group flex min-h-14 cursor-pointer items-center gap-4 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="relative grid size-[30px] flex-none place-items-center overflow-hidden rounded-[9px] border-2 border-tcb21-box bg-white text-white transition-colors duration-250 peer-checked:border-tcb21-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb21-acc"><span class="absolute inset-0 bg-white blur-[4px] contrast-[14]"><span class="absolute left-1/2 top-1/2 size-4 -translate-1/2 scale-0 rounded-full bg-tcb21-acc transition-[scale] duration-400 ease-[cubic-bezier(.3,1.2,.4,1)] group-has-checked:scale-[2.6] motion-reduce:transition-none"></span><span class="absolute left-1/2 top-1/2 size-[9px] -translate-1/2 scale-0 rounded-full bg-tcb21-acc group-has-checked:animate-tcb21-orbit group-has-checked:scale-200 motion-reduce:animate-none"></span></span><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="relative z-10 size-[15px] scale-50 opacity-0 transition delay-120 duration-250 ease-[cubic-bezier(.2,.9,.3,1.3)] group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px] font-medium">Fuse particles</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb21-bg: #fbf3f1;
  --color-tcb21-bg: oklch(0.97 0.012 30);
  --color-tcb21-ink: #3a2723;
  --color-tcb21-ink: oklch(0.29 0.03 30);
  --color-tcb21-line: #f0ded9;
  --color-tcb21-line: oklch(0.92 0.02 30);
  --color-tcb21-box: #d59c90;
  --color-tcb21-box: oklch(0.74 0.07 30);
  --color-tcb21-acc: #e0364a;
  --color-tcb21-acc: oklch(0.6 0.21 18);
  --font-tcb21-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --animate-tcb21-orbit: tcb21-orbit 0.55s ease;

  @keyframes tcb21-orbit {
    0% {
      translate: -50% -50%;
      scale: 0;
    }

    45% {
      translate: 30% -160%;
      scale: 1;
    }

    100% {
      translate: -50% -50%;
      scale: 2;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-21 {
  width: 100%;
  min-height: 100svh;
}
```
