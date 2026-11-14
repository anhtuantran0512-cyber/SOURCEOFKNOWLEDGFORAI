---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-masking-tape-label-button/"
title: "Tailwind Masking Tape Label Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A strip of drafting tape stuck slightly crooked: translucent so the surface shows through, fibrous weave running lengthwise, ragged torn ends cut by a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Masking Tape Label Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-masking-tape-label-button/

A strip of drafting tape stuck slightly crooked: translucent so the surface shows through, fibrous weave running lengthwise, ragged torn ends cut by a repeating mask, and a hand-written label. Hover presses the tape flatter; pressing sticks it down.
## HTML
```html
<div class="tb-33 w-full min-h-svh grid place-items-center font-tb33-hand p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-33__tape group cursor-pointer border-0 px-10 py-3.5 rounded-none text-2xl font-semibold tracking-[0.01em] text-tb33-ink -rotate-[1.7deg] drop-shadow-[0_4px_5px_#3c301e47] transition-[rotate,translate,filter] duration-[400ms] ease-tb33-out [-webkit-tap-highlight-color:transparent] hover:-rotate-[0.4deg] hover:-translate-y-0.5 hover:drop-shadow-[0_8px_9px_#3c301e4d] focus-visible:-rotate-[0.4deg] focus-visible:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-dashed focus-visible:outline-tb33-ink focus-visible:outline-offset-4 active:-rotate-[1.2deg] active:translate-y-px active:drop-shadow-[0_2px_2px_#3c301e4d] disabled:cursor-not-allowed disabled:opacity-60 disabled:drop-shadow-none motion-reduce:transition-none motion-reduce:hover:rotate-0">
    <span class="inline-block transition-[rotate] duration-[400ms] ease-tb33-out group-hover:rotate-[0.6deg] group-focus-visible:rotate-[0.6deg] motion-reduce:transition-none">pin this for later</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb33-bg: #dfd8c8;
  --color-tb33-bg: oklch(0.88 0.022 88);
  --color-tb33-tape: #eee2bee6;
  --color-tb33-tape-2: #decea4eb;
  --color-tb33-ink: #33291c;
  --color-tb33-ink: oklch(0.27 0.025 75);
  --color-tb33-grid: #0000000a;
  --font-tb33-hand: "Caveat", ui-rounded, "Comic Sans MS", cursive;
  --ease-tb33-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-33 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: repeating-linear-gradient(0deg, var(--color-tb33-grid) 0 1px, transparent 1px 1.75rem), repeating-linear-gradient(90deg, var(--color-tb33-grid) 0 1px, transparent 1px 1.75rem), var(--color-tb33-bg);
}
/* THE TAPE: translucent base + lengthwise weave (2px and 5px) + diagonal sheen,
   then a three-layer mask that tears both ends. Every mask layer needs its own
   size and repeat — a missing no-repeat tiles the base and eats the tape. */

.tb-33__tape {
  background-color: var(--color-tb33-tape);
  background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.22) 0 1px, transparent 1px 2px), repeating-linear-gradient(90deg, rgba(0,0,0,.045) 0 1px, transparent 1px 5px), linear-gradient(102deg, rgba(255,255,255,.3), transparent 40%, rgba(0,0,0,.07)), linear-gradient(180deg, var(--color-tb33-tape), var(--color-tb33-tape-2));
  -webkit-mask: radial-gradient(.22rem .3rem at 0 50%, transparent 96%, #000 0) 0 0/.42rem .5rem repeat-y, radial-gradient(.22rem .3rem at 100% 50%, transparent 96%, #000 0) 100% 0/.42rem .5rem repeat-y, linear-gradient(#000, #000) .4rem 0/calc(100% - .8rem) 100% no-repeat;
  mask: radial-gradient(.22rem .3rem at 0 50%, transparent 96%, #000 0) 0 0/.42rem .5rem repeat-y, radial-gradient(.22rem .3rem at 100% 50%, transparent 96%, #000 0) 100% 0/.42rem .5rem repeat-y, linear-gradient(#000, #000) .4rem 0/calc(100% - .8rem) 100% no-repeat;
}

@media (prefers-color-scheme: dark) {
  .tb-33:not([data-theme="light"]) {
    --color-tb33-bg: oklch(0.22 0.018 80);
    --color-tb33-tape: oklch(0.82 0.05 88 / 0.88);
    --color-tb33-tape-2: oklch(0.75 0.055 85 / 0.9);
    --color-tb33-grid: #ffffff0f;
  }
}

.tb-33[data-theme="dark"] {
  --color-tb33-bg: oklch(0.22 0.018 80);
  --color-tb33-tape: oklch(0.82 0.05 88 / 0.88);
  --color-tb33-grid: #ffffff0f;
}

@media (forced-colors: active) {
  .tb-33__tape {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
    rotate: 0deg;
  }
}
```
