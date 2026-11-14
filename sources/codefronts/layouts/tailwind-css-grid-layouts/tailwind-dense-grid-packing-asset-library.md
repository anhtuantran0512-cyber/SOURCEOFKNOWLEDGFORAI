---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-dense-grid-packing-asset-library/"
title: "Tailwind Dense Grid Packing for a Mixed-Size Asset Library"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A brand-asset library where tiles come in three footprints and the grid refuses to leave holes."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dense Grid Packing for a Mixed-Size Asset Library
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-dense-grid-packing-asset-library/

A brand-asset library where tiles come in three footprints and the grid refuses to leave holes. The numbers are upload order, so you can watch the algorithm pull later assets backwards — and see exactly when that trade is acceptable.
## HTML
```html
<section class="tgx-24 w-full min-h-svh bg-tgx24-bg font-tgx24-sans p-6">
  <header class="flex items-start justify-between gap-4 flex-wrap mb-4">
    <div class="flex flex-col gap-1">
      <p class="font-tgx24-mono text-[0.66rem] tracking-[0.16em] uppercase text-tgx24-note">Brandkit · Asset library</p>
      <h2 class="text-[1.25rem] font-semibold text-white tracking-[-0.01em]">Autumn campaign · 15 assets</h2>
    </div>
    <p class="text-[0.72rem] leading-[1.5] text-tgx24-note max-w-[38ch]">Numbers are upload order. Tab order follows them too — which is why dense packing belongs on a browsing surface, not a ranked list.</p>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(84px,100%),1fr))] auto-rows-[72px] grid-flow-dense gap-2">
    <div class="col-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">01 · banner</span><strong class="text-[0.78rem] font-medium text-white">Hero 3200×800</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">02</span><strong class="text-[0.72rem] font-medium text-white">Icon</strong></div>
    <div class="col-span-2 row-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">03 · key art</span><strong class="text-[0.78rem] font-medium text-white">Poster 2000×2500</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">04</span><strong class="text-[0.72rem] font-medium text-white">Swatch</strong></div>
    <div class="col-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">05 · social</span><strong class="text-[0.78rem] font-medium text-white">OG 1200×630</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">06</span><strong class="text-[0.72rem] font-medium text-white">Mark</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">07</span><strong class="text-[0.72rem] font-medium text-white">Favicon</strong></div>
    <div class="col-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">08 · email</span><strong class="text-[0.78rem] font-medium text-white">Header 600×200</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">09</span><strong class="text-[0.72rem] font-medium text-white">Badge</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">10</span><strong class="text-[0.72rem] font-medium text-white">Sticker</strong></div>
    <div class="row-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">11 · story</span><strong class="text-[0.78rem] font-medium text-white">1080×1920</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">12</span><strong class="text-[0.72rem] font-medium text-white">Avatar</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">13</span><strong class="text-[0.72rem] font-medium text-white">Glyph</strong></div>
    <div class="col-span-2 grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellB p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">14 · print</span><strong class="text-[0.78rem] font-medium text-white">A4 flyer</strong></div>
    <div class="grid content-between rounded-xl border border-tgx24-edge bg-tgx24-cellA p-2.5"><span class="font-tgx24-mono text-[0.62rem] text-tgx24-note">15</span><strong class="text-[0.72rem] font-medium text-white">Tile</strong></div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx24-bg: #1e1426;
  --color-tgx24-bg: oklch(0.2 0.03 310);
  --color-tgx24-cellA: #47286a;
  --color-tgx24-cellA: oklch(0.36 0.11 310);
  --color-tgx24-cellB: #3a2157;
  --color-tgx24-cellB: oklch(0.31 0.09 310);
  --color-tgx24-edge: #6b46a0;
  --color-tgx24-edge: oklch(0.48 0.14 310);
  --color-tgx24-note: #c6b0dd;
  --color-tgx24-note: oklch(0.82 0.05 310);
  --font-tgx24-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx24-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-24 {
  width: 100%;
  min-height: 100svh;
}
```
