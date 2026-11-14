---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-industrial-rocker-io-power-switch/"
title: "Tailwind Industrial Rocker I/O Power Switch"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The power switch off the back of real hardware: a rectangular rocker with engraved I and O halves seesawing inside a riveted steel panel, and a red pilot…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Industrial Rocker I/O Power Switch
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-industrial-rocker-io-power-switch/

The power switch off the back of real hardware: a rectangular rocker with engraved I and O halves seesawing inside a riveted steel panel, and a red pilot lamp that ignites on power. Perspective, gradients and text-shadow do all the machining.
## HTML
```html
<section class="ttg-26 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg26-bg font-ttg26-sans" aria-label="Industrial rocker power switch">
  <div class="relative flex flex-col items-center gap-3 px-11 pt-9 pb-5 rounded-[10px] [background:repeating-linear-gradient(92deg,var(--color-ttg26-steelhi)_0_2px,var(--color-ttg26-steello)_2px_4px)] shadow-[0_22px_46px_-20px_oklch(0_0_0/0.9),inset_0_1px_0_oklch(1_0_0/0.18),inset_0_-2px_4px_oklch(0_0_0/0.4)] has-checked:[&_.ttg26-lamp]:bg-ttg26-lamp has-checked:[&_.ttg26-lamp]:shadow-[0_0_8px_var(--color-ttg26-lamp),0_0_20px_color-mix(in_oklab,var(--color-ttg26-lamp)_50%,transparent)]">
      <span aria-hidden="true" class="absolute top-2 left-2 w-[9px] h-[9px] rounded-full bg-radial-[at_35%_30%] from-ttg26-rivethi to-ttg26-rivetlo shadow-[inset_0_-1px_2px_oklch(0_0_0/0.6)]"></span>
      <span aria-hidden="true" class="absolute top-2 right-2 w-[9px] h-[9px] rounded-full bg-radial-[at_35%_30%] from-ttg26-rivethi to-ttg26-rivetlo shadow-[inset_0_-1px_2px_oklch(0_0_0/0.6)]"></span>
      <span aria-hidden="true" class="absolute bottom-2 left-2 w-[9px] h-[9px] rounded-full bg-radial-[at_35%_30%] from-ttg26-rivethi to-ttg26-rivetlo shadow-[inset_0_-1px_2px_oklch(0_0_0/0.6)]"></span>
      <span aria-hidden="true" class="absolute bottom-2 right-2 w-[9px] h-[9px] rounded-full bg-radial-[at_35%_30%] from-ttg26-rivethi to-ttg26-rivetlo shadow-[inset_0_-1px_2px_oklch(0_0_0/0.6)]"></span>
      <span aria-hidden="true" class="ttg26-lamp absolute top-3.5 right-5.5 w-3 h-3 rounded-full bg-ttg26-lampdark shadow-[inset_0_1px_3px_oklch(0_0_0/0.8)] transition-[background-color,box-shadow] duration-200"></span>
      <span class="relative block w-15 h-28 p-[5px] rounded-[7px] bg-ttg26-well shadow-[inset_0_3px_8px_oklch(0_0_0/0.85),inset_0_0_0_2px_var(--color-ttg26-wellring)] perspective-[280px]">
        <input type="checkbox" id="ttg-26-sw" role="switch" aria-label="Main power" class="peer sr-only">
        <label for="ttg-26-sw" aria-hidden="true" class="grid grid-rows-2 w-full h-full rounded-[5px] cursor-pointer bg-linear-to-b from-ttg26-rockerlo via-ttg26-rockerhi via-50% to-ttg26-rockerdk origin-center rotate-x-[-16deg] transition-transform duration-[160ms] ease-[cubic-bezier(0.5,1.5,0.6,1)] peer-checked:rotate-x-[16deg] peer-checked:bg-linear-to-t peer-checked:[&_.ttg26-i]:text-ttg26-lit peer-checked:[&_.ttg26-o]:text-ttg26-dim peer-focus-visible:outline-3 peer-focus-visible:outline-ttg26-focus peer-focus-visible:outline-offset-[5px] motion-reduce:transition-none">
          <i class="ttg26-i grid place-items-center not-italic text-[17px] font-extrabold text-ttg26-dim [text-shadow:0_-1px_1px_oklch(0_0_0/0.8),0_1px_1px_oklch(1_0_0/0.15)]">I</i>
          <i class="ttg26-o grid place-items-center not-italic text-[17px] font-extrabold text-ttg26-lit [text-shadow:0_-1px_1px_oklch(0_0_0/0.8),0_1px_1px_oklch(1_0_0/0.15)]">O</i>
        </label>
      </span>
      <span class="px-2.5 py-[3px] rounded-[3px] bg-ttg26-tag text-ttg26-tagink text-[10px] font-bold tracking-[0.24em] shadow-[inset_0_1px_0_oklch(1_0_0/0.6)]">MAIN PWR</span>
  </div>
  <p class="text-[11px] tracking-[0.16em] uppercase text-ttg26-mute">IEC rocker &middot; I = on, O = off</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg26-bg: #1d1f24;
  --color-ttg26-bg: oklch(0.24 0.006 265);
  --color-ttg26-steelhi: #5a5f68;
  --color-ttg26-steelhi: oklch(0.47 0.008 265);
  --color-ttg26-steello: #4f545d;
  --color-ttg26-steello: oklch(0.43 0.008 265);
  --color-ttg26-rivethi: #a2a8b3;
  --color-ttg26-rivethi: oklch(0.72 0.01 265);
  --color-ttg26-rivetlo: #4a4f58;
  --color-ttg26-rivetlo: oklch(0.42 0.009 265);
  --color-ttg26-well: #191b1f;
  --color-ttg26-well: oklch(0.21 0.006 265);
  --color-ttg26-wellring: #101114;
  --color-ttg26-wellring: oklch(0.16 0.005 265);
  --color-ttg26-rockerhi: #3c4049;
  --color-ttg26-rockerhi: oklch(0.36 0.008 265);
  --color-ttg26-rockerlo: #2c2f35;
  --color-ttg26-rockerlo: oklch(0.29 0.007 265);
  --color-ttg26-rockerdk: #22252a;
  --color-ttg26-rockerdk: oklch(0.25 0.006 265);
  --color-ttg26-dim: #8b919d;
  --color-ttg26-dim: oklch(0.65 0.012 265);
  --color-ttg26-lit: #dde2ea;
  --color-ttg26-lit: oklch(0.91 0.008 265);
  --color-ttg26-lamp: #ff4a3d;
  --color-ttg26-lamp: oklch(0.65 0.22 27);
  --color-ttg26-lampdark: #3d2426;
  --color-ttg26-lampdark: oklch(0.29 0.03 20);
  --color-ttg26-tag: #c2c7d0;
  --color-ttg26-tag: oklch(0.83 0.008 265);
  --color-ttg26-tagink: #1e2128;
  --color-ttg26-tagink: oklch(0.24 0.008 265);
  --color-ttg26-mute: #7c828c;
  --color-ttg26-mute: oklch(0.6 0.01 265);
  --color-ttg26-focus: #6cb6f0;
  --color-ttg26-focus: oklch(0.74 0.14 235);
  --font-ttg26-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-26 {
  width: 100%;
  min-height: 100svh;
}
```
