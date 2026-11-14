---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-underline-draw-hover-effect/"
title: "Tailwind Underline Draw Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six link underline hovers in utilities — left-to-right draw, centre expand, two-tone dual line, highlighter bar, dotted grow and a gradient background-size…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Underline Draw Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-underline-draw-hover-effect/

Six link underline hovers in utilities — left-to-right draw, centre expand, two-tone dual line, highlighter bar, dotted grow and a gradient background-size sweep. The port's win is that the resting transform and the hover transform sit side by side in one class list, so the pair cannot drift apart.
## HTML
```html
<section class="thv-01 w-full min-h-svh grid place-items-center bg-thv01-bg font-thv01-sans px-6 py-14">
  <div class="w-[min(900px,100%)] grid grid-cols-[repeat(auto-fit,minmax(210px,1fr))] gap-8">
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv01-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-acc motion-reduce:after:transition-none">Left-to-Right Draw</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">scaleX · left origin</span>
    </div>
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv01-cyan after:origin-center after:scale-x-0 after:transition-transform after:duration-400 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-cyan motion-reduce:after:transition-none">Center Expand</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">scaleX · center origin</span>
    </div>
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs before:content-[''] before:absolute before:inset-x-0 before:bottom-1.5 before:h-0.5 before:bg-thv01-gold before:origin-right before:scale-x-0 before:transition-transform before:duration-400 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-thv01-gold after:origin-left after:scale-x-0 after:transition-transform after:duration-400 hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-gold motion-reduce:before:transition-none motion-reduce:after:transition-none">Dual Line Sweep</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">before + after toward center</span>
    </div>
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative isolate inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs transition-colors duration-300 after:content-[''] after:absolute after:-left-1.5 after:bottom-0 after:-z-10 after:w-[calc(100%+12px)] after:h-full after:rounded-sm after:bg-thv01-green/85 after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.22,1,.36,1)] hover:text-thv01-bg hover:after:scale-x-100 focus-visible:text-thv01-bg focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-green motion-reduce:after:transition-none">Highlighter Bar</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">isolate + negative z-index</span>
    </div>
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs transition-colors duration-300 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:border-b-2 after:border-dotted after:border-thv01-orange after:origin-left after:scale-x-0 after:transition-transform after:duration-400 hover:text-thv01-orange hover:after:scale-x-100 focus-visible:text-thv01-orange focus-visible:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-orange motion-reduce:after:transition-none">Dotted Border Grow</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">border-bottom + scaleX</span>
    </div>
    <div class="flex flex-col items-center gap-4 px-6 py-10 rounded-xl bg-white/[0.03] border border-white/[0.07]">
      <a href="#" class="relative inline-block pb-1 text-xl font-semibold text-thv01-text no-underline rounded-xs bg-[linear-gradient(90deg,var(--color-thv01-acc),var(--color-thv01-cyan))] bg-no-repeat [background-position:left_bottom] [background-size:0%_2px] transition-[background-size,color] duration-400 ease-[cubic-bezier(.4,0,.2,1)] hover:[background-size:100%_2px] hover:text-thv01-acc focus-visible:[background-size:100%_2px] focus-visible:text-thv01-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv01-acc motion-reduce:transition-none">Gradient Sweep</a>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv01-dim text-center">background-size animation</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv01-bg: #0a0a0f;
  --color-thv01-bg: oklch(0.14 0.01 285);
  --color-thv01-text: #e8e6f0;
  --color-thv01-text: oklch(0.92 0.01 285);
  --color-thv01-dim: #666666;
  --color-thv01-dim: oklch(0.52 0 0);
  --color-thv01-acc: #f72585;
  --color-thv01-acc: oklch(0.63 0.26 5);
  --color-thv01-cyan: #4cc9f0;
  --color-thv01-cyan: oklch(0.78 0.13 220);
  --color-thv01-gold: #ffd60a;
  --color-thv01-gold: oklch(0.88 0.18 95);
  --color-thv01-green: #06d6a0;
  --color-thv01-green: oklch(0.79 0.16 168);
  --color-thv01-orange: #fb5607;
  --color-thv01-orange: oklch(0.65 0.22 40);
  --font-thv01-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.thv-01 {
  width: 100%;
  min-height: 100svh;
}

.thv-01 ::selection {
  background: var(--color-thv01-acc);
  color: #fff;
}
```
