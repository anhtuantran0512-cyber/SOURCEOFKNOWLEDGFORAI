---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-outline-text-stroke-to-fill-hover-effect/"
title: "Tailwind Outline Text Stroke to Fill Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A foundry wordmark that pours from outline to solid: one element carries both the stroke ([-webkit-text-stroke:…]) and a gradient clipped to the glyphs whose…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Outline Text Stroke to Fill Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-outline-text-stroke-to-fill-hover-effect/

A foundry wordmark that pours from outline to solid: one element carries both the stroke ([-webkit-text-stroke:…]) and a gradient clipped to the glyphs whose height grows bg-[length:100%_0%] → hover:bg-[length:100%_100%] from the baseline. The nav bars fill left to right with the same two utilities rotated.
## HTML
```html
<section class="tth-16 @container w-full min-h-svh grid place-items-center bg-tth16-bg bg-[radial-gradient(90%_70%_at_50%_100%,var(--color-tth16-glow),var(--color-tth16-bg)_70%)] px-5 py-14 font-tth16-sans text-tth16-ink" aria-label="Outline to fill text demo">
  <div class="flex w-full max-w-[47.5rem] flex-col items-center gap-[clamp(20px,3.6cqi,32px)] text-center">
    <header class="flex w-full flex-wrap items-center justify-between gap-3.5 border-b border-tth16-line pb-3.5">
      <p class="text-xs font-bold uppercase tracking-[0.22em] text-tth16-mut">Grade 900 &mdash; a display face in 5 weights</p>
      <span class="rounded-full border border-tth16-heat2/40 px-3 py-1.5 font-tth16-mono text-[11px] text-tth16-heat2 @max-[35rem]:hidden">bg-[length:100%_0%] &rarr; 100%_100%</span>
    </header>
    <a id="tth16-top" href="#tth16-top" class="inline-block rounded-md px-[0.06em] py-[0.08em] font-tth16-display text-[clamp(84px,20cqi,210px)] uppercase leading-none tracking-[0.02em] no-underline text-transparent [-webkit-text-stroke:1.5px_color-mix(in_oklch,var(--color-tth16-ink)_65%,transparent)] bg-[linear-gradient(15deg,var(--color-tth16-heat1),var(--color-tth16-heat2))] bg-no-repeat bg-[position:0_100%] bg-[length:100%_0%] bg-clip-text transition-[background-size,-webkit-text-stroke-color] duration-600 ease-[cubic-bezier(.3,.85,.2,1)] hover:bg-[length:100%_100%] hover:[-webkit-text-stroke-color:color-mix(in_oklch,var(--color-tth16-heat1)_60%,transparent)] focus-visible:bg-[length:100%_100%] focus-visible:outline-2 focus-visible:outline-offset-[10px] focus-visible:outline-tth16-heat2 pointer-coarse:bg-[length:100%_100%] motion-reduce:transition-none">FORGE</a>
    <nav class="flex flex-wrap justify-center gap-[clamp(10px,2.4cqi,20px)]" aria-label="Foundry">
      <a href="#tth16-top" class="grid min-h-12 place-items-center rounded-[10px] border-[1.5px] border-tth16-line px-6 font-tth16-display text-lg uppercase tracking-[0.06em] no-underline text-transparent [-webkit-text-stroke:1px_color-mix(in_oklch,var(--color-tth16-ink)_85%,transparent)] bg-[linear-gradient(90deg,var(--color-tth16-heat1),var(--color-tth16-heat2))] bg-no-repeat bg-[position:0_0] bg-[length:0%_100%] bg-clip-text transition-[background-size,border-color] duration-450 ease-[cubic-bezier(.3,.85,.2,1)] hover:border-tth16-heat1/60 hover:bg-[length:100%_100%] focus-visible:bg-[length:100%_100%] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth16-heat2 motion-reduce:transition-none">Trial fonts</a>
      <a href="#tth16-top" class="grid min-h-12 place-items-center rounded-[10px] border-[1.5px] border-tth16-line px-6 font-tth16-display text-lg uppercase tracking-[0.06em] no-underline text-transparent [-webkit-text-stroke:1px_color-mix(in_oklch,var(--color-tth16-ink)_85%,transparent)] bg-[linear-gradient(90deg,var(--color-tth16-heat1),var(--color-tth16-heat2))] bg-no-repeat bg-[position:0_0] bg-[length:0%_100%] bg-clip-text transition-[background-size,border-color] duration-450 ease-[cubic-bezier(.3,.85,.2,1)] hover:border-tth16-heat1/60 hover:bg-[length:100%_100%] focus-visible:bg-[length:100%_100%] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth16-heat2 motion-reduce:transition-none">Licensing</a>
      <a href="#tth16-top" class="grid min-h-12 place-items-center rounded-[10px] border-[1.5px] border-tth16-line px-6 font-tth16-display text-lg uppercase tracking-[0.06em] no-underline text-transparent [-webkit-text-stroke:1px_color-mix(in_oklch,var(--color-tth16-ink)_85%,transparent)] bg-[linear-gradient(90deg,var(--color-tth16-heat1),var(--color-tth16-heat2))] bg-no-repeat bg-[position:0_0] bg-[length:0%_100%] bg-clip-text transition-[background-size,border-color] duration-450 ease-[cubic-bezier(.3,.85,.2,1)] hover:border-tth16-heat1/60 hover:bg-[length:100%_100%] focus-visible:bg-[length:100%_100%] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth16-heat2 motion-reduce:transition-none">Specimens</a>
    </nav>
    <p class="max-w-[56ch] text-[12.5px] leading-[1.7] text-tth16-mut">Hover the wordmark: the fill pours up from the baseline through <code class="rounded bg-tth16-chip px-1.5 py-px font-tth16-mono text-[0.9em] text-tth16-heat2">bg-clip-text</code> &mdash; one element, stroke and fill on separate paint channels.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth16-bg: #15120e;
  --color-tth16-bg: oklch(0.18 0.008 60);
  --color-tth16-glow: #221a12;
  --color-tth16-glow: oklch(0.23 0.02 55);
  --color-tth16-chip: #2a241d;
  --color-tth16-chip: oklch(0.27 0.012 60);
  --color-tth16-ink: #eee9e1;
  --color-tth16-ink: oklch(0.93 0.008 75);
  --color-tth16-mut: #a59d92;
  --color-tth16-mut: oklch(0.72 0.015 70);
  --color-tth16-heat1: #f07a32;
  --color-tth16-heat1: oklch(0.72 0.18 45);
  --color-tth16-heat2: #f7c84a;
  --color-tth16-heat2: oklch(0.85 0.15 80);
  --color-tth16-line: #3a332b;
  --color-tth16-line: oklch(0.32 0.012 65);
  --font-tth16-display: 'Anton', Impact, sans-serif;
  --font-tth16-sans: 'Work Sans', system-ui, sans-serif;
  --font-tth16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-16 {
  width: 100%;
  min-height: 100svh;
}
```
