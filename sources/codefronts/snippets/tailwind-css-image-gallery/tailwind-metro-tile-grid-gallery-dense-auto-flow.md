---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-metro-tile-grid-gallery-dense-auto-flow/"
title: "Tailwind Metro Tile Grid Gallery with Dense Auto-Flow"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A Windows-8 'Metro' mosaic mixing 2&times;2 hero tiles, 2&times;1 banners and 1&times;1 squares into one dense asymmetric grid."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Metro Tile Grid Gallery with Dense Auto-Flow
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-metro-tile-grid-gallery-dense-auto-flow/

A Windows-8 'Metro' mosaic mixing 2&times;2 hero tiles, 2&times;1 banners and 1&times;1 squares into one dense asymmetric grid. The port makes each tile's size a property of the tile — col-span-2 row-span-2 sits in the markup next to the photograph that earned the space.
## HTML
```html
<section class="tgl-08 w-full min-h-svh grid place-items-center bg-tgl08-bg font-tgl08-sans px-5 py-10" aria-label="Metro tile image gallery">
  <div class="w-[min(760px,100%)] grid grid-cols-4 gap-2 auto-rows-[1fr] [grid-auto-flow:dense] max-[640px]:grid-cols-2">
    <a href="#" class="group relative col-span-2 row-span-2 [aspect-ratio:auto] overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=800&h=800&auto=format&fit=crop" alt="Modern city architecture" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Architecture</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=400&h=400&auto=format&fit=crop" alt="Busy city street" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Street</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=400&h=400&auto=format&fit=crop" alt="Coffee on a cafe table" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Cafe</span>
    </a>
    <a href="#" class="group relative col-span-2 [aspect-ratio:auto] overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1573496799652-408c2ac9fe98?q=80&w=800&h=400&auto=format&fit=crop" alt="Suspension bridge at dusk" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Bridge</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=400&h=400&auto=format&fit=crop" alt="Open air market stalls" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Market</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1523362628745-0c100150b504?q=80&w=400&h=400&auto=format&fit=crop" alt="Underground subway platform" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Transit</span>
    </a>
    <a href="#" class="group relative row-span-2 [aspect-ratio:auto] overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1418985991508-e47386d96a71?q=80&w=400&h=800&auto=format&fit=crop" alt="Glass tower rising overhead" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Skyline</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1507473885765-e6ed057f782c?q=80&w=400&h=400&auto=format&fit=crop" alt="City park in spring" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Park</span>
    </a>
    <a href="#" class="group relative aspect-square overflow-hidden rounded bg-tgl08-cell no-underline focus-visible:outline-3 focus-visible:outline-tgl08-acc focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=400&h=400&auto=format&fit=crop" alt="Neon signs at night" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.08] group-focus-visible:scale-[1.08] motion-reduce:transition-none">
      <span class="absolute inset-x-0 bottom-0 px-3.5 pt-6 pb-3 text-white text-[13px] font-semibold bg-[linear-gradient(0deg,rgba(6,10,14,0.85),transparent)] opacity-0 translate-y-2 transition-[opacity,translate] duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-visible:opacity-100 group-focus-visible:translate-y-0 motion-reduce:transition-none">Nightlife</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl08-bg: #101418;
  --color-tgl08-bg: oklch(0.17 0.01 230);
  --color-tgl08-cell: #1a2027;
  --color-tgl08-cell: oklch(0.24 0.014 230);
  --color-tgl08-acc: #35b6d4;
  --color-tgl08-acc: oklch(0.72 0.12 210);
  --font-tgl08-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-08 {
  width: 100%;
  min-height: 100svh;
}

.tgl-08 ::selection {
  background: var(--color-tgl08-acc);
  color: #06131a;
}
```
