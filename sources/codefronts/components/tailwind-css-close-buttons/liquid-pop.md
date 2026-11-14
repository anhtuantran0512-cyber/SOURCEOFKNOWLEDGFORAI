---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/liquid-pop/"
title: "Liquid Goo Tailwind Close Button (SVG Filter)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Metaballs in utilities: a blurred, re-thresholded SVG filter applied with [filter:url(#tcb15-goo)] fuses a main blob and two droplets into one liquid shape."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Goo Tailwind Close Button (SVG Filter)
Source: https://codefronts.com/components/tailwind-css-close-buttons/liquid-pop/

Metaballs in utilities: a blurred, re-thresholded SVG filter applied with [filter:url(#tcb15-goo)] fuses a main blob and two droplets into one liquid shape. Hover (or keyboard focus) flings the droplets out on a back-and-overshoot curve with group-hover/stack:translate-x-[38px], and the surface tension visibly snaps as they separate.
## HTML
```html
<section class="tcb-15 w-full min-h-svh grid place-items-center bg-[linear-gradient(170deg,var(--color-tcb15-bg),var(--color-tcb15-bg2))] px-6 py-12 font-tcb15-sans" aria-label="Liquid goo close button demo">
  <svg class="absolute" width="0" height="0" aria-hidden="true"><defs><filter id="tcb15-goo"><feGaussianBlur in="SourceGraphic" stdDeviation="6" result="b"/><feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="g"/><feComposite in="SourceGraphic" in2="g" operator="atop"/></filter></defs></svg>
  <div class="grid w-full justify-items-center gap-7">
    <div class="group/stack relative grid size-[130px] place-items-center">
      <div aria-hidden="true" class="absolute inset-0 grid place-items-center [filter:url(#tcb15-goo)]">
        <span class="absolute size-16 rounded-full bg-tcb15-goo"></span>
        <span class="absolute size-5 rounded-full bg-tcb15-goo transition-[translate] duration-550 ease-[cubic-bezier(.68,-.55,.265,1.55)] group-hover/stack:translate-x-[38px] group-hover/stack:-translate-y-[27px] group-has-[:focus-visible]/stack:translate-x-[38px] group-has-[:focus-visible]/stack:-translate-y-[27px] motion-reduce:transition-none motion-reduce:translate-0!"></span>
        <span class="absolute size-3.5 rounded-full bg-tcb15-goo transition-[translate] delay-40 duration-550 ease-[cubic-bezier(.68,-.55,.265,1.55)] group-hover/stack:-translate-x-[34px] group-hover/stack:translate-y-[30px] group-has-[:focus-visible]/stack:-translate-x-[34px] group-has-[:focus-visible]/stack:translate-y-[30px] motion-reduce:transition-none motion-reduce:translate-0!"></span>
      </div>
      <button type="button" aria-label="Close" class="relative grid size-16 cursor-pointer place-items-center rounded-full transition-[scale] duration-300 ease-[cubic-bezier(.34,1.56,.64,1)] hover:scale-106 focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tcb15-ring active:scale-90 motion-reduce:transition-none">
        <span aria-hidden="true" class="relative size-5.5 before:absolute before:top-1/2 before:left-1/2 before:h-[3px] before:w-5.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-[3px] after:w-5.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white"></span>
      </button>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb15-mono text-[11.5px] text-tcb15-mut ring-1 ring-black/8">[filter:url(#tcb15-goo)] · group-hover/stack:translate-x-[38px]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb15-bg: #fbf1f5;
  --color-tcb15-bg: oklch(0.96 0.012 350);
  --color-tcb15-bg2: #f3dde6;
  --color-tcb15-bg2: oklch(0.92 0.03 340);
  --color-tcb15-goo: #dd3d87;
  --color-tcb15-goo: oklch(0.6 0.21 350);
  --color-tcb15-ring: #a8155b;
  --color-tcb15-ring: oklch(0.48 0.19 355);
  --color-tcb15-mut: #7a4c60;
  --color-tcb15-mut: oklch(0.47 0.07 350);
  --font-tcb15-sans: 'Geist', system-ui, sans-serif;
  --font-tcb15-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-15 {
  width: 100%;
  min-height: 100svh;
}
```
