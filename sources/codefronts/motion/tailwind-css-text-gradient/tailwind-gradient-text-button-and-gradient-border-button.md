---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-button-and-gradient-border-button/"
title: "Tailwind Gradient Text Button & Gradient Border Button"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "Every gradient CTA in one panel: a ghost button with a gradient label, a true gradient-border button with rounded corners, and a filled gradient button whose…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text Button & Gradient Border Button
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-gradient-text-button-and-gradient-border-button/

Every gradient CTA in one panel: a ghost button with a gradient label, a true gradient-border button with rounded corners, and a filled gradient button whose colours slide on hover. The gradient border drops the original's mask-composite pseudo-element for a two-layer padding-box / border-box background &mdash; one element, no prefixes.
## HTML
```html
<section class="ttg-06 w-full min-h-svh grid place-items-center bg-ttg06-bg bg-[radial-gradient(80%_60%_at_50%_120%,var(--color-ttg06-glow),transparent)] px-5 py-14 font-ttg06-sans text-ttg06-ink" aria-labelledby="ttg06-title">
  <div class="w-full max-w-3xl">
    <h2 id="ttg06-title" class="text-[clamp(1.75rem,4.5vw,2.75rem)] font-extrabold tracking-[-0.03em]">Ready to <span class="bg-linear-to-r from-ttg06-a via-ttg06-b to-ttg06-c bg-clip-text text-transparent">launch?</span></h2>
    <p class="mt-2 text-[15px] text-ttg06-mut">Three CTA patterns, one gradient — pick the weight that fits the moment.</p>
    <div class="mt-10 grid gap-5 sm:grid-cols-3">
      <div class="flex flex-col gap-3 rounded-2xl border border-white/8 bg-white/[0.02] p-5">
        <p class="text-[11px] font-bold tracking-[0.14em] text-ttg06-mut uppercase">Ghost · gradient label</p>
        <a href="#" class="inline-flex min-h-12 items-center justify-center rounded-xl border border-white/12 text-[15px] font-bold transition hover:border-ttg06-b/50 hover:bg-white/[0.03] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg06-b motion-reduce:transition-none"><span class="bg-linear-to-r from-ttg06-a to-ttg06-c bg-clip-text text-transparent">Get started free</span></a>
        <a href="#" class="inline-flex min-h-11 items-center justify-center gap-1.5 rounded-xl text-sm font-semibold transition hover:bg-white/[0.04] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-ttg06-b motion-reduce:transition-none"><span class="bg-linear-to-r from-ttg06-a to-ttg06-c bg-clip-text text-transparent">Read the docs</span><span aria-hidden="true" class="text-ttg06-c">&rarr;</span></a>
      </div>
      <div class="flex flex-col gap-3 rounded-2xl border border-white/8 bg-white/[0.02] p-5">
        <p class="text-[11px] font-bold tracking-[0.14em] text-ttg06-mut uppercase">Gradient border</p>
        <a href="#" class="inline-flex min-h-12 items-center justify-center rounded-xl border-2 border-transparent text-[15px] font-bold transition [background:linear-gradient(var(--color-ttg06-surface),var(--color-ttg06-surface))_padding-box,linear-gradient(90deg,var(--color-ttg06-a),var(--color-ttg06-c))_border-box] hover:shadow-[0_10px_30px_-10px_var(--color-ttg06-b)] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg06-b motion-reduce:transition-none"><span class="bg-linear-to-r from-ttg06-a to-ttg06-c bg-clip-text text-transparent">Start building</span></a>
        <a href="#" class="inline-flex min-h-11 items-center justify-center rounded-full border-[1.5px] border-transparent text-sm font-semibold text-ttg06-ink transition [background:linear-gradient(var(--color-ttg06-surface),var(--color-ttg06-surface))_padding-box,linear-gradient(90deg,var(--color-ttg06-a),var(--color-ttg06-c))_border-box] hover:text-white active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg06-b motion-reduce:transition-none">Talk to sales</a>
      </div>
      <div class="flex flex-col gap-3 rounded-2xl border border-white/8 bg-white/[0.02] p-5">
        <p class="text-[11px] font-bold tracking-[0.14em] text-ttg06-mut uppercase">Filled · sliding</p>
        <a href="#" class="inline-flex min-h-12 items-center justify-center rounded-xl bg-linear-to-r from-ttg06-a via-ttg06-b to-ttg06-c bg-[length:200%_100%] bg-left text-[15px] font-bold text-ttg06-bg transition-[background-position,box-shadow,transform] duration-500 hover:bg-right hover:shadow-[0_12px_32px_-10px_var(--color-ttg06-b)] active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg06-b motion-reduce:transition-none">Upgrade to Pro</a>
        <a href="#" class="inline-flex min-h-11 items-center justify-center rounded-xl bg-linear-to-r from-ttg06-a via-ttg06-b to-ttg06-c bg-[length:200%_100%] bg-left text-sm font-bold text-ttg06-bg transition-[background-position,transform] duration-500 hover:bg-right active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg06-b motion-reduce:transition-none">Learn more</a>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg06-bg: #0b0b0f;
  --color-ttg06-bg: oklch(0.15 0.006 285);
  --color-ttg06-surface: #121218;
  --color-ttg06-surface: oklch(0.18 0.01 285);
  --color-ttg06-glow: #4a1d1d66;
  --color-ttg06-glow: oklch(0.3 0.09 25 / 0.4);
  --color-ttg06-ink: #f2f4f7;
  --color-ttg06-ink: oklch(0.96 0.005 260);
  --color-ttg06-mut: #a0a6b3;
  --color-ttg06-mut: oklch(0.73 0.018 265);
  --color-ttg06-a: #f8b13a;
  --color-ttg06-a: oklch(0.81 0.15 75);
  --color-ttg06-b: #f2524a;
  --color-ttg06-b: oklch(0.65 0.21 27);
  --color-ttg06-c: #ef4f9d;
  --color-ttg06-c: oklch(0.66 0.22 355);
  --font-ttg06-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-06 {
  width: 100%;
  min-height: 100svh;
}
```
