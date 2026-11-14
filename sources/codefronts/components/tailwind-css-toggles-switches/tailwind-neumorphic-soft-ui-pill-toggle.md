---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neumorphic-soft-ui-pill-toggle/"
title: "Tailwind Neumorphic Soft-UI Pill Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Dual-source lighting as utilities: the track is carved INTO the surface with two inset shadows, the knob extrudes out of it with two outset shadows, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neumorphic Soft-UI Pill Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-neumorphic-soft-ui-pill-toggle/

Dual-source lighting as utilities: the track is carved INTO the surface with two inset shadows, the knob extrudes out of it with two outset shadows, and active:before:scale-90 presses it physically into the pit before it glides across.
## HTML
```html
<section class="ttg-03 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg03-surface font-ttg03-sans" aria-label="Neumorphic pill toggle">
  <label for="ttg-03-sw" class="flex items-center gap-9 px-8 py-6 rounded-3xl cursor-pointer bg-ttg03-surface shadow-[9px_9px_20px_var(--color-ttg03-shade),-9px_-9px_20px_var(--color-ttg03-light)] transition-shadow duration-300 hover:shadow-[11px_11px_24px_var(--color-ttg03-shade),-11px_-11px_24px_var(--color-ttg03-light)]">
    <span class="flex flex-col gap-0.5">
      <span class="text-[15.5px] font-semibold text-ttg03-ink">Focus mode</span>
      <span class="text-[12.5px] text-ttg03-mute">Mutes every non-urgent ping</span>
    </span>
    <input type="checkbox" id="ttg-03-sw" role="switch" class="appearance-none shrink-0 w-20 h-11 rounded-full relative cursor-pointer bg-ttg03-surface transition-shadow duration-300 shadow-[inset_5px_5px_10px_var(--color-ttg03-shade),inset_-5px_-5px_10px_var(--color-ttg03-light)] checked:shadow-[inset_5px_5px_10px_var(--color-ttg03-shade),inset_-5px_-5px_10px_var(--color-ttg03-light),inset_0_0_14px_2px_color-mix(in_oklab,var(--color-ttg03-acc)_45%,transparent)] before:content-[''] before:absolute before:top-1.5 before:left-1.5 before:w-8 before:h-8 before:rounded-full before:bg-linear-145 before:from-ttg03-knobhi before:to-ttg03-knoblo before:shadow-[4px_4px_9px_var(--color-ttg03-shade),-4px_-4px_9px_var(--color-ttg03-light)] before:transition-[transform,box-shadow,background-color] before:duration-300 before:ease-[cubic-bezier(0.3,1.1,0.4,1)] checked:before:translate-x-9 checked:before:from-ttg03-acchi checked:before:to-ttg03-acc active:before:scale-90 checked:active:before:translate-x-9 checked:active:before:scale-90 focus-visible:outline-3 focus-visible:outline-ttg03-acc focus-visible:outline-offset-4 motion-reduce:transition-none motion-reduce:before:transition-none">
  </label>
  <p class="font-ttg03-mono text-[11px] tracking-[0.14em] uppercase text-ttg03-mute">Press it &mdash; it pushes back</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg03-surface: #e2e7ee;
  --color-ttg03-surface: oklch(0.92 0.008 255);
  --color-ttg03-shade: #b6bdc9;
  --color-ttg03-shade: oklch(0.79 0.015 255);
  --color-ttg03-light: #ffffff;
  --color-ttg03-light: oklch(1 0 0);
  --color-ttg03-knobhi: #f2f5fa;
  --color-ttg03-knobhi: oklch(0.97 0.005 255);
  --color-ttg03-knoblo: #d2d8e2;
  --color-ttg03-knoblo: oklch(0.87 0.01 255);
  --color-ttg03-acc: #5b6ef5;
  --color-ttg03-acc: oklch(0.6 0.19 273);
  --color-ttg03-acchi: #97a3ff;
  --color-ttg03-acchi: oklch(0.74 0.13 273);
  --color-ttg03-ink: #4f5765;
  --color-ttg03-ink: oklch(0.44 0.02 260);
  --color-ttg03-mute: #8c94a3;
  --color-ttg03-mute: oklch(0.65 0.015 260);
  --font-ttg03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg03-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.ttg-03 {
  width: 100%;
  min-height: 100svh;
}

.ttg-03 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
