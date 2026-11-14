---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-border-draw-hover-effect/"
title: "Tailwind Border Draw Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six border-draw hovers — clockwise stroke, corner brackets, double rail, dashed grow, a spinning conic ring and an inset box-shadow flood."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Border Draw Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-border-draw-hover-effect/

Six border-draw hovers — clockwise stroke, corner brackets, double rail, dashed grow, a spinning conic ring and an inset box-shadow flood. The conic ring animates a registered --angle rather than rotating the element, which is what keeps a wide rectangle from flailing.
## HTML
```html
<section class="thv-08 w-full min-h-svh grid place-items-center bg-thv08-bg font-thv08-sans px-6 py-14">
  <div class="w-[min(880px,100%)] grid grid-cols-[repeat(auto-fit,minmax(230px,1fr))] gap-9">
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative min-h-11 px-8 py-3 bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-amber cursor-pointer transition-[color,box-shadow] duration-300 delay-[390ms] hover:text-thv08-text hover:shadow-[inset_2px_0_0_var(--color-thv08-amber),inset_-2px_0_0_var(--color-thv08-amber)] hover:delay-200 focus-visible:text-thv08-text focus-visible:shadow-[inset_2px_0_0_var(--color-thv08-amber),inset_-2px_0_0_var(--color-thv08-amber)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv08-amber before:content-[''] before:absolute before:top-0 before:right-0 before:w-0 before:h-0.5 before:bg-thv08-amber before:transition-[width] before:duration-200 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-thv08-amber after:transition-[width] after:duration-200 after:delay-400 hover:before:w-full hover:after:w-full hover:after:delay-200 focus-visible:before:w-full focus-visible:after:w-full motion-reduce:before:transition-none motion-reduce:after:transition-none">Clockwise Draw</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">clockwise stroke</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-visible min-h-11 px-8 py-3 bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-orange cursor-pointer transition-colors duration-300 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv08-orange before:content-[''] before:absolute before:-top-0.5 before:-left-0.5 before:w-3 before:h-3 before:border-t-2 before:border-l-2 before:border-thv08-orange before:transition-[width,height] before:duration-250 after:content-[''] after:absolute after:-bottom-0.5 after:-right-0.5 after:w-3 after:h-3 after:border-b-2 after:border-r-2 after:border-thv08-orange after:transition-[width,height] after:duration-250 hover:before:w-[calc(100%+4px)] hover:before:h-[calc(100%+4px)] hover:after:w-[calc(100%+4px)] hover:after:h-[calc(100%+4px)] focus-visible:before:w-[calc(100%+4px)] focus-visible:before:h-[calc(100%+4px)] focus-visible:after:w-[calc(100%+4px)] focus-visible:after:h-[calc(100%+4px)] motion-reduce:before:transition-none motion-reduce:after:transition-none">Corner Flash</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">corner brackets</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative overflow-hidden min-h-11 px-8 py-3 bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-red cursor-pointer transition-colors duration-300 hover:text-thv08-text focus-visible:text-thv08-text focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv08-red before:content-[''] before:absolute before:top-0 before:-left-full before:w-full before:h-0.5 before:bg-thv08-red before:transition-[left] before:duration-350 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[''] after:absolute after:bottom-0 after:-right-full after:w-full after:h-0.5 after:bg-thv08-red after:transition-[right] after:duration-350 after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:left-0 hover:after:right-0 focus-visible:before:left-0 focus-visible:after:right-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">Double Rail</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">dual-rail slide</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 bg-transparent border-2 border-dashed border-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-yellow cursor-pointer transition-[border-color,color,padding] duration-300 hover:border-thv08-yellow hover:text-thv08-text hover:px-10 focus-visible:border-thv08-yellow focus-visible:text-thv08-text focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv08-yellow motion-reduce:transition-[border-color,color] motion-reduce:hover:px-8">Dashed Grow</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">dashed border scale</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="relative isolate overflow-visible min-h-11 px-8 py-3 bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-text cursor-pointer focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv08-amber before:content-[''] before:absolute before:-inset-0.5 before:-z-10 before:rounded-[4px] before:opacity-0 before:transition-opacity before:duration-300 before:[--thv08-angle:0deg] before:[background:conic-gradient(from_var(--thv08-angle),transparent_0%,var(--color-thv08-amber)_30%,var(--color-thv08-orange)_50%,transparent_70%)] after:content-[''] after:absolute after:inset-0 after:-z-10 after:rounded-[2px] after:bg-thv08-bg hover:before:opacity-100 hover:before:animate-thv08-spin focus-visible:before:opacity-100 focus-visible:before:animate-thv08-spin motion-reduce:hover:before:animate-none">Gradient Sweep</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">conic border sweep</span>
    </div>
    <div class="flex flex-col items-center gap-5 px-5 py-10 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <button type="button" class="min-h-11 px-8 py-3 bg-transparent text-[0.95rem] font-semibold tracking-[0.05em] text-thv08-gold cursor-pointer shadow-[inset_0_0_0_0_var(--color-thv08-amber)] transition-[box-shadow,color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:text-black hover:shadow-[inset_0_0_0_60px_var(--color-thv08-amber)] focus-visible:text-black focus-visible:shadow-[inset_0_0_0_60px_var(--color-thv08-amber)] focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-thv08-amber motion-reduce:transition-none">Inset Reveal</button>
      <span class="text-[11px] tracking-[0.12em] uppercase text-thv08-dim">box-shadow inset</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv08-bg: #0c0a03;
  --color-thv08-bg: oklch(0.14 0.02 85);
  --color-thv08-text: #fef3c7;
  --color-thv08-text: oklch(0.95 0.06 95);
  --color-thv08-dim: #6b7280;
  --color-thv08-dim: oklch(0.55 0.02 265);
  --color-thv08-amber: #f59e0b;
  --color-thv08-amber: oklch(0.77 0.16 70);
  --color-thv08-orange: #f97316;
  --color-thv08-orange: oklch(0.7 0.19 45);
  --color-thv08-red: #ef4444;
  --color-thv08-red: oklch(0.64 0.21 25);
  --color-thv08-yellow: #fde047;
  --color-thv08-yellow: oklch(0.91 0.17 99);
  --color-thv08-gold: #b45309;
  --color-thv08-gold: oklch(0.55 0.14 55);
  --font-thv08-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv08-spin: thv08-spin 1.5s linear infinite;
}

.thv-08 {
  width: 100%;
  min-height: 100svh;
}

.thv-08 ::selection {
  background: var(--color-thv08-amber);
  color: #000;
}
/* A registered custom property: a declaration, not a value — stays in CSS. */

@property --thv08-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@keyframes thv08-spin {
  to {
    --thv08-angle: 360deg;
  }
}
```
