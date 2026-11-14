---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-liquid-text-fill-hover-animation/"
title: "Tailwind Liquid Text Fill Hover Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A hollow wordmark that floods with water on hover: an outlined layer ([-webkit-text-stroke:…]) under a gradient layer clipped with bg-clip-text and a typed…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Text Fill Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-liquid-text-fill-hover-animation/

A hollow wordmark that floods with water on hover: an outlined layer ([-webkit-text-stroke:…]) under a gradient layer clipped with bg-clip-text and a typed @property level that tweens from 0% to 104%, then bobs. The nav pills below fill bottom-up with bg-[length:100%_0%] → hover:bg-[length:100%_100%].
## HTML
```html
<section class="tth-02 @container w-full min-h-svh grid place-items-center bg-tth02-bg bg-[radial-gradient(120%_90%_at_50%_0%,var(--color-tth02-deep),var(--color-tth02-bg)_60%)] px-5 py-14 font-tth02-sans text-tth02-ink" aria-label="Liquid text fill on hover demo">
  <div class="flex w-full max-w-[52rem] flex-col items-center gap-6 text-center">
    <p class="text-xs font-bold uppercase tracking-[0.28em] text-tth02-mut">Tidewater Swim Co. &mdash; Summer '26</p>
    <a id="tth02-top" href="#tth02-top" class="group/word relative inline-block rounded px-[0.04em] py-[0.06em] font-tth02-display text-[clamp(44px,11cqi,118px)] font-black leading-[1.04] tracking-[-0.03em] no-underline [--tth02-fill:0%] transition-[--tth02-fill] duration-900 ease-[cubic-bezier(.3,.9,.2,1)] hover:[--tth02-fill:104%] focus-visible:[--tth02-fill:104%] focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-tth02-hi motion-reduce:transition-none">
      <span class="block text-tth02-bg [paint-order:stroke_fill] [-webkit-text-stroke:3px_color-mix(in_oklch,var(--color-tth02-ink)_55%,transparent)]">TIDEWATER</span>
      <span aria-hidden="true" class="absolute inset-0 block px-[0.04em] py-[0.06em] bg-[linear-gradient(180deg,var(--color-tth02-hi)_0%,var(--color-tth02-hi)_6%,var(--color-tth02-lo)_60%,var(--color-tth02-abyss)_100%)] bg-clip-text text-transparent [clip-path:inset(calc(100%-var(--tth02-fill)+var(--tth02-bob))_-6%_-6%_-6%)] group-hover/word:animate-tth02-bob group-focus-visible/word:animate-tth02-bob motion-reduce:animate-none!">TIDEWATER</span>
    </a>
    <p class="max-w-[52ch] text-[15px] leading-[1.7] text-tth02-mut">Hold the cursor on the wordmark and let it flood. The level is one typed <code class="rounded-[5px] bg-tth02-chip px-1.5 py-px font-tth02-mono text-[0.88em] text-tth02-hi">@property</code>; the wave is a 3s keyframe on the clip edge.</p>
    <nav class="mt-1.5 flex flex-wrap justify-center gap-2.5" aria-label="Collection">
      <a href="#tth02-top" class="grid min-h-11 place-items-center rounded-full border-[1.5px] border-tth02-ink/30 px-6 text-sm font-semibold no-underline bg-[linear-gradient(180deg,var(--color-tth02-hi),var(--color-tth02-lo))] bg-no-repeat bg-[position:0_100%] bg-[length:100%_0%] transition-[background-size,color,border-color] duration-450 ease-[cubic-bezier(.3,.9,.2,1)] hover:bg-[length:100%_100%] hover:border-transparent hover:text-tth02-bg focus-visible:bg-[length:100%_100%] focus-visible:text-tth02-bg focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth02-hi motion-reduce:transition-none">Swimwear</a>
      <a href="#tth02-top" class="grid min-h-11 place-items-center rounded-full border-[1.5px] border-tth02-ink/30 px-6 text-sm font-semibold no-underline bg-[linear-gradient(180deg,var(--color-tth02-hi),var(--color-tth02-lo))] bg-no-repeat bg-[position:0_100%] bg-[length:100%_0%] transition-[background-size,color,border-color] duration-450 ease-[cubic-bezier(.3,.9,.2,1)] hover:bg-[length:100%_100%] hover:border-transparent hover:text-tth02-bg focus-visible:bg-[length:100%_100%] focus-visible:text-tth02-bg focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth02-hi motion-reduce:transition-none">Wetsuits</a>
      <a href="#tth02-top" class="grid min-h-11 place-items-center rounded-full border-[1.5px] border-tth02-ink/30 px-6 text-sm font-semibold no-underline bg-[linear-gradient(180deg,var(--color-tth02-hi),var(--color-tth02-lo))] bg-no-repeat bg-[position:0_100%] bg-[length:100%_0%] transition-[background-size,color,border-color] duration-450 ease-[cubic-bezier(.3,.9,.2,1)] hover:bg-[length:100%_100%] hover:border-transparent hover:text-tth02-bg focus-visible:bg-[length:100%_100%] focus-visible:text-tth02-bg focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth02-hi motion-reduce:transition-none">Open water</a>
      <a href="#tth02-top" class="grid min-h-11 place-items-center rounded-full border-[1.5px] border-tth02-ink/30 px-6 text-sm font-semibold no-underline bg-[linear-gradient(180deg,var(--color-tth02-hi),var(--color-tth02-lo))] bg-no-repeat bg-[position:0_100%] bg-[length:100%_0%] transition-[background-size,color,border-color] duration-450 ease-[cubic-bezier(.3,.9,.2,1)] hover:bg-[length:100%_100%] hover:border-transparent hover:text-tth02-bg focus-visible:bg-[length:100%_100%] focus-visible:text-tth02-bg focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth02-hi motion-reduce:transition-none">Journal</a>
    </nav>
    <p class="text-[12.5px] text-tth02-mut">Nav pills fill bottom-up with <code class="rounded-[5px] bg-tth02-chip px-1.5 py-px font-tth02-mono text-[0.88em] text-tth02-hi">bg-[length:100%_0%]</code> alone &mdash; the one-element version of the same idea.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Typed properties: the one thing utilities cannot declare. Without them the level snaps instead of tweening. */

@property --tth02-fill {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@property --tth02-bob {
  syntax: '<percentage>';
  inherits: true;
  initial-value: 0%;
}

@theme {
  --color-tth02-bg: #0b1424;
  --color-tth02-bg: oklch(0.17 0.03 250);
  --color-tth02-deep: #112241;
  --color-tth02-deep: oklch(0.23 0.05 255);
  --color-tth02-chip: #1b2a42;
  --color-tth02-chip: oklch(0.27 0.04 250);
  --color-tth02-ink: #ebf1f6;
  --color-tth02-ink: oklch(0.95 0.01 230);
  --color-tth02-mut: #9eabbe;
  --color-tth02-mut: oklch(0.74 0.03 240);
  --color-tth02-hi: #8fd6f5;
  --color-tth02-hi: oklch(0.85 0.11 220);
  --color-tth02-lo: #2f6de0;
  --color-tth02-lo: oklch(0.55 0.19 255);
  --color-tth02-abyss: #23409a;
  --color-tth02-abyss: oklch(0.4 0.16 262);
  --font-tth02-display: 'Unbounded', system-ui, sans-serif;
  --font-tth02-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tth02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tth02-bob: tth02-bob 3s ease-in-out 0.9s infinite;

  @keyframes tth02-bob {
    0%,
        100% {
      --tth02-bob: 0%;
    }

    50% {
      --tth02-bob: 1.6%;
    }
  }
}

.tth-02 {
  width: 100%;
  min-height: 100svh;
}
```
