---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/brutalist-stamp/"
title: "Brutalist Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Neo-brutalism with honest physics: a thick black border and a zero-blur shadow-[4px_4px_0_#000]; hover lifts the button with hover:-translate-1 while the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/brutalist-stamp/

Neo-brutalism with honest physics: a thick black border and a zero-blur shadow-[4px_4px_0_#000]; hover lifts the button with hover:-translate-1 while the shadow grows to 8px, and press slams it down with active:translate-1 active:shadow-none — transform and shadow move in opposition, so the "floor" never moves. Set in Space Grotesk and Space Mono.
## HTML
```html
<section class="tcb-27 w-full min-h-svh grid place-items-center bg-tcb27-bg px-6 py-12 font-tcb27-sans text-black" aria-label="Brutalist close button demo">
  <div class="grid w-full justify-items-center gap-8">
    <div class="w-full max-w-[22rem] border-3 border-black bg-white p-5 shadow-[8px_8px_0_#000]">
      <div class="mb-4 flex items-start justify-between gap-4">
        <span class="bg-black px-2 py-1.5 font-tcb27-mono text-xs leading-tight font-bold tracking-[0.08em] text-tcb27-paper">NOTICE №4</span>
        <button type="button" aria-label="Close notice" class="grid size-11 flex-none cursor-pointer place-items-center border-3 border-black bg-tcb27-paper shadow-[4px_4px_0_#000] transition-[translate,box-shadow] duration-100 ease-out hover:-translate-1 hover:shadow-[8px_8px_0_#000] focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-black active:translate-1 active:shadow-none motion-reduce:transition-none">
          <span aria-hidden="true" class="relative size-4.5 before:absolute before:top-1/2 before:left-1/2 before:h-1 before:w-5 before:-translate-1/2 before:rotate-45 before:bg-black after:absolute after:top-1/2 after:left-1/2 after:h-1 after:w-5 after:-translate-1/2 after:-rotate-45 after:bg-black"></span>
        </button>
      </div>
      <p class="text-[17px] leading-snug font-semibold">Your free trial ends in 3 days.</p>
      <a href="#" class="mt-5 inline-flex min-h-11 items-center border-3 border-black bg-black px-4 font-tcb27-mono text-sm font-bold text-tcb27-paper shadow-[4px_4px_0_var(--color-tcb27-paper),4px_4px_0_3px_#000] transition-[translate] duration-100 hover:-translate-0.5 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-black active:translate-0.5">UPGRADE →</a>
    </div>
    <p aria-hidden="true" class="border-2 border-black bg-white px-3.5 py-2 font-tcb27-mono text-[11.5px]">hover:-translate-1 · active:translate-1 active:shadow-none</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb27-bg: #efede6;
  --color-tcb27-bg: oklch(0.94 0.008 90);
  --color-tcb27-paper: #f2e33a;
  --color-tcb27-paper: oklch(0.9 0.18 100);
  --font-tcb27-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcb27-mono: 'Space Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-27 {
  width: 100%;
  min-height: 100svh;
}
```
