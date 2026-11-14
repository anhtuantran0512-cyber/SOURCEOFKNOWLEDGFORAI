---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-dashboard-kpi-stat-cards-grid/"
title: "Tailwind CSS Dashboard KPI Stat Cards Grid"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Four KPI cards that flow 4 → 2 → 1 columns from the width of their own container (@min-[34rem]/kpi:grid-cols-2 @min-[60rem]/kpi:grid-cols-4) &mdash; never…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Dashboard KPI Stat Cards Grid
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-dashboard-kpi-stat-cards-grid/

Four KPI cards that flow 4 → 2 → 1 columns from the width of their own container (@min-[34rem]/kpi:grid-cols-2 @min-[60rem]/kpi:grid-cols-4) &mdash; never the orphaned 3 + 1 row that auto-fit produces. New in the port: a working 7d / 28d / 90d range switch built from a radio group, where group-has-[#tdl03-7:checked]/kpi:inline swaps every value, delta and sparkline with zero JavaScript.
## HTML
```html
<section class="tdl-03 w-full min-h-svh bg-tdl03-bg bg-linear-175 from-tdl03-bg to-tdl03-bg2 font-tdl03-sans text-tdl03-ink antialiased" aria-label="KPI card grid demo">
  <div class="group/kpi @container/kpi mx-auto grid min-h-svh w-full max-w-6xl content-center gap-5 p-4 sm:p-8">
    <header class="flex flex-wrap items-end justify-between gap-3">
      <div><p class="text-[12px] font-semibold tracking-[0.12em] text-tdl03-acc uppercase">Storefront</p><h2 class="text-2xl font-bold tracking-tight">Performance</h2></div>
      <fieldset class="flex rounded-xl border border-tdl03-edge bg-tdl03-track p-1 *:relative *:grid *:h-9 *:min-w-14 *:cursor-pointer *:place-items-center *:rounded-lg *:px-3 *:text-[13px] *:font-semibold *:text-tdl03-mut *:transition *:has-checked:bg-tdl03-panel *:has-checked:text-tdl03-ink *:has-checked:shadow-[0_1px_3px_oklch(0.3_0.03_200/0.18)] *:has-focus-visible:outline-2 *:has-focus-visible:outline-tdl03-acc">
        <legend class="sr-only">Date range</legend>
        <label><input class="sr-only" type="radio" name="tdl03-range" id="tdl03-7">7d</label>
        <label><input class="sr-only" type="radio" name="tdl03-range" id="tdl03-28" checked>28d</label>
        <label><input class="sr-only" type="radio" name="tdl03-range" id="tdl03-90">90d</label>
      </fieldset>
    </header>
    <div class="grid grid-cols-1 gap-4 @min-[34rem]/kpi:grid-cols-2 @min-[60rem]/kpi:grid-cols-4">
      <article class="flex flex-col gap-1.5 rounded-2xl border border-tdl03-edge bg-tdl03-panel p-5 transition duration-200 hover:-translate-y-0.75 hover:border-tdl03-acc/50 hover:shadow-[0_14px_30px_-18px_var(--color-tdl03-shadow)]">
        <h3 class="text-[11px] font-semibold tracking-[0.11em] text-tdl03-mut uppercase">Revenue</h3>
        <p class="text-[30px] font-bold tracking-[-0.02em] tabular-nums"><span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">$21,980</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">$86,410</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">$251,300</span></p>
        <p class="flex items-center gap-2 text-[11.5px]"><span class="rounded-full bg-tdl03-good/13 px-2.25 py-0.75 font-bold text-tdl03-good tabular-nums"><span class="sr-only">Up </span>▲ <span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">4.2%</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">12.4%</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">18.9%</span></span><span class="text-tdl03-mut">vs prior period</span></p>
        <div aria-hidden="true" class="mt-3 flex h-12 items-end gap-1.25 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-tdl03-acc/40 *:animate-tdl03-rise [&>i:last-child]:bg-tdl03-acc"><i style="--h:38%"></i><i style="--h:52%;animation-delay:60ms"></i><i style="--h:46%;animation-delay:120ms"></i><i style="--h:64%;animation-delay:180ms"></i><i style="--h:58%;animation-delay:240ms"></i><i style="--h:78%;animation-delay:300ms"></i><i style="--h:100%;animation-delay:360ms"></i></div>
      </article>
      <article class="flex flex-col gap-1.5 rounded-2xl border border-tdl03-edge bg-tdl03-panel p-5 transition duration-200 hover:-translate-y-0.75 hover:border-tdl03-acc/50 hover:shadow-[0_14px_30px_-18px_var(--color-tdl03-shadow)]">
        <h3 class="text-[11px] font-semibold tracking-[0.11em] text-tdl03-mut uppercase">Orders</h3>
        <p class="text-[30px] font-bold tracking-[-0.02em] tabular-nums"><span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">1,072</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">4,203</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">12,880</span></p>
        <p class="flex items-center gap-2 text-[11.5px]"><span class="rounded-full bg-tdl03-good/13 px-2.25 py-0.75 font-bold text-tdl03-good tabular-nums"><span class="sr-only">Up </span>▲ <span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">1.8%</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">3.1%</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">7.6%</span></span><span class="text-tdl03-mut">vs prior period</span></p>
        <div aria-hidden="true" class="mt-3 flex h-12 items-end gap-1.25 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-tdl03-acc/40 *:animate-tdl03-rise [&>i:last-child]:bg-tdl03-acc"><i style="--h:55%"></i><i style="--h:48%;animation-delay:60ms"></i><i style="--h:66%;animation-delay:120ms"></i><i style="--h:60%;animation-delay:180ms"></i><i style="--h:74%;animation-delay:240ms"></i><i style="--h:69%;animation-delay:300ms"></i><i style="--h:88%;animation-delay:360ms"></i></div>
      </article>
      <article class="flex flex-col gap-1.5 rounded-2xl border border-tdl03-edge bg-tdl03-panel p-5 transition duration-200 hover:-translate-y-0.75 hover:border-tdl03-acc/50 hover:shadow-[0_14px_30px_-18px_var(--color-tdl03-shadow)]">
        <h3 class="text-[11px] font-semibold tracking-[0.11em] text-tdl03-mut uppercase">Conversion rate</h3>
        <p class="text-[30px] font-bold tracking-[-0.02em] tabular-nums"><span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">3.31%</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">3.42%</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">3.58%</span></p>
        <p class="flex items-center gap-2 text-[11.5px]"><span class="rounded-full bg-tdl03-bad/12 px-2.25 py-0.75 font-bold text-tdl03-bad tabular-nums"><span class="sr-only">Down </span>▼ <span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">0.6 pts</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">0.4 pts</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">0.1 pts</span></span><span class="text-tdl03-mut">vs prior period</span></p>
        <div aria-hidden="true" class="mt-3 flex h-12 items-end gap-1.25 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-tdl03-bad/30 *:animate-tdl03-rise [&>i:last-child]:bg-tdl03-bad"><i style="--h:82%"></i><i style="--h:74%;animation-delay:60ms"></i><i style="--h:88%;animation-delay:120ms"></i><i style="--h:70%;animation-delay:180ms"></i><i style="--h:64%;animation-delay:240ms"></i><i style="--h:58%;animation-delay:300ms"></i><i style="--h:52%;animation-delay:360ms"></i></div>
      </article>
      <article class="flex flex-col gap-1.5 rounded-2xl border border-tdl03-edge bg-tdl03-panel p-5 transition duration-200 hover:-translate-y-0.75 hover:border-tdl03-acc/50 hover:shadow-[0_14px_30px_-18px_var(--color-tdl03-shadow)]">
        <h3 class="text-[11px] font-semibold tracking-[0.11em] text-tdl03-mut uppercase">Avg. order value</h3>
        <p class="text-[30px] font-bold tracking-[-0.02em] tabular-nums"><span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">$20.50</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">$20.56</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">$19.51</span></p>
        <p class="flex items-center gap-2 text-[11.5px]"><span class="rounded-full bg-tdl03-good/13 px-2.25 py-0.75 font-bold text-tdl03-good tabular-nums"><span class="sr-only">Up </span>▲ <span class="hidden group-has-[#tdl03-7:checked]/kpi:inline">2.3%</span><span class="hidden group-has-[#tdl03-28:checked]/kpi:inline">5.8%</span><span class="hidden group-has-[#tdl03-90:checked]/kpi:inline">4.4%</span></span><span class="text-tdl03-mut">vs prior period</span></p>
        <div aria-hidden="true" class="mt-3 flex h-12 items-end gap-1.25 *:h-(--h) *:flex-1 *:origin-bottom *:rounded-t-[3px] *:bg-tdl03-acc/40 *:animate-tdl03-rise [&>i:last-child]:bg-tdl03-acc"><i style="--h:44%"></i><i style="--h:58%;animation-delay:60ms"></i><i style="--h:50%;animation-delay:120ms"></i><i style="--h:62%;animation-delay:180ms"></i><i style="--h:70%;animation-delay:240ms"></i><i style="--h:66%;animation-delay:300ms"></i><i style="--h:80%;animation-delay:360ms"></i></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl03-bg: #f5f9f9;
  --color-tdl03-bg: oklch(0.977 0.006 190);
  --color-tdl03-bg2: #ebf2f2;
  --color-tdl03-bg2: oklch(0.955 0.01 190);
  --color-tdl03-track: #e5eded;
  --color-tdl03-track: oklch(0.935 0.01 190);
  --color-tdl03-panel: #ffffff;
  --color-tdl03-panel: oklch(1 0 0);
  --color-tdl03-edge: #dbe5e5;
  --color-tdl03-edge: oklch(0.91 0.012 190);
  --color-tdl03-ink: #1d2d31;
  --color-tdl03-ink: oklch(0.27 0.025 210);
  --color-tdl03-mut: #55666a;
  --color-tdl03-mut: oklch(0.49 0.02 210);
  --color-tdl03-acc: #00899a;
  --color-tdl03-acc: oklch(0.57 0.11 205);
  --color-tdl03-good: #18804a;
  --color-tdl03-good: oklch(0.52 0.13 155);
  --color-tdl03-bad: #c8352f;
  --color-tdl03-bad: oklch(0.56 0.19 25);
  --color-tdl03-shadow: #4f7f86;
  --color-tdl03-shadow: oklch(0.45 0.06 205 / 0.55);
  --font-tdl03-sans: 'Instrument Sans', system-ui, sans-serif;
  --animate-tdl03-rise: tdl03-rise 0.6s cubic-bezier(0.2,0.7,0.2,1) backwards;

  @keyframes tdl03-rise {
    from {
      scale: 1 0;
    }
  }
}

.tdl-03 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-03 * {
    animation: none !important;
    transition: none !important;
  }
}
```
