---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-minimalist-ecommerce-product-card/"
title: "Tailwind Minimalist eCommerce Product Card"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "Restraint as the technique: no border, no shadow at rest, a Cormorant display name over a Jost micro-label, and a text CTA whose underline draws itself in…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist eCommerce Product Card
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-minimalist-ecommerce-product-card/

Restraint as the technique: no border, no shadow at rest, a Cormorant display name over a Jost micro-label, and a text CTA whose underline draws itself in from the left. The whole card is whitespace and type — and the one piece Tailwind has no utility for, the animated background-size underline, is a single arbitrary background value.
## HTML
```html
<section class="tpc-06 w-full min-h-svh grid place-items-center bg-tpc06-bg font-tpc06-sans px-5 py-14" aria-label="Minimalist eCommerce product card demo">
  <article class="group w-80 max-w-full p-5 rounded-md bg-transparent transition-[background-color,box-shadow] duration-400 hover:bg-tpc06-card hover:shadow-[0_24px_60px_-34px_oklch(0.2_0.01_80/0.28)] focus-within:bg-tpc06-card focus-within:shadow-[0_24px_60px_-34px_oklch(0.2_0.01_80/0.28)] motion-reduce:transition-none">
    <div role="img" aria-label="Product photo: fine gold hoop earrings" class="aspect-[4/5] bg-linear-[160deg,var(--color-tpc06-ph),var(--color-tpc06-ph2)] bg-[url('https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=700&h=880&fit=crop&q=70')] bg-cover bg-center"></div>
    <div class="pt-5.5 px-1 pb-1.5 text-center">
      <h3 class="font-tpc06-display text-[22px] font-normal tracking-[0.02em] text-tpc06-ink">Fine Gold Hoops</h3>
      <p class="mt-2 text-[13px] font-light tracking-[0.12em] text-tpc06-mut tabular-nums">$320</p>
      <a href="#fine-gold-hoops" class="inline-block mt-4.5 py-2 text-[11px] font-medium tracking-[0.22em] uppercase no-underline text-tpc06-ink bg-[linear-gradient(currentColor,currentColor)] bg-[position:0_100%] bg-[length:0_1px] bg-no-repeat transition-[background-size] duration-400 ease-out hover:bg-[length:100%_1px] focus-visible:bg-[length:100%_1px] focus-visible:outline-1 focus-visible:outline-dashed focus-visible:outline-tpc06-ink focus-visible:outline-offset-6 motion-reduce:transition-none">View product</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc06-bg: #faf9f6;
  --color-tpc06-bg: oklch(0.98 0.005 85);
  --color-tpc06-card: #ffffff;
  --color-tpc06-card: oklch(1 0 0);
  --color-tpc06-ink: #1a1a1a;
  --color-tpc06-ink: oklch(0.22 0.002 85);
  --color-tpc06-mut: #6e685e;
  --color-tpc06-mut: oklch(0.5 0.012 85);
  --color-tpc06-ph: #f0ece4;
  --color-tpc06-ph: oklch(0.94 0.01 85);
  --color-tpc06-ph2: #e6ded1;
  --color-tpc06-ph2: oklch(0.9 0.015 85);
  --font-tpc06-display: 'Cormorant Garamond', Georgia, serif;
  --font-tpc06-sans: 'Jost', system-ui, sans-serif;
}

.tpc-06 {
  width: 100%;
  min-height: 100svh;
}

.tpc-06 ::selection {
  background: var(--color-tpc06-ink);
  color: #fff;
}
```
