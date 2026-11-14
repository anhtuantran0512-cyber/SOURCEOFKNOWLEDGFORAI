---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-classic-card-deck-stack-shadow/"
title: "Tailwind Classic Card Deck Stack Shadow"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Depth from tone and shadow alone &mdash; no colour tricks, no 3D."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Classic Card Deck Stack Shadow
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-classic-card-deck-stack-shadow/

Depth from tone and shadow alone &mdash; no colour tricks, no 3D. Four cards share a footprint, stepped by [transform:translate(calc(var(--i)*5px),calc(var(--i)*6px))], and the thickness comes from a two-layer shadow: a hard 2px offset for the cut edge, a soft blur for the drop. On hover the same expression runs at a larger step, so one utility describes both the resting deck and the spread.
## HTML
```html
<section class="stk-10 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk10-sans bg-stk10-paper" aria-label="Classic card deck">
  <div class="group relative w-[min(320px,100%)] h-55 rounded-[20px] outline-none focus-visible:outline-3 focus-visible:outline-stk10-accent focus-visible:outline-offset-8" tabindex="0">
    <div class="absolute inset-0 rounded-2xl border border-stk10-line bg-stk10-under shadow-[0_2px_0_var(--color-stk10-edge),0_12px_24px_-14px_rgba(60,50,30,0.5)] [transform:translate(calc(var(--i)*5px),calc(var(--i)*6px))] transition-transform duration-400 ease-stk10 group-hover:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] group-focus-visible:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] motion-reduce:transition-none" style="--i:3" aria-hidden="true"></div>
    <div class="absolute inset-0 rounded-2xl border border-stk10-line bg-stk10-under shadow-[0_2px_0_var(--color-stk10-edge),0_12px_24px_-14px_rgba(60,50,30,0.5)] [transform:translate(calc(var(--i)*5px),calc(var(--i)*6px))] transition-transform duration-400 ease-stk10 group-hover:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] group-focus-visible:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] motion-reduce:transition-none" style="--i:2" aria-hidden="true"></div>
    <div class="absolute inset-0 rounded-2xl border border-stk10-line bg-stk10-under shadow-[0_2px_0_var(--color-stk10-edge),0_12px_24px_-14px_rgba(60,50,30,0.5)] [transform:translate(calc(var(--i)*5px),calc(var(--i)*6px))] transition-transform duration-400 ease-stk10 group-hover:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] group-focus-visible:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] motion-reduce:transition-none" style="--i:1" aria-hidden="true"></div>
    <div class="absolute inset-0 z-5 rounded-2xl border border-stk10-line bg-stk10-face p-7 shadow-[0_3px_0_var(--color-stk10-edge),0_20px_34px_-18px_rgba(60,50,30,0.55)] [transform:translate(calc(var(--i)*5px),calc(var(--i)*6px))] transition-transform duration-400 ease-stk10 group-hover:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] group-focus-visible:[transform:translate(calc(var(--i)*12px),calc(var(--i)*13px))] motion-reduce:transition-none" style="--i:0">
      <p class="m-0 font-stk10-mono text-xs font-medium tracking-[0.16em] uppercase text-stk10-accent">Field Notes</p>
      <h3 class="mt-2 mb-2.5 text-3xl font-extrabold tracking-[-0.02em] text-stk10-ink">Deck No.&thinsp;7</h3>
      <p class="m-0 max-w-[32ch] text-[15px] leading-relaxed text-stk10-body">Fifty-two ideas, shuffled weekly. Draw one and build it before Friday.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk10-paper: #e7e4dc;
  --color-stk10-paper: oklch(0.91 0.008 85);
  --color-stk10-face: #fdfcf9;
  --color-stk10-face: oklch(0.99 0.004 85);
  --color-stk10-under: #f6f3ec;
  --color-stk10-under: oklch(0.96 0.007 85);
  --color-stk10-line: #e0dcd0;
  --color-stk10-line: oklch(0.89 0.010 85);
  --color-stk10-edge: #d9d4c6;
  --color-stk10-edge: oklch(0.86 0.014 85);
  --color-stk10-ink: #3a3324;
  --color-stk10-ink: oklch(0.33 0.020 80);
  --color-stk10-body: #6a6250;
  --color-stk10-body: oklch(0.50 0.018 80);
  --color-stk10-accent: #a89b7c;
  --color-stk10-accent: oklch(0.68 0.035 85);
  --font-stk10-sans: 'Archivo', system-ui, sans-serif;
  --font-stk10-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk10: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
