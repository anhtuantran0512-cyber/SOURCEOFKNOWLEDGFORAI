---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-modern-3d-skeuomorphic-button-press-effects/"
title: "Tailwind Modern 3D Skeuomorphic Button Press Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A soft tactile neumorphic CTA that appears extruded from the surface using paired light/dark shadows, depressing inward on press as the shadows invert."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Modern 3D Skeuomorphic Button Press Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-modern-3d-skeuomorphic-button-press-effects/

A soft tactile neumorphic CTA that appears extruded from the surface using paired light/dark shadows, depressing inward on press as the shadows invert. The port's contribution is legibility: four shadow stacks that used to live in four rules now sit next to each other, where you can actually see that they invert.
## HTML
```html
<div class="tbh-10-group w-full min-h-svh flex flex-wrap">
<section class="tbh-10a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh10-sans bg-tbh10a-surf" aria-label="Skeuomorphic press button">
  <button type="button" class="cursor-pointer border-0 rounded-2xl px-10 py-[18px] text-base font-extrabold text-tbh10a-ink bg-tbh10a-surf shadow-[-6px_-6px_14px_color-mix(in_oklab,var(--color-tbh10a-surf)_60%,white),7px_7px_16px_color-mix(in_oklab,var(--color-tbh10a-surf)_62%,black)] transition-[translate,box-shadow,color] duration-[180ms] hover:text-tbh10a-acc hover:shadow-[-8px_-8px_18px_color-mix(in_oklab,var(--color-tbh10a-surf)_55%,white),9px_9px_20px_color-mix(in_oklab,var(--color-tbh10a-surf)_58%,black)] focus-visible:text-tbh10a-acc active:translate-y-0.5 active:shadow-[inset_-4px_-4px_10px_color-mix(in_oklab,var(--color-tbh10a-surf)_60%,white),inset_5px_5px_12px_color-mix(in_oklab,var(--color-tbh10a-surf)_62%,black)] focus-visible:outline-3 focus-visible:outline-tbh10a-acc focus-visible:outline-offset-4 motion-reduce:transition-[box-shadow,color] motion-reduce:duration-[120ms]">
    Save changes
  </button>
</section>
<section class="tbh-10b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh10-sans bg-tbh10b-stage" aria-label="Glossy plastic button">
  <button type="button" class="relative overflow-hidden cursor-pointer border-0 rounded-[14px] px-[42px] py-[18px] text-base font-extrabold text-white bg-[linear-gradient(180deg,color-mix(in_oklab,var(--color-tbh10b-acc)_78%,white),var(--color-tbh10b-acc))] [text-shadow:0_1px_1px_oklch(0_0_0/0.25)] shadow-[inset_0_1px_0_oklch(1_0_0/0.7),inset_0_-6px_12px_-6px_oklch(0_0_0/0.4),0_10px_20px_-8px_color-mix(in_oklab,var(--color-tbh10b-acc)_60%,transparent)] transition-[translate,box-shadow] duration-[140ms] before:content-[''] before:absolute before:top-0.5 before:left-2 before:right-2 before:h-[42%] before:pointer-events-none before:[border-radius:12px_12px_40%_40%/12px_12px_60%_60%] before:bg-[linear-gradient(180deg,oklch(1_0_0/0.55),transparent)] hover:-translate-y-px focus-visible:-translate-y-px active:translate-y-0.5 active:shadow-[inset_0_1px_0_oklch(1_0_0/0.5),inset_0_4px_10px_-4px_oklch(0_0_0/0.5),0_4px_10px_-6px_color-mix(in_oklab,var(--color-tbh10b-acc)_60%,transparent)] focus-visible:outline-3 focus-visible:outline-tbh10b-acc focus-visible:outline-offset-4 motion-reduce:transition-[box-shadow] motion-reduce:duration-100 motion-reduce:hover:translate-y-0">
    Confirm order
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh10a-surf: #e6e9ef;
  --color-tbh10a-surf: oklch(0.92 0.008 265);
  --color-tbh10a-ink: #6b7280;
  --color-tbh10a-ink: oklch(0.5 0.02 265);
  --color-tbh10a-acc: #5b7cdb;
  --color-tbh10a-acc: oklch(0.55 0.16 265);
  --color-tbh10b-acc: #4d7ce0;
  --color-tbh10b-acc: oklch(0.6 0.18 250);
  --color-tbh10b-stage: #e8ecf3;
  --color-tbh10b-stage: oklch(0.93 0.01 255);
  --font-tbh10-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing stays CSS: every shadow stack, gradient and text-shadow is an arbitrary value. */

.tbh-10-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-10a,
.tbh-10b {
  min-height: 100svh;
}
```
