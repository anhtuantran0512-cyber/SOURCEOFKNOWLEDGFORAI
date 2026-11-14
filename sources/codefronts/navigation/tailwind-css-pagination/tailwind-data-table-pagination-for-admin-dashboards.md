---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-data-table-pagination-for-admin-dashboards/"
title: "Tailwind Data Table Pagination for Admin Dashboards"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "An admin invoice table whose footer really pages it &mdash; with zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Data Table Pagination for Admin Dashboards
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-data-table-pagination-for-admin-dashboards/

An admin invoice table whose footer really pages it &mdash; with zero JavaScript. Three radios live inside the page buttons; group-has-[#tpg-10-p2:checked]/tbl:hidden on each row hides everything off-page, has-checked: turns the current button into an indigo-slate key wrapped in a spinning jade&rarr;teal conic ring, and the Previous / Next arrows are <label for>s that swap in per page. Arrow keys page the table natively, and rows fade in with starting:opacity-0.
## HTML
```html
<section class="tpg-10 w-full min-h-svh grid place-items-center bg-tpg10-bg bg-[radial-gradient(60%_50%_at_15%_10%,var(--color-tpg10-glow),transparent_70%),radial-gradient(60%_50%_at_90%_95%,var(--color-tpg10-glow2),transparent_70%)] px-5 py-14 font-tpg10-sans text-tpg10-ink antialiased" aria-label="Data table pagination for admin dashboards demo">
  <div class="grid w-full justify-items-center gap-7">
    <div id="tpg-10-table" class="group/tbl w-full max-w-[58rem] overflow-hidden rounded-2xl bg-tpg10-card shadow-tpg10-card ring-1 ring-tpg10-jade/20 transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <header class="flex flex-wrap items-center justify-between gap-3 px-5 py-4 sm:px-6">
        <div>
          <h2 class="text-[17px] font-semibold tracking-[-0.01em]">Invoices</h2>
          <p class="mt-0.5 text-[13px] text-tpg10-mut tabular-nums">12 invoices · <b class="font-semibold text-tpg10-ink">$24,760.00</b> outstanding</p>
        </div>
        <p class="inline-flex items-center gap-2 rounded-full bg-tpg10-jade/8 px-2.5 py-1 font-tpg10-mono text-[11.5px] text-tpg10-jade-ink ring-1 ring-tpg10-jade/25"><span aria-hidden="true" class="relative grid size-2 place-items-center"><span class="absolute inline-flex size-full animate-ping rounded-full bg-tpg10-ring/60 motion-reduce:hidden"></span><span class="relative size-2 rounded-full bg-tpg10-ring"></span></span>Live · synced 09:42</p>
      </header>

      <div class="overflow-x-auto">
        <table class="w-full border-separate border-spacing-0 text-left text-sm">
          <caption class="sr-only">Invoices, four per page, newest first</caption>
          <thead class="bg-linear-to-r from-tpg10-band to-tpg10-band2">
            <tr class="text-[11px] font-semibold tracking-[0.08em] text-tpg10-band-mut uppercase">
              <th scope="col" class="border-t border-tpg10-band py-2.5 pr-3 pl-5 font-semibold sm:pl-6">Customer</th>
              <th scope="col" aria-sort="descending" class="border-t border-tpg10-band px-3 py-2.5 font-semibold max-sm:hidden"><span class="inline-flex items-center gap-1 text-tpg10-band-ink">Issued<svg class="size-3.5 text-tpg10-jade" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 4v12M5.5 11.5L10 16l4.5-4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></span></th>
              <th scope="col" class="border-t border-tpg10-band px-3 py-2.5 font-semibold">Status</th>
              <th scope="col" class="border-t border-tpg10-band py-2.5 pr-5 pl-3 text-right font-semibold sm:pr-6">Amount</th>
            </tr>
          </thead>
          <tbody>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p2:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">AC</span><div class="min-w-0"><p class="truncate font-medium">Alex Chen</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2041</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 12</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$4,280.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p2:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">PS</span><div class="min-w-0"><p class="truncate font-medium">Priya Sharma</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2040</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 11</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-warn/10 text-tpg10-warn ring-tpg10-warn/25">pending</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$1,150.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p2:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">JL</span><div class="min-w-0"><p class="truncate font-medium">Jordan Lee</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2039</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 10</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$860.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p2:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">SR</span><div class="min-w-0"><p class="truncate font-medium">Sam Rivera</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2038</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 9</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-due/10 text-tpg10-due ring-tpg10-due/25">overdue</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$2,940.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">ML</span><div class="min-w-0"><p class="truncate font-medium">Mara Lindqvist</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2037</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 8</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$515.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">KM</span><div class="min-w-0"><p class="truncate font-medium">Kofi Mensah</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2036</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 7</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-warn/10 text-tpg10-warn ring-tpg10-warn/25">pending</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$7,320.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">HS</span><div class="min-w-0"><p class="truncate font-medium">Hana Sato</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2035</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 6</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$1,995.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p3:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">LO</span><div class="min-w-0"><p class="truncate font-medium">Luis Ortega</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2034</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 4</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-sunk text-tpg10-mut ring-tpg10-line">draft</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$430.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p2:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">AC</span><div class="min-w-0"><p class="truncate font-medium">Alex Chen</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2033</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 3</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-due/10 text-tpg10-due ring-tpg10-due/25">overdue</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$12,600.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p2:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">NR</span><div class="min-w-0"><p class="truncate font-medium">Nadia Rahman</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2032</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Oct 2</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$3,210.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p2:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">TB</span><div class="min-w-0"><p class="truncate font-medium">Tom Becker</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2031</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Sep 30</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-ok/10 text-tpg10-ok ring-tpg10-ok/25">paid</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$2,375.00</td>
            </tr>
            <tr class="transition-[opacity,background-color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] starting:opacity-0 hover:bg-tpg10-jade/6 motion-reduce:transition-none group-has-[#tpg-10-p1:checked]/tbl:hidden group-has-[#tpg-10-p2:checked]/tbl:hidden">
              <td class="border-t border-tpg10-line py-3 pr-3 pl-5 sm:pl-6"><div class="flex items-center gap-3"><span aria-hidden="true" class="grid size-8 flex-none max-sm:hidden place-items-center rounded-full bg-linear-to-br from-tpg10-jade/20 to-tpg10-teal/20 text-[11px] font-semibold text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">PS</span><div class="min-w-0"><p class="truncate font-medium">Priya Sharma</p><p class="font-tpg10-mono text-[12px] text-tpg10-mut">INV-2030</p></div></div></td>
              <td class="border-t border-tpg10-line px-3 py-3 whitespace-nowrap text-tpg10-mut tabular-nums max-sm:hidden">Sep 29</td>
              <td class="border-t border-tpg10-line px-3 py-3"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium capitalize ring-1 ring-inset before:size-1.5 before:rounded-full before:bg-current bg-tpg10-warn/10 text-tpg10-warn ring-tpg10-warn/25">pending</span></td>
              <td class="border-t border-tpg10-line py-3 pr-5 pl-3 text-right font-tpg10-mono text-[13px] font-medium whitespace-nowrap tabular-nums sm:pr-6">$750.00</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="flex flex-wrap items-center justify-between gap-x-6 gap-y-3 border-t border-tpg10-line px-5 py-3 sm:px-6">
        <p class="text-[13px] text-tpg10-mut tabular-nums">Showing <b class="font-semibold text-tpg10-ink"><span class="hidden group-has-[#tpg-10-p1:checked]/tbl:inline">1–4</span><span class="hidden group-has-[#tpg-10-p2:checked]/tbl:inline">5–8</span><span class="hidden group-has-[#tpg-10-p3:checked]/tbl:inline">9–12</span></b> of <b class="font-semibold text-tpg10-ink">12</b> invoices</p>
        <nav aria-label="Table pagination" class="flex items-center gap-1.5 max-sm:w-full max-sm:justify-between">
          <span aria-hidden="true" class="hidden size-11 place-items-center rounded-lg bg-tpg10-sunk text-tpg10-mut/50 ring-1 ring-tpg10-line group-has-[#tpg-10-p1:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <label for="tpg-10-p1" aria-hidden="true" title="Previous page" class="hidden size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-tpg10-jade-ink ring-1 ring-tpg10-jade/25 transition-[background-color,box-shadow,translate,scale] duration-200 hover:-translate-y-px hover:bg-tpg10-jade/10 hover:ring-tpg10-jade/60 hover:shadow-[0_8px_18px_-10px_var(--color-tpg10-jade)] active:scale-95 motion-reduce:hover:translate-y-0 group-has-[#tpg-10-p2:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
          <label for="tpg-10-p2" aria-hidden="true" title="Previous page" class="hidden size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-tpg10-jade-ink ring-1 ring-tpg10-jade/25 transition-[background-color,box-shadow,translate,scale] duration-200 hover:-translate-y-px hover:bg-tpg10-jade/10 hover:ring-tpg10-jade/60 hover:shadow-[0_8px_18px_-10px_var(--color-tpg10-jade)] active:scale-95 motion-reduce:hover:translate-y-0 group-has-[#tpg-10-p3:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
          <div role="radiogroup" aria-label="Page">
            <ol class="flex items-center gap-1.5">
              <li><label class="relative grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-sm font-medium tabular-nums ring-1 ring-tpg10-jade/25 transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-has-checked:hover:-translate-y-px not-has-checked:hover:bg-tpg10-jade/10 not-has-checked:hover:text-tpg10-jade-ink not-has-checked:hover:ring-tpg10-jade/60 has-checked:border-2 has-checked:border-transparent has-checked:font-semibold has-checked:text-tpg10-band-ink has-checked:ring-0 has-checked:[background:linear-gradient(var(--color-tpg10-band),var(--color-tpg10-band2))_padding-box,conic-gradient(from_var(--tpg10-a),var(--color-tpg10-jade),var(--color-tpg10-teal),var(--color-tpg10-band2),var(--color-tpg10-jade))_border-box] has-checked:shadow-[0_8px_22px_-8px_var(--color-tpg10-jade)] has-checked:animate-tpg10-spin motion-reduce:hover:translate-y-0 motion-reduce:has-checked:animate-none has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpg10-ring motion-reduce:transition-none"><input type="radio" name="tpg-10-page" id="tpg-10-p1" aria-label="Page 1" checked class="sr-only">1</label></li>
              <li><label class="relative grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-sm font-medium tabular-nums ring-1 ring-tpg10-jade/25 transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-has-checked:hover:-translate-y-px not-has-checked:hover:bg-tpg10-jade/10 not-has-checked:hover:text-tpg10-jade-ink not-has-checked:hover:ring-tpg10-jade/60 has-checked:border-2 has-checked:border-transparent has-checked:font-semibold has-checked:text-tpg10-band-ink has-checked:ring-0 has-checked:[background:linear-gradient(var(--color-tpg10-band),var(--color-tpg10-band2))_padding-box,conic-gradient(from_var(--tpg10-a),var(--color-tpg10-jade),var(--color-tpg10-teal),var(--color-tpg10-band2),var(--color-tpg10-jade))_border-box] has-checked:shadow-[0_8px_22px_-8px_var(--color-tpg10-jade)] has-checked:animate-tpg10-spin motion-reduce:hover:translate-y-0 motion-reduce:has-checked:animate-none has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpg10-ring motion-reduce:transition-none"><input type="radio" name="tpg-10-page" id="tpg-10-p2" aria-label="Page 2" class="sr-only">2</label></li>
              <li><label class="relative grid size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-sm font-medium tabular-nums ring-1 ring-tpg10-jade/25 transition-[background-color,color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-has-checked:hover:-translate-y-px not-has-checked:hover:bg-tpg10-jade/10 not-has-checked:hover:text-tpg10-jade-ink not-has-checked:hover:ring-tpg10-jade/60 has-checked:border-2 has-checked:border-transparent has-checked:font-semibold has-checked:text-tpg10-band-ink has-checked:ring-0 has-checked:[background:linear-gradient(var(--color-tpg10-band),var(--color-tpg10-band2))_padding-box,conic-gradient(from_var(--tpg10-a),var(--color-tpg10-jade),var(--color-tpg10-teal),var(--color-tpg10-band2),var(--color-tpg10-jade))_border-box] has-checked:shadow-[0_8px_22px_-8px_var(--color-tpg10-jade)] has-checked:animate-tpg10-spin motion-reduce:hover:translate-y-0 motion-reduce:has-checked:animate-none has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tpg10-ring motion-reduce:transition-none"><input type="radio" name="tpg-10-page" id="tpg-10-p3" aria-label="Page 3" class="sr-only">3</label></li>
            </ol>
          </div>
          <label for="tpg-10-p2" aria-hidden="true" title="Next page" class="hidden size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-tpg10-jade-ink ring-1 ring-tpg10-jade/25 transition-[background-color,box-shadow,translate,scale] duration-200 hover:-translate-y-px hover:bg-tpg10-jade/10 hover:ring-tpg10-jade/60 hover:shadow-[0_8px_18px_-10px_var(--color-tpg10-jade)] active:scale-95 motion-reduce:hover:translate-y-0 group-has-[#tpg-10-p1:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
          <label for="tpg-10-p3" aria-hidden="true" title="Next page" class="hidden size-11 cursor-pointer place-items-center rounded-lg bg-tpg10-card text-tpg10-jade-ink ring-1 ring-tpg10-jade/25 transition-[background-color,box-shadow,translate,scale] duration-200 hover:-translate-y-px hover:bg-tpg10-jade/10 hover:ring-tpg10-jade/60 hover:shadow-[0_8px_18px_-10px_var(--color-tpg10-jade)] active:scale-95 motion-reduce:hover:translate-y-0 group-has-[#tpg-10-p2:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></label>
          <span aria-hidden="true" class="hidden size-11 place-items-center rounded-lg bg-tpg10-sunk text-tpg10-mut/50 ring-1 ring-tpg10-line group-has-[#tpg-10-p3:checked]/tbl:grid"><svg class="size-4" viewBox="0 0 20 20" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg10-card px-3.5 py-2 text-center font-tpg10-mono text-[11.5px] text-tpg10-jade-ink ring-1 ring-tpg10-jade/25">group-has-[…:checked]/tbl: · has-checked:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg10-bg: #ecf8f4;
  --color-tpg10-bg: oklch(0.97 0.014 175);
  --color-tpg10-glow: #b0eed799;
  --color-tpg10-glow: oklch(0.9 0.07 170 / 0.6);
  --color-tpg10-glow2: #cdd6f999;
  --color-tpg10-glow2: oklch(0.88 0.05 275 / 0.6);
  --color-tpg10-card: #fbfffe;
  --color-tpg10-card: oklch(0.997 0.004 175);
  --color-tpg10-sunk: #eaf7f3;
  --color-tpg10-sunk: oklch(0.965 0.014 175);
  --color-tpg10-ink: #021f21;
  --color-tpg10-ink: oklch(0.22 0.035 200);
  --color-tpg10-mut: #436163;
  --color-tpg10-mut: oklch(0.47 0.035 200);
  --color-tpg10-line: #d1e3de;
  --color-tpg10-line: oklch(0.9 0.02 180);
  --color-tpg10-band: #252b4c;
  --color-tpg10-band: oklch(0.3 0.06 275);
  --color-tpg10-band2: #3f4177;
  --color-tpg10-band2: oklch(0.4 0.09 280);
  --color-tpg10-band-ink: #f3f5fc;
  --color-tpg10-band-ink: oklch(0.97 0.01 275);
  --color-tpg10-band-mut: #c2c9e5;
  --color-tpg10-band-mut: oklch(0.84 0.04 275);
  --color-tpg10-jade: #00bc7d;
  --color-tpg10-jade: oklch(0.696 0.17 162.5);
  --color-tpg10-teal: #00bba7;
  --color-tpg10-teal: oklch(0.704 0.14 182.5);
  --color-tpg10-jade-ink: #007852;
  --color-tpg10-jade-ink: oklch(0.5 0.12 165);
  --color-tpg10-ring: #00885e;
  --color-tpg10-ring: oklch(0.55 0.13 165);
  --color-tpg10-ok: #0b7643;
  --color-tpg10-ok: oklch(0.5 0.12 155);
  --color-tpg10-warn: #975d00;
  --color-tpg10-warn: oklch(0.53 0.12 70);
  --color-tpg10-due: #c2272d;
  --color-tpg10-due: oklch(0.53 0.19 25);
  --font-tpg10-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-tpg10-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg10-card: 0 1px 2px oklch(0.3 0.06 190 / 0.08), 0 28px 56px -26px oklch(0.35 0.1 200 / 0.4);
  --animate-tpg10-spin: tpg10-spin 4s linear infinite;

  @keyframes tpg10-spin {
    to {
      --tpg10-a: 360deg;
    }
  }
}
/* @property is an at-rule with no utility: it makes the conic ring's start angle animatable. */

@property --tpg10-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
/* Dark "jade night": the same tokens re-pointed; the indigo-slate band deepens, jade brightens. */

@media (prefers-color-scheme: dark) {
  .tpg-10:not([data-theme="light"]) {
    --color-tpg10-bg: #001213;
    --color-tpg10-bg: oklch(0.165 0.03 200);
    --color-tpg10-glow: #003a2773;
    --color-tpg10-glow: oklch(0.3 0.08 170 / 0.45);
    --color-tpg10-glow2: #34347059;
    --color-tpg10-glow2: oklch(0.36 0.1 280 / 0.35);
    --color-tpg10-card: #041b1b;
    --color-tpg10-card: oklch(0.205 0.03 195);
    --color-tpg10-sunk: #062424;
    --color-tpg10-sunk: oklch(0.24 0.035 195);
    --color-tpg10-ink: #e8f1ef;
    --color-tpg10-ink: oklch(0.95 0.01 180);
    --color-tpg10-mut: #a0bbb7;
    --color-tpg10-mut: oklch(0.77 0.03 185);
    --color-tpg10-line: #173937;
    --color-tpg10-line: oklch(0.32 0.04 190);
    --color-tpg10-band: #1d2248;
    --color-tpg10-band: oklch(0.27 0.07 275);
    --color-tpg10-band2: #343470;
    --color-tpg10-band2: oklch(0.36 0.1 280);
    --color-tpg10-band-ink: #f3f5fc;
    --color-tpg10-band-ink: oklch(0.97 0.01 275);
    --color-tpg10-band-mut: #c2c9e5;
    --color-tpg10-band-mut: oklch(0.84 0.04 275);
    --color-tpg10-jade: #43d59a;
    --color-tpg10-jade: oklch(0.78 0.15 162);
    --color-tpg10-teal: #47d0bd;
    --color-tpg10-teal: oklch(0.78 0.12 182);
    --color-tpg10-jade-ink: #5ed8a9;
    --color-tpg10-jade-ink: oklch(0.8 0.13 165);
    --color-tpg10-ring: #5ed8a9;
    --color-tpg10-ring: oklch(0.8 0.13 165);
    --color-tpg10-ok: #66d592;
    --color-tpg10-ok: oklch(0.79 0.14 155);
    --color-tpg10-warn: #f0be67;
    --color-tpg10-warn: oklch(0.83 0.12 80);
    --color-tpg10-due: #fb817a;
    --color-tpg10-due: oklch(0.74 0.15 25);
  }
}

.tpg-10[data-theme="dark"] {
  --color-tpg10-bg: #001213;
  --color-tpg10-bg: oklch(0.165 0.03 200);
  --color-tpg10-glow: #003a2773;
  --color-tpg10-glow: oklch(0.3 0.08 170 / 0.45);
  --color-tpg10-glow2: #34347059;
  --color-tpg10-glow2: oklch(0.36 0.1 280 / 0.35);
  --color-tpg10-card: #041b1b;
  --color-tpg10-card: oklch(0.205 0.03 195);
  --color-tpg10-sunk: #062424;
  --color-tpg10-sunk: oklch(0.24 0.035 195);
  --color-tpg10-ink: #e8f1ef;
  --color-tpg10-ink: oklch(0.95 0.01 180);
  --color-tpg10-mut: #a0bbb7;
  --color-tpg10-mut: oklch(0.77 0.03 185);
  --color-tpg10-line: #173937;
  --color-tpg10-line: oklch(0.32 0.04 190);
  --color-tpg10-band: #1d2248;
  --color-tpg10-band: oklch(0.27 0.07 275);
  --color-tpg10-band2: #343470;
  --color-tpg10-band2: oklch(0.36 0.1 280);
  --color-tpg10-band-ink: #f3f5fc;
  --color-tpg10-band-ink: oklch(0.97 0.01 275);
  --color-tpg10-band-mut: #c2c9e5;
  --color-tpg10-band-mut: oklch(0.84 0.04 275);
  --color-tpg10-jade: #43d59a;
  --color-tpg10-jade: oklch(0.78 0.15 162);
  --color-tpg10-teal: #47d0bd;
  --color-tpg10-teal: oklch(0.78 0.12 182);
  --color-tpg10-jade-ink: #5ed8a9;
  --color-tpg10-jade-ink: oklch(0.8 0.13 165);
  --color-tpg10-ring: #5ed8a9;
  --color-tpg10-ring: oklch(0.8 0.13 165);
  --color-tpg10-ok: #66d592;
  --color-tpg10-ok: oklch(0.79 0.14 155);
  --color-tpg10-warn: #f0be67;
  --color-tpg10-warn: oklch(0.83 0.12 80);
  --color-tpg10-due: #fb817a;
  --color-tpg10-due: oklch(0.74 0.15 25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-10 {
  width: 100%;
  min-height: 100svh;
}
```
