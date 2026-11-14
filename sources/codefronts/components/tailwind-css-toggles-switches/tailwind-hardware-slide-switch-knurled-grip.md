---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-hardware-slide-switch-knurled-grip/"
title: "Tailwind Hardware Slide Switch with Knurled Grip"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The mute slider off the side of a phone: a knurled grip that slides in a machined channel and reveals a painted orange band behind it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hardware Slide Switch with Knurled Grip
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-hardware-slide-switch-knurled-grip/

The mute slider off the side of a phone: a knurled grip that slides in a machined channel and reveals a painted orange band behind it. No thumb glides &mdash; it travels in a slot, and the colour underneath is what tells you the state.
## HTML
```html
<section class="ttg-44 w-full min-h-svh flex flex-col items-center justify-center gap-8 px-5 py-14 bg-ttg44-bg font-ttg44-sans" aria-label="Hardware slide switch">
  <label for="ttg-44-sw" class="flex items-center gap-9 px-8 py-6 rounded-[20px] cursor-pointer bg-linear-165 from-ttg44-chassishi to-ttg44-chassislo shadow-[0_24px_50px_-26px_oklch(0_0_0/0.9),inset_0_1px_0_oklch(1_0_0/0.09)] has-checked:[&_.ttg44-state]:text-ttg44-paint">
    <span class="flex flex-col gap-0.5">
      <b class="text-[15.5px] font-semibold text-ttg44-ink">Ringer</b>
      <span class="ttg44-state text-[12.5px] text-ttg44-mute transition-colors duration-200">Slide down to silence</span>
    </span>
    <span class="relative shrink-0 w-[74px] h-11 rounded-[13px] overflow-hidden bg-ttg44-channel shadow-[inset_0_2px_5px_oklch(0_0_0/0.75),inset_0_0_0_1px_oklch(0_0_0/0.5)]">
      <span aria-hidden="true" class="absolute inset-y-1.5 left-1.5 w-8 rounded-lg bg-ttg44-paint shadow-[inset_0_1px_2px_oklch(0_0_0/0.35)]"></span>
      <input type="checkbox" id="ttg-44-sw" role="switch" aria-label="Silent mode" class="peer appearance-none absolute inset-0 w-full h-full bg-transparent cursor-pointer z-20 focus-visible:outline-3 focus-visible:outline-ttg44-focus focus-visible:outline-offset-4">
      <span aria-hidden="true" class="ttg44-grip pointer-events-none absolute top-1 left-1 z-10 w-9 h-9 rounded-[10px] bg-linear-to-b from-ttg44-griphi to-ttg44-griplo shadow-[0_2px_5px_oklch(0_0_0/0.6),inset_0_1px_0_oklch(1_0_0/0.45)] transition-transform duration-150 ease-out peer-checked:translate-x-[30px] motion-reduce:transition-none">
        <i class="absolute inset-y-2 inset-x-1.5 rounded-sm opacity-70 [background:repeating-linear-gradient(90deg,var(--color-ttg44-ridgehi)_0_1px,var(--color-ttg44-ridgelo)_1px_3px)]"></i>
      </span>
    </span>
  </label>
  <p class="text-[11px] tracking-[0.16em] uppercase text-ttg44-mute">Orange showing = silent</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg44-bg: #1b1d21;
  --color-ttg44-bg: oklch(0.23 0.005 265);
  --color-ttg44-chassishi: #3a3e45;
  --color-ttg44-chassishi: oklch(0.36 0.007 265);
  --color-ttg44-chassislo: #2b2e34;
  --color-ttg44-chassislo: oklch(0.3 0.006 265);
  --color-ttg44-channel: #17191d;
  --color-ttg44-channel: oklch(0.2 0.005 265);
  --color-ttg44-paint: #f07a2a;
  --color-ttg44-paint: oklch(0.7 0.18 50);
  --color-ttg44-griphi: #e6e9ef;
  --color-ttg44-griphi: oklch(0.93 0.006 265);
  --color-ttg44-griplo: #b7bcc6;
  --color-ttg44-griplo: oklch(0.79 0.008 265);
  --color-ttg44-ridgehi: #ffffff;
  --color-ttg44-ridgehi: oklch(1 0 0 / 0.75);
  --color-ttg44-ridgelo: #8d929c;
  --color-ttg44-ridgelo: oklch(0.65 0.01 265 / 0.6);
  --color-ttg44-ink: #e4e7ee;
  --color-ttg44-ink: oklch(0.92 0.006 265);
  --color-ttg44-mute: #949aa6;
  --color-ttg44-mute: oklch(0.68 0.012 265);
  --color-ttg44-focus: #6cb6f0;
  --color-ttg44-focus: oklch(0.74 0.14 235);
  --font-ttg44-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-44 {
  width: 100%;
  min-height: 100svh;
}

.ttg-44 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
