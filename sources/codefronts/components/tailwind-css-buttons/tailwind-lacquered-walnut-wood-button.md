---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-lacquered-walnut-wood-button/"
title: "Tailwind Lacquered Walnut Wood Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Book-matched walnut under high-gloss lacquer: grain from four repeating gradients at incommensurate frequencies so it never visibly tiles, a brass inlay…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Lacquered Walnut Wood Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-lacquered-walnut-wood-button/

Book-matched walnut under high-gloss lacquer: grain from four repeating gradients at incommensurate frequencies so it never visibly tiles, a brass inlay label cut with background-clip:text, and a gloss band that travels across the finish on hover.
## HTML
```html
<div class="tb-25 w-full min-h-svh grid place-items-center font-tb25-serif p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-25__veneer group relative overflow-hidden isolate cursor-pointer min-h-16 px-10 border border-tb25-edge rounded-[0.65rem] text-xl font-semibold tracking-[0.06em] text-tb25-brass shadow-[inset_0_1px_0_#ffffff38,inset_0_-2px_4px_#00000073,0_16px_30px_-14px_#000000cc] transition-[translate,box-shadow,filter] duration-[220ms] ease-tb25-out before:content-[''] before:absolute before:inset-x-0 before:top-0 before:h-[38%] before:z-20 before:pointer-events-none before:rounded-t-[0.65rem] before:bg-[linear-gradient(180deg,rgba(255,255,255,0.16),transparent)] hover:-translate-y-0.5 hover:brightness-105 active:translate-y-px active:shadow-[inset_0_3px_8px_#00000099] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tb25-brass disabled:cursor-not-allowed disabled:grayscale-[0.6] disabled:brightness-80 motion-reduce:transition-none">
    <span aria-hidden="true" class="absolute -inset-y-[20%] -inset-x-[30%] z-20 pointer-events-none -translate-x-[60%] bg-[linear-gradient(104deg,transparent_40%,rgba(255,255,255,0.34)_50%,transparent_60%)] transition-transform duration-[900ms] ease-tb25-out group-hover:translate-x-[60%] group-focus-visible:translate-x-[60%] motion-reduce:hidden"></span>
    <span class="tb-25__inlay relative z-30 bg-[linear-gradient(180deg,#f6e3ae,#c99f4f_55%,#8d6a2c)] bg-clip-text text-transparent drop-shadow-[0_1px_0_#00000099]">Open the cabinet</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb25-bg: #120d09;
  --color-tb25-bg: oklch(0.15 0.02 55);
  --color-tb25-wood: #5b3a1f;
  --color-tb25-wood: oklch(0.38 0.07 55);
  --color-tb25-wood-hi: #7d5229;
  --color-tb25-wood-hi: oklch(0.47 0.08 58);
  --color-tb25-wood-lo: #33200f;
  --color-tb25-wood-lo: oklch(0.25 0.05 52);
  --color-tb25-edge: #22150b;
  --color-tb25-edge: oklch(0.18 0.03 52);
  --color-tb25-brass: #e8cd97;
  --color-tb25-brass: oklch(0.86 0.06 85);
  --font-tb25-serif: "Cormorant Garamond", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb25-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(40rem 24rem at 50% 40%, color-mix(in oklab, #d8a55e 12%, transparent), transparent 70%), var(--color-tb25-bg);
}
/* THE VENEER: four repeating gradients at 3/7/11/23px periods, each 1-3° off the
   others so the grain wanders instead of tiling. Meaningless as separate values. */

.tb-25__veneer {
  background-color: var(--color-tb25-wood);
  background-image: repeating-linear-gradient(92deg, rgba(0,0,0,.14) 0 1px, transparent 1px 3px), repeating-linear-gradient(88deg, rgba(0,0,0,.10) 0 2px, transparent 2px 7px), repeating-linear-gradient(91deg, rgba(255,255,255,.055) 0 1px, transparent 1px 11px), repeating-linear-gradient(89deg, rgba(0,0,0,.16) 0 3px, transparent 3px 23px), linear-gradient(100deg, var(--color-tb25-wood-hi), var(--color-tb25-wood) 45%, var(--color-tb25-wood-lo));
}

@media (prefers-color-scheme: light) {
  .tb-25:not([data-theme="dark"]) {
    --color-tb25-bg: oklch(0.22 0.025 52);
  }
}

.tb-25[data-theme="light"] {
  --color-tb25-bg: oklch(0.22 0.025 52);
}

@media (forced-colors: active) {
  .tb-25__veneer {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .tb-25__inlay {
    background: none;
    color: ButtonText;
    -webkit-text-fill-color: ButtonText;
    filter: none;
  }

  .tb-25__veneer span[aria-hidden] {
    display: none;
  }
}
```
