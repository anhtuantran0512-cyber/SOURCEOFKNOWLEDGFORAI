---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-animated-gradient-border-draw-card/"
title: "Tailwind Animated Conic Gradient Border Card with @property"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A dark edge-compute card where a multi-colour conic gradient traces a live circuit around the border on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Conic Gradient Border Card with @property
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-animated-gradient-border-draw-card/

A dark edge-compute card where a multi-colour conic gradient traces a live circuit around the border on hover. This is the port's honest limit: @property and @keyframes must stay in the stylesheet, but --animate-tch08-spin turns the result into one animate-tch08-spin utility, and the play-state gating happens in the class list.
## HTML
```html
<section class="tch-08 w-full min-h-svh grid place-items-center bg-tch08-bg font-tch08-mono p-8">
  <article class="group relative w-[340px] h-[420px] rounded-[20px] bg-tch08-card isolate cursor-pointer
    before:content-[''] before:absolute before:inset-0 before:rounded-[inherit] before:p-[2px] before:opacity-0 before:transition-opacity before:duration-400 group-hover:before:opacity-100 group-focus-within:before:opacity-100 before:bg-[conic-gradient(from_var(--tch08-angle,0deg),transparent_0deg,transparent_70deg,var(--color-tch08-a)_130deg,var(--color-tch08-b)_200deg,var(--color-tch08-c)_250deg,transparent_320deg)] before:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[-webkit-mask-composite:xor] before:[mask-composite:exclude] before:animate-tch08-spin before:[animation-play-state:paused] group-hover:before:[animation-play-state:running] motion-reduce:before:animate-none
    after:content-[''] after:absolute after:inset-0 after:rounded-[inherit] after:border-2 after:border-white/6 after:pointer-events-none">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch08-ink">
      <span class="text-[0.7rem] tracking-[0.3em] uppercase text-tch08-mut">/ Edge Compute</span>
      <h2 class="font-tch08-display font-extrabold text-[2.3rem] leading-[1.05] bg-linear-to-r from-tch08-a via-tch08-b to-tch08-c bg-clip-text text-transparent">Halo<br>Runtime</h2>
      <p class="text-[0.82rem] leading-[1.65] text-tch08-body">A serverless mesh that traces a live circuit around every active deployment region.</p>
      <a href="#" class="flex items-center justify-between min-h-11 text-[0.72rem] text-tch08-mut no-underline border-t border-white/8 pt-4 transition-colors duration-200 hover:text-tch08-ink focus-visible:outline-2 focus-visible:outline-tch08-a focus-visible:outline-offset-2"><span>v3.2.0</span><span>99.99% SLA</span></a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tch08-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@keyframes tch08-spin {
  to {
    --tch08-angle: 360deg;
  }
}

@theme {
  --color-tch08-bg: #07080d;
  --color-tch08-bg: oklch(0.09 0.01 265);
  --color-tch08-card: #0d0f17;
  --color-tch08-card: oklch(0.14 0.015 265);
  --color-tch08-ink: #e8eaf2;
  --color-tch08-ink: oklch(0.93 0.008 265);
  --color-tch08-body: #9499ab;
  --color-tch08-body: oklch(0.68 0.015 265);
  --color-tch08-mut: #6f7488;
  --color-tch08-mut: oklch(0.54 0.02 265);
  --color-tch08-a: #00f0ff;
  --color-tch08-a: oklch(0.87 0.14 200);
  --color-tch08-b: #7b5cff;
  --color-tch08-b: oklch(0.58 0.24 285);
  --color-tch08-c: #ff4dd8;
  --color-tch08-c: oklch(0.7 0.27 335);
  --font-tch08-mono: 'DM Mono', ui-monospace, monospace;
  --font-tch08-display: 'Syne', system-ui, sans-serif;
  --animate-tch08-spin: tch08-spin 4s linear infinite;
}

.tch-08 {
  width: 100%;
  min-height: 100svh;
}
```
