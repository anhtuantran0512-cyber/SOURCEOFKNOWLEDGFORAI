---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-ecommerce-product-card/"
title: "Tailwind Minimalist Product Card for Ecommerce"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A three-up storefront row where the product does the talking: a 4:5 image area, maker, name in a serif, one spec line, price and a single outlined action."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Product Card for Ecommerce
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-ecommerce-product-card/

A three-up storefront row where the product does the talking: a 4:5 image area, maker, name in a serif, one spec line, price and a single outlined action. Hover or keyboard focus lifts the card 3px and eases the image to 103% &mdash; both via group-hover: and group-focus-within:, so keyboard shoppers get the same feedback as mouse users.
## HTML
```html
<section class="tmu-16 relative w-full min-h-svh bg-tmu16-bg font-tmu16-ui text-tmu16-ink antialiased" aria-labelledby="tmu16-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu16-theme" type="checkbox" class="peer sr-only">
    <label for="tmu16-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu16-line bg-tmu16-surface text-tmu16-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu16-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu16-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[72rem] gap-12 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu16-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu16-ink-2"><span class="tabular-nums text-tmu16-acc">16</span><span aria-hidden="true" class="h-px w-6 bg-tmu16-line"></span>Product card</p>
      <h2 id="tmu16-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">Let the product do the talking</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu16-ink-2 text-pretty">Image, maker, name, one spec, price, one action. Hover and keyboard focus get the same lift.</p>
    </header>
    <ul class="grid gap-x-6 gap-y-8 grid-cols-[repeat(auto-fit,minmax(min(100%,15rem),1fr))]">
      <li class="min-w-0">
        <article aria-labelledby="tmu16-p1" class="group grid min-w-0 gap-4 overflow-hidden rounded-lg bg-tmu16-surface shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition-[translate,box-shadow] duration-200 hover:-translate-y-[3px] hover:shadow-[0_18px_40px_-24px_rgb(40_30_20/0.35)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
          <div class="relative aspect-[4/5] min-w-0 overflow-hidden bg-tmu16-media">
            <div role="img" aria-label="Product photograph area, 4 by 5 &mdash; stoneware carafe" class="grid size-full place-items-center transition-[scale] duration-300 group-hover:scale-[1.03] group-focus-within:scale-[1.03] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
              <span class="text-[0.6875rem] uppercase tracking-[0.14em] text-tmu16-ink-2">4:5 image area</span>
            </div>
            <button type="button" aria-label="Save Unglazed stoneware carafe to wishlist" aria-pressed="false" class="absolute top-3 right-3 grid size-11 place-items-center rounded-full bg-tmu16-surface/90 text-tmu16-ink-2 cursor-pointer backdrop-blur-sm transition-colors duration-150 hover:text-tmu16-acc aria-pressed:text-tmu16-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button>
          </div>
          <div class="grid min-w-0 gap-1.5 px-[1.125rem] pb-5">
            <p class="text-[0.6875rem] font-medium uppercase tracking-[0.14em] text-tmu16-ink-2">Nova Studio</p>
            <h3 id="tmu16-p1" class="font-tmu16-serif text-lg/[1.25] font-medium tracking-[-0.012em] text-pretty">Unglazed stoneware carafe</h3>
            <p class="text-[0.8125rem] text-tmu16-ink-2">1.2 L &middot; matte body, polished lip</p>
            <p class="mt-1 font-tmu16-serif text-[1.3125rem] font-semibold tracking-[-0.016em] tabular-nums">&pound;68</p>
            <button type="button" class="mt-2 inline-flex min-h-11 min-w-11 items-center justify-between gap-2 rounded-md border border-tmu16-acc px-4 text-sm font-semibold text-tmu16-acc cursor-pointer transition-colors duration-200 hover:bg-tmu16-acc hover:text-tmu16-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none">Add to bag<svg class="size-[17px] flex-none transition-transform duration-200 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
          </div>
        </article>
      </li>
      <li class="min-w-0">
        <article aria-labelledby="tmu16-p2" class="group grid min-w-0 gap-4 overflow-hidden rounded-lg bg-tmu16-surface shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition-[translate,box-shadow] duration-200 hover:-translate-y-[3px] hover:shadow-[0_18px_40px_-24px_rgb(40_30_20/0.35)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
          <div class="relative aspect-[4/5] min-w-0 overflow-hidden bg-tmu16-media">
            <div role="img" aria-label="Product photograph area, 4 by 5 &mdash; linen throw" class="grid size-full place-items-center transition-[scale] duration-300 group-hover:scale-[1.03] group-focus-within:scale-[1.03] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
              <span class="text-[0.6875rem] uppercase tracking-[0.14em] text-tmu16-ink-2">4:5 image area</span>
            </div>
            <button type="button" aria-label="Save Heavyweight linen throw to wishlist" aria-pressed="false" class="absolute top-3 right-3 grid size-11 place-items-center rounded-full bg-tmu16-surface/90 text-tmu16-ink-2 cursor-pointer backdrop-blur-sm transition-colors duration-150 hover:text-tmu16-acc aria-pressed:text-tmu16-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button>
          </div>
          <div class="grid min-w-0 gap-1.5 px-[1.125rem] pb-5">
            <p class="text-[0.6875rem] font-medium uppercase tracking-[0.14em] text-tmu16-ink-2">Aperture Goods</p>
            <h3 id="tmu16-p2" class="font-tmu16-serif text-lg/[1.25] font-medium tracking-[-0.012em] text-pretty">Heavyweight linen throw</h3>
            <p class="text-[0.8125rem] text-tmu16-ink-2">140 &times; 200 cm &middot; undyed European flax</p>
            <p class="mt-1 font-tmu16-serif text-[1.3125rem] font-semibold tracking-[-0.016em] tabular-nums">&pound;145</p>
            <button type="button" class="mt-2 inline-flex min-h-11 min-w-11 items-center justify-between gap-2 rounded-md border border-tmu16-acc px-4 text-sm font-semibold text-tmu16-acc cursor-pointer transition-colors duration-200 hover:bg-tmu16-acc hover:text-tmu16-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none">Add to bag<svg class="size-[17px] flex-none transition-transform duration-200 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
          </div>
        </article>
      </li>
      <li class="min-w-0">
        <article aria-labelledby="tmu16-p3" class="group grid min-w-0 gap-4 overflow-hidden rounded-lg bg-tmu16-surface shadow-[0_1px_2px_rgb(0_0_0/0.04)] transition-[translate,box-shadow] duration-200 hover:-translate-y-[3px] hover:shadow-[0_18px_40px_-24px_rgb(40_30_20/0.35)] focus-within:-translate-y-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:focus-within:translate-y-0">
          <div class="relative aspect-[4/5] min-w-0 overflow-hidden bg-tmu16-media">
            <div role="img" aria-label="Product photograph area, 4 by 5 &mdash; desk lamp" class="grid size-full place-items-center transition-[scale] duration-300 group-hover:scale-[1.03] group-focus-within:scale-[1.03] motion-reduce:transition-none motion-reduce:group-hover:scale-100">
              <span class="text-[0.6875rem] uppercase tracking-[0.14em] text-tmu16-ink-2">4:5 image area</span>
            </div>
            <button type="button" aria-label="Save Anodised desk lamp to wishlist" aria-pressed="false" class="absolute top-3 right-3 grid size-11 place-items-center rounded-full bg-tmu16-surface/90 text-tmu16-ink-2 cursor-pointer backdrop-blur-sm transition-colors duration-150 hover:text-tmu16-acc aria-pressed:text-tmu16-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none"><svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button>
          </div>
          <div class="grid min-w-0 gap-1.5 px-[1.125rem] pb-5">
            <p class="text-[0.6875rem] font-medium uppercase tracking-[0.14em] text-tmu16-ink-2">Sable Works</p>
            <h3 id="tmu16-p3" class="font-tmu16-serif text-lg/[1.25] font-medium tracking-[-0.012em] text-pretty">Anodised desk lamp</h3>
            <p class="text-[0.8125rem] text-tmu16-ink-2">2700 K &middot; stepless dimming</p>
            <p class="mt-1 font-tmu16-serif text-[1.3125rem] font-semibold tracking-[-0.016em] tabular-nums">&pound;210</p>
            <button type="button" class="mt-2 inline-flex min-h-11 min-w-11 items-center justify-between gap-2 rounded-md border border-tmu16-acc px-4 text-sm font-semibold text-tmu16-acc cursor-pointer transition-colors duration-200 hover:bg-tmu16-acc hover:text-tmu16-acc-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu16-acc motion-reduce:transition-none">Add to bag<svg class="size-[17px] flex-none transition-transform duration-200 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
          </div>
        </article>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu16-bg: light-dark(#f7f5f1, #14120f);
  --color-tmu16-bg: light-dark(oklch(96.8% 0.006 80), oklch(18% 0.006 70));
  --color-tmu16-surface: light-dark(#fffefc, #1c1a16);
  --color-tmu16-surface: light-dark(oklch(99.5% 0.003 85), oklch(22.5% 0.007 72));
  --color-tmu16-media: light-dark(#eae5dd, #262219);
  --color-tmu16-media: light-dark(oklch(92% 0.01 80), oklch(27% 0.01 78));
  --color-tmu16-ink: light-dark(#1a1815, #f4f1eb);
  --color-tmu16-ink: light-dark(oklch(20.5% 0.007 70), oklch(96% 0.006 85));
  --color-tmu16-ink-2: light-dark(#56514a, #b0a99e);
  --color-tmu16-ink-2: light-dark(oklch(45% 0.01 72), oklch(75% 0.011 80));
  --color-tmu16-line: light-dark(#d9d3c9, #3a352c);
  --color-tmu16-line: light-dark(oklch(86% 0.012 80), oklch(33% 0.012 78));
  --color-tmu16-acc: light-dark(#23433a, #8ecfb8);
  --color-tmu16-acc: light-dark(oklch(33% 0.05 165), oklch(83% 0.08 168));
  --color-tmu16-acc-ink: light-dark(#fbfaf8, #14211c);
  --color-tmu16-acc-ink: light-dark(oklch(98.5% 0.003 85), oklch(19% 0.02 168));
  --font-tmu16-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --font-tmu16-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu16-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-16:has(#tmu16-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-16:has(#tmu16-theme:checked) {
    color-scheme: light;
  }
}
```
