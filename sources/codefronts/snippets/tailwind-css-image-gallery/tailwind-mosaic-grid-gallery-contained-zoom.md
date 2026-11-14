---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-mosaic-grid-gallery-contained-zoom/"
title: "Tailwind Mosaic Grid Gallery with Contained Zoom on Hover"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A crisp mosaic where hovering a tile zooms the photograph cleanly inside its frame: the image scales, the tile does not, so nothing overlaps its neighbours…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mosaic Grid Gallery with Contained Zoom on Hover
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-mosaic-grid-gallery-contained-zoom/

A crisp mosaic where hovering a tile zooms the photograph cleanly inside its frame: the image scales, the tile does not, so nothing overlaps its neighbours and nothing reflows. The catalog micro-interaction, done the performant way.
## HTML
```html
<section class="tgl-13 w-full min-h-svh grid place-items-center bg-tgl13-bg font-tgl13-sans px-5 py-10" aria-label="Mosaic zoom gallery">
  <div class="w-[min(820px,100%)] grid grid-cols-4 gap-2.5 auto-rows-[1fr] [grid-auto-flow:dense] max-[600px]:grid-cols-2">
    <figure class="group relative m-0 col-span-2 row-span-2 [aspect-ratio:auto] overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=800&h=800&auto=format&fit=crop" alt="Golden hour over rolling hills" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Hills</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-square overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=400&h=400&auto=format&fit=crop" alt="Macro of a flower" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Bloom</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-square overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1519125323398-675f0ddb6308?q=80&w=400&h=400&auto=format&fit=crop" alt="Wild deer in a field" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Wildlife</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-square overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=400&h=400&auto=format&fit=crop" alt="Backlit green leaf" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Detail</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-square overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=400&h=400&auto=format&fit=crop" alt="Forest waterfall" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Falls</figcaption>
    </figure>
    <figure class="group relative m-0 col-span-2 [aspect-ratio:auto] overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=800&h=400&auto=format&fit=crop" alt="Valley panorama" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Valley</figcaption>
    </figure>
    <figure class="group relative m-0 aspect-square overflow-hidden rounded-[10px] bg-tgl13-well">
      <img src="https://images.unsplash.com/photo-1589003077984-894e133dabab?q=80&w=400&h=400&auto=format&fit=crop" alt="Dramatic cloudscape" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.16] group-focus-within:scale-[1.16] motion-reduce:transition-none">
      <figcaption class="absolute inset-x-0 bottom-0 px-3 pt-5 pb-2.5 text-white text-xs font-semibold tracking-[0.04em] bg-[linear-gradient(0deg,rgba(8,20,12,0.8),transparent)] opacity-0 transition-opacity duration-[350ms] group-hover:opacity-100 group-focus-within:opacity-100 motion-reduce:transition-none">Sky</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl13-bg: #f2f4f1;
  --color-tgl13-bg: oklch(0.96 0.006 145);
  --color-tgl13-well: #dfe4de;
  --color-tgl13-well: oklch(0.91 0.008 145);
  --color-tgl13-acc: #2f8a5a;
  --color-tgl13-acc: oklch(0.56 0.13 155);
  --font-tgl13-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-13 {
  width: 100%;
  min-height: 100svh;
}

.tgl-13 ::selection {
  background: var(--color-tgl13-acc);
  color: #fff;
}
```
