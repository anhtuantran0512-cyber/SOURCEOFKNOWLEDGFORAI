---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-ecommerce-product-grid-card/"
title: "Tailwind E-Commerce Product Grid Card with Hover Quick-Add"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "The reference-grade commerce tile: one hero product beside a stacked pair, with badges, a wishlist counter, a star-rating pill, colour swatches, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Product Grid Card with Hover Quick-Add
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-ecommerce-product-grid-card/

The reference-grade commerce tile: one hero product beside a stacked pair, with badges, a wishlist counter, a star-rating pill, colour swatches, a strikethrough price and a quick-add bar that rises on hover. The port's win is group/card — image zoom, quick-add reveal and CTA lift all read one named ancestor, so a small tile nested in the hero row can never capture the wrong parent.
## HTML
```html
<section class="twc-01 w-full min-h-svh flex flex-col items-center justify-center gap-4 px-5 py-9 bg-twc01-bg [background-image:radial-gradient(ellipse_at_20%_15%,oklch(0.78_0.15_60/0.07),transparent_45%),radial-gradient(ellipse_at_80%_85%,oklch(0.68_0.2_350/0.05),transparent_45%),linear-gradient(180deg,#fff8f1_0%,#f4ede4_100%)] font-twc01-sans" aria-label="Products">

  <header class="w-full max-w-[780px]">
    <div class="inline-flex items-center gap-1.5 mb-2.5 px-2.5 py-1 rounded-full font-twc01-mono text-[10px] font-extrabold tracking-[0.14em] text-twc01-accink bg-twc01-acc/8 border border-twc01-acc/20">
      <span aria-hidden="true" class="size-[5px] rounded-full bg-twc01-acc shadow-[0_0_8px_oklch(0.62_0.19_45/0.5)] animate-twc01-pulse motion-reduce:animate-none"></span>
      NEW ARRIVALS &middot; KITCHEN
    </div>
    <div class="flex max-sm:flex-col max-sm:items-start items-center justify-between gap-3">
      <h3 class="m-0 text-xl font-extrabold tracking-[-0.025em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Trending this week</h3>
      <div role="tablist" aria-label="Sort" class="inline-flex gap-0.5 p-[3px] rounded-full bg-white/65 border border-black/5">
        <button type="button" role="tab" aria-selected="true" class="min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[11px] font-bold bg-twc01-ink text-white transition-colors duration-200 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2">Popular</button>
        <button type="button" role="tab" aria-selected="false" class="min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[11px] font-bold bg-transparent text-twc01-muted transition-colors duration-200 hover:text-twc01-ink focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2">New</button>
      </div>
    </div>
  </header>

  <div class="w-full max-w-[780px] grid grid-cols-[minmax(0,1.4fr)_minmax(0,1fr)] max-sm:grid-cols-1 max-sm:max-w-[360px] gap-3.5 items-stretch">

    <article class="group/card flex flex-col overflow-hidden rounded-twc01-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.45_0.06_50/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc01-acc/25 hover:shadow-[0_24px_44px_-18px_oklch(0.45_0.06_50/0.26),inset_0_0_0_1px_oklch(1_0_0/0.5)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative aspect-square overflow-hidden bg-twc01-mediabg">
        <img src="https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=1000&q=80&auto=format&fit=crop" alt="Ceramic pour-over kettle by Fellow" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">

        <div class="absolute top-2.5 left-2.5 flex flex-wrap gap-1.5 max-w-[calc(100%-60px)]">
          <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc01-mono text-[9px] font-extrabold tracking-[0.14em] bg-twc01-ink text-white border border-white/15">NEW</span>
          <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc01-mono text-[9px] font-extrabold tracking-[0.14em] [background:linear-gradient(180deg,#fef3c7,#fde68a)] text-twc01-amberink border border-twc01-amberink/25 shadow-[0_2px_5px_oklch(0.78_0.15_70/0.3)]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            BESTSELLER
          </span>
        </div>

        <button type="button" aria-label="Add to wishlist" class="absolute top-2.5 right-2.5 inline-flex items-center gap-1 pl-1.5 pr-2 py-1 min-h-8 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc01-ink text-[10.5px] font-bold cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc01-red hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          <span class="font-twc01-mono text-[10px] [font-variant-numeric:tabular-nums]">248</span>
        </button>

        <div class="absolute bottom-[46px] left-3 right-3 opacity-0 translate-y-2.5 pointer-events-none transition-[opacity,transform] duration-250 group-hover/card:opacity-100 group-hover/card:translate-y-0 group-hover/card:pointer-events-auto group-focus-within/card:opacity-100 group-focus-within/card:translate-y-0 group-focus-within/card:pointer-events-auto [@media(hover:none)]:opacity-100 [@media(hover:none)]:translate-y-0 [@media(hover:none)]:pointer-events-auto motion-reduce:transition-none">
          <button type="button" class="w-full min-h-11 px-3 py-2 rounded-[10px] bg-twc01-ink/92 backdrop-blur-[8px] border border-white/15 text-white text-xs font-bold cursor-pointer transition-colors duration-200 hover:bg-twc01-ink focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Quick add &middot; $68</button>
        </div>

        <div class="absolute bottom-2.5 left-3 inline-flex items-center gap-1.5 px-2 py-[3px] rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc01-greenink text-[10px] font-bold">
          <span aria-hidden="true" class="size-[5px] rounded-full bg-twc01-green shadow-[0_0_6px_oklch(0.72_0.15_163)] animate-twc01-pulse motion-reduce:animate-none"></span>
          Ships tomorrow &middot; 12 left
        </div>
      </div>

      <div class="flex-1 flex flex-col gap-2 px-4 py-3.5">
        <p class="m-0 font-twc01-mono text-[9.5px] font-extrabold tracking-[0.14em] text-twc01-acc">KITCHEN &middot; BREW</p>
        <div class="flex items-start justify-between gap-2">
          <h4 class="m-0 text-[15px]/[1.3] font-extrabold tracking-[-0.015em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Ceramic Pour-Over Kettle</h4>
          <span class="inline-flex flex-none items-center gap-1 pt-0.5 text-[10.5px] font-bold text-twc01-muted">
            <span aria-hidden="true" class="inline-flex items-center justify-center size-4 rounded bg-[linear-gradient(135deg,#1a1a1a,#4b4b57)] text-white text-[9px] font-extrabold">F</span>
            Fellow
          </span>
        </div>
        <div role="img" aria-label="Rated 4.8 out of 5, 127 reviews" class="self-start inline-flex items-center gap-1.5 px-[7px] py-[3px] rounded-full bg-twc01-amber/10 border border-twc01-amber/20">
          <span class="inline-flex gap-px text-twc01-amber">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
          </span>
          <span class="font-twc01-mono text-[10.5px] font-extrabold text-twc01-amberink [font-variant-numeric:tabular-nums]">4.8<span class="font-bold text-twc01-dim"> (127)</span></span>
        </div>
        <div aria-label="Available colors" class="flex items-center -mx-3.5">
          <button type="button" aria-label="Matte black" class="inline-flex items-center justify-center size-11 p-3.5 rounded-full bg-transparent border-0 cursor-pointer transition-transform duration-200 hover:scale-110 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full bg-twc01-ink border-[1.5px] border-black/10"></span></button>
          <button type="button" aria-label="Cream" aria-pressed="true" class="inline-flex items-center justify-center size-11 p-3.5 rounded-full bg-transparent border-0 cursor-pointer transition-transform duration-200 hover:scale-110 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full bg-twc01-bg2 border-[1.5px] border-white shadow-[0_0_0_2px_var(--color-twc01-acc)]"></span></button>
          <button type="button" aria-label="Sage" class="inline-flex items-center justify-center size-11 p-3.5 rounded-full bg-transparent border-0 cursor-pointer transition-transform duration-200 hover:scale-110 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100"><span class="block size-full rounded-full bg-twc01-sage border-[1.5px] border-black/10"></span></button>
          <span class="ml-1 text-[10px] font-bold text-twc01-muted">+2</span>
        </div>
        <div class="flex items-center justify-between gap-2 mt-1">
          <div class="inline-flex items-center gap-1.5">
            <span class="text-xl font-extrabold tracking-[-0.02em] [font-variant-numeric:tabular-nums] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">$68</span>
            <span class="text-xs text-twc01-dim line-through [font-variant-numeric:tabular-nums]">$84</span>
            <span class="inline-flex items-center px-1.5 py-0.5 rounded [background:linear-gradient(180deg,#dc2626,#b91c1c)] text-white font-twc01-mono text-[9.5px] font-extrabold tracking-[0.02em] shadow-[0_2px_4px_oklch(0.58_0.22_25/0.3)]">&minus;19%</span>
          </div>
          <button type="button" class="inline-flex items-center justify-center gap-1.5 min-h-11 px-4 py-2 rounded-full border-0 cursor-pointer text-xs font-extrabold text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_4px_12px_oklch(0_0_0/0.2),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,box-shadow,background] duration-200 hover:-translate-y-px hover:[background:linear-gradient(180deg,#ea580c_0%,#9a3412_100%)] hover:shadow-[0_6px_16px_oklch(0.62_0.19_45/0.35)] focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
            Add
          </button>
        </div>
        <div class="flex items-center gap-2 mt-1.5 px-2.5 py-2 rounded-[10px] bg-twc01-acc/6 border border-twc01-acc/15">
          <div aria-hidden="true" class="flex">
            <span class="flex items-center justify-center size-5 rounded-full border-[1.5px] border-white text-white text-[8px] font-extrabold [background:linear-gradient(135deg,#f472b6,#ec4899)]">AR</span>
            <span class="flex items-center justify-center size-5 -ml-1.5 rounded-full border-[1.5px] border-white text-white text-[8px] font-extrabold [background:linear-gradient(135deg,#60a5fa,#3b82f6)]">JL</span>
            <span class="flex items-center justify-center size-5 -ml-1.5 rounded-full border-[1.5px] border-white text-white text-[8px] font-extrabold [background:linear-gradient(135deg,#34d399,#10b981)]">MK</span>
          </div>
          <span class="text-[10.5px] text-twc01-accink"><strong class="font-extrabold text-twc01-acc">34</strong> people bought today</span>
        </div>
      </div>
    </article>

    <div class="flex flex-col gap-3.5 min-w-0">

      <article class="group/card flex-1 flex flex-col overflow-hidden rounded-twc01-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.45_0.06_50/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc01-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative aspect-[4/3] overflow-hidden bg-twc01-mediabg">
          <img src="https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=600&q=80&auto=format&fit=crop" alt="Stainless reusable coffee filter" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute top-2 left-2 inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc01-mono text-[9px] font-extrabold tracking-[0.14em] [background:linear-gradient(180deg,#d1fae5,#a7f3d0)] text-twc01-greenink border border-twc01-greenink/20">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/></svg>
            ECO
          </span>
          <button type="button" aria-label="Add Stainless Reusable Filter to wishlist" class="absolute top-1.5 right-1.5 inline-flex items-center justify-center size-11 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc01-ink cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc01-red hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          </button>
        </div>
        <div class="flex-1 flex flex-col gap-1.5 px-3 pt-2.5 pb-3">
          <h4 class="m-0 text-[12.5px]/[1.3] font-extrabold tracking-[-0.01em] text-twc01-ink line-clamp-2">Stainless Reusable Filter</h4>
          <p class="m-0 text-[10px] font-semibold text-twc01-muted">Barista &amp; Co</p>
          <div class="self-start inline-flex items-center gap-1 px-1.5 py-0.5 rounded-full bg-twc01-amber/10 font-twc01-mono text-[10px] font-extrabold text-twc01-amberink [font-variant-numeric:tabular-nums]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" class="text-twc01-amber" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.6<span class="font-bold text-twc01-dim"> &middot; 89</span>
          </div>
          <div class="flex items-center justify-between gap-2 mt-auto pt-1">
            <span class="text-base font-extrabold tracking-[-0.02em] text-twc01-ink [font-variant-numeric:tabular-nums]">$24</span>
            <button type="button" aria-label="Add Stainless Reusable Filter to cart" class="inline-flex items-center justify-center size-11 rounded-full border-0 cursor-pointer text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_4px_12px_oklch(0_0_0/0.2),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,background] duration-200 hover:-translate-y-px hover:[background:linear-gradient(180deg,#ea580c_0%,#9a3412_100%)] focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
          </div>
        </div>
      </article>

      <article class="group/card flex-1 flex flex-col overflow-hidden rounded-twc01-card bg-white border border-black/6 shadow-[0_12px_30px_-18px_oklch(0.45_0.06_50/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-[3px] hover:border-twc01-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
        <div class="relative aspect-[4/3] overflow-hidden bg-twc01-mediabg">
          <img src="https://images.unsplash.com/photo-1611854779393-1b2da9d400fe?w=600&q=80&auto=format&fit=crop" alt="Single-origin Yirgacheffe coffee bag" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-500 ease-out group-hover/card:scale-105 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
          <span class="absolute top-2 left-2 inline-flex items-center gap-1 px-2 py-[3px] rounded-[5px] font-twc01-mono text-[9px] font-extrabold tracking-[0.14em] bg-twc01-red/90 backdrop-blur-[6px] text-white border border-white/15">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            LIMITED
          </span>
          <button type="button" aria-label="Add Single-Origin Yirgacheffe to wishlist" class="absolute top-1.5 right-1.5 inline-flex items-center justify-center size-11 rounded-full bg-white/92 backdrop-blur-[6px] border border-black/6 text-twc01-ink cursor-pointer transition-[color,background,transform] duration-200 hover:text-twc01-red hover:bg-white hover:scale-105 focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 1 0-7.8 7.8L12 21.1l8.8-8.7a5.5 5.5 0 0 0 0-7.8z"/></svg>
          </button>
        </div>
        <div class="flex-1 flex flex-col gap-1.5 px-3 pt-2.5 pb-3">
          <h4 class="m-0 text-[12.5px]/[1.3] font-extrabold tracking-[-0.01em] text-twc01-ink line-clamp-2">Single-Origin Yirgacheffe</h4>
          <p class="m-0 text-[10px] font-semibold text-twc01-muted">Blue Bottle</p>
          <div class="self-start inline-flex items-center gap-1 px-1.5 py-0.5 rounded-full bg-twc01-amber/10 font-twc01-mono text-[10px] font-extrabold text-twc01-amberink [font-variant-numeric:tabular-nums]">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" class="text-twc01-amber" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.9<span class="font-bold text-twc01-dim"> &middot; 342</span>
          </div>
          <div class="flex items-center justify-between gap-2 mt-auto pt-1">
            <span class="text-base font-extrabold tracking-[-0.02em] text-twc01-ink [font-variant-numeric:tabular-nums]">$32</span>
            <button type="button" aria-label="Add Single-Origin Yirgacheffe to cart" class="inline-flex items-center justify-center size-11 rounded-full border-0 cursor-pointer text-white [background:linear-gradient(180deg,#1e1e2c_0%,#06070c_100%)] shadow-[0_4px_12px_oklch(0_0_0/0.2),inset_0_0_0_1px_oklch(1_0_0/0.14)] transition-[transform,background] duration-200 hover:-translate-y-px hover:[background:linear-gradient(180deg,#ea580c_0%,#9a3412_100%)] focus-visible:outline-2 focus-visible:outline-twc01-ink focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
            </button>
          </div>
        </div>
      </article>

    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc01-bg: #fff8f1;
  --color-twc01-bg: oklch(0.98 0.015 70);
  --color-twc01-bg2: #f4ede4;
  --color-twc01-bg2: oklch(0.94 0.014 75);
  --color-twc01-mediabg: #f5f1e6;
  --color-twc01-mediabg: oklch(0.95 0.018 90);
  --color-twc01-ink: #1a1a1a;
  --color-twc01-ink: oklch(0.21 0.005 270);
  --color-twc01-muted: #6b6459;
  --color-twc01-muted: oklch(0.49 0.015 75);
  --color-twc01-dim: #a1a1aa;
  --color-twc01-dim: oklch(0.7 0.01 285);
  --color-twc01-acc: #ea580c;
  --color-twc01-acc: oklch(0.62 0.19 45);
  --color-twc01-accink: #9a3412;
  --color-twc01-accink: oklch(0.44 0.15 42);
  --color-twc01-amber: #f59e0b;
  --color-twc01-amber: oklch(0.78 0.16 70);
  --color-twc01-amberink: #92400e;
  --color-twc01-amberink: oklch(0.44 0.12 55);
  --color-twc01-green: #10b981;
  --color-twc01-green: oklch(0.72 0.15 163);
  --color-twc01-greenink: #065f46;
  --color-twc01-greenink: oklch(0.43 0.09 165);
  --color-twc01-red: #dc2626;
  --color-twc01-red: oklch(0.58 0.22 25);
  --color-twc01-sage: #7a8471;
  --color-twc01-sage: oklch(0.58 0.03 130);
  --font-twc01-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc01-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --radius-twc01-card: 20px;
  --animate-twc01-pulse: twc01-pulse 2s ease-in-out infinite;
}
/* Keyframes cannot be utilities, so they stay here; --animate-twc01-pulse in
   @theme is what mints animate-twc01-pulse for the two live dots. */

@keyframes twc01-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

.twc-01 {
  width: 100%;
  min-height: 100svh;
}
```
