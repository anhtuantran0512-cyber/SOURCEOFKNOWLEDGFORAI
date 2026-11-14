---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/neo-brutalist-tailwind-tabs-press-effect/"
title: "Neo-Brutalist Tailwind Tabs with Press Effect"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Heavy uppercase keys with hard 4px offset shadows."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist Tailwind Tabs with Press Effect
Source: https://codefronts.com/navigation/tailwind-css-tabs/neo-brutalist-tailwind-tabs-press-effect/

Heavy uppercase keys with hard 4px offset shadows. The checked tab presses flush: it translates exactly as far as its shadow shrinks, so the shadow's far edge never moves and the key appears to sink into the page. The panel is a brutalist card of its own.
## HTML
```html
<section class="ttb-03 group/tabs grid min-h-svh w-full place-items-center bg-ttb03-bg bg-[radial-gradient(var(--color-ttb03-dot)_1px,transparent_1px)] bg-size-[18px_18px] px-6 py-14 font-ttb03-sans text-ttb03-ink" aria-label="Neo-brutalist press tabs demo">
  <div class="grid w-full max-w-lg justify-items-center gap-8">
    <div role="radiogroup" aria-label="Workflow stage" class="flex w-full gap-4">
      <label class="flex min-h-12 flex-1 cursor-pointer items-center justify-center border-3 border-ttb03-ink bg-white text-[13px] font-bold tracking-[0.12em] uppercase shadow-[4px_4px_0_var(--color-ttb03-ink)] transition-[translate,box-shadow,background-color,color] duration-150 ease-out hover:bg-ttb03-soft active:translate-x-0.5 active:translate-y-0.5 active:shadow-[2px_2px_0_var(--color-ttb03-ink)] has-checked:translate-x-1 has-checked:translate-y-1 has-checked:bg-ttb03-ink has-checked:text-ttb03-bg has-checked:shadow-[0_0_0_var(--color-ttb03-ink)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb03-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb03" id="ttb03-r1" checked>Build</label>
      <label class="flex min-h-12 flex-1 cursor-pointer items-center justify-center border-3 border-ttb03-ink bg-white text-[13px] font-bold tracking-[0.12em] uppercase shadow-[4px_4px_0_var(--color-ttb03-ink)] transition-[translate,box-shadow,background-color,color] duration-150 ease-out hover:bg-ttb03-soft active:translate-x-0.5 active:translate-y-0.5 active:shadow-[2px_2px_0_var(--color-ttb03-ink)] has-checked:translate-x-1 has-checked:translate-y-1 has-checked:bg-ttb03-ink has-checked:text-ttb03-bg has-checked:shadow-[0_0_0_var(--color-ttb03-ink)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb03-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb03" id="ttb03-r2">Ship</label>
      <label class="flex min-h-12 flex-1 cursor-pointer items-center justify-center border-3 border-ttb03-ink bg-white text-[13px] font-bold tracking-[0.12em] uppercase shadow-[4px_4px_0_var(--color-ttb03-ink)] transition-[translate,box-shadow,background-color,color] duration-150 ease-out hover:bg-ttb03-soft active:translate-x-0.5 active:translate-y-0.5 active:shadow-[2px_2px_0_var(--color-ttb03-ink)] has-checked:translate-x-1 has-checked:translate-y-1 has-checked:bg-ttb03-ink has-checked:text-ttb03-bg has-checked:shadow-[0_0_0_var(--color-ttb03-ink)] has-focus-visible:outline-3 has-focus-visible:outline-offset-4 has-focus-visible:outline-dashed has-focus-visible:outline-ttb03-ink motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb03" id="ttb03-r3">Iterate</label>
    </div>
    <div class="w-full border-3 border-ttb03-ink bg-white p-5 shadow-[6px_6px_0_var(--color-ttb03-ink)]">
      <div class="hidden group-has-[#ttb03-r1:checked]/tabs:block"><p class="font-ttb03-mono text-[11px] font-bold tracking-[0.1em] uppercase">Step 01 / 03</p><p class="mt-2 text-lg leading-snug font-bold">Build — assemble the parts, wire the data, make it run.</p></div>
      <div class="hidden group-has-[#ttb03-r2:checked]/tabs:block"><p class="font-ttb03-mono text-[11px] font-bold tracking-[0.1em] uppercase">Step 02 / 03</p><p class="mt-2 text-lg leading-snug font-bold">Ship — push it to production while it's still a little rough.</p></div>
      <div class="hidden group-has-[#ttb03-r3:checked]/tabs:block"><p class="font-ttb03-mono text-[11px] font-bold tracking-[0.1em] uppercase">Step 03 / 03</p><p class="mt-2 text-lg leading-snug font-bold">Iterate — measure what people actually do, then refine.</p></div>
    </div>
    <p aria-hidden="true" class="border-2 border-ttb03-ink bg-white px-3.5 py-2 font-ttb03-mono text-[11.5px] font-bold">shadow-[4px_4px_0] · has-checked:translate-1 · active: half-press</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb03-bg: #fdeeb8;
  --color-ttb03-bg: oklch(0.948 0.071 94.4);
  --color-ttb03-dot: #e9d48a;
  --color-ttb03-dot: oklch(0.871 0.096 94.1);
  --color-ttb03-soft: #fff6d6;
  --color-ttb03-soft: oklch(0.972 0.043 94.1);
  --color-ttb03-ink: #0b0b0b;
  --color-ttb03-ink: oklch(0.150 0 0);
  --font-ttb03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-ttb03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-03 {
  width: 100%;
  min-height: 100svh;
}
```
