---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-with-outline-stroke/"
title: "Tailwind Gradient Text with Outline Stroke"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "Stroke-only, fill-only and stroke-plus-fill side by side, plus a hollow display word whose outline fills with gradient on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text with Outline Stroke
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-with-outline-stroke/

Stroke-only, fill-only and stroke-plus-fill side by side, plus a hollow display word whose outline fills with gradient on hover. Tailwind has no stroke-text utility, so [-webkit-text-stroke:2px_…] and [paint-order:stroke_fill] arbitrary properties do the work &mdash; right in the class list.
## HTML
```html
<section class="ttg-16 w-full min-h-svh grid place-items-center bg-ttg16-bg px-5 py-16 font-ttg16-sans text-ttg16-ink" aria-label="Gradient text with outline stroke demo">
  <div class="w-full max-w-3xl">
    <p class="font-ttg16-mono text-[11px] tracking-[0.16em] text-ttg16-mut uppercase">Stroke + gradient fill · hover the outline</p>
    <h1 class="mt-4 w-fit cursor-default bg-linear-to-r from-ttg16-a via-ttg16-b to-ttg16-c bg-[length:0%_100%] bg-no-repeat bg-clip-text font-ttg16-display text-[clamp(3.5rem,13vw,7.5rem)] leading-[0.95] tracking-[0.02em] text-transparent transition-[background-size] duration-700 ease-out [-webkit-text-stroke:2px_var(--color-ttg16-a)] hover:bg-[length:100%_100%] motion-reduce:transition-none">OUTLINE</h1>
    <h2 class="mt-3 w-fit bg-linear-to-r from-ttg16-a via-ttg16-b to-ttg16-c bg-clip-text text-[clamp(1.6rem,5vw,2.8rem)] font-bold tracking-[-0.02em] text-transparent [-webkit-text-stroke:1px_var(--color-ttg16-stroke)] [paint-order:stroke_fill]">Gradient fill + stroke</h2>
    <div class="mt-10 grid gap-4 sm:grid-cols-3">
      <figure class="grid gap-3 rounded-2xl border border-white/8 bg-white/[0.025] p-5">
        <span class="font-ttg16-display text-6xl text-transparent [-webkit-text-stroke:2px_var(--color-ttg16-a)]">Type</span>
        <figcaption class="font-ttg16-mono text-[11.5px] text-ttg16-mut">Stroke only<br><span class="text-ttg16-ink/80">text-transparent + stroke</span></figcaption>
      </figure>
      <figure class="grid gap-3 rounded-2xl border border-white/8 bg-white/[0.025] p-5">
        <span class="w-fit bg-linear-to-r from-ttg16-b to-ttg16-c bg-clip-text font-ttg16-display text-6xl text-transparent">Type</span>
        <figcaption class="font-ttg16-mono text-[11.5px] text-ttg16-mut">Fill only<br><span class="text-ttg16-ink/80">bg-clip-text</span></figcaption>
      </figure>
      <figure class="grid gap-3 rounded-2xl border border-white/8 bg-white/[0.025] p-5">
        <span class="w-fit bg-linear-to-r from-ttg16-a via-ttg16-b to-ttg16-c bg-clip-text font-ttg16-display text-6xl text-transparent [-webkit-text-stroke:3px_var(--color-ttg16-stroke)] [paint-order:stroke_fill]">Type</span>
        <figcaption class="font-ttg16-mono text-[11.5px] text-ttg16-mut">Stroke + fill<br><span class="text-ttg16-ink/80">[paint-order:stroke_fill]</span></figcaption>
      </figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg16-bg: #04070b;
  --color-ttg16-bg: oklch(0.13 0.012 250);
  --color-ttg16-ink: #eef3f8;
  --color-ttg16-ink: oklch(0.96 0.008 245);
  --color-ttg16-mut: #98a3b3;
  --color-ttg16-mut: oklch(0.72 0.025 255);
  --color-ttg16-stroke: #ffffff59;
  --color-ttg16-stroke: oklch(1 0 0 / 0.35);
  --color-ttg16-a: #38bdf8;
  --color-ttg16-a: oklch(0.77 0.14 230);
  --color-ttg16-b: #8b8ff7;
  --color-ttg16-b: oklch(0.68 0.15 280);
  --color-ttg16-c: #ea7cf8;
  --color-ttg16-c: oklch(0.75 0.19 320);
  --font-ttg16-display: 'Archivo Black', system-ui, sans-serif;
  --font-ttg16-sans: 'Geist', system-ui, sans-serif;
  --font-ttg16-mono: 'Geist Mono', ui-monospace, monospace;
}

.ttg-16 {
  width: 100%;
  min-height: 100svh;
}
```
