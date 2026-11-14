---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-justified-image-gallery-aspect-ratio-flex/"
title: "Tailwind Justified Image Gallery with Aspect-Ratio Flex Rows"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "The Google-Images / Flickr look: fluid rows where every photo keeps its native aspect ratio — nothing is cropped — yet each row stretches flush to both edges."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Justified Image Gallery with Aspect-Ratio Flex Rows
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-justified-image-gallery-aspect-ratio-flex/

The Google-Images / Flickr look: fluid rows where every photo keeps its native aspect ratio — nothing is cropped — yet each row stretches flush to both edges. No JS measuring pass, and in Tailwind the whole trick reduces to two arbitrary values that both read the same per-item variable.
## HTML
```html
<section class="tgl-02 w-full min-h-svh grid place-items-center bg-tgl02-bg font-tgl02-sans px-5 py-10" aria-label="Justified aspect-ratio gallery">
  <div class="w-[min(920px,100%)] flex flex-col gap-2">
    <div class="flex gap-2 max-[600px]:flex-wrap">
      <figure style="--r:1.5" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1618773928121-c32242e63f39?q=80&w=600&h=400&auto=format&fit=crop" alt="Wide sandy beach" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:0.75" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?q=80&w=450&h=600&auto=format&fit=crop" alt="Coastal lighthouse" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:1.33" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=600&h=450&auto=format&fit=crop" alt="Wooden pier over water" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
    </div>
    <div class="flex gap-2 max-[600px]:flex-wrap">
      <figure style="--r:1.78" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1483412033650-1015ddeb83d1?q=80&w=640&h=360&auto=format&fit=crop" alt="Green valley panorama" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:1" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?q=80&w=500&h=500&auto=format&fit=crop" alt="Close-up of a wildflower" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:1.4" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=560&h=400&auto=format&fit=crop" alt="River through a forest" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
    </div>
    <div class="flex gap-2 max-[600px]:flex-wrap">
      <figure style="--r:0.8" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=480&h=600&auto=format&fit=crop" alt="Tall narrow waterfall" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:1.6" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=640&h=400&auto=format&fit=crop" alt="Sunlit sand dunes" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
      <figure style="--r:1.2" class="group flex-[var(--r)_1_0] [aspect-ratio:var(--r)] rounded-lg overflow-hidden bg-tgl02-well m-0 max-[600px]:flex-[1_1_40%]"><img src="https://images.unsplash.com/photo-1522542550221-31fd19575a2d?q=80&w=540&h=450&auto=format&fit=crop" alt="Alpine meadow in bloom" loading="lazy" decoding="async" class="block w-full h-full object-cover transition-transform duration-[400ms] group-hover:scale-105 motion-reduce:transition-none"></figure>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl02-bg: #fafafa;
  --color-tgl02-bg: oklch(0.98 0 0);
  --color-tgl02-well: #e6e8ea;
  --color-tgl02-well: oklch(0.92 0.004 220);
  --color-tgl02-acc: #2f9e6e;
  --color-tgl02-acc: oklch(0.62 0.13 160);
  --font-tgl02-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-02 {
  width: 100%;
  min-height: 100svh;
}

.tgl-02 ::selection {
  background: var(--color-tgl02-acc);
  color: #fff;
}
```
