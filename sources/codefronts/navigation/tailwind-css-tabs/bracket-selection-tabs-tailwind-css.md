---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/bracket-selection-tabs-tailwind-css/"
title: "Bracket Selection Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "A pair of crimson brackets frames the active word and slides between choices."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bracket Selection Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/bracket-selection-tabs-tailwind-css/

A pair of crimson brackets frames the active word and slides between choices. The original positioned two spans from measured offsets; the port puts both brackets inside one span the width of a column and moves that span — the brackets stay pinned to the cell edges and travel together.
## HTML
```html
<section class="ttb-21 group/tabs grid min-h-svh w-full place-items-center bg-ttb21-bg px-5 py-14 font-ttb21-serif text-ttb21-paper" aria-label="Bracket selection tabs demo">
  <div class="grid w-full max-w-md justify-items-center gap-8">
    <div role="radiogroup" aria-label="Marker" class="relative grid w-full grid-cols-3 [--i:0] has-[#ttb21-r2:checked]:[--i:1] has-[#ttb21-r3:checked]:[--i:2]">
      <label class="flex min-h-14 cursor-pointer items-center justify-center text-[26px] text-ttb21-mut transition-colors hover:text-ttb21-paper has-checked:text-ttb21-paper has-focus-visible:outline-1 has-focus-visible:-outline-offset-8 has-focus-visible:outline-dashed has-focus-visible:outline-ttb21-paper"><input class="sr-only" type="radio" name="ttb21" id="ttb21-r1" checked>One</label>
      <label class="flex min-h-14 cursor-pointer items-center justify-center text-[26px] text-ttb21-mut transition-colors hover:text-ttb21-paper has-checked:text-ttb21-paper has-focus-visible:outline-1 has-focus-visible:-outline-offset-8 has-focus-visible:outline-dashed has-focus-visible:outline-ttb21-paper"><input class="sr-only" type="radio" name="ttb21" id="ttb21-r2">Two</label>
      <label class="flex min-h-14 cursor-pointer items-center justify-center text-[26px] text-ttb21-mut transition-colors hover:text-ttb21-paper has-checked:text-ttb21-paper has-focus-visible:outline-1 has-focus-visible:-outline-offset-8 has-focus-visible:outline-dashed has-focus-visible:outline-ttb21-paper"><input class="sr-only" type="radio" name="ttb21" id="ttb21-r3">Three</label>
      <span aria-hidden="true" class="pointer-events-none absolute inset-y-0 left-0 flex w-1/3 translate-x-[calc(var(--i)*100%)] items-center justify-between px-1 text-[44px] leading-none font-light text-ttb21-crimson transition-transform duration-500 ease-[cubic-bezier(0.65,0,0.35,1)] motion-reduce:transition-none"><span>[</span><span>]</span></span>
    </div>
    <div class="min-h-6 text-center text-[17px] text-ttb21-soft italic">
      <p class="hidden transition-opacity duration-300 group-has-[#ttb21-r1:checked]/tabs:block starting:opacity-0">The first marker — a beginning.</p>
      <p class="hidden transition-opacity duration-300 group-has-[#ttb21-r2:checked]/tabs:block starting:opacity-0">The second marker — a turn.</p>
      <p class="hidden transition-opacity duration-300 group-has-[#ttb21-r3:checked]/tabs:block starting:opacity-0">The third marker — a close.</p>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/10 px-3.5 py-2 font-ttb21-mono text-[11.5px] text-ttb21-mut">one frame w-1/3 · justify-between brackets · translate by --i</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb21-bg: #25222e;
  --color-ttb21-bg: oklch(0.261 0.023 296.3);
  --color-ttb21-paper: #ece6d4;
  --color-ttb21-paper: oklch(0.925 0.025 91.6);
  --color-ttb21-soft: #cfc9b8;
  --color-ttb21-soft: oklch(0.836 0.024 90.8);
  --color-ttb21-mut: #a9a395;
  --color-ttb21-mut: oklch(0.717 0.021 87.5);
  --color-ttb21-crimson: #f04a5f;
  --color-ttb21-crimson: oklch(0.649 0.201 17.8);
  --font-ttb21-serif: 'Instrument Serif', Georgia, serif;
  --font-ttb21-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-21 {
  width: 100%;
  min-height: 100svh;
}
```
