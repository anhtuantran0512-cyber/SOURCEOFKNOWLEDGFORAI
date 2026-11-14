---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-dark-mode-gadget-product-card-glow/"
title: "Tailwind Dark-Mode Gadget Product Card with Accent Glow"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "A near-black card with a cool-grey edge and a cyan bloom that grows on hover — tuned so it reads on charcoal and on true-black OLED alike."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark-Mode Gadget Product Card with Accent Glow
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-dark-mode-gadget-product-card-glow/

A near-black card with a cool-grey edge and a cyan bloom that grows on hover — tuned so it reads on charcoal and on true-black OLED alike. Every coloured pixel derives from one --color-tpc08-acc token through color-mix() in arbitrary values, so retinting the card for gaming violet or crypto green is a one-line edit.
## HTML
```html
<section class="tpc-08 w-full min-h-svh grid place-items-center font-tpc08-sans px-5 py-14 bg-[radial-gradient(120%_120%_at_50%_20%,oklch(0.2_0.015_235),oklch(0.12_0.01_260))]" aria-label="Dark-mode gadget product card demo">
  <article class="group w-80 max-w-full rounded-[18px] overflow-hidden bg-linear-[180deg,var(--color-tpc08-card),var(--color-tpc08-card2)] border border-tpc08-edge shadow-[0_30px_60px_-34px_oklch(0_0_0/0.9)] transition-[translate,box-shadow,border-color] duration-350 hover:-translate-y-1 hover:border-[color-mix(in_oklch,var(--color-tpc08-acc)_45%,var(--color-tpc08-edge))] hover:shadow-[0_34px_70px_-34px_oklch(0_0_0/0.9),0_0_40px_-12px_color-mix(in_oklch,var(--color-tpc08-acc)_60%,transparent)] focus-within:-translate-y-1 focus-within:border-[color-mix(in_oklch,var(--color-tpc08-acc)_45%,var(--color-tpc08-edge))] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
    <div class="relative aspect-[16/11]">
      <div role="img" aria-label="Product photo: Vantage Pro wireless mouse" class="absolute inset-0 bg-linear-[135deg,var(--color-tpc08-ph),var(--color-tpc08-ph2)] bg-[url('https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&h=550&fit=crop&q=70')] bg-cover bg-center"></div>
      <span class="absolute top-3 left-3 px-3 py-[5px] rounded-full font-tpc08-mono text-[10px] tracking-[0.14em] uppercase text-tpc08-acc bg-[color-mix(in_oklch,var(--color-tpc08-acc)_14%,var(--color-tpc08-card2))] border border-[color-mix(in_oklch,var(--color-tpc08-acc)_40%,transparent)] shadow-[0_0_16px_-4px_var(--color-tpc08-acc)]">In stock</span>
    </div>
    <div class="px-5.5 pt-5 pb-5.5">
      <p class="font-tpc08-mono text-[11px] tracking-[0.2em] uppercase text-tpc08-mut">Vantage</p>
      <h3 class="mt-1.5 text-[18px] font-semibold leading-[1.3] text-tpc08-ink text-pretty">Vantage Pro Wireless Mouse</h3>
      <p class="mt-2 text-[13px] text-tpc08-mut2 tabular-nums">26K DPI &middot; 74g &middot; 90h battery</p>
      <div class="mt-4.5 flex items-center justify-between gap-3">
        <p class="text-[22px] font-extrabold text-tpc08-hi tabular-nums [text-shadow:0_0_18px_color-mix(in_oklch,var(--color-tpc08-acc)_45%,transparent)]">$99</p>
        <button type="button" class="min-h-11 h-11 px-5.5 rounded-xl border-0 bg-tpc08-acc text-tpc08-onacc text-sm font-bold cursor-pointer shadow-[0_0_22px_-6px_var(--color-tpc08-acc)] transition-[filter,scale] duration-200 hover:brightness-110 active:scale-97 focus-visible:outline-3 focus-visible:outline-[color-mix(in_oklch,var(--color-tpc08-acc)_55%,oklch(0_0_0))] focus-visible:outline-offset-2 motion-reduce:transition-none">Add to Cart</button>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc08-card: #12161b;
  --color-tpc08-card: oklch(0.19 0.012 235);
  --color-tpc08-card2: #0c0f13;
  --color-tpc08-card2: oklch(0.15 0.01 235);
  --color-tpc08-edge: #1e252c;
  --color-tpc08-edge: oklch(0.25 0.012 235);
  --color-tpc08-ph: #1a2027;
  --color-tpc08-ph: oklch(0.23 0.013 235);
  --color-tpc08-ph2: #11161b;
  --color-tpc08-ph2: oklch(0.18 0.012 235);
  --color-tpc08-ink: #eef4f8;
  --color-tpc08-ink: oklch(0.95 0.008 235);
  --color-tpc08-hi: #ffffff;
  --color-tpc08-hi: oklch(1 0 0);
  --color-tpc08-mut: #8fa0ab;
  --color-tpc08-mut: oklch(0.7 0.018 235);
  --color-tpc08-mut2: #a3b3c0;
  --color-tpc08-mut2: oklch(0.76 0.02 235);
  --color-tpc08-acc: #6fd8ee;
  --color-tpc08-acc: oklch(0.82 0.16 195);
  --color-tpc08-onacc: #04141a;
  --color-tpc08-onacc: oklch(0.16 0.02 220);
  --font-tpc08-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tpc08-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tpc-08 {
  width: 100%;
  min-height: 100svh;
}

.tpc-08 ::selection {
  background: var(--color-tpc08-acc);
  color: var(--color-tpc08-onacc);
}
```
