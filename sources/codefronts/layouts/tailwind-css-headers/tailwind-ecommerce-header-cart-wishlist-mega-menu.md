---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-headers/tailwind-ecommerce-header-cart-wishlist-mega-menu/"
title: "Tailwind E-Commerce Header with Cart, Wishlist and Mega Menu"
section: "layouts"
category: "tailwind-css-headers"
category_name: "Tailwind CSS Headers"
description: "A storefront header with the utility cluster shoppers reach for — account, a wishlist heart with its count and a cart pill with a running total — plus a Shop…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Header with Cart, Wishlist and Mega Menu
Source: https://codefronts.com/layouts/tailwind-css-headers/tailwind-ecommerce-header-cart-wishlist-mega-menu/

A storefront header with the utility cluster shoppers reach for — account, a wishlist heart with its count and a cart pill with a running total — plus a Shop mega panel of categories, three featured products and a members promo. Counts use tabular-nums so nothing shifts as the basket changes.
## HTML
```html
<div class="thd-04 group/thd04 w-full min-h-svh bg-[linear-gradient(160deg,var(--color-thd04-bg-a),var(--color-thd04-bg-b))] font-thd04-sans text-thd04-ink antialiased">
  <a href="#thd-04-main" class="sr-only focus:not-sr-only focus:absolute focus:left-3 focus:top-3 focus:z-[60] focus:rounded-lg focus:bg-thd04-acc focus:px-4 focus:py-2.5 focus:text-sm focus:font-semibold focus:text-white">Skip to content</a>
  <p class="bg-thd04-ink px-4 py-2 text-center text-xs font-medium tracking-wide text-thd04-bar">Free returns for 60 days &middot; Free shipping over $150</p>
  <header class="sticky top-0 z-40 border-b border-thd04-line bg-thd04-bar/90 backdrop-blur-lg">
    <div class="mx-auto flex h-16 max-w-7xl items-center gap-3 px-[clamp(.75rem,3vw,1.5rem)] sm:gap-6">
      <a href="#thd-04-main" class="whitespace-nowrap font-thd04-display text-[1.6rem] font-extrabold uppercase leading-none tracking-tight">Lumen <span class="text-thd04-acc">&amp;</span> Field</a>
      <nav aria-label="Main" class="hidden md:block">
        <ul class="flex items-center gap-1 text-sm font-semibold">
          <li class="group/shop">
            <a href="#thd-04-main" aria-haspopup="true" class="flex min-h-11 items-center gap-1 rounded-full px-3.5 hover:bg-thd04-ink/5 group-hover/shop:bg-thd04-ink/5">Shop <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true" class="size-3.5 transition-transform group-hover/shop:rotate-180 group-focus-within/shop:rotate-180"><path d="m6 9 6 6 6-6"/></svg></a>
            <div class="invisible absolute inset-x-0 top-full z-50 border-b border-thd04-line bg-thd04-bar opacity-0 shadow-[0_30px_60px_-30px_var(--color-thd04-acc)] transition-[opacity,visibility] duration-150 group-hover/shop:visible group-hover/shop:opacity-100 group-focus-within/shop:visible group-focus-within/shop:opacity-100">
              <div class="mx-auto grid max-w-7xl gap-8 px-[clamp(.75rem,3vw,1.5rem)] py-8 lg:grid-cols-[12rem_1fr_15rem]">
                <div><p class="mb-3 text-[11px] font-bold uppercase tracking-[.14em] text-thd04-mut">Categories</p><ul class="grid gap-0.5 text-[15px] font-medium"><li><a href="#thd-04-main" class="flex min-h-9 items-center hover:text-thd04-acc">New arrivals</a></li><li><a href="#thd-04-main" class="flex min-h-9 items-center hover:text-thd04-acc">Footwear</a></li><li><a href="#thd-04-main" class="flex min-h-9 items-center hover:text-thd04-acc">Outerwear</a></li><li><a href="#thd-04-main" class="flex min-h-9 items-center hover:text-thd04-acc">Accessories</a></li><li><a href="#thd-04-main" class="flex min-h-9 items-center hover:text-thd04-acc">Home objects</a></li><li><a href="#thd-04-main" class="flex min-h-9 items-center text-thd04-acc">Last chance</a></li></ul></div>
                <div><p class="mb-3 text-[11px] font-bold uppercase tracking-[.14em] text-thd04-mut">Featured this week</p>
                  <ul class="grid grid-cols-3 gap-4">
                    <li><a href="#thd-04-main" class="group/p block"><span class="block aspect-[4/3] overflow-hidden rounded-xl"><span class="block size-full bg-[radial-gradient(circle_at_30%_30%,#f6d2b8,#d98a6a)] transition-transform duration-500 group-hover/p:scale-105"></span></span><span class="mt-2 block text-sm font-semibold">Ridge low-top</span><span class="block text-sm tabular-nums text-thd04-mut">$128.00</span></a></li>
                    <li><a href="#thd-04-main" class="group/p block"><span class="block aspect-[4/3] overflow-hidden rounded-xl"><span class="block size-full bg-[radial-gradient(circle_at_60%_40%,#e6e1f5,#9b8fcf)] transition-transform duration-500 group-hover/p:scale-105"></span></span><span class="mt-2 block text-sm font-semibold">Field watch 38</span><span class="block text-sm tabular-nums text-thd04-mut">$245.00</span></a></li>
                    <li><a href="#thd-04-main" class="group/p block"><span class="block aspect-[4/3] overflow-hidden rounded-xl"><span class="block size-full bg-[radial-gradient(circle_at_40%_60%,#fbe7c6,#e0a458)] transition-transform duration-500 group-hover/p:scale-105"></span></span><span class="mt-2 block text-sm font-semibold">Meridian shades</span><span class="block text-sm tabular-nums text-thd04-mut">$96.00</span></a></li>
                  </ul>
                </div>
                <div class="rounded-2xl bg-thd04-ink p-5 text-thd04-bar"><p class="text-[11px] font-bold uppercase tracking-[.14em] opacity-70">Members</p><p class="mt-2 font-thd04-display text-2xl font-bold uppercase leading-none">Free returns for 60 days</p><p class="mt-2 text-sm opacity-80">Plus early access to the autumn drop on 2 October.</p><a href="#thd-04-main" class="mt-4 inline-flex min-h-10 items-center rounded-full bg-thd04-acc px-4 text-sm font-bold text-white">Join free &rarr;</a></div>
              </div>
            </div>
          </li>
          <li><a href="#thd-04-main" class="flex min-h-11 items-center rounded-full px-3.5 hover:bg-thd04-ink/5">Collections</a></li>
          <li><a href="#thd-04-main" class="flex min-h-11 items-center rounded-full px-3.5 hover:bg-thd04-ink/5">Journal</a></li>
          <li class="hidden lg:block"><a href="#thd-04-main" class="flex min-h-11 items-center rounded-full px-3.5 hover:bg-thd04-ink/5">Stores</a></li>
        </ul>
      </nav>
      <label class="ml-auto hidden min-h-10 w-56 items-center gap-2 rounded-full border border-thd04-line bg-thd04-ink/[.03] px-3.5 text-sm transition focus-within:border-thd04-acc focus-within:ring-4 focus-within:ring-thd04-acc/15 xl:flex">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" class="size-4 flex-none text-thd04-mut"><circle cx="11" cy="11" r="6.4"/><path d="m15.8 15.8 5.2 5.2"/></svg>
        <input type="search" placeholder="Search the shop" aria-label="Search products" class="min-w-0 flex-1 bg-transparent outline-none placeholder:text-thd04-mut">
      </label>
      <div class="ml-auto flex items-center gap-0.5 xl:ml-0">
        <input id="thd-04-t" type="checkbox" class="peer/t sr-only">
        <label for="thd-04-t" class="grid size-11 cursor-pointer place-items-center rounded-full hover:bg-thd04-ink/5 peer-focus-visible/t:outline-2 peer-focus-visible/t:outline-thd04-acc">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5 group-has-[#thd-04-t:checked]/thd04:hidden"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5a8.6 8.6 0 1 0 10.9 10.9Z"/></svg>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="hidden size-5 group-has-[#thd-04-t:checked]/thd04:block"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5"/></svg>
          <span class="sr-only">Switch light or dark theme</span>
        </label>
        <a href="#thd-04-main" aria-label="Account" class="hidden size-11 place-items-center rounded-full hover:bg-thd04-ink/5 sm:grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" class="size-5"><circle cx="12" cy="8.5" r="3.6"/><path d="M5 20a7 7 0 0 1 14 0"/></svg></a>
        <a href="#thd-04-main" aria-label="Wishlist, 4 items" class="relative grid size-11 place-items-center rounded-full hover:bg-thd04-ink/5"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true" class="size-5"><path d="M12 20s-7.5-4.6-7.5-10.2A4.2 4.2 0 0 1 12 7.3a4.2 4.2 0 0 1 7.5 2.5C19.5 15.4 12 20 12 20Z"/></svg><span aria-hidden="true" class="absolute right-1 top-1 grid min-w-[18px] place-items-center rounded-full bg-thd04-acc px-1 text-[10px] font-bold leading-[18px] tabular-nums text-white ring-2 ring-thd04-bar">4</span></a>
        <a href="#thd-04-main" aria-label="Cart, 3 items, $142.00 — $8.00 away from free shipping" class="ml-1 flex min-h-11 flex-col justify-center gap-1 rounded-full bg-thd04-ink px-4 text-thd04-bar transition hover:-translate-y-px hover:shadow-[0_12px_28px_-12px_var(--color-thd04-acc)]">
          <span aria-hidden="true" class="flex items-center gap-2 text-sm font-bold tabular-nums"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 8h14l-1.2 12H6.2L5 8Z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/></svg>$142.00<span class="rounded-full bg-thd04-acc px-1.5 text-[10px] leading-4">3</span></span>
          <span aria-hidden="true" class="h-0.5 w-full overflow-hidden rounded-full bg-thd04-bar/20"><span class="block h-full w-[95%] rounded-full bg-thd04-acc"></span></span>
        </a>
      </div>
    </div>
  </header>
  <main id="thd-04-main" class="mx-auto max-w-7xl px-[clamp(.75rem,3vw,1.5rem)] py-12">
    <p class="text-xs font-bold uppercase tracking-[.16em] text-thd04-acc">Autumn &rsquo;26</p>
    <h1 class="mt-2 max-w-[14ch] font-thd04-display text-[clamp(2.6rem,9vw,5.5rem)] font-extrabold uppercase leading-[.9] tracking-tight">Made for the long walk home.</h1>
    <p class="mt-4 max-w-[46ch] text-thd04-mut">Hover or focus <strong class="text-thd04-ink">Shop</strong> for the mega panel. The cart pill shows how close you are to free shipping.</p>
    <div aria-hidden="true" class="h-[60svh]"></div>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme inline {
  --color-thd04-bg-a: var(--thd04-bg-a);
  --color-thd04-bg-b: var(--thd04-bg-b);
  --color-thd04-bar: var(--thd04-bar);
  --color-thd04-ink: var(--thd04-ink);
  --color-thd04-mut: var(--thd04-mut);
  --color-thd04-line: var(--thd04-line);
  --color-thd04-acc: var(--thd04-acc);
}

@theme {
  --font-thd04-display: 'Barlow Condensed', system-ui, sans-serif;
  --font-thd04-sans: 'DM Sans', system-ui, sans-serif;
}

.thd-04 {
  width: 100%;
  min-height: 100svh;
  --thd04-bg-a: #fde8dc;
  --thd04-bg-b: #ece6fa;
  --thd04-bar: #fffaf6;
  --thd04-ink: #1f1633;
  --thd04-mut: #5e556f;
  --thd04-line: rgb(31 22 51 / 0.1);
  --thd04-acc: #e0533d;
}

.thd-04:has(#thd-04-t:checked) {
  --thd04-bg-a: #1c1418;
  --thd04-bg-b: #15131f;
  --thd04-bar: #191520;
  --thd04-ink: #f7f1ec;
  --thd04-mut: #b3a9bd;
  --thd04-line: rgb(255 255 255 / 0.1);
  --thd04-acc: #ff7a5c;
}
```
