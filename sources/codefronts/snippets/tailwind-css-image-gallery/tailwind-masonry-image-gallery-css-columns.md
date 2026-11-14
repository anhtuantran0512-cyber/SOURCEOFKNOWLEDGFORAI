---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-masonry-image-gallery-css-columns/"
title: "Tailwind Masonry Image Gallery with CSS Columns (No JavaScript)"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "The Pinterest classic and the single most-searched gallery pattern in Tier-1 markets: staggered columns where images of different heights pack tightly with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Masonry Image Gallery with CSS Columns (No JavaScript)
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-masonry-image-gallery-css-columns/

The Pinterest classic and the single most-searched gallery pattern in Tier-1 markets: staggered columns where images of different heights pack tightly with no gaps and no layout library. In Tailwind the entire layout is three utilities — columns-4, gap-3.5, break-inside-avoid.
## HTML
```html
<section class="tgl-07 w-full min-h-svh flex items-start justify-center bg-tgl07-bg font-tgl07-sans px-5 py-10" aria-label="Masonry photo gallery">
  <div class="w-[min(920px,100%)] columns-4 gap-3.5 max-[820px]:columns-3 max-[560px]:columns-2">
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=500&h=700&auto=format&fit=crop" alt="Snow-capped mountain ridge at dawn" loading="lazy" decoding="async" width="500" height="700" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?q=80&w=500&h=400&auto=format&fit=crop" alt="Misty pine forest canopy" loading="lazy" decoding="async" width="500" height="400" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=500&h=560&auto=format&fit=crop" alt="Still alpine lake reflecting the sky" loading="lazy" decoding="async" width="500" height="560" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=500&h=620&auto=format&fit=crop" alt="Rolling desert sand dunes" loading="lazy" decoding="async" width="500" height="620" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=500&h=380&auto=format&fit=crop" alt="Turquoise ocean waves from above" loading="lazy" decoding="async" width="500" height="380" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=500&h=680&auto=format&fit=crop" alt="Tall waterfall in a green gorge" loading="lazy" decoding="async" width="500" height="680" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=500&h=460&auto=format&fit=crop" alt="City skyline at blue hour" loading="lazy" decoding="async" width="500" height="460" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=500&h=540&auto=format&fit=crop" alt="Autumn trees in gold and red" loading="lazy" decoding="async" width="500" height="540" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1449157291145-7efd050a4d0e?q=80&w=500&h=420&auto=format&fit=crop" alt="Layered red canyon walls" loading="lazy" decoding="async" width="500" height="420" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
    <figure class="group break-inside-avoid m-0 mb-3.5 rounded-xl overflow-hidden bg-tgl07-well shadow-[0_8px_22px_-16px_oklch(0.3_0.04_265/0.6)] transition-shadow duration-300 hover:shadow-[0_16px_34px_-18px_oklch(0.3_0.04_265/0.55)]"><img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=500&h=600&auto=format&fit=crop" alt="Green aurora over a snowy valley" loading="lazy" decoding="async" width="500" height="600" class="block w-full h-auto transition-transform duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:scale-[1.06] group-focus-within:scale-[1.06] motion-reduce:transition-none"></figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl07-bg: #f4f5f7;
  --color-tgl07-bg: oklch(0.97 0.003 265);
  --color-tgl07-well: #e7eaef;
  --color-tgl07-well: oklch(0.92 0.006 265);
  --color-tgl07-acc: #3d6ed6;
  --color-tgl07-acc: oklch(0.58 0.16 260);
  --font-tgl07-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-07 {
  width: 100%;
  min-height: 100svh;
}

.tgl-07 ::selection {
  background: var(--color-tgl07-acc);
  color: #fff;
}
```
