---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-sunburst-expand-radiant-button-effect/"
title: "Tailwind Sunburst Expand Radiant Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A warm radiant CTA where a glow blooms from the centre on hover, flooding the button like a sunrise &mdash; an opaque flood, distinct from entry 28's fading…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sunburst Expand Radiant Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-sunburst-expand-radiant-button-effect/

A warm radiant CTA where a glow blooms from the centre on hover, flooding the button like a sunrise &mdash; an opaque flood, distinct from entry 28's fading ring. Design B swaps the bloom for repeating-conic-gradient rays that scale AND rotate into place.
## HTML
```html
<div class="tbh-34-group w-full min-h-svh flex flex-wrap">
<section class="tbh-34a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh34-sans bg-tbh34a-stage" aria-label="Sunburst expand button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded-full border border-[color-mix(in_oklab,var(--color-tbh34a-warm)_60%,transparent)] px-11 py-[17px] text-base font-extrabold text-white bg-[color-mix(in_oklab,var(--color-tbh34a-warm)_22%,var(--color-tbh34a-stage))] focus-visible:outline-3 focus-visible:outline-tbh34a-warm focus-visible:outline-offset-4 before:content-[''] before:absolute before:left-1/2 before:top-1/2 before:-translate-x-1/2 before:-translate-y-1/2 before:w-full before:h-full before:z-0 before:scale-0 before:bg-[radial-gradient(circle,var(--color-tbh34a-warm)_0%,color-mix(in_oklab,var(--color-tbh34a-warm)_70%,transparent)_45%,transparent_70%)] before:transition-[scale] before:duration-500 before:ease-[cubic-bezier(.2,.9,.2,1)] hover:before:scale-[2.4] focus-visible:before:scale-[2.4] motion-reduce:before:transition-none">
    <span class="relative z-[1] transition-[text-shadow] duration-300 group-hover/btn:[text-shadow:0_0_12px_oklch(0.95_0.04_85/0.8)] group-focus-visible/btn:[text-shadow:0_0_12px_oklch(0.95_0.04_85/0.8)]">Start today</span>
  </button>
</section>
<section class="tbh-34b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh34-sans bg-tbh34b-stage" aria-label="Radial rays button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer border-0 rounded-full px-[46px] py-[17px] text-base font-extrabold text-tbh34b-ink bg-tbh34b-warm focus-visible:outline-3 focus-visible:outline-tbh34b-ink focus-visible:outline-offset-4">
    <span aria-hidden="true" class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[200%] aspect-square z-0 scale-0 opacity-0 bg-[repeating-conic-gradient(from_0deg,oklch(1_0_0/0.5)_0deg_6deg,transparent_6deg_18deg)] transition-[scale,rotate,opacity] duration-600 ease-[cubic-bezier(.2,.9,.2,1)] group-hover/btn:scale-100 group-hover/btn:[rotate:30deg] group-hover/btn:opacity-60 group-focus-visible/btn:scale-100 group-focus-visible/btn:[rotate:30deg] group-focus-visible/btn:opacity-60 motion-reduce:transition-opacity motion-reduce:group-hover/btn:scale-100 motion-reduce:group-hover/btn:[rotate:0deg] motion-reduce:group-hover/btn:opacity-40"></span>
    <span class="relative z-[1]">Shine</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh34a-warm: #e8a94a;
  --color-tbh34a-warm: oklch(0.78 0.16 65);
  --color-tbh34a-stage: #1a1206;
  --color-tbh34a-stage: oklch(0.2 0.04 70);
  --color-tbh34b-warm: #e8c04a;
  --color-tbh34b-warm: oklch(0.82 0.16 85);
  --color-tbh34b-ink: #1a1206;
  --color-tbh34b-ink: oklch(0.22 0.04 85);
  --color-tbh34b-stage: #171205;
  --color-tbh34b-stage: oklch(0.18 0.03 85);
  --font-tbh34-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: two gradients, a scale, a rotation and a text-shadow. */

.tbh-34-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-34a,
.tbh-34b {
  min-height: 100svh;
}
```
