---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-with-ellipsis-for-large-page-ranges/"
title: "Tailwind CSS Pagination with Ellipsis for Large Page Ranges"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A data-table footer for 24 pages that always renders exactly seven slots &mdash; first, last, the neighbourhood of the current page and an ellipsis wherever…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pagination with Ellipsis for Large Page Ranges
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-with-ellipsis-for-large-page-ranges/

A data-table footer for 24 pages that always renders exactly seven slots &mdash; first, last, the neighbourhood of the current page and an ellipsis wherever the run really skips &mdash; so Previous and Next never jump under the pointer. The script only writes attributes (data-gap, aria-current, disabled); utilities like group-data-gap/s:hidden and aria-[current=page]:animate-tpg02-spin draw every state &mdash; including a rotating Lagoon conic ring around the current page.
## HTML
```html
<section class="tpg-02 w-full min-h-svh grid place-items-center bg-tpg02-bg bg-[radial-gradient(75%_60%_at_50%_0%,var(--color-tpg02-glow),transparent_72%)] px-5 py-14 font-tpg02-sans text-tpg02-ink antialiased" aria-label="Tailwind CSS pagination with ellipsis demo">
  <div class="grid w-full max-w-[46rem] justify-items-center gap-6">
    <article id="tpg-02-table" class="@container w-full overflow-hidden rounded-2xl bg-tpg02-card shadow-tpg02-card ring-1 ring-tpg02-line starting:translate-y-2 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none">
      <header class="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 px-4 pt-5 pb-4 sm:px-5">
        <div>
          <h2 class="text-[17px] font-semibold tracking-[-0.015em]">Shipments</h2>
          <p class="mt-0.5 text-[13px] text-tpg02-mut tabular-nums" role="status" aria-live="polite" data-status>Showing 31–35 of 120</p>
        </div>
        <p class="rounded-md bg-tpg02-acc/8 px-2 py-1 font-tpg02-mono text-[11.5px] text-tpg02-acc-ink tabular-nums ring-1 ring-tpg02-acc/20 ring-inset">24 pages · 5 per page</p>
      </header>
      <div class="overflow-x-auto border-y border-tpg02-line">
        <table class="w-full text-left text-[13.5px]">
          <thead class="bg-tpg02-sub text-[11.5px] font-medium tracking-[0.06em] text-tpg02-mut uppercase">
            <tr>
              <th scope="col" class="px-4 py-2.5 font-medium sm:px-5">Shipment</th>
              <th scope="col" class="px-4 py-2.5 font-medium sm:px-5">Destination</th>
              <th scope="col" class="px-4 py-2.5 font-medium max-sm:hidden sm:px-5">Carrier</th>
              <th scope="col" class="px-4 py-2.5 font-medium sm:px-5">Status</th>
              <th scope="col" class="px-4 py-2.5 text-right font-medium max-sm:hidden sm:px-5">ETA</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-tpg02-line">
          <tr class="transition-colors duration-150 hover:bg-tpg02-sub">
            <td class="px-4 py-3 sm:px-5 font-tpg02-mono text-[12.5px] font-medium tabular-nums" data-id>SHP-40031</td>
            <td class="px-4 py-3 sm:px-5">Rotterdam, NL</td>
            <td class="px-4 py-3 sm:px-5 text-tpg02-mut max-sm:hidden">DHL Freight</td>
            <td class="px-4 py-3 sm:px-5"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium whitespace-nowrap ring-1 ring-inset bg-tpg02-acc/10 text-tpg02-acc-ink ring-tpg02-acc/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>In transit</span></td>
            <td class="px-4 py-3 sm:px-5 text-right text-tpg02-mut tabular-nums max-sm:hidden">Oct 18</td>
          </tr>
          <tr class="transition-colors duration-150 hover:bg-tpg02-sub">
            <td class="px-4 py-3 sm:px-5 font-tpg02-mono text-[12.5px] font-medium tabular-nums" data-id>SHP-40032</td>
            <td class="px-4 py-3 sm:px-5">Austin, TX</td>
            <td class="px-4 py-3 sm:px-5 text-tpg02-mut max-sm:hidden">FedEx Ground</td>
            <td class="px-4 py-3 sm:px-5"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium whitespace-nowrap ring-1 ring-inset bg-tpg02-ok/10 text-tpg02-ok ring-tpg02-ok/20"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Delivered</span></td>
            <td class="px-4 py-3 sm:px-5 text-right text-tpg02-mut tabular-nums max-sm:hidden">Oct 12</td>
          </tr>
          <tr class="transition-colors duration-150 hover:bg-tpg02-sub">
            <td class="px-4 py-3 sm:px-5 font-tpg02-mono text-[12.5px] font-medium tabular-nums" data-id>SHP-40033</td>
            <td class="px-4 py-3 sm:px-5">Leeds, UK</td>
            <td class="px-4 py-3 sm:px-5 text-tpg02-mut max-sm:hidden">Royal Mail</td>
            <td class="px-4 py-3 sm:px-5"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium whitespace-nowrap ring-1 ring-inset bg-tpg02-ok/10 text-tpg02-ok ring-tpg02-ok/20"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Delivered</span></td>
            <td class="px-4 py-3 sm:px-5 text-right text-tpg02-mut tabular-nums max-sm:hidden">Oct 11</td>
          </tr>
          <tr class="transition-colors duration-150 hover:bg-tpg02-sub">
            <td class="px-4 py-3 sm:px-5 font-tpg02-mono text-[12.5px] font-medium tabular-nums" data-id>SHP-40034</td>
            <td class="px-4 py-3 sm:px-5">Auckland, NZ</td>
            <td class="px-4 py-3 sm:px-5 text-tpg02-mut max-sm:hidden">NZ Post</td>
            <td class="px-4 py-3 sm:px-5"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium whitespace-nowrap ring-1 ring-inset bg-tpg02-warn/10 text-tpg02-warn ring-tpg02-warn/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>Delayed</span></td>
            <td class="px-4 py-3 sm:px-5 text-right text-tpg02-mut tabular-nums max-sm:hidden">Oct 21</td>
          </tr>
          <tr class="transition-colors duration-150 hover:bg-tpg02-sub">
            <td class="px-4 py-3 sm:px-5 font-tpg02-mono text-[12.5px] font-medium tabular-nums" data-id>SHP-40035</td>
            <td class="px-4 py-3 sm:px-5">Toronto, CA</td>
            <td class="px-4 py-3 sm:px-5 text-tpg02-mut max-sm:hidden">Purolator</td>
            <td class="px-4 py-3 sm:px-5"><span class="inline-flex items-center gap-1.5 rounded-full px-2 py-0.5 text-[12px] font-medium whitespace-nowrap ring-1 ring-inset bg-tpg02-acc/10 text-tpg02-acc-ink ring-tpg02-acc/25"><span aria-hidden="true" class="size-1.5 rounded-full bg-current"></span>In transit</span></td>
            <td class="px-4 py-3 sm:px-5 text-right text-tpg02-mut tabular-nums max-sm:hidden">Oct 16</td>
          </tr>
          </tbody>
        </table>
      </div>
      <nav aria-label="Pagination" class="flex items-center justify-between gap-2 px-3 py-3 sm:px-4 @max-[34rem]:flex-wrap">
        <button type="button" data-prev class="inline-flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg bg-tpg02-card px-3.5 text-[14px] font-medium text-tpg02-ink shadow-tpg02-btn ring-1 ring-tpg02-line transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/8 hover:text-tpg02-acc-ink hover:ring-tpg02-acc/45 active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring disabled:cursor-not-allowed disabled:text-tpg02-mut disabled:opacity-55 disabled:shadow-none disabled:hover:bg-tpg02-card @max-[34rem]:flex-1"><svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>Previous</button>
        <ol class="flex items-center gap-0.5 @max-[34rem]:order-first @max-[34rem]:w-full @max-[34rem]:justify-center">
          <li data-slot class="group/s">
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="1" aria-label="Page 1">1</button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s" data-gap>
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="" aria-label="Page 0"></button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s">
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="6" aria-label="Page 6">6</button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s">
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="7" aria-label="Page 7" aria-current="page">7</button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s">
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="8" aria-label="Page 8">8</button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s" data-gap>
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="" aria-label="Page 0"></button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
          <li data-slot class="group/s">
            <button type="button" class="grid min-h-11 min-w-11 cursor-pointer place-items-center rounded-lg px-2 text-[14px] font-medium tabular-nums text-tpg02-ink border-2 border-transparent transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/10 hover:text-tpg02-acc-ink active:scale-95 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring group-data-gap/s:hidden aria-[current=page]:font-semibold aria-[current=page]:text-tpg02-acc-ink aria-[current=page]:shadow-tpg02-pill aria-[current=page]:[background:linear-gradient(var(--color-tpg02-cur),var(--color-tpg02-cur))_padding-box,conic-gradient(from_var(--tpg02-a),var(--color-tpg02-acc2),var(--color-tpg02-hi)_18%,var(--color-tpg02-acc)_40%,var(--color-tpg02-cur)_68%,var(--color-tpg02-acc2))_border-box] aria-[current=page]:animate-tpg02-spin motion-reduce:aria-[current=page]:animate-none" data-page="24" aria-label="Page 24">24</button>
            <span aria-hidden="true" class="hidden h-11 w-7 place-items-center font-bold tracking-[0.12em] text-tpg02-acc select-none group-data-gap/s:grid">…</span>
          </li>
        </ol>
        <button type="button" data-next class="inline-flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-lg bg-tpg02-card px-3.5 text-[14px] font-medium text-tpg02-ink shadow-tpg02-btn ring-1 ring-tpg02-line transition-[background-color,color,box-shadow,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none hover:bg-tpg02-acc/8 hover:text-tpg02-acc-ink hover:ring-tpg02-acc/45 active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg02-ring disabled:cursor-not-allowed disabled:text-tpg02-mut disabled:opacity-55 disabled:shadow-none disabled:hover:bg-tpg02-card @max-[34rem]:flex-1">Next<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      </nav>
    </article>
    <p class="flex flex-wrap items-center justify-center gap-1.5 text-[12.5px] text-tpg02-mut">Focus the pager, then <kbd class="rounded-md bg-tpg02-card px-1.5 py-0.5 font-tpg02-mono text-[11px] ring-1 ring-tpg02-line">←</kbd><kbd class="rounded-md bg-tpg02-card px-1.5 py-0.5 font-tpg02-mono text-[11px] ring-1 ring-tpg02-line">→</kbd><kbd class="rounded-md bg-tpg02-card px-1.5 py-0.5 font-tpg02-mono text-[11px] ring-1 ring-tpg02-line">Home</kbd><kbd class="rounded-md bg-tpg02-card px-1.5 py-0.5 font-tpg02-mono text-[11px] ring-1 ring-tpg02-line">End</kbd></p>
    <p aria-hidden="true" class="rounded-full bg-tpg02-card px-3.5 py-2 text-center font-tpg02-mono text-[11.5px] text-tpg02-mut ring-1 ring-tpg02-line">group-data-gap/s: · aria-[current=page]: · @container</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg02-bg: #e5f8fa;
  --color-tpg02-bg: oklch(0.966 0.02 205);
  --color-tpg02-glow: #93e5e9b3;
  --color-tpg02-glow: oklch(0.87 0.08 200 / 0.7);
  --color-tpg02-card: #fafeff;
  --color-tpg02-card: oklch(0.995 0.005 200);
  --color-tpg02-sub: #eaf9fa;
  --color-tpg02-sub: oklch(0.972 0.016 202);
  --color-tpg02-ink: #04232c;
  --color-tpg02-ink: oklch(0.24 0.04 220);
  --color-tpg02-mut: #41606a;
  --color-tpg02-mut: oklch(0.47 0.04 220);
  --color-tpg02-line: #c8e4e7;
  --color-tpg02-line: oklch(0.9 0.03 205);
  --color-tpg02-acc: #0092b8;
  --color-tpg02-acc: oklch(0.609 0.126 221.7);
  --color-tpg02-acc2: #009689;
  --color-tpg02-acc2: oklch(0.6 0.118 184.7);
  --color-tpg02-hi: #3ceedd;
  --color-tpg02-hi: oklch(0.86 0.14 185);
  --color-tpg02-cur: #d0f7f9;
  --color-tpg02-cur: oklch(0.95 0.04 200);
  --color-tpg02-acc-ink: #005e71;
  --color-tpg02-acc-ink: oklch(0.44 0.09 215);
  --color-tpg02-ring: #00829d;
  --color-tpg02-ring: oklch(0.55 0.12 215);
  --color-tpg02-ok: #007852;
  --color-tpg02-ok: oklch(0.5 0.12 165);
  --color-tpg02-warn: #a45e00;
  --color-tpg02-warn: oklch(0.55 0.13 65);
  --font-tpg02-sans: 'Geist', system-ui, sans-serif;
  --font-tpg02-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tpg02-card: 0 1px 2px oklch(0.3 0.06 215 / 0.07), 0 26px 56px -24px oklch(0.45 0.12 210 / 0.34);
  --shadow-tpg02-btn: 0 1px 2px oklch(0.3 0.06 215 / 0.08);
  --shadow-tpg02-pill: 0 6px 18px -6px oklch(0.6 0.13 205 / 0.55), inset 0 1px 0 oklch(1 0 0 / 0.35);
  --animate-tpg02-spin: tpg02-spin 3.6s linear infinite;

  @keyframes tpg02-spin {
    to {
      --tpg02-a: 360deg;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-02 {
  width: 100%;
  min-height: 100svh;
}
/* @property is an at-rule utilities can't emit: it makes --tpg02-a a typed <angle>, so the conic ring can animate. */

@property --tpg02-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tpg-02:not([data-theme="light"]) {
    --color-tpg02-bg: #00121b;
    --color-tpg02-bg: oklch(0.17 0.035 225);
    --color-tpg02-glow: #00404980;
    --color-tpg02-glow: oklch(0.33 0.08 205 / 0.5);
    --color-tpg02-card: #001c26;
    --color-tpg02-card: oklch(0.21 0.04 225);
    --color-tpg02-sub: #02232d;
    --color-tpg02-sub: oklch(0.24 0.042 222);
    --color-tpg02-ink: #e7f5f6;
    --color-tpg02-ink: oklch(0.96 0.015 200);
    --color-tpg02-mut: #98bcc2;
    --color-tpg02-mut: oklch(0.77 0.04 210);
    --color-tpg02-line: #113b47;
    --color-tpg02-line: oklch(0.33 0.05 220);
    --color-tpg02-acc: #00b2d1;
    --color-tpg02-acc: oklch(0.7 0.13 215);
    --color-tpg02-acc2: #2bbdaa;
    --color-tpg02-acc2: oklch(0.72 0.12 182);
    --color-tpg02-hi: #67f1e9;
    --color-tpg02-hi: oklch(0.88 0.12 190);
    --color-tpg02-cur: #002e36;
    --color-tpg02-cur: oklch(0.27 0.06 210);
    --color-tpg02-acc-ink: #7de8ee;
    --color-tpg02-acc-ink: oklch(0.87 0.1 200);
    --color-tpg02-ring: #43d5dc;
    --color-tpg02-ring: oklch(0.8 0.12 200);
    --color-tpg02-ok: #5ed8a9;
    --color-tpg02-ok: oklch(0.8 0.13 165);
    --color-tpg02-warn: #f5b75b;
    --color-tpg02-warn: oklch(0.82 0.13 75);
  }
}

.tpg-02[data-theme="dark"] {
  --color-tpg02-bg: #00121b;
  --color-tpg02-bg: oklch(0.17 0.035 225);
  --color-tpg02-glow: #00404980;
  --color-tpg02-glow: oklch(0.33 0.08 205 / 0.5);
  --color-tpg02-card: #001c26;
  --color-tpg02-card: oklch(0.21 0.04 225);
  --color-tpg02-sub: #02232d;
  --color-tpg02-sub: oklch(0.24 0.042 222);
  --color-tpg02-ink: #e7f5f6;
  --color-tpg02-ink: oklch(0.96 0.015 200);
  --color-tpg02-mut: #98bcc2;
  --color-tpg02-mut: oklch(0.77 0.04 210);
  --color-tpg02-line: #113b47;
  --color-tpg02-line: oklch(0.33 0.05 220);
  --color-tpg02-acc: #00b2d1;
  --color-tpg02-acc: oklch(0.7 0.13 215);
  --color-tpg02-acc2: #2bbdaa;
  --color-tpg02-acc2: oklch(0.72 0.12 182);
  --color-tpg02-hi: #67f1e9;
  --color-tpg02-hi: oklch(0.88 0.12 190);
  --color-tpg02-cur: #002e36;
  --color-tpg02-cur: oklch(0.27 0.06 210);
  --color-tpg02-acc-ink: #7de8ee;
  --color-tpg02-acc-ink: oklch(0.87 0.1 200);
  --color-tpg02-ring: #43d5dc;
  --color-tpg02-ring: oklch(0.8 0.12 200);
  --color-tpg02-ok: #5ed8a9;
  --color-tpg02-ok: oklch(0.8 0.13 165);
  --color-tpg02-warn: #f5b75b;
  --color-tpg02-warn: oklch(0.82 0.13 75);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-02-table');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const nav = root.querySelector('nav');
  const slots = [...root.querySelectorAll('[data-slot]')];
  const prev = root.querySelector('[data-prev]');
  const next = root.querySelector('[data-next]');
  const status = root.querySelector('[data-status]');
  const ids = [...root.querySelectorAll('[data-id]')];
  const total = 24, per = 5, records = 120;
  let current = 7;
  const windowOf = (c) => {
    if (total <= 7) return Array.from({ length: total }, (_, i) => i + 1);
    if (c <= 4) return [1, 2, 3, 4, 5, 0, total];
    if (c >= total - 3) return [1, 0, total - 4, total - 3, total - 2, total - 1, total];
    return [1, 0, c - 1, c, c + 1, 0, total];
  };
  const focusCurrent = () => root.querySelector('[aria-current="page"]').focus();
  const go = (p) => {
    current = Math.min(total, Math.max(1, p));
    const pages = windowOf(current);
    slots.forEach((li, i) => {
      const n = pages[i], b = li.querySelector('button');
      li.hidden = n === undefined;
      li.toggleAttribute('data-gap', n === 0);
      b.textContent = n || '';
      b.dataset.page = n || '';
      b.setAttribute('aria-label', 'Page ' + n);
      if (n === current) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current');
    });
    prev.disabled = current === 1;
    next.disabled = current === total;
    const first = (current - 1) * per + 1;
    ids.forEach((el, i) => { el.textContent = 'SHP-' + (40000 + first + i); });
    status.textContent = 'Showing ' + first + '–' + current * per + ' of ' + records;
  };
  slots.forEach((li) => li.querySelector('button').addEventListener('click', (e) => { go(+e.currentTarget.dataset.page); focusCurrent(); }));
  prev.addEventListener('click', () => { go(current - 1); if (prev.disabled) focusCurrent(); });
  next.addEventListener('click', () => { go(current + 1); if (next.disabled) focusCurrent(); });
  nav.addEventListener('keydown', (e) => {
    const to = { ArrowLeft: current - 1, ArrowRight: current + 1, Home: 1, End: total }[e.key];
    if (to === undefined) return;
    e.preventDefault(); go(to); focusCurrent();
  });
})();
```
