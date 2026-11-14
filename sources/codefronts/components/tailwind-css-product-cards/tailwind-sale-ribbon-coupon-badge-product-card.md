---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-sale-ribbon-coupon-badge-product-card/"
title: "Tailwind Sale Ribbon &amp; Coupon Badge Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The clearance-page card: a diagonal ribbon wrapped across the top-right corner, a 'Best Seller' pill top-left, and a struck-through original beside the sale…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sale Ribbon &amp; Coupon Badge Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-sale-ribbon-coupon-badge-product-card/

The clearance-page card: a diagonal ribbon wrapped across the top-right corner, a 'Best Seller' pill top-left, and a struck-through original beside the sale price. Every piece is positioning and a rotation, so the whole ribbon is absolute -right-[42px] top-[18px] w-[170px] rotate-45 and the card's overflow-hidden does the clipping.
## HTML
```html
<section class="tpc-13 w-full min-h-svh grid place-items-center bg-tpc13-bg font-tpc13-sans px-5 py-12" aria-label="Sale ribbon product card demo">
  <article class="group relative w-[min(320px,100%)] rounded-2xl overflow-hidden bg-tpc13-card shadow-[0_16px_40px_-22px_oklch(0.25_0.03_260/0.45)]">
    <span aria-hidden="true" class="absolute top-[18px] -right-[42px] z-2 w-[170px] rotate-45 text-center py-1.75 bg-tpc13-sale text-tpc13-onacc text-[12px] font-extrabold tracking-[0.06em] shadow-[0_6px_14px_-6px_oklch(0.2_0.02_260/0.4)] transition-shadow duration-300 group-hover:shadow-[0_10px_22px_-6px_oklch(0.2_0.02_260/0.55)] motion-reduce:transition-none">SALE &minus;50%</span>
    <span class="absolute top-3.5 left-3.5 z-2 px-3 py-1.25 rounded-full bg-tpc13-ink text-tpc13-onacc text-[11px] font-bold tracking-[0.04em]">Best Seller</span>
    <div role="img" aria-label="Product photo: Halcyon bluetooth speaker" class="aspect-square bg-linear-[135deg,var(--color-tpc13-ph),var(--color-tpc13-ph2)] bg-[url('https://images.unsplash.com/photo-1589003077984-894e133dabab?w=700&h=700&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="px-5 pt-4.5 pb-5">
      <h3 class="text-[17px] font-semibold text-tpc13-ink text-pretty">Halcyon Bluetooth Speaker</h3>
      <p class="mt-2 text-[13px] text-tpc13-mut" aria-label="Rated 4.8 out of 5 from 2,140 reviews"><span aria-hidden="true" class="text-tpc13-star tracking-[0.05em]">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 4.8 (2,140)</p>
      <div class="mt-3 flex items-baseline gap-2.5">
        <span class="text-[15px] text-tpc13-was line-through tabular-nums">$120</span>
        <span class="text-[24px] font-extrabold text-tpc13-sale tabular-nums">$60</span>
        <span class="sr-only">50 percent off</span>
      </div>
      <p class="mt-3 inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border border-dashed border-tpc13-edge font-tpc13-mono text-[11px] font-bold tracking-[0.12em] text-tpc13-ghostink">CODE: SAVE20</p>
      <button type="button" class="mt-3.5 w-full min-h-11 h-11.5 rounded-xl border-0 cursor-pointer bg-tpc13-acc text-tpc13-onacc text-[15px] font-semibold transition-colors duration-150 hover:bg-tpc13-acc2 focus-visible:outline-3 focus-visible:outline-tpc13-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc13-bg: #f1f2f6;
  --color-tpc13-bg: oklch(0.95 0.005 265);
  --color-tpc13-card: #ffffff;
  --color-tpc13-card: oklch(1 0 0);
  --color-tpc13-ink: #111827;
  --color-tpc13-ink: oklch(0.23 0.03 265);
  --color-tpc13-mut: #5b6478;
  --color-tpc13-mut: oklch(0.5 0.025 265);
  --color-tpc13-ghostink: #3f4657;
  --color-tpc13-ghostink: oklch(0.42 0.025 265);
  --color-tpc13-was: #7d879a;
  --color-tpc13-was: oklch(0.62 0.02 265);
  --color-tpc13-edge: #c8cdd8;
  --color-tpc13-edge: oklch(0.84 0.012 265);
  --color-tpc13-ph: #e4e7ee;
  --color-tpc13-ph: oklch(0.92 0.008 265);
  --color-tpc13-ph2: #d3d8e4;
  --color-tpc13-ph2: oklch(0.87 0.014 265);
  --color-tpc13-sale: #c2341f;
  --color-tpc13-sale: oklch(0.55 0.18 28);
  --color-tpc13-acc: #3a55b0;
  --color-tpc13-acc: oklch(0.5 0.15 262);
  --color-tpc13-acc2: #2f4693;
  --color-tpc13-acc2: oklch(0.44 0.14 262);
  --color-tpc13-star: #d8a01f;
  --color-tpc13-star: oklch(0.75 0.14 82);
  --color-tpc13-ring: #a9b8e6;
  --color-tpc13-ring: oklch(0.78 0.08 262);
  --color-tpc13-onacc: #ffffff;
  --color-tpc13-onacc: oklch(1 0 0);
  --font-tpc13-sans: 'Archivo', system-ui, sans-serif;
  --font-tpc13-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tpc-13 {
  width: 100%;
  min-height: 100svh;
}

.tpc-13 ::selection {
  background: var(--color-tpc13-sale);
  color: #fff;
}
```
