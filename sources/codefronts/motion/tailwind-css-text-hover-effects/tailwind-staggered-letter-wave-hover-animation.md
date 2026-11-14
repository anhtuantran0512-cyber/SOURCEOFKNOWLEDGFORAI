---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-staggered-letter-wave-hover-animation/"
title: "Tailwind Staggered Letter Wave Hover Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A juice-brand wordmark whose letters jump in a wave: each letter sets style=\"--i:N\", and one class list on the parent — *:delay-[calc(var(--i)*45ms)] —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Staggered Letter Wave Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-staggered-letter-wave-hover-animation/

A juice-brand wordmark whose letters jump in a wave: each letter sets style="--i:N", and one class list on the parent — *:delay-[calc(var(--i)*45ms)] — staggers them all. Because it's transitions, not keyframes, leaving mid-wave reverses through the same stagger. The flavour pills reuse the trick at a smaller amplitude.
## HTML
```html
<section class="tth-10 w-full min-h-svh grid place-items-center bg-[linear-gradient(180deg,var(--color-tth10-sky),var(--color-tth10-bg)_55%,var(--color-tth10-sand))] px-5 py-14 font-tth10-sans text-tth10-ink" aria-label="Staggered letter wave demo">
  <div class="flex flex-col items-center gap-[clamp(16px,3vw,26px)] text-center">
    <p class="text-[12.5px] font-extrabold uppercase tracking-[0.26em] text-tth10-mut">Cold-pressed &middot; Bondi since 2019</p>
    <a id="tth10-top" href="#tth10-top" aria-label="SUNDAZE" class="group/wave inline-block rounded-[10px] px-[0.1em] pt-[0.18em] pb-[0.1em] font-tth10-display text-[clamp(56px,13.5vw,140px)] leading-none tracking-[-0.01em] no-underline focus-visible:outline-3 focus-visible:outline-offset-8 focus-visible:outline-tth10-acc">
      <span aria-hidden="true" class="*:inline-block *:not-italic *:transition-[translate,rotate,color] *:duration-500 *:ease-[cubic-bezier(.34,1.9,.5,1)] *:delay-[calc(var(--i)*45ms)] group-hover/wave:*:-translate-y-[0.22em] group-hover/wave:*:text-tth10-acc group-hover/wave:*:even:rotate-6 group-hover/wave:*:even:text-tth10-sea group-focus-visible/wave:*:-translate-y-[0.22em] group-focus-visible/wave:*:text-tth10-acc group-focus-visible/wave:*:even:rotate-6 group-focus-visible/wave:*:even:text-tth10-sea motion-reduce:*:transition-[color] motion-reduce:*:delay-0"><i style="--i:0">S</i><i style="--i:1">U</i><i style="--i:2">N</i><i style="--i:3">D</i><i style="--i:4">A</i><i style="--i:5">Z</i><i style="--i:6">E</i></span>
    </a>
    <nav class="flex flex-wrap justify-center gap-[clamp(10px,2.4vw,22px)]" aria-label="Flavours">
      <a href="#tth10-top" aria-label="Mango" class="group/pill grid min-h-12 place-items-center rounded-full border-[2.5px] border-tth10-ink bg-tth10-paper px-[22px] text-[17px] font-black no-underline shadow-[0_3px_0_var(--color-tth10-ink)] transition-[background-color,border-color,translate,box-shadow] duration-300 hover:-translate-y-0.5 hover:border-tth10-acc hover:bg-white hover:shadow-[0_5px_0_var(--color-tth10-acc)] focus-visible:border-tth10-acc focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth10-acc"><span aria-hidden="true" class="*:inline-block *:not-italic *:transition-[translate,color] *:duration-400 *:ease-[cubic-bezier(.34,1.9,.5,1)] *:delay-[calc(var(--i)*45ms)] group-hover/pill:*:-translate-y-[0.14em] group-hover/pill:*:text-tth10-acc group-focus-visible/pill:*:-translate-y-[0.14em] group-focus-visible/pill:*:text-tth10-acc motion-reduce:*:delay-0"><i style="--i:0">M</i><i style="--i:1">a</i><i style="--i:2">n</i><i style="--i:3">g</i><i style="--i:4">o</i></span></a>
      <a href="#tth10-top" aria-label="Guava" class="group/pill grid min-h-12 place-items-center rounded-full border-[2.5px] border-tth10-ink bg-tth10-paper px-[22px] text-[17px] font-black no-underline shadow-[0_3px_0_var(--color-tth10-ink)] transition-[background-color,border-color,translate,box-shadow] duration-300 hover:-translate-y-0.5 hover:border-tth10-acc hover:bg-white hover:shadow-[0_5px_0_var(--color-tth10-acc)] focus-visible:border-tth10-acc focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth10-acc"><span aria-hidden="true" class="*:inline-block *:not-italic *:transition-[translate,color] *:duration-400 *:ease-[cubic-bezier(.34,1.9,.5,1)] *:delay-[calc(var(--i)*45ms)] group-hover/pill:*:-translate-y-[0.14em] group-hover/pill:*:text-tth10-acc group-focus-visible/pill:*:-translate-y-[0.14em] group-focus-visible/pill:*:text-tth10-acc motion-reduce:*:delay-0"><i style="--i:0">G</i><i style="--i:1">u</i><i style="--i:2">a</i><i style="--i:3">v</i><i style="--i:4">a</i></span></a>
      <a href="#tth10-top" aria-label="Yuzu" class="group/pill grid min-h-12 place-items-center rounded-full border-[2.5px] border-tth10-ink bg-tth10-paper px-[22px] text-[17px] font-black no-underline shadow-[0_3px_0_var(--color-tth10-ink)] transition-[background-color,border-color,translate,box-shadow] duration-300 hover:-translate-y-0.5 hover:border-tth10-acc hover:bg-white hover:shadow-[0_5px_0_var(--color-tth10-acc)] focus-visible:border-tth10-acc focus-visible:outline-3 focus-visible:outline-offset-[3px] focus-visible:outline-tth10-acc"><span aria-hidden="true" class="*:inline-block *:not-italic *:transition-[translate,color] *:duration-400 *:ease-[cubic-bezier(.34,1.9,.5,1)] *:delay-[calc(var(--i)*45ms)] group-hover/pill:*:-translate-y-[0.14em] group-hover/pill:*:text-tth10-acc group-focus-visible/pill:*:-translate-y-[0.14em] group-focus-visible/pill:*:text-tth10-acc motion-reduce:*:delay-0"><i style="--i:0">Y</i><i style="--i:1">u</i><i style="--i:2">z</i><i style="--i:3">u</i></span></a>
    </nav>
    <p class="max-w-[54ch] text-[12.5px] leading-[1.7] text-tth10-mut">Hover, leave mid-wave, hover again &mdash; transitions reverse through the same stagger, which keyframes can't do. The real word lives in <code class="rounded bg-tth10-chip px-1.5 py-px font-tth10-mono text-[0.9em]">aria-label</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth10-sky: #fbefcd;
  --color-tth10-sky: oklch(0.95 0.05 90);
  --color-tth10-bg: #f6e3b4;
  --color-tth10-bg: oklch(0.93 0.06 85);
  --color-tth10-sand: #f2d39b;
  --color-tth10-sand: oklch(0.9 0.07 70);
  --color-tth10-paper: #fcf6e6;
  --color-tth10-paper: oklch(0.97 0.02 90);
  --color-tth10-chip: #ecd9a8;
  --color-tth10-chip: oklch(0.88 0.05 85);
  --color-tth10-ink: #5a2d10;
  --color-tth10-ink: oklch(0.32 0.08 50);
  --color-tth10-mut: #6c4a33;
  --color-tth10-mut: oklch(0.43 0.06 55);
  --color-tth10-acc: #e2532c;
  --color-tth10-acc: oklch(0.62 0.19 35);
  --color-tth10-sea: #2b8cc0;
  --color-tth10-sea: oklch(0.6 0.13 220);
  --font-tth10-display: 'Bagel Fat One', system-ui, sans-serif;
  --font-tth10-sans: 'Nunito', system-ui, sans-serif;
  --font-tth10-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-10 {
  width: 100%;
  min-height: 100svh;
}
```
