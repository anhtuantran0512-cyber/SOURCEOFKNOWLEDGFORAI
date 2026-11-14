---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-ecommerce-department-store-mega-menu/"
title: "Tailwind E-commerce Department Store Mega Menu Grid"
section: "navigation"
category: "tailwind-css-mega-menus"
category_name: "Tailwind CSS Mega Menus"
description: "Dense retail navigation done the Swiss way: four ruled columns of up to seven links each, heavy black rules, one red accent, and a footer row of…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-commerce Department Store Mega Menu Grid
Source: https://codefronts.com/navigation/tailwind-css-mega-menus/tailwind-ecommerce-department-store-mega-menu/

Dense retail navigation done the Swiss way: four ruled columns of up to seven links each, heavy black rules, one red accent, and a footer row of department-wide links. Columns share rows through grid-rows-subgrid so headings sit on one line, and they wipe in strictly left to right on a linear clock. New lines are flagged inline. Zero JavaScript.
## HTML
```html
<section class="tmm-18 relative w-full min-h-svh bg-tmm18-bg font-tmm18-sans leading-normal text-tmm18-ink [&_:focus-visible]:outline-2 [&_:focus-visible]:outline-offset-2 [&_:focus-visible]:outline-tmm18-acc" aria-labelledby="tmm18-title">
  <h2 class="sr-only" id="tmm18-title">Sable and Vale</h2>

  <div class="absolute top-[43px] right-[clamp(0.75rem,3vw,1.5rem)] z-60">
    <input class="peer absolute inset-0 m-0 size-full cursor-pointer opacity-0" type="checkbox" id="tmm18-theme">
    <label class="grid size-11 cursor-pointer place-items-center rounded-none border border-tmm18-line bg-tmm18-surf text-tmm18-ink peer-focus-visible:outline-2 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tmm18-acc" for="tmm18-theme">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sr-only">Toggle dark theme</span>
    </label>
  </div>

  <header class="relative z-10 w-full border-b-2 border-tmm18-line bg-tmm18-surf">
    <div class="mx-auto flex min-h-[34px] w-[min(82rem,calc(100%-2rem))] flex-wrap items-center gap-x-5 border-b border-tmm18-soft font-tmm18-display text-[0.76rem]/none font-medium tracking-[0.08em] text-tmm18-mut uppercase">
      <span>Free click and collect from 68 stores</span>
      <a class="ml-auto inline-flex min-h-[34px] items-center hover:text-tmm18-acc" href="#tmm18-title">Store finder</a>
      <a class="inline-flex min-h-[34px] items-center hover:text-tmm18-acc" href="#tmm18-title">Account</a>
      <a class="inline-flex min-h-[34px] items-center hover:text-tmm18-acc" href="#tmm18-title">Bag (0)</a>
    </div>
    <div class="mx-auto flex min-h-[62px] w-[min(82rem,calc(100%-2rem))] flex-wrap items-stretch gap-x-[clamp(0.75rem,3vw,2.5rem)] pr-15 max-[52rem]:flex-col max-[52rem]:py-2">
      <a class="inline-flex items-center font-tmm18-display text-[1.05rem]/none font-bold tracking-[0.22em] text-tmm18-ink" href="#tmm18-title">SABLE &amp; VALE</a>
      <nav class="flex min-w-0" aria-label="Primary">
        <ul class="flex flex-wrap gap-[clamp(0.15rem,1.5vw,0.75rem)] max-[52rem]:flex-col">
          <li data-tmm18-item class="flex items-stretch max-[52rem]:block">
            <button type="button" id="tmm18-trigger-home" aria-expanded="false" aria-controls="tmm18-panel-home" class="inline-flex min-h-11 cursor-pointer items-center px-2 font-tmm18-display text-[0.9rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase transition-[color,box-shadow] hover:text-tmm18-acc tmm18-open:text-tmm18-acc! tmm18-open:shadow-[inset_0_-3px_0_var(--color-tmm18-acc)]">Home</button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm18-line bg-tmm18-surf opacity-0 pointer-events-none transition-[opacity,visibility] duration-150 tmm18-open:visible tmm18-open:opacity-100 tmm18-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm18-open:block" id="tmm18-panel-home" aria-labelledby="tmm18-trigger-home">
              <div class="mx-auto grid w-[min(82rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] grid-rows-[auto_minmax(0,1fr)] gap-x-[clamp(1.25rem,4vw,3rem)] gap-y-1.5 py-[clamp(1.1rem,3vw,1.9rem)] min-[66rem]:grid-cols-4 max-[52rem]:w-full max-[52rem]:px-4">
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-0 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Kitchen &amp; dining</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Cookware</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Knives</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Tableware</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Glassware<span class="bg-tmm18-acc px-1.5 py-0.5 font-tmm18-display text-[0.62rem]/none font-bold tracking-[0.12em] text-white uppercase">New</span></a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Small appliances</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Storage</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Table linen</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-90 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Bed &amp; bath</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Duvets</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Bed linen</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Pillows</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Towels</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Bath mats</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Robes</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-180 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Furniture</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Sofas</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Dining tables<span class="bg-tmm18-acc px-1.5 py-0.5 font-tmm18-display text-[0.62rem]/none font-bold tracking-[0.12em] text-white uppercase">New</span></a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Chairs</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Storage units</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Desks</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-270 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Decoration</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Lighting</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Rugs</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Mirrors</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Candles</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Frames</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Vases</a></li>
                  </ul>
                </section>
              </div>
              <div class="mx-auto flex w-[min(82rem,calc(100%-2rem))] flex-wrap gap-x-[clamp(0.75rem,3vw,2rem)] border-t border-tmm18-line pt-2 pb-3.5 max-[52rem]:w-full max-[52rem]:px-4">
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">All home departments<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">Delivery and assembly<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">Returns<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">Gift registry<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
              </div>
            </div>
          </li>
          <li data-tmm18-item class="flex items-stretch max-[52rem]:block">
            <button type="button" id="tmm18-trigger-women" aria-expanded="false" aria-controls="tmm18-panel-women" class="inline-flex min-h-11 cursor-pointer items-center px-2 font-tmm18-display text-[0.9rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase transition-[color,box-shadow] hover:text-tmm18-acc tmm18-open:text-tmm18-acc! tmm18-open:shadow-[inset_0_-3px_0_var(--color-tmm18-acc)]">Women</button>
            <div class="invisible absolute inset-x-0 top-full z-30 border-b border-tmm18-line bg-tmm18-surf opacity-0 pointer-events-none transition-[opacity,visibility] duration-150 tmm18-open:visible tmm18-open:opacity-100 tmm18-open:pointer-events-auto motion-reduce:transition-none max-[52rem]:static max-[52rem]:hidden max-[52rem]:visible max-[52rem]:opacity-100 max-[52rem]:tmm18-open:block" id="tmm18-panel-women" aria-labelledby="tmm18-trigger-women">
              <div class="mx-auto grid w-[min(82rem,calc(100%-2rem))] grid-cols-[repeat(auto-fit,minmax(min(100%,12rem),1fr))] grid-rows-[auto_minmax(0,1fr)] gap-x-[clamp(1.25rem,4vw,3rem)] gap-y-1.5 py-[clamp(1.1rem,3vw,1.9rem)] min-[66rem]:grid-cols-4 max-[52rem]:w-full max-[52rem]:px-4">
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-0 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Clothing</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Coats<span class="bg-tmm18-acc px-1.5 py-0.5 font-tmm18-display text-[0.62rem]/none font-bold tracking-[0.12em] text-white uppercase">New</span></a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Knitwear</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Dresses</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Trousers</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Denim</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-90 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Shoes</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Boots</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Flats</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Trainers</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-180 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Accessories</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Bags</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Scarves</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Jewellery</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Belts</a></li>
                  </ul>
                </section>
                <section class="row-span-2 grid min-w-0 grid-rows-[auto_minmax(0,1fr)] gap-1.5 [clip-path:inset(0_100%_0_0)] transition-[clip-path] duration-300 ease-linear delay-270 supports-[grid-template-rows:subgrid]:grid-rows-subgrid tmm18-open:[clip-path:inset(-4px)] motion-reduce:[clip-path:none] motion-reduce:transition-none">
                  <h3 class="border-b-2 border-tmm18-line pb-1.5 font-tmm18-display text-[0.8rem]/tight font-bold tracking-[0.16em] uppercase">Brands</h3>
                  <ul class="grid content-start">
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Meridian</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Fern</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Orbit</a></li>
                    <li><a href="#tmm18-title" class="flex min-h-11 min-w-0 items-center justify-between gap-2 border-b border-tmm18-soft text-[0.9rem]/snug text-tmm18-mut transition-colors hover:text-tmm18-acc">Quill</a></li>
                  </ul>
                </section>
              </div>
              <div class="mx-auto flex w-[min(82rem,calc(100%-2rem))] flex-wrap gap-x-[clamp(0.75rem,3vw,2rem)] border-t border-tmm18-line pt-2 pb-3.5 max-[52rem]:w-full max-[52rem]:px-4">
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">New in<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">Sale<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
                <a class="group/f inline-flex min-h-11 items-center gap-1.5 font-tmm18-display text-[0.76rem]/none font-semibold tracking-[0.14em] text-tmm18-ink uppercase hover:text-tmm18-acc" href="#tmm18-title">Size guide<span aria-hidden="true" class="transition-transform group-hover/f:translate-x-0.5">&rarr;</span></a>
              </div>
            </div>
          </li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-2 font-tmm18-display text-[0.9rem]/none font-semibold tracking-[0.14em] uppercase hover:text-tmm18-acc " href="#tmm18-title">Men</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-2 font-tmm18-display text-[0.9rem]/none font-semibold tracking-[0.14em] uppercase hover:text-tmm18-acc " href="#tmm18-title">Beauty</a></li>
          <li class="flex items-stretch"><a class="inline-flex min-h-11 items-center px-2 font-tmm18-display text-[0.9rem]/none font-semibold tracking-[0.14em] uppercase hover:text-tmm18-acc text-tmm18-acc" href="#tmm18-title">Sale</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="mx-auto w-[min(82rem,calc(100%-2rem))] py-[clamp(2.5rem,8vw,5rem)]">
    <div class="grid max-w-[40rem] gap-2.5">
      <p class="font-tmm18-display text-[0.76rem]/none font-bold tracking-[0.24em] text-tmm18-acc uppercase">Autumn edit</p>
      <h1 class="font-tmm18-display text-[clamp(2.1rem,6vw,3.6rem)]/[1.02] font-bold tracking-[-0.01em] text-balance">Sixty years of the Sable &amp; Vale winter table.</h1>
      <a class="mt-2 inline-flex min-h-12 w-fit items-center gap-2 bg-tmm18-ink px-5.5 font-tmm18-display text-[0.82rem]/none font-semibold tracking-[0.16em] text-tmm18-bg uppercase transition-colors hover:bg-tmm18-acc hover:text-white" href="#tmm18-title">Shop the collection <span aria-hidden="true">&rarr;</span></a>
    </div>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmm18-bg: #ffffff;
  --color-tmm18-bg: oklch(1 0 0);
  --color-tmm18-surf: #ffffff;
  --color-tmm18-surf: oklch(1 0 0);
  --color-tmm18-line: #111111;
  --color-tmm18-line: oklch(0.18 0 0);
  --color-tmm18-soft: #e8e8e8;
  --color-tmm18-soft: oklch(0.93 0 0);
  --color-tmm18-ink: #111111;
  --color-tmm18-ink: oklch(0.18 0 0);
  --color-tmm18-mut: #5e5e5e;
  --color-tmm18-mut: oklch(0.46 0 0);
  --color-tmm18-acc: #e10600;
  --color-tmm18-acc: oklch(0.56 0.24 28);
  --font-tmm18-display: 'Barlow Condensed', 'Archivo Narrow', sans-serif;
  --font-tmm18-sans: 'Barlow', system-ui, sans-serif;
}
/* The open state as ONE variant: focus-within or a scripted [data-open], hover only where hover exists.
   Every panel, chevron and entry utility reads tmm18-open: instead of a repeated selector list. */

@custom-variant tmm18-open {
  &:where([data-tmm18-item]:is(:focus-within, [data-open]) *) {
    @slot;
  }

  @media (hover: hover) {
    &:where([data-tmm18-item]:hover *) {
      @slot;
    }
  }
}
/* Root rule: the full-bleed contract, sized before the browser build compiles. */

.tmm-18 {
  width: 100%;
  min-height: 100svh;
}
/* Theme toggle: the checkbox flips the token set; the OS preference flips the default. */

.tmm-18:has(#tmm18-theme:checked) {
  --color-tmm18-bg: #0a0a0a;
  --color-tmm18-bg: oklch(0.14 0 0);
  --color-tmm18-surf: #101010;
  --color-tmm18-surf: oklch(0.17 0 0);
  --color-tmm18-line: #f0f0f0;
  --color-tmm18-line: oklch(0.95 0 0);
  --color-tmm18-soft: #242424;
  --color-tmm18-soft: oklch(0.26 0 0);
  --color-tmm18-ink: #f0f0f0;
  --color-tmm18-ink: oklch(0.95 0 0);
  --color-tmm18-mut: #a0a0a0;
  --color-tmm18-mut: oklch(0.71 0 0);
  --color-tmm18-acc: #ff4d3d;
  --color-tmm18-acc: oklch(0.7 0.19 32);
}

@media (prefers-color-scheme: dark) {
  .tmm-18 {
    --color-tmm18-bg: #0a0a0a;
    --color-tmm18-bg: oklch(0.14 0 0);
    --color-tmm18-surf: #101010;
    --color-tmm18-surf: oklch(0.17 0 0);
    --color-tmm18-line: #f0f0f0;
    --color-tmm18-line: oklch(0.95 0 0);
    --color-tmm18-soft: #242424;
    --color-tmm18-soft: oklch(0.26 0 0);
    --color-tmm18-ink: #f0f0f0;
    --color-tmm18-ink: oklch(0.95 0 0);
    --color-tmm18-mut: #a0a0a0;
    --color-tmm18-mut: oklch(0.71 0 0);
    --color-tmm18-acc: #ff4d3d;
    --color-tmm18-acc: oklch(0.7 0.19 32);
  }

  .tmm-18:has(#tmm18-theme:checked) {
    --color-tmm18-bg: #ffffff;
    --color-tmm18-bg: oklch(1 0 0);
    --color-tmm18-surf: #ffffff;
    --color-tmm18-surf: oklch(1 0 0);
    --color-tmm18-line: #111111;
    --color-tmm18-line: oklch(0.18 0 0);
    --color-tmm18-soft: #e8e8e8;
    --color-tmm18-soft: oklch(0.93 0 0);
    --color-tmm18-ink: #111111;
    --color-tmm18-ink: oklch(0.18 0 0);
    --color-tmm18-mut: #5e5e5e;
    --color-tmm18-mut: oklch(0.46 0 0);
    --color-tmm18-acc: #e10600;
    --color-tmm18-acc: oklch(0.56 0.24 28);
  }
}
```
