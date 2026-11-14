---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-auto-fit-product-catalog-grid/"
title: "Tailwind Auto-Fit Product Catalog Grid"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "Not one card but the container: a catalog that fits as many ≥200px columns as the space allows, with zero breakpoints."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Auto-Fit Product Catalog Grid
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-auto-fit-product-catalog-grid/

Not one card but the container: a catalog that fits as many ≥200px columns as the space allows, with zero breakpoints. Tailwind's grid-cols-* scale is integers, so the whole pattern is one honest arbitrary value — grid-cols-[repeat(auto-fit,minmax(200px,1fr))] — and the six cells are a tiny compact card repeated.
## HTML
```html
<section class="tpc-12 w-full min-h-svh grid place-items-center bg-tpc12-bg font-tpc12-sans px-5 py-12" aria-label="Auto-fit product catalog grid demo">
  <div class="w-[min(920px,100%)] grid gap-5 content-start grid-cols-[repeat(auto-fit,minmax(200px,1fr))]">
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: canvas sneaker" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Canvas Sneaker</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$68</span>
        <button type="button" aria-label="Add Canvas Sneaker to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: merino crew sweatshirt" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Merino Crew</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$24</span>
        <button type="button" aria-label="Add Wool Beanie to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: denim jacket" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1543076447-215ad9ba6923?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Denim Jacket</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$96</span>
        <button type="button" aria-label="Add Denim Jacket to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: linen shirt" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Linen Shirt</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$54</span>
        <button type="button" aria-label="Add Linen Shirt to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: trail cap" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Trail Cap</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$29</span>
        <button type="button" aria-label="Add Trail Cap to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
    <article class="group rounded-[14px] overflow-hidden pb-3.5 bg-tpc12-card shadow-[0_10px_26px_-18px_oklch(0.25_0.03_50/0.4)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_20px_40px_-20px_oklch(0.25_0.03_50/0.45)] focus-within:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div role="img" aria-label="Product photo: suede loafer" class="aspect-square bg-linear-[135deg,var(--color-tpc12-ph),var(--color-tpc12-ph2)] bg-[url('https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=500&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
      <h3 class="px-3.5 pt-3.5 text-[15px] font-semibold text-tpc12-ink">Suede Loafer</h3>
      <div class="flex items-center justify-between gap-2 px-3.5 pt-2">
        <span class="text-base font-extrabold text-tpc12-acc tabular-nums">$120</span>
        <button type="button" aria-label="Add Suede Loafer to cart" class="grid place-items-center min-w-11 min-h-11 rounded-[10px] border-0 bg-tpc12-acc text-tpc12-onacc text-[22px] leading-none font-semibold cursor-pointer transition-colors duration-150 hover:bg-tpc12-acc2 focus-visible:outline-3 focus-visible:outline-tpc12-ring focus-visible:outline-offset-2 motion-reduce:transition-none">+</button>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc12-bg: #f5f4f2;
  --color-tpc12-bg: oklch(0.96 0.004 70);
  --color-tpc12-card: #ffffff;
  --color-tpc12-card: oklch(1 0 0);
  --color-tpc12-ink: #2a2118;
  --color-tpc12-ink: oklch(0.27 0.02 60);
  --color-tpc12-ph: #ece7e2;
  --color-tpc12-ph: oklch(0.93 0.01 60);
  --color-tpc12-ph2: #ddd4cb;
  --color-tpc12-ph2: oklch(0.87 0.018 60);
  --color-tpc12-acc: #b23a26;
  --color-tpc12-acc: oklch(0.52 0.16 30);
  --color-tpc12-acc2: #94301f;
  --color-tpc12-acc2: oklch(0.45 0.15 30);
  --color-tpc12-onacc: #ffffff;
  --color-tpc12-onacc: oklch(1 0 0);
  --color-tpc12-ring: #e8a898;
  --color-tpc12-ring: oklch(0.78 0.09 30);
  --font-tpc12-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tpc-12 {
  width: 100%;
  min-height: 100svh;
}

.tpc-12 ::selection {
  background: var(--color-tpc12-acc);
  color: #fff;
}
```
