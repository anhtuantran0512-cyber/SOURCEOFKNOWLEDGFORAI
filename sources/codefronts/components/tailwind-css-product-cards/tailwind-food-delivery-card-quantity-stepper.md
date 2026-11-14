---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-food-delivery-card-quantity-stepper/"
title: "Tailwind Food Delivery Card with Quantity Stepper"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The delivery-app dish card: dietary pills, a rating and prep-time line, and a &plus;/&minus; stepper driving a live running total."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Food Delivery Card with Quantity Stepper
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-food-delivery-card-quantity-stepper/

The delivery-app dish card: dietary pills, a rating and prep-time line, and a &plus;/&minus; stepper driving a live running total. CSS owns all of it except two numbers — the script writes the count and the total, sets [disabled] so disabled: can style it, and announces the change in an aria-live region.
## HTML
```html
<section class="tpc-16 w-full min-h-svh grid place-items-center bg-tpc16-bg font-tpc16-sans px-5 py-12" data-price="12.5" aria-label="Food delivery dish card with quantity stepper demo">
  <article class="w-[min(360px,100%)] rounded-[18px] overflow-hidden bg-tpc16-card shadow-[0_16px_40px_-22px_oklch(0.3_0.04_60/0.4)]">
    <div role="img" aria-label="Dish photo: Smoky bean chilli bowl" class="aspect-[16/10] bg-linear-[135deg,var(--color-tpc16-ph),var(--color-tpc16-ph2)] bg-[url('https://images.unsplash.com/photo-1547592166-23ac45744acd?w=800&h=500&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="px-5 pt-4.5 pb-5">
      <div class="flex items-start justify-between gap-3">
        <h3 class="text-[18px] font-bold text-tpc16-ink text-pretty">Smoky Bean Chilli Bowl</h3>
        <div class="flex gap-1.5 shrink-0">
          <span class="px-2.25 py-1 rounded-full bg-tpc16-veg text-tpc16-vegink text-[10px] font-bold tracking-[0.04em] uppercase">Vegan</span>
          <span class="px-2.25 py-1 rounded-full bg-tpc16-gf text-tpc16-gfink text-[10px] font-bold tracking-[0.04em] uppercase">GF</span>
        </div>
      </div>
      <p class="mt-2.5 text-[13.5px] leading-[1.5] text-tpc16-mut">Slow-cooked black beans, fire-roasted peppers, lime crema.</p>
      <p class="mt-2.5 text-[13px] text-tpc16-mut2"><span aria-hidden="true" class="text-tpc16-star">&#9733;</span> 4.7 &middot; 20&ndash;30 min &middot; $2.99 delivery</p>
      <div class="mt-4.5 flex items-center justify-between gap-3">
        <div role="group" aria-label="Quantity" class="inline-flex items-center border border-tpc16-edge rounded-xl overflow-hidden">
          <button type="button" data-dec aria-label="Decrease quantity" class="grid place-items-center min-w-11 min-h-11 border-0 cursor-pointer bg-tpc16-step text-tpc16-ink text-[20px] font-semibold leading-none transition-colors duration-150 hover:bg-tpc16-step2 disabled:opacity-35 disabled:cursor-not-allowed focus-visible:outline-2 focus-visible:outline-tpc16-acc focus-visible:-outline-offset-2 motion-reduce:transition-none">&minus;</button>
          <span data-qty class="min-w-9 text-center text-[15px] font-bold text-tpc16-ink tabular-nums">1</span>
          <button type="button" data-inc aria-label="Increase quantity" class="grid place-items-center min-w-11 min-h-11 border-0 cursor-pointer bg-tpc16-step text-tpc16-ink text-[20px] font-semibold leading-none transition-colors duration-150 hover:bg-tpc16-step2 disabled:opacity-35 disabled:cursor-not-allowed focus-visible:outline-2 focus-visible:outline-tpc16-acc focus-visible:-outline-offset-2 motion-reduce:transition-none">&plus;</button>
        </div>
        <button type="button" data-add aria-live="polite" class="flex-1 min-h-11 h-11.5 rounded-xl border-0 cursor-pointer bg-tpc16-acc text-tpc16-onacc text-[14px] font-bold tabular-nums transition-[filter] duration-150 hover:brightness-108 focus-visible:outline-3 focus-visible:outline-tpc16-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Add &middot; $12.50</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc16-bg: #f6f3ee;
  --color-tpc16-bg: oklch(0.96 0.008 75);
  --color-tpc16-card: #ffffff;
  --color-tpc16-card: oklch(1 0 0);
  --color-tpc16-ink: #2a1e12;
  --color-tpc16-ink: oklch(0.26 0.025 60);
  --color-tpc16-mut: #5f5344;
  --color-tpc16-mut: oklch(0.46 0.02 65);
  --color-tpc16-mut2: #6d6152;
  --color-tpc16-mut2: oklch(0.51 0.02 68);
  --color-tpc16-edge: #e4dccf;
  --color-tpc16-edge: oklch(0.9 0.015 80);
  --color-tpc16-step: #faf7f2;
  --color-tpc16-step: oklch(0.98 0.006 80);
  --color-tpc16-step2: #f0e8db;
  --color-tpc16-step2: oklch(0.94 0.014 80);
  --color-tpc16-ph: #f0e4d4;
  --color-tpc16-ph: oklch(0.93 0.02 75);
  --color-tpc16-ph2: #e6d2b8;
  --color-tpc16-ph2: oklch(0.88 0.035 78);
  --color-tpc16-veg: #dcf2e0;
  --color-tpc16-veg: oklch(0.93 0.06 150);
  --color-tpc16-vegink: #1f6b3b;
  --color-tpc16-vegink: oklch(0.42 0.12 150);
  --color-tpc16-gf: #dde9f8;
  --color-tpc16-gf: oklch(0.93 0.05 250);
  --color-tpc16-gfink: #1f548f;
  --color-tpc16-gfink: oklch(0.44 0.12 255);
  --color-tpc16-star: #c78a12;
  --color-tpc16-star: oklch(0.68 0.14 75);
  --color-tpc16-acc: #d4601f;
  --color-tpc16-acc: oklch(0.6 0.17 45);
  --color-tpc16-ring: #f0b48c;
  --color-tpc16-ring: oklch(0.82 0.09 45);
  --color-tpc16-onacc: #ffffff;
  --color-tpc16-onacc: oklch(1 0 0);
  --font-tpc16-sans: 'Outfit', system-ui, sans-serif;
}

.tpc-16 {
  width: 100%;
  min-height: 100svh;
}

.tpc-16 ::selection {
  background: var(--color-tpc16-acc);
  color: #fff;
}
```

## JavaScript
```js
document.querySelectorAll('.tpc-16').forEach(function (root) {
  if (root.dataset.bound) return;
  root.dataset.bound = '1';

  var unit = parseFloat(root.dataset.price) || 0;
  var qtyEl = root.querySelector('[data-qty]');
  var addEl = root.querySelector('[data-add]');
  var inc = root.querySelector('[data-inc]');
  var dec = root.querySelector('[data-dec]');
  if (!qtyEl || !addEl || !inc || !dec) return;

  var qty = 1;
  var MAX = 20;

  function render() {
    qtyEl.textContent = qty;
    addEl.textContent = 'Add \u00b7 $' + (unit * qty).toFixed(2);
    dec.disabled = qty <= 1;      // JS sets the attribute; disabled: styles it
    inc.disabled = qty >= MAX;
  }

  inc.addEventListener('click', function () { if (qty < MAX) { qty++; render(); } });
  dec.addEventListener('click', function () { if (qty > 1) { qty--; render(); } });
  render();
});
```
