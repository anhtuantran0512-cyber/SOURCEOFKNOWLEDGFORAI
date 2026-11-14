---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-3d-press-plunger-key-button-effect/"
title: "Tailwind 3D Press Plunger Key Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A deeply tactile CTA on a thick 3D base like a plunger key: on press it drives straight down while the base compresses in lockstep &mdash; a vertical plunge,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Press Plunger Key Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-3d-press-plunger-key-button-effect/

A deeply tactile CTA on a thick 3D base like a plunger key: on press it drives straight down while the base compresses in lockstep &mdash; a vertical plunge, distinct from entry 06's isometric tilt. The invariant is arithmetic, and the port puts all three stages where you can check it.
## HTML
```html
<div class="tbh-35-group w-full min-h-svh flex flex-wrap">
<section class="tbh-35a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-[60px] font-tbh35-sans bg-tbh35a-stage" aria-label="3D plunger press button">
  <button type="button" class="cursor-pointer border-0 rounded-[14px] px-[42px] py-4 text-[17px] font-extrabold text-white bg-tbh35a-cap -translate-y-2 shadow-[0_8px_0_var(--color-tbh35a-base),0_14px_18px_-6px_oklch(0_0_0/0.5)] transition-[translate,box-shadow] duration-[120ms] ease-out hover:-translate-y-2.5 hover:shadow-[0_10px_0_var(--color-tbh35a-base),0_18px_22px_-6px_oklch(0_0_0/0.5)] focus-visible:-translate-y-2.5 focus-visible:shadow-[0_10px_0_var(--color-tbh35a-base),0_18px_22px_-6px_oklch(0_0_0/0.5)] active:-translate-y-0.5 active:shadow-[0_2px_0_var(--color-tbh35a-base),0_6px_10px_-4px_oklch(0_0_0/0.5)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[5px] motion-reduce:transition-[box-shadow] motion-reduce:duration-100">
    Confirm
  </button>
</section>
<section class="tbh-35b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-[60px] font-tbh35-mono bg-tbh35b-stage" aria-label="Chunky keycap button">
  <button type="button" class="cursor-pointer border-0 rounded-xl px-10 py-[18px] text-base font-extrabold text-tbh35b-ink bg-[linear-gradient(180deg,white,var(--color-tbh35b-cap))] -translate-y-2.5 shadow-[0_10px_0_var(--color-tbh35b-base),inset_0_2px_0_oklch(1_0_0),0_16px_20px_-6px_oklch(0_0_0/0.5)] transition-[translate,box-shadow] duration-100 ease-out active:-translate-y-0.5 active:shadow-[0_2px_0_var(--color-tbh35b-base),inset_0_2px_0_oklch(1_0_0),0_6px_10px_-4px_oklch(0_0_0/0.5)] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[5px] motion-reduce:transition-[box-shadow]">
    Enter &#9166;
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh35a-cap: #e0563c;
  --color-tbh35a-cap: oklch(0.62 0.2 25);
  --color-tbh35a-base: #8f3220;
  --color-tbh35a-base: oklch(0.4 0.15 25);
  --color-tbh35a-stage: #160a08;
  --color-tbh35a-stage: oklch(0.17 0.03 25);
  --color-tbh35b-cap: #dfe2ea;
  --color-tbh35b-cap: oklch(0.9 0.02 260);
  --color-tbh35b-base: #9298a8;
  --color-tbh35b-base: oklch(0.62 0.03 260);
  --color-tbh35b-ink: #2a2f42;
  --color-tbh35b-ink: oklch(0.32 0.03 265);
  --color-tbh35b-stage: #1c2030;
  --color-tbh35b-stage: oklch(0.25 0.03 265);
  --font-tbh35-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tbh35-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Nothing stays CSS: three shadow stacks and three matching translates. */

.tbh-35-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-35a,
.tbh-35b {
  min-height: 100svh;
}
```
