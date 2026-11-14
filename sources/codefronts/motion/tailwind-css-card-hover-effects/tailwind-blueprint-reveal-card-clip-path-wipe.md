---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-blueprint-reveal-card-clip-path-wipe/"
title: "Tailwind Blueprint Reveal Card with Circular clip-path Wipe"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A product card that wipes into a technical blueprint &mdash; grid paper, dimension lines, tolerances &mdash; via a circle that expands from the top-right…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blueprint Reveal Card with Circular clip-path Wipe
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-blueprint-reveal-card-clip-path-wipe/

A product card that wipes into a technical blueprint &mdash; grid paper, dimension lines, tolerances &mdash; via a circle that expands from the top-right corner. clip-path: circle() animates cleanly because only the radius changes, and that single-value interpolation is what makes the wipe smooth.
## HTML
```html
<section class="tch-28 w-full min-h-svh grid place-items-center bg-tch28-bg font-tch28-mono p-8">
  <article tabindex="0" class="group relative w-[340px] h-[440px] rounded-md overflow-hidden cursor-pointer outline-none bg-tch28-paper border border-tch28-edge shadow-[0_16px_36px_rgb(30_50_80/0.15)] focus-visible:outline-2 focus-visible:outline-tch28-blue focus-visible:outline-offset-4">
    <div class="absolute inset-0 z-1 p-[2.4rem] flex flex-col justify-between text-tch28-ink bg-[radial-gradient(circle_at_70%_20%,#f0f3f7,#fdfdfb_60%)] transition-opacity duration-500 group-hover:opacity-0 group-focus-visible:opacity-0">
      <span class="text-[0.72rem] tracking-[0.16em] text-tch28-mut">MODEL · ARC-01</span>
      <div class="size-[130px] mx-auto my-4 rounded-[50%_50%_50%_12px] bg-[linear-gradient(145deg,#2d6cdf,#16306b)] shadow-[0_14px_30px_rgb(40_80_160/0.35)]"></div>
      <div>
        <h2 class="font-tch28-display font-bold text-[2rem] leading-none">Arc Pendant</h2>
        <p class="text-[0.82rem] leading-[1.6] text-tch28-mut mt-1.5">Hand-blown matte ceramic lamp.</p>
      </div>
    </div>
    <div class="absolute inset-0 z-2 p-[2.4rem] flex flex-col justify-between text-tch28-bink bg-tch28-blue bg-[linear-gradient(rgb(255_255_255/0.12)_1px,transparent_1px),linear-gradient(90deg,rgb(255_255_255/0.12)_1px,transparent_1px)] bg-[length:22px_22px] [clip-path:circle(0%_at_100%_0%)] transition-[clip-path] duration-600 ease-[cubic-bezier(0.65,0,0.35,1)] group-hover:[clip-path:circle(150%_at_100%_0%)] group-focus-visible:[clip-path:circle(150%_at_100%_0%)] motion-reduce:transition-none">
      <span class="text-[0.72rem] tracking-[0.16em]">DRAWING № 01 — REV C</span>
      <div class="relative size-[130px] mx-auto my-4 rounded-[50%_50%_50%_12px] border-[1.5px] border-tch28-line before:content-[''] before:absolute before:-inset-x-8 before:top-1/2 before:h-px before:bg-[repeating-linear-gradient(90deg,#6f9aff_0_6px,transparent_6px_10px)] after:content-[''] after:absolute after:-inset-y-8 after:left-1/2 after:w-px after:bg-[repeating-linear-gradient(0deg,#6f9aff_0_6px,transparent_6px_10px)]"></div>
      <div>
        <h2 class="font-tch28-display font-bold text-[1.6rem] leading-[1.05]">Arc Pendant<br>Cross-Section</h2>
        <p class="text-[0.74rem] leading-[1.7] text-tch28-spec mt-1.5">Ø 130mm · cord 1.8m<br>E27 · 2700K · matte glaze<br>TOL ±0.5mm</p>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch28-bg: #e9ebee;
  --color-tch28-bg: oklch(0.93 0.004 250);
  --color-tch28-paper: #fdfdfb;
  --color-tch28-paper: oklch(0.99 0.003 95);
  --color-tch28-edge: #d4d8de;
  --color-tch28-edge: oklch(0.87 0.006 250);
  --color-tch28-ink: #1a2533;
  --color-tch28-ink: oklch(0.25 0.02 250);
  --color-tch28-mut: #5a6a7d;
  --color-tch28-mut: oklch(0.5 0.03 250);
  --color-tch28-blue: #0d3b8c;
  --color-tch28-blue: oklch(0.36 0.16 265);
  --color-tch28-bink: #cfe0ff;
  --color-tch28-bink: oklch(0.89 0.05 260);
  --color-tch28-spec: #aecaff;
  --color-tch28-spec: oklch(0.82 0.07 260);
  --color-tch28-line: #9dc0ff;
  --color-tch28-line: oklch(0.79 0.09 260);
  --font-tch28-mono: 'Spline Sans Mono', ui-monospace, monospace;
  --font-tch28-display: 'Archivo', system-ui, sans-serif;
}

.tch-28 {
  width: 100%;
  min-height: 100svh;
}
```
