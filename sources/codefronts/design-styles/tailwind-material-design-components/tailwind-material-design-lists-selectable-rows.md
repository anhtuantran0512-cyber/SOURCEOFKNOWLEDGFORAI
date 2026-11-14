---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-lists-selectable-rows/"
title: "Tailwind Material Design Lists and Swipeable Rows"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "The full M3 list vocabulary &mdash; one, two and three-line items, leading avatars and icons, trailing metadata, checkboxes and switches, inset dividers and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Lists and Swipeable Rows
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-lists-selectable-rows/

The full M3 list vocabulary &mdash; one, two and three-line items, leading avatars and icons, trailing metadata, checkboxes and switches, inset dividers and a sticky subheader. The port's structural idea: every item is the same grid-cols-[auto_1fr_auto], so a one-line row and a three-line row differ only in how many children the middle track holds.
## HTML
```html
<section class="tmd-12 w-full min-h-svh bg-tmd12-bg font-tmd12-sans text-tmd12-onsurface px-5 py-9" aria-label="Material Design lists demo">
  <div class="w-[min(860px,100%)] mx-auto grid gap-6 md:grid-cols-2">
    <div class="grid content-start gap-1.5 md:col-span-2">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Lists</h2>
      <p class="text-sm text-tmd12-onvariant">One item recipe &mdash; <code class="font-tmd12-mono text-[12px]">grid-cols-[auto_1fr_auto]</code> &mdash; at three densities.</p>
    </div>

    <div class="rounded-3xl overflow-hidden bg-tmd12-surface shadow-tmd12-1">
      <ul role="list" class="list-none m-0 p-0 divide-y divide-tmd12-outlinevariant max-h-96 overflow-y-auto">
        <li class="sticky top-0 z-1 px-4 py-2 bg-tmd12-surface font-tmd12-mono text-[11px] uppercase tracking-[0.1em] text-tmd12-onvariant">Today</li>
        <li><a href="#m1" class="relative overflow-hidden grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-22 px-4 py-3 no-underline text-tmd12-onsurface focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd12-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">
          <span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-primary text-white font-tmd12-mono text-sm" aria-hidden="true">MK</span>
          <span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">Marta Kovač</b><small class="text-sm text-tmd12-onvariant line-clamp-2 leading-5">Calibration drift on ST-022 is now outside tolerance &mdash; I have queued a service window for Thursday and attached the last four casts for comparison.</small></span>
          <span class="grid justify-items-end gap-1.5"><small class="font-tmd12-mono text-[11px] text-tmd12-onvariant">10:24</small><b class="min-w-4 h-4 px-1 grid place-items-center rounded-full bg-tmd12-primary text-white font-tmd12-mono text-[10px] not-italic">2</b></span>
        </a></li>
        <li><a href="#m2" class="relative overflow-hidden grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-18 px-4 no-underline text-tmd12-onsurface focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd12-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">
          <span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 text-tmd12-onvariant font-tmd12-icon text-[20px] leading-none" aria-hidden="true">cloud_done</span>
          <span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">Nightly sync complete</b><small class="text-sm text-tmd12-onvariant truncate">18 stations &middot; 4 210 readings</small></span>
          <small class="font-tmd12-mono text-[11px] text-tmd12-onvariant">04:00</small>
        </a></li>
        <li class="sticky top-0 z-1 px-4 py-2 bg-tmd12-surface font-tmd12-mono text-[11px] uppercase tracking-[0.1em] text-tmd12-onvariant">Earlier</li>
        <li><a href="#m3" class="relative overflow-hidden grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-14 px-4 no-underline text-tmd12-onsurface focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd12-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">
          <span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 text-tmd12-onvariant font-tmd12-icon text-[20px] leading-none" aria-hidden="true">description</span>
          <b class="text-[15px] font-normal min-w-0 truncate">Q2 survey report.pdf</b>
          <span class="font-tmd12-icon text-[20px] leading-none text-tmd12-onvariant" aria-hidden="true">chevron_right</span>
        </a></li>
        <li><a href="#m4" class="relative overflow-hidden grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-14 px-4 no-underline text-tmd12-onsurface focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tmd12-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">
          <span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 text-tmd12-onvariant font-tmd12-icon text-[20px] leading-none" aria-hidden="true">table_chart</span>
          <b class="text-[15px] font-normal min-w-0 truncate">station-metadata.csv</b>
          <span class="font-tmd12-icon text-[20px] leading-none text-tmd12-onvariant" aria-hidden="true">chevron_right</span>
        </a></li>
      </ul>
    </div>

    <div class="grid content-start gap-6">
      <div class="rounded-3xl overflow-hidden bg-tmd12-surface shadow-tmd12-1">
        <span class="block px-4 pt-4 pb-2 font-tmd12-mono text-[11px] uppercase tracking-[0.1em] text-tmd12-onvariant">Selectable rows &mdash; has-checked:</span>
        <ul role="list" class="list-none m-0 p-0 divide-y divide-tmd12-outlinevariant">
          <li class="transition-colors duration-150 has-checked:bg-tmd12-selected"><label class="grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-18 px-4 cursor-pointer"><span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 font-tmd12-icon text-[20px] leading-none text-tmd12-onvariant" aria-hidden="true">sensors</span><span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">ST-014</b><small class="text-sm text-tmd12-onvariant truncate">North Atlantic &middot; online</small></span><input type="checkbox" checked class="w-5 h-5 accent-tmd12-primary cursor-pointer"></label></li>
          <li class="transition-colors duration-150 has-checked:bg-tmd12-selected"><label class="grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-18 px-4 cursor-pointer"><span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 font-tmd12-icon text-[20px] leading-none text-tmd12-onvariant" aria-hidden="true">sensors</span><span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">ST-022</b><small class="text-sm text-tmd12-onvariant truncate">Baltic &middot; drifting</small></span><input type="checkbox" class="w-5 h-5 accent-tmd12-primary cursor-pointer"></label></li>
          <li class="transition-colors duration-150 has-checked:bg-tmd12-selected"><label class="grid grid-cols-[auto_1fr_auto] items-center gap-4 min-h-18 px-4 cursor-pointer"><span class="grid place-items-center w-10 h-10 rounded-full bg-tmd12-surface2 font-tmd12-icon text-[20px] leading-none text-tmd12-onvariant" aria-hidden="true">sensors</span><span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">ST-047</b><small class="text-sm text-tmd12-onvariant truncate">Norwegian Sea &middot; offline</small></span><input type="checkbox" class="w-5 h-5 accent-tmd12-primary cursor-pointer"></label></li>
        </ul>
      </div>

      <div class="rounded-3xl overflow-hidden bg-tmd12-surface shadow-tmd12-1">
        <span class="block px-4 pt-4 pb-2 font-tmd12-mono text-[11px] uppercase tracking-[0.1em] text-tmd12-onvariant">Trailing switches</span>
        <ul role="list" class="list-none m-0 p-0 divide-y divide-tmd12-outlinevariant">
          <li><label class="grid grid-cols-[1fr_auto] items-center gap-4 min-h-18 px-4 cursor-pointer"><span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">Push alerts</b><small class="text-sm text-tmd12-onvariant">Drift and offline events</small></span><input type="checkbox" role="switch" checked class="peer sr-only"><span class="relative w-13 h-8 rounded-full bg-tmd12-outlinevariant border-2 border-tmd12-outline transition-colors duration-200 peer-checked:bg-tmd12-primary peer-checked:border-tmd12-primary peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmd12-primary after:absolute after:top-1/2 after:left-1 after:[transform:translate(0,-50%)] after:w-4 after:h-4 after:rounded-full after:bg-tmd12-outline after:transition-[transform,width,height,background] after:duration-200 peer-checked:after:[transform:translate(20px,-50%)] peer-checked:after:w-6 peer-checked:after:h-6 peer-checked:after:bg-white motion-reduce:transition-none" aria-hidden="true"></span></label></li>
          <li><label class="grid grid-cols-[1fr_auto] items-center gap-4 min-h-18 px-4 cursor-pointer"><span class="grid gap-0.5 min-w-0"><b class="text-[15px] font-medium">Offline copies</b><small class="text-sm text-tmd12-onvariant">Roughly 40 MB per survey</small></span><input type="checkbox" role="switch" class="peer sr-only"><span class="relative w-13 h-8 rounded-full bg-tmd12-outlinevariant border-2 border-tmd12-outline transition-colors duration-200 peer-checked:bg-tmd12-primary peer-checked:border-tmd12-primary peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmd12-primary after:absolute after:top-1/2 after:left-1 after:[transform:translate(0,-50%)] after:w-4 after:h-4 after:rounded-full after:bg-tmd12-outline after:transition-[transform,width,height,background] after:duration-200 peer-checked:after:[transform:translate(20px,-50%)] peer-checked:after:w-6 peer-checked:after:h-6 peer-checked:after:bg-white motion-reduce:transition-none" aria-hidden="true"></span></label></li>
        </ul>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd12-bg: #f5f7fa;
  --color-tmd12-bg: oklch(0.975 0.005 258.3);
  --color-tmd12-surface: #ffffff;
  --color-tmd12-surface: oklch(1 0 89.9);
  --color-tmd12-surface2: #eef2f7;
  --color-tmd12-surface2: oklch(0.96 0.008 253.9);
  --color-tmd12-primary: #1976d2;
  --color-tmd12-primary: oklch(0.565 0.163 253.3);
  --color-tmd12-selected: #e3f2fd;
  --color-tmd12-selected: oklch(0.953 0.022 239.4);
  --color-tmd12-onsurface: #1c1b1f;
  --color-tmd12-onsurface: oklch(0.225 0.008 297.2);
  --color-tmd12-onvariant: #4f5b66;
  --color-tmd12-onvariant: oklch(0.465 0.023 246);
  --color-tmd12-outline: #79747e;
  --color-tmd12-outline: oklch(0.567 0.016 308.1);
  --color-tmd12-outlinevariant: #e2e6ec;
  --color-tmd12-outlinevariant: oklch(0.924 0.009 258.3);
  --font-tmd12-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd12-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd12-icon: 'Material Symbols Outlined';
  --shadow-tmd12-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-12 {
  width: 100%;
  min-height: 100svh;
}

.tmd-12 .font-tmd12-icon {
  font-feature-settings: 'liga';
}
```
