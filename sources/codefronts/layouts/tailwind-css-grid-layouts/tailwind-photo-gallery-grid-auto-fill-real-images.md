---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-photo-gallery-grid-auto-fill-real-images/"
title: "Tailwind Photo Gallery Grid with auto-fill and Real Images"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A photographer's portfolio index: mixed crops, two feature tiles, captions that surface on hover and on keyboard focus alike."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Photo Gallery Grid with auto-fill and Real Images
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-photo-gallery-grid-auto-fill-real-images/

A photographer's portfolio index: mixed crops, two feature tiles, captions that surface on hover and on keyboard focus alike. Real images, real lazy loading, and not one media query.
## HTML
```html
<section class="tgx-03 w-full min-h-svh bg-tgx03-bg font-tgx03-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-5">
    <div class="flex flex-col gap-1">
      <p class="text-[0.68rem] tracking-[0.2em] uppercase text-tgx03-dim">Marit Solheim · Selected work</p>
      <h2 class="text-[1.4rem] font-semibold text-tgx03-ink tracking-[-0.01em]">North Atlantic, 2024–2026</h2>
    </div>
    <p class="text-[0.78rem] text-tgx03-dim tabular-nums">8 of 64 frames</p>
  </header>
  <div class="grid grid-cols-[repeat(auto-fill,minmax(min(170px,100%),1fr))] [grid-auto-flow:dense] gap-2.5">
    <figure tabindex="0" class="group relative col-span-2 aspect-[2.05/1] overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=900&h=440&q=80&auto=format&fit=crop" alt="Still lake below a wooded ridge at dusk" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Still water, Sørvágur <span class="text-white/70">· 24mm, f/8</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative aspect-square overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500&h=500&q=80&auto=format&fit=crop" alt="Sunlight through a dense stand of birch trees" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Birch stand <span class="text-white/70">· 85mm</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative row-span-2 overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=500&h=1000&q=80&auto=format&fit=crop" alt="Tall rock face rising into mist, vertical crop" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Rock face, vertical <span class="text-white/70">· 35mm</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative aspect-square overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=500&h=500&q=80&auto=format&fit=crop" alt="Green valley with a river running through it" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">River valley <span class="text-white/70">· 50mm</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative aspect-square overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=500&h=500&q=80&auto=format&fit=crop" alt="Calm sea meeting a pale sky at the horizon" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Horizon study <span class="text-white/70">· 200mm</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative aspect-square overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=500&h=500&q=80&auto=format&fit=crop" alt="Sunlit mountain range with low cloud in the valley" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Cloud line <span class="text-white/70">· 24mm</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 aspect-[2.05/1] overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=900&h=440&q=80&auto=format&fit=crop" alt="Coastal ridge under breaking cloud, panoramic crop" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Ridge, panorama <span class="text-white/70">· stitched, 3 frames</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative aspect-square overflow-hidden rounded-xl bg-tgx03-cell focus-visible:outline-2 focus-visible:outline-tgx03-ring focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=500&h=500&q=80&auto=format&fit=crop" alt="Forest path receding into soft light" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 group-focus-within:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100">
      <figcaption class="absolute inset-x-0 bottom-0 pt-8 px-3 pb-2.5 text-[0.75rem] text-white bg-[linear-gradient(180deg,transparent,oklch(0.15_0.01_260/0.88))] opacity-0 translate-y-1.5 transition duration-300 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 motion-reduce:transition-none">Path, late light <span class="text-white/70">· 35mm</span></figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx03-bg: #16161a;
  --color-tgx03-bg: oklch(0.19 0.005 285);
  --color-tgx03-cell: #232329;
  --color-tgx03-cell: oklch(0.26 0.008 285);
  --color-tgx03-ink: #f0efee;
  --color-tgx03-ink: oklch(0.95 0.004 90);
  --color-tgx03-dim: #a3a1a8;
  --color-tgx03-dim: oklch(0.72 0.008 285);
  --color-tgx03-ring: #e6b872;
  --color-tgx03-ring: oklch(0.82 0.11 75);
  --font-tgx03-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-03 {
  width: 100%;
  min-height: 100svh;
}
```
