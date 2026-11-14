---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-washi-paper-crane-button/"
title: "Tailwind Washi Paper Crane Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Handmade washi stock with fibrous speckle, a deckled bottom edge cut by a mask, and a folded paper crane whose wing lifts on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Washi Paper Crane Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-washi-paper-crane-button/

Handmade washi stock with fibrous speckle, a deckled bottom edge cut by a mask, and a folded paper crane whose wing lifts on hover. The button tilts on its long axis like a sheet being picked up — and the two-layer mask that tears the edge is the part that stays CSS.
## HTML
```html
<div class="tb-22 w-full min-h-svh grid place-items-center font-tb22-sans p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-22__sheet group relative cursor-pointer inline-grid grid-flow-col items-center gap-3.5 min-h-14 pt-3.5 pb-4.5 px-8 border-0 rounded-[0.35rem] text-base font-medium tracking-[0.03em] text-tb22-ink drop-shadow-[0_10px_14px_var(--color-tb22-shadow)] transition-[rotate,translate,filter] duration-[450ms] ease-tb22-out hover:-rotate-[1.4deg] hover:-translate-y-[3px] hover:drop-shadow-[0_18px_22px_var(--color-tb22-shadow-lift)] focus-visible:-rotate-[1.4deg] focus-visible:-translate-y-[3px] focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb22-accent active:rotate-0 active:translate-y-px active:drop-shadow-[0_4px_6px_var(--color-tb22-shadow)] disabled:cursor-not-allowed disabled:opacity-55 disabled:drop-shadow-none motion-reduce:transition-none motion-reduce:hover:rotate-0 motion-reduce:hover:translate-y-0">
    <span aria-hidden="true" class="relative w-6 h-[1.35rem] shrink-0 bg-tb22-accent [clip-path:polygon(0_68%,52%_8%,100%_46%,60%_100%)] transition-[rotate] duration-500 ease-tb22-out group-hover:-rotate-12 group-focus-visible:-rotate-12 motion-reduce:transition-none">
      <span class="absolute inset-0 bg-tb22-accent-light [clip-path:polygon(6%_62%,52%_10%,58%_62%)] [transform-origin:52%_62%] transition-[rotate] duration-[550ms] ease-tb22-out group-hover:-rotate-[38deg] group-focus-visible:-rotate-[38deg] motion-reduce:transition-none"></span>
    </span>
    <span class="relative z-20">Send a note</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb22-bg: #efe9df;
  --color-tb22-bg: oklch(0.935 0.012 85);
  --color-tb22-paper: #fbf7f0;
  --color-tb22-paper: oklch(0.975 0.01 85);
  --color-tb22-fibre: #cdbfa8;
  --color-tb22-fibre: oklch(0.8 0.022 78);
  --color-tb22-ink: #2c2620;
  --color-tb22-ink: oklch(0.26 0.012 60);
  --color-tb22-accent: #a8503a;
  --color-tb22-accent: oklch(0.52 0.13 35);
  --color-tb22-accent-light: #c98771;
  --color-tb22-accent-light: oklch(0.66 0.1 35);
  --color-tb22-shadow: #2c262038;
  --color-tb22-shadow: oklch(0.26 0.012 60 / 0.22);
  --color-tb22-shadow-lift: #2c262047;
  --color-tb22-shadow-lift: oklch(0.26 0.012 60 / 0.28);
  --font-tb22-sans: "Zen Maru Gothic", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb22-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(50rem 30rem at 50% 20%, color-mix(in oklab, white 60%, transparent), transparent 65%), var(--color-tb22-bg);
}
/* THE SHEET: fibre speckle (three sub-pixel radial tiles) + a deckled bottom edge.
   The mask is two layers and every size/repeat must be explicit — a missing
   no-repeat tiles the base layer and erases the button. */

.tb-22__sheet {
  background-color: var(--color-tb22-paper);
  background-image: radial-gradient(.05rem .05rem at 12% 24%, color-mix(in oklab, var(--color-tb22-fibre) 45%, transparent) 99%, transparent), radial-gradient(.04rem .04rem at 63% 71%, color-mix(in oklab, var(--color-tb22-fibre) 35%, transparent) 99%, transparent), radial-gradient(.045rem .045rem at 84% 33%, color-mix(in oklab, var(--color-tb22-fibre) 30%, transparent) 99%, transparent), linear-gradient(170deg, color-mix(in oklab, white 30%, transparent), transparent 55%);
  background-size: 9px 9px, 14px 14px, 19px 19px, 100% 100%;
  -webkit-mask: radial-gradient(.42rem .3rem at 50% 100%, transparent 96%, #000 0) 0 100% / 1.15rem .38rem repeat-x, linear-gradient(#000, #000) 0 0 / 100% calc(100% - .37rem) no-repeat;
  mask: radial-gradient(.42rem .3rem at 50% 100%, transparent 96%, #000 0) 0 100% / 1.15rem .38rem repeat-x, linear-gradient(#000, #000) 0 0 / 100% calc(100% - .37rem) no-repeat;
}

@media (prefers-color-scheme: dark) {
  .tb-22:not([data-theme="light"]) {
    --color-tb22-bg: oklch(0.2 0.012 60);
    --color-tb22-paper: oklch(0.26 0.014 60);
    --color-tb22-fibre: oklch(0.42 0.02 60);
    --color-tb22-ink: oklch(0.94 0.014 80);
    --color-tb22-accent: oklch(0.72 0.11 40);
    --color-tb22-accent-light: oklch(0.82 0.08 40);
  }
}

.tb-22[data-theme="dark"] {
  --color-tb22-bg: oklch(0.2 0.012 60);
  --color-tb22-paper: oklch(0.26 0.014 60);
  --color-tb22-ink: oklch(0.94 0.014 80);
  --color-tb22-accent: oklch(0.72 0.11 40);
}

@media (forced-colors: active) {
  .tb-22__sheet {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .tb-22__sheet span[aria-hidden] {
    background: ButtonText;
  }
}
```
