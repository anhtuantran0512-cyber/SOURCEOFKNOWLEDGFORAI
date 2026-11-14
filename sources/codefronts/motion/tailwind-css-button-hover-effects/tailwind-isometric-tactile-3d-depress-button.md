---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-isometric-tactile-3d-depress-button/"
title: "Tailwind Isometric Tactile 3D Depress Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A chunky game-UI button in isometric perspective with a thick extruded side, so it looks like a real key."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Isometric Tactile 3D Depress Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-isometric-tactile-3d-depress-button/

A chunky game-UI button in isometric perspective with a thick extruded side, so it looks like a real key. On hover the tilt eases toward flat and the shadow stack collapses; on press it lands. This is the batch's best illustration of v4's discrete rotate property &mdash; three states, and not one of them restates the others.
## HTML
```html
<div class="tbh-06-group w-full min-h-svh flex flex-wrap">
<section class="tbh-06a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-[70px] font-tbh06-sans bg-tbh06a-stage [perspective:700px]" aria-label="Isometric 3D button">
  <button type="button" class="cursor-pointer border-0 rounded-2xl px-10 py-[18px] text-[18px] font-extrabold text-tbh06a-ink bg-tbh06a-cap [rotate:x_15deg] -translate-y-1.5 shadow-[0_1px_0_var(--color-tbh06a-side),0_2px_0_var(--color-tbh06a-side),0_3px_0_var(--color-tbh06a-side),0_4px_0_var(--color-tbh06a-side),0_5px_0_var(--color-tbh06a-side),0_6px_0_var(--color-tbh06a-side),0_7px_0_var(--color-tbh06a-side),0_8px_0_var(--color-tbh06a-side),0_20px_24px_-8px_oklch(0_0_0/0.45)] transition-[rotate,translate,box-shadow] duration-[220ms] ease-[cubic-bezier(.3,.7,.4,1)] hover:[rotate:x_4deg] hover:-translate-y-px hover:shadow-[0_1px_0_var(--color-tbh06a-side),0_2px_0_var(--color-tbh06a-side),0_3px_0_var(--color-tbh06a-side),0_4px_0_var(--color-tbh06a-side),0_12px_16px_-8px_oklch(0_0_0/0.4)] focus-visible:[rotate:x_4deg] focus-visible:-translate-y-px active:[rotate:x_0deg] active:translate-y-0.5 active:shadow-[0_1px_0_var(--color-tbh06a-side),0_2px_0_var(--color-tbh06a-side),0_6px_10px_-6px_oklch(0_0_0/0.4)] focus-visible:outline-3 focus-visible:outline-tbh06a-ink focus-visible:outline-offset-4 motion-reduce:transition-[box-shadow] motion-reduce:duration-150">
    Press me
  </button>
</section>
<section class="tbh-06b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh06-sans bg-tbh06b-stage" aria-label="Pushable 3D pill button">
  <button type="button" class="group/btn relative cursor-pointer border-0 bg-transparent p-0 rounded-[14px] text-[17px] font-extrabold text-white focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span aria-hidden="true" class="absolute inset-0 rounded-[14px] bg-tbh06b-edge"></span>
    <span class="block relative px-10 py-4 rounded-[14px] bg-tbh06b-front -translate-y-1.5 transition-[translate] duration-[120ms] ease-[cubic-bezier(.3,.7,.4,1)] group-hover/btn:-translate-y-2 group-focus-visible/btn:-translate-y-2 group-active/btn:-translate-y-px motion-reduce:duration-[100ms]">Buy now</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh06a-cap: #5ed39a;
  --color-tbh06a-cap: oklch(0.72 0.16 155);
  --color-tbh06a-side: #2e8f63;
  --color-tbh06a-side: oklch(0.5 0.13 155);
  --color-tbh06a-ink: #08351f;
  --color-tbh06a-ink: oklch(0.3 0.08 160);
  --color-tbh06a-stage: #eef6f1;
  --color-tbh06a-stage: oklch(0.96 0.015 160);
  --color-tbh06b-front: #ef8a4a;
  --color-tbh06b-front: oklch(0.68 0.18 40);
  --color-tbh06b-edge: #9c5122;
  --color-tbh06b-edge: oklch(0.42 0.14 40);
  --color-tbh06b-stage: #1a120c;
  --color-tbh06b-stage: oklch(0.2 0.03 50);
  --font-tbh06-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Nothing needs to stay CSS here: perspective, rotate and the shadow stacks are all
   expressible as utilities or arbitrary properties. */

.tbh-06-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-06a,
.tbh-06b {
  min-height: 100svh;
}
```
