---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-buttons/tailwind-victorian-cigar-band-foil-button/"
title: "Tailwind Victorian Cigar Band Foil Button"
section: "components"
category: "tailwind-css-buttons"
category_name: "Tailwind CSS Buttons"
description: "A cigar band in embossed gold foil: scalloped top and bottom edges, a guilloché lattice engraved into the field, a laurel medallion struck in the centre, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Victorian Cigar Band Foil Button
Source: https://codefronts.com/components/tailwind-css-buttons/tailwind-victorian-cigar-band-foil-button/

A cigar band in embossed gold foil: scalloped top and bottom edges, a guilloché lattice engraved into the field, a laurel medallion struck in the centre, and small-caps lettering raised with a two-tone bevel. Hover tilts the foil so the light runs the other way.
## HTML
```html
<div class="tb-46 w-full min-h-svh grid place-items-center font-tb46-serif p-[clamp(1.5rem,6vw,4rem)]">
  <button type="button" class="tb-46__band relative overflow-hidden cursor-pointer grid grid-flow-col items-center gap-3.5 min-h-18 px-10 py-4 border-0 rounded-[0.2rem] text-[1.0625rem] font-bold tracking-[0.14em] uppercase text-tb46-ink bg-[linear-gradient(104deg,#7d5a1e,#f6e3ae_22%,#c99f4f_42%,#8d6a2c_58%,#f2dda6_78%,#8a6528)] bg-[length:180%_100%] bg-[position:0%_0%] [text-shadow:0_1px_0_#fff7dcb8,0_-1px_0_#3c2a0c80] drop-shadow-[0_10px_16px_#00000099] transition-[background-position,translate,filter] duration-700 ease-tb46-out [-webkit-tap-highlight-color:transparent] hover:bg-[position:100%_0%] hover:-translate-y-0.5 hover:drop-shadow-[0_16px_22px_#000000a6] focus-visible:bg-[position:100%_0%] focus-visible:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-[5px] focus-visible:outline-tb46-foil-hi active:translate-y-px active:drop-shadow-[0_4px_8px_#00000099] disabled:cursor-not-allowed disabled:grayscale-[0.7] disabled:opacity-75 motion-reduce:transition-none">
    <span aria-hidden="true" class="tb-46__lattice absolute inset-0 pointer-events-none opacity-50"></span>
    <span aria-hidden="true" class="tb-46__medal relative z-20 grid place-items-center size-8.5 rounded-full text-tb46-ink shadow-[inset_0_1px_0_#fff7dcb3,inset_0_-1px_2px_#3c2a0c80,0_1px_2px_#00000066]">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" class="size-5"><path d="M12 4c-2.4 2.6-3.4 5.6-3 8.6.3 2.4 1.5 4.4 3 6.4 1.5-2 2.7-4 3-6.4.4-3-.6-6-3-8.6z"/><path d="M8.4 9.6c-1.6.3-2.8 1.2-3.6 2.6M15.6 9.6c1.6.3 2.8 1.2 3.6 2.6"/></svg>
    </span>
    <span class="relative z-20">Havana Reserve</span>
  </button>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tb46-bg: #1a120c;
  --color-tb46-bg: oklch(0.17 0.03 52);
  --color-tb46-ink: #3c2a0c;
  --color-tb46-ink: oklch(0.28 0.06 78);
  --color-tb46-foil-hi: #f6e3ae;
  --color-tb46-foil-hi: oklch(0.91 0.07 88);
  --font-tb46-serif: "Cinzel", ui-serif, Georgia, "Times New Roman", serif;
  --ease-tb46-out: cubic-bezier(0.16, 1, 0.3, 1);
}

.tb-46 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: radial-gradient(32rem 20rem at 50% 42%, rgba(215,170,90,.16), transparent 72%), var(--color-tb46-bg);
}
/* SCALLOPED EDGES: the perforation technique inverted — the mask KEEPS the
   circles and unions them with a shorter base. No composite needed. */

.tb-46__band {
  -webkit-mask: radial-gradient(.42rem .42rem at 50% 100%, #000 96%, transparent 0) 0 0/.84rem .42rem repeat-x, radial-gradient(.42rem .42rem at 50% 0, #000 96%, transparent 0) 0 100%/.84rem .42rem repeat-x, linear-gradient(#000, #000) 0 .4rem/100% calc(100% - .8rem) no-repeat;
  mask: radial-gradient(.42rem .42rem at 50% 100%, #000 96%, transparent 0) 0 0/.84rem .42rem repeat-x, radial-gradient(.42rem .42rem at 50% 0, #000 96%, transparent 0) 0 100%/.84rem .42rem repeat-x, linear-gradient(#000, #000) 0 .4rem/100% calc(100% - .8rem) no-repeat;
}
/* GUILLOCHÉ: two crossing repeating gradients at ±30°, very low alpha so it
   engraves rather than stripes. */

.tb-46__lattice {
  background: repeating-linear-gradient(30deg, rgba(60,42,12,.16) 0 1px, transparent 1px 7px), repeating-linear-gradient(-30deg, rgba(60,42,12,.14) 0 1px, transparent 1px 7px);
}

.tb-46__medal {
  background: radial-gradient(circle at 36% 30%, #fbeec2, #c99f4f 62%, #8a6528);
}

@media (prefers-color-scheme: light) {
  .tb-46:not([data-theme="dark"]) {
    --color-tb46-bg: oklch(0.22 0.035 52);
  }
}

.tb-46[data-theme="light"] {
  --color-tb46-bg: oklch(0.22 0.035 52);
}

@media (forced-colors: active) {
  .tb-46__band {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    text-shadow: none;
    filter: none;
  }

  .tb-46__lattice {
    display: none;
  }

  .tb-46__medal {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```
