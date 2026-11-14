---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-strikethrough-hover-link-effect/"
title: "Tailwind Strikethrough Hover Link Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six strikethroughs that draw themselves — solid, hairline, chunky, wavy, dashed and a double line with a staggered second pass."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Strikethrough Hover Link Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-strikethrough-hover-link-effect/

Six strikethroughs that draw themselves — solid, hairline, chunky, wavy, dashed and a double line with a staggered second pass. All are mid-height after: bars scaled from zero; only the fill changes.
## HTML
```html
<section class="thv-27 w-full min-h-svh bg-thv27-bg font-thv27-sans px-8 py-12 flex flex-col items-center justify-center gap-10">
  <p class="text-[0.72rem] tracking-[0.15em] uppercase text-thv27-dim">Strikethrough Hover Links — 6 Styles</p>
  <div class="flex flex-wrap justify-center gap-12">
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-dim focus-visible:text-thv27-dim focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv27-acc after:content-[''] after:absolute after:left-0 after:top-1/2 after:-mt-px after:w-full after:h-0.5 after:bg-thv27-acc after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Solid Strike</a>
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-dim focus-visible:text-thv27-dim focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white after:content-[''] after:absolute after:left-0 after:top-1/2 after:-mt-px after:w-full after:h-px after:bg-white/70 after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Hair-thin Strike</a>
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-amber focus-visible:text-thv27-amber focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv27-amber after:content-[''] after:absolute after:left-0 after:top-[44%] after:-mt-[3px] after:w-full after:h-1.5 after:rounded-[3px] after:bg-thv27-amber/85 after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Chunky Strike</a>
  </div>
  <div class="flex flex-wrap justify-center gap-12">
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-acc focus-visible:text-thv27-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv27-acc after:content-[''] after:absolute after:left-0 after:top-[54%] after:w-full after:h-1 after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] after:[background:radial-gradient(ellipse_3px_2px_at_3px_2px,#e0055f_100%,transparent)_0/6px_4px_repeat-x,radial-gradient(ellipse_3px_2px_at_3px_0,transparent_100%,#e0055f)_3px/6px_4px_repeat-x] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Wavy Strike</a>
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-violet focus-visible:text-thv27-violet focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv27-violet after:content-[''] after:absolute after:left-0 after:top-1/2 after:-mt-px after:w-full after:h-0.5 after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.4,0,.2,1)] after:[background:repeating-linear-gradient(90deg,#7c6af7_0,#7c6af7_6px,transparent_6px,transparent_10px)] hover:after:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:after:transition-none">Dashed Strike</a>
    <a href="#" class="relative text-[1.35rem] font-semibold text-thv27-ink no-underline rounded-xs transition-colors duration-250 hover:text-thv27-sky focus-visible:text-thv27-sky focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-thv27-sky before:content-[''] before:absolute before:left-0 before:top-[42%] before:w-full before:h-[1.5px] before:bg-thv27-sky before:origin-right before:scale-x-0 before:transition-transform before:duration-300 before:ease-[cubic-bezier(.4,0,.2,1)] after:content-[''] after:absolute after:left-0 after:top-[56%] after:w-full after:h-[1.5px] after:bg-thv27-sky after:origin-left after:scale-x-0 after:transition-transform after:duration-300 after:delay-[60ms] after:ease-[cubic-bezier(.4,0,.2,1)] hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none">Double Strike</a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv27-bg: #0c0c0f;
  --color-thv27-bg: oklch(0.13 0.01 285);
  --color-thv27-ink: #dddddd;
  --color-thv27-ink: oklch(0.88 0 0);
  --color-thv27-dim: #8e8e96;
  --color-thv27-dim: oklch(0.65 0.01 285);
  --color-thv27-acc: #e0055f;
  --color-thv27-acc: oklch(0.58 0.24 3);
  --color-thv27-amber: #f7a600;
  --color-thv27-amber: oklch(0.78 0.17 72);
  --color-thv27-violet: #7c6af7;
  --color-thv27-violet: oklch(0.62 0.2 285);
  --color-thv27-sky: #55ccff;
  --color-thv27-sky: oklch(0.79 0.13 227);
  --font-thv27-sans: 'Space Grotesk', system-ui, sans-serif;
}

.thv-27 {
  width: 100%;
  min-height: 100svh;
}

.thv-27 ::selection {
  background: var(--color-thv27-acc);
  color: #fff;
}
```
