---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-dual-line-intersection-border-draw-button/"
title: "Tailwind Dual-Line Intersection Border Draw Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A crisp architectural outline CTA for editorial and agency sites: on hover two lines draw from opposite corners and meet to close a rectangular border around…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dual-Line Intersection Border Draw Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-dual-line-intersection-border-draw-button/

A crisp architectural outline CTA for editorial and agency sites: on hover two lines draw from opposite corners and meet to close a rectangular border around the label. The port is the cleanest kind &mdash; two pseudo-elements, four utilities each, and the staggered corner-meet is one delay-300.
## HTML
```html
<div class="tbh-05-group w-full min-h-svh flex flex-wrap">
<section class="tbh-05a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh05-sans bg-tbh05a-bg" aria-label="Dual-line border draw button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-10 py-[18px] text-[15px] font-bold uppercase tracking-[0.08em] text-tbh05a-line before:content-[''] before:absolute before:inset-0 before:pointer-events-none before:border-t-2 before:border-r-2 before:border-tbh05a-line before:scale-0 before:origin-top-left before:transition-[scale] before:duration-300 before:ease-out after:content-[''] after:absolute after:inset-0 after:pointer-events-none after:border-b-2 after:border-l-2 after:border-tbh05a-line after:scale-0 after:origin-bottom-right after:transition-[scale] after:duration-300 after:ease-out hover:before:scale-100 hover:after:scale-100 hover:after:delay-300 focus-visible:before:scale-100 focus-visible:after:scale-100 focus-visible:after:delay-300 focus-visible:outline-2 focus-visible:outline-dashed focus-visible:outline-tbh05a-line focus-visible:outline-offset-[6px] motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:hover:after:delay-0">
    <span>Explore work</span>
  </button>
</section>
<section class="tbh-05b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh05-mono bg-tbh05b-bg" aria-label="Corner bracket button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-[46px] py-5 text-sm font-bold uppercase tracking-[0.14em] text-tbh05b-line before:content-[''] before:absolute before:top-0 before:left-0 before:w-[18px] before:h-[18px] before:pointer-events-none before:border-2 before:border-r-0 before:border-b-0 before:border-tbh05b-line before:transition-[width,height] before:duration-300 before:ease-out after:content-[''] after:absolute after:bottom-0 after:right-0 after:w-[18px] after:h-[18px] after:pointer-events-none after:border-2 after:border-l-0 after:border-t-0 after:border-tbh05b-line after:transition-[width,height] after:duration-300 after:ease-out hover:before:w-full hover:before:h-full hover:after:w-full hover:after:h-full focus-visible:before:w-full focus-visible:before:h-full focus-visible:after:w-full focus-visible:after:h-full focus-visible:outline-none focus-visible:underline focus-visible:underline-offset-4 motion-reduce:before:transition-none motion-reduce:after:transition-none">
    <span>View case study</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh05a-line: #6b7280;
  --color-tbh05a-line: oklch(0.55 0.02 260);
  --color-tbh05a-bg: #f4f3ef;
  --color-tbh05a-bg: oklch(0.96 0.005 90);
  --color-tbh05b-line: #3ad8cf;
  --color-tbh05b-line: oklch(0.72 0.16 190);
  --color-tbh05b-bg: #0a1416;
  --color-tbh05b-bg: oklch(0.16 0.02 200);
  --font-tbh05-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbh05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Nothing needs to stay CSS in this demo — the whole effect is utilities, which is why it is
   the batch's clearest argument for the port. */

.tbh-05-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-05a,
.tbh-05b {
  min-height: 100svh;
}
```
