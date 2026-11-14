---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/responsive-tailwind-pagination-with-mobile-page-x-of-y/"
title: "Responsive Tailwind Pagination with Mobile Page X of Y"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "One pagination markup, three layouts, zero media queries: the full number row on roomy cards, a trimmed row with icon-only edges in the middle, and a compact…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Pagination with Mobile Page X of Y
Source: https://codefronts.com/navigation/tailwind-css-pagination/responsive-tailwind-pagination-with-mobile-page-x-of-y/

One pagination markup, three layouts, zero media queries: the full number row on roomy cards, a trimmed row with icon-only edges in the middle, and a compact Page 3 of 12 readout with a progress bar when the card gets narrow. It queries a named container (@container/pg), so the same component switches correctly in a main column and a 19rem sidebar on the same screen.
## HTML
```html
<section class="tpg-03 w-full min-h-svh grid place-items-center bg-tpg03-bg bg-[radial-gradient(80%_60%_at_50%_0%,var(--color-tpg03-glow),transparent_72%)] px-5 py-14 font-tpg03-sans text-tpg03-ink antialiased" aria-label="Responsive Tailwind pagination with mobile page X of Y demo">
  <div class="grid w-full max-w-[62rem] justify-items-center gap-6">
    <div class="grid w-full items-start gap-5 lg:grid-cols-[minmax(0,1fr)_19rem]">
      <article class="flex flex-col overflow-hidden rounded-2xl bg-tpg03-card shadow-tpg03-card ring-1 ring-tpg03-line" aria-labelledby="tpg-03-orders-h">
        <header class="flex items-end justify-between gap-4 px-4 pt-5 pb-4 sm:px-5">
          <div>
            <h2 id="tpg-03-orders-h" class="text-[17px] font-bold tracking-[-0.02em]">Orders</h2>
            <p class="mt-0.5 text-[13px] text-tpg03-mut tabular-nums">128 orders · showing 21–24</p>
          </div>
        </header>
        <ul class="divide-y divide-tpg03-line border-t border-tpg03-line">
          <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-tpg03-acc/20 to-tpg03-acc2/15 text-[12px] font-bold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset">MO</span>
            <div class="min-w-0 flex-1">
              <p class="truncate text-[14.5px] font-semibold tracking-[-0.01em]">Maya Okafor</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut tabular-nums"><span class="font-tpg03-mono">#3021</span> · 2 items</p>
            </div>
            <span class="rounded-full bg-tpg03-acc/8 px-2 py-0.5 text-[11.5px] font-semibold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset max-sm:hidden">Paid</span>
            <p class="w-20 text-right text-[14px] font-semibold tabular-nums">$184.00</p>
          </li>
          <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-tpg03-acc/20 to-tpg03-acc2/15 text-[12px] font-bold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset">LG</span>
            <div class="min-w-0 flex-1">
              <p class="truncate text-[14.5px] font-semibold tracking-[-0.01em]">Liam Gallagher</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut tabular-nums"><span class="font-tpg03-mono">#3020</span> · 1 item</p>
            </div>
            <span class="rounded-full bg-tpg03-acc/8 px-2 py-0.5 text-[11.5px] font-semibold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset max-sm:hidden">Pending</span>
            <p class="w-20 text-right text-[14px] font-semibold tabular-nums">$62.50</p>
          </li>
          <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-tpg03-acc/20 to-tpg03-acc2/15 text-[12px] font-bold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset">SB</span>
            <div class="min-w-0 flex-1">
              <p class="truncate text-[14.5px] font-semibold tracking-[-0.01em]">Sofia Bianchi</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut tabular-nums"><span class="font-tpg03-mono">#3019</span> · 4 items</p>
            </div>
            <span class="rounded-full bg-tpg03-acc/8 px-2 py-0.5 text-[11.5px] font-semibold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset max-sm:hidden">Paid</span>
            <p class="w-20 text-right text-[14px] font-semibold tabular-nums">$412.80</p>
          </li>
          <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-5">
            <span aria-hidden="true" class="grid size-9 shrink-0 place-items-center rounded-full bg-linear-to-br from-tpg03-acc/20 to-tpg03-acc2/15 text-[12px] font-bold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset">NW</span>
            <div class="min-w-0 flex-1">
              <p class="truncate text-[14.5px] font-semibold tracking-[-0.01em]">Noah Whitfield</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut tabular-nums"><span class="font-tpg03-mono">#3018</span> · 3 items</p>
            </div>
            <span class="rounded-full bg-tpg03-acc/8 px-2 py-0.5 text-[11.5px] font-semibold text-tpg03-acc-ink ring-1 ring-tpg03-acc/20 ring-inset max-sm:hidden">Shipped</span>
            <p class="w-20 text-right text-[14px] font-semibold tabular-nums">$97.15</p>
          </li>
        </ul>
        <div class="@container/pg border-t border-tpg03-line bg-tpg03-sub px-3 py-3 sm:px-4">
          <nav aria-label="Pagination, orders" class="flex items-center justify-between gap-3">
            <a href="#tpg-03-orders-2" aria-label="Previous page, page 2" class="inline-flex min-h-11 min-w-11 shrink-0 items-center justify-center gap-1.5 rounded-xl bg-tpg03-card px-3 text-[14px] font-semibold text-tpg03-ink shadow-tpg03-btn ring-1 ring-tpg03-line transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink hover:ring-tpg03-acc/45 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring @max-[30rem]/pg:px-0"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[38rem]/pg:sr-only">Previous</span></a>
            <ol class="flex items-center gap-0.5 @max-[30rem]/pg:hidden">
            <li><a href="#tpg-03-orders-1" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">1</a></li>
            <li><a href="#tpg-03-orders-2" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">2</a></li>
            <li><a href="#tpg-03-orders-3" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70" aria-current="page">3</a></li>
            <li><a href="#tpg-03-orders-4" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">4</a></li>
            <li class="@max-[38rem]/pg:hidden"><a href="#tpg-03-orders-5" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">5</a></li>
            <li aria-hidden="true" class="grid h-11 w-6 place-items-center text-tpg03-mut select-none">…</li>
            <li><a href="#tpg-03-orders-12" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">12</a></li>
            </ol>
            <p class="hidden min-w-0 justify-items-center gap-1.5 text-[13.5px] text-tpg03-mut tabular-nums @max-[30rem]/pg:grid">
              <span>Page <b class="font-bold text-tpg03-ink">3</b> of <b class="font-bold text-tpg03-ink">12</b></span>
              <span aria-hidden="true" class="block h-1 w-24 overflow-hidden rounded-full bg-tpg03-acc/15"><span class="block h-full w-[25%] rounded-full bg-linear-to-r from-tpg03-acc to-tpg03-acc2 shadow-[0_0_8px] shadow-tpg03-acc2/60"></span></span>
            </p>
            <a href="#tpg-03-orders-4" aria-label="Next page, page 4" class="inline-flex min-h-11 min-w-11 shrink-0 items-center justify-center gap-1.5 rounded-xl bg-tpg03-card px-3 text-[14px] font-semibold text-tpg03-ink shadow-tpg03-btn ring-1 ring-tpg03-line transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink hover:ring-tpg03-acc/45 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring @max-[30rem]/pg:px-0"><span class="@max-[38rem]/pg:sr-only">Next</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
          </nav>
        </div>
      </article>
      <aside class="flex flex-col overflow-hidden rounded-2xl bg-tpg03-card shadow-tpg03-card ring-1 ring-tpg03-line" aria-labelledby="tpg-03-inv-h">
        <header class="flex items-end justify-between gap-4 px-4 pt-5 pb-4">
          <div>
            <h2 id="tpg-03-inv-h" class="text-[17px] font-bold tracking-[-0.02em]">Invoices</h2>
            <p class="mt-0.5 text-[13px] text-tpg03-mut tabular-nums">48 invoices</p>
          </div>
        </header>
        <ul class="divide-y divide-tpg03-line border-t border-tpg03-line">
          <li class="flex items-baseline justify-between gap-3 px-4 py-3.5">
            <div>
              <p class="font-tpg03-mono text-[13px] font-medium">INV-0412</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut">Due Oct 30</p>
            </div>
            <p class="text-[14px] font-semibold tabular-nums">$1,240.00</p>
          </li>
          <li class="flex items-baseline justify-between gap-3 px-4 py-3.5">
            <div>
              <p class="font-tpg03-mono text-[13px] font-medium">INV-0411</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut">Paid Oct 2</p>
            </div>
            <p class="text-[14px] font-semibold tabular-nums">$860.00</p>
          </li>
          <li class="flex items-baseline justify-between gap-3 px-4 py-3.5">
            <div>
              <p class="font-tpg03-mono text-[13px] font-medium">INV-0410</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut">Paid Sep 28</p>
            </div>
            <p class="text-[14px] font-semibold tabular-nums">$2,115.50</p>
          </li>
          <li class="flex items-baseline justify-between gap-3 px-4 py-3.5">
            <div>
              <p class="font-tpg03-mono text-[13px] font-medium">INV-0409</p>
              <p class="mt-0.5 text-[12.5px] text-tpg03-mut">Paid Sep 14</p>
            </div>
            <p class="text-[14px] font-semibold tabular-nums">$430.00</p>
          </li>
        </ul>
        <div class="@container/pg border-t border-tpg03-line bg-tpg03-sub px-3 py-3 sm:px-4">
          <nav aria-label="Pagination, invoices" class="flex items-center justify-between gap-3">
            <a href="#tpg-03-inv-2" aria-label="Previous page, page 2" class="inline-flex min-h-11 min-w-11 shrink-0 items-center justify-center gap-1.5 rounded-xl bg-tpg03-card px-3 text-[14px] font-semibold text-tpg03-ink shadow-tpg03-btn ring-1 ring-tpg03-line transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink hover:ring-tpg03-acc/45 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring @max-[30rem]/pg:px-0"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[38rem]/pg:sr-only">Previous</span></a>
            <ol class="flex items-center gap-0.5 @max-[30rem]/pg:hidden">
            <li><a href="#tpg-03-inv-1" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">1</a></li>
            <li><a href="#tpg-03-inv-2" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">2</a></li>
            <li><a href="#tpg-03-inv-3" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70" aria-current="page">3</a></li>
            <li><a href="#tpg-03-inv-4" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">4</a></li>
            <li class="@max-[38rem]/pg:hidden"><a href="#tpg-03-inv-5" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">5</a></li>
            <li aria-hidden="true" class="grid h-11 w-6 place-items-center text-tpg03-mut select-none">…</li>
            <li><a href="#tpg-03-inv-12" class="grid min-h-11 min-w-11 place-items-center rounded-xl px-2 text-[14px] font-semibold tabular-nums text-tpg03-mut transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none relative hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring after:pointer-events-none after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[3px] after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg03-acc after:to-tpg03-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:scale-x-100 motion-reduce:after:transition-none aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg03-acc/16 aria-[current=page]:to-tpg03-acc2/8 aria-[current=page]:text-tpg03-acc-ink aria-[current=page]:shadow-tpg03-cur aria-[current=page]:after:scale-x-100 aria-[current=page]:after:shadow-[0_0_10px] aria-[current=page]:after:shadow-tpg03-acc2/70">12</a></li>
            </ol>
            <p class="hidden min-w-0 justify-items-center gap-1.5 text-[13.5px] text-tpg03-mut tabular-nums @max-[30rem]/pg:grid">
              <span>Page <b class="font-bold text-tpg03-ink">3</b> of <b class="font-bold text-tpg03-ink">12</b></span>
              <span aria-hidden="true" class="block h-1 w-24 overflow-hidden rounded-full bg-tpg03-acc/15"><span class="block h-full w-[25%] rounded-full bg-linear-to-r from-tpg03-acc to-tpg03-acc2 shadow-[0_0_8px] shadow-tpg03-acc2/60"></span></span>
            </p>
            <a href="#tpg-03-inv-4" aria-label="Next page, page 4" class="inline-flex min-h-11 min-w-11 shrink-0 items-center justify-center gap-1.5 rounded-xl bg-tpg03-card px-3 text-[14px] font-semibold text-tpg03-ink shadow-tpg03-btn ring-1 ring-tpg03-line transition-[background-color,color,box-shadow,scale,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:-translate-y-px hover:bg-tpg03-acc/8 hover:text-tpg03-acc-ink hover:ring-tpg03-acc/45 active:translate-y-0 active:scale-[0.97] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg03-ring @max-[30rem]/pg:px-0"><span class="@max-[38rem]/pg:sr-only">Next</span><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
          </nav>
        </div>
      </aside>
    </div>
    <p class="max-w-[34rem] text-center text-[13px] leading-relaxed text-tpg03-mut text-balance">Same markup in both cards. Each footer queries its own width: numbers above 30rem, a <b class="font-semibold text-tpg03-ink">Page 3 of 12</b> readout below it.</p>
    <p aria-hidden="true" class="rounded-full bg-tpg03-card px-3.5 py-2 text-center font-tpg03-mono text-[11.5px] text-tpg03-mut ring-1 ring-tpg03-line">@container/pg · @max-[30rem]/pg:hidden · @max-[38rem]/pg:sr-only</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg03-bg: #e8f9ef;
  --color-tpg03-bg: oklch(0.966 0.022 160);
  --color-tpg03-glow: #b0ecbcb3;
  --color-tpg03-glow: oklch(0.89 0.09 150 / 0.7);
  --color-tpg03-card: #fafffc;
  --color-tpg03-card: oklch(0.995 0.006 160);
  --color-tpg03-sub: #eefaf2;
  --color-tpg03-sub: oklch(0.974 0.016 158);
  --color-tpg03-ink: #09251a;
  --color-tpg03-ink: oklch(0.24 0.04 165);
  --color-tpg03-mut: #435f52;
  --color-tpg03-mut: oklch(0.46 0.04 165);
  --color-tpg03-line: #cde5d7;
  --color-tpg03-line: oklch(0.9 0.032 160);
  --color-tpg03-acc: #009966;
  --color-tpg03-acc: oklch(0.596 0.145 163.2);
  --color-tpg03-acc2: #5ea500;
  --color-tpg03-acc2: oklch(0.648 0.2 131.7);
  --color-tpg03-acc-ink: #00603c;
  --color-tpg03-acc-ink: oklch(0.43 0.1 160);
  --color-tpg03-ring: #008954;
  --color-tpg03-ring: oklch(0.55 0.14 160);
  --font-tpg03-sans: 'Manrope', system-ui, sans-serif;
  --font-tpg03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --shadow-tpg03-card: 0 1px 2px oklch(0.3 0.06 160 / 0.07), 0 26px 56px -24px oklch(0.45 0.12 155 / 0.32);
  --shadow-tpg03-btn: 0 1px 2px oklch(0.3 0.06 160 / 0.08);
  --shadow-tpg03-cur: inset 0 0 0 1px oklch(0.6 0.15 160 / 0.3), inset 0 1px 0 oklch(1 0 0 / 0.4), 0 6px 16px -8px oklch(0.6 0.16 150 / 0.55);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-03 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-03:not([data-theme="light"]) {
    --color-tpg03-bg: #00140c;
    --color-tpg03-bg: oklch(0.17 0.035 165);
    --color-tpg03-glow: #01421a80;
    --color-tpg03-glow: oklch(0.33 0.09 150 / 0.5);
    --color-tpg03-card: #031e14;
    --color-tpg03-card: oklch(0.21 0.04 165);
    --color-tpg03-sub: #072418;
    --color-tpg03-sub: oklch(0.235 0.042 163);
    --color-tpg03-ink: #e9f6eb;
    --color-tpg03-ink: oklch(0.96 0.02 150);
    --color-tpg03-mut: #9ebda8;
    --color-tpg03-mut: oklch(0.77 0.045 155);
    --color-tpg03-line: #1a3d2e;
    --color-tpg03-line: oklch(0.33 0.05 163);
    --color-tpg03-acc: #12c281;
    --color-tpg03-acc: oklch(0.72 0.16 160);
    --color-tpg03-acc2: #a6e146;
    --color-tpg03-acc2: oklch(0.84 0.19 128);
    --color-tpg03-acc-ink: #93eca6;
    --color-tpg03-acc-ink: oklch(0.87 0.13 150);
    --color-tpg03-ring: #6ed889;
    --color-tpg03-ring: oklch(0.8 0.15 150);
  }
}

.tpg-03[data-theme="dark"] {
  --color-tpg03-bg: #00140c;
  --color-tpg03-bg: oklch(0.17 0.035 165);
  --color-tpg03-glow: #01421a80;
  --color-tpg03-glow: oklch(0.33 0.09 150 / 0.5);
  --color-tpg03-card: #031e14;
  --color-tpg03-card: oklch(0.21 0.04 165);
  --color-tpg03-sub: #072418;
  --color-tpg03-sub: oklch(0.235 0.042 163);
  --color-tpg03-ink: #e9f6eb;
  --color-tpg03-ink: oklch(0.96 0.02 150);
  --color-tpg03-mut: #9ebda8;
  --color-tpg03-mut: oklch(0.77 0.045 155);
  --color-tpg03-line: #1a3d2e;
  --color-tpg03-line: oklch(0.33 0.05 163);
  --color-tpg03-acc: #12c281;
  --color-tpg03-acc: oklch(0.72 0.16 160);
  --color-tpg03-acc2: #a6e146;
  --color-tpg03-acc2: oklch(0.84 0.19 128);
  --color-tpg03-acc-ink: #93eca6;
  --color-tpg03-acc-ink: oklch(0.87 0.13 150);
  --color-tpg03-ring: #6ed889;
  --color-tpg03-ring: oklch(0.8 0.15 150);
}
```
