---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-wine-velvet-ribbon-button/"
title: "Tailwind Wine Velvet Ribbon Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "Crushed burgundy velvet cut as an awards ribbon: notched swallow-tail ends, a nap sheen that reverses direction as the pointer crosses — the way velvet…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Wine Velvet Ribbon Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-wine-velvet-ribbon-button/

Crushed burgundy velvet cut as an awards ribbon: notched swallow-tail ends, a nap sheen that reverses direction as the pointer crosses — the way velvet changes tone when you brush it — and gold-foil lettering with a proper bevel.
## HTML
```html
<div class="tb-35 w-full min-h-svh grid place-items-center font-tb35-serif p-[clamp(1.5rem,6vw,4rem)]">
  <span class="group inline-block drop-shadow-[0_16px_24px_#000000a6] transition-[translate,filter] duration-[350ms] ease-tb35-out has-hover:-translate-y-0.5 has-hover:drop-shadow-[0_22px_30px_#000000b3] has-focus-visible:outline-2 has-focus-visible:outline-offset-[6px] has-focus-visible:outline-tb35-foil motion-reduce:transition-none">
    <button type="button" class="tb-35__velvet relative overflow-hidden cursor-pointer grid place-items-center min-h-22 px-11 pb-[2.1rem] border-0 text-[1.0625rem] font-semibold uppercase tracking-[0.1em] text-tb35-foil transition-[scale] duration-200 ease-tb35-out focus-visible:outline-none active:scale-[0.99] disabled:cursor-not-allowed disabled:grayscale-[0.6] disabled:brightness-80 motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 z-20 pointer-events-none opacity-100 bg-[linear-gradient(78deg,rgba(255,255,255,0.16),transparent_55%)] transition-opacity duration-500 group-hover:opacity-0 group-focus-within:opacity-0 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-0 z-20 pointer-events-none opacity-0 bg-[linear-gradient(-78deg,rgba(255,255,255,0.2),transparent_58%)] transition-opacity duration-500 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none"></span>
      <span class="tb-35__foil relative z-30 pb-1.5 bg-[linear-gradient(180deg,#fbeec2,#dfb96a_52%,#a67c30)] bg-clip-text drop-shadow-[0_1px_0_#0000008c]">Reserve the cellar</span>
    </button>
  </span>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb35-bg: #160b10;
  --color-tb35-bg: oklch(0.15 0.04 12);
  --color-tb35-wine: #5c1026;
  --color-tb35-wine: oklch(0.33 0.14 12);
  --color-tb35-wine-hi: #8a1c3a;
  --color-tb35-wine-hi: oklch(0.42 0.17 10);
  --color-tb35-wine-lo: #320611;
  --color-tb35-wine-lo: oklch(0.22 0.11 12);
  --color-tb35-foil: #e8c67a;
  --color-tb35-foil: oklch(0.84 0.1 84);
  --font-tb35-serif: "Playfair Display", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb35-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-35 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(34rem 22rem at 50% 42%, color-mix(in oklab, var(--color-tb35-wine) 32%, transparent), transparent 74%), var(--color-tb35-bg);
}
/* THE RIBBON. Band across the top, a tail at each end, a V notch cut up into each
   tail. One continuous outline — trace the points in order before changing them:
   a self-intersecting path fills as stray wedges under nonzero. */

.tb-35__velvet {
  clip-path: polygon(
      0 0, 100% 0,
      100% 100%, 91% 74%, 82% 100%,
      82% 58%, 18% 58%,
      18% 100%, 9% 74%, 0 100%);
  background-color: var(--color-tb35-wine);
  background-image: radial-gradient(.045rem .045rem at 30% 40%, rgba(255,255,255,.1) 99%, transparent), radial-gradient(.04rem .04rem at 72% 66%, rgba(0,0,0,.2) 99%, transparent), linear-gradient(165deg, var(--color-tb35-wine-hi), var(--color-tb35-wine) 50%, var(--color-tb35-wine-lo));
  background-size: 9px 9px, 13px 13px, 100% 100%;
}
/* bg-clip-text needs the fill transparent; the solid token above it is the fallback. */

.tb-35__foil {
  -webkit-text-fill-color: transparent;
}

@media (prefers-color-scheme: light) {
  .tb-35:not([data-theme="dark"]) {
    --color-tb35-bg: oklch(0.22 0.06 12);
  }
}

.tb-35[data-theme="light"] {
  --color-tb35-bg: oklch(0.22 0.06 12);
}

@media (forced-colors: active) {
  .tb-35__velvet {
    clip-path: none;
    background: ButtonFace;
    border: 1px solid ButtonText;
  }

  .tb-35__foil {
    background: none;
    -webkit-text-fill-color: ButtonText;
    color: ButtonText;
    filter: none;
  }

  .tb-35__velvet span[aria-hidden] {
    display: none;
  }
}
```
