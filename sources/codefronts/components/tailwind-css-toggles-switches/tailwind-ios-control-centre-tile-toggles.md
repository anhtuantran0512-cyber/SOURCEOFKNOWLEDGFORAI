---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-control-centre-tile-toggles/"
title: "Tailwind iOS Control Centre Tile Toggles"
section: "components"
category: "tailwind-css-toggles-switches"
category_name: "Tailwind CSS Toggles & Switches"
description: "Settings as tiles, not rows: a 2&times;2 quick-settings grid where the whole tile is the switch &mdash; it fills with its accent when on, dims to frosted…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind iOS Control Centre Tile Toggles
Source: https://codefronts.com/components/tailwind-css-toggles-switches/tailwind-ios-control-centre-tile-toggles/

Settings as tiles, not rows: a 2&times;2 quick-settings grid where the whole tile is the switch &mdash; it fills with its accent when on, dims to frosted glass when off, and dips under the finger. The touch target is 150&times;80, so nobody misses.
## HTML
```html
<section class="ttg-34 relative overflow-hidden w-full min-h-svh grid place-items-center px-5 py-14 bg-linear-150 from-ttg34-wallhi via-ttg34-wallmid to-ttg34-walllo font-ttg34-sans" aria-label="Control centre tile toggles">
  <div class="grid grid-cols-2 gap-3.5 w-[min(340px,100%)]">
    <label class="relative isolate overflow-hidden flex flex-col justify-between h-24 p-4 rounded-[22px] cursor-pointer bg-white/10 border border-white/15 transition-transform duration-200 active:scale-[0.97] motion-reduce:transition-none" style="--accent:oklch(0.62 0.2 256)">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-20 rounded-[22px] backdrop-blur-xl"></span>
      <input type="checkbox" role="switch" checked aria-label="Wi-Fi" class="peer sr-only">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[22px] bg-(--accent) opacity-0 transition-opacity duration-200 peer-checked:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[22px] peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-[3px]"></span>
      <span class="relative flex items-center justify-between peer-checked:[&_.ttg34-dot]:bg-white">
        <span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full bg-white/20 text-white text-[14px]">&#9679;</span>
        <span class="ttg34-dot w-2 h-2 rounded-full bg-white/25 transition-colors duration-200"></span>
      </span>
      <span class="relative flex flex-col peer-checked:[&_.ttg34-state]:text-white/85">
        <b class="text-[14px] font-semibold text-white leading-tight">Wi-Fi</b>
        <small class="ttg34-state text-[11.5px] text-white/55 transition-colors duration-200">Studio 5G</small>
      </span>
    </label>
    <label class="relative isolate overflow-hidden flex flex-col justify-between h-24 p-4 rounded-[22px] cursor-pointer bg-white/10 border border-white/15 transition-transform duration-200 active:scale-[0.97] motion-reduce:transition-none" style="--accent:oklch(0.6 0.19 285)">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-20 rounded-[22px] backdrop-blur-xl"></span>
      <input type="checkbox" role="switch" checked aria-label="Bluetooth" class="peer sr-only">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[22px] bg-(--accent) opacity-0 transition-opacity duration-200 peer-checked:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[22px] peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-[3px]"></span>
      <span class="relative flex items-center justify-between peer-checked:[&_.ttg34-dot]:bg-white">
        <span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full bg-white/20 text-white text-[14px]">&#10022;</span>
        <span class="ttg34-dot w-2 h-2 rounded-full bg-white/25 transition-colors duration-200"></span>
      </span>
      <span class="relative flex flex-col peer-checked:[&_.ttg34-state]:text-white/85">
        <b class="text-[14px] font-semibold text-white leading-tight">Bluetooth</b>
        <small class="ttg34-state text-[11.5px] text-white/55 transition-colors duration-200">2 devices</small>
      </span>
    </label>
    <label class="relative isolate overflow-hidden flex flex-col justify-between h-24 p-4 rounded-[22px] cursor-pointer bg-white/10 border border-white/15 transition-transform duration-200 active:scale-[0.97] motion-reduce:transition-none" style="--accent:oklch(0.68 0.19 50)">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-20 rounded-[22px] backdrop-blur-xl"></span>
      <input type="checkbox" role="switch" aria-label="Focus" class="peer sr-only">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[22px] bg-(--accent) opacity-0 transition-opacity duration-200 peer-checked:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[22px] peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-[3px]"></span>
      <span class="relative flex items-center justify-between peer-checked:[&_.ttg34-dot]:bg-white">
        <span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full bg-white/20 text-white text-[14px]">&#9790;</span>
        <span class="ttg34-dot w-2 h-2 rounded-full bg-white/25 transition-colors duration-200"></span>
      </span>
      <span class="relative flex flex-col peer-checked:[&_.ttg34-state]:text-white/85">
        <b class="text-[14px] font-semibold text-white leading-tight">Focus</b>
        <small class="ttg34-state text-[11.5px] text-white/55 transition-colors duration-200">Off</small>
      </span>
    </label>
    <label class="relative isolate overflow-hidden flex flex-col justify-between h-24 p-4 rounded-[22px] cursor-pointer bg-white/10 border border-white/15 transition-transform duration-200 active:scale-[0.97] motion-reduce:transition-none" style="--accent:oklch(0.72 0.17 150)">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-20 rounded-[22px] backdrop-blur-xl"></span>
      <input type="checkbox" role="switch" aria-label="Low power mode" class="peer sr-only">
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 rounded-[22px] bg-(--accent) opacity-0 transition-opacity duration-200 peer-checked:opacity-100 motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="pointer-events-none absolute inset-0 rounded-[22px] peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-[3px]"></span>
      <span class="relative flex items-center justify-between peer-checked:[&_.ttg34-dot]:bg-white">
        <span aria-hidden="true" class="grid place-items-center w-7 h-7 rounded-full bg-white/20 text-white text-[14px]">&#9889;</span>
        <span class="ttg34-dot w-2 h-2 rounded-full bg-white/25 transition-colors duration-200"></span>
      </span>
      <span class="relative flex flex-col peer-checked:[&_.ttg34-state]:text-white/85">
        <b class="text-[14px] font-semibold text-white leading-tight">Low Power</b>
        <small class="ttg34-state text-[11.5px] text-white/55 transition-colors duration-200">Off</small>
      </span>
    </label>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg34-wallhi: #2a1f4d;
  --color-ttg34-wallhi: oklch(0.3 0.09 295);
  --color-ttg34-wallmid: #1b2a52;
  --color-ttg34-wallmid: oklch(0.31 0.08 265);
  --color-ttg34-walllo: #123240;
  --color-ttg34-walllo: oklch(0.33 0.06 220);
  --font-ttg34-sans: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif;
}

.ttg-34 {
  width: 100%;
  min-height: 100svh;
}
/* The frost lives on an inner layer, never on the :has() subject — see notes. */

.ttg-34 label > span[aria-hidden]:first-child {
  -webkit-backdrop-filter: blur(24px);
}
```
