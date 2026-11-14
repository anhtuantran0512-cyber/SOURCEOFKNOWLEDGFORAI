---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/bold-minimalist-gradient-heading-in-tailwind-css/"
title: "Bold Minimalist Gradient Heading in Tailwind CSS"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "An editorial type specimen: three font-black words, each with its own dual-tone gradient, on a white page."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bold Minimalist Gradient Heading in Tailwind CSS
Source: https://codefronts.com/motion/tailwind-css-text-gradient/bold-minimalist-gradient-heading-in-tailwind-css/

An editorial type specimen: three font-black words, each with its own dual-tone gradient, on a white page. w-fit is the quiet hero &mdash; it shrinks each block heading to its glyphs so the gradient spans the word, not the viewport.
## HTML
```html
<section class="ttg-04 w-full min-h-svh grid place-items-center bg-ttg04-bg px-8 py-16 font-ttg04-sans text-ttg04-ink" aria-label="Bold minimalist gradient heading demo">
  <div class="w-full max-w-3xl">
    <p class="flex items-center gap-3 font-ttg04-mono text-xs tracking-[0.14em] text-ttg04-mut uppercase"><span aria-hidden="true" class="h-px w-8 bg-ttg04-ink"></span>Type scale specimen</p>
    <div class="mt-8 grid gap-1">
      <div class="flex items-start gap-5"><span aria-hidden="true" class="mt-[1.4em] font-ttg04-mono text-[11px] text-ttg04-mut">01</span><h2 class="w-fit bg-linear-to-r from-ttg04-a1 to-ttg04-b1 bg-clip-text pb-[0.08em] text-[clamp(4rem,15vw,8rem)] leading-[0.9] font-black tracking-[-0.05em] text-transparent">Clarity</h2></div>
      <div class="flex items-start gap-5"><span aria-hidden="true" class="mt-[1.1em] font-ttg04-mono text-[11px] text-ttg04-mut">02</span><h2 class="w-fit bg-linear-to-r from-ttg04-a2 to-ttg04-b2 bg-clip-text pb-[0.08em] text-[clamp(3rem,11vw,5.75rem)] leading-[0.9] font-black tracking-[-0.045em] text-transparent">Purpose</h2></div>
      <div class="flex items-start gap-5"><span aria-hidden="true" class="mt-[0.9em] font-ttg04-mono text-[11px] text-ttg04-mut">03</span><h2 class="w-fit bg-linear-to-r from-ttg04-a3 to-ttg04-b3 bg-clip-text pb-[0.08em] text-[clamp(2.1rem,7.5vw,4rem)] leading-[0.9] font-black tracking-[-0.04em] text-transparent">Impact</h2></div>
    </div>
    <div class="mt-10 grid gap-6 border-t border-ttg04-line pt-7 sm:grid-cols-[1fr_auto]">
      <p class="max-w-md text-[15px]/[1.7] text-ttg04-mut text-pretty">Dual-tone gradients on heavy weights create editorial impact without imagery. Each ramp travels left to right across exactly one word.</p>
      <p aria-hidden="true" class="self-end font-ttg04-mono text-[11.5px] text-ttg04-mut">w-fit · font-black · bg-clip-text</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg04-bg: #ffffff;
  --color-ttg04-bg: oklch(1 0 0);
  --color-ttg04-ink: #12131a;
  --color-ttg04-ink: oklch(0.19 0.01 275);
  --color-ttg04-mut: #5c6273;
  --color-ttg04-mut: oklch(0.49 0.025 265);
  --color-ttg04-line: #e6e7ec;
  --color-ttg04-line: oklch(0.93 0.006 270);
  --color-ttg04-a1: #1e1b4b;
  --color-ttg04-a1: oklch(0.26 0.1 280);
  --color-ttg04-b1: #6366f1;
  --color-ttg04-b1: oklch(0.59 0.2 277);
  --color-ttg04-a2: #312e81;
  --color-ttg04-a2: oklch(0.36 0.14 279);
  --color-ttg04-b2: #c026d3;
  --color-ttg04-b2: oklch(0.59 0.25 322);
  --color-ttg04-a3: #0f172a;
  --color-ttg04-a3: oklch(0.21 0.04 265);
  --color-ttg04-b3: #0ea5e9;
  --color-ttg04-b3: oklch(0.68 0.15 237);
  --font-ttg04-sans: 'Archivo', system-ui, sans-serif;
  --font-ttg04-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.ttg-04 {
  width: 100%;
  min-height: 100svh;
}
```
