---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-contained-image-zoom-product-card/"
title: "Tailwind Contained Image Zoom Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The classic CRO zoom: the photo scales inside its frame while a gradient scrim and a 'Quick view' chip fade up over it — and because the frame is the link,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Contained Image Zoom Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-contained-image-zoom-product-card/

The classic CRO zoom: the photo scales inside its frame while a gradient scrim and a 'Quick view' chip fade up over it — and because the frame is the link, the whole thing is one group with a group-focus-visible: twin on every hover state. The zoom is clipped by overflow-hidden, so nothing ever spills into the neighbouring grid cell.
## HTML
```html
<section class="tpc-03 w-full min-h-svh grid place-items-center bg-tpc03-bg font-tpc03-sans px-5 py-12" aria-label="Contained image zoom product card demo">
  <article class="w-75 max-w-full">
    <a href="#meridian-tote" aria-label="Quick view: Meridian leather tote" class="group/frame relative block aspect-[4/5] rounded-2xl overflow-hidden no-underline transition-shadow duration-400 shadow-[0_14px_34px_-20px_oklch(0.35_0.06_50/0.5)] hover:shadow-[0_22px_48px_-20px_oklch(0.35_0.06_50/0.55)] focus-visible:outline-3 focus-visible:outline-tpc03-acc focus-visible:outline-offset-3">
      <span role="img" aria-label="Product photo: model carrying the Meridian leather tote" class="absolute inset-0 bg-linear-[135deg,var(--color-tpc03-ph),var(--color-tpc03-ph2)] bg-[url('https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=700&h=880&fit=crop&q=70')] bg-cover bg-center transition-transform duration-500 ease-tpc03 group-hover/frame:scale-109 group-focus-visible/frame:scale-109 motion-reduce:transition-none motion-reduce:group-hover/frame:scale-100 motion-reduce:group-focus-visible/frame:scale-100"></span>
      <span class="absolute inset-0 flex items-end justify-center pb-5.5 bg-linear-[0deg,oklch(0.28_0.04_50/0.45),transparent_55%] opacity-0 transition-opacity duration-400 group-hover/frame:opacity-100 group-focus-visible/frame:opacity-100 motion-reduce:transition-none">
        <span class="px-5 py-2.5 rounded-full bg-tpc03-chip text-tpc03-chipink text-[13px] font-semibold tracking-[0.02em] translate-y-2 transition-transform duration-400 ease-tpc03 group-hover/frame:translate-y-0 group-focus-visible/frame:translate-y-0 motion-reduce:transition-none motion-reduce:translate-y-0">Quick view</span>
      </span>
    </a>
    <div class="flex items-baseline justify-between gap-3 pt-4 px-1">
      <h3 class="text-base font-semibold text-tpc03-ink text-pretty">Meridian Leather Tote</h3>
      <p class="text-base font-bold text-tpc03-acc tabular-nums">$240</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc03-bg: #f6f3ef;
  --color-tpc03-bg: oklch(0.96 0.008 70);
  --color-tpc03-ink: #2c2115;
  --color-tpc03-ink: oklch(0.28 0.03 60);
  --color-tpc03-ph: #e8ddd0;
  --color-tpc03-ph: oklch(0.91 0.02 70);
  --color-tpc03-ph2: #d8c7b3;
  --color-tpc03-ph2: oklch(0.84 0.035 70);
  --color-tpc03-chip: #fffdfa;
  --color-tpc03-chip: oklch(0.99 0.004 70);
  --color-tpc03-chipink: #3a2a1a;
  --color-tpc03-chipink: oklch(0.3 0.035 55);
  --color-tpc03-acc: #8a5a28;
  --color-tpc03-acc: oklch(0.47 0.09 55);
  --font-tpc03-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --ease-tpc03: cubic-bezier(0.2, 0.7, 0.2, 1);
}

.tpc-03 {
  width: 100%;
  min-height: 100svh;
}

.tpc-03 ::selection {
  background: var(--color-tpc03-acc);
  color: #fff;
}
```
