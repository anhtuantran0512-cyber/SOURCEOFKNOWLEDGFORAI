---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-close-buttons/accessible-tailwind-close-button-focus-ring/"
title: "Accessible Tailwind Close Button with Focus Ring (WCAG)"
section: "components"
category: "tailwind-css-close-buttons"
category_name: "Tailwind CSS Close Buttons"
description: "A close button that passes WCAG 2.4.7 and 2.4.11 on any surface: focus-visible:outline-3 plus a two-stop focus-visible:shadow-[…] halo paints…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Close Button with Focus Ring (WCAG)
Source: https://codefronts.com/components/tailwind-css-close-buttons/accessible-tailwind-close-button-focus-ring/

A close button that passes WCAG 2.4.7 and 2.4.11 on any surface: focus-visible:outline-3 plus a two-stop focus-visible:shadow-[…] halo paints ink-on-white-on-ink, so the ring reads on both the light and dark panels. The border and × are currentColor, so one class list serves both themes, and forced-colors: hands the glyph to the system palette in Windows High Contrast.
## HTML
```html
<section class="tcb-02 w-full min-h-svh grid place-items-center bg-tcb02-bg px-6 py-12 font-tcb02-sans" aria-label="Accessible focus ring close button demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="@container w-full max-w-[30rem]">
      <div class="grid grid-cols-2 overflow-hidden rounded-[1.25rem] shadow-[0_24px_54px_-30px_var(--color-tcb02-shadow)] ring-1 ring-black/5 @max-[22rem]:grid-cols-1">
        <div class="flex flex-col items-center gap-4 bg-white px-5 py-10 text-tcb02-lmut">
          <span class="text-[11px] font-semibold tracking-[0.12em] uppercase">Light surface</span>
          <button type="button" aria-label="Close light panel" class="relative size-11 cursor-pointer rounded-xl border-[1.5px] border-current transition-colors duration-150 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-current after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-current hover:bg-current/10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tcb02-ring focus-visible:shadow-[0_0_0_6px_white,0_0_0_9px_var(--color-tcb02-ring)] active:scale-95 forced-colors:border-[ButtonText] forced-colors:before:bg-[ButtonText] forced-colors:after:bg-[ButtonText] motion-reduce:transition-none"></button>
          <span class="flex items-center gap-1.5 text-xs">Press <kbd class="rounded-md border border-current/30 px-1.5 py-0.5 font-tcb02-mono text-[11px]">Tab</kbd></span>
        </div>
        <div class="flex flex-col items-center gap-4 bg-tcb02-dark px-5 py-10 text-tcb02-dmut">
          <span class="text-[11px] font-semibold tracking-[0.12em] uppercase">Dark surface</span>
          <button type="button" aria-label="Close dark panel" class="relative size-11 cursor-pointer rounded-xl border-[1.5px] border-current transition-colors duration-150 before:absolute before:top-1/2 before:left-1/2 before:h-0.5 before:w-4 before:-translate-1/2 before:rotate-45 before:rounded-full before:bg-current after:absolute after:top-1/2 after:left-1/2 after:h-0.5 after:w-4 after:-translate-1/2 after:-rotate-45 after:rounded-full after:bg-current hover:bg-current/10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tcb02-ring focus-visible:shadow-[0_0_0_6px_white,0_0_0_9px_var(--color-tcb02-ring)] active:scale-95 forced-colors:border-[ButtonText] forced-colors:before:bg-[ButtonText] forced-colors:after:bg-[ButtonText] motion-reduce:transition-none"></button>
          <span class="flex items-center gap-1.5 text-xs">then <kbd class="rounded-md border border-current/30 px-1.5 py-0.5 font-tcb02-mono text-[11px]">Tab</kbd> again</span>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-white/70 px-3.5 py-2 font-tcb02-mono text-[11.5px] text-tcb02-lmut ring-1 ring-black/8">focus-visible:outline-3 · shadow halo · forced-colors:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb02-bg: #e6e9f0;
  --color-tcb02-bg: oklch(0.93 0.01 260);
  --color-tcb02-dark: #1c2233;
  --color-tcb02-dark: oklch(0.22 0.03 265);
  --color-tcb02-lmut: #4d5163;
  --color-tcb02-lmut: oklch(0.43 0.025 265);
  --color-tcb02-dmut: #c5cad8;
  --color-tcb02-dmut: oklch(0.84 0.02 265);
  --color-tcb02-ring: #3346c9;
  --color-tcb02-ring: oklch(0.45 0.19 265);
  --color-tcb02-shadow: #33384d80;
  --color-tcb02-shadow: oklch(0.35 0.05 265 / 0.5);
  --font-tcb02-sans: 'Geist', system-ui, sans-serif;
  --font-tcb02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-02 {
  width: 100%;
  min-height: 100svh;
}
```
