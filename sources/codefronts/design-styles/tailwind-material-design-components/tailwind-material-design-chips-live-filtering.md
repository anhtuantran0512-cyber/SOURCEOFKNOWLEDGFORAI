---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-chips-live-filtering/"
title: "Tailwind Material Design Chips with Live Filtering"
section: "design-styles"
category: "tailwind-material-design-components"
category_name: "Material Design Components in Tailwind CSS"
description: "All four M3 chip types &mdash; assist, filter, input and suggestion &mdash; and then the part the CSS version could only fake: the filter chips actually filter."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material Design Chips with Live Filtering
Source: https://codefronts.com/design-styles/tailwind-material-design-components/tailwind-material-design-chips-live-filtering/

All four M3 chip types &mdash; assist, filter, input and suggestion &mdash; and then the part the CSS version could only fake: the filter chips actually filter. Checking a chip reveals its matching cards through a has-[#id:checked]: rule on the results grid, so a live filter runs with no JavaScript at all.
## HTML
```html
<section class="tmd-08 w-full min-h-svh bg-tmd08-bg font-tmd08-sans text-tmd08-onsurface px-5 py-9" aria-label="Material Design chips demo">
  <div class="w-[min(900px,100%)] mx-auto grid gap-6">
    <header class="grid gap-1.5">
      <h2 class="text-[26px] font-medium tracking-[-0.01em]">Chips that actually filter</h2>
      <p class="text-sm text-tmd08-onvariant">Four M3 chip types, and a working facet filter built from <code class="font-tmd08-mono text-[12px]">has-[…:checked]:*:data-[tag]:block</code>.</p>
    </header>

    <div class="group/filter grid gap-4 p-5.5 rounded-3xl bg-tmd08-surface shadow-tmd08-1">
      <span class="font-tmd08-mono text-[11px] uppercase tracking-[0.1em] text-tmd08-onvariant">Filter chips &mdash; live</span>
      <div class="flex flex-wrap gap-2">
        <input type="checkbox" id="tmd08-f1" class="peer/f1 sr-only">
        <label for="tmd08-f1" class="relative overflow-hidden inline-flex items-center gap-1.5 min-h-11 px-4 rounded-lg cursor-pointer border border-tmd08-outline text-sm font-medium text-tmd08-onsurface transition-colors duration-200 group-has-[#tmd08-f1:checked]/filter:bg-tmd08-secondarycontainer group-has-[#tmd08-f1:checked]/filter:text-tmd08-onsecondarycontainer group-has-[#tmd08-f1:checked]/filter:border-transparent peer-focus-visible/f1:outline-2 peer-focus-visible/f1:outline-offset-2 peer-focus-visible/f1:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon shrink-0 w-0 overflow-hidden text-[18px] leading-none transition-[width] duration-200 group-has-[#tmd08-f1:checked]/filter:w-4.5 motion-reduce:transition-none" aria-hidden="true">check</span>Deep water</label>
        <input type="checkbox" id="tmd08-f2" class="peer/f2 sr-only">
        <label for="tmd08-f2" class="relative overflow-hidden inline-flex items-center gap-1.5 min-h-11 px-4 rounded-lg cursor-pointer border border-tmd08-outline text-sm font-medium text-tmd08-onsurface transition-colors duration-200 group-has-[#tmd08-f2:checked]/filter:bg-tmd08-secondarycontainer group-has-[#tmd08-f2:checked]/filter:text-tmd08-onsecondarycontainer group-has-[#tmd08-f2:checked]/filter:border-transparent peer-focus-visible/f2:outline-2 peer-focus-visible/f2:outline-offset-2 peer-focus-visible/f2:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon shrink-0 w-0 overflow-hidden text-[18px] leading-none transition-[width] duration-200 group-has-[#tmd08-f2:checked]/filter:w-4.5 motion-reduce:transition-none" aria-hidden="true">check</span>Coastal</label>
        <input type="checkbox" id="tmd08-f3" class="peer/f3 sr-only">
        <label for="tmd08-f3" class="relative overflow-hidden inline-flex items-center gap-1.5 min-h-11 px-4 rounded-lg cursor-pointer border border-tmd08-outline text-sm font-medium text-tmd08-onsurface transition-colors duration-200 group-has-[#tmd08-f3:checked]/filter:bg-tmd08-secondarycontainer group-has-[#tmd08-f3:checked]/filter:text-tmd08-onsecondarycontainer group-has-[#tmd08-f3:checked]/filter:border-transparent peer-focus-visible/f3:outline-2 peer-focus-visible/f3:outline-offset-2 peer-focus-visible/f3:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon shrink-0 w-0 overflow-hidden text-[18px] leading-none transition-[width] duration-200 group-has-[#tmd08-f3:checked]/filter:w-4.5 motion-reduce:transition-none" aria-hidden="true">check</span>Estuary</label>
      </div>

      <div class="grid gap-2 grid-cols-[repeat(auto-fit,minmax(min(200px,100%),1fr))] group-has-[:checked]/filter:*:hidden group-has-[#tmd08-f1:checked]/filter:*:data-[tag=deep]:block group-has-[#tmd08-f2:checked]/filter:*:data-[tag=coastal]:block group-has-[#tmd08-f3:checked]/filter:*:data-[tag=estuary]:block">
        <article data-tag="deep" class="grid gap-1 p-4 rounded-2xl bg-tmd08-surface2"><b class="text-sm font-medium">ST-014 &middot; 1 240 m</b><span class="text-xs text-tmd08-onvariant">Deep water &middot; North Atlantic</span></article>
        <article data-tag="coastal" class="grid gap-1 p-4 rounded-2xl bg-tmd08-surface2"><b class="text-sm font-medium">ST-059 &middot; 312 m</b><span class="text-xs text-tmd08-onvariant">Coastal &middot; Irish Shelf</span></article>
        <article data-tag="estuary" class="grid gap-1 p-4 rounded-2xl bg-tmd08-surface2"><b class="text-sm font-medium">ST-022 &middot; 86 m</b><span class="text-xs text-tmd08-onvariant">Estuary &middot; Baltic</span></article>
        <article data-tag="deep" class="grid gap-1 p-4 rounded-2xl bg-tmd08-surface2"><b class="text-sm font-medium">ST-047 &middot; 2 010 m</b><span class="text-xs text-tmd08-onvariant">Deep water &middot; Norwegian Sea</span></article>
      </div>
      <p class="text-xs text-tmd08-onvariant">Unchecked shows everything; checking a chip narrows the grid. No script &mdash; the grid states its own filter rules.</p>
    </div>

    <div class="grid gap-4 p-5.5 rounded-3xl bg-tmd08-surface shadow-tmd08-1">
      <span class="font-tmd08-mono text-[11px] uppercase tracking-[0.1em] text-tmd08-onvariant">Assist, suggestion &amp; elevated</span>
      <div class="flex flex-wrap gap-2">
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-4 rounded-lg cursor-pointer bg-transparent border border-tmd08-outline text-sm font-medium text-tmd08-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd08-icon text-[18px] leading-none text-tmd08-primary" aria-hidden="true">event</span>Schedule dive</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center gap-2 min-h-11 px-4 rounded-lg cursor-pointer bg-transparent border border-tmd08-outline text-sm font-medium text-tmd08-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08] active:before:opacity-[0.12]"><span class="font-tmd08-icon text-[18px] leading-none text-tmd08-primary" aria-hidden="true">near_me</span>Nearest station</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-lg cursor-pointer bg-tmd08-surface border-0 shadow-tmd08-1 text-sm font-medium text-tmd08-onsurface focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Elevated chip</button>
        <button type="button" class="relative overflow-hidden inline-flex items-center min-h-11 px-4 rounded-lg cursor-pointer bg-transparent border border-tmd08-outlinevariant text-sm font-medium text-tmd08-onvariant focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmd08-primary before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]">Suggestion</button>
        <span aria-disabled="true" class="inline-flex items-center min-h-11 px-4 rounded-lg border border-tmd08-outline text-sm font-medium text-tmd08-onsurface opacity-38 pointer-events-none">Disabled</span>
      </div>
    </div>

    <div class="grid gap-4 p-5.5 rounded-3xl bg-tmd08-surface shadow-tmd08-1">
      <span class="font-tmd08-mono text-[11px] uppercase tracking-[0.1em] text-tmd08-onvariant">Input chips &mdash; with remove controls</span>
      <div class="flex flex-wrap gap-2">
        <span class="inline-flex items-center gap-1 min-h-11 pl-1.5 pr-1 rounded-lg border border-tmd08-outline text-sm has-[button:focus-visible]:ring-2 has-[button:focus-visible]:ring-tmd08-primary"><span class="grid place-items-center w-7 h-7 rounded-full bg-tmd08-primary text-white font-tmd08-mono text-[11px]">MK</span>M. Kovač<button type="button" aria-label="Remove M. Kovač" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-lg border-0 bg-transparent cursor-pointer text-tmd08-onvariant focus-visible:outline-none before:absolute before:inset-2 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon text-[18px] leading-none" aria-hidden="true">close</span></button></span>
        <span class="inline-flex items-center gap-1 min-h-11 pl-3 pr-1 rounded-lg border border-tmd08-outline text-sm has-[button:focus-visible]:ring-2 has-[button:focus-visible]:ring-tmd08-primary">depth &gt; 500 m<button type="button" aria-label="Remove depth filter" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-lg border-0 bg-transparent cursor-pointer text-tmd08-onvariant focus-visible:outline-none before:absolute before:inset-2 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon text-[18px] leading-none" aria-hidden="true">close</span></button></span>
        <span class="inline-flex items-center gap-1 min-h-11 pl-3 pr-1 rounded-lg bg-tmd08-secondarycontainer text-tmd08-onsecondarycontainer text-sm has-[button:focus-visible]:ring-2 has-[button:focus-visible]:ring-tmd08-primary">QC flagged<button type="button" aria-label="Remove QC filter" class="relative overflow-hidden grid place-items-center min-w-11 min-h-11 rounded-lg border-0 bg-transparent cursor-pointer text-current focus-visible:outline-none before:absolute before:inset-2 before:rounded-full before:bg-current before:opacity-0 before:transition-opacity hover:before:opacity-[0.08]"><span class="font-tmd08-icon text-[18px] leading-none" aria-hidden="true">close</span></button></span>
      </div>
      <p class="text-xs text-tmd08-onvariant">The chip shows a ring when its remove button takes focus &mdash; <span class="font-tmd08-mono text-[11px]">has-[button:focus-visible]:ring-2</span>, the wrapper reacting to a descendant.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmd08-bg: #fce4ec;
  --color-tmd08-bg: oklch(0.941 0.028 355.4);
  --color-tmd08-surface: #ffffff;
  --color-tmd08-surface: oklch(1 0 89.9);
  --color-tmd08-surface2: #fdf0f4;
  --color-tmd08-surface2: oklch(0.966 0.015 356.6);
  --color-tmd08-primary: #ad1457;
  --color-tmd08-primary: oklch(0.49 0.187 2.5);
  --color-tmd08-secondarycontainer: #ffd8e4;
  --color-tmd08-secondarycontainer: oklch(0.918 0.046 357.6);
  --color-tmd08-onsecondarycontainer: #31111d;
  --color-tmd08-onsecondarycontainer: oklch(0.232 0.054 358.6);
  --color-tmd08-onsurface: #1f1a1c;
  --color-tmd08-onsurface: oklch(0.224 0.009 351.7);
  --color-tmd08-onvariant: #5c4650;
  --color-tmd08-onvariant: oklch(0.421 0.034 349.6);
  --color-tmd08-outline: #85737b;
  --color-tmd08-outline: oklch(0.575 0.025 349.3);
  --color-tmd08-outlinevariant: #e4c8d2;
  --color-tmd08-outlinevariant: oklch(0.859 0.034 354.3);
  --font-tmd08-sans: 'Roboto Flex', 'Roboto', system-ui, sans-serif;
  --font-tmd08-mono: 'Roboto Mono', ui-monospace, monospace;
  --font-tmd08-icon: 'Material Symbols Outlined';
  --shadow-tmd08-1: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 3px 1px rgb(0 0 0 / 0.15);
}

.tmd-08 {
  width: 100%;
  min-height: 100svh;
}

.tmd-08 .font-tmd08-icon {
  font-feature-settings: 'liga';
}
```
