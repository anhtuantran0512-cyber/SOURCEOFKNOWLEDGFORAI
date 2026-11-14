---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-magazine-cover-hero-section/"
title: "Magazine Cover Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A print-magazine cover — issue line, oversized italic serif headline, a vertical spine label, a foil-stamped issue number and a double-rule offset shadow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Magazine Cover Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-magazine-cover-hero-section/

A print-magazine cover — issue line, oversized italic serif headline, a vertical spine label, a foil-stamped issue number and a double-rule offset shadow. Plum and champagne on ruled linen, with cover lines that read like a real masthead.
## HTML
```html
<section class="ths-11 grid w-full min-h-svh place-items-center bg-ths11-bg bg-[repeating-linear-gradient(0deg,transparent_0_47px,rgb(60_40_80/0.05)_47px_48px)] px-5 py-14 font-ths11-serif text-ths11-ink sm:px-10" aria-label="Magazine cover hero">
  <div class="relative w-full max-w-[46rem] border border-ths11-ink bg-ths11-paper py-[clamp(28px,4vw,56px)] pr-[clamp(24px,4vw,56px)] pl-[clamp(52px,7vw,80px)] shadow-[12px_12px_0_var(--color-ths11-gold),12px_12px_0_1px_var(--color-ths11-ink)]">
    <span class="absolute top-1/2 left-4 -translate-y-1/2 border-y border-ths11-wine px-1 py-3.5 font-ths11-mono text-[10.5px] tracking-[0.32em] whitespace-nowrap text-ths11-wine [writing-mode:vertical-rl]">Vol. XII · No. 47 · Spring</span>
    <span aria-hidden="true" class="absolute top-3 right-6 bg-linear-to-br from-ths11-gold via-ths11-foil to-ths11-gold bg-clip-text font-ths11-serif text-[clamp(44px,6vw,60px)] font-black text-transparent italic drop-shadow-[1px_1px_0_var(--color-ths11-ink)]">04</span>
    <header class="flex flex-wrap items-baseline gap-x-6 gap-y-1 border-b border-ths11-ink pb-4">
      <span class="font-ths11-mono text-[10.5px] font-bold tracking-[0.24em]">SPRING 2026 · INDEX NO. 04</span>
      <span class="font-ths11-mono text-[10.5px] tracking-[0.18em] text-ths11-mut">$14 US / £11 UK</span>
    </header>
    <h1 class="mt-6 text-[clamp(42px,7.4vw,84px)] leading-[0.94] font-semibold tracking-[-0.025em]">The Quiet <em class="block text-[1.2em] font-bold text-ths11-wine">Revolution</em> of slow type.</h1>
    <p class="mt-6 max-w-[29rem] font-ths11-body text-xl/snug text-ths11-mut italic">Why every serious editorial brand is going back to serifs, italics, and a single column wide enough to think in.</p>
    <div class="mt-8 flex flex-wrap items-end justify-between gap-6">
      <a href="#read" class="inline-flex min-h-11 items-center border-b-2 border-ths11-ink font-ths11-mono text-xs font-bold tracking-[0.16em] transition hover:border-ths11-wine hover:text-ths11-wine focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths11-wine">READ THE ISSUE →</a>
      <ul class="space-y-1 text-right font-ths11-mono text-[10.5px] tracking-[0.12em] text-ths11-mut">
        <li>P. 18 — The return of the italic</li>
        <li>P. 42 — Margins as manifesto</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths11-bg: #ede4d3;
  --color-ths11-bg: oklch(0.921 0.025 83.4);
  --color-ths11-paper: #f7f1e1;
  --color-ths11-paper: oklch(0.959 0.022 89.8);
  --color-ths11-ink: #2a1f3a;
  --color-ths11-ink: oklch(0.266 0.051 301.8);
  --color-ths11-mut: #4a3858;
  --color-ths11-mut: oklch(0.374 0.058 309.5);
  --color-ths11-wine: #6b1f4a;
  --color-ths11-wine: oklch(0.374 0.118 349.4);
  --color-ths11-gold: #c69e5a;
  --color-ths11-gold: oklch(0.722 0.099 79.5);
  --color-ths11-foil: #f3dca0;
  --color-ths11-foil: oklch(0.899 0.081 89.5);
  --font-ths11-serif: 'Playfair Display', Georgia, serif;
  --font-ths11-body: 'Cormorant Garamond', Georgia, serif;
  --font-ths11-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-11 {
  width: 100%;
  min-height: 100svh;
}
```
