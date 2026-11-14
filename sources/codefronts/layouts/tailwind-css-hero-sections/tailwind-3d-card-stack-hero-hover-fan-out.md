---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-3d-card-stack-hero-hover-fan-out/"
title: "3D Card Stack Hero in Tailwind CSS with Hover Fan-Out"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A luxury-fragrance hero — three 50 / 100 / 15 ml product cards in 3D perspective that fan forward on hover or keyboard focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Card Stack Hero in Tailwind CSS with Hover Fan-Out
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-3d-card-stack-hero-hover-fan-out/

A luxury-fragrance hero — three 50 / 100 / 15 ml product cards in 3D perspective that fan forward on hover or keyboard focus. Champagne and blush on jet, with foil numerals, sizes and prices on each card.
## HTML
```html
<section class="ths-27 grid w-full min-h-svh items-center gap-12 overflow-hidden bg-ths27-bg bg-[radial-gradient(50%_60%_at_75%_50%,rgb(198_158_90/0.14),transparent_70%)] px-5 py-16 font-ths27-sans text-ths27-champ sm:px-12 lg:grid-cols-2" aria-label="3D card stack hero">
  <div class="max-w-lg">
    <span class="font-ths27-body text-lg text-ths27-gold italic">— Cuvée 04</span>
    <h1 class="mt-3 font-ths27-serif text-[clamp(34px,4.8vw,54px)] leading-[1.08] font-semibold tracking-[-0.01em] text-balance">The fragrance <em class="text-ths27-blush">three editors couldn't stop wearing.</em></h1>
    <p class="mt-5 max-w-sm text-base/relaxed text-ths27-mut">Bergamot, oud, and a single drop of Damascus rose. Limited to 1,200 bottles.</p>
    <a href="#shop" class="mt-8 inline-flex min-h-11 items-center border-b-[1.5px] border-ths27-gold font-ths27-mono text-xs font-bold tracking-[0.16em] text-ths27-gold transition hover:border-ths27-blush hover:text-ths27-blush focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths27-gold">DISCOVER THE BOTTLE →</a>
  </div>
  <div class="group relative grid min-h-[400px] place-items-center perspective-[1200px]" role="list" aria-label="Bottle sizes">
    <a role="listitem" href="#size-15" class="absolute flex h-[260px] w-[180px] -translate-x-[90px] translate-z-[-40px] rotate-y-[20deg] flex-col items-center justify-center gap-2 rounded-md border border-ths27-gold/70 bg-linear-135 from-ths27-card to-ths27-bg transition-transform duration-500 ease-[cubic-bezier(.22,1,.36,1)] group-focus-within:-translate-x-[140px] group-focus-within:translate-z-0 group-hover:-translate-x-[140px] group-hover:translate-z-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths27-blush motion-reduce:transition-none">
      <strong class="bg-linear-to-b from-ths27-foil to-ths27-gold bg-clip-text font-ths27-serif text-6xl font-extrabold text-transparent italic">04</strong>
      <span class="font-ths27-mono text-[11px] tracking-[0.24em] text-ths27-gold">15 ML</span><span class="text-xs text-ths27-mut">$68</span>
    </a>
    <a role="listitem" href="#size-100" class="absolute flex h-[260px] w-[180px] translate-x-[90px] translate-z-[-40px] -rotate-y-[20deg] flex-col items-center justify-center gap-2 rounded-md border border-ths27-gold/70 bg-linear-135 from-ths27-card to-ths27-bg transition-transform duration-500 ease-[cubic-bezier(.22,1,.36,1)] group-focus-within:translate-x-[140px] group-focus-within:translate-z-0 group-hover:translate-x-[140px] group-hover:translate-z-0 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths27-blush motion-reduce:transition-none">
      <strong class="bg-linear-to-b from-ths27-foil to-ths27-gold bg-clip-text font-ths27-serif text-6xl font-extrabold text-transparent italic">04</strong>
      <span class="font-ths27-mono text-[11px] tracking-[0.24em] text-ths27-gold">100 ML</span><span class="text-xs text-ths27-mut">$295</span>
    </a>
    <a role="listitem" href="#size-50" class="relative z-10 flex h-[280px] w-[190px] flex-col items-center justify-center gap-2 rounded-md border border-ths27-gold bg-linear-135 from-ths27-card2 to-ths27-card shadow-[0_30px_60px_-20px_rgb(0_0_0/0.8),0_0_40px_rgb(198_158_90/0.12)] transition-transform duration-500 ease-[cubic-bezier(.22,1,.36,1)] group-focus-within:translate-z-[40px] group-hover:translate-z-[40px] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths27-blush motion-reduce:transition-none">
      <span class="absolute top-3 rounded-full border border-ths27-blush/50 px-2 py-0.5 font-ths27-mono text-[9px] tracking-[0.18em] text-ths27-blush">SIGNATURE</span>
      <strong class="bg-linear-to-b from-ths27-foil to-ths27-gold bg-clip-text font-ths27-serif text-7xl font-extrabold text-transparent italic">04</strong>
      <span class="font-ths27-mono text-[11px] tracking-[0.24em] text-ths27-gold">50 ML</span><span class="text-xs text-ths27-mut">$185</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths27-bg: #0d0a0a;
  --color-ths27-bg: oklch(0.149 0.005 17.8);
  --color-ths27-card: #2a1a1a;
  --color-ths27-card: oklch(0.239 0.026 19.1);
  --color-ths27-card2: #3a2828;
  --color-ths27-card2: oklch(0.298 0.027 18.8);
  --color-ths27-champ: #f0e0c8;
  --color-ths27-champ: oklch(0.913 0.036 78.1);
  --color-ths27-mut: #bfa182;
  --color-ths27-mut: oklch(0.728 0.056 67.7);
  --color-ths27-gold: #c69e5a;
  --color-ths27-gold: oklch(0.722 0.099 79.5);
  --color-ths27-foil: #f3dca0;
  --color-ths27-foil: oklch(0.899 0.081 89.5);
  --color-ths27-blush: #f5c2c8;
  --color-ths27-blush: oklch(0.861 0.059 10.5);
  --font-ths27-serif: 'Playfair Display', Georgia, serif;
  --font-ths27-body: 'Cormorant Garamond', Georgia, serif;
  --font-ths27-sans: 'Geist', system-ui, sans-serif;
  --font-ths27-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-27 {
  width: 100%;
  min-height: 100svh;
}
```
