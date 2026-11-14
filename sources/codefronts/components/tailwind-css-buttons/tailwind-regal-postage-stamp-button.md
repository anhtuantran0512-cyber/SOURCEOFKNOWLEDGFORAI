---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-regal-postage-stamp-button/"
title: "Tailwind Regal Postage Stamp Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A commemorative stamp with true perforations on all four edges, an engraved portrait in sepia, a denomination cartouche, and a postmark that lands across the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Regal Postage Stamp Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-regal-postage-stamp-button/

A commemorative stamp with true perforations on all four edges, an engraved portrait in sepia, a denomination cartouche, and a postmark that lands across the corner on hover — concentric rings plus a wavy cancellation bar, rotated and off-centre.
## HTML
```html
<div class="tb-45 w-full min-h-svh grid place-items-center font-tb45-body p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-45__stamp group relative cursor-pointer border-0 p-2 w-54 text-center text-tb45-ink bg-[linear-gradient(165deg,var(--color-tb45-stock),var(--color-tb45-stock-lo))] drop-shadow-[0_12px_18px_#0000008c] transition-[translate,rotate,filter] duration-[320ms] ease-tb45-out [-webkit-tap-highlight-color:transparent] hover:-translate-y-[3px] hover:-rotate-[1.2deg] hover:drop-shadow-[0_20px_26px_#00000099] focus-visible:-translate-y-[3px] focus-visible:-rotate-[1.2deg] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb45-accent active:translate-y-px active:rotate-0 disabled:cursor-not-allowed disabled:grayscale-[0.6] disabled:opacity-75 motion-reduce:transition-none">
    <span class="grid gap-2 px-2.5 pt-3 pb-2.5 border border-tb45-frame">
      <span class="tb-45__win block aspect-[7/5] overflow-hidden">
        <img src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Engraved view of a European cathedral square" width="700" height="500" loading="lazy" decoding="async" class="block size-full object-cover sepia-[0.72] contrast-125 saturate-[0.7] brightness-95">
      </span>
      <span class="grid gap-0.5">
        <span class="font-tb45-serif text-[0.6875rem] tracking-[0.18em] uppercase text-tb45-accent">Post &amp; Telegraph</span>
        <span class="font-tb45-serif text-[0.9375rem] font-semibold tracking-[0.03em]">Send the letter</span>
      </span>
    </span>
    <span class="absolute top-4 right-4 px-1.5 py-0.5 rounded-[0.1rem] font-tb45-serif text-[0.9375rem] font-bold leading-none tabular-nums text-tb45-stock bg-tb45-accent">7½<small class="text-[0.6875rem]">d</small></span>
    <span aria-hidden="true" class="absolute left-3.5 top-5.5 size-26 pointer-events-none -rotate-16 scale-150 opacity-0 transition-[scale,opacity] duration-[380ms] ease-[cubic-bezier(0.2,1.5,0.4,1)] group-hover:scale-100 group-hover:opacity-[0.72] group-focus-visible:scale-100 group-focus-visible:opacity-[0.72] motion-reduce:transition-opacity motion-reduce:duration-150 motion-reduce:scale-100">
      <span class="absolute inset-0 rounded-full border-2 border-tb45-mark"></span>
      <span class="absolute inset-[12%] rounded-full border border-tb45-mark"></span>
      <span class="tb-45__bar absolute -inset-x-[25%] top-[46%] h-3.5 opacity-85"></span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb45-bg: #20211c;
  --color-tb45-bg: oklch(0.25 0.012 110);
  --color-tb45-stock: #f0e6cf;
  --color-tb45-stock: oklch(0.93 0.03 88);
  --color-tb45-stock-lo: #ddd0b3;
  --color-tb45-stock-lo: oklch(0.86 0.04 86);
  --color-tb45-ink: #2d2a1f;
  --color-tb45-ink: oklch(0.27 0.02 95);
  --color-tb45-frame: #2d2a1f59;
  --color-tb45-frame: oklch(0.27 0.02 95 / 0.35);
  --color-tb45-accent: #6d3526;
  --color-tb45-accent: oklch(0.38 0.09 38);
  --color-tb45-mark: #2c3a4a;
  --color-tb45-mark: oklch(0.33 0.04 245);
  --font-tb45-serif: "Cinzel", ui-serif, Georgia, "Times New Roman", serif;
  --font-tb45-body: "EB Garamond", ui-serif, Georgia, serif;
  --ease-tb45-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-45 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(32rem 20rem at 50% 40%, rgba(255,255,255,.06), transparent 72%), var(--color-tb45-bg);
}
/* PERFORATION on four edges: opaque dot columns/rows XOR-ed against a solid base.
   Exclude subtracts each dot; where two edges overlap at a corner, parity keeps
   the metal — real stamps have that quirk too. */

.tb-45__stamp {
  -webkit-mask: radial-gradient(.3rem .3rem at 50% 0, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 50% 100%, #000 96%, transparent 0) 0 100%/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-y, radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% 0/.62rem .62rem repeat-y, linear-gradient(#000, #000);
  mask: radial-gradient(.3rem .3rem at 50% 0, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 50% 100%, #000 96%, transparent 0) 0 100%/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-y, radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% 0/.62rem .62rem repeat-y, linear-gradient(#000, #000);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}
/* The flat fallback stays a legible engraved-looking plate if the photo 404s. */

.tb-45__win {
  background: repeating-linear-gradient(28deg, color-mix(in oklab, var(--color-tb45-ink) 30%, transparent) 0 1px, transparent 1px 5px), color-mix(in oklab, var(--color-tb45-ink) 18%, var(--color-tb45-stock));
}
/* CANCELLATION BAR: a striped bar with a scalloped top edge. */

.tb-45__bar {
  background: repeating-linear-gradient(0deg, var(--color-tb45-mark) 0 2px, transparent 2px 5px);
  -webkit-mask: radial-gradient(.4rem .35rem at 50% 0, transparent 96%, #000 0) 0 0/.8rem .9rem repeat-x;
  mask: radial-gradient(.4rem .35rem at 50% 0, transparent 96%, #000 0) 0 0/.8rem .9rem repeat-x;
}

@media (prefers-color-scheme: light) {
  .tb-45:not([data-theme="dark"]) {
    --color-tb45-bg: oklch(0.31 0.015 110);
  }
}

.tb-45[data-theme="light"] {
  --color-tb45-bg: oklch(0.31 0.015 110);
}

@media (forced-colors: active) {
  .tb-45__stamp {
    mask: none;
    -webkit-mask: none;
    filter: none;
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .tb-45__stamp span[aria-hidden] {
    display: none;
  }
}
```
