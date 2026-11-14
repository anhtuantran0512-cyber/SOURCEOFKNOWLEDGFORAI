---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/bouncy-checkbox-animation-tailwind/"
title: "Bouncy Checkbox Animation in Tailwind CSS — Spring cubic-bezier"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "A squash-and-stretch pop on check: peer-checked:animate-tcb10-pop squeezes the box to 82% then overshoots to 112%, while the tick springs in on an…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncy Checkbox Animation in Tailwind CSS — Spring cubic-bezier
Source: https://codefronts.com/components/tailwind-css-checkboxes/bouncy-checkbox-animation-tailwind/

A squash-and-stretch pop on check: peer-checked:animate-tcb10-pop squeezes the box to 82% then overshoots to 112%, while the tick springs in on an ease-[cubic-bezier(.34,1.7,.5,1)] overshoot curve. Pressing now squashes the box before release.
## HTML
```html
<section class="tcb-10 w-full min-h-svh grid place-items-center bg-tcb10-bg px-5 py-14 font-tcb10-sans text-tcb10-ink selection:bg-tcb10-acc selection:text-white" aria-label="Bouncy pop checkboxes">
  <div class="w-full max-w-[25rem] rounded-2xl border border-tcb10-line bg-white px-4 py-2.5">
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only" checked><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb10-box bg-white text-white transition-[background-color,border-color,scale] duration-200 group-active:scale-90 peer-checked:animate-tcb10-pop peer-checked:border-tcb10-acc peer-checked:bg-tcb10-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb10-acc motion-reduce:animate-none motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-0 opacity-0 transition-[opacity,scale] duration-300 ease-[cubic-bezier(.34,1.7,.5,1)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:scale-100 motion-reduce:transition-opacity"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Add to favourites</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb10-box bg-white text-white transition-[background-color,border-color,scale] duration-200 group-active:scale-90 peer-checked:animate-tcb10-pop peer-checked:border-tcb10-acc peer-checked:bg-tcb10-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb10-acc motion-reduce:animate-none motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-0 opacity-0 transition-[opacity,scale] duration-300 ease-[cubic-bezier(.34,1.7,.5,1)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:scale-100 motion-reduce:transition-opacity"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Remind me later</span></label>
    <label class="group flex min-h-13 cursor-pointer items-center gap-3.5 px-2"><input type="checkbox" class="peer sr-only"><span aria-hidden="true" class="grid size-[26px] flex-none place-items-center rounded-lg border-2 border-tcb10-box bg-white text-white transition-[background-color,border-color,scale] duration-200 group-active:scale-90 peer-checked:animate-tcb10-pop peer-checked:border-tcb10-acc peer-checked:bg-tcb10-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tcb10-acc motion-reduce:animate-none motion-reduce:transition-none"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-[15px] scale-0 opacity-0 transition-[opacity,scale] duration-300 ease-[cubic-bezier(.34,1.7,.5,1)] group-has-checked:scale-100 group-has-checked:opacity-100 motion-reduce:scale-100 motion-reduce:transition-opacity"><path d="M20 6 9 17l-5-5"/></svg></span><span class="text-[15px]">Follow this thread</span></label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb10-bg: #fbf4f2;
  --color-tcb10-bg: oklch(0.97 0.01 35);
  --color-tcb10-ink: #3a2a27;
  --color-tcb10-ink: oklch(0.3 0.025 35);
  --color-tcb10-line: #f0dfda;
  --color-tcb10-line: oklch(0.92 0.02 35);
  --color-tcb10-box: #d49f93;
  --color-tcb10-box: oklch(0.74 0.07 35);
  --color-tcb10-acc: #df3d3d;
  --color-tcb10-acc: oklch(0.6 0.2 25);
  --font-tcb10-sans: 'Sora', system-ui, sans-serif;
  --animate-tcb10-pop: tcb10-pop 0.32s ease;

  @keyframes tcb10-pop {
    0% {
      scale: 1;
    }

    35% {
      scale: 0.82;
    }

    70% {
      scale: 1.12;
    }

    100% {
      scale: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-10 {
  width: 100%;
  min-height: 100svh;
}
```
