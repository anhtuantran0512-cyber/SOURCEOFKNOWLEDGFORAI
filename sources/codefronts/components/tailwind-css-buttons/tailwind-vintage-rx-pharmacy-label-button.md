---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-rx-pharmacy-label-button/"
title: "Tailwind Vintage Rx Pharmacy Label Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "An apothecary label on aged amber stock: typewriter setting with a red rule, a serrated tear edge along the top, and a rubber \"REFILL\" stamp that thuds in at…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vintage Rx Pharmacy Label Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-vintage-rx-pharmacy-label-button/

An apothecary label on aged amber stock: typewriter setting with a red rule, a serrated tear edge along the top, and a rubber "REFILL" stamp that thuds in at an angle on hover — off-register and unevenly inked, the way a real stamp lands.
## HTML
```html
<div class="tb-43 w-full min-h-svh grid place-items-center font-tb43-mono p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-43__label group relative overflow-hidden cursor-pointer grid gap-2 justify-items-start w-[min(100%,22rem)] px-5.5 pt-5 pb-5 border-0 rounded-[0.15rem] text-left text-tb43-ink drop-shadow-[0_12px_18px_#00000080] transition-[translate,filter] duration-300 ease-tb43-out [-webkit-tap-highlight-color:transparent] hover:-translate-y-0.5 hover:drop-shadow-[0_18px_24px_#0000008c] focus-visible:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb43-rule active:translate-y-px disabled:cursor-not-allowed disabled:grayscale-50 disabled:opacity-70 motion-reduce:transition-none">
    <span class="flex items-baseline gap-2.5 mt-1.5">
      <span class="font-tb43-slab text-2xl leading-none text-tb43-rule">℞</span>
      <span class="text-xs tracking-[0.1em] uppercase tabular-nums">No. 40218</span>
    </span>
    <span class="relative font-tb43-slab text-[1.35rem] leading-tight tracking-[-0.01em] pb-1.5 after:content-[''] after:absolute after:inset-x-0 after:bottom-0 after:h-0.5 after:bg-tb43-rule">Tincture of Focus</span>
    <span class="text-[0.8125rem] leading-relaxed tabular-nums text-tb43-ink-soft">Take one capsule at dawn · 30 ct · 1953</span>
    <span aria-hidden="true" class="tb-43__stamp absolute right-3.5 bottom-2 px-2.5 py-1 font-tb43-slab text-xl tracking-[0.14em] uppercase text-tb43-stamp border-2 border-tb43-stamp rounded-[0.2rem] -rotate-[14deg] scale-[1.6] opacity-0 transition-[scale,opacity] duration-[340ms] ease-[cubic-bezier(0.2,1.6,0.4,1)] group-hover:scale-100 group-hover:opacity-[0.88] group-focus-visible:scale-100 group-focus-visible:opacity-[0.88] motion-reduce:transition-opacity motion-reduce:duration-150 motion-reduce:scale-100">Refill</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb43-bg: #2b241b;
  --color-tb43-bg: oklch(0.26 0.02 70);
  --color-tb43-paper: #e8d9b0;
  --color-tb43-paper: oklch(0.88 0.05 88);
  --color-tb43-paper-lo: #d6c393;
  --color-tb43-paper-lo: oklch(0.81 0.06 86);
  --color-tb43-ink: #2a2318;
  --color-tb43-ink: oklch(0.25 0.02 75);
  --color-tb43-ink-soft: #443a29;
  --color-tb43-ink-soft: oklch(0.36 0.025 75);
  --color-tb43-rule: #a8321f;
  --color-tb43-rule: oklch(0.48 0.16 33);
  --color-tb43-stamp: #8f2119;
  --color-tb43-stamp: oklch(0.42 0.16 30);
  --font-tb43-mono: "Courier Prime", ui-monospace, "Courier New", Courier, monospace;
  --font-tb43-slab: "Special Elite", ui-monospace, "Courier New", Courier, monospace;
  --ease-tb43-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-43 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 34%, rgba(255,255,255,.06), transparent 72%), var(--color-tb43-bg);
}
/* AGED STOCK: fine grain + two foxing blotches over the amber base.
   SERRATED TEAR: the tooth layer is confined to its own .35rem strip and unioned
   with a base covering everything below — one gradient over the whole box is
   where cross-engine differences show up. */

.tb-43__label {
  background-color: var(--color-tb43-paper);
  background-image: radial-gradient(.05rem .05rem at 30% 42%, rgba(90,70,40,.22) 99%, transparent), radial-gradient(3rem 2rem at 84% 22%, rgba(150,110,50,.16), transparent 72%), radial-gradient(2.4rem 1.8rem at 14% 82%, rgba(150,110,50,.14), transparent 74%), linear-gradient(168deg, var(--color-tb43-paper), var(--color-tb43-paper-lo));
  background-size: 6px 6px, 100% 100%, 100% 100%, 100% 100%;
  -webkit-mask: conic-gradient(from -45deg at 50% 100%, #000 90deg, transparent 0) 0 0/.7rem .35rem repeat-x, linear-gradient(#000, #000) 0 100%/100% calc(100% - .34rem) no-repeat;
  mask: conic-gradient(from -45deg at 50% 100%, #000 90deg, transparent 0) 0 0/.7rem .35rem repeat-x, linear-gradient(#000, #000) 0 100%/100% calc(100% - .34rem) no-repeat;
}
/* UNEVEN INK: a speckle mask INTERSECTED with the stamp — the one place in the
   collection where intersect (not exclude) is the right composite. */

.tb-43__stamp {
  -webkit-mask: radial-gradient(.09rem .09rem at 32% 44%, transparent 99%, #000 0) 0 0/5px 5px, linear-gradient(#000, #000);
  mask: radial-gradient(.09rem .09rem at 32% 44%, transparent 99%, #000 0) 0 0/5px 5px, linear-gradient(#000, #000);
  -webkit-mask-composite: source-in;
  mask-composite: intersect;
}

@media (prefers-color-scheme: light) {
  .tb-43:not([data-theme="dark"]) {
    --color-tb43-bg: oklch(0.32 0.025 70);
  }
}

.tb-43[data-theme="light"] {
  --color-tb43-bg: oklch(0.32 0.025 70);
}

@media (forced-colors: active) {
  .tb-43__label {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .tb-43__stamp {
    color: ButtonText;
    border-color: ButtonText;
    mask: none;
    -webkit-mask: none;
  }
}
```
