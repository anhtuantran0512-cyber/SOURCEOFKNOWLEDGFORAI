---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-product-card-hover-reveal-add-to-cart/"
title: "Tailwind Product Card with Hover-Reveal Add to Cart"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The most-searched hover pattern in Tier-1 e-commerce, ported to variants: the card stays calm and type-led at rest, and the 'Add to Cart' button rises into…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Product Card with Hover-Reveal Add to Cart
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-product-card-hover-reveal-add-to-cart/

The most-searched hover pattern in Tier-1 e-commerce, ported to variants: the card stays calm and type-led at rest, and the 'Add to Cart' button rises into place on hover — or on group-focus-within:, which is the part most implementations forget. One group on the card drives the CTA, the shadow lift and a slow media zoom, so all three read off the same state.
## HTML
```html
<section class="tpc-01 w-full min-h-svh grid place-items-center bg-tpc01-bg font-tpc01-sans px-5 py-12" aria-label="Hover-reveal add to cart product card demo">
  <article class="group w-75 max-w-full rounded-[18px] overflow-hidden bg-tpc01-card shadow-[0_1px_2px_oklch(0.25_0.03_260/0.06),0_12px_32px_-18px_oklch(0.25_0.03_260/0.28)] transition-shadow duration-300 hover:shadow-[0_1px_2px_oklch(0.25_0.03_260/0.06),0_26px_50px_-22px_oklch(0.25_0.03_260/0.4)] focus-within:shadow-[0_1px_2px_oklch(0.25_0.03_260/0.06),0_26px_50px_-22px_oklch(0.25_0.03_260/0.4)]">
    <div class="aspect-square overflow-hidden bg-linear-[135deg,var(--color-tpc01-ph),var(--color-tpc01-ph2)]">
      <div role="img" aria-label="Product photo: Aurora wireless headphones" class="w-full h-full bg-[url('https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=700&h=700&fit=crop&q=70')] bg-cover bg-center transition-transform duration-700 ease-tpc01 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
    </div>
    <div class="flex flex-col gap-1 px-5 pt-5 pb-5.5">
      <p class="font-tpc01-mono text-[11px] tracking-[0.18em] uppercase text-tpc01-dim">SoundField</p>
      <h3 class="text-[17px] font-semibold leading-[1.3] text-tpc01-ink text-pretty">Aurora Wireless Headphones</h3>
      <p class="mt-0.5 text-[18px] font-bold text-tpc01-ink tabular-nums">$149.00</p>
      <button type="button" class="mt-3.5 min-h-11 h-11.5 rounded-xl border-0 bg-tpc01-acc text-tpc01-onacc text-[15px] font-semibold tracking-[0.01em] cursor-pointer opacity-0 translate-y-3.5 transition-[opacity,translate,background-color] duration-300 ease-tpc01 group-hover:opacity-100 group-hover:translate-y-0 group-focus-within:opacity-100 group-focus-within:translate-y-0 hover:bg-tpc01-acc2 focus-visible:outline-3 focus-visible:outline-tpc01-ring focus-visible:outline-offset-2 motion-reduce:opacity-100 motion-reduce:translate-y-0 motion-reduce:transition-none">Add to Cart</button>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc01-bg: #f4f5f7;
  --color-tpc01-bg: oklch(0.97 0.004 265);
  --color-tpc01-card: #ffffff;
  --color-tpc01-card: oklch(1 0 0);
  --color-tpc01-ink: #101828;
  --color-tpc01-ink: oklch(0.23 0.03 265);
  --color-tpc01-dim: #98a2b3;
  --color-tpc01-dim: oklch(0.7 0.02 265);
  --color-tpc01-ph: #e9edf3;
  --color-tpc01-ph: oklch(0.93 0.01 265);
  --color-tpc01-ph2: #dfe4ec;
  --color-tpc01-ph2: oklch(0.9 0.015 265);
  --color-tpc01-acc: #3a5ccc;
  --color-tpc01-acc: oklch(0.55 0.16 265);
  --color-tpc01-acc2: #2f4cab;
  --color-tpc01-acc2: oklch(0.48 0.15 265);
  --color-tpc01-onacc: #ffffff;
  --color-tpc01-onacc: oklch(1 0 0);
  --color-tpc01-ring: #9db0ea;
  --color-tpc01-ring: oklch(0.75 0.09 265);
  --font-tpc01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpc01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-tpc01: cubic-bezier(0.2, 0.7, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tpc-01 {
  width: 100%;
  min-height: 100svh;
}
/* The one rule with no variant form: a scoped ::selection. */

.tpc-01 ::selection {
  background: var(--color-tpc01-acc);
  color: #fff;
}
```
