---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-material-design-elevation-product-card/"
title: "Tailwind Material-Design Elevation Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The Material recipe, and the port makes its central idea explicit: elevation is a named scale, so the two shadow tiers become --shadow-tpc10-e2 and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Material-Design Elevation Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-material-design-elevation-product-card/

The Material recipe, and the port makes its central idea explicit: elevation is a named scale, so the two shadow tiers become --shadow-tpc10-e2 and --shadow-tpc10-e8 in @theme and the card reads shadow-tpc10-e2 group-hover:shadow-tpc10-e8. Key and ambient layers travel together as one token, exactly as the spec intends.
## HTML
```html
<section class="tpc-10 w-full min-h-svh grid place-items-center bg-tpc10-bg font-tpc10-sans px-5 py-14" aria-label="Material-design elevation product card demo">
  <article class="group w-80 max-w-full rounded-xl overflow-hidden bg-tpc10-card shadow-tpc10-e2 transition-[translate,box-shadow] duration-300 ease-tpc10 hover:-translate-y-1.5 hover:shadow-tpc10-e8 focus-within:-translate-y-1.5 focus-within:shadow-tpc10-e8 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <div role="img" aria-label="Product photo: Terra ceramic planter" class="aspect-[16/10] bg-linear-[135deg,var(--color-tpc10-ph),var(--color-tpc10-ph2)] bg-[url('https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=800&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="px-4.5 pt-4.5 pb-3.5">
      <span class="inline-block px-3 py-1 rounded-full text-[11px] font-bold tracking-[0.06em] uppercase text-tpc10-acc bg-[color-mix(in_oklch,var(--color-tpc10-acc)_14%,oklch(1_0_0))]">Home</span>
      <h3 class="mt-3 text-[19px] font-medium text-tpc10-ink text-pretty">Terra Ceramic Planter</h3>
      <p class="mt-1 text-[13px] text-tpc10-mut">Matte glaze &middot; 3 sizes</p>
      <div class="mt-3.5 flex items-center justify-between gap-3">
        <p class="text-[20px] font-bold text-tpc10-ink tabular-nums">$44</p>
        <button type="button" class="relative overflow-hidden min-h-11 h-11 px-4 rounded-lg border-0 bg-transparent text-tpc10-acc text-[13px] font-bold tracking-[0.06em] uppercase cursor-pointer before:absolute before:inset-0 before:bg-current before:opacity-0 before:transition-opacity before:duration-200 before:ease-tpc10 hover:before:opacity-10 focus-visible:before:opacity-10 focus-visible:outline-2 focus-visible:outline-tpc10-acc focus-visible:outline-offset-2 motion-reduce:before:transition-none">Add to Cart</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc10-bg: #eceff1;
  --color-tpc10-bg: oklch(0.94 0.005 220);
  --color-tpc10-card: #ffffff;
  --color-tpc10-card: oklch(1 0 0);
  --color-tpc10-ink: #1c2321;
  --color-tpc10-ink: oklch(0.25 0.012 165);
  --color-tpc10-mut: #5d6a65;
  --color-tpc10-mut: oklch(0.5 0.012 165);
  --color-tpc10-ph: #d7e3d9;
  --color-tpc10-ph: oklch(0.9 0.02 155);
  --color-tpc10-ph2: #c3d4c6;
  --color-tpc10-ph2: oklch(0.84 0.028 155);
  --color-tpc10-acc: #2e7d4f;
  --color-tpc10-acc: oklch(0.52 0.13 150);
  --font-tpc10-sans: 'Roboto', system-ui, sans-serif;
  --font-tpc10-mono: 'Roboto Mono', ui-monospace, monospace;
  /* The elevation scale as tokens: each tier is a key shadow plus an ambient
       shadow, and the pair is one design decision — so it is one utility. */
  --shadow-tpc10-e2: 0 2px 4px oklch(0 0 0 / 0.16), 0 8px 20px -8px oklch(0 0 0 / 0.22);
  --shadow-tpc10-e8: 0 8px 12px oklch(0 0 0 / 0.2), 0 24px 44px -12px oklch(0 0 0 / 0.32);
  --ease-tpc10: cubic-bezier(0.4, 0, 0.2, 1);
}

.tpc-10 {
  width: 100%;
  min-height: 100svh;
}

.tpc-10 ::selection {
  background: var(--color-tpc10-acc);
  color: #fff;
}
```
