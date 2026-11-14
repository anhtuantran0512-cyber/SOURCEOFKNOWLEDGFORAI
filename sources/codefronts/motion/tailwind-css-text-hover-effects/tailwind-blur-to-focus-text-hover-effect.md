---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-blur-to-focus-text-hover-effect/"
title: "Tailwind Blur to Focus Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "An editorial index where hovering one line pushes every other line out of focus."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blur to Focus Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-blur-to-focus-text-hover-effect/

An editorial index where hovering one line pushes every other line out of focus. The whole effect is one stacked variant on each row — group-hover/list:not-hover:blur-[4px] — plus its keyboard twin group-has-focus-visible/list:not-has-focus-visible:. A hidden P.S. sits blurred below until you hover it.
## HTML
```html
<section class="tth-13 w-full min-h-svh grid place-items-center bg-tth13-bg px-5 py-14 font-tth13-serif text-tth13-ink" aria-label="Blur to focus list demo">
  <div class="flex w-full max-w-[43.75rem] flex-col gap-[clamp(16px,3vw,24px)]">
    <header class="flex flex-wrap items-center justify-between gap-3.5 border-b-[1.5px] border-tth13-ink pb-3.5">
      <p class="font-tth13-sans text-[13px] font-bold uppercase tracking-[0.16em] text-tth13-mut">Field Notes &mdash; six essays on light</p>
      <span class="rounded-full border border-tth13-acc/40 px-3 py-1.5 font-tth13-mono text-[11px] text-tth13-acc">group-hover/list:not-hover:</span>
    </header>
    <ol class="group/list">
      <li class="border-b border-tth13-line transition-[filter,opacity,scale] duration-250 group-hover/list:not-hover:scale-[.985] group-hover/list:not-hover:opacity-40 group-hover/list:not-hover:blur-[4px] group-hover/list:not-hover:saturate-60 group-hover/list:not-hover:duration-500 group-has-focus-visible/list:not-has-focus-visible:opacity-40 group-has-focus-visible/list:not-has-focus-visible:blur-[4px] motion-reduce:transition-none"><a id="tth13-top" href="#tth13-top" class="flex items-baseline justify-between gap-[18px] rounded px-1 py-[clamp(13px,2.4vw,19px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth13-acc"><span class="text-[clamp(23px,4vw,34px)] leading-[1.2] tracking-[-0.005em]"><span class="mr-3 font-tth13-mono text-xs tracking-[0.05em] text-tth13-acc">01</span>Fog line at Bodega Bay</span><span class="whitespace-nowrap font-tth13-mono text-xs text-tth13-mut">35mm &middot; 06:12</span></a></li>
      <li class="border-b border-tth13-line transition-[filter,opacity,scale] duration-250 group-hover/list:not-hover:scale-[.985] group-hover/list:not-hover:opacity-40 group-hover/list:not-hover:blur-[4px] group-hover/list:not-hover:saturate-60 group-hover/list:not-hover:duration-500 group-has-focus-visible/list:not-has-focus-visible:opacity-40 group-has-focus-visible/list:not-has-focus-visible:blur-[4px] motion-reduce:transition-none"><a href="#tth13-top" class="flex items-baseline justify-between gap-[18px] rounded px-1 py-[clamp(13px,2.4vw,19px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth13-acc"><span class="text-[clamp(23px,4vw,34px)] leading-[1.2] tracking-[-0.005em]"><span class="mr-3 font-tth13-mono text-xs tracking-[0.05em] text-tth13-acc">02</span>Sodium lamps, last winter</span><span class="whitespace-nowrap font-tth13-mono text-xs text-tth13-mut">digital &middot; 23:40</span></a></li>
      <li class="border-b border-tth13-line transition-[filter,opacity,scale] duration-250 group-hover/list:not-hover:scale-[.985] group-hover/list:not-hover:opacity-40 group-hover/list:not-hover:blur-[4px] group-hover/list:not-hover:saturate-60 group-hover/list:not-hover:duration-500 group-has-focus-visible/list:not-has-focus-visible:opacity-40 group-has-focus-visible/list:not-has-focus-visible:blur-[4px] motion-reduce:transition-none"><a href="#tth13-top" class="flex items-baseline justify-between gap-[18px] rounded px-1 py-[clamp(13px,2.4vw,19px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth13-acc"><span class="text-[clamp(23px,4vw,34px)] leading-[1.2] tracking-[-0.005em]"><span class="mr-3 font-tth13-mono text-xs tracking-[0.05em] text-tth13-acc">03</span>The greenhouse negatives</span><span class="whitespace-nowrap font-tth13-mono text-xs text-tth13-mut">120 film &middot; noon</span></a></li>
      <li class="border-b border-tth13-line transition-[filter,opacity,scale] duration-250 group-hover/list:not-hover:scale-[.985] group-hover/list:not-hover:opacity-40 group-hover/list:not-hover:blur-[4px] group-hover/list:not-hover:saturate-60 group-hover/list:not-hover:duration-500 group-has-focus-visible/list:not-has-focus-visible:opacity-40 group-has-focus-visible/list:not-has-focus-visible:blur-[4px] motion-reduce:transition-none"><a href="#tth13-top" class="flex items-baseline justify-between gap-[18px] rounded px-1 py-[clamp(13px,2.4vw,19px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth13-acc"><span class="text-[clamp(23px,4vw,34px)] leading-[1.2] tracking-[-0.005em]"><span class="mr-3 font-tth13-mono text-xs tracking-[0.05em] text-tth13-acc">04</span>Harbour glass, <em>overexposed</em></span><span class="whitespace-nowrap font-tth13-mono text-xs text-tth13-mut">35mm &middot; 15:55</span></a></li>
      <li class="border-b border-tth13-line transition-[filter,opacity,scale] duration-250 group-hover/list:not-hover:scale-[.985] group-hover/list:not-hover:opacity-40 group-hover/list:not-hover:blur-[4px] group-hover/list:not-hover:saturate-60 group-hover/list:not-hover:duration-500 group-has-focus-visible/list:not-has-focus-visible:opacity-40 group-has-focus-visible/list:not-has-focus-visible:blur-[4px] motion-reduce:transition-none"><a href="#tth13-top" class="flex items-baseline justify-between gap-[18px] rounded px-1 py-[clamp(13px,2.4vw,19px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth13-acc"><span class="text-[clamp(23px,4vw,34px)] leading-[1.2] tracking-[-0.005em]"><span class="mr-3 font-tth13-mono text-xs tracking-[0.05em] text-tth13-acc">05</span>Aurora over the car park</span><span class="whitespace-nowrap font-tth13-mono text-xs text-tth13-mut">digital &middot; 01:03</span></a></li>
    </ol>
    <p class="pt-1.5"><a href="#tth13-top" class="text-[17px] italic text-tth13-mut no-underline blur-[3.5px] transition-[filter,color] duration-450 hover:text-tth13-acc hover:blur-none focus-visible:text-tth13-acc focus-visible:blur-none focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth13-acc pointer-coarse:blur-none motion-reduce:transition-none">P.S. &mdash; the sixth essay was never published. Hover to read why.</a></p>
    <p class="font-tth13-sans text-[12.5px] text-tth13-mut">Hover the index: everything but your line drops out of focus. <kbd class="rounded-[5px] border border-b-2 border-tth13-line bg-white px-1.5 py-0.5 font-tth13-mono text-[11px]">Tab</kbd> does the same via <code class="rounded bg-tth13-chip px-1.5 py-px font-tth13-mono text-[0.9em]">group-has-focus-visible/list:</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth13-bg: #f8f7f3;
  --color-tth13-bg: oklch(0.975 0.004 90);
  --color-tth13-chip: #ebe8e0;
  --color-tth13-chip: oklch(0.93 0.008 85);
  --color-tth13-ink: #221e18;
  --color-tth13-ink: oklch(0.24 0.01 80);
  --color-tth13-mut: #6a6359;
  --color-tth13-mut: oklch(0.5 0.015 80);
  --color-tth13-acc: #b06a1c;
  --color-tth13-acc: oklch(0.58 0.14 60);
  --color-tth13-line: #e2dfd7;
  --color-tth13-line: oklch(0.9 0.008 85);
  --font-tth13-serif: 'Instrument Serif', Georgia, serif;
  --font-tth13-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tth13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-13 {
  width: 100%;
  min-height: 100svh;
}
```
