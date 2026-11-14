---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-neo-brutalist-cyberpunk-button-glow-effects/"
title: "Tailwind Neo-Brutalist & Cyberpunk Button Glow Effects"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A loud neo-brutalist CTA: flat fill, thick solid border and a hard blur-free offset shadow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neo-Brutalist & Cyberpunk Button Glow Effects
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-neo-brutalist-cyberpunk-button-glow-effects/

A loud neo-brutalist CTA: flat fill, thick solid border and a hard blur-free offset shadow. On hover it snaps onto its shadow and the shadow flips to saturated neon &mdash; a hard, instant snap, not a soft glow. The port makes the effect's one invariant visible: the snap distance and the shadow offset are the same number.
## HTML
```html
<div class="tbh-11-group w-full min-h-svh flex flex-wrap">
<section class="tbh-11a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh11-sans bg-tbh11a-stage" aria-label="Neo-brutalist neon button">
  <button type="button" class="cursor-pointer rounded-none border-[3px] border-tbh11-ink px-[38px] py-[17px] text-[17px] font-extrabold uppercase tracking-[0.02em] text-tbh11-ink bg-white shadow-[7px_7px_0_var(--color-tbh11-ink)] transition-[translate,scale,box-shadow] duration-[120ms] ease-out hover:translate-x-[7px] hover:translate-y-[7px] hover:shadow-[0_0_0_var(--color-tbh11-ink),0_0_22px_2px_var(--color-tbh11a-mag),0_0_34px_6px_color-mix(in_oklab,var(--color-tbh11a-cyan)_70%,transparent)] focus-visible:translate-x-[7px] focus-visible:translate-y-[7px] focus-visible:shadow-[0_0_0_var(--color-tbh11-ink),0_0_22px_2px_var(--color-tbh11a-mag)] active:scale-[.98] focus-visible:outline-3 focus-visible:outline-tbh11-ink focus-visible:outline-offset-[5px] motion-reduce:transition-[box-shadow] motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">
    Subscribe
  </button>
</section>
<section class="tbh-11b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh11-sans bg-tbh11b-stage" aria-label="Brutalist sticker button">
  <button type="button" class="cursor-pointer rounded-[10px] border-[3px] border-tbh11-ink px-10 py-[17px] text-[17px] font-extrabold uppercase text-tbh11-ink bg-tbh11b-lime shadow-[-6px_6px_0_var(--color-tbh11-ink)] transition-[translate,scale,box-shadow,background-color] duration-[120ms] ease-out hover:-translate-x-[6px] hover:translate-y-[6px] hover:bg-tbh11b-hot hover:shadow-[0_0_0_var(--color-tbh11-ink)] focus-visible:-translate-x-[6px] focus-visible:translate-y-[6px] focus-visible:bg-tbh11b-hot focus-visible:shadow-[0_0_0_var(--color-tbh11-ink)] active:scale-[.98] focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-[5px] motion-reduce:transition-[background-color,box-shadow] motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0">
    Get access
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh11-ink: #111111;
  --color-tbh11-ink: oklch(0.15 0 0);
  --color-tbh11a-stage: #f5e94a;
  --color-tbh11a-stage: oklch(0.92 0.18 100);
  --color-tbh11a-mag: #ff2bd6;
  --color-tbh11a-mag: oklch(0.7 0.28 330);
  --color-tbh11a-cyan: #22e3ff;
  --color-tbh11a-cyan: oklch(0.85 0.15 210);
  --color-tbh11b-stage: #111111;
  --color-tbh11b-stage: oklch(0.15 0 0);
  --color-tbh11b-lime: #4df08a;
  --color-tbh11b-lime: oklch(0.85 0.2 150);
  --color-tbh11b-hot: #ffe14d;
  --color-tbh11b-hot: oklch(0.91 0.17 95);
  --font-tbh11-sans: 'Space Grotesk', ui-monospace, sans-serif;
}
/* Nothing stays CSS: two shadow stacks, two translates, one colour flip. */

.tbh-11-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-11a,
.tbh-11b {
  min-height: 100svh;
}
```
