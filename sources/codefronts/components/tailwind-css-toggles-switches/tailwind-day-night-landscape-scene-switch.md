---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-day-night-landscape-scene-switch/"
title: "Tailwind Day / Night Landscape Scene Switch"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A wide cinematic switch that IS a landscape: the sun sets behind clip-path mountains as the moon climbs the mirrored path, stars fade in, the ridges darken,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Day / Night Landscape Scene Switch
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-day-night-landscape-scene-switch/

A wide cinematic switch that IS a landscape: the sun sets behind clip-path mountains as the moon climbs the mirrored path, stars fade in, the ridges darken, and the page follows the scene into night. The most shareable control in the collection.
## HTML
```html
<section class="ttg-18 w-full min-h-svh grid place-items-center px-5 py-14 bg-ttg18-daybg font-ttg18-sans transition-colors duration-700 has-checked:bg-ttg18-nightbg motion-reduce:transition-none" aria-label="Day night landscape scene switch">
  <label for="ttg-18-sw" class="flex flex-col items-center gap-4 cursor-pointer">
    <span class="relative block w-55 h-25 rounded-[50px] overflow-hidden shadow-[0_18px_40px_-18px_oklch(0.2_0.05_265/0.6),inset_0_0_0_1px_oklch(1_0_0/0.25)]">
      <input type="checkbox" id="ttg-18-sw" role="switch" aria-label="Night mode" class="peer appearance-none absolute inset-0 w-full h-full z-[1] cursor-pointer bg-linear-to-b from-ttg18-skyday via-ttg18-skydaymid via-70% to-ttg18-skydaylo transition-[background-color,filter] duration-700 checked:from-ttg18-skynight checked:via-ttg18-skynightmid checked:to-ttg18-skynightlo before:content-[''] before:absolute before:top-3.5 before:left-6.5 before:w-9.5 before:h-9.5 before:rounded-full before:bg-radial-[at_35%_30%] before:from-ttg18-sunhi before:to-ttg18-sunlo before:shadow-[0_0_22px_oklch(0.85_0.16_80/0.9)] before:transition-transform before:duration-700 before:ease-[cubic-bezier(0.5,0,0.6,1)] checked:before:translate-x-[60px] checked:before:translate-y-[95px] focus-visible:outline-3 focus-visible:outline-ttg18-focus focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none"></input>
      <span aria-hidden="true" class="pointer-events-none absolute top-3 left-7.5 z-[2] w-0.5 h-0.5 rounded-full bg-white opacity-0 transition-opacity duration-700 shadow-[24px_8px_0_#fff,58px_2px_0_0_#cfd8ff,96px_14px_0_#fff,130px_5px_0_0_#cfd8ff,74px_26px_0_#fff,150px_22px_0_0_#cfd8ff] peer-checked:opacity-95 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute top-3.5 right-7.5 z-[2] w-7.5 h-7.5 rounded-full bg-ttg18-moon shadow-[inset_-6px_-4px_0_oklch(0.62_0.01_90/0.35),0_0_14px_oklch(0.92_0.02_265/0.5)] -translate-x-10 translate-y-[95px] transition-transform duration-700 ease-[cubic-bezier(0.4,0,0.5,1)] peer-checked:translate-x-0 peer-checked:translate-y-0 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="ttg18-ridge pointer-events-none absolute bottom-0 inset-x-0 z-[3] h-11 bg-ttg18-ridgefar transition-[filter] duration-700 [clip-path:polygon(0_100%,0_55%,18%_20%,34%_62%,52%_10%,70%_58%,86%_30%,100%_65%,100%_100%)] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="ttg18-ridge pointer-events-none absolute bottom-0 inset-x-0 z-[3] h-8 bg-ttg18-ridgenear transition-[filter] duration-700 [clip-path:polygon(0_100%,0_70%,14%_35%,30%_75%,48%_25%,66%_70%,84%_40%,100%_72%,100%_100%)] motion-reduce:transition-none"></span>
    </span>
    <span class="text-[14px] font-semibold tracking-[0.06em] text-ttg18-dayink transition-colors duration-700 [.ttg-18:has(:checked)_&]:text-ttg18-nightink motion-reduce:transition-none">Night mode</span>
  </label>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg18-daybg: #dde9f3;
  --color-ttg18-daybg: oklch(0.92 0.02 240);
  --color-ttg18-nightbg: #0a1020;
  --color-ttg18-nightbg: oklch(0.17 0.03 265);
  --color-ttg18-skyday: #5fb0e6;
  --color-ttg18-skyday: oklch(0.73 0.12 235);
  --color-ttg18-skydaymid: #b8dff5;
  --color-ttg18-skydaymid: oklch(0.88 0.06 235);
  --color-ttg18-skydaylo: #ffd9a0;
  --color-ttg18-skydaylo: oklch(0.89 0.08 75);
  --color-ttg18-skynight: #0d1b3d;
  --color-ttg18-skynight: oklch(0.24 0.06 265);
  --color-ttg18-skynightmid: #22355e;
  --color-ttg18-skynightmid: oklch(0.34 0.05 265);
  --color-ttg18-skynightlo: #3a4a72;
  --color-ttg18-skynightlo: oklch(0.43 0.05 265);
  --color-ttg18-sunhi: #fff3c0;
  --color-ttg18-sunhi: oklch(0.96 0.07 95);
  --color-ttg18-sunlo: #ffcf4d;
  --color-ttg18-sunlo: oklch(0.86 0.15 85);
  --color-ttg18-moon: #f1eee2;
  --color-ttg18-moon: oklch(0.95 0.015 90);
  --color-ttg18-ridgefar: #5d7c66;
  --color-ttg18-ridgefar: oklch(0.55 0.05 155);
  --color-ttg18-ridgenear: #3f5a48;
  --color-ttg18-ridgenear: oklch(0.42 0.05 155);
  --color-ttg18-dayink: #2f4560;
  --color-ttg18-dayink: oklch(0.38 0.05 250);
  --color-ttg18-nightink: #b9c4de;
  --color-ttg18-nightink: oklch(0.82 0.03 265);
  --color-ttg18-focus: #6ea8ff;
  --color-ttg18-focus: oklch(0.73 0.15 255);
  --font-ttg18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-18 {
  width: 100%;
  min-height: 100svh;
}

.ttg-18 input[type="checkbox"] {
  -webkit-appearance: none;
}
/* Nightfall on both ridges. brightness-35 is a filter utility, but it has to apply to a
   class-matched pair from an ancestor's state, which is one step past readable as a variant. */

.ttg-18:has(input:checked) .ttg18-ridge {
  filter: brightness(0.35) saturate(0.6);
}
```
