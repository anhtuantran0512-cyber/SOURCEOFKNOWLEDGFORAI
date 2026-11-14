---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-odometer-roll-on-off-toggle/"
title: "Tailwind Odometer Roll ON / OFF Toggle"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "The split-flap's mechanical cousin, rebuilt without 3D: a word stack rolls vertically behind a slotted window, with gradient shadows at the top and bottom…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Odometer Roll ON / OFF Toggle
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-odometer-roll-on-off-toggle/

The split-flap's mechanical cousin, rebuilt without 3D: a word stack rolls vertically behind a slotted window, with gradient shadows at the top and bottom edges selling the curve of a drum. Cheaper than a 3D flip and it reverses perfectly.
## HTML
```html
<section class="ttg-32 w-full min-h-svh flex flex-col items-center justify-center gap-7 px-5 py-14 bg-ttg32-bg font-ttg32-mono" aria-label="Odometer roll toggle">
  <label for="ttg-32-sw" class="flex flex-col items-center gap-5 cursor-pointer">
    <input type="checkbox" id="ttg-32-sw" role="switch" aria-label="Departures feed" class="peer sr-only">
    <span aria-hidden="true" class="relative flex items-center gap-4 px-6 py-5 rounded-2xl bg-ttg32-case shadow-[0_18px_36px_-20px_oklch(0_0_0/0.8),inset_0_1px_0_oklch(1_0_0/0.06)] peer-checked:[&_.ttg32-drum]:-translate-y-1/2 peer-checked:[&_.ttg32-status]:-translate-y-1/2 peer-focus-visible:outline-3 peer-focus-visible:outline-ttg32-glyph peer-focus-visible:outline-offset-4">
      <span class="relative block w-[132px] h-[62px] overflow-hidden rounded-lg bg-ttg32-slot shadow-[inset_0_2px_6px_oklch(0_0_0/0.7)]">
        <span class="ttg32-drum block h-[124px] transition-transform duration-[520ms] ease-[cubic-bezier(0.2,0.9,0.25,1.08)] motion-reduce:duration-150">
          <b class="grid place-items-center h-[62px] text-[36px] font-bold tracking-[0.06em] text-ttg32-dim">OFF</b>
          <b class="grid place-items-center h-[62px] text-[36px] font-bold tracking-[0.06em] text-ttg32-glyph">ON</b>
        </span>
        <span class="pointer-events-none absolute inset-x-0 top-0 h-4 bg-linear-to-b from-ttg32-shade to-transparent"></span>
        <span class="pointer-events-none absolute inset-x-0 bottom-0 h-4 bg-linear-to-t from-ttg32-shade to-transparent"></span>
      </span>
      <span class="relative block w-[86px] h-[22px] overflow-hidden">
        <span class="ttg32-status block h-11 transition-transform duration-[680ms] ease-[cubic-bezier(0.2,0.9,0.25,1.08)] motion-reduce:duration-150">
          <i class="grid place-items-center h-[22px] not-italic text-[11px] tracking-[0.18em] text-ttg32-dim">HOLDING</i>
          <i class="grid place-items-center h-[22px] not-italic text-[11px] tracking-[0.18em] text-ttg32-live">RUNNING</i>
        </span>
      </span>
    </span>
    <span class="font-ttg32-sans text-[13px] tracking-[0.06em] text-ttg32-label">Departures feed</span>
  </label>
  <p class="font-ttg32-sans text-[11px] tracking-[0.14em] uppercase text-ttg32-mute">Geared drums &middot; two weights, one state</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg32-bg: #14140f;
  --color-ttg32-bg: oklch(0.19 0.008 100);
  --color-ttg32-case: #26241e;
  --color-ttg32-case: oklch(0.27 0.01 85);
  --color-ttg32-slot: #171613;
  --color-ttg32-slot: oklch(0.2 0.008 85);
  --color-ttg32-shade: #0e0d0b;
  --color-ttg32-shade: oklch(0.15 0.006 85 / 0.85);
  --color-ttg32-glyph: #f7dc84;
  --color-ttg32-glyph: oklch(0.89 0.12 92);
  --color-ttg32-dim: #9b937a;
  --color-ttg32-dim: oklch(0.67 0.035 92);
  --color-ttg32-live: #7fdcae;
  --color-ttg32-live: oklch(0.83 0.13 165);
  --color-ttg32-label: #b6ad93;
  --color-ttg32-label: oklch(0.75 0.03 92);
  --color-ttg32-mute: #7b7460;
  --color-ttg32-mute: oklch(0.56 0.025 92);
  --font-ttg32-mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
  --font-ttg32-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.ttg-32 {
  width: 100%;
  min-height: 100svh;
}
```
