---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-waveform-mute-toggle-animated-eq-bars/"
title: "Tailwind Waveform Mute Toggle with Animated EQ Bars"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "A mute switch that shows sound instead of describing it: five bars dance while audio is live and snap to a flatline the instant you mute."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Waveform Mute Toggle with Animated EQ Bars
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-waveform-mute-toggle-animated-eq-bars/

A mute switch that shows sound instead of describing it: five bars dance while audio is live and snap to a flatline the instant you mute. --animate-ttg09-eq in @theme mints the animate-ttg09-eq utility; per-bar delays stay inline, because a stagger is data, not a design token.
## HTML
```html
<section class="ttg-09 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg09-bg font-ttg09-sans" aria-label="Waveform mute toggle">
  <label for="ttg-09-sw" class="flex items-center gap-8 px-7 py-5 rounded-3xl cursor-pointer bg-ttg09-card border border-ttg09-edge">
    <span class="flex flex-col gap-0.5">
      <span class="text-[15.5px] font-semibold text-ttg09-ink">Studio monitor</span>
      <span class="text-[12.5px] text-ttg09-mute">Routes to the desk, not the interface</span>
    </span>
    <span class="relative shrink-0 w-24 h-12 rounded-[26px] bg-ttg09-track transition-shadow duration-300 shadow-[inset_0_2px_6px_oklch(0_0_0/0.6),inset_0_0_0_1px_var(--color-ttg09-edge)] has-checked:shadow-[inset_0_2px_6px_oklch(0_0_0/0.6),inset_0_0_0_1px_color-mix(in_oklab,var(--color-ttg09-live)_55%,transparent),0_0_18px_-4px_color-mix(in_oklab,var(--color-ttg09-live)_60%,transparent)]">
      <input type="checkbox" id="ttg-09-sw" role="switch" checked class="peer appearance-none absolute inset-0 w-full h-full rounded-[26px] bg-transparent cursor-pointer z-10 focus-visible:outline-3 focus-visible:outline-ttg09-live focus-visible:outline-offset-4">
      <span aria-hidden="true" class="absolute inset-0 flex items-center justify-center gap-[5px] pointer-events-none peer-checked:[&_i]:bg-ttg09-live peer-checked:[&_i]:[animation:ttg09-eq_var(--dur,0.9s)_ease-in-out_var(--d)_infinite_alternate] motion-reduce:peer-checked:[&_i]:[animation:none] motion-reduce:peer-checked:[&_i]:scale-y-[0.7] motion-reduce:peer-checked:[&_i:nth-child(odd)]:scale-y-[0.45]">
        <i style="--d:0s;" class="w-[5px] h-7 rounded-[3px] bg-ttg09-flat origin-center scale-y-[0.12] transition-[background-color,transform] duration-300"></i>
        <i style="--d:.14s; --dur:0.75s;" class="w-[5px] h-7 rounded-[3px] bg-ttg09-flat origin-center scale-y-[0.12] transition-[background-color,transform] duration-300"></i>
        <i style="--d:.28s;" class="w-[5px] h-7 rounded-[3px] bg-ttg09-flat origin-center scale-y-[0.12] transition-[background-color,transform] duration-300"></i>
        <i style="--d:.07s; --dur:1.05s;" class="w-[5px] h-7 rounded-[3px] bg-ttg09-flat origin-center scale-y-[0.12] transition-[background-color,transform] duration-300"></i>
        <i style="--d:.21s; --dur:0.8s;" class="w-[5px] h-7 rounded-[3px] bg-ttg09-flat origin-center scale-y-[0.12] transition-[background-color,transform] duration-300"></i>
      </span>
    </span>
  </label>
  <p class="font-ttg09-mono text-[11px] tracking-[0.14em] uppercase text-ttg09-mute">Live = dancing bars &middot; muted = flatline</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg09-bg: #0f1216;
  --color-ttg09-bg: oklch(0.18 0.008 255);
  --color-ttg09-card: #171b21;
  --color-ttg09-card: oklch(0.23 0.01 255);
  --color-ttg09-edge: #272d36;
  --color-ttg09-edge: oklch(0.31 0.012 255);
  --color-ttg09-track: #1b2028;
  --color-ttg09-track: oklch(0.25 0.012 255);
  --color-ttg09-flat: #454e5c;
  --color-ttg09-flat: oklch(0.44 0.015 255);
  --color-ttg09-live: #3ddc9a;
  --color-ttg09-live: oklch(0.82 0.16 165);
  --color-ttg09-ink: #d3dae4;
  --color-ttg09-ink: oklch(0.89 0.01 255);
  --color-ttg09-mute: #8d95a3;
  --color-ttg09-mute: oklch(0.66 0.015 255);
  --font-ttg09-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ttg09-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-ttg09-eq: ttg09-eq 0.9s ease-in-out infinite alternate;
}
/* The keyframes an --animate-* token refers to still live in plain CSS; v4 mints the
   utility from the token, not the block. */

@keyframes ttg09-eq {
  0% {
    transform: scaleY(0.25);
  }

  100% {
    transform: scaleY(1);
  }
}

.ttg-09 {
  width: 100%;
  min-height: 100svh;
}

.ttg-09 input[type="checkbox"] {
  -webkit-appearance: none;
}
```
