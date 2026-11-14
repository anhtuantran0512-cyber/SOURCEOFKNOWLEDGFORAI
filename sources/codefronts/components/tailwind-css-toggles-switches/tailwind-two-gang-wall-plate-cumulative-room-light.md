---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-two-gang-wall-plate-cumulative-room-light/"
title: "Tailwind Two-Gang Wall Plate with Cumulative Room Light"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Two switches on one plate, and the room responds to BOTH: one on is a dim pool of light, two on floods the scene."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two-Gang Wall Plate with Cumulative Room Light
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-two-gang-wall-plate-cumulative-room-light/

Two switches on one plate, and the room responds to BOTH: one on is a dim pool of light, two on floods the scene. Counting children in pure CSS is the trick &mdash; :has() can test combinations even though it cannot count.
## HTML
```html
<section class="ttg-36 relative overflow-hidden w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg36-dark font-ttg36-sans transition-colors duration-700 has-[#ttg-36-a:checked]:bg-ttg36-dim has-[#ttg-36-b:checked]:bg-ttg36-dim has-[#ttg-36-a:checked]:has-[#ttg-36-b:checked]:bg-ttg36-bright has-[#ttg-36-a:checked]:[&_.ttg36-pool]:opacity-100 has-[#ttg-36-b:checked]:[&_.ttg36-pool]:opacity-100 has-[#ttg-36-a:checked]:has-[#ttg-36-b:checked]:[&_.ttg36-wash]:opacity-100 motion-reduce:transition-none" aria-label="Two gang wall plate">
  <span aria-hidden="true" class="ttg36-pool pointer-events-none absolute top-[10%] left-1/2 -translate-x-1/2 w-80 h-80 rounded-full opacity-0 transition-opacity duration-700 bg-radial from-ttg36-glow to-transparent to-70% motion-reduce:transition-none"></span>
  <span aria-hidden="true" class="ttg36-wash pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-700 bg-radial from-ttg36-wash to-transparent to-75% motion-reduce:transition-none"></span>
  <div class="relative z-10 flex gap-5 px-7 py-8 rounded-2xl bg-linear-170 from-ttg36-platehi to-ttg36-platelo shadow-[inset_0_2px_0_oklch(1_0_0/0.85),inset_0_-3px_5px_oklch(0.4_0.03_80/0.3),0_20px_38px_-16px_oklch(0_0_0/0.6)]">
    <span class="flex flex-col items-center gap-3">
      <span class="relative block w-14 h-24 p-1 rounded-lg bg-ttg36-well shadow-[inset_0_3px_7px_oklch(0.4_0.03_80/0.5)] perspective-[320px]">
        <input type="checkbox" id="ttg-36-a" role="switch" aria-label="Ceiling light" class="peer sr-only">
        <label for="ttg-36-a" aria-hidden="true" class="block w-full h-full rounded-md cursor-pointer bg-linear-to-b from-ttg36-paddlelo via-ttg36-paddlehi via-55% to-ttg36-paddlemid shadow-[0_4px_8px_oklch(0.4_0.03_80/0.35),inset_0_1px_0_oklch(1_0_0/0.8)] origin-center rotate-x-[15deg] transition-transform duration-200 ease-[cubic-bezier(0.5,1.4,0.6,1)] peer-checked:-rotate-x-[15deg] peer-checked:bg-linear-to-t peer-focus-visible:outline-3 peer-focus-visible:outline-ttg36-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-none"></label>
      </span>
      <span class="text-[10px] font-bold tracking-[0.2em] text-ttg36-tag">CEILING</span>
    </span>
    <span class="flex flex-col items-center gap-3">
      <span class="relative block w-14 h-24 p-1 rounded-lg bg-ttg36-well shadow-[inset_0_3px_7px_oklch(0.4_0.03_80/0.5)] perspective-[320px]">
        <input type="checkbox" id="ttg-36-b" role="switch" aria-label="Lamps" class="peer sr-only">
        <label for="ttg-36-b" aria-hidden="true" class="block w-full h-full rounded-md cursor-pointer bg-linear-to-b from-ttg36-paddlelo via-ttg36-paddlehi via-55% to-ttg36-paddlemid shadow-[0_4px_8px_oklch(0.4_0.03_80/0.35),inset_0_1px_0_oklch(1_0_0/0.8)] origin-center rotate-x-[15deg] transition-transform duration-200 ease-[cubic-bezier(0.5,1.4,0.6,1)] peer-checked:-rotate-x-[15deg] peer-checked:bg-linear-to-t peer-focus-visible:outline-3 peer-focus-visible:outline-ttg36-focus peer-focus-visible:outline-offset-4 motion-reduce:transition-none"></label>
      </span>
      <span class="text-[10px] font-bold tracking-[0.2em] text-ttg36-tag">LAMPS</span>
    </span>
  </div>
  <p class="relative z-10 text-[12px] tracking-[0.12em] uppercase text-ttg36-caption transition-colors duration-700 [.ttg-36:has(:checked)_&]:text-ttg36-captionlit motion-reduce:transition-none">One on dims the room &middot; two floods it</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg36-dark: #1f232c;
  --color-ttg36-dark: oklch(0.25 0.015 265);
  --color-ttg36-dim: #4a4436;
  --color-ttg36-dim: oklch(0.44 0.03 85);
  --color-ttg36-bright: #efe1c2;
  --color-ttg36-bright: oklch(0.92 0.05 88);
  --color-ttg36-glow: #ffd07a;
  --color-ttg36-glow: oklch(0.87 0.13 80 / 0.45);
  --color-ttg36-wash: #ffe6b5;
  --color-ttg36-wash: oklch(0.92 0.08 85 / 0.4);
  --color-ttg36-platehi: #f5f2eb;
  --color-ttg36-platehi: oklch(0.96 0.008 85);
  --color-ttg36-platelo: #d9d4c8;
  --color-ttg36-platelo: oklch(0.87 0.012 85);
  --color-ttg36-well: #c7c1b3;
  --color-ttg36-well: oklch(0.81 0.014 85);
  --color-ttg36-paddlehi: #f8f5ee;
  --color-ttg36-paddlehi: oklch(0.97 0.006 85);
  --color-ttg36-paddlemid: #efece3;
  --color-ttg36-paddlemid: oklch(0.94 0.008 85);
  --color-ttg36-paddlelo: #cdc7b9;
  --color-ttg36-paddlelo: oklch(0.83 0.013 85);
  --color-ttg36-tag: #6e6858;
  --color-ttg36-tag: oklch(0.5 0.015 85);
  --color-ttg36-caption: #9ba1ae;
  --color-ttg36-caption: oklch(0.7 0.014 265);
  --color-ttg36-captionlit: #6b5f43;
  --color-ttg36-captionlit: oklch(0.48 0.045 85);
  --color-ttg36-focus: #5b8def;
  --color-ttg36-focus: oklch(0.65 0.16 258);
  --font-ttg36-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-36 {
  width: 100%;
  min-height: 100svh;
}
```
