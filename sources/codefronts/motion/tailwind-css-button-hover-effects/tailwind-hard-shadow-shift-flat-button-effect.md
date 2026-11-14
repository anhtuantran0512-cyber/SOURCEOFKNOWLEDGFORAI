---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-hard-shadow-shift-flat-button-effect/"
title: "Tailwind Hard Shadow Shift Flat Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A graphic flat-design CTA with a solid blur-free offset shadow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hard Shadow Shift Flat Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-hard-shadow-shift-flat-button-effect/

A graphic flat-design CTA with a solid blur-free offset shadow. On hover it slides onto its shadow and flattens against the page as if pressed &mdash; monochrome and graphic, distinct from entry 11's neon snap. Design B runs the same mechanic in reverse, lifting off the page instead.
## HTML
```html
<div class="tbh-27-group w-full min-h-svh flex flex-wrap">
<section class="tbh-27a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh27-sans bg-tbh27a-stage" aria-label="Hard shadow shift button">
  <button type="button" class="cursor-pointer rounded-lg border-2 border-tbh27-ink px-[38px] py-4 text-base font-extrabold text-white bg-tbh27a-fill shadow-[6px_6px_0_var(--color-tbh27-ink)] transition-[translate,scale,box-shadow] duration-[160ms] ease-out hover:translate-x-[6px] hover:translate-y-[6px] hover:shadow-[0_0_0_var(--color-tbh27-ink)] focus-visible:translate-x-[6px] focus-visible:translate-y-[6px] focus-visible:shadow-[0_0_0_var(--color-tbh27-ink)] active:scale-[.98] focus-visible:outline-3 focus-visible:outline-tbh27-ink focus-visible:outline-offset-[5px] motion-reduce:transition-[box-shadow] motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">
    Get the kit
  </button>
</section>
<section class="tbh-27b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh27-sans bg-tbh27b-stage" aria-label="Lift hard shadow button">
  <button type="button" class="cursor-pointer rounded-lg border-2 border-tbh27b-ink px-10 py-4 text-base font-extrabold text-tbh27b-ink bg-tbh27b-fill shadow-[0_0_0_var(--color-tbh27b-ink)] transition-[translate,box-shadow] duration-[160ms] ease-out hover:-translate-x-[5px] hover:-translate-y-[5px] hover:shadow-[5px_5px_0_var(--color-tbh27b-ink)] focus-visible:-translate-x-[5px] focus-visible:-translate-y-[5px] focus-visible:shadow-[5px_5px_0_var(--color-tbh27b-ink)] active:-translate-x-[2px] active:-translate-y-[2px] active:shadow-[2px_2px_0_var(--color-tbh27b-ink)] focus-visible:outline-3 focus-visible:outline-tbh27b-ink focus-visible:outline-offset-[5px] motion-reduce:transition-[box-shadow] motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">
    Download deck
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh27-ink: #16130f;
  --color-tbh27-ink: oklch(0.18 0.01 60);
  --color-tbh27a-fill: #3f6ad0;
  --color-tbh27a-fill: oklch(0.55 0.17 255);
  --color-tbh27a-stage: #f0ede4;
  --color-tbh27a-stage: oklch(0.94 0.012 90);
  --color-tbh27b-ink: #1a1206;
  --color-tbh27b-ink: oklch(0.22 0.04 85);
  --color-tbh27b-fill: #ffcf4d;
  --color-tbh27b-fill: oklch(0.88 0.17 90);
  --color-tbh27b-stage: #faf4e8;
  --color-tbh27b-stage: oklch(0.97 0.015 85);
  --font-tbh27-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: one shadow and one matching translate per state. */

.tbh-27-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-27a,
.tbh-27b {
  min-height: 100svh;
}
```
