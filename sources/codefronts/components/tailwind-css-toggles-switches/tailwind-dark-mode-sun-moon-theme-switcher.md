---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-dark-mode-sun-moon-theme-switcher/"
title: "Tailwind Dark Mode Sun / Moon Theme Switcher"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The day/night switch, ported whole: the thumb is a glowing sun that morphs into a crescent via a single inset box-shadow transition, stars fade in, a cloud…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Sun / Moon Theme Switcher
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-dark-mode-sun-moon-theme-switcher/

The day/night switch, ported whole: the thumb is a glowing sun that morphs into a crescent via a single inset box-shadow transition, stars fade in, a cloud drifts out &mdash; and the surrounding panel re-themes itself through has-checked:, the utility form of :has(:checked).
## HTML
```html
<section class="ttg-02 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg02-daybg text-ttg02-dayink font-ttg02-sans transition-colors duration-500 has-checked:bg-ttg02-nightbg has-checked:text-ttg02-nightink" aria-label="Dark mode sun and moon theme switcher">
  <label for="ttg-02-sw" class="flex items-center gap-7 min-h-14 px-6 py-4 rounded-2xl cursor-pointer transition-colors duration-500 bg-white/60 has-checked:bg-white/5 shadow-[0_1px_2px_oklch(0.4_0.05_250/0.08)]">
    <span class="flex flex-col gap-0.5">
      <span class="text-[15.5px] font-semibold">Appearance</span>
      <span class="text-[12.5px] opacity-60">Follows this switch, not the system</span>
    </span>
    <span class="relative inline-block shrink-0">
      <input type="checkbox" id="ttg-02-sw" role="switch" class="peer appearance-none block w-[74px] h-9 rounded-full cursor-pointer relative bg-ttg02-day bg-linear-to-b from-ttg02-day to-ttg02-dayhi transition-[background-color,background-image] duration-[450ms] shadow-[inset_0_2px_5px_oklch(0.35_0.09_250/0.3)] checked:from-ttg02-night checked:to-ttg02-nighthi before:content-[''] before:absolute before:top-1 before:left-1 before:w-7 before:h-7 before:rounded-full before:z-10 before:shadow-[inset_0_0_0_14px_#ffd54f,0_0_12px_oklch(0.85_0.17_85/0.75)] before:transition-[transform,box-shadow] before:duration-[450ms] before:ease-[cubic-bezier(0.3,1.2,0.4,1)] checked:before:translate-x-[38px] checked:before:shadow-[inset_-8px_-4px_0_1px_#f4f1de,0_0_10px_oklch(0.9_0.03_270/0.45)] focus-visible:outline-3 focus-visible:outline-ttg02-focus focus-visible:outline-offset-3 motion-reduce:transition-none motion-reduce:before:transition-none">
      <span aria-hidden="true" class="pointer-events-none absolute top-[9px] left-3 w-0.5 h-0.5 rounded-full bg-white opacity-0 transition-opacity duration-[450ms] shadow-[10px_4px_0_#fff,4px_14px_0_0_#dfe8ff,16px_16px_0_#fff,26px_7px_0_0_#dfe8ff] peer-checked:opacity-95 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute top-[19px] right-3 w-[18px] h-[7px] rounded-lg bg-white opacity-95 transition-[opacity,transform] duration-[450ms] shadow-[-7px_-4px_0_-1px_#fff,6px_-3px_0_-2px_#fff] peer-checked:opacity-0 peer-checked:translate-x-2 motion-reduce:transition-none"></span>
    </span>
  </label>
  <p class="font-ttg02-mono text-[11px] tracking-[0.14em] uppercase opacity-55">Sun &harr; moon &middot; pure Tailwind morph</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg02-day: #7ecbf5;
  --color-ttg02-day: oklch(0.8 0.1 235);
  --color-ttg02-dayhi: #b3e0f9;
  --color-ttg02-dayhi: oklch(0.88 0.06 235);
  --color-ttg02-night: #1c2a4a;
  --color-ttg02-night: oklch(0.3 0.06 265);
  --color-ttg02-nighthi: #0f1830;
  --color-ttg02-nighthi: oklch(0.22 0.05 265);
  --color-ttg02-daybg: #e7f2fb;
  --color-ttg02-daybg: oklch(0.95 0.02 235);
  --color-ttg02-dayink: #1f2936;
  --color-ttg02-dayink: oklch(0.29 0.02 250);
  --color-ttg02-nightbg: #0b1220;
  --color-ttg02-nightbg: oklch(0.18 0.03 265);
  --color-ttg02-nightink: #d5dcec;
  --color-ttg02-nightink: oklch(0.88 0.02 265);
  --color-ttg02-focus: #4d9fff;
  --color-ttg02-focus: oklch(0.7 0.16 250);
  --font-ttg02-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg02-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.ttg-02 {
  width: 100%;
  min-height: 100svh;
}

.ttg-02 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
