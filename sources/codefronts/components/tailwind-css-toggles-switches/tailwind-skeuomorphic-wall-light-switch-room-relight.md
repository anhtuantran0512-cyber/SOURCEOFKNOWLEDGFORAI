---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-skeuomorphic-wall-light-switch-room-relight/"
title: "Tailwind Skeuomorphic Wall Light Switch with Room Relight"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A wall-plate rocker with a bevelled plate, slotted screws and a paddle that tips in real perspective &mdash; and when you flip it the whole room warms from…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Skeuomorphic Wall Light Switch with Room Relight
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-skeuomorphic-wall-light-switch-room-relight/

A wall-plate rocker with a bevelled plate, slotted screws and a paddle that tips in real perspective &mdash; and when you flip it the whole room warms from dusk to lamp-light, because the section watches the switch with has-checked:.
## HTML
```html
<section class="ttg-15 relative overflow-hidden w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg15-dusk font-ttg15-sans transition-colors duration-[800ms] has-checked:bg-ttg15-lamp has-checked:[&_.ttg15-glow]:opacity-100 motion-reduce:transition-none" aria-label="Skeuomorphic wall light switch">
  <span aria-hidden="true" class="ttg15-glow pointer-events-none absolute top-[8%] left-1/2 -translate-x-1/2 w-[420px] h-[420px] rounded-full opacity-0 transition-opacity duration-[800ms] bg-radial from-ttg15-halo to-transparent to-65% motion-reduce:transition-none"></span>
  <div class="relative z-10 flex flex-col items-center gap-4 w-32 py-6 rounded-xl bg-linear-170 from-ttg15-platehi to-ttg15-platelo shadow-[inset_0_2px_0_oklch(1_0_0/0.9),inset_0_-3px_5px_oklch(0.4_0.03_80/0.35),0_18px_34px_-14px_oklch(0_0_0/0.55)]">
    <span aria-hidden="true" class="relative w-[11px] h-[11px] rounded-full bg-radial-[at_35%_30%] from-ttg15-screwhi to-ttg15-screwlo shadow-[inset_0_-1px_2px_oklch(0.35_0.03_80/0.5)] before:content-[''] before:absolute before:top-[4.5px] before:left-[1.5px] before:right-[1.5px] before:h-[1.5px] before:rounded-[1px] before:bg-ttg15-slot before:-rotate-[38deg]"></span>
    <span class="relative block w-[58px] h-26 p-[5px] rounded-lg bg-ttg15-well shadow-[inset_0_3px_7px_oklch(0.4_0.03_80/0.55)] perspective-[300px]">
      <input type="checkbox" id="ttg-15-sw" role="switch" aria-label="Room light" class="peer sr-only">
      <label for="ttg-15-sw" aria-hidden="true" class="block w-full h-full rounded-md cursor-pointer bg-linear-to-b from-ttg15-paddlelo via-ttg15-paddlehi via-55% to-ttg15-paddlemid shadow-[0_4px_8px_oklch(0.4_0.03_80/0.4),inset_0_1px_0_oklch(1_0_0/0.8)] origin-center rotate-x-[14deg] transition-transform duration-[220ms] ease-[cubic-bezier(0.5,1.4,0.6,1)] peer-checked:-rotate-x-[14deg] peer-checked:bg-linear-to-t peer-focus-visible:outline-3 peer-focus-visible:outline-ttg15-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-none"></label>
    </span>
    <span aria-hidden="true" class="relative w-[11px] h-[11px] rounded-full bg-radial-[at_35%_30%] from-ttg15-screwhi to-ttg15-screwlo shadow-[inset_0_-1px_2px_oklch(0.35_0.03_80/0.5)] before:content-[''] before:absolute before:top-[4.5px] before:left-[1.5px] before:right-[1.5px] before:h-[1.5px] before:rounded-[1px] before:bg-ttg15-slot before:rotate-[24deg]"></span>
  </div>
  <p class="relative z-10 text-[12px] tracking-[0.12em] uppercase text-ttg15-duskink transition-colors duration-[800ms] [.ttg-15:has(:checked)_&]:text-ttg15-lampink motion-reduce:transition-none">Flip it &mdash; the room lights up</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg15-dusk: #262a35;
  --color-ttg15-dusk: oklch(0.28 0.02 265);
  --color-ttg15-lamp: #f3e6c9;
  --color-ttg15-lamp: oklch(0.93 0.05 85);
  --color-ttg15-halo: #ffd682;
  --color-ttg15-halo: oklch(0.88 0.13 82 / 0.55);
  --color-ttg15-platehi: #f6f3ec;
  --color-ttg15-platehi: oklch(0.96 0.008 85);
  --color-ttg15-platelo: #d8d3c7;
  --color-ttg15-platelo: oklch(0.87 0.012 85);
  --color-ttg15-well: #c7c1b3;
  --color-ttg15-well: oklch(0.81 0.014 85);
  --color-ttg15-paddlehi: #f8f5ee;
  --color-ttg15-paddlehi: oklch(0.97 0.006 85);
  --color-ttg15-paddlemid: #efece3;
  --color-ttg15-paddlemid: oklch(0.94 0.008 85);
  --color-ttg15-paddlelo: #cdc7b9;
  --color-ttg15-paddlelo: oklch(0.83 0.013 85);
  --color-ttg15-screwhi: #e9e5db;
  --color-ttg15-screwhi: oklch(0.93 0.008 85);
  --color-ttg15-screwlo: #9e988a;
  --color-ttg15-screwlo: oklch(0.67 0.014 85);
  --color-ttg15-slot: #6c6659;
  --color-ttg15-slot: oklch(0.49 0.012 85);
  --color-ttg15-duskink: #a3a8b6;
  --color-ttg15-duskink: oklch(0.72 0.014 265);
  --color-ttg15-lampink: #7a6a45;
  --color-ttg15-lampink: oklch(0.52 0.05 85);
  --color-ttg15-focus: #5b8def;
  --color-ttg15-focus: oklch(0.65 0.16 258);
  --font-ttg15-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-15 {
  width: 100%;
  min-height: 100svh;
}
```
