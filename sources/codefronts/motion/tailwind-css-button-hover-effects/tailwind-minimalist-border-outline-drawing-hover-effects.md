---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-minimalist-border-outline-drawing-hover-effects/"
title: "Tailwind Minimalist Border & Outline Drawing Hover Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A refined understated CTA for editorial and luxury layouts: at rest it's just text, and on hover a hairline stroke draws itself continuously around the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Border & Outline Drawing Hover Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-minimalist-border-outline-drawing-hover-effects/

A refined understated CTA for editorial and luxury layouts: at rest it's just text, and on hover a hairline stroke draws itself continuously around the rounded-rectangle perimeter. Tailwind reaches SVG presentation attributes the same way it reaches anything else it has no scale for &mdash; arbitrary properties.
## HTML
```html
<div class="tbh-09-group w-full min-h-svh flex flex-wrap">
<section class="tbh-09a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh09-sans bg-tbh09a-stage" aria-label="Outline drawing button">
  <button type="button" class="group/btn relative cursor-pointer border-0 bg-transparent px-[42px] py-5 text-[15px] font-bold uppercase tracking-[0.06em] text-tbh09a-line focus-visible:outline-none">
    <svg aria-hidden="true" preserveAspectRatio="none" class="absolute inset-0 w-full h-full overflow-visible">
      <rect x="1" y="1" rx="12" ry="12" class="fill-none [stroke:var(--color-tbh09a-line)] [stroke-width:2] [width:calc(100%-2px)] [height:calc(100%-2px)] [stroke-dasharray:0_1000] transition-[stroke-dasharray] duration-[800ms] ease-out group-hover/btn:[stroke-dasharray:1000_0] group-focus-visible/btn:[stroke-dasharray:1000_0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:1000_0] motion-reduce:opacity-50"></rect>
    </svg>
    <span class="relative z-[1] group-focus-visible/btn:underline group-focus-visible/btn:underline-offset-4">Read the story</span>
  </button>
</section>
<section class="tbh-09b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh09-sans bg-tbh09b-stage" aria-label="Underline to box button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-8 py-4 text-base font-bold text-tbh09b-line focus-visible:outline-none before:content-[''] before:absolute before:left-0 before:bottom-0 before:w-full before:h-0.5 before:bg-tbh09b-line before:origin-left after:content-[''] after:absolute after:inset-0 after:border-2 after:border-b-0 after:border-tbh09b-line after:[clip-path:inset(0_0_100%_0)] after:transition-[clip-path] after:duration-[350ms] after:delay-150 after:ease-out hover:after:[clip-path:inset(0_0_0_0)] focus-visible:after:[clip-path:inset(0_0_0_0)] focus-visible:underline focus-visible:underline-offset-4 motion-reduce:after:transition-none motion-reduce:after:delay-0">
    <span>Discover more</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh09a-line: #4a5068;
  --color-tbh09a-line: oklch(0.45 0.03 265);
  --color-tbh09a-stage: #f6f5f1;
  --color-tbh09a-stage: oklch(0.97 0.006 90);
  --color-tbh09b-line: #b04a2f;
  --color-tbh09b-line: oklch(0.5 0.14 25);
  --color-tbh09b-stage: #faf6f4;
  --color-tbh09b-stage: oklch(0.98 0.008 35);
  --font-tbh09-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: SVG presentation attributes are reachable as arbitrary properties,
   which is the useful discovery in this port. */

.tbh-09-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-09a,
.tbh-09b {
  min-height: 100svh;
}
```
