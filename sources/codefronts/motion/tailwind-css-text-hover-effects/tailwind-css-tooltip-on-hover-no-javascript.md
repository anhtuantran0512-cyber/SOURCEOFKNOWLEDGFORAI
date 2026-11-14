---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-tooltip-on-hover-no-javascript/"
title: "Tailwind CSS Tooltip on Hover (No JavaScript)"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Glossary tooltips for a pricing page: each dotted term is a real <button> whose bubble is after:content-[attr(data-tip)] with a CSS-triangle before: arrow."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Tooltip on Hover (No JavaScript)
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-css-tooltip-on-hover-no-javascript/

Glossary tooltips for a pricing page: each dotted term is a real <button> whose bubble is after:content-[attr(data-tip)] with a CSS-triangle before: arrow. Hover waits 350ms (hover:after:delay-350) to ignore drive-by cursors; focus and tap show it instantly. Screen readers get the same text via aria-describedby.
## HTML
```html
<section class="tth-28 w-full min-h-svh grid place-items-center bg-tth28-bg px-5 py-14 font-tth28-sans text-tth28-ink" aria-label="CSS tooltip text reveal demo">
  <div class="w-full max-w-[38.75rem] rounded-[20px] border border-tth28-line bg-white p-[clamp(24px,4.6vw,40px)] shadow-[0_20px_60px_oklch(0.4_0.05_245/0.1)]">
    <div class="flex items-center justify-between gap-3">
      <p class="text-[11.5px] font-bold uppercase tracking-[0.2em] text-tth28-acc">Ledgerline &mdash; what's in the Pro tier</p>
      <span class="rounded-full bg-tth28-acc/10 px-2.5 py-1 text-[11px] font-bold text-tth28-acc">PRO</span>
    </div>
    <h2 class="mt-2 text-[clamp(22px,3.8vw,30px)] font-extrabold tracking-[-0.02em]">Every export, explained on hover</h2>
    <ul class="mt-[18px] flex flex-col">
      <li class="border-b border-tth28-line px-0.5 py-3.5 text-[16.5px] leading-[1.75] text-tth28-mut">Nightly <button type="button" data-tip="Data copied straight from disk to network — no serialization step, no CPU spike at 2am." aria-describedby="tth28-d1" class="relative inline cursor-help border-0 border-b-2 border-dotted border-tth28-acc bg-transparent pb-px font-[inherit] font-bold text-tth28-ink transition-colors duration-200 hover:text-tth28-acc focus:text-tth28-acc focus-visible:rounded-[2px] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth28-acc before:pointer-events-none before:absolute before:bottom-[calc(100%+5px)] before:left-1/2 before:z-10 before:-translate-x-1/2 before:translate-y-1.5 before:border-6 before:border-transparent before:border-t-tth28-tip before:opacity-0 before:transition-[opacity,translate] before:duration-220 before:content-[''] after:pointer-events-none after:absolute after:bottom-[calc(100%+11px)] after:left-1/2 after:z-10 after:w-max after:max-w-[28ch] after:-translate-x-1/2 after:translate-y-1.5 after:scale-94 after:rounded-[10px] after:bg-tth28-tip after:px-[13px] after:py-2.5 after:text-left after:text-[12.5px] after:font-medium after:leading-[1.55] after:text-tth28-tip-ink after:opacity-0 after:shadow-[0_12px_30px_oklch(0.2_0.03_255/0.35)] after:transition-[opacity,translate,scale] after:duration-220 after:content-[attr(data-tip)] hover:before:translate-y-0 hover:before:opacity-100 hover:before:delay-350 hover:after:translate-y-0 hover:after:scale-100 hover:after:opacity-100 hover:after:delay-350 focus:before:translate-y-0 focus:before:opacity-100 focus:before:delay-0 focus:after:translate-y-0 focus:after:scale-100 focus:after:opacity-100 focus:after:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">zero-copy exports<span id="tth28-d1" class="sr-only">Data copied straight from disk to network — no serialization step, no CPU spike at 2am.</span></button> to your warehouse.</li>
      <li class="border-b border-tth28-line px-0.5 py-3.5 text-[16.5px] leading-[1.75] text-tth28-mut">Ledgers stay consistent under <button type="button" data-tip="Multiple writers land in one agreed order — nobody's Tuesday overwrites somebody's Monday." aria-describedby="tth28-d2" class="relative inline cursor-help border-0 border-b-2 border-dotted border-tth28-acc bg-transparent pb-px font-[inherit] font-bold text-tth28-ink transition-colors duration-200 hover:text-tth28-acc focus:text-tth28-acc focus-visible:rounded-[2px] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth28-acc before:pointer-events-none before:absolute before:bottom-[calc(100%+5px)] before:left-1/2 before:z-10 before:-translate-x-1/2 before:translate-y-1.5 before:border-6 before:border-transparent before:border-t-tth28-tip before:opacity-0 before:transition-[opacity,translate] before:duration-220 before:content-[''] after:pointer-events-none after:absolute after:bottom-[calc(100%+11px)] after:left-1/2 after:z-10 after:w-max after:max-w-[28ch] after:-translate-x-1/2 after:translate-y-1.5 after:scale-94 after:rounded-[10px] after:bg-tth28-tip after:px-[13px] after:py-2.5 after:text-left after:text-[12.5px] after:font-medium after:leading-[1.55] after:text-tth28-tip-ink after:opacity-0 after:shadow-[0_12px_30px_oklch(0.2_0.03_255/0.35)] after:transition-[opacity,translate,scale] after:duration-220 after:content-[attr(data-tip)] hover:before:translate-y-0 hover:before:opacity-100 hover:before:delay-350 hover:after:translate-y-0 hover:after:scale-100 hover:after:opacity-100 hover:after:delay-350 focus:before:translate-y-0 focus:before:opacity-100 focus:before:delay-0 focus:after:translate-y-0 focus:after:scale-100 focus:after:opacity-100 focus:after:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">multi-writer ordering<span id="tth28-d2" class="sr-only">Multiple writers land in one agreed order — nobody's Tuesday overwrites somebody's Monday.</span></button> at any scale.</li>
      <li class="border-b border-tth28-line px-0.5 py-3.5 text-[16.5px] leading-[1.75] text-tth28-mut">Vaults are <button type="button" data-tip="Your data never leaves the region you pinned it to. Auditors love this one weird trick." aria-describedby="tth28-d3" class="relative inline cursor-help border-0 border-b-2 border-dotted border-tth28-acc bg-transparent pb-px font-[inherit] font-bold text-tth28-ink transition-colors duration-200 hover:text-tth28-acc focus:text-tth28-acc focus-visible:rounded-[2px] focus-visible:outline-2 focus-visible:outline-offset-[3px] focus-visible:outline-tth28-acc before:pointer-events-none before:absolute before:bottom-[calc(100%+5px)] before:left-1/2 before:z-10 before:-translate-x-1/2 before:translate-y-1.5 before:border-6 before:border-transparent before:border-t-tth28-tip before:opacity-0 before:transition-[opacity,translate] before:duration-220 before:content-[''] after:pointer-events-none after:absolute after:bottom-[calc(100%+11px)] after:left-1/2 after:z-10 after:w-max after:max-w-[28ch] after:-translate-x-1/2 after:translate-y-1.5 after:scale-94 after:rounded-[10px] after:bg-tth28-tip after:px-[13px] after:py-2.5 after:text-left after:text-[12.5px] after:font-medium after:leading-[1.55] after:text-tth28-tip-ink after:opacity-0 after:shadow-[0_12px_30px_oklch(0.2_0.03_255/0.35)] after:transition-[opacity,translate,scale] after:duration-220 after:content-[attr(data-tip)] hover:before:translate-y-0 hover:before:opacity-100 hover:before:delay-350 hover:after:translate-y-0 hover:after:scale-100 hover:after:opacity-100 hover:after:delay-350 focus:before:translate-y-0 focus:before:opacity-100 focus:before:delay-0 focus:after:translate-y-0 focus:after:scale-100 focus:after:opacity-100 focus:after:delay-0 motion-reduce:before:transition-none motion-reduce:after:transition-none">region-pinned<span id="tth28-d3" class="sr-only">Your data never leaves the region you pinned it to. Auditors love this one weird trick.</span></button> by default.</li>
    </ul>
    <p class="mt-4 text-[12.5px] leading-[1.7] text-tth28-mut">Hover a dotted term (350ms intent delay), tap it, or <kbd class="rounded-[5px] border border-b-2 border-tth28-line bg-tth28-bg px-1.5 py-0.5 font-tth28-mono text-[11px]">Tab</kbd> to it (instant). Bubble = <code class="rounded bg-tth28-chip px-1.5 py-px font-tth28-mono text-[0.9em]">after:content-[attr(data-tip)]</code>; screen readers get <code class="rounded bg-tth28-chip px-1.5 py-px font-tth28-mono text-[0.9em]">aria-describedby</code>.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth28-bg: #f4f7f9;
  --color-tth28-bg: oklch(0.97 0.005 230);
  --color-tth28-chip: #eaeef3;
  --color-tth28-chip: oklch(0.94 0.006 240);
  --color-tth28-ink: #1c2433;
  --color-tth28-ink: oklch(0.25 0.02 250);
  --color-tth28-mut: #586173;
  --color-tth28-mut: oklch(0.48 0.02 250);
  --color-tth28-acc: #1f6fc4;
  --color-tth28-acc: oklch(0.53 0.15 245);
  --color-tth28-line: #dfe4ea;
  --color-tth28-line: oklch(0.9 0.008 240);
  --color-tth28-tip: #1b2232;
  --color-tth28-tip: oklch(0.24 0.02 255);
  --color-tth28-tip-ink: #f1f4f8;
  --color-tth28-tip-ink: oklch(0.96 0.005 240);
  --font-tth28-sans: 'DM Sans', system-ui, sans-serif;
  --font-tth28-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-28 {
  width: 100%;
  min-height: 100svh;
}
```
