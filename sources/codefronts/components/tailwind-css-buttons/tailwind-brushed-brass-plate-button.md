---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-brushed-brass-plate-button/"
title: "Tailwind Brushed Brass Plate Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A machined brass nameplate: horizontal brush grain from stacked repeating gradients, four countersunk screws, engraved letterforms cut with a two-shadow…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brushed Brass Plate Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-brushed-brass-plate-button/

A machined brass nameplate: horizontal brush grain from stacked repeating gradients, four countersunk screws, engraved letterforms cut with a two-shadow bevel, and a specular band that sweeps across the metal on hover. The grain is the collection's first clear case for keeping paint in CSS.
## HTML
```html
<div class="tb-21 w-full min-h-svh grid place-items-center font-tb21-serif p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-21__plate group relative overflow-hidden isolate cursor-pointer min-h-16 px-12 border border-tb21-brass-lo rounded-lg text-base font-semibold uppercase tracking-[0.16em] text-tb21-engrave [text-shadow:0_1px_0_#ffffff8c,0_-1px_0_#0000006b] shadow-[inset_0_1px_0_#ffffff73,inset_0_-1px_0_#00000059,0_14px_26px_-14px_#000000bf] transition-[translate,box-shadow,filter] duration-200 hover:brightness-105 active:translate-y-px active:shadow-[inset_0_2px_6px_#00000080] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb21-brass-hi disabled:cursor-not-allowed disabled:grayscale-[0.7] disabled:brightness-[0.85] motion-reduce:transition-none">
    <span aria-hidden="true" class="tb-21__screw absolute z-30 top-2 left-2.5 size-2.5 rounded-full transition-[rotate] duration-300 group-active:rotate-[12deg] motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="tb-21__screw absolute z-30 top-2 right-2.5 size-2.5 rounded-full rotate-[34deg] transition-[rotate] duration-300 group-active:rotate-[12deg] motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="tb-21__screw absolute z-30 bottom-2 left-2.5 size-2.5 rounded-full -rotate-[22deg] transition-[rotate] duration-300 group-active:rotate-[12deg] motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="tb-21__screw absolute z-30 bottom-2 right-2.5 size-2.5 rounded-full rotate-[12deg] transition-[rotate] duration-300 group-active:rotate-[12deg] motion-reduce:transition-none"></span>
    <span aria-hidden="true" class="absolute inset-0 z-20 pointer-events-none -translate-x-[62%] bg-[linear-gradient(100deg,transparent_38%,rgba(255,255,255,0.42)_50%,transparent_62%)] transition-transform duration-[850ms] ease-tb21-out group-hover:translate-x-[62%] group-focus-visible:translate-x-[62%] motion-reduce:hidden"></span>
    <span class="relative z-40">Reserve a table</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb21-bg: #171310;
  --color-tb21-bg: oklch(0.18 0.015 60);
  --color-tb21-brass: #b08d4f;
  --color-tb21-brass: oklch(0.66 0.08 82);
  --color-tb21-brass-hi: #e6cd94;
  --color-tb21-brass-hi: oklch(0.86 0.08 88);
  --color-tb21-brass-lo: #7d6132;
  --color-tb21-brass-lo: oklch(0.48 0.07 80);
  --color-tb21-engrave: #3d2d12;
  --color-tb21-engrave: oklch(0.29 0.05 72);
  --font-tb21-serif: "Cinzel", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb21-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(40rem 24rem at 50% 40%, color-mix(in oklab, var(--color-tb21-brass) 14%, transparent), transparent 70%), var(--color-tb21-bg);
}
/* THE GRAIN. Three repeating gradients at 5px / 7px periods over a diagonal base —
   one indivisible texture recipe, illegible as an arbitrary utility. */

.tb-21__plate {
  background-color: var(--color-tb21-brass);
  background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.10) 0 1px, transparent 1px 2px, rgba(0,0,0,.07) 2px 3px, transparent 3px 5px), repeating-linear-gradient(90deg, rgba(255,255,255,.05) 0 1px, transparent 1px 7px), linear-gradient(112deg, var(--color-tb21-brass-hi), var(--color-tb21-brass) 34%, var(--color-tb21-brass-lo) 62%, var(--color-tb21-brass) 86%);
}
/* Countersunk screw head + slot. The slot is a clipped pseudo-element. */

.tb-21__screw {
  background: radial-gradient(circle at 35% 30%, #f0e0b8, #8d6f38 60%, #5c4520);
  box-shadow: inset 0 -1px 1px rgba(0,0,0,.5), 0 1px 1px rgba(255,255,255,.25);
}

.tb-21__screw::after {
  content: '';
  position: absolute;
  inset: 22% 12%;
  background: rgba(0,0,0,.55);
  clip-path: polygon(0 42%, 100% 42%, 100% 58%, 0 58%);
}

@media (prefers-color-scheme: light) {
  .tb-21:not([data-theme="dark"]) {
    --color-tb21-bg: oklch(0.28 0.02 60);
  }
}

.tb-21[data-theme="light"] {
  --color-tb21-bg: oklch(0.28 0.02 60);
}

@media (forced-colors: active) {
  .tb-21__plate {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    text-shadow: none;
    box-shadow: none;
  }

  .tb-21__plate span[aria-hidden] {
    display: none;
  }
}
```
