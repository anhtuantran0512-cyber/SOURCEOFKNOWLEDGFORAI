---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/rotate-out/"
title: "Rotate on Hover Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The most-searched close-button animation, done cleanly: a 180° group-hover:rotate-180 on the glyph with an ease-out-expo curve, the ring and bars shifting to…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate on Hover Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/rotate-out/

The most-searched close-button animation, done cleanly: a 180° group-hover:rotate-180 on the glyph with an ease-out-expo curve, the ring and bars shifting to the accent. grid place-items-center kills the sub-pixel wobble that plagues spinning icons, and v4's hover: is already gated behind @media (hover:hover) — the original's hand-written media query simply disappears.
## HTML
```html
<section class="tcb-13 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb13-bg),var(--color-tcb13-bg2))] px-6 py-12 font-tcb13-sans" aria-label="Rotate on hover close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <button type="button" aria-label="Close" class="group grid size-15 cursor-pointer place-items-center rounded-full border-2 border-tcb13-ink/30 bg-white shadow-[0_12px_28px_-16px_var(--color-tcb13-shadow)] transition duration-250 hover:border-tcb13-acc focus-visible:border-tcb13-acc focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-tcb13-acc active:scale-92 motion-reduce:transition-none">
      <span aria-hidden="true" class="relative size-5.5 transition-transform duration-450 ease-[cubic-bezier(.22,1,.36,1)] before:absolute before:top-1/2 before:left-1/2 before:h-[2.5px] before:w-5.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-tcb13-ink before:transition-colors before:duration-250 after:absolute after:top-1/2 after:left-1/2 after:h-[2.5px] after:w-5.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-tcb13-ink after:transition-colors after:duration-250 group-hover:rotate-180 group-hover:before:bg-tcb13-acc group-hover:after:bg-tcb13-acc group-focus-visible:rotate-180 motion-reduce:transition-none"></span>
    </button>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb13-mono text-[11.5px] text-tcb13-mut ring-1 ring-black/8">group-hover:rotate-180 · ease-[cubic-bezier(.22,1,.36,1)]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb13-bg: #f5f6fa;
  --color-tcb13-bg: oklch(0.97 0.006 265);
  --color-tcb13-bg2: #e8e9f2;
  --color-tcb13-bg2: oklch(0.93 0.014 265);
  --color-tcb13-ink: #3a3e52;
  --color-tcb13-ink: oklch(0.35 0.03 265);
  --color-tcb13-mut: #555a70;
  --color-tcb13-mut: oklch(0.46 0.03 265);
  --color-tcb13-acc: #4150d8;
  --color-tcb13-acc: oklch(0.52 0.19 268);
  --color-tcb13-shadow: #4a4f7080;
  --color-tcb13-shadow: oklch(0.4 0.06 265 / 0.5);
  --font-tcb13-sans: 'Geist', system-ui, sans-serif;
  --font-tcb13-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-13 {
  width: 100%;
  min-height: 100svh;
}
```
