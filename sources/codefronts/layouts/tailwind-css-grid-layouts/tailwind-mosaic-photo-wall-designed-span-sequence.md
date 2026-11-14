---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-mosaic-photo-wall-designed-span-sequence/"
title: "Tailwind Mosaic Photo Wall with a Designed Span Sequence"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A destination wall for a travel brand: ten photographs in a designed span sequence where every visual row sums to six columns, so the mosaic interlocks with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mosaic Photo Wall with a Designed Span Sequence
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-mosaic-photo-wall-designed-span-sequence/

A destination wall for a travel brand: ten photographs in a designed span sequence where every visual row sums to six columns, so the mosaic interlocks with no holes and keeps its curated order.
## HTML
```html
<section class="tgx-23 w-full min-h-svh bg-tgx23-bg font-tgx23-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-4">
    <div class="flex flex-col gap-1">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx23-accent">Meridian Travel</p>
      <h2 class="text-[1.35rem] font-semibold text-white tracking-[-0.01em]">Where we go in autumn</h2>
    </div>
    <p class="text-[0.76rem] text-tgx23-dim">Ten frames · one repeat unit</p>
  </header>
  <div class="grid grid-cols-6 max-sm:grid-cols-3 auto-rows-[minmax(70px,auto)] gap-2.5">
    <figure tabindex="0" class="group relative col-span-3 row-span-2 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=700&h=500&q=80&auto=format&fit=crop" alt="Sunlight falling through a birch forest" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-8 px-3 pb-2.5 text-[0.76rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Kuusamo, Finland <span class="font-normal text-white/75">· 6 nights</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 row-span-2 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1426604966848-d7adac402bff?w=500&h=500&q=80&auto=format&fit=crop" alt="Broad green valley with a river below" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-8 px-3 pb-2.5 text-[0.76rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Glen Affric <span class="font-normal text-white/75">· 4 nights</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=300&h=300&q=80&auto=format&fit=crop" alt="Flat sea under a pale sky" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-2 pb-1.5 text-[0.66rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Skagen</figcaption>
    </figure>
    <figure tabindex="0" class="group relative rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?w=300&h=300&q=80&auto=format&fit=crop" alt="Path through pine woodland" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-2 pb-1.5 text-[0.66rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Harz</figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 row-span-3 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=500&h=750&q=80&auto=format&fit=crop" alt="Tall rock face rising into mist" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-8 px-3 pb-2.5 text-[0.76rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Lofoten <span class="font-normal text-white/75">· 8 nights</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=500&h=280&q=80&auto=format&fit=crop" alt="Mountain range with cloud in the valley" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-3 pb-1.5 text-[0.7rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Hardanger</figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 row-span-2 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=500&h=500&q=80&auto=format&fit=crop" alt="Still lake below a wooded ridge at dusk" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-8 px-3 pb-2.5 text-[0.76rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Lake Bled <span class="font-normal text-white/75">· 3 nights</span></figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-2 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500&h=280&q=80&auto=format&fit=crop" alt="Coastal ridge under breaking cloud" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-3 pb-1.5 text-[0.7rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Faroes</figcaption>
    </figure>
    <figure tabindex="0" class="group relative col-span-3 rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=700&h=280&q=80&auto=format&fit=crop" alt="City skyline at night from across the water" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-3 pb-1.5 text-[0.7rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Stopover: Copenhagen</figcaption>
    </figure>
    <figure tabindex="0" class="group relative rounded-xl overflow-hidden bg-tgx23-cell focus-visible:outline-2 focus-visible:outline-tgx23-ring focus-visible:outline-offset-2">
      <img src="https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=300&h=300&q=80&auto=format&fit=crop" alt="Dense city skyline at dusk" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-black/0 transition-colors duration-300 group-hover:bg-black/35 group-focus-within:bg-black/35 motion-reduce:transition-none"></span>
      <figcaption class="absolute inset-x-0 bottom-0 z-10 pt-6 px-2 pb-1.5 text-[0.66rem] font-medium text-white bg-[linear-gradient(180deg,transparent,oklch(0.14_0.02_140/0.88))] opacity-0 transition-opacity duration-300 group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">+ 12 more</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx23-bg: #1b241d;
  --color-tgx23-bg: oklch(0.23 0.02 145);
  --color-tgx23-cell: #2b362d;
  --color-tgx23-cell: oklch(0.31 0.02 145);
  --color-tgx23-dim: #b3c1b6;
  --color-tgx23-dim: oklch(0.79 0.02 145);
  --color-tgx23-accent: #9fdc86;
  --color-tgx23-accent: oklch(0.84 0.13 135);
  --color-tgx23-ring: #b7e87f;
  --color-tgx23-ring: oklch(0.87 0.13 130);
  --font-tgx23-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-23 {
  width: 100%;
  min-height: 100svh;
}
```
