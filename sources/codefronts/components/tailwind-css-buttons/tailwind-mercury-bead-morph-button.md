---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-mercury-bead-morph-button/"
title: "Tailwind Mercury Bead Morph Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A bead of mercury detaches from the button, stretches, and is reabsorbed on hover — genuine metaball merging from an SVG goo filter applied to plain CSS shapes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mercury Bead Morph Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-mercury-bead-morph-button/

A bead of mercury detaches from the button, stretches, and is reabsorbed on hover — genuine metaball merging from an SVG goo filter applied to plain CSS shapes. The filter is markup, the geometry is utilities, and the label sits outside the filtered layer so it stays sharp.
## HTML
```html
<div class="tb-31 w-full min-h-svh grid place-items-center font-tb31-sans antialiased p-[clamp(1.5rem,6vw,4rem)]">
  <svg aria-hidden="true" focusable="false" width="0" height="0" class="absolute size-0 overflow-hidden">
    <filter id="tb-31-goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"></feGaussianBlur>
      <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="g"></feColorMatrix>
      <feBlend in="SourceGraphic" in2="g"></feBlend>
    </filter>
  </svg>
  <button type="button" class="group relative cursor-pointer border-0 bg-transparent w-64 h-32 p-0 text-base font-bold tracking-[-0.01em] text-tb31-ink [-webkit-tap-highlight-color:transparent] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tb31-hg focus-visible:rounded-2xl disabled:cursor-not-allowed disabled:grayscale disabled:brightness-80">
    <span aria-hidden="true" class="absolute inset-0 z-10 [filter:url(#tb-31-goo)]">
      <span class="tb-31__metal absolute left-9 top-10 w-[8.2rem] h-[3.2rem] rounded-full bg-[length:8.2rem_3.2rem] bg-no-repeat bg-left-top"></span>
      <span class="tb-31__metal absolute left-9 top-10 size-[3.2rem] rounded-full bg-[length:8.2rem_3.2rem] bg-no-repeat bg-left-top transition-[translate,scale] duration-[750ms] ease-tb31-out group-hover:translate-x-[8.4rem] group-hover:scale-[0.62] group-focus-visible:translate-x-[8.4rem] group-focus-visible:scale-[0.62] group-active:scale-50 motion-reduce:transition-none"></span>
    </span>
    <span class="absolute z-30 left-[3.9rem] top-1/2 -translate-y-1/2 transition-[translate,color] duration-500 ease-tb31-out group-hover:translate-x-[0.4rem] motion-reduce:transition-none">Liquify</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb31-bg: #0c0e12;
  --color-tb31-bg: oklch(0.15 0.012 260);
  --color-tb31-hg: #c9d2dc;
  --color-tb31-hg: oklch(0.84 0.015 250);
  --color-tb31-hg-lo: #5c6672;
  --color-tb31-hg-lo: oklch(0.48 0.02 250);
  --color-tb31-ink: #0b0d11;
  --color-tb31-ink: oklch(0.14 0.01 260);
  --font-tb31-sans: "Space Grotesk", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --ease-tb31-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-31 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(36rem 22rem at 50% 45%, #1b2029, transparent 72%), var(--color-tb31-bg);
}
/* Both shapes paint the SAME gradient at the SAME size, so at rest the bead is
   pixel-identical to the pill's left cap and disappears into it completely.
   The goo threshold merges silhouettes, not tones. */

.tb-31__metal {
  background-image: radial-gradient(120% 120% at 30% 20%, #ffffff, transparent 55%), linear-gradient(160deg, var(--color-tb31-hg), var(--color-tb31-hg-lo));
}

@media (prefers-color-scheme: light) {
  .tb-31:not([data-theme="dark"]) {
    --color-tb31-bg: oklch(0.92 0.006 260);
  }
}

.tb-31[data-theme="light"] {
  --color-tb31-bg: oklch(0.92 0.006 260);
}

@media (forced-colors: active) {
  .tb-31 button > span:first-of-type {
    display: none;
  }

  .tb-31 button {
    border: 1px solid ButtonText;
    background: ButtonFace;
    width: auto;
    height: auto;
    padding: 1rem 2rem;
  }

  .tb-31 button > span:last-child {
    position: static;
    translate: none;
    color: ButtonText;
  }
}
```
