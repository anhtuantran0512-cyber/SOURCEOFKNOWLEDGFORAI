---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-gradient-text-hover-effect-bg-clip-text/"
title: "Tailwind Gradient Text Hover Effect with bg-clip-text"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "Solid ink that crossfades into a live gradient: the gradient is always painted behind the glyphs with bg-clip-text, and hover just fades text-tth03-ink to…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Text Hover Effect with bg-clip-text
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-gradient-text-hover-effect-bg-clip-text/

Solid ink that crossfades into a live gradient: the gradient is always painted behind the glyphs with bg-clip-text, and hover just fades text-tth03-ink to text-transparent. Once revealed, a typed --tth03-angle keeps the gradient slowly turning. Each row sets its own two stops with a two-variable style.
## HTML
```html
<section class="tth-03 @container w-full min-h-svh grid place-items-center bg-tth03-bg px-5 py-14 font-tth03-sans text-tth03-ink" aria-label="Gradient text color reveal demo">
  <div class="flex w-full max-w-[52rem] flex-col gap-6">
    <header class="flex flex-wrap items-center justify-between gap-3.5">
      <p class="text-xs font-bold uppercase tracking-[0.24em] text-tth03-mut">Northlight platform &mdash; 2026.3</p>
      <span class="rounded-full border border-tth03-line bg-white px-3 py-1.5 font-tth03-mono text-[11px] text-tth03-mut @max-[35rem]:hidden">text-ink &rarr; text-transparent over bg-clip-text</span>
    </header>
    <ol class="border-t-[1.5px] border-tth03-ink">
      <li class="border-b border-tth03-line"><a id="tth03-top" href="#tth03-top" style="--tth03-from:oklch(0.68 0.21 25);--tth03-to:oklch(0.76 0.17 65)" class="flex items-baseline gap-[clamp(14px,3cqi,26px)] rounded-[3px] px-1 py-[clamp(14px,2.6cqi,22px)] text-[clamp(26px,5.4cqi,46px)] font-extrabold leading-[1.12] tracking-[-0.025em] no-underline bg-[linear-gradient(var(--tth03-angle),var(--tth03-from),var(--tth03-to))] bg-clip-text text-tth03-ink transition-[color,translate] duration-500 ease-[cubic-bezier(.22,1,.36,1)] hover:translate-x-1.5 hover:text-transparent hover:animate-tth03-turn focus-visible:text-transparent focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth03-ink motion-reduce:transition-none motion-reduce:animate-none!"><small class="font-tth03-mono text-xs font-semibold tracking-[0.08em] [-webkit-text-fill-color:var(--color-tth03-mut)]">001</small>Realtime ledger sync</a></li>
      <li class="border-b border-tth03-line"><a href="#tth03-top" style="--tth03-from:oklch(0.7 0.17 150);--tth03-to:oklch(0.74 0.14 210)" class="flex items-baseline gap-[clamp(14px,3cqi,26px)] rounded-[3px] px-1 py-[clamp(14px,2.6cqi,22px)] text-[clamp(26px,5.4cqi,46px)] font-extrabold leading-[1.12] tracking-[-0.025em] no-underline bg-[linear-gradient(var(--tth03-angle),var(--tth03-from),var(--tth03-to))] bg-clip-text text-tth03-ink transition-[color,translate] duration-500 ease-[cubic-bezier(.22,1,.36,1)] hover:translate-x-1.5 hover:text-transparent hover:animate-tth03-turn focus-visible:text-transparent focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth03-ink motion-reduce:transition-none motion-reduce:animate-none!"><small class="font-tth03-mono text-xs font-semibold tracking-[0.08em] [-webkit-text-fill-color:var(--color-tth03-mut)]">002</small>Anomaly-aware alerts</a></li>
      <li class="border-b border-tth03-line"><a href="#tth03-top" style="--tth03-from:oklch(0.6 0.22 300);--tth03-to:oklch(0.68 0.2 345)" class="flex items-baseline gap-[clamp(14px,3cqi,26px)] rounded-[3px] px-1 py-[clamp(14px,2.6cqi,22px)] text-[clamp(26px,5.4cqi,46px)] font-extrabold leading-[1.12] tracking-[-0.025em] no-underline bg-[linear-gradient(var(--tth03-angle),var(--tth03-from),var(--tth03-to))] bg-clip-text text-tth03-ink transition-[color,translate] duration-500 ease-[cubic-bezier(.22,1,.36,1)] hover:translate-x-1.5 hover:text-transparent hover:animate-tth03-turn focus-visible:text-transparent focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth03-ink motion-reduce:transition-none motion-reduce:animate-none!"><small class="font-tth03-mono text-xs font-semibold tracking-[0.08em] [-webkit-text-fill-color:var(--color-tth03-mut)]">003</small>Zero-copy exports</a></li>
      <li class="border-b border-tth03-line"><a href="#tth03-top" style="--tth03-from:oklch(0.62 0.18 255);--tth03-to:oklch(0.74 0.14 195)" class="flex items-baseline gap-[clamp(14px,3cqi,26px)] rounded-[3px] px-1 py-[clamp(14px,2.6cqi,22px)] text-[clamp(26px,5.4cqi,46px)] font-extrabold leading-[1.12] tracking-[-0.025em] no-underline bg-[linear-gradient(var(--tth03-angle),var(--tth03-from),var(--tth03-to))] bg-clip-text text-tth03-ink transition-[color,translate] duration-500 ease-[cubic-bezier(.22,1,.36,1)] hover:translate-x-1.5 hover:text-transparent hover:animate-tth03-turn focus-visible:text-transparent focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth03-ink motion-reduce:transition-none motion-reduce:animate-none!"><small class="font-tth03-mono text-xs font-semibold tracking-[0.08em] [-webkit-text-fill-color:var(--color-tth03-mut)]">004</small>Region-pinned vaults</a></li>
    </ol>
    <p class="text-[12.5px] text-tth03-mut">Hover or <kbd class="rounded-[5px] border border-b-2 border-tth03-line bg-white px-1.5 py-0.5 font-tth03-mono text-[11px]">Tab</kbd>: solid ink crossfades to a live gradient &mdash; and the gradient keeps slowly turning while you stay.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tth03-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 100deg;
}

@theme {
  --color-tth03-bg: #f4f5f8;
  --color-tth03-bg: oklch(0.965 0.005 250);
  --color-tth03-ink: #1c1f27;
  --color-tth03-ink: oklch(0.24 0.015 260);
  --color-tth03-mut: #5e636e;
  --color-tth03-mut: oklch(0.49 0.015 255);
  --color-tth03-line: #dcdee4;
  --color-tth03-line: oklch(0.89 0.008 250);
  --font-tth03-sans: 'Geist', system-ui, sans-serif;
  --font-tth03-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tth03-turn: tth03-turn 4s ease-in-out 0.5s infinite alternate;

  @keyframes tth03-turn {
    from {
      --tth03-angle: 100deg;
    }

    to {
      --tth03-angle: 220deg;
    }
  }
}

.tth-03 {
  width: 100%;
  min-height: 100svh;
}
```
