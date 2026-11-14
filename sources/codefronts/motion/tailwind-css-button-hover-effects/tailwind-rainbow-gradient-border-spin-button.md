---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-rainbow-gradient-border-spin-button/"
title: "Tailwind Rainbow Gradient Border Spin Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A vivid CTA framed by a rotating full-spectrum gradient border with a soft blurred glow bleeding behind it &mdash; the 'AI / Pro' badge look."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rainbow Gradient Border Spin Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-rainbow-gradient-border-spin-button/

A vivid CTA framed by a rotating full-spectrum gradient border with a soft blurred glow bleeding behind it &mdash; the 'AI / Pro' badge look. Unlike entry 08 it rotates the LAYER rather than a registered angle, so it needs no @property and works further back.
## HTML
```html
<div class="tbh-29-group w-full min-h-svh flex flex-wrap">
<section class="tbh-29a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh29-sans bg-tbh29a-stage" aria-label="Rainbow border spin button">
  <div class="group/btn relative isolate overflow-hidden rounded-[22px] p-2">
    <span aria-hidden="true" class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[150%] aspect-square -z-10 blur-[18px] opacity-55 bg-[conic-gradient(var(--color-tbh29a-c1),var(--color-tbh29a-c2),var(--color-tbh29a-c3),var(--color-tbh29a-c4),var(--color-tbh29a-c5),var(--color-tbh29a-c6),var(--color-tbh29a-c1))] animate-tbh29a-spin transition-opacity duration-300 group-hover/btn:opacity-85 group-hover/btn:[animation-duration:1.4s] motion-reduce:animate-none"></span>
    <button type="button" class="relative isolate overflow-hidden cursor-pointer border-0 rounded-[14px] px-[38px] py-4 text-base font-extrabold text-white bg-tbh29a-card transition-[translate] duration-200 before:content-[''] before:absolute before:left-1/2 before:top-1/2 before:-translate-x-1/2 before:-translate-y-1/2 before:w-[150%] before:aspect-square before:z-0 before:bg-[conic-gradient(var(--color-tbh29a-c1),var(--color-tbh29a-c2),var(--color-tbh29a-c3),var(--color-tbh29a-c4),var(--color-tbh29a-c5),var(--color-tbh29a-c6),var(--color-tbh29a-c1))] before:animate-tbh29a-spin hover:-translate-y-0.5 hover:before:[animation-duration:1.4s] focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:before:animate-none motion-reduce:hover:translate-y-0">
      <span aria-hidden="true" class="absolute inset-0.5 z-[1] rounded-xl bg-tbh29a-card"></span>
      <span class="relative z-[2]">Upgrade to Pro</span>
    </button>
  </div>
</section>
<section class="tbh-29b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh29-sans bg-tbh29b-stage" aria-label="Duotone border spin button">
  <button type="button" class="relative isolate overflow-hidden cursor-pointer border-0 rounded-full px-10 py-4 text-base font-extrabold text-white bg-tbh29b-card transition-[translate] duration-200 before:content-[''] before:absolute before:left-1/2 before:top-1/2 before:-translate-x-1/2 before:-translate-y-1/2 before:w-[160%] before:aspect-square before:z-0 before:bg-[conic-gradient(from_0deg,var(--color-tbh29b-c1),var(--color-tbh29b-c2),var(--color-tbh29b-c1))] before:animate-tbh29b-spin hover:-translate-y-0.5 hover:before:[animation-duration:1.2s] focus-visible:-translate-y-0.5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:before:animate-none motion-reduce:hover:translate-y-0">
    <span aria-hidden="true" class="absolute inset-0.5 z-[1] rounded-full bg-tbh29b-card"></span>
    <span class="relative z-[2]">Go premium</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh29a-card: #12121a;
  --color-tbh29a-card: oklch(0.18 0.015 285);
  --color-tbh29a-stage: #07070d;
  --color-tbh29a-stage: oklch(0.11 0.01 285);
  --color-tbh29a-c1: #ff3d81;
  --color-tbh29a-c1: oklch(0.68 0.24 0);
  --color-tbh29a-c2: #ffb03d;
  --color-tbh29a-c2: oklch(0.82 0.17 70);
  --color-tbh29a-c3: #f5f13d;
  --color-tbh29a-c3: oklch(0.93 0.19 105);
  --color-tbh29a-c4: #3dff8b;
  --color-tbh29a-c4: oklch(0.89 0.22 150);
  --color-tbh29a-c5: #3dc9ff;
  --color-tbh29a-c5: oklch(0.8 0.15 225);
  --color-tbh29a-c6: #8b3dff;
  --color-tbh29a-c6: oklch(0.55 0.28 295);
  --color-tbh29b-card: #0e1220;
  --color-tbh29b-card: oklch(0.17 0.025 265);
  --color-tbh29b-stage: #060810;
  --color-tbh29b-stage: oklch(0.1 0.015 265);
  --color-tbh29b-c1: #3d7bff;
  --color-tbh29b-c1: oklch(0.6 0.22 265);
  --color-tbh29b-c2: #b03dff;
  --color-tbh29b-c2: oklch(0.58 0.27 305);
  --font-tbh29-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh29a-spin: tbh29a-spin 4s linear infinite;
  --animate-tbh29b-spin: tbh29b-spin 3s linear infinite;
}
/* Stays CSS: the spin keyframes — and note what they no longer carry. The layers are centred
   with -translate-x-1/2 / -translate-y-1/2 on the discrete translate property, so rotation
   is all the keyframe owns. In the CSS original every stop restated translate(-50%,-50%). */

@keyframes tbh29a-spin {
  to {
    rotate: 360deg;
  }
}

@keyframes tbh29b-spin {
  to {
    rotate: 360deg;
  }
}

.tbh-29-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-29a,
.tbh-29b {
  min-height: 100svh;
}
```
