---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/ribbon-tag/"
title: "Corner Ribbon Tailwind Close Button"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "The dismiss control is the ribbon: a 150px band rotated with rotate-45, parked off the card's corner with -end-[38px] and clipped by overflow-hidden, with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Ribbon Tailwind Close Button
Source: https://codefronts.com/components/tailwind-css-close-buttons/ribbon-tag/

The dismiss control is the ribbon: a 150px band rotated with rotate-45, parked off the card's corner with -end-[38px] and clipped by overflow-hidden, with a counter-rotated -rotate-45 × that stays upright. Because v4's translate is applied before rotate, hover:-translate-y-[3px] lifts the band straight up without restating the angle.
## HTML
```html
<section class="tcb-22 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tcb22-bg),var(--color-tcb22-bg2))] px-6 py-12 font-tcb22-sans text-tcb22-ink" aria-label="Corner ribbon close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="relative w-full max-w-[22rem] overflow-hidden rounded-2xl border border-tcb22-line bg-white px-6 pt-7 pb-6 shadow-[0_20px_46px_-26px_var(--color-tcb22-shadow)]">
      <button type="button" aria-label="Dismiss offer" class="absolute top-[18px] -end-[38px] z-10 grid h-[34px] w-[150px] rotate-45 cursor-pointer place-items-center bg-linear-to-b from-tcb22-ribbon to-tcb22-ribbon2 shadow-[0_4px_10px_-4px_var(--color-tcb22-shadow)] transition-[translate,scale] duration-200 hover:-translate-y-[3px] focus-visible:outline-[2.5px] focus-visible:outline-offset-[-5px] focus-visible:outline-white active:translate-y-0 active:scale-97 motion-reduce:transition-none">
        <span aria-hidden="true" class="relative size-3.5 -rotate-45 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-3.5 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-white after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-3.5 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-white"></span>
      </button>
      <span class="inline-flex rounded-full bg-tcb22-soft px-2.5 py-1 text-[11px] font-semibold tracking-[0.06em] text-tcb22-deep uppercase">Ends Sunday</span>
      <h3 class="mt-3 text-lg font-semibold tracking-[-0.01em]">Spring offer</h3>
      <p class="mt-1.5 max-w-[24ch] text-sm/[1.55] text-tcb22-mut">3 months free on annual plans.</p>
      <a href="#" class="mt-5 inline-flex min-h-11 items-center rounded-xl bg-tcb22-ink px-4.5 text-sm font-semibold text-white transition hover:brightness-125 focus-visible:outline-[2.5px] focus-visible:outline-offset-2 focus-visible:outline-tcb22-deep">Claim offer</a>
    </article>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb22-mono text-[11.5px] text-tcb22-mut ring-1 ring-black/8">rotate-45 band · -rotate-45 glyph · hover:-translate-y-[3px]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb22-bg: #fbf3f2;
  --color-tcb22-bg: oklch(0.96 0.01 25);
  --color-tcb22-bg2: #f4e5e2;
  --color-tcb22-bg2: oklch(0.93 0.02 30);
  --color-tcb22-ink: #3b2a28;
  --color-tcb22-ink: oklch(0.3 0.03 25);
  --color-tcb22-mut: #6c5552;
  --color-tcb22-mut: oklch(0.47 0.03 25);
  --color-tcb22-line: #efe0dd;
  --color-tcb22-line: oklch(0.91 0.015 25);
  --color-tcb22-soft: #fbe3de;
  --color-tcb22-soft: oklch(0.93 0.04 30);
  --color-tcb22-deep: #a3291e;
  --color-tcb22-deep: oklch(0.47 0.16 28);
  --color-tcb22-ribbon: #e85d4f;
  --color-tcb22-ribbon: oklch(0.66 0.17 28);
  --color-tcb22-ribbon2: #c9362c;
  --color-tcb22-ribbon2: oklch(0.56 0.19 27);
  --color-tcb22-shadow: #8b3a3080;
  --color-tcb22-shadow: oklch(0.45 0.1 25 / 0.5);
  --font-tcb22-sans: 'Geist', system-ui, sans-serif;
  --font-tcb22-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-22 {
  width: 100%;
  min-height: 100svh;
}
```
