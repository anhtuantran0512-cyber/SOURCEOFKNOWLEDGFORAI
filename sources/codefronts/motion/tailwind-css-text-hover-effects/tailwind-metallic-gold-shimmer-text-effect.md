---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-metallic-gold-shimmer-text-effect/"
title: "Tailwind Metallic Gold Shimmer Text Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A membership card in gold leaf: the type is a 250%-wide gradient with a bright band in the middle, clipped to the glyphs with bg-clip-text."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Metallic Gold Shimmer Text Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-metallic-gold-shimmer-text-effect/

A membership card in gold leaf: the type is a 250%-wide gradient with a bright band in the middle, clipped to the glyphs with bg-clip-text. Hovering the card slides bg-[position:97%_0] to 3%_0, so the glint sweeps across the wordmark and price while the eyebrow keeps an ambient 6s glint.
## HTML
```html
<section class="tth-08 w-full min-h-svh grid place-items-center bg-tth08-bg bg-[radial-gradient(100%_80%_at_50%_0%,var(--color-tth08-glow),var(--color-tth08-bg)_70%)] px-5 py-14 font-tth08-serif text-tth08-ink" aria-label="Metallic shimmer text demo">
  <a id="tth08-top" href="#tth08-top" class="group/card flex w-full max-w-[35rem] flex-col gap-[clamp(18px,3.4vw,30px)] rounded-[20px] border border-tth08-line bg-[linear-gradient(160deg,var(--color-tth08-card),var(--color-tth08-card2))] p-[clamp(26px,5vw,46px)] no-underline shadow-[0_30px_80px_oklch(0.05_0.01_70/0.6),inset_0_1px_0_oklch(1_0_0/0.06)] transition-[border-color,translate,box-shadow] duration-500 ease-[cubic-bezier(.22,1,.36,1)] hover:-translate-y-1 hover:border-tth08-gold-2/55 hover:shadow-[0_40px_90px_oklch(0.05_0.01_70/0.7),0_0_0_1px_oklch(0.72_0.11_85/0.15),inset_0_1px_0_oklch(1_0_0/0.08)] focus-visible:-translate-y-1 focus-visible:border-tth08-gold-2/55 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth08-gold-1 motion-reduce:transition-none">
    <p class="font-tth08-sans text-xs font-medium uppercase tracking-[0.3em]"><span class="bg-[linear-gradient(105deg,var(--color-tth08-gold-3)_0%,var(--color-tth08-gold-2)_34%,var(--color-tth08-shine)_49%,var(--color-tth08-gold-2)_64%,var(--color-tth08-gold-3)_100%)] bg-[length:250%_100%] bg-[position:97%_0] bg-clip-text text-transparent animate-tth08-glint motion-reduce:animate-none">Est. MMXXVI &middot; by invitation</span></p>
    <h2 class="text-[clamp(44px,9.4vw,84px)] font-bold leading-[1.02] tracking-[0.03em] drop-shadow-[0_3px_10px_oklch(0.05_0.01_70/0.7)]"><span class="bg-[linear-gradient(105deg,var(--color-tth08-gold-3)_0%,var(--color-tth08-gold-2)_34%,var(--color-tth08-shine)_49%,var(--color-tth08-gold-2)_64%,var(--color-tth08-gold-3)_100%)] bg-[length:250%_100%] bg-[position:97%_0] bg-clip-text text-transparent transition-[background-position] duration-1100 ease-[cubic-bezier(.25,.66,.15,1)] group-hover/card:bg-[position:3%_0] group-focus-visible/card:bg-[position:3%_0] motion-reduce:transition-none">AURUM<br>RESERVE</span></h2>
    <div class="flex items-end justify-between gap-3.5 border-t border-tth08-line pt-[clamp(14px,2.6vw,20px)]">
      <span class="font-tth08-sans text-xs font-medium uppercase tracking-[0.14em] text-tth08-mut">Founding member &mdash; No. 047</span>
      <span class="flex items-baseline gap-1.5"><b class="bg-[linear-gradient(105deg,var(--color-tth08-gold-3)_0%,var(--color-tth08-gold-2)_34%,var(--color-tth08-shine)_49%,var(--color-tth08-gold-2)_64%,var(--color-tth08-gold-3)_100%)] bg-[length:250%_100%] bg-[position:97%_0] bg-clip-text text-[clamp(24px,4vw,32px)] font-bold text-transparent transition-[background-position] duration-1100 delay-120 ease-[cubic-bezier(.25,.66,.15,1)] group-hover/card:bg-[position:3%_0] group-focus-visible/card:bg-[position:3%_0] motion-reduce:transition-none">$890</b><small class="font-tth08-sans text-xs text-tth08-mut">/year</small></span>
    </div>
    <span class="inline-flex items-center gap-2 self-start font-tth08-sans text-[13px] font-semibold text-tth08-gold-1">Request your invitation <span aria-hidden="true" class="transition-transform duration-300 group-hover/card:translate-x-1">&rarr;</span></span>
    <p class="font-tth08-sans text-xs leading-[1.7] text-tth08-mut">Hover the card: the gradient never changes &mdash; <code class="rounded bg-tth08-chip px-1.5 py-px font-tth08-mono text-[0.92em] text-tth08-gold-1">bg-[position]</code> slides the glint band through the glyphs.</p>
  </a>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth08-bg: #110f0b;
  --color-tth08-bg: oklch(0.15 0.008 70);
  --color-tth08-glow: #1a1712;
  --color-tth08-glow: oklch(0.2 0.012 75);
  --color-tth08-card: #1b1813;
  --color-tth08-card: oklch(0.19 0.01 75);
  --color-tth08-card2: #13110d;
  --color-tth08-card2: oklch(0.16 0.009 72);
  --color-tth08-chip: #2a261e;
  --color-tth08-chip: oklch(0.26 0.015 75);
  --color-tth08-line: #3d3729;
  --color-tth08-line: oklch(0.34 0.03 85);
  --color-tth08-ink: #ece5d6;
  --color-tth08-ink: oklch(0.9 0.02 85);
  --color-tth08-mut: #a89f8b;
  --color-tth08-mut: oklch(0.72 0.03 80);
  --color-tth08-gold-1: #ead59a;
  --color-tth08-gold-1: oklch(0.88 0.09 92);
  --color-tth08-gold-2: #c2a052;
  --color-tth08-gold-2: oklch(0.72 0.11 85);
  --color-tth08-gold-3: #7a6229;
  --color-tth08-gold-3: oklch(0.5 0.09 78);
  --color-tth08-shine: #fdf6dc;
  --color-tth08-shine: oklch(0.97 0.05 95);
  --font-tth08-serif: 'Bodoni Moda', Didot, Georgia, serif;
  --font-tth08-sans: 'Hanken Grotesk', system-ui, sans-serif;
  --font-tth08-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth08-glint: tth08-glint 6s ease-in-out infinite;

  @keyframes tth08-glint {
    0%,
        100% {
      background-position: 97% 0;
    }

    50% {
      background-position: 3% 0;
    }
  }
}

.tth-08 {
  width: 100%;
  min-height: 100svh;
}
```
