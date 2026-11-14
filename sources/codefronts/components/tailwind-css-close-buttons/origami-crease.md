---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/origami-crease/"
title: "Origami Fold Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "Each bar of the × is a strip of creased paper: perspective-[400px] on the button, transform-3d on the rig, and on hover each pseudo-element tips back along…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Origami Fold Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/origami-crease/

Each bar of the × is a strip of creased paper: perspective-[400px] on the button, transform-3d on the rig, and on hover each pseudo-element tips back along its own length with group-hover:before:rotate-x-[58deg], its two-tone gradient becoming the lit and shaded faces of the fold. Keyboard focus now folds it too.
## HTML
```html
<section class="tcb-11 w-full min-h-svh grid place-items-center bg-[linear-gradient(170deg,var(--color-tcb11-bg),var(--color-tcb11-bg2))] px-6 py-12 font-tcb11-sans" aria-label="Origami fold close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group relative size-18 cursor-pointer rounded-[1.25rem] bg-tcb11-card shadow-[0_16px_34px_-18px_var(--color-tcb11-shadow),inset_0_0_0_1px_var(--color-tcb11-edge)] perspective-[400px] focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb11-acc active:scale-95">
      <span aria-hidden="true" class="absolute inset-0 transform-3d before:absolute before:top-1/2 before:left-1/2 before:h-[9px] before:w-8 before:-translate-1/2 before:rotate-45 before:rounded-[2px] before:bg-[linear-gradient(180deg,var(--color-tcb11-pa)_50%,var(--color-tcb11-pb)_50%)] before:shadow-[0_6px_10px_-4px_var(--color-tcb11-shadow)] before:transition before:duration-380 before:ease-[cubic-bezier(.34,1.3,.5,1)] after:absolute after:top-1/2 after:left-1/2 after:h-[9px] after:w-8 after:-translate-1/2 after:-rotate-45 after:rounded-[2px] after:bg-[linear-gradient(180deg,var(--color-tcb11-pa)_50%,var(--color-tcb11-pb)_50%)] after:shadow-[0_6px_10px_-4px_var(--color-tcb11-shadow)] after:transition after:duration-380 after:ease-[cubic-bezier(.34,1.3,.5,1)] group-hover:before:rotate-x-[58deg] group-hover:before:bg-[linear-gradient(180deg,var(--color-tcb11-pa)_50%,var(--color-tcb11-pc)_50%)] group-hover:after:rotate-x-[58deg] group-hover:after:bg-[linear-gradient(180deg,var(--color-tcb11-pa)_50%,var(--color-tcb11-pc)_50%)] group-focus-visible:before:rotate-x-[58deg] group-focus-visible:after:rotate-x-[58deg] motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:group-hover:before:rotate-x-0 motion-reduce:group-hover:after:rotate-x-0"></span>
    </button>
    <p aria-hidden="true" class="rounded-full bg-white/60 px-3.5 py-2 font-tcb11-mono text-[11.5px] text-tcb11-mut ring-1 ring-black/8">perspective-[400px] · transform-3d · group-hover:before:rotate-x-[58deg]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb11-bg: #f2ebdc;
  --color-tcb11-bg: oklch(0.93 0.025 80);
  --color-tcb11-bg2: #e3d5bb;
  --color-tcb11-bg2: oklch(0.87 0.04 70);
  --color-tcb11-card: #fdfbf6;
  --color-tcb11-card: oklch(0.99 0.008 85);
  --color-tcb11-edge: #eadfca;
  --color-tcb11-edge: oklch(0.9 0.03 80);
  --color-tcb11-pa: #fbf5e6;
  --color-tcb11-pa: oklch(0.97 0.02 85);
  --color-tcb11-pb: #c4ae8b;
  --color-tcb11-pb: oklch(0.78 0.05 75);
  --color-tcb11-pc: #a38c6b;
  --color-tcb11-pc: oklch(0.68 0.06 70);
  --color-tcb11-acc: #a0732c;
  --color-tcb11-acc: oklch(0.58 0.12 70);
  --color-tcb11-mut: #6b5a3e;
  --color-tcb11-mut: oklch(0.47 0.05 70);
  --color-tcb11-shadow: #7e653f8c;
  --color-tcb11-shadow: oklch(0.5 0.08 70 / 0.55);
  --font-tcb11-sans: 'Geist', system-ui, sans-serif;
  --font-tcb11-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-11 {
  width: 100%;
  min-height: 100svh;
}
```
