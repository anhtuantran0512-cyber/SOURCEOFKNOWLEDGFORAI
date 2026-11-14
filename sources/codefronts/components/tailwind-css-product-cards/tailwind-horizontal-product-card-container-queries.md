---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-horizontal-product-card-container-queries/"
title: "Tailwind Horizontal Product Card with Container Queries"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The cart-row card that responds to its own width instead of the viewport's — and in v4 that is a first-class variant, not a raw @container block."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Horizontal Product Card with Container Queries
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-horizontal-product-card-container-queries/

The cart-row card that responds to its own width instead of the viewport's — and in v4 that is a first-class variant, not a raw @container block. @container/card on the wrapper plus @max-\[420px\]/card:flex-col on the card is the entire responsive story, so the same component works in a wide cart column and a narrow sidebar.
## HTML
```html
<section class="tpc-11 w-full min-h-svh grid place-items-center bg-tpc11-bg font-tpc11-sans px-5 py-12" aria-label="Horizontal container-query product card demo">
  <div class="@container/card w-[min(520px,100%)]">
    <article class="flex rounded-2xl overflow-hidden bg-tpc11-card shadow-[0_14px_36px_-20px_oklch(0.25_0.03_260/0.4)] @max-[420px]/card:flex-col">
      <div role="img" aria-label="Product photo: Ridge insulated bottle" class="flex-[0_0_40%] aspect-square bg-linear-[135deg,var(--color-tpc11-ph),var(--color-tpc11-ph2)] bg-[url('https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=700&h=700&fit=crop&q=70')] bg-cover bg-center @max-[420px]/card:flex-none @max-[420px]/card:w-full @max-[420px]/card:aspect-[16/9]"></div>
      <div class="flex-1 flex flex-col justify-between gap-4.5 px-5.5 py-5">
        <div>
          <h3 class="text-[17px] font-semibold leading-[1.35] text-tpc11-ink text-pretty">Ridge Insulated Bottle &middot; 750ml</h3>
          <p class="mt-1 text-[13px] text-tpc11-mut">Slate &middot; Keeps cold 24h</p>
        </div>
        <div class="flex flex-wrap items-center justify-between gap-3">
          <p class="text-[20px] font-extrabold text-tpc11-ink tabular-nums">$35</p>
          <div class="flex gap-2">
            <button type="button" class="min-h-11 h-11 px-4 rounded-[10px] border border-tpc11-edge bg-tpc11-card text-tpc11-ghostink text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:border-tpc11-acc hover:text-tpc11-acc focus-visible:outline-3 focus-visible:outline-[color-mix(in_oklch,var(--color-tpc11-acc)_45%,oklch(1_0_0))] focus-visible:outline-offset-2 motion-reduce:transition-none">Save</button>
            <button type="button" class="min-h-11 h-11 px-4.5 rounded-[10px] border-0 bg-tpc11-acc text-tpc11-onacc text-[13px] font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc11-acc2 focus-visible:outline-3 focus-visible:outline-[color-mix(in_oklch,var(--color-tpc11-acc)_45%,oklch(1_0_0))] focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc11-bg: #eef1f5;
  --color-tpc11-bg: oklch(0.95 0.008 250);
  --color-tpc11-card: #ffffff;
  --color-tpc11-card: oklch(1 0 0);
  --color-tpc11-ink: #101828;
  --color-tpc11-ink: oklch(0.23 0.03 260);
  --color-tpc11-mut: #5b6678;
  --color-tpc11-mut: oklch(0.5 0.025 260);
  --color-tpc11-ghostink: #344054;
  --color-tpc11-ghostink: oklch(0.4 0.03 260);
  --color-tpc11-edge: #d0d5dd;
  --color-tpc11-edge: oklch(0.86 0.012 260);
  --color-tpc11-ph: #dbe3ee;
  --color-tpc11-ph: oklch(0.9 0.02 250);
  --color-tpc11-ph2: #c9d5e6;
  --color-tpc11-ph2: oklch(0.85 0.03 250);
  --color-tpc11-acc: #2f5fbf;
  --color-tpc11-acc: oklch(0.52 0.14 260);
  --color-tpc11-acc2: #26509f;
  --color-tpc11-acc2: oklch(0.45 0.13 260);
  --color-tpc11-onacc: #ffffff;
  --color-tpc11-onacc: oklch(1 0 0);
  --font-tpc11-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tpc-11 {
  width: 100%;
  min-height: 100svh;
}

.tpc-11 ::selection {
  background: var(--color-tpc11-acc);
  color: #fff;
}
```
