---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-rotary-knob-toggle-brushed-metal-conic-gradient/"
title: "Tailwind Rotary Knob Toggle with Brushed-Metal Conic Gradient"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A machined aluminium knob that twists between OFF and ON detents: brushed-metal conic sheen, a milled indicator, bezel tick marks and a pilot LED that…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rotary Knob Toggle with Brushed-Metal Conic Gradient
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-rotary-knob-toggle-brushed-metal-conic-gradient/

A machined aluminium knob that twists between OFF and ON detents: brushed-metal conic sheen, a milled indicator, bezel tick marks and a pilot LED that ignites at the ON position. The checkbox IS the knob &mdash; click or press Space to twist it.
## HTML
```html
<section class="ttg-22 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg22-bg font-ttg22-sans" aria-label="Rotary knob toggle">
  <div class="relative flex items-end gap-3.5 px-6 pt-7 pb-5 rounded-[18px] bg-linear-170 from-ttg22-facehi to-ttg22-facelo shadow-[0_20px_44px_-22px_oklch(0_0_0/0.9),inset_0_1px_0_oklch(1_0_0/0.07)] has-checked:[&_.ttg22-led]:bg-ttg22-led has-checked:[&_.ttg22-led]:shadow-[0_0_7px_var(--color-ttg22-led),0_0_16px_color-mix(in_oklab,var(--color-ttg22-led)_55%,transparent)]">
    <span aria-hidden="true" class="pb-8.5 text-[11px] font-bold tracking-[0.18em] text-ttg22-legend">OFF</span>
    <span class="relative grid place-items-center w-26 h-26 rounded-full [background:radial-gradient(circle,var(--color-ttg22-wellhi)_58%,var(--color-ttg22-wellmid)_60%,var(--color-ttg22-welllo)_100%)] shadow-[inset_0_2px_6px_oklch(0_0_0/0.7)] before:content-[''] before:absolute before:bottom-1.5 before:left-3.5 before:w-0.5 before:h-[7px] before:rounded-[1px] before:bg-ttg22-tick before:rotate-[38deg] after:content-[''] after:absolute after:bottom-1.5 after:right-3.5 after:w-0.5 after:h-[7px] after:rounded-[1px] after:bg-ttg22-tick after:-rotate-[38deg]">
      <input type="checkbox" id="ttg-22-sw" role="switch" aria-label="Amplifier power" class="appearance-none w-22 h-22 rounded-full relative cursor-pointer [background:radial-gradient(circle_at_32%_26%,oklch(1_0_0/0.35),transparent_46%),conic-gradient(var(--color-ttg22-mhi)_0_8%,var(--color-ttg22-mlo)_8%_16%,var(--color-ttg22-mmid)_16%_24%,var(--color-ttg22-mlo)_24%_32%,var(--color-ttg22-mhi)_32%_40%,var(--color-ttg22-mlo)_40%_48%,var(--color-ttg22-mmid)_48%_56%,var(--color-ttg22-mlo)_56%_64%,var(--color-ttg22-mhi)_64%_72%,var(--color-ttg22-mlo)_72%_80%,var(--color-ttg22-mmid)_80%_88%,var(--color-ttg22-mlo)_88%_96%,var(--color-ttg22-mhi)_96%_100%)] shadow-[0_6px_14px_oklch(0_0_0/0.6),inset_0_-3px_6px_oklch(0_0_0/0.35),inset_0_2px_3px_oklch(1_0_0/0.5)] rotate-[-32deg] transition-transform duration-[350ms] ease-[cubic-bezier(0.3,1.4,0.4,1)] checked:rotate-[32deg] active:scale-[0.97] checked:active:scale-[0.97] before:content-[''] before:absolute before:top-[7px] before:left-1/2 before:-ml-[2.5px] before:w-[5px] before:h-[22px] before:rounded-[3px] before:bg-ttg22-indicator before:shadow-[inset_0_1px_2px_oklch(0_0_0/0.8),0_1px_0_oklch(1_0_0/0.3)] focus-visible:outline-3 focus-visible:outline-ttg22-focus focus-visible:outline-offset-[5px] motion-reduce:duration-100">
    </span>
    <span aria-hidden="true" class="pb-8.5 text-[11px] font-bold tracking-[0.18em] text-ttg22-legend">ON</span>
    <span aria-hidden="true" class="ttg22-led absolute top-3.5 right-4 w-[9px] h-[9px] rounded-full bg-ttg22-leddark shadow-[inset_0_1px_2px_oklch(0_0_0/0.7)] transition-[background-color,box-shadow] duration-250"></span>
  </div>
  <p class="text-[11px] tracking-[0.16em] uppercase text-ttg22-mute">Machined detent &middot; click to twist</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg22-bg: #24262a;
  --color-ttg22-bg: oklch(0.27 0.005 265);
  --color-ttg22-facehi: #34373d;
  --color-ttg22-facehi: oklch(0.34 0.007 265);
  --color-ttg22-facelo: #2a2c31;
  --color-ttg22-facelo: oklch(0.29 0.006 265);
  --color-ttg22-wellhi: #1d1f23;
  --color-ttg22-wellhi: oklch(0.23 0.005 265);
  --color-ttg22-wellmid: #3b3e45;
  --color-ttg22-wellmid: oklch(0.37 0.007 265);
  --color-ttg22-welllo: #22242a;
  --color-ttg22-welllo: oklch(0.25 0.006 265);
  --color-ttg22-mhi: #c2c7d1;
  --color-ttg22-mhi: oklch(0.83 0.01 265);
  --color-ttg22-mmid: #b3b8c2;
  --color-ttg22-mmid: oklch(0.78 0.01 265);
  --color-ttg22-mlo: #8d939e;
  --color-ttg22-mlo: oklch(0.65 0.012 265);
  --color-ttg22-indicator: #1e2027;
  --color-ttg22-indicator: oklch(0.23 0.008 265);
  --color-ttg22-tick: #8f95a1;
  --color-ttg22-tick: oklch(0.66 0.012 265);
  --color-ttg22-legend: #a2a8b4;
  --color-ttg22-legend: oklch(0.73 0.012 265);
  --color-ttg22-led: #ff5a48;
  --color-ttg22-led: oklch(0.7 0.2 25);
  --color-ttg22-leddark: #3a3026;
  --color-ttg22-leddark: oklch(0.3 0.02 60);
  --color-ttg22-mute: #7e848f;
  --color-ttg22-mute: oklch(0.6 0.012 265);
  --color-ttg22-focus: #6cb6f0;
  --color-ttg22-focus: oklch(0.74 0.14 235);
  --font-ttg22-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-22 {
  width: 100%;
  min-height: 100svh;
}

.ttg-22 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
