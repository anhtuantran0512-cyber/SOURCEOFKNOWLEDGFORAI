---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-variable-font-weight-hover-animation/"
title: "Tailwind Variable Font Weight Hover Animation"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "An issue index where titles glide from font-light to font-extrabold through every intermediate weight — with zero layout shift."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Variable Font Weight Hover Animation
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-variable-font-weight-hover-animation/

An issue index where titles glide from font-light to font-extrabold through every intermediate weight — with zero layout shift. A hidden bold twin, after:content-[attr(data-text)] after:h-0 after:invisible after:font-extrabold, reserves the bold width from the first paint.
## HTML
```html
<section class="tth-20 w-full min-h-svh grid place-items-center bg-tth20-bg px-5 py-14 font-tth20-sans text-tth20-ink [font-synthesis-weight:none]" aria-label="Variable font weight shift demo">
  <div class="flex w-full max-w-[45rem] flex-col gap-[clamp(16px,3vw,24px)]">
    <header class="flex flex-wrap items-center justify-between gap-3.5 border-b-[1.5px] border-tth20-ink pb-3.5">
      <p class="text-[12.5px] font-bold uppercase tracking-[0.2em] text-tth20-mut">Grain &amp; Gradient &mdash; issue index</p>
      <span class="rounded-full border border-tth20-acc/40 px-3 py-1.5 font-tth20-mono text-[11px] text-tth20-acc">wght 300 &rarr; 800, one axis</span>
    </header>
    <nav class="flex flex-col" aria-label="Issues">
      <a id="tth20-top" href="#tth20-top" class="group/item flex items-baseline gap-[clamp(14px,3vw,24px)] rounded border-b border-tth20-line px-1 py-[clamp(12px,2.4vw,18px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth20-acc"><em class="font-tth20-mono text-xs font-bold not-italic text-tth20-mut transition-[font-weight,color] duration-450 group-hover/item:font-normal group-hover/item:text-tth20-mut/60 group-focus-visible/item:text-tth20-mut/60">01</em><span data-text="The Typography Issue" class="block text-[clamp(24px,4.8vw,40px)] font-light leading-[1.2] tracking-[-0.015em] transition-[font-weight,color] duration-450 after:invisible after:block after:h-0 after:overflow-hidden after:font-extrabold after:content-[attr(data-text)] group-hover/item:font-extrabold group-hover/item:text-tth20-acc group-focus-visible/item:font-extrabold group-focus-visible/item:text-tth20-acc motion-reduce:transition-none">The Typography Issue</span><span aria-hidden="true" class="ml-auto -translate-x-2 text-xl text-tth20-acc opacity-0 transition-[opacity,translate] duration-300 group-hover/item:translate-x-0 group-hover/item:opacity-100 group-focus-visible/item:opacity-100">&rarr;</span></a>
      <a href="#tth20-top" class="group/item flex items-baseline gap-[clamp(14px,3vw,24px)] rounded border-b border-tth20-line px-1 py-[clamp(12px,2.4vw,18px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth20-acc"><em class="font-tth20-mono text-xs font-bold not-italic text-tth20-mut transition-[font-weight,color] duration-450 group-hover/item:font-normal group-hover/item:text-tth20-mut/60 group-focus-visible/item:text-tth20-mut/60">02</em><span data-text="Color, Carefully" class="block text-[clamp(24px,4.8vw,40px)] font-light leading-[1.2] tracking-[-0.015em] transition-[font-weight,color] duration-450 after:invisible after:block after:h-0 after:overflow-hidden after:font-extrabold after:content-[attr(data-text)] group-hover/item:font-extrabold group-hover/item:text-tth20-acc group-focus-visible/item:font-extrabold group-focus-visible/item:text-tth20-acc motion-reduce:transition-none">Color, Carefully</span><span aria-hidden="true" class="ml-auto -translate-x-2 text-xl text-tth20-acc opacity-0 transition-[opacity,translate] duration-300 group-hover/item:translate-x-0 group-hover/item:opacity-100 group-focus-visible/item:opacity-100">&rarr;</span></a>
      <a href="#tth20-top" class="group/item flex items-baseline gap-[clamp(14px,3vw,24px)] rounded border-b border-tth20-line px-1 py-[clamp(12px,2.4vw,18px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth20-acc"><em class="font-tth20-mono text-xs font-bold not-italic text-tth20-mut transition-[font-weight,color] duration-450 group-hover/item:font-normal group-hover/item:text-tth20-mut/60 group-focus-visible/item:text-tth20-mut/60">03</em><span data-text="Grids Against Chaos" class="block text-[clamp(24px,4.8vw,40px)] font-light leading-[1.2] tracking-[-0.015em] transition-[font-weight,color] duration-450 after:invisible after:block after:h-0 after:overflow-hidden after:font-extrabold after:content-[attr(data-text)] group-hover/item:font-extrabold group-hover/item:text-tth20-acc group-focus-visible/item:font-extrabold group-focus-visible/item:text-tth20-acc motion-reduce:transition-none">Grids Against Chaos</span><span aria-hidden="true" class="ml-auto -translate-x-2 text-xl text-tth20-acc opacity-0 transition-[opacity,translate] duration-300 group-hover/item:translate-x-0 group-hover/item:opacity-100 group-focus-visible/item:opacity-100">&rarr;</span></a>
      <a href="#tth20-top" class="group/item flex items-baseline gap-[clamp(14px,3vw,24px)] rounded border-b border-tth20-line px-1 py-[clamp(12px,2.4vw,18px)] no-underline focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tth20-acc"><em class="font-tth20-mono text-xs font-bold not-italic text-tth20-mut transition-[font-weight,color] duration-450 group-hover/item:font-normal group-hover/item:text-tth20-mut/60 group-focus-visible/item:text-tth20-mut/60">04</em><span data-text="Motion With Manners" class="block text-[clamp(24px,4.8vw,40px)] font-light leading-[1.2] tracking-[-0.015em] transition-[font-weight,color] duration-450 after:invisible after:block after:h-0 after:overflow-hidden after:font-extrabold after:content-[attr(data-text)] group-hover/item:font-extrabold group-hover/item:text-tth20-acc group-focus-visible/item:font-extrabold group-focus-visible/item:text-tth20-acc motion-reduce:transition-none">Motion With Manners</span><span aria-hidden="true" class="ml-auto -translate-x-2 text-xl text-tth20-acc opacity-0 transition-[opacity,translate] duration-300 group-hover/item:translate-x-0 group-hover/item:opacity-100 group-focus-visible/item:opacity-100">&rarr;</span></a>
    </nav>
    <p class="max-w-[60ch] text-[12.5px] leading-[1.7] text-tth20-mut">Hover a title: every intermediate weight renders &mdash; and the row never shifts, because a hidden bold twin (<code class="rounded bg-tth20-chip px-1.5 py-px font-tth20-mono text-[0.9em]">after:content-[attr(data-text)]</code>) reserved the width on day one.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth20-bg: #f9f6f3;
  --color-tth20-bg: oklch(0.97 0.005 60);
  --color-tth20-chip: #ece8e3;
  --color-tth20-chip: oklch(0.92 0.006 55);
  --color-tth20-ink: #221a14;
  --color-tth20-ink: oklch(0.22 0.012 50);
  --color-tth20-mut: #6b6158;
  --color-tth20-mut: oklch(0.5 0.015 55);
  --color-tth20-acc: #bf5427;
  --color-tth20-acc: oklch(0.58 0.16 40);
  --color-tth20-line: #e3ded8;
  --color-tth20-line: oklch(0.89 0.008 55);
  --font-tth20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tth20-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-20 {
  width: 100%;
  min-height: 100svh;
}
```
