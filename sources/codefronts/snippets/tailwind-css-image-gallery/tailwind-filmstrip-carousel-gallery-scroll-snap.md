---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-filmstrip-carousel-gallery-scroll-snap/"
title: "Tailwind Filmstrip Carousel Gallery with CSS Scroll-Snap"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A low-profile strip of thumbnails that scrolls and snaps like a camera filmstrip, sprocket holes included."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Filmstrip Carousel Gallery with CSS Scroll-Snap
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-filmstrip-carousel-gallery-scroll-snap/

A low-profile strip of thumbnails that scrolls and snaps like a camera filmstrip, sprocket holes included. Tailwind ships the whole snap family as utilities, so the carousel — normally a library — is five classes on a container and one on each frame.
## HTML
```html
<section class="tgl-11 w-full min-h-svh grid place-items-center bg-tgl11-bg font-tgl11-sans py-10" aria-label="Filmstrip carousel gallery">
  <div tabindex="0" role="region" aria-label="Scrollable filmstrip, use arrow keys" class="flex gap-2.5 w-full px-5 py-6 overflow-x-auto snap-x snap-mandatory scroll-smooth bg-tgl11-film bg-[repeating-linear-gradient(90deg,#0a0a0a_0_14px,#1c1c1c_14px_22px,#0a0a0a_22px_36px),repeating-linear-gradient(90deg,#0a0a0a_0_14px,#1c1c1c_14px_22px,#0a0a0a_22px_36px)] [background-size:36px_12px,36px_12px] [background-position:0_6px,0_calc(100%-6px)] bg-repeat-x focus-visible:outline-3 focus-visible:outline-tgl11-acc focus-visible:-outline-offset-[3px] motion-reduce:[scroll-behavior:auto]">
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=500&h=340&auto=format&fit=crop" alt="Market street in Lisbon" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=500&h=340&auto=format&fit=crop" alt="Backstreet in the old town" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1505142468610-359e7d316be0?q=80&w=500&h=340&auto=format&fit=crop" alt="Hillside in early summer" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1511499767150-a48a237f0083?q=80&w=500&h=340&auto=format&fit=crop" alt="Concrete stairwell" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=500&h=340&auto=format&fit=crop" alt="Lunch at a roadside table" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1439066615861-d1af74d74000?q=80&w=500&h=340&auto=format&fit=crop" alt="Empty beach at low tide" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=500&h=340&auto=format&fit=crop" alt="Fruit stall at the market" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
    <figure class="group m-0 flex-[0_0_auto] w-[min(340px,72vw)] snap-center border-[3px] border-tgl11-frame rounded-sm bg-tgl11-frame overflow-hidden"><img src="https://images.unsplash.com/photo-1518495973542-4542c06a5843?q=80&w=500&h=340&auto=format&fit=crop" alt="Pass road above the treeline" loading="lazy" decoding="async" class="block w-full [aspect-ratio:3/2] object-cover grayscale-[0.1] contrast-[1.02] transition-[filter] duration-300 group-hover:grayscale-0 group-hover:contrast-100 motion-reduce:transition-none"></figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl11-bg: #111111;
  --color-tgl11-bg: oklch(0.18 0 0);
  --color-tgl11-film: #0a0a0a;
  --color-tgl11-film: oklch(0.13 0 0);
  --color-tgl11-frame: #e8e8e8;
  --color-tgl11-frame: oklch(0.93 0 0);
  --color-tgl11-acc: #d8b23c;
  --color-tgl11-acc: oklch(0.78 0.14 90);
  --font-tgl11-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-11 {
  width: 100%;
  min-height: 100svh;
}
/* Scrollbar styling has no variant form — it stays CSS. */

.tgl-11 [role="region"] {
  scrollbar-width: thin;
  scrollbar-color: var(--color-tgl11-acc) #222;
}

.tgl-11 [role="region"]::-webkit-scrollbar {
  height: 8px;
}

.tgl-11 [role="region"]::-webkit-scrollbar-thumb {
  background: var(--color-tgl11-acc);
  border-radius: 8px;
}

.tgl-11 ::selection {
  background: var(--color-tgl11-acc);
  color: #111;
}
```
