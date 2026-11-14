---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-conic-gradient-ring-hero/"
title: "Animated Conic Gradient Ring Hero in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A solar-corona ring orbiting a glowing core — a conic gradient whose start angle is animated through a registered @property, masked into a ring that scales…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Conic Gradient Ring Hero in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-conic-gradient-ring-hero/

A solar-corona ring orbiting a glowing core — a conic gradient whose start angle is animated through a registered @property, masked into a ring that scales with its container. Gold and ember on jet black, the AI / hardware launch treatment.
## HTML
```html
<section class="ths-30 relative isolate grid w-full min-h-svh items-center gap-10 overflow-hidden bg-ths30-bg px-5 py-16 font-ths30-sans text-ths30-ink sm:px-12 lg:grid-cols-2 lg:gap-14" aria-label="Conic gradient ring hero">
  <div aria-hidden="true" class="relative grid min-h-[340px] place-items-center">
    <div class="absolute size-[min(520px,90vw)] rounded-full bg-[radial-gradient(closest-side,rgb(255_107_26/0.18),transparent)]"></div>
    <div class="size-[min(340px,72vw)] animate-ths30-orbit rounded-full bg-[conic-gradient(from_var(--ths30-a),var(--color-ths30-gold),var(--color-ths30-ember),var(--color-ths30-red),var(--color-ths30-ember),var(--color-ths30-gold))] blur-[6px] [mask:radial-gradient(closest-side,transparent_60%,#000_62%,#000_97%,transparent_100%)] motion-reduce:animate-none"></div>
    <div class="absolute size-[min(210px,44vw)] rounded-full bg-[radial-gradient(circle_at_40%_35%,var(--color-ths30-gold),var(--color-ths30-ember)_35%,var(--color-ths30-red)_65%,#6b1a08)] shadow-[0_0_90px_rgb(255_107_26/0.45)]"></div>
  </div>
  <div class="max-w-lg">
    <span class="inline-flex items-center gap-2 rounded-full border border-ths30-gold/40 bg-ths30-gold/10 px-3 py-1 font-ths30-mono text-[11.5px] tracking-[0.16em] text-ths30-gold uppercase">Solar v3 · shipping Q1</span>
    <h1 class="mt-5 font-ths30-display text-[clamp(34px,4.6vw,54px)] leading-[1.06] font-bold tracking-[-0.03em] text-balance">Compute that <em class="bg-linear-to-r from-ths30-gold to-ths30-ember bg-clip-text pr-1 text-transparent">moves at the speed of light.</em></h1>
    <p class="mt-5 max-w-md text-[17px] leading-relaxed text-ths30-mut">The new generation of inference cards. 3× the throughput. Half the heat.</p>
    <dl class="mt-7 grid max-w-sm grid-cols-3 gap-4 border-y border-white/10 py-5">
      <div><dt class="text-xs text-ths30-mut">Throughput</dt><dd class="mt-1 font-ths30-display text-2xl font-bold">3×</dd></div>
      <div><dt class="text-xs text-ths30-mut">TDP</dt><dd class="mt-1 font-ths30-display text-2xl font-bold">150W</dd></div>
      <div><dt class="text-xs text-ths30-mut">Memory</dt><dd class="mt-1 font-ths30-display text-2xl font-bold">96GB</dd></div>
    </dl>
    <div class="mt-8 flex flex-wrap items-center gap-3">
      <a href="#preorder" class="inline-flex min-h-12 items-center rounded-full bg-linear-135 from-ths30-ember to-ths30-red px-7 text-[15px] font-extrabold text-ths30-bg shadow-[0_14px_36px_rgb(255_107_26/0.35)] transition hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths30-gold motion-reduce:transition-none">Pre-order →</a>
      <a href="#specs" class="inline-flex min-h-12 items-center rounded-full px-5 text-[15px] font-semibold text-ths30-ink ring-1 ring-white/20 transition hover:ring-ths30-gold focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths30-gold">Full specs</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --ths30-a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@theme {
  --color-ths30-bg: #0a0805;
  --color-ths30-bg: oklch(0.136 0.009 82.5);
  --color-ths30-ink: #f8e8c8;
  --color-ths30-ink: oklch(0.936 0.045 84.6);
  --color-ths30-mut: #c4a585;
  --color-ths30-mut: oklch(0.741 0.057 67.7);
  --color-ths30-gold: #f8d248;
  --color-ths30-gold: oklch(0.873 0.155 93.2);
  --color-ths30-ember: #ff6b1a;
  --color-ths30-ember: oklch(0.703 0.198 43.4);
  --color-ths30-red: #d63a18;
  --color-ths30-red: oklch(0.581 0.198 33.4);
  --font-ths30-display: 'Space Grotesk', system-ui, sans-serif;
  --font-ths30-sans: 'Geist', system-ui, sans-serif;
  --font-ths30-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths30-orbit: ths30-orbit 12s linear infinite;

  @keyframes ths30-orbit {
    to {
      --ths30-a: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-30 {
  width: 100%;
  min-height: 100svh;
}
```
