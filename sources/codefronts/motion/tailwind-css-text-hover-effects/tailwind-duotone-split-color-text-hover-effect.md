---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-duotone-split-color-text-hover-effect/"
title: "Tailwind Duotone Split Color Text Hover Effect"
section: "motion"
category: "tailwind-css-text-hover-effects"
category_name: "Tailwind CSS Text Hover Effects"
description: "A risograph poster headline printed in two plates: before: and after: both print attr(data-text), clipped to top and bottom halves."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Duotone Split Color Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-text-hover-effects/tailwind-duotone-split-color-text-hover-effect/

A risograph poster headline printed in two plates: before: and after: both print attr(data-text), clipped to top and bottom halves. On hover the plates shear sideways and their clips overlap — with mix-blend-multiply, the overlap band overprints into a third ink, exactly like misregistered riso. Nav buttons split left/right.
## HTML
```html
<section class="tth-27 @container w-full min-h-svh grid place-items-center bg-tth27-bg px-5 py-14 font-tth27-sans text-tth27-ink" aria-label="Duotone split color text demo">
  <div class="flex w-full max-w-[53.75rem] flex-col items-center gap-[clamp(16px,3cqi,26px)] text-center">
    <header class="flex w-full flex-wrap items-center justify-between gap-3.5 border-b-[1.5px] border-tth27-ink pb-3.5">
      <p class="text-xs font-bold uppercase tracking-[0.22em] text-tth27-mut">Riso Press &mdash; open studio night</p>
      <span class="rounded-full border border-tth27-line px-3 py-1.5 font-tth27-mono text-[11px] text-tth27-mut @max-[35rem]:hidden">two plates &middot; one string &middot; attr(data-text)</span>
    </header>
    <h2 data-text="BASEMENT TAPES" class="relative inline-block whitespace-nowrap font-tth27-display text-[clamp(32px,6.2cqi,64px)] leading-[1.08] tracking-[-0.01em] text-transparent selection:bg-tth27-a/30 selection:text-tth27-ink before:pointer-events-none before:absolute before:inset-0 before:text-tth27-a before:mix-blend-multiply before:[clip-path:inset(0_0_50%_0)] before:transition-[clip-path,translate] before:duration-500 before:ease-[cubic-bezier(.25,.8,.25,1)] before:content-[attr(data-text)] after:pointer-events-none after:absolute after:inset-0 after:text-tth27-b after:mix-blend-multiply after:[clip-path:inset(50%_0_0_0)] after:transition-[clip-path,translate] after:duration-500 after:ease-[cubic-bezier(.25,.8,.25,1)] after:content-[attr(data-text)] hover:before:-translate-x-[.045em] hover:before:[clip-path:inset(0_0_40%_0)] hover:after:translate-x-[.045em] hover:after:[clip-path:inset(44%_0_0_0)] motion-reduce:before:transition-none motion-reduce:after:transition-none @max-[40rem]:whitespace-normal">BASEMENT TAPES</h2>
    <p class="font-tth27-mono text-[12.5px] tracking-[0.22em] text-tth27-mut">VOL. IX &mdash; printed loud, aligned rarely</p>
    <nav class="mt-1.5 flex flex-wrap justify-center gap-[clamp(10px,2.4cqi,20px)]" aria-label="Editions">
      <a id="tth27-top" href="#tth27-top" data-text="Prints" class="relative grid min-h-[50px] place-items-center rounded border-2 border-tth27-ink bg-tth27-paper px-[26px] text-[17px] font-bold tracking-[0.02em] text-transparent no-underline shadow-[3px_3px_0_var(--color-tth27-ink)] transition-[translate,box-shadow] duration-300 before:absolute before:inset-0 before:grid before:place-items-center before:text-tth27-a before:mix-blend-multiply before:[clip-path:inset(0_50%_0_0)] before:transition-[clip-path,translate] before:duration-400 before:content-[attr(data-text)] after:absolute after:inset-0 after:grid after:place-items-center after:text-tth27-b after:mix-blend-multiply after:[clip-path:inset(0_0_0_50%)] after:transition-[clip-path,translate] after:duration-400 after:content-[attr(data-text)] hover:-translate-y-0.5 hover:shadow-[4px_5px_0_var(--color-tth27-ink)] hover:before:-translate-y-[.06em] hover:before:[clip-path:inset(0_40%_0_0)] hover:after:translate-y-[.06em] hover:after:[clip-path:inset(0_0_0_44%)] focus-visible:before:[clip-path:inset(0_40%_0_0)] focus-visible:after:[clip-path:inset(0_0_0_44%)] focus-visible:outline-[2.5px] focus-visible:outline-offset-[3px] focus-visible:outline-tth27-a">Prints</a>
      <a href="#tth27-top" data-text="Zines" class="relative grid min-h-[50px] place-items-center rounded border-2 border-tth27-ink bg-tth27-paper px-[26px] text-[17px] font-bold tracking-[0.02em] text-transparent no-underline shadow-[3px_3px_0_var(--color-tth27-ink)] transition-[translate,box-shadow] duration-300 before:absolute before:inset-0 before:grid before:place-items-center before:text-tth27-a before:mix-blend-multiply before:[clip-path:inset(0_50%_0_0)] before:transition-[clip-path,translate] before:duration-400 before:content-[attr(data-text)] after:absolute after:inset-0 after:grid after:place-items-center after:text-tth27-b after:mix-blend-multiply after:[clip-path:inset(0_0_0_50%)] after:transition-[clip-path,translate] after:duration-400 after:content-[attr(data-text)] hover:-translate-y-0.5 hover:shadow-[4px_5px_0_var(--color-tth27-ink)] hover:before:-translate-y-[.06em] hover:before:[clip-path:inset(0_40%_0_0)] hover:after:translate-y-[.06em] hover:after:[clip-path:inset(0_0_0_44%)] focus-visible:before:[clip-path:inset(0_40%_0_0)] focus-visible:after:[clip-path:inset(0_0_0_44%)] focus-visible:outline-[2.5px] focus-visible:outline-offset-[3px] focus-visible:outline-tth27-a">Zines</a>
      <a href="#tth27-top" data-text="Posters" class="relative grid min-h-[50px] place-items-center rounded border-2 border-tth27-ink bg-tth27-paper px-[26px] text-[17px] font-bold tracking-[0.02em] text-transparent no-underline shadow-[3px_3px_0_var(--color-tth27-ink)] transition-[translate,box-shadow] duration-300 before:absolute before:inset-0 before:grid before:place-items-center before:text-tth27-a before:mix-blend-multiply before:[clip-path:inset(0_50%_0_0)] before:transition-[clip-path,translate] before:duration-400 before:content-[attr(data-text)] after:absolute after:inset-0 after:grid after:place-items-center after:text-tth27-b after:mix-blend-multiply after:[clip-path:inset(0_0_0_50%)] after:transition-[clip-path,translate] after:duration-400 after:content-[attr(data-text)] hover:-translate-y-0.5 hover:shadow-[4px_5px_0_var(--color-tth27-ink)] hover:before:-translate-y-[.06em] hover:before:[clip-path:inset(0_40%_0_0)] hover:after:translate-y-[.06em] hover:after:[clip-path:inset(0_0_0_44%)] focus-visible:before:[clip-path:inset(0_40%_0_0)] focus-visible:after:[clip-path:inset(0_0_0_44%)] focus-visible:outline-[2.5px] focus-visible:outline-offset-[3px] focus-visible:outline-tth27-a">Posters</a>
    </nav>
    <p class="max-w-[60ch] text-[12.5px] leading-[1.7] text-tth27-mut">Hover the headline: the plates shear apart and their clips overlap &mdash; <code class="rounded bg-tth27-chip px-1.5 py-px font-tth27-mono text-[0.9em]">mix-blend-multiply</code> overprints the band into a third ink. Links split left/right instead.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tth27-bg: #f5f1e6;
  --color-tth27-bg: oklch(0.955 0.012 85);
  --color-tth27-paper: #fcfaf5;
  --color-tth27-paper: oklch(0.99 0.004 85);
  --color-tth27-chip: #e7e1d4;
  --color-tth27-chip: oklch(0.9 0.01 80);
  --color-tth27-ink: #241f1a;
  --color-tth27-ink: oklch(0.24 0.01 60);
  --color-tth27-mut: #685f56;
  --color-tth27-mut: oklch(0.48 0.02 60);
  --color-tth27-line: #d8d0c2;
  --color-tth27-line: oklch(0.85 0.015 70);
  --color-tth27-a: #e3352b;
  --color-tth27-a: oklch(0.6 0.22 28);
  --color-tth27-b: #2c5bd1;
  --color-tth27-b: oklch(0.52 0.18 262);
  --font-tth27-display: 'Dela Gothic One', system-ui, sans-serif;
  --font-tth27-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tth27-mono: 'Space Mono', ui-monospace, monospace;
}

.tth-27 {
  width: 100%;
  min-height: 100svh;
}
```
