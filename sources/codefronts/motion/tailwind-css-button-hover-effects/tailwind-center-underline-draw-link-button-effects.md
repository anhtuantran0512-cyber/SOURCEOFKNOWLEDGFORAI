---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-center-underline-draw-link-button-effects/"
title: "Tailwind Center Underline Draw Link Button Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "The minimal one: a crisp underline grows outward from the centre to full width on hover &mdash; the cleanest affordance for nav links and inline CTAs, in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Center Underline Draw Link Button Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-center-underline-draw-link-button-effects/

The minimal one: a crisp underline grows outward from the centre to full width on hover &mdash; the cleanest affordance for nav links and inline CTAs, in three treatments. Design B contains the trick worth stealing: swapping transform-origin between states turns a grow into a directional swipe.
## HTML
```html
<div class="tbh-22-group w-full min-h-svh flex flex-wrap">
<section class="tbh-22a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh22-sans bg-tbh22a-stage" aria-label="Center underline button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-1 pt-1.5 pb-2.5 text-lg font-bold text-tbh22a-ink transition-colors duration-200 hover:text-tbh22a-line focus-visible:text-tbh22a-line focus-visible:outline-none after:content-[''] after:absolute after:left-0 after:bottom-0 after:w-full after:h-0.5 after:bg-tbh22a-line after:scale-x-0 after:origin-center after:transition-[scale,height] after:duration-300 after:ease-out hover:after:scale-x-100 focus-visible:after:scale-x-100 focus-visible:after:h-[3px] motion-reduce:after:transition-none">
    Learn more
  </button>
</section>
<section class="tbh-22b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh22-serif bg-tbh22b-stage" aria-label="Ink swipe underline button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-0.5 pt-1 pb-2.5 text-xl italic text-tbh22b-ink transition-colors duration-200 hover:text-tbh22b-line focus-visible:text-tbh22b-line focus-visible:outline-none after:content-[''] after:absolute after:left-0 after:bottom-0.5 after:w-full after:h-[3px] after:bg-tbh22b-line after:scale-x-0 after:origin-right after:transition-[scale] after:duration-[350ms] after:ease-[cubic-bezier(.6,0,.2,1)] hover:after:scale-x-100 hover:after:origin-left focus-visible:after:scale-x-100 focus-visible:after:origin-left motion-reduce:after:transition-none">
    Read essay
  </button>
</section>
<section class="tbh-22c flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh22-sans bg-tbh22c-stage" aria-label="Double rule underline button">
  <button type="button" class="relative cursor-pointer border-0 bg-transparent px-1 pt-1.5 pb-3.5 text-lg font-bold text-tbh22c-ink transition-colors duration-200 hover:text-tbh22c-line focus-visible:text-tbh22c-line focus-visible:outline-none before:content-[''] before:absolute before:left-0 before:bottom-1.5 before:w-full before:h-0.5 before:bg-tbh22c-line before:scale-x-0 before:origin-left before:transition-[scale] before:duration-300 before:ease-out after:content-[''] after:absolute after:left-0 after:bottom-0 after:w-full after:h-0.5 after:bg-tbh22c-line after:scale-x-0 after:origin-right after:transition-[scale] after:duration-300 after:delay-[80ms] after:ease-out hover:before:scale-x-100 hover:after:scale-x-100 focus-visible:before:scale-x-100 focus-visible:after:scale-x-100 motion-reduce:before:transition-none motion-reduce:after:transition-none motion-reduce:after:delay-0">
    See pricing
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh22a-line: #3f74d8;
  --color-tbh22a-line: oklch(0.55 0.18 255);
  --color-tbh22a-ink: #1a1a1a;
  --color-tbh22a-ink: oklch(0.22 0 0);
  --color-tbh22a-stage: #fafafa;
  --color-tbh22a-stage: oklch(0.98 0 0);
  --color-tbh22b-line: #a8452c;
  --color-tbh22b-line: oklch(0.5 0.15 25);
  --color-tbh22b-ink: #241c17;
  --color-tbh22b-ink: oklch(0.25 0.02 45);
  --color-tbh22b-stage: #fbf8f3;
  --color-tbh22b-stage: oklch(0.98 0.008 85);
  --color-tbh22c-line: #3d8e96;
  --color-tbh22c-line: oklch(0.55 0.14 200);
  --color-tbh22c-ink: #0e2a2c;
  --color-tbh22c-ink: oklch(0.28 0.03 200);
  --color-tbh22c-stage: #f4f8f8;
  --color-tbh22c-stage: oklch(0.97 0.008 200);
  --font-tbh22-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbh22-serif: 'Newsreader', Georgia, serif;
}
/* Nothing stays CSS: three underline treatments, all utilities. */

.tbh-22-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-22a,
.tbh-22b,
.tbh-22c {
  min-height: 100svh;
}
```
