---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-slide-up-details-panel-product-card/"
title: "Tailwind Slide-Up Details Panel Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The space-saving overlay dense catalogs live on: name and price at rest, and a full detail panel — description, size chips, CTA — slides up over the photo on…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-Up Details Panel Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-slide-up-details-panel-product-card/

The space-saving overlay dense catalogs live on: name and price at rest, and a full detail panel — description, size chips, CTA — slides up over the photo on hover or focus. The peek height is a single arbitrary translate-y-[calc(100%-66px)], so the resting strip and the open state are one edit apart.
## HTML
```html
<section class="tpc-05 w-full min-h-svh grid place-items-center bg-tpc05-bg font-tpc05-sans px-5 py-12" aria-label="Slide-up details panel product card demo">
  <article class="group relative w-75 max-w-full aspect-[3/4] rounded-[18px] overflow-hidden shadow-[0_18px_40px_-22px_oklch(0.35_0.04_80/0.55)]">
    <div role="img" aria-label="Product photo: model wearing the Field canvas jacket" class="absolute inset-0 bg-linear-[135deg,var(--color-tpc05-ph),var(--color-tpc05-ph2)] bg-[url('https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=700&h=930&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="absolute inset-x-0 bottom-0 px-5 pt-4.5 pb-5 rounded-t-[18px] bg-tpc05-panel backdrop-blur-sm translate-y-[calc(100%-66px)] transition-transform duration-450 ease-tpc05 group-hover:translate-y-0 group-focus-within:translate-y-0 motion-reduce:transition-none">
      <div class="flex items-baseline justify-between gap-2.5">
        <h3 class="text-[17px] font-semibold text-tpc05-ink">Field Canvas Jacket</h3>
        <p class="text-[17px] font-bold text-tpc05-acc tabular-nums">$128</p>
      </div>
      <p class="mt-3 text-[13.5px] leading-[1.55] text-tpc05-mut text-pretty">Waxed 12oz cotton canvas with a corduroy collar and a relaxed field cut.</p>
      <div role="group" aria-label="Available sizes" class="mt-3.5 flex gap-2">
        <button type="button" class="min-w-11 min-h-11 rounded-[10px] border border-tpc05-edge bg-tpc05-chip text-tpc05-chipink text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:border-tpc05-acc hover:text-tpc05-acc focus-visible:outline-2 focus-visible:outline-tpc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none">S</button>
        <button type="button" class="min-w-11 min-h-11 rounded-[10px] border border-tpc05-edge bg-tpc05-chip text-tpc05-chipink text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:border-tpc05-acc hover:text-tpc05-acc focus-visible:outline-2 focus-visible:outline-tpc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none">M</button>
        <button type="button" class="min-w-11 min-h-11 rounded-[10px] border border-tpc05-edge bg-tpc05-chip text-tpc05-chipink text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:border-tpc05-acc hover:text-tpc05-acc focus-visible:outline-2 focus-visible:outline-tpc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none">L</button>
        <button type="button" class="min-w-11 min-h-11 rounded-[10px] border border-tpc05-edge bg-tpc05-chip text-tpc05-chipink text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:border-tpc05-acc hover:text-tpc05-acc focus-visible:outline-2 focus-visible:outline-tpc05-acc focus-visible:outline-offset-2 motion-reduce:transition-none">XL</button>
      </div>
      <button type="button" class="mt-3.5 w-full min-h-11 h-11 rounded-[11px] border-0 bg-tpc05-acc text-tpc05-onacc text-sm font-semibold cursor-pointer transition-colors duration-200 hover:bg-tpc05-acc2 focus-visible:outline-3 focus-visible:outline-tpc05-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc05-bg: #f2efe9;
  --color-tpc05-bg: oklch(0.95 0.008 85);
  --color-tpc05-ink: #2a2213;
  --color-tpc05-ink: oklch(0.27 0.03 80);
  --color-tpc05-mut: #6b6252;
  --color-tpc05-mut: oklch(0.48 0.02 80);
  --color-tpc05-ph: #ddd3c4;
  --color-tpc05-ph: oklch(0.87 0.02 80);
  --color-tpc05-ph2: #c9bca8;
  --color-tpc05-ph2: oklch(0.79 0.03 80);
  --color-tpc05-panel: #fffffff5;
  --color-tpc05-panel: oklch(1 0 0 / 0.96);
  --color-tpc05-chip: #ffffff;
  --color-tpc05-chip: oklch(1 0 0);
  --color-tpc05-chipink: #3a3020;
  --color-tpc05-chipink: oklch(0.32 0.03 80);
  --color-tpc05-edge: #d8cebd;
  --color-tpc05-edge: oklch(0.86 0.02 80);
  --color-tpc05-acc: #8a6a20;
  --color-tpc05-acc: oklch(0.5 0.11 80);
  --color-tpc05-acc2: #6f5518;
  --color-tpc05-acc2: oklch(0.43 0.1 80);
  --color-tpc05-onacc: #ffffff;
  --color-tpc05-onacc: oklch(1 0 0);
  --color-tpc05-ring: #d4b878;
  --color-tpc05-ring: oklch(0.8 0.08 85);
  --font-tpc05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --ease-tpc05: cubic-bezier(0.2, 0.7, 0.2, 1);
}

.tpc-05 {
  width: 100%;
  min-height: 100svh;
}

.tpc-05 ::selection {
  background: var(--color-tpc05-acc);
  color: #fff;
}
```
