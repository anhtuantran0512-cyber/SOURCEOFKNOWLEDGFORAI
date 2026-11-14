---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-real-estate-listing-card-favourite-toggle/"
title: "Tailwind Real Estate Listing Card with Favourite Toggle"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "A property card led by price, with a status pill, a beds/baths/sqft feature row and a favourite heart that is a real checkbox — no script."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Real Estate Listing Card with Favourite Toggle
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-real-estate-listing-card-favourite-toggle/

A property card led by price, with a status pill, a beds/baths/sqft feature row and a favourite heart that is a real checkbox — no script. peer-checked: fills and pops the heart, and because the same checkbox is read by a peer-checked:opacity-100 pill, the saved state is text as well as colour.
## HTML
```html
<section class="tpc-17 w-full min-h-svh grid place-items-center bg-tpc17-bg font-tpc17-sans px-5 py-12" aria-label="Real estate listing card demo">
  <article class="w-[min(350px,100%)] rounded-[18px] overflow-hidden bg-tpc17-card shadow-[0_16px_40px_-22px_oklch(0.25_0.02_240/0.4)]">
    <div class="relative aspect-[16/10] bg-linear-[135deg,var(--color-tpc17-ph),var(--color-tpc17-ph2)] bg-[url('https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&h=500&fit=crop&q=70')] bg-cover bg-center">
      <div class="absolute top-3 left-3 flex items-center gap-2">
        <span class="px-3 py-1.25 rounded-full bg-tpc17-acc text-tpc17-onacc text-[11px] font-bold tracking-[0.04em]">For Sale</span>
        <span aria-hidden="true" class="tpc17-saved px-3 py-1.25 rounded-full bg-tpc17-card text-tpc17-fav text-[11px] font-bold tracking-[0.04em] transition-opacity duration-200 motion-reduce:transition-none">Saved</span>
      </div>
      <input type="checkbox" id="tpc17-fav" class="peer sr-only">
      <label for="tpc17-fav" aria-label="Save to favourites" class="absolute top-3 right-3 grid place-items-center size-11 rounded-full cursor-pointer bg-tpc17-card/92 text-[20px] leading-none text-tpc17-heart shadow-[0_4px_12px_-4px_oklch(0.2_0.02_240/0.35)] transition-[color,scale] duration-200 hover:text-tpc17-fav peer-checked:text-tpc17-fav peer-checked:scale-110 peer-focus-visible:outline-3 peer-focus-visible:outline-tpc17-acc peer-focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:peer-checked:scale-100"><span aria-hidden="true">&hearts;</span></label>
    </div>
    <div class="px-5 pt-4.5 pb-5">
      <p class="text-[24px] font-extrabold text-tpc17-ink tabular-nums">$685,000</p>
      <h3 class="mt-1 text-[16px] font-semibold text-tpc17-ink2">12 Larch Grove, Portland</h3>
      <p class="mt-0.5 text-[13px] text-tpc17-mut">Detached &middot; 2 storeys</p>
      <ul class="mt-4 pt-4 border-t border-tpc17-edge flex justify-between list-none">
        <li class="flex flex-col items-center gap-0.5"><b class="text-[17px] font-bold text-tpc17-ink tabular-nums">3</b><span class="text-[11px] tracking-[0.06em] uppercase text-tpc17-mut">Beds</span></li>
        <li class="flex flex-col items-center gap-0.5"><b class="text-[17px] font-bold text-tpc17-ink tabular-nums">2</b><span class="text-[11px] tracking-[0.06em] uppercase text-tpc17-mut">Baths</span></li>
        <li class="flex flex-col items-center gap-0.5"><b class="text-[17px] font-bold text-tpc17-ink tabular-nums">1,840</b><span class="text-[11px] tracking-[0.06em] uppercase text-tpc17-mut">Sq&nbsp;Ft</span></li>
      </ul>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc17-bg: #eef1f4;
  --color-tpc17-bg: oklch(0.95 0.006 240);
  --color-tpc17-card: #ffffff;
  --color-tpc17-card: oklch(1 0 0);
  --color-tpc17-ink: #101828;
  --color-tpc17-ink: oklch(0.23 0.03 260);
  --color-tpc17-ink2: #344054;
  --color-tpc17-ink2: oklch(0.4 0.03 260);
  --color-tpc17-mut: #5b6678;
  --color-tpc17-mut: oklch(0.5 0.025 260);
  --color-tpc17-edge: #e4e8ee;
  --color-tpc17-edge: oklch(0.93 0.008 250);
  --color-tpc17-ph: #d7dfe8;
  --color-tpc17-ph: oklch(0.89 0.015 240);
  --color-tpc17-ph2: #c3cdda;
  --color-tpc17-ph2: oklch(0.84 0.022 245);
  --color-tpc17-heart: #9aa5b4;
  --color-tpc17-heart: oklch(0.71 0.018 250);
  --color-tpc17-fav: #c8324a;
  --color-tpc17-fav: oklch(0.55 0.18 15);
  --color-tpc17-acc: #16688f;
  --color-tpc17-acc: oklch(0.47 0.11 225);
  --color-tpc17-onacc: #ffffff;
  --color-tpc17-onacc: oklch(1 0 0);
  --font-tpc17-sans: 'Manrope', system-ui, sans-serif;
}

.tpc-17 {
  width: 100%;
  min-height: 100svh;
}

.tpc-17 ::selection {
  background: var(--color-tpc17-acc);
  color: #fff;
}
/* The 'Saved' pill sits BEFORE the checkbox in source order, and peer-* only looks
   forward — so one :has() rule owns the pill's visibility outright. Declaring it here
   rather than fighting an opacity-0 utility also sidesteps the layering question:
   this rule is unlayered, so nothing in @layer utilities can override it. */

.tpc-17 .tpc17-saved {
  opacity: 0;
}

.tpc-17 :has(> #tpc17-fav:checked) .tpc17-saved {
  opacity: 1;
}
```
