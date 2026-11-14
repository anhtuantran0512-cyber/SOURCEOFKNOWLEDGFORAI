---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/trash-compactor/"
title: "Trash Compactor Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A little machine: on hover two steel plates slam inward with group-hover:translate-y-[15px] while the × is crushed flat by scale-y-22 and bows out with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Trash Compactor Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/trash-compactor/

A little machine: on hover two steel plates slam inward with group-hover:translate-y-[15px] while the × is crushed flat by scale-y-22 and bows out with scale-x-125. One anticipation curve, declared once in @theme as --ease-tcb17-crush, drives every part, so the plates and the glyph move as a single mechanism.
## HTML
```html
<section class="tcb-17 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb17-bg),var(--color-tcb17-bg2))] px-6 py-12 font-tcb17-sans" aria-label="Trash compactor close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative grid size-19 cursor-pointer place-items-center overflow-hidden rounded-[14px] border border-tcb17-edge/60 bg-linear-to-b from-tcb17-h1 to-tcb17-h2 shadow-[0_16px_36px_-18px_rgb(0_0_0/0.85),inset_0_1px_0_var(--color-tcb17-hl)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb17-ring active:scale-95">
      <span aria-hidden="true" class="absolute inset-x-2.5 top-2 h-2 rounded-[3px] bg-linear-to-b from-tcb17-steel to-tcb17-steel2 shadow-[0_2px_4px_rgb(0_0_0/0.5)] transition-[translate] duration-340 ease-tcb17-crush group-hover:translate-y-[15px] group-focus-visible:translate-y-[15px] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="relative size-6 transition-[scale] duration-340 ease-tcb17-crush before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-6 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-tcb17-x after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-6 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-tcb17-x group-hover:scale-x-125 group-hover:scale-y-22 group-focus-visible:scale-x-125 group-focus-visible:scale-y-22 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-x-2.5 bottom-2 h-2 rounded-[3px] bg-linear-to-b from-tcb17-steel to-tcb17-steel2 shadow-[0_2px_4px_rgb(0_0_0/0.5)] transition-[translate] duration-340 ease-tcb17-crush group-hover:-translate-y-[15px] group-focus-visible:-translate-y-[15px] motion-reduce:transition-none"></span>
    </button>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tcb17-mono text-[11.5px] text-tcb17-mut ring-1 ring-white/12">ease-tcb17-crush · group-hover:scale-y-22 · translate-y-[15px]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb17-bg: #2d3139;
  --color-tcb17-bg: oklch(0.32 0.02 255);
  --color-tcb17-bg2: #1c1f25;
  --color-tcb17-bg2: oklch(0.22 0.015 250);
  --color-tcb17-h1: #4a4f59;
  --color-tcb17-h1: oklch(0.4 0.02 250);
  --color-tcb17-h2: #33373f;
  --color-tcb17-h2: oklch(0.3 0.02 250);
  --color-tcb17-hl: #6b717c80;
  --color-tcb17-hl: oklch(0.55 0.02 250 / 0.5);
  --color-tcb17-edge: #666b75;
  --color-tcb17-edge: oklch(0.5 0.02 250);
  --color-tcb17-steel: #b4b9c2;
  --color-tcb17-steel: oklch(0.75 0.02 250);
  --color-tcb17-steel2: #797e88;
  --color-tcb17-steel2: oklch(0.55 0.02 250);
  --color-tcb17-x: #e5e8ec;
  --color-tcb17-x: oklch(0.92 0.01 250);
  --color-tcb17-ring: #a7c3ec;
  --color-tcb17-ring: oklch(0.8 0.1 250);
  --color-tcb17-mut: #b3b8c2;
  --color-tcb17-mut: oklch(0.77 0.02 250);
  --font-tcb17-sans: 'Geist', system-ui, sans-serif;
  --font-tcb17-mono: 'Geist Mono', ui-monospace, monospace;
  --ease-tcb17-crush: cubic-bezier(0.6, -.28, 0.55, 1.32);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-17 {
  width: 100%;
  min-height: 100svh;
}
```
