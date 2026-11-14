---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-polaroid-snapshot-button/"
title: "Tailwind Polaroid Snapshot Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "An instant photo mid-development: the image starts dark, flat and green-shifted, then blooms to full colour as you hover — a pure filter transition, exactly…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Polaroid Snapshot Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-polaroid-snapshot-button/

An instant photo mid-development: the image starts dark, flat and green-shifted, then blooms to full colour as you hover — a pure filter transition, exactly how the chemistry behaves. The frame tilts, lifts off the table, and the caption is hand-written on the wide bottom border.
## HTML
```html
<div class="tb-40 w-full min-h-svh grid place-items-center font-tb40-hand p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="group cursor-pointer border-0 bg-transparent p-0 [-webkit-tap-highlight-color:transparent] focus-visible:outline-2 focus-visible:outline-offset-[6px] focus-visible:outline-tb40-accent disabled:cursor-not-allowed disabled:grayscale-[0.6]">
    <span class="grid gap-2 w-56 pt-3 px-3 pb-1.5 rounded-[0.15rem] bg-[linear-gradient(170deg,var(--color-tb40-card),var(--color-tb40-card-lo))] shadow-[0_14px_24px_-14px_#000000b3,inset_0_0_0_1px_#0000000f] -rotate-[2.2deg] transition-[rotate,translate,box-shadow] duration-[450ms] ease-tb40-out group-hover:-rotate-[0.5deg] group-hover:-translate-y-1 group-hover:shadow-[0_22px_34px_-14px_#000000bf] group-focus-visible:-rotate-[0.5deg] group-focus-visible:-translate-y-1 group-active:-rotate-[1.6deg] group-active:translate-y-px motion-reduce:transition-none motion-reduce:group-hover:rotate-[-2.2deg] motion-reduce:group-hover:translate-y-0">
      <span class="relative block aspect-square overflow-hidden bg-tb40-well">
        <img src="https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="800" height="800" loading="lazy" decoding="async" class="block size-full object-cover scale-[1.06] brightness-[0.34] contrast-[0.7] saturate-[0.32] hue-rotate-[28deg] blur-[1.2px] transition-[filter,scale] duration-[1600ms] ease-[cubic-bezier(0.3,0.7,0.3,1)] group-hover:scale-100 group-hover:brightness-100 group-hover:contrast-[1.04] group-hover:saturate-[1.06] group-hover:hue-rotate-0 group-hover:blur-none group-focus-visible:scale-100 group-focus-visible:brightness-100 group-focus-visible:contrast-[1.04] group-focus-visible:saturate-[1.06] group-focus-visible:hue-rotate-0 group-focus-visible:blur-none motion-reduce:transition-none motion-reduce:filter-none motion-reduce:scale-100">
        <span aria-hidden="true" class="absolute inset-0 pointer-events-none shadow-[inset_0_0_2.2rem_#00000073,inset_0_0_0.3rem_#ffffff26]"></span>
      </span>
      <span class="px-1 pt-0.5 pb-1.5 text-xl leading-tight text-center text-tb40-ink">shake it once — open album</span>
    </span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb40-bg: #2a2723;
  --color-tb40-bg: oklch(0.27 0.012 70);
  --color-tb40-card: #fbfaf5;
  --color-tb40-card: oklch(0.98 0.006 90);
  --color-tb40-card-lo: #e8e5dc;
  --color-tb40-card-lo: oklch(0.92 0.008 90);
  --color-tb40-ink: #2a2520;
  --color-tb40-ink: oklch(0.26 0.012 70);
  --color-tb40-well: #14161a;
  --color-tb40-well: oklch(0.18 0.012 265);
  --color-tb40-accent: #3b7ea1;
  --color-tb40-accent: oklch(0.58 0.09 235);
  --font-tb40-hand: "Caveat", ui-rounded, cursive;
  --ease-tb40-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-40 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 40%, rgba(255,255,255,.06), transparent 72%), repeating-linear-gradient(94deg, rgba(0,0,0,.04) 0 2px, transparent 2px 12px), var(--color-tb40-bg);
}

@media (prefers-color-scheme: light) {
  .tb-40:not([data-theme="dark"]) {
    --color-tb40-bg: oklch(0.34 0.012 70);
  }
}

.tb-40[data-theme="light"] {
  --color-tb40-bg: oklch(0.34 0.012 70);
}

@media (forced-colors: active) {
  .tb-40 button > span {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
    rotate: 0deg;
  }

  .tb-40 button span:last-child {
    color: ButtonText;
  }

  .tb-40 button span[aria-hidden] {
    display: none;
  }
}
```
