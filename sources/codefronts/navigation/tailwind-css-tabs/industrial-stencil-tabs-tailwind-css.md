---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-tabs/industrial-stencil-tabs-tailwind-css/"
title: "Industrial Stencil Tabs in Tailwind CSS"
section: "navigation"
category: "tailwind-css-tabs"
category_name: "Tailwind CSS Tabs"
description: "Two-colour print: safety-yellow plates stamped on matte ink."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Industrial Stencil Tabs in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-tabs/industrial-stencil-tabs-tailwind-css/

Two-colour print: safety-yellow plates stamped on matte ink. The active plate lifts 2px and gains a hazard-stripe header, and the labels are set in Big Shoulders Stencil — a real stencil face with bridges in its counters — instead of tracked monospace pretending to be one.
## HTML
```html
<section class="ttb-20 group/tabs grid min-h-svh w-full place-items-center bg-ttb20-ink px-5 py-14 font-ttb20-stencil text-ttb20-yellow" aria-label="Industrial stencil tabs demo">
  <div class="grid w-full max-w-xl justify-items-center gap-7">
    <div class="w-full">
      <div role="radiogroup" aria-label="Mode" class="flex gap-2">
        <label class="relative flex min-h-14 flex-1 cursor-pointer items-center justify-center overflow-hidden text-[24px] font-extrabold tracking-[0.14em] text-ttb20-yellow/60 uppercase ring-1 ring-ttb20-yellow/20 transition-[color,background-color,translate,box-shadow] duration-250 before:absolute before:inset-x-0 before:top-0 before:h-1.5 before:bg-[repeating-linear-gradient(-45deg,var(--color-ttb20-ink)_0_6px,transparent_6px_12px)] before:opacity-0 before:transition-opacity hover:text-ttb20-yellow has-checked:-translate-y-0.5 has-checked:bg-ttb20-yellow has-checked:text-ttb20-ink has-checked:shadow-[0_4px_0_-1px_rgb(0_0_0/0.6)] has-checked:ring-0 has-checked:before:opacity-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb20-yellow motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb20" id="ttb20-r1">Read</label>
        <label class="relative flex min-h-14 flex-1 cursor-pointer items-center justify-center overflow-hidden text-[24px] font-extrabold tracking-[0.14em] text-ttb20-yellow/60 uppercase ring-1 ring-ttb20-yellow/20 transition-[color,background-color,translate,box-shadow] duration-250 before:absolute before:inset-x-0 before:top-0 before:h-1.5 before:bg-[repeating-linear-gradient(-45deg,var(--color-ttb20-ink)_0_6px,transparent_6px_12px)] before:opacity-0 before:transition-opacity hover:text-ttb20-yellow has-checked:-translate-y-0.5 has-checked:bg-ttb20-yellow has-checked:text-ttb20-ink has-checked:shadow-[0_4px_0_-1px_rgb(0_0_0/0.6)] has-checked:ring-0 has-checked:before:opacity-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb20-yellow motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb20" id="ttb20-r2" checked>Write</label>
        <label class="relative flex min-h-14 flex-1 cursor-pointer items-center justify-center overflow-hidden text-[24px] font-extrabold tracking-[0.14em] text-ttb20-yellow/60 uppercase ring-1 ring-ttb20-yellow/20 transition-[color,background-color,translate,box-shadow] duration-250 before:absolute before:inset-x-0 before:top-0 before:h-1.5 before:bg-[repeating-linear-gradient(-45deg,var(--color-ttb20-ink)_0_6px,transparent_6px_12px)] before:opacity-0 before:transition-opacity hover:text-ttb20-yellow has-checked:-translate-y-0.5 has-checked:bg-ttb20-yellow has-checked:text-ttb20-ink has-checked:shadow-[0_4px_0_-1px_rgb(0_0_0/0.6)] has-checked:ring-0 has-checked:before:opacity-100 has-focus-visible:outline-2 has-focus-visible:outline-offset-3 has-focus-visible:outline-dashed has-focus-visible:outline-ttb20-yellow motion-reduce:transition-none"><input class="sr-only" type="radio" name="ttb20" id="ttb20-r3">Ship</label>
      </div>
      <div class="pt-5 font-ttb20-serif text-[16px] text-ttb20-paper italic">
        <p class="hidden group-has-[#ttb20-r1:checked]/tabs:block">Drafts, archives and reference material.</p>
        <p class="hidden group-has-[#ttb20-r2:checked]/tabs:block">The current notebook, open in edit mode.</p>
        <p class="hidden group-has-[#ttb20-r3:checked]/tabs:block">Approvals, releases and publication state.</p>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-ttb20-yellow/20 px-3.5 py-2 font-ttb20-mono text-[11.5px] text-ttb20-paper">stencil face · has-checked:-translate-y-0.5 · hazard before:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb20-ink: #161616;
  --color-ttb20-ink: oklch(0.200 0 0);
  --color-ttb20-yellow: #f5cb1a;
  --color-ttb20-yellow: oklch(0.854 0.171 93.3);
  --color-ttb20-paper: #d9d3c3;
  --color-ttb20-paper: oklch(0.867 0.023 89.8);
  --font-ttb20-stencil: 'Big Shoulders Stencil Display', Impact, sans-serif;
  --font-ttb20-serif: 'Newsreader', Georgia, serif;
  --font-ttb20-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-20 {
  width: 100%;
  min-height: 100svh;
}
```
