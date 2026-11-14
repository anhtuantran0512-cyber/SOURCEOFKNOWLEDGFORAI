---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-text-swap-and-flip-up-hover-effect/"
title: "Tailwind Text Swap and Flip Up Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "The agency-site nav where each word slides up and a twin slides in from below — here an English/Japanese pair — plus a real 3D rolodex: a transform-3d prism…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Text Swap and Flip Up Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-text-swap-and-flip-up-hover-effect/

The agency-site nav where each word slides up and a twin slides in from below — here an English/Japanese pair — plus a real 3D rolodex: a transform-3d prism with two faces that rotates -90deg on X. Twins are aria-hidden, so screen readers hear one language.
## HTML
```html
<section class="tth-05 w-full min-h-svh grid place-items-center bg-tth05-bg px-5 py-14 font-tth05-sans text-tth05-ink" aria-label="Text swap and flip up demo">
  <div class="flex w-full max-w-[47rem] flex-col gap-7">
    <header class="flex flex-wrap items-center justify-between gap-3.5 border-b-[1.5px] border-tth05-ink pb-3.5">
      <p class="text-xs font-bold uppercase tracking-[0.22em] text-tth05-mut">Atelier Kōyō &mdash; Kyoto / Melbourne</p>
      <span class="rounded-full border border-tth05-acc/40 px-3 py-1.5 font-tth05-mono text-[11px] text-tth05-acc">EN &harr; JA on hover</span>
    </header>
    <nav class="flex flex-wrap gap-[clamp(6px,1.6vw,14px)]" aria-label="Primary">
      <a id="tth05-top" href="#tth05-top" class="group/swap relative inline-block overflow-clip rounded-lg px-[0.45em] py-[0.3em] text-[clamp(26px,5.4vw,44px)] font-extrabold leading-[1.15] tracking-[-0.02em] no-underline transition-colors duration-300 hover:bg-tth05-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tth05-acc"><span class="block transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:-translate-y-[150%] group-focus-visible/swap:-translate-y-[150%] motion-reduce:transition-none">Works</span><span aria-hidden="true" lang="ja" class="absolute inset-x-[0.45em] inset-y-[0.3em] block translate-y-[150%] font-tth05-ja text-tth05-acc transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:translate-y-0 group-focus-visible/swap:translate-y-0 motion-reduce:transition-none">作品</span></a>
      <a href="#tth05-top" class="group/swap relative inline-block overflow-clip rounded-lg px-[0.45em] py-[0.3em] text-[clamp(26px,5.4vw,44px)] font-extrabold leading-[1.15] tracking-[-0.02em] no-underline transition-colors duration-300 hover:bg-tth05-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tth05-acc"><span class="block transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:-translate-y-[150%] group-focus-visible/swap:-translate-y-[150%] motion-reduce:transition-none">Studio</span><span aria-hidden="true" lang="ja" class="absolute inset-x-[0.45em] inset-y-[0.3em] block translate-y-[150%] font-tth05-ja text-tth05-acc transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:translate-y-0 group-focus-visible/swap:translate-y-0 motion-reduce:transition-none">工房</span></a>
      <a href="#tth05-top" class="group/swap relative inline-block overflow-clip rounded-lg px-[0.45em] py-[0.3em] text-[clamp(26px,5.4vw,44px)] font-extrabold leading-[1.15] tracking-[-0.02em] no-underline transition-colors duration-300 hover:bg-tth05-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tth05-acc"><span class="block transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:-translate-y-[150%] group-focus-visible/swap:-translate-y-[150%] motion-reduce:transition-none">Journal</span><span aria-hidden="true" lang="ja" class="absolute inset-x-[0.45em] inset-y-[0.3em] block translate-y-[150%] font-tth05-ja text-tth05-acc transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:translate-y-0 group-focus-visible/swap:translate-y-0 motion-reduce:transition-none">日誌</span></a>
      <a href="#tth05-top" class="group/swap relative inline-block overflow-clip rounded-lg px-[0.45em] py-[0.3em] text-[clamp(26px,5.4vw,44px)] font-extrabold leading-[1.15] tracking-[-0.02em] no-underline transition-colors duration-300 hover:bg-tth05-ink/5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tth05-acc"><span class="block transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:-translate-y-[150%] group-focus-visible/swap:-translate-y-[150%] motion-reduce:transition-none">Contact</span><span aria-hidden="true" lang="ja" class="absolute inset-x-[0.45em] inset-y-[0.3em] block translate-y-[150%] font-tth05-ja text-tth05-acc transition-transform duration-450 ease-[cubic-bezier(.76,0,.24,1)] group-hover/swap:translate-y-0 group-focus-visible/swap:translate-y-0 motion-reduce:transition-none">連絡</span></a>
    </nav>
    <div class="flex flex-wrap items-center gap-[clamp(14px,3vw,24px)]">
      <a href="#tth05-top" aria-label="Commissions, open for autumn" class="group/roll inline-flex min-h-12 items-center rounded-full border-[1.5px] border-tth05-ink px-6 no-underline perspective-[900px] transition-colors duration-300 hover:border-tth05-acc hover:bg-tth05-acc/8 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tth05-acc">
        <span aria-hidden="true" class="relative block h-[1em] text-[clamp(19px,3vw,25px)] font-bold leading-none transform-3d transition-transform duration-550 ease-[cubic-bezier(.68,-0.15,.27,1.15)] group-hover/roll:rotate-x-[-90deg] group-focus-visible/roll:rotate-x-[-90deg] motion-reduce:transition-none">
          <span class="flex h-[1em] items-center whitespace-nowrap text-tth05-ink translate-z-[0.52em] backface-hidden">Commissions</span>
          <span class="absolute inset-0 flex h-[1em] items-center whitespace-nowrap text-tth05-acc rotate-x-90 translate-z-[0.52em] backface-hidden">Open for autumn</span>
        </span>
      </a>
      <p class="text-[13px] text-tth05-mut">&larr; the rolodex: a real <code class="rounded bg-tth05-ink/7 px-1.5 py-px font-tth05-mono text-[0.9em]">rotate-x</code> prism, not a slide</p>
    </div>
    <p class="text-[12.5px] text-tth05-mut">Hover or <kbd class="rounded-[5px] border border-b-2 border-tth05-line bg-white px-1.5 py-0.5 font-tth05-mono text-[11px]">Tab</kbd>. The Japanese twins are <code class="rounded bg-tth05-ink/7 px-1.5 py-px font-tth05-mono text-[0.9em]">aria-hidden</code> &mdash; screen readers hear one language, not both.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth05-bg: #f5f6f1;
  --color-tth05-bg: oklch(0.968 0.005 110);
  --color-tth05-ink: #1d211b;
  --color-tth05-ink: oklch(0.23 0.012 130);
  --color-tth05-mut: #5b6157;
  --color-tth05-mut: oklch(0.47 0.015 125);
  --color-tth05-acc: #2d8a4a;
  --color-tth05-acc: oklch(0.54 0.15 145);
  --color-tth05-line: #dcdfd6;
  --color-tth05-line: oklch(0.885 0.01 115);
  --font-tth05-sans: 'Syne', system-ui, sans-serif;
  --font-tth05-ja: 'Zen Kaku Gothic New', 'Hiragino Sans', sans-serif;
  --font-tth05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tth-05 {
  width: 100%;
  min-height: 100svh;
}
```
