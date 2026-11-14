---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-e-commerce-product-grid-pagination-with-results-count/"
title: "Tailwind E-commerce Product Grid Pagination with Results Count"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A category-page footer that answers the two questions shoppers actually have — how many are there and where am I — under a product grid that never reflows…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-commerce Product Grid Pagination with Results Count
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-e-commerce-product-grid-pagination-with-results-count/

A category-page footer that answers the two questions shoppers actually have — how many are there and where am I — under a product grid that never reflows while images load. Columns come from grid-cols-[repeat(auto-fill,minmax(13rem,1fr))], every photo is pinned with aspect-4/3, and the number row collapses to a compact Page 1 of 24 through a container query instead of overflowing on phones.
## HTML
```html
<section class="tpg-11 w-full min-h-svh grid place-items-center bg-tpg11-bg bg-[radial-gradient(70%_55%_at_50%_-5%,var(--color-tpg11-glow),transparent_70%)] px-5 py-14 font-tpg11-sans text-tpg11-ink antialiased" aria-label="E-commerce product grid pagination with results count demo">
  <div class="grid w-full max-w-[64rem] justify-items-center gap-8">
    <div class="grid w-full gap-6">
      <header class="flex flex-wrap items-end justify-between gap-x-6 gap-y-3">
        <div>
          <p class="text-xs font-semibold tracking-[0.14em] uppercase text-tpg11-a">Audio &amp; wearables</p>
          <h2 class="mt-1.5 text-[clamp(1.5rem,3.2vw,2rem)] font-semibold tracking-[-0.025em]">Headphones &amp; watches</h2>
        </div>
        <p class="text-sm text-tpg11-mut tabular-nums">Showing <b class="font-semibold text-tpg11-a">1&ndash;4</b> of <b class="font-semibold text-tpg11-ink">96</b> products</p>
      </header>

      <ul class="grid grid-cols-[repeat(auto-fill,minmax(min(13rem,calc(50%_-_0.375rem)),1fr))] gap-3 sm:gap-4" role="list">
        <li class="group relative flex flex-col overflow-hidden rounded-2xl bg-tpg11-card shadow-tpg11-card ring-1 ring-tpg11-line transition-[translate,box-shadow,opacity] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-1 hover:shadow-tpg11-lift starting:translate-y-2 starting:opacity-0 has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-2 has-[a:focus-visible]:outline-tpg11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <div class="relative overflow-hidden bg-tpg11-img">
            <img class="block aspect-4/3 w-full object-cover text-transparent transition-[scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-[1.04] motion-reduce:transition-none" src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=480&amp;h=360&amp;fit=crop&amp;auto=format" alt="Over-ear wireless headphones on a yellow background" width="480" height="360" loading="lazy" decoding="async">
            <span class="absolute top-3 left-3 rounded-full bg-tpg11-card/90 px-2.5 py-1 text-[11px] font-semibold text-tpg11-ink shadow-tpg11-btn ring-1 ring-tpg11-line backdrop-blur">New</span>
          </div>
          <div class="flex flex-1 flex-col gap-1 p-4">
            <p class="text-xs text-tpg11-mut">Halden Audio</p>
            <h3 class="text-[15px] font-semibold tracking-[-0.01em]"><a href="#tpg-11-studio-anc" class="after:absolute after:inset-0 after:rounded-[inherit] focus-visible:outline-none">Studio ANC Headphones</a></h3>
            <p class="text-[13px] text-tpg11-mut">Active noise cancelling &middot; 40 h</p>
            <p class="mt-auto flex flex-wrap items-baseline gap-x-2 gap-y-1 pt-3 tabular-nums"><span class="text-base font-semibold">$249</span><span class="ml-auto font-tpg11-mono text-[11px] whitespace-nowrap text-tpg11-mut">4.8 &middot; 1.2k</span></p>
          </div>
        </li>
        <li class="group relative flex flex-col overflow-hidden rounded-2xl bg-tpg11-card shadow-tpg11-card ring-1 ring-tpg11-line transition-[translate,box-shadow,opacity] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-1 hover:shadow-tpg11-lift starting:translate-y-2 starting:opacity-0 has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-2 has-[a:focus-visible]:outline-tpg11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <div class="relative overflow-hidden bg-tpg11-img">
            <img class="block aspect-4/3 w-full object-cover text-transparent transition-[scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-[1.04] motion-reduce:transition-none" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=480&amp;h=360&amp;fit=crop&amp;auto=format" alt="Minimal analogue watch with a white strap" width="480" height="360" loading="lazy" decoding="async">
            <span class="absolute top-3 left-3 rounded-full bg-linear-to-br from-tpg11-a to-tpg11-b px-2.5 py-1 text-[11px] font-semibold text-tpg11-on-acc tabular-nums shadow-tpg11-pill">&minus;20%</span>
          </div>
          <div class="flex flex-1 flex-col gap-1 p-4">
            <p class="text-xs text-tpg11-mut">Nordvik</p>
            <h3 class="text-[15px] font-semibold tracking-[-0.01em]"><a href="#tpg-11-field-watch" class="after:absolute after:inset-0 after:rounded-[inherit] focus-visible:outline-none">Field Watch 38</a></h3>
            <p class="text-[13px] text-tpg11-mut">Sapphire crystal &middot; 5 ATM</p>
            <p class="mt-auto flex flex-wrap items-baseline gap-x-2 gap-y-1 pt-3 tabular-nums"><span class="text-base font-semibold">$144</span><s class="text-[13px] text-tpg11-mut">$180</s><span class="ml-auto font-tpg11-mono text-[11px] whitespace-nowrap text-tpg11-mut">4.6 &middot; 640</span></p>
          </div>
        </li>
        <li class="group relative flex flex-col overflow-hidden rounded-2xl bg-tpg11-card shadow-tpg11-card ring-1 ring-tpg11-line transition-[translate,box-shadow,opacity] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-1 hover:shadow-tpg11-lift starting:translate-y-2 starting:opacity-0 has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-2 has-[a:focus-visible]:outline-tpg11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <div class="relative overflow-hidden bg-tpg11-img">
            <img class="block aspect-4/3 w-full object-cover text-transparent transition-[scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-[1.04] motion-reduce:transition-none" src="https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=480&amp;h=360&amp;fit=crop&amp;auto=format" alt="Smartwatch with a dark case showing a colourful face" width="480" height="360" loading="lazy" decoding="async">
          </div>
          <div class="flex flex-1 flex-col gap-1 p-4">
            <p class="text-xs text-tpg11-mut">Contour</p>
            <h3 class="text-[15px] font-semibold tracking-[-0.01em]"><a href="#tpg-11-trail-s2" class="after:absolute after:inset-0 after:rounded-[inherit] focus-visible:outline-none">Trail Tracker S2</a></h3>
            <p class="text-[13px] text-tpg11-mut">Dual-band GPS &middot; 7-day battery</p>
            <p class="mt-auto flex flex-wrap items-baseline gap-x-2 gap-y-1 pt-3 tabular-nums"><span class="text-base font-semibold">$329</span><span class="ml-auto font-tpg11-mono text-[11px] whitespace-nowrap text-tpg11-mut">4.7 &middot; 2.3k</span></p>
          </div>
        </li>
        <li class="group relative flex flex-col overflow-hidden rounded-2xl bg-tpg11-card shadow-tpg11-card ring-1 ring-tpg11-line transition-[translate,box-shadow,opacity] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-1 hover:shadow-tpg11-lift starting:translate-y-2 starting:opacity-0 has-[a:focus-visible]:outline-2 has-[a:focus-visible]:outline-offset-2 has-[a:focus-visible]:outline-tpg11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <div class="relative overflow-hidden bg-tpg11-img">
            <img class="block aspect-4/3 w-full object-cover text-transparent transition-[scale] duration-500 ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-[1.04] motion-reduce:transition-none" src="https://images.unsplash.com/photo-1498049794561-7780e7231661?w=480&amp;h=360&amp;fit=crop&amp;auto=format" alt="Headphones, a phone and a notebook arranged on a white desk" width="480" height="360" loading="lazy" decoding="async">
            <span class="absolute top-3 left-3 rounded-full bg-tpg11-card/90 px-2.5 py-1 text-[11px] font-semibold text-tpg11-ink shadow-tpg11-btn ring-1 ring-tpg11-line backdrop-blur">Bundle</span>
          </div>
          <div class="flex flex-1 flex-col gap-1 p-4">
            <p class="text-xs text-tpg11-mut">Halden Audio</p>
            <h3 class="text-[15px] font-semibold tracking-[-0.01em]"><a href="#tpg-11-desk-bundle" class="after:absolute after:inset-0 after:rounded-[inherit] focus-visible:outline-none">Desk Listening Kit</a></h3>
            <p class="text-[13px] text-tpg11-mut">Stand, braided cable, case</p>
            <p class="mt-auto flex flex-wrap items-baseline gap-x-2 gap-y-1 pt-3 tabular-nums"><span class="text-base font-semibold">$74</span><span class="ml-auto font-tpg11-mono text-[11px] whitespace-nowrap text-tpg11-mut">4.9 &middot; 310</span></p>
          </div>
        </li>
      </ul>

      <nav class="@container border-t border-tpg11-line pt-5" aria-label="Pagination">
        <div class="flex items-center justify-between gap-3">
          <a aria-disabled="true" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tpg11-card px-4 text-sm font-medium shadow-tpg11-btn ring-1 ring-tpg11-line transition-[box-shadow,background-color] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring not-aria-disabled:hover:text-tpg11-a not-aria-disabled:hover:ring-tpg11-c1/50 not-aria-disabled:hover:shadow-tpg11-glow aria-disabled:cursor-not-allowed aria-disabled:opacity-45 aria-disabled:shadow-none"><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M10 3.5 5.5 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[22rem]:sr-only">Previous</span></a>
          <ol class="flex items-center gap-1" role="list">
            <li><a href="#tpg-11-p1" aria-current="page" aria-label="Page 1, current page" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-sm font-medium tabular-nums transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg11-c1/10 not-aria-[current=page]:hover:text-tpg11-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg11-a aria-[current=page]:to-tpg11-b aria-[current=page]:font-semibold aria-[current=page]:text-tpg11-on-acc aria-[current=page]:shadow-tpg11-pill @max-[34rem]:hidden">1</a></li>
            <li><a href="#tpg-11-p2" aria-label="Page 2" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-sm font-medium tabular-nums transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg11-c1/10 not-aria-[current=page]:hover:text-tpg11-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg11-a aria-[current=page]:to-tpg11-b aria-[current=page]:font-semibold aria-[current=page]:text-tpg11-on-acc aria-[current=page]:shadow-tpg11-pill @max-[34rem]:hidden">2</a></li>
            <li><a href="#tpg-11-p3" aria-label="Page 3" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-sm font-medium tabular-nums transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg11-c1/10 not-aria-[current=page]:hover:text-tpg11-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg11-a aria-[current=page]:to-tpg11-b aria-[current=page]:font-semibold aria-[current=page]:text-tpg11-on-acc aria-[current=page]:shadow-tpg11-pill @max-[34rem]:hidden">3</a></li>
            <li aria-hidden="true" class="grid min-h-11 w-6 place-items-center text-sm font-semibold text-tpg11-c1 @max-[34rem]:hidden">&hellip;</li>
            <li><a href="#tpg-11-p24" aria-label="Page 24, last page" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-sm font-medium tabular-nums transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg11-c1/10 not-aria-[current=page]:hover:text-tpg11-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg11-a aria-[current=page]:to-tpg11-b aria-[current=page]:font-semibold aria-[current=page]:text-tpg11-on-acc aria-[current=page]:shadow-tpg11-pill @max-[34rem]:hidden">24</a></li>
            <li class="hidden text-sm text-tpg11-mut tabular-nums @max-[34rem]:block">Page <b class="font-semibold text-tpg11-a">1</b> of 24</li>
          </ol>
          <a href="#tpg-11-p2" rel="next" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tpg11-card px-4 text-sm font-medium shadow-tpg11-btn ring-1 ring-tpg11-line transition-[box-shadow,background-color] duration-200 ease-[cubic-bezier(.16,1,.3,1)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg11-ring not-aria-disabled:hover:text-tpg11-a not-aria-disabled:hover:ring-tpg11-c1/50 not-aria-disabled:hover:shadow-tpg11-glow aria-disabled:cursor-not-allowed aria-disabled:opacity-45 aria-disabled:shadow-none"><span class="@max-[22rem]:sr-only">Next</span><svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M6 3.5 10.5 8 6 12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <div class="mx-auto mt-5 grid max-w-56 gap-2 text-center">
          <p class="text-xs text-tpg11-mut tabular-nums">You&rsquo;ve viewed 4 of 96 products</p>
          <div class="h-1 overflow-hidden rounded-full bg-tpg11-c1/12" aria-hidden="true"><div class="h-full w-[4.2%] rounded-full bg-linear-to-r from-tpg11-c1 to-tpg11-c2 shadow-tpg11-bar"></div></div>
        </div>
      </nav>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg11-card px-3.5 py-2 font-tpg11-mono text-[11.5px] text-tpg11-mut ring-1 ring-tpg11-line">auto-fill · aspect-4/3 · @max-[34rem]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg11-bg: #fdf4ec;
  --color-tpg11-bg: oklch(0.972 0.014 64);
  --color-tpg11-glow: #fcd3c4b3;
  --color-tpg11-glow: oklch(0.898 0.051 41 / 0.70);
  --color-tpg11-card: #fffaf6;
  --color-tpg11-card: oklch(0.988 0.008 61);
  --color-tpg11-img: #f7e4d8;
  --color-tpg11-img: oklch(0.931 0.026 55);
  --color-tpg11-ink: #2b1510;
  --color-tpg11-ink: oklch(0.226 0.038 34);
  --color-tpg11-mut: #7d4a3c;
  --color-tpg11-mut: oklch(0.465 0.074 36);
  --color-tpg11-line: #f1dccf;
  --color-tpg11-line: oklch(0.908 0.029 54);
  --color-tpg11-a: #be123c;
  --color-tpg11-a: oklch(0.514 0.198 17);
  --color-tpg11-b: #c2410c;
  --color-tpg11-b: oklch(0.553 0.174 38);
  --color-tpg11-c1: #f43f5e;
  --color-tpg11-c1: oklch(0.645 0.215 16);
  --color-tpg11-c2: #ea580c;
  --color-tpg11-c2: oklch(0.646 0.194 41);
  --color-tpg11-on-acc: #ffffff;
  --color-tpg11-on-acc: oklch(1.000 0.000 0);
  --color-tpg11-ring: #e11d48;
  --color-tpg11-ring: oklch(0.586 0.222 18);
  --font-tpg11-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpg11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tpg11-card: 0 1px 2px oklch(0.45 0.12 30 / 0.06), 0 8px 20px -8px oklch(0.55 0.15 25 / 0.16);
  --shadow-tpg11-lift: 0 2px 4px oklch(0.45 0.12 30 / 0.08), 0 24px 44px -16px oklch(0.6 0.2 20 / 0.35);
  --shadow-tpg11-btn: 0 1px 2px oklch(0.45 0.12 30 / 0.08);
  --shadow-tpg11-glow: 0 6px 18px -8px oklch(0.64 0.21 16 / 0.55);
  --shadow-tpg11-pill: inset 0 1px 0 oklch(1 0 0 / 0.28), 0 2px 4px oklch(0.5 0.2 20 / 0.25), 0 10px 24px -6px oklch(0.64 0.21 22 / 0.6);
  --shadow-tpg11-bar: 0 0 10px oklch(0.64 0.21 16 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-11 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: espresso night — same tokens re-pointed, gradient stops lift to coral and apricot with dark ink on top. */

@media (prefers-color-scheme: dark) {
  .tpg-11:not([data-theme="light"]) {
    --color-tpg11-bg: #1b110d;
    --color-tpg11-bg: oklch(0.190 0.019 43);
    --color-tpg11-glow: #6a231c80;
    --color-tpg11-glow: oklch(0.364 0.103 29 / 0.50);
    --color-tpg11-card: #251813;
    --color-tpg11-card: oklch(0.224 0.023 42);
    --color-tpg11-img: #33221a;
    --color-tpg11-img: oklch(0.270 0.030 46);
    --color-tpg11-ink: #fbeee6;
    --color-tpg11-ink: oklch(0.957 0.018 54);
    --color-tpg11-mut: #cfa898;
    --color-tpg11-mut: oklch(0.762 0.051 43);
    --color-tpg11-line: #3d2a21;
    --color-tpg11-line: oklch(0.305 0.033 46);
    --color-tpg11-a: #fb7185;
    --color-tpg11-a: oklch(0.719 0.169 13);
    --color-tpg11-b: #fdba74;
    --color-tpg11-b: oklch(0.837 0.117 66);
    --color-tpg11-c1: #fb7185;
    --color-tpg11-c1: oklch(0.719 0.169 13);
    --color-tpg11-c2: #fb923c;
    --color-tpg11-c2: oklch(0.758 0.159 56);
    --color-tpg11-on-acc: #2a0a08;
    --color-tpg11-on-acc: oklch(0.200 0.054 27);
    --color-tpg11-ring: #fda4af;
    --color-tpg11-ring: oklch(0.810 0.106 12);
    --shadow-tpg11-card: 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 10px 24px -12px oklch(0 0 0 / 0.7);
    --shadow-tpg11-lift: 0 1px 0 oklch(1 0 0 / 0.07) inset, 0 28px 48px -18px oklch(0.35 0.1 25 / 0.8);
    --shadow-tpg11-btn: 0 1px 0 oklch(1 0 0 / 0.05) inset;
    --shadow-tpg11-glow: 0 6px 20px -8px oklch(0.72 0.17 15 / 0.55);
    --shadow-tpg11-pill: inset 0 1px 0 oklch(1 0 0 / 0.45), 0 0 0 1px oklch(0.72 0.17 15 / 0.35), 0 10px 28px -6px oklch(0.72 0.17 20 / 0.6);
    --shadow-tpg11-bar: 0 0 12px oklch(0.72 0.17 15 / 0.7);
  }
}

.tpg-11[data-theme="dark"] {
  --color-tpg11-bg: #1b110d;
  --color-tpg11-bg: oklch(0.190 0.019 43);
  --color-tpg11-glow: #6a231c80;
  --color-tpg11-glow: oklch(0.364 0.103 29 / 0.50);
  --color-tpg11-card: #251813;
  --color-tpg11-card: oklch(0.224 0.023 42);
  --color-tpg11-img: #33221a;
  --color-tpg11-img: oklch(0.270 0.030 46);
  --color-tpg11-ink: #fbeee6;
  --color-tpg11-ink: oklch(0.957 0.018 54);
  --color-tpg11-mut: #cfa898;
  --color-tpg11-mut: oklch(0.762 0.051 43);
  --color-tpg11-line: #3d2a21;
  --color-tpg11-line: oklch(0.305 0.033 46);
  --color-tpg11-a: #fb7185;
  --color-tpg11-a: oklch(0.719 0.169 13);
  --color-tpg11-b: #fdba74;
  --color-tpg11-b: oklch(0.837 0.117 66);
  --color-tpg11-c1: #fb7185;
  --color-tpg11-c1: oklch(0.719 0.169 13);
  --color-tpg11-c2: #fb923c;
  --color-tpg11-c2: oklch(0.758 0.159 56);
  --color-tpg11-on-acc: #2a0a08;
  --color-tpg11-on-acc: oklch(0.200 0.054 27);
  --color-tpg11-ring: #fda4af;
  --color-tpg11-ring: oklch(0.810 0.106 12);
  --shadow-tpg11-card: 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 10px 24px -12px oklch(0 0 0 / 0.7);
  --shadow-tpg11-lift: 0 1px 0 oklch(1 0 0 / 0.07) inset, 0 28px 48px -18px oklch(0.35 0.1 25 / 0.8);
  --shadow-tpg11-btn: 0 1px 0 oklch(1 0 0 / 0.05) inset;
  --shadow-tpg11-glow: 0 6px 20px -8px oklch(0.72 0.17 15 / 0.55);
  --shadow-tpg11-pill: inset 0 1px 0 oklch(1 0 0 / 0.45), 0 0 0 1px oklch(0.72 0.17 15 / 0.35), 0 10px 28px -6px oklch(0.72 0.17 20 / 0.6);
  --shadow-tpg11-bar: 0 0 12px oklch(0.72 0.17 15 / 0.7);
}
```
