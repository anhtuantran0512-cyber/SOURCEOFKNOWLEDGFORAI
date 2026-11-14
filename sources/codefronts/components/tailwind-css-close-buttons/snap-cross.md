---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/snap-cross/"
title: "Spring Snap Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A spring with no physics engine: cubic-bezier(.68,-.55,.265,1.55) — declared once as --ease-tcb20-spring — winds back below zero, overshoots past one, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spring Snap Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/snap-cross/

A spring with no physics engine: cubic-bezier(.68,-.55,.265,1.55) — declared once as --ease-tcb20-spring — winds back below zero, overshoots past one, and settles, so a plain group-hover:rotate-90 reads as a snap. The drafting-grid face is four stacked backgrounds in a single arbitrary property; press squashes the whole tile on the same spring.
## HTML
```html
<section class="tcb-20 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb20-bg),var(--color-tcb20-bg2))] px-6 py-12 font-tcb20-sans" aria-label="Spring snap close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group grid size-20 cursor-pointer place-items-center rounded-[22px] border-2 border-tcb20-grid shadow-[0_16px_36px_-22px_var(--color-tcb20-shadow)] transition-[scale,border-color] duration-500 ease-tcb20-spring [background:radial-gradient(circle,var(--color-tcb20-dot)_1px,transparent_1.5px)_0_0/10px_10px,linear-gradient(0deg,transparent_calc(50%_-_.5px),var(--color-tcb20-grid)_calc(50%_-_.5px)_calc(50%_+_.5px),transparent_calc(50%_+_.5px)),linear-gradient(90deg,transparent_calc(50%_-_.5px),var(--color-tcb20-grid)_calc(50%_-_.5px)_calc(50%_+_.5px),transparent_calc(50%_+_.5px)),#fff] hover:border-tcb20-acc focus-visible:border-tcb20-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb20-acc active:scale-90 motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-6.5 transition-[rotate] duration-500 ease-tcb20-spring before:absolute before:top-1/2 before:left-1/2 before:h-[3.5px] before:w-6.5 before:-translate-1/2 before:rotate-45 before:rounded-[3px] before:bg-tcb20-acc after:absolute after:top-1/2 after:left-1/2 after:h-[3.5px] after:w-6.5 after:-translate-1/2 after:-rotate-45 after:rounded-[3px] after:bg-tcb20-acc group-hover:rotate-90 group-focus-visible:rotate-90 motion-reduce:transition-none"></span>
    </button>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb20-mono text-[11.5px] text-tcb20-mut ring-1 ring-black/8">ease-tcb20-spring · group-hover:rotate-90 · active:scale-90</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb20-bg: #fbf2ee;
  --color-tcb20-bg: oklch(0.96 0.01 35);
  --color-tcb20-bg2: #f3e3dc;
  --color-tcb20-bg2: oklch(0.92 0.02 40);
  --color-tcb20-grid: #e8d3ca;
  --color-tcb20-grid: oklch(0.87 0.03 35);
  --color-tcb20-dot: #e3cbc099;
  --color-tcb20-dot: oklch(0.85 0.02 35 / 0.6);
  --color-tcb20-acc: #d9532a;
  --color-tcb20-acc: oklch(0.62 0.18 38);
  --color-tcb20-mut: #7a5345;
  --color-tcb20-mut: oklch(0.47 0.06 35);
  --color-tcb20-shadow: #9b573b99;
  --color-tcb20-shadow: oklch(0.5 0.1 35 / 0.6);
  --font-tcb20-sans: 'Geist', system-ui, sans-serif;
  --font-tcb20-mono: 'Geist Mono', ui-monospace, monospace;
  --ease-tcb20-spring: cubic-bezier(0.68, -.55, 0.265, 1.55);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-20 {
  width: 100%;
  min-height: 100svh;
}
```
