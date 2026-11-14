---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-equal-height-product-grid/"
title: "Tailwind Equal-Height Product Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "The alignment problem every catalogue has &mdash; titles of different lengths pushing the Add-to-Cart buttons out of line &mdash; solved in four utilities:…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Equal-Height Product Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-equal-height-product-grid/

The alignment problem every catalogue has &mdash; titles of different lengths pushing the Add-to-Cart buttons out of line &mdash; solved in four utilities: items-stretch on the grid, h-full flex flex-col on the card, and mt-auto on the price row. The port's value here is that the contract is now visible on the elements that make it.
## HTML
```html
<section class="tcg-03 w-full min-h-svh bg-tcg03-bg font-tcg03-sans text-tcg03-ink px-6 py-12" aria-label="Equal-height product card grid demo">
  <div class="max-w-[980px] mx-auto grid [grid-template-columns:repeat(auto-fill,minmax(220px,1fr))] items-stretch gap-6">

    <article class="h-full flex flex-col p-5 rounded-[14px] border border-tcg03-line bg-tcg03-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_30px_-18px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[4/3] mb-3.5 rounded-[10px] bg-linear-[135deg,#fde68a,#f59e0b]" aria-hidden="true"></div>
      <h3 class="text-[.98rem] font-bold leading-[1.35] mb-1.5">Ceramic Pour-Over Set</h3>
      <p class="text-[.82rem] leading-[1.5] text-tcg03-muted text-pretty">Hand-glazed dripper and carafe.</p>
      <div class="mt-auto pt-4 flex items-center justify-between gap-2.5">
        <span class="text-[1.05rem] font-extrabold tabular-nums">$48</span>
        <button type="button" class="min-h-11 px-3.5 rounded-lg border-0 bg-tcg03-ink text-white font-tcg03-sans text-[.78rem] font-bold cursor-pointer transition-[background] duration-200 hover:bg-tcg03-inkdeep focus-visible:outline-2 focus-visible:outline-tcg03-accent focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </article>

    <article class="h-full flex flex-col p-5 rounded-[14px] border border-tcg03-line bg-tcg03-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_30px_-18px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[4/3] mb-3.5 rounded-[10px] bg-linear-[135deg,#a7f3d0,#10b981]" aria-hidden="true"></div>
      <h3 class="text-[.98rem] font-bold leading-[1.35] mb-1.5">Walnut Cutting Board With Reversible Edge and Juice Groove</h3>
      <p class="text-[.82rem] leading-[1.5] text-tcg03-muted text-pretty">FSC-certified solid walnut, oiled and ready for daily use in any kitchen.</p>
      <div class="mt-auto pt-4 flex items-center justify-between gap-2.5">
        <span class="text-[1.05rem] font-extrabold tabular-nums">$72</span>
        <button type="button" class="min-h-11 px-3.5 rounded-lg border-0 bg-tcg03-ink text-white font-tcg03-sans text-[.78rem] font-bold cursor-pointer transition-[background] duration-200 hover:bg-tcg03-inkdeep focus-visible:outline-2 focus-visible:outline-tcg03-accent focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </article>

    <article class="h-full flex flex-col p-5 rounded-[14px] border border-tcg03-line bg-tcg03-card transition-[translate,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_30px_-18px_oklch(0.3_0.02_260/0.25)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[4/3] mb-3.5 rounded-[10px] bg-linear-[135deg,#bfdbfe,#3b82f6]" aria-hidden="true"></div>
      <h3 class="text-[.98rem] font-bold leading-[1.35] mb-1.5">Linen Napkin Set</h3>
      <p class="text-[.82rem] leading-[1.5] text-tcg03-muted text-pretty">Set of four, stonewashed for softness.</p>
      <div class="mt-auto pt-4 flex items-center justify-between gap-2.5">
        <span class="text-[1.05rem] font-extrabold tabular-nums">$34</span>
        <button type="button" class="min-h-11 px-3.5 rounded-lg border-0 bg-tcg03-ink text-white font-tcg03-sans text-[.78rem] font-bold cursor-pointer transition-[background] duration-200 hover:bg-tcg03-inkdeep focus-visible:outline-2 focus-visible:outline-tcg03-accent focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg03-bg: #f8f7f4;
  --color-tcg03-bg: oklch(0.97 0.005 90);
  --color-tcg03-card: #ffffff;
  --color-tcg03-card: oklch(1 0 0);
  --color-tcg03-ink: #1f2937;
  --color-tcg03-ink: oklch(0.29 0.03 260);
  --color-tcg03-inkdeep: #111827;
  --color-tcg03-inkdeep: oklch(0.21 0.03 265);
  --color-tcg03-muted: #6b7280;
  --color-tcg03-muted: oklch(0.55 0.02 260);
  --color-tcg03-line: #e7e4dd;
  --color-tcg03-line: oklch(0.91 0.008 90);
  --color-tcg03-accent: #f59e0b;
  --color-tcg03-accent: oklch(0.77 0.16 70);
  --font-tcg03-sans: 'Space Grotesk', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract. */

.tcg-03 {
  width: 100%;
  min-height: 100svh;
}

.tcg-03 ::selection {
  background: #f59e0b;
  color: #1a1a1a;
}
```
