---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/fold-away/"
title: "3D Fold Away Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The × splits along its horizon and both halves hinge away from the viewer like a split-flap display: two copies of one glyph, cropped with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Fold Away Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/fold-away/

The × splits along its horizon and both halves hinge away from the viewer like a split-flap display: two copies of one glyph, cropped with [clip-path:inset(0_0_50%_0)] and its mirror, tip with group-hover:rotate-x-[78deg] and -rotate-x-[78deg] while brightness-72 darkens them into shadow. A 40ms stagger makes the fold feel physical.
## HTML
```html
<section class="tcb-23 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb23-bg),var(--color-tcb23-bg2))] px-6 py-12 font-tcb23-sans" aria-label="3D fold away close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative size-19 cursor-pointer rounded-[18px] border-[1.5px] border-tcb23-line bg-white shadow-[0_18px_40px_-24px_var(--color-tcb23-shadow)] transition-shadow duration-300 perspective-[500px] hover:shadow-[0_10px_22px_-16px_var(--color-tcb23-shadow)] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb23-acc active:scale-95">
      <span aria-hidden="true" class="absolute inset-0 grid place-items-center transition duration-450 ease-[cubic-bezier(.4,0,.2,1)] [clip-path:inset(0_0_50%_0)] group-hover:rotate-x-[78deg] group-hover:brightness-72 group-focus-visible:rotate-x-[78deg] group-focus-visible:brightness-72 motion-reduce:transition-none motion-reduce:transform-none! motion-reduce:filter-none!">
        <i class="relative block size-6.5 before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-6.5 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-tcb23-ink after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-6.5 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-tcb23-ink"></i>
      </span>
      <span aria-hidden="true" class="absolute inset-0 grid place-items-center transition delay-40 duration-450 ease-[cubic-bezier(.4,0,.2,1)] [clip-path:inset(50%_0_0_0)] group-hover:-rotate-x-[78deg] group-hover:brightness-82 group-focus-visible:-rotate-x-[78deg] group-focus-visible:brightness-82 motion-reduce:transition-none motion-reduce:transform-none! motion-reduce:filter-none!">
        <i class="relative block size-6.5 before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-6.5 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-tcb23-ink after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-6.5 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-tcb23-ink"></i>
      </span>
    </button>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb23-mono text-[11.5px] text-tcb23-mut ring-1 ring-black/8">[clip-path:inset(0_0_50%_0)] · group-hover:rotate-x-[78deg]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb23-bg: #eef2f8;
  --color-tcb23-bg: oklch(0.95 0.012 240);
  --color-tcb23-bg2: #dde3ee;
  --color-tcb23-bg2: oklch(0.9 0.02 245);
  --color-tcb23-ink: #2d3748;
  --color-tcb23-ink: oklch(0.3 0.03 250);
  --color-tcb23-mut: #4f5a6d;
  --color-tcb23-mut: oklch(0.45 0.035 250);
  --color-tcb23-line: #d2d9e4;
  --color-tcb23-line: oklch(0.87 0.02 245);
  --color-tcb23-acc: #3d6ad1;
  --color-tcb23-acc: oklch(0.55 0.15 262);
  --color-tcb23-shadow: #3f4d6799;
  --color-tcb23-shadow: oklch(0.4 0.06 245 / 0.6);
  --font-tcb23-sans: 'Geist', system-ui, sans-serif;
  --font-tcb23-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-23 {
  width: 100%;
  min-height: 100svh;
}
```
