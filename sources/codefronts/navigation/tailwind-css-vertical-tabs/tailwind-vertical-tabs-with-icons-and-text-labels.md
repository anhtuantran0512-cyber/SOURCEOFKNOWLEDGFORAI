---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-icons-and-text-labels/"
title: "Tailwind Vertical Tabs with Icons and Text Labels"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "An analytics dashboard sidebar where every tab is an inline SVG icon plus a text label, styled entirely through currentColor: hover, active and focus…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Tabs with Icons and Text Labels
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-vertical-tabs-with-icons-and-text-labels/

An analytics dashboard sidebar where every tab is an inline SVG icon plus a text label, styled entirely through currentColor: hover, active and focus recolour the icon with zero icon-specific CSS. The active icon draws itself with a stroke-dashoffset sweep (pathLength="1" makes one keyframe fit every icon), count badges pin right, and on narrow cards the rail becomes a horizontally scrolling chip row.
## HTML
```html
<section class="tvt-03 w-full min-h-svh grid place-items-center bg-tvt03-bg bg-[radial-gradient(80%_60%_at_50%_100%,var(--color-tvt03-halo),transparent_70%)] px-4 py-14 font-tvt03-sans text-tvt03-ink antialiased sm:px-6" aria-label="Tailwind vertical tabs with icons and text labels demo">
  <div class="grid w-full max-w-[60rem] justify-items-center gap-6">
    <header class="grid justify-items-center gap-2.5 text-center">
      <p class="font-tvt03-mono text-[11.5px] font-medium tracking-[0.16em] text-tvt03-acc-ink uppercase">Icon + label · currentColor</p>
      <h2 class="text-[clamp(28px,4.2vw,42px)] leading-[1.05] font-extrabold tracking-[-0.04em] text-balance">Sidebar tabs that <span class="bg-linear-to-r from-tvt03-acc-ink to-tvt03-acc2 bg-clip-text pe-1 text-transparent">draw themselves</span></h2>
    </header>
    <div class="@container w-full">
    <div class="group/card grid w-full grid-cols-[15.5rem_minmax(0,1fr)] overflow-hidden rounded-[24px] bg-tvt03-card shadow-tvt03-card ring-1 ring-tvt03-line starting:scale-[0.98] starting:opacity-0 transition-[opacity,scale] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none @max-[44rem]:grid-cols-1">
      <nav aria-label="Workspace" class="relative flex flex-col gap-1 overflow-hidden bg-tvt03-rail bg-[radial-gradient(120%_60%_at_0%_0%,var(--color-tvt03-rail-glow),transparent_70%)] p-3.5 @max-[44rem]:p-2.5">
        <p class="flex items-center gap-2.5 px-2 pt-1.5 pb-4 text-[15px] font-extrabold tracking-[-0.02em] text-tvt03-rail-ink @max-[44rem]:hidden"><span aria-hidden="true" class="grid size-8 place-items-center rounded-lg bg-linear-to-br from-tvt03-acc to-tvt03-acc2 text-tvt03-rail shadow-[0_0_20px_-4px] shadow-tvt03-acc"><svg viewBox="0 0 20 20" width="16" height="16" focusable="false"><path d="M4 15 8 9l3 3 5-7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>Northwind</p>
        <p class="px-3 pb-1.5 text-[11px] font-bold tracking-[0.14em] text-tvt03-rail-mut uppercase @max-[44rem]:hidden">Main</p>
        <div role="radiogroup" aria-label="Workspace sections" class="flex flex-col gap-1 @max-[44rem]:flex-row @max-[44rem]:snap-x @max-[44rem]:overflow-x-auto @max-[44rem]:[scrollbar-width:none] @max-[44rem]:[mask-image:linear-gradient(to_right,black_82%,transparent)]">

          <input type="radio" name="tvt-03-nav" id="tvt-03-t1" class="sr-only" checked>
          <label for="tvt-03-t1" class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14.5px] font-semibold text-tvt03-rail-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-white/[0.06] hover:text-tvt03-rail-ink [:checked+&]:bg-white/[0.09] [:checked+&]:text-tvt03-rail-ink [:checked+&]:shadow-tvt03-tab [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt03-glow motion-reduce:transition-none @max-[44rem]:snap-start @max-[44rem]:pe-3.5">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" class="size-5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-dasharray:1] transition-[scale,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] [:checked+*_&]:scale-110 [:checked+*_&]:animate-tvt03-draw [:checked+*_&]:text-tvt03-glow motion-reduce:transition-none motion-reduce:[:checked+*_&]:animate-none"><path pathLength="1" d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" stroke-linejoin="round"/></svg>
            <span class="flex-1 whitespace-nowrap">Dashboard</span><span class="rounded-full bg-tvt03-glow/15 px-2 py-0.5 font-tvt03-mono text-[11px] font-semibold text-tvt03-glow tabular-nums">4</span>
          </label>

          <input type="radio" name="tvt-03-nav" id="tvt-03-t2" class="sr-only">
          <label for="tvt-03-t2" class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14.5px] font-semibold text-tvt03-rail-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-white/[0.06] hover:text-tvt03-rail-ink [:checked+&]:bg-white/[0.09] [:checked+&]:text-tvt03-rail-ink [:checked+&]:shadow-tvt03-tab [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt03-glow motion-reduce:transition-none @max-[44rem]:snap-start @max-[44rem]:pe-3.5">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" class="size-5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-dasharray:1] transition-[scale,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] [:checked+*_&]:scale-110 [:checked+*_&]:animate-tvt03-draw [:checked+*_&]:text-tvt03-glow motion-reduce:transition-none motion-reduce:[:checked+*_&]:animate-none"><path pathLength="1" d="M4 19V5m0 14h16" stroke-linecap="round"/><path pathLength="1" d="M8 16V9m4 7V6m4 10v-4" stroke-linecap="round"/></svg>
            <span class="flex-1 whitespace-nowrap">Analytics</span><span class="rounded-full bg-white/10 px-2 py-0.5 text-[10.5px] font-bold tracking-[0.06em] text-tvt03-rail-ink uppercase">New</span>
          </label>

          <input type="radio" name="tvt-03-nav" id="tvt-03-t3" class="sr-only">
          <label for="tvt-03-t3" class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14.5px] font-semibold text-tvt03-rail-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-white/[0.06] hover:text-tvt03-rail-ink [:checked+&]:bg-white/[0.09] [:checked+&]:text-tvt03-rail-ink [:checked+&]:shadow-tvt03-tab [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt03-glow motion-reduce:transition-none @max-[44rem]:snap-start @max-[44rem]:pe-3.5">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" class="size-5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-dasharray:1] transition-[scale,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] [:checked+*_&]:scale-110 [:checked+*_&]:animate-tvt03-draw [:checked+*_&]:text-tvt03-glow motion-reduce:transition-none motion-reduce:[:checked+*_&]:animate-none"><circle pathLength="1" cx="9" cy="8" r="3.2"/><path pathLength="1" d="M3 20a6 6 0 0 1 12 0m2.5-11.6a3 3 0 0 1 0 5.9M18 20a5.6 5.6 0 0 0-2-4.2" stroke-linecap="round"/></svg>
            <span class="flex-1 whitespace-nowrap">Audience</span>
          </label>

          <input type="radio" name="tvt-03-nav" id="tvt-03-t4" class="sr-only">
          <label for="tvt-03-t4" class="group/tab relative flex min-h-11 shrink-0 cursor-pointer items-center gap-3 rounded-xl px-3 text-[14.5px] font-semibold text-tvt03-rail-mut transition-[background-color,color,box-shadow] duration-200 select-none hover:bg-white/[0.06] hover:text-tvt03-rail-ink [:checked+&]:bg-white/[0.09] [:checked+&]:text-tvt03-rail-ink [:checked+&]:shadow-tvt03-tab [:focus-visible+&]:outline-2 [:focus-visible+&]:outline-offset-2 [:focus-visible+&]:outline-tvt03-glow motion-reduce:transition-none @max-[44rem]:snap-start @max-[44rem]:pe-3.5">
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" class="size-5 shrink-0 fill-none stroke-current stroke-[1.7] [stroke-dasharray:1] transition-[scale,color] duration-300 ease-[cubic-bezier(.34,1.4,.5,1)] [:checked+*_&]:scale-110 [:checked+*_&]:animate-tvt03-draw [:checked+*_&]:text-tvt03-glow motion-reduce:transition-none motion-reduce:[:checked+*_&]:animate-none"><circle pathLength="1" cx="12" cy="12" r="3"/><path pathLength="1" d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7" stroke-linecap="round"/></svg>
            <span class="flex-1 whitespace-nowrap">Settings</span>
          </label>
        </div>
        <div class="mt-auto flex items-center gap-3 rounded-2xl bg-white/[0.06] p-3 ring-1 ring-white/10 @max-[44rem]:hidden">
          <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-linear-to-br from-[oklch(0.78_0.14_75)] to-[oklch(0.65_0.18_40)] text-[12px] font-bold text-white">EH</span>
          <div class="min-w-0 leading-tight"><p class="truncate text-[13.5px] font-semibold text-tvt03-rail-ink">Emma Hart</p><p class="truncate text-[12px] text-tvt03-rail-mut">Growth lead</p></div>
        </div>
      </nav>

      <div class="grid min-h-[26rem] p-6 sm:p-8 @max-[44rem]:min-h-0 @max-[44rem]:p-5">

          <article id="tvt-03-p1" aria-labelledby="tvt-03-h1" class="invisible col-start-1 row-start-1 translate-x-3 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-03-t1:checked]/card:visible group-has-[#tvt-03-t1:checked]/card:translate-x-0 group-has-[#tvt-03-t1:checked]/card:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <p class="font-tvt03-mono text-[11.5px] text-tvt03-mut">Northwind <span aria-hidden="true">/</span> Dashboard</p>
                <h3 id="tvt-03-h1" class="mt-1 text-[clamp(21px,2.5vw,26px)] font-extrabold tracking-[-0.03em]">Dashboard</h3>
              </div>
              <span class="inline-flex items-center gap-2 rounded-lg bg-tvt03-sub px-3 py-1.5 text-[12.5px] font-semibold text-tvt03-mut ring-1 ring-tvt03-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="3" y="4.5" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 8.5h14M7 3v3M13 3v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Last 30 days</span>
            </div>
            <dl class="mt-6 grid grid-cols-3 gap-3 @max-[44rem]:grid-cols-2">
              <div class="rounded-2xl bg-tvt03-sub p-4 ring-1 ring-tvt03-line @max-[44rem]:col-span-2"><dt class="text-[12.5px] font-semibold text-tvt03-mut">Revenue</dt><dd class="mt-1 flex items-baseline gap-2"><span class="text-[26px] font-extrabold tracking-[-0.03em] tabular-nums">$84.2k</span><span class="text-[12.5px] font-bold text-tvt03-acc-ink">↑ 12.4%</span></dd></div>
              <div class="rounded-2xl bg-tvt03-sub p-4 ring-1 ring-tvt03-line"><dt class="text-[12.5px] font-semibold text-tvt03-mut">Orders</dt><dd class="mt-1 text-[26px] font-extrabold tracking-[-0.03em] tabular-nums">1,284</dd></div>
              <div class="rounded-2xl bg-tvt03-sub p-4 ring-1 ring-tvt03-line"><dt class="text-[12.5px] font-semibold text-tvt03-mut">Conversion</dt><dd class="mt-1 text-[26px] font-extrabold tracking-[-0.03em] tabular-nums">3.8%</dd></div>
            </dl>
            <figure class="mt-3 rounded-2xl p-4 ring-1 ring-tvt03-line">
              <figcaption class="flex justify-between text-[13px] font-semibold"><span>Monthly revenue</span><span class="text-tvt03-mut">Nov – Oct</span></figcaption>
              <svg viewBox="0 0 300 100" class="mt-3 h-28 w-full" preserveAspectRatio="none" role="img" aria-label="Revenue rose from 38 to 96 thousand dollars over twelve months"><defs><linearGradient id="tvt-03-bar" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="var(--color-tvt03-acc)"/><stop offset="1" stop-color="var(--color-tvt03-acc2)"/></linearGradient></defs><rect x="3" y="62" width="17" height="38" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="28" y="48" width="17" height="52" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="53" y="56" width="17" height="44" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="78" y="39" width="17" height="61" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="103" y="43" width="17" height="57" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="128" y="30" width="17" height="70" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="153" y="36" width="17" height="64" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="178" y="21" width="17" height="79" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="203" y="28" width="17" height="72" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="228" y="12" width="17" height="88" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="253" y="19" width="17" height="81" rx="4" fill="url(#tvt-03-bar)" opacity=".55"/><rect x="278" y="4" width="17" height="96" rx="4" fill="url(#tvt-03-bar)"/></svg>
            </figure>
          </article>

          <article id="tvt-03-p2" aria-labelledby="tvt-03-h2" class="invisible col-start-1 row-start-1 translate-x-3 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-03-t2:checked]/card:visible group-has-[#tvt-03-t2:checked]/card:translate-x-0 group-has-[#tvt-03-t2:checked]/card:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <p class="font-tvt03-mono text-[11.5px] text-tvt03-mut">Northwind <span aria-hidden="true">/</span> Analytics</p>
                <h3 id="tvt-03-h2" class="mt-1 text-[clamp(21px,2.5vw,26px)] font-extrabold tracking-[-0.03em]">Analytics</h3>
              </div>
              <span class="inline-flex items-center gap-2 rounded-lg bg-tvt03-sub px-3 py-1.5 text-[12.5px] font-semibold text-tvt03-mut ring-1 ring-tvt03-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="3" y="4.5" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 8.5h14M7 3v3M13 3v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Last 30 days</span>
            </div>
            <p class="mt-2 max-w-[50ch] text-[14.5px] leading-relaxed text-tvt03-mut">Checkout funnel for the autumn collection. Cart → checkout is the step to fix.</p>
            <ol class="mt-5 grid gap-3">
              <li class="grid gap-1.5"><p class="flex justify-between text-[13.5px]"><span class="font-semibold">Visitors</span><span class="font-tvt03-mono text-tvt03-mut tabular-nums">48,210 · 100%</span></p><span class="block h-3 overflow-hidden rounded-full bg-tvt03-sub ring-1 ring-tvt03-line"><span class="block h-full rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2 w-[100%] opacity-100"></span></span></li>
              <li class="grid gap-1.5"><p class="flex justify-between text-[13.5px]"><span class="font-semibold">Product views</span><span class="font-tvt03-mono text-tvt03-mut tabular-nums">21,904 · 45%</span></p><span class="block h-3 overflow-hidden rounded-full bg-tvt03-sub ring-1 ring-tvt03-line"><span class="block h-full rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2 w-[45%] opacity-85"></span></span></li>
              <li class="grid gap-1.5"><p class="flex justify-between text-[13.5px]"><span class="font-semibold">Added to cart</span><span class="font-tvt03-mono text-tvt03-mut tabular-nums">6,380 · 13%</span></p><span class="block h-3 overflow-hidden rounded-full bg-tvt03-sub ring-1 ring-tvt03-line"><span class="block h-full rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2 w-[13%] opacity-70"></span></span></li>
              <li class="grid gap-1.5"><p class="flex justify-between text-[13.5px]"><span class="font-semibold">Checkout</span><span class="font-tvt03-mono text-tvt03-mut tabular-nums">2,410 · 5%</span></p><span class="block h-3 overflow-hidden rounded-full bg-tvt03-sub ring-1 ring-tvt03-line"><span class="block h-full rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2 w-[5%] opacity-55"></span></span></li>
            </ol>
          </article>

          <article id="tvt-03-p3" aria-labelledby="tvt-03-h3" class="invisible col-start-1 row-start-1 translate-x-3 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-03-t3:checked]/card:visible group-has-[#tvt-03-t3:checked]/card:translate-x-0 group-has-[#tvt-03-t3:checked]/card:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <p class="font-tvt03-mono text-[11.5px] text-tvt03-mut">Northwind <span aria-hidden="true">/</span> Audience</p>
                <h3 id="tvt-03-h3" class="mt-1 text-[clamp(21px,2.5vw,26px)] font-extrabold tracking-[-0.03em]">Audience</h3>
              </div>
              <span class="inline-flex items-center gap-2 rounded-lg bg-tvt03-sub px-3 py-1.5 text-[12.5px] font-semibold text-tvt03-mut ring-1 ring-tvt03-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="3" y="4.5" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 8.5h14M7 3v3M13 3v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Last 30 days</span>
            </div>
            <p class="mt-2 text-[14.5px] text-tvt03-mut">Top markets by sessions · 61.4k total</p>
            <ul class="mt-5 divide-y divide-tvt03-line rounded-2xl ring-1 ring-tvt03-line">
              <li class="flex items-center gap-3 px-4 py-3"><span class="grid h-7 w-9 shrink-0 place-items-center rounded-md bg-tvt03-sub font-tvt03-mono text-[11.5px] font-semibold text-tvt03-acc-ink ring-1 ring-tvt03-line">US</span><span class="min-w-0 flex-1 truncate text-[14px] font-semibold">United States</span><span aria-hidden="true" class="hidden h-1.5 w-28 overflow-hidden rounded-full bg-tvt03-sub sm:block"><span class="block h-full rounded-full bg-tvt03-acc w-[84%]"></span></span><span class="w-10 text-end font-tvt03-mono text-[13px] tabular-nums">42%</span></li>
              <li class="flex items-center gap-3 px-4 py-3"><span class="grid h-7 w-9 shrink-0 place-items-center rounded-md bg-tvt03-sub font-tvt03-mono text-[11.5px] font-semibold text-tvt03-acc-ink ring-1 ring-tvt03-line">GB</span><span class="min-w-0 flex-1 truncate text-[14px] font-semibold">United Kingdom</span><span aria-hidden="true" class="hidden h-1.5 w-28 overflow-hidden rounded-full bg-tvt03-sub sm:block"><span class="block h-full rounded-full bg-tvt03-acc w-[36%]"></span></span><span class="w-10 text-end font-tvt03-mono text-[13px] tabular-nums">18%</span></li>
              <li class="flex items-center gap-3 px-4 py-3"><span class="grid h-7 w-9 shrink-0 place-items-center rounded-md bg-tvt03-sub font-tvt03-mono text-[11.5px] font-semibold text-tvt03-acc-ink ring-1 ring-tvt03-line">CA</span><span class="min-w-0 flex-1 truncate text-[14px] font-semibold">Canada</span><span aria-hidden="true" class="hidden h-1.5 w-28 overflow-hidden rounded-full bg-tvt03-sub sm:block"><span class="block h-full rounded-full bg-tvt03-acc w-[22%]"></span></span><span class="w-10 text-end font-tvt03-mono text-[13px] tabular-nums">11%</span></li>
              <li class="flex items-center gap-3 px-4 py-3"><span class="grid h-7 w-9 shrink-0 place-items-center rounded-md bg-tvt03-sub font-tvt03-mono text-[11.5px] font-semibold text-tvt03-acc-ink ring-1 ring-tvt03-line">AU</span><span class="min-w-0 flex-1 truncate text-[14px] font-semibold">Australia</span><span aria-hidden="true" class="hidden h-1.5 w-28 overflow-hidden rounded-full bg-tvt03-sub sm:block"><span class="block h-full rounded-full bg-tvt03-acc w-[18%]"></span></span><span class="w-10 text-end font-tvt03-mono text-[13px] tabular-nums">9%</span></li>
            </ul>
          </article>

          <article id="tvt-03-p4" aria-labelledby="tvt-03-h4" class="invisible col-start-1 row-start-1 translate-x-3 opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-03-t4:checked]/card:visible group-has-[#tvt-03-t4:checked]/card:translate-x-0 group-has-[#tvt-03-t4:checked]/card:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center justify-between gap-3">
              <div>
                <p class="font-tvt03-mono text-[11.5px] text-tvt03-mut">Northwind <span aria-hidden="true">/</span> Settings</p>
                <h3 id="tvt-03-h4" class="mt-1 text-[clamp(21px,2.5vw,26px)] font-extrabold tracking-[-0.03em]">Settings</h3>
              </div>
              <span class="inline-flex items-center gap-2 rounded-lg bg-tvt03-sub px-3 py-1.5 text-[12.5px] font-semibold text-tvt03-mut ring-1 ring-tvt03-line"><svg viewBox="0 0 20 20" width="14" height="14" aria-hidden="true" focusable="false"><rect x="3" y="4.5" width="14" height="12" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M3 8.5h14M7 3v3M13 3v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Last 30 days</span>
            </div>
            <ul class="mt-6 divide-y divide-tvt03-line rounded-2xl ring-1 ring-tvt03-line">
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Weekly digest</p><p class="text-[12.5px] text-tvt03-mut">Monday 8am, your time zone</p></div><span aria-hidden="true" class="relative h-6 w-10 shrink-0 rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2"><span class="absolute top-0.5 end-0.5 size-5 rounded-full bg-white shadow-[0_1px_3px_oklch(0_0_0/0.3)]"></span></span></li>
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Anomaly alerts</p><p class="text-[12.5px] text-tvt03-mut">Email when revenue moves ±20%</p></div><span aria-hidden="true" class="relative h-6 w-10 shrink-0 rounded-full bg-linear-to-r from-tvt03-acc to-tvt03-acc2"><span class="absolute top-0.5 end-0.5 size-5 rounded-full bg-white shadow-[0_1px_3px_oklch(0_0_0/0.3)]"></span></span></li>
              <li class="flex items-center gap-4 px-4 py-3.5"><div class="min-w-0 flex-1"><p class="text-[14px] font-semibold">Share with workspace</p><p class="text-[12.5px] text-tvt03-mut">Let editors see this dashboard</p></div><span aria-hidden="true" class="relative h-6 w-10 shrink-0 rounded-full bg-tvt03-line"><span class="absolute top-0.5 start-0.5 size-5 rounded-full bg-white shadow-[0_1px_3px_oklch(0_0_0/0.3)]"></span></span></li>
            </ul>
            <p class="mt-4 text-[12.5px] text-tvt03-mut">Data retention: <b class="font-semibold text-tvt03-ink">25 months</b> · GDPR region <b class="font-semibold text-tvt03-ink">EU-West</b></p>
          </article>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt03-card px-3.5 py-2 text-center font-tvt03-mono text-[11.5px] text-tvt03-mut ring-1 ring-tvt03-line">shrink-0 · stroke-current · pathLength="1"</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt03-bg: #eaf7f2;
  --color-tvt03-bg: oklch(0.966 0.016 168);
  --color-tvt03-halo: #a9e7d099;
  --color-tvt03-halo: oklch(0.88 0.07 170 / 0.6);
  --color-tvt03-card: #fcfffe;
  --color-tvt03-card: oklch(0.997 0.003 165);
  --color-tvt03-sub: #f1f9f6;
  --color-tvt03-sub: oklch(0.976 0.01 168);
  --color-tvt03-ink: #0a251e;
  --color-tvt03-ink: oklch(0.24 0.035 175);
  --color-tvt03-mut: #46625a;
  --color-tvt03-mut: oklch(0.47 0.035 175);
  --color-tvt03-line: #d5e6df;
  --color-tvt03-line: oklch(0.91 0.02 170);
  --color-tvt03-rail: #032a22;
  --color-tvt03-rail: oklch(0.255 0.045 175);
  --color-tvt03-rail-glow: #0065488c;
  --color-tvt03-rail-glow: oklch(0.45 0.11 165 / 0.55);
  --color-tvt03-rail-ink: #eef8f3;
  --color-tvt03-rail-ink: oklch(0.97 0.012 165);
  --color-tvt03-rail-mut: #a9c5b9;
  --color-tvt03-rail-mut: oklch(0.8 0.035 168);
  --color-tvt03-acc: #00ad72;
  --color-tvt03-acc: oklch(0.66 0.15 160);
  --color-tvt03-acc2: #009a9a;
  --color-tvt03-acc2: oklch(0.62 0.12 195);
  --color-tvt03-acc-ink: #006c4d;
  --color-tvt03-acc-ink: oklch(0.47 0.11 165);
  --color-tvt03-glow: #65ebac;
  --color-tvt03-glow: oklch(0.85 0.15 160);
  --font-tvt03-sans: 'Manrope', system-ui, sans-serif;
  --font-tvt03-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tvt03-card: 0 1px 2px oklch(0.3 0.06 175 / 0.07), 0 32px 72px -32px oklch(0.35 0.1 170 / 0.45);
  --shadow-tvt03-tab: inset 0 1px 0 oklch(1 0 0 / 0.08), 0 8px 20px -10px oklch(0 0 0 / 0.5), inset 3px 0 0 var(--color-tvt03-glow);
  --animate-tvt03-draw: tvt03-draw 0.7s cubic-bezier(0.4, 0.6, 0.3, 1);

  @keyframes tvt03-draw {
    from {
      stroke-dashoffset: 1;
    }

    to {
      stroke-dashoffset: 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-03 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-03:not([data-theme="light"]) {
    --color-tvt03-bg: #02100c;
    --color-tvt03-bg: oklch(0.155 0.025 175);
    --color-tvt03-halo: #003d2c80;
    --color-tvt03-halo: oklch(0.32 0.08 168 / 0.5);
    --color-tvt03-card: #051a15;
    --color-tvt03-card: oklch(0.2 0.03 175);
    --color-tvt03-sub: #09221c;
    --color-tvt03-sub: oklch(0.23 0.033 175);
    --color-tvt03-ink: #ebf4f0;
    --color-tvt03-ink: oklch(0.96 0.012 165);
    --color-tvt03-mut: #9fbcb1;
    --color-tvt03-mut: oklch(0.77 0.035 170);
    --color-tvt03-line: #18372f;
    --color-tvt03-line: oklch(0.31 0.04 175);
    --color-tvt03-rail: #011510;
    --color-tvt03-rail: oklch(0.175 0.03 178);
    --color-tvt03-rail-glow: #00493380;
    --color-tvt03-rail-glow: oklch(0.36 0.1 165 / 0.5);
    --color-tvt03-rail-ink: #eef8f3;
    --color-tvt03-rail-ink: oklch(0.97 0.012 165);
    --color-tvt03-rail-mut: #a3bfb3;
    --color-tvt03-rail-mut: oklch(0.78 0.035 168);
    --color-tvt03-acc: #12c281;
    --color-tvt03-acc: oklch(0.72 0.16 160);
    --color-tvt03-acc2: #00aeae;
    --color-tvt03-acc2: oklch(0.68 0.12 195);
    --color-tvt03-acc-ink: #72e5b0;
    --color-tvt03-acc-ink: oklch(0.84 0.13 162);
    --color-tvt03-glow: #68efaf;
    --color-tvt03-glow: oklch(0.86 0.15 160);
  }
}

.tvt-03[data-theme="dark"] {
  --color-tvt03-bg: #02100c;
  --color-tvt03-bg: oklch(0.155 0.025 175);
  --color-tvt03-halo: #003d2c80;
  --color-tvt03-halo: oklch(0.32 0.08 168 / 0.5);
  --color-tvt03-card: #051a15;
  --color-tvt03-card: oklch(0.2 0.03 175);
  --color-tvt03-sub: #09221c;
  --color-tvt03-sub: oklch(0.23 0.033 175);
  --color-tvt03-ink: #ebf4f0;
  --color-tvt03-ink: oklch(0.96 0.012 165);
  --color-tvt03-mut: #9fbcb1;
  --color-tvt03-mut: oklch(0.77 0.035 170);
  --color-tvt03-line: #18372f;
  --color-tvt03-line: oklch(0.31 0.04 175);
  --color-tvt03-rail: #011510;
  --color-tvt03-rail: oklch(0.175 0.03 178);
  --color-tvt03-rail-glow: #00493380;
  --color-tvt03-rail-glow: oklch(0.36 0.1 165 / 0.5);
  --color-tvt03-rail-ink: #eef8f3;
  --color-tvt03-rail-ink: oklch(0.97 0.012 165);
  --color-tvt03-rail-mut: #a3bfb3;
  --color-tvt03-rail-mut: oklch(0.78 0.035 168);
  --color-tvt03-acc: #12c281;
  --color-tvt03-acc: oklch(0.72 0.16 160);
  --color-tvt03-acc2: #00aeae;
  --color-tvt03-acc2: oklch(0.68 0.12 195);
  --color-tvt03-acc-ink: #72e5b0;
  --color-tvt03-acc-ink: oklch(0.84 0.13 162);
  --color-tvt03-glow: #68efaf;
  --color-tvt03-glow: oklch(0.86 0.15 160);
}
```
