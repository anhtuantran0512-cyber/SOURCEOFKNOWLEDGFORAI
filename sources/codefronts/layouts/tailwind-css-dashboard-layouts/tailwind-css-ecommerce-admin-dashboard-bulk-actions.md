---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-ecommerce-admin-dashboard-bulk-actions/"
title: "Tailwind CSS E-commerce Admin Dashboard with Bulk Actions"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "Merchant-panel density with zero JavaScript: a stat strip, an orders table and a quick-action rail."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS E-commerce Admin Dashboard with Bulk Actions
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-ecommerce-admin-dashboard-bulk-actions/

Merchant-panel density with zero JavaScript: a stat strip, an orders table and a quick-action rail. Tick any order and a bulk-actions bar slides up via group-has-[tbody_input:checked]/card:translate-y-0 &mdash; and now it counts your selection with a CSS counter and the filter tabs really filter, each row hiding itself with group-has-[#tdl09-unpaid:checked]/card:hidden.
## HTML
```html
<section class="tdl-09 @container/panel w-full min-h-svh bg-tdl09-bg bg-linear-175 from-tdl09-bg to-tdl09-bg2 font-tdl09-sans text-tdl09-ink antialiased" aria-label="E-commerce merchant panel demo">
  <div class="grid h-svh min-h-[36rem] grid-cols-[minmax(0,1fr)_16rem] grid-rows-[auto_minmax(0,1fr)] gap-3.5 p-4 @max-[45rem]/panel:h-auto @max-[45rem]/panel:grid-cols-1 @max-[45rem]/panel:grid-rows-none">
    <div class="col-span-full grid grid-cols-[repeat(auto-fit,minmax(min(10rem,100%),1fr))] gap-3 [&>article]:rounded-2xl [&>article]:border [&>article]:border-tdl09-edge [&>article]:bg-tdl09-panel [&>article]:px-4 [&>article]:py-3.25 [&_h3]:text-[10.5px] [&_h3]:font-bold [&_h3]:tracking-[0.1em] [&_h3]:text-tdl09-mut [&_h3]:uppercase [&_p]:mt-1 [&_p]:mb-px [&_p]:text-[22px] [&_p]:font-extrabold [&_p]:tracking-tight [&_p]:tabular-nums [&_small]:text-[11.5px] [&_small]:font-semibold [&_small]:text-tdl09-mut">
      <article><h3>Today's sales</h3><p>$4,982</p><small class="text-tdl09-good!">▲ 9.4% vs yesterday</small></article>
      <article><h3>Open orders</h3><p>37</p><small>12 awaiting shipment</small></article>
      <article><h3>Conversion</h3><p>3.1%</p><small class="text-tdl09-good!">▲ 0.3 pts</small></article>
      <article><h3>Low stock</h3><p>5 SKUs</p><small class="text-tdl09-warnink!">restock soon</small></article>
    </div>
    <div class="group/card relative flex min-w-0 flex-col overflow-hidden rounded-2xl border border-tdl09-edge bg-tdl09-panel [counter-reset:tdl09] @max-[45rem]/panel:min-h-[26rem]">
      <header class="flex flex-wrap items-center justify-between gap-3 border-b border-tdl09-edge px-4 py-3.5">
        <h2 class="text-base font-bold">Orders</h2>
        <fieldset class="flex gap-1 rounded-xl border border-tdl09-edge bg-tdl09-bg p-0.75 [&>label]:grid [&>label]:h-8.5 [&>label]:cursor-pointer [&>label]:place-items-center [&>label]:rounded-lg [&>label]:px-3 [&>label]:text-xs [&>label]:font-bold [&>label]:text-tdl09-mut [&>label]:transition [&>label:hover]:text-tdl09-ink [&>label:has(:checked)]:bg-tdl09-panel [&>label:has(:checked)]:text-tdl09-ink [&>label:has(:checked)]:shadow-[0_1px_3px_var(--color-tdl09-shadow)] [&>label:has(:focus-visible)]:outline-2 [&>label:has(:focus-visible)]:-outline-offset-2 [&>label:has(:focus-visible)]:outline-tdl09-acc">
          <legend class="sr-only">Filter orders</legend>
          <label><input class="sr-only" type="radio" name="tdl09-f" id="tdl09-all" checked>All</label>
          <label><input class="sr-only" type="radio" name="tdl09-f" id="tdl09-unf">Unfulfilled</label>
          <label><input class="sr-only" type="radio" name="tdl09-f" id="tdl09-unpaid">Unpaid</label>
          <label><input class="sr-only" type="radio" name="tdl09-f" id="tdl09-ref">Refunded</label>
        </fieldset>
      </header>
      <div role="region" aria-label="Orders table, scrollable" tabindex="0" class="min-h-0 min-w-0 flex-1 overflow-auto overscroll-contain pb-16 focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tdl09-acc">
        <table class="w-full border-collapse text-[13px] [&_td]:border-b [&_td]:border-tdl09-edge/50 [&_td]:px-3.5 [&_td]:py-2.75 [&_td]:whitespace-nowrap [&_th]:sticky [&_th]:top-0 [&_th]:z-10 [&_th]:border-b [&_th]:border-tdl09-edge [&_th]:bg-tdl09-panel [&_th]:px-3.5 [&_th]:py-2.5 [&_th]:text-left [&_th]:text-[10.5px] [&_th]:font-bold [&_th]:tracking-[0.09em] [&_th]:text-tdl09-mut [&_th]:uppercase [&_tbody_tr]:transition-colors [&_tbody_tr:nth-child(even)]:bg-tdl09-zebra [&_tbody_tr:hover]:bg-tdl09-acc/5 [&_tbody_tr:has(:checked)]:bg-tdl09-acc/9 [&_tbody_tr:has(:checked)_td:first-child]:shadow-[inset_3px_0_0_var(--color-tdl09-acc)] [&_td:first-child]:w-11 [&_td:first-child]:text-center [&_td:last-child]:text-right [&_td:last-child]:tabular-nums [&_th:last-child]:text-right [&_input]:size-4 [&_input]:cursor-pointer [&_input]:accent-tdl09-acc [&_input]:align-middle [&_input:focus-visible]:outline-2 [&_input:focus-visible]:outline-offset-2 [&_input:focus-visible]:outline-tdl09-acc [&_tbody_input:checked]:[counter-increment:tdl09] [&_td:nth-child(2)]:font-semibold">
          <caption class="sr-only">Recent orders — select rows to reveal bulk actions</caption>
          <thead><tr><th scope="col" class="w-11"><span class="sr-only">Select</span></th><th scope="col">Order</th><th scope="col">Customer</th><th scope="col">Status</th><th scope="col">Total</th></tr></thead>
          <tbody>
            <tr class="group-has-[#tdl09-unpaid:checked]/card:hidden group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1207"></td><td>#1207</td><td>Ava Thompson</td><td><span class="rounded-full bg-tdl09-good/12 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-good">Paid</span></td><td>$129.00</td></tr>
            <tr class="group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1206"></td><td>#1206</td><td>Noah Clarke</td><td><span class="rounded-full bg-tdl09-warn/18 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-warnink">Pending</span></td><td>$54.50</td></tr>
            <tr class="group-has-[#tdl09-unpaid:checked]/card:hidden group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1205"></td><td>#1205</td><td>Isla Morgan</td><td><span class="rounded-full bg-tdl09-good/12 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-good">Paid</span></td><td>$310.99</td></tr>
            <tr class="group-has-[#tdl09-unf:checked]/card:hidden group-has-[#tdl09-unpaid:checked]/card:hidden group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1204"></td><td>#1204</td><td>Leo Bennett</td><td><span class="rounded-full bg-tdl09-ship/11 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-ship">Shipped</span></td><td>$89.00</td></tr>
            <tr class="group-has-[#tdl09-unf:checked]/card:hidden group-has-[#tdl09-unpaid:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1203"></td><td>#1203</td><td>Mia Foster</td><td><span class="rounded-full bg-tdl09-bad/10 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-bad">Refunded</span></td><td>−$47.20</td></tr>
            <tr class="group-has-[#tdl09-unpaid:checked]/card:hidden group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1202"></td><td>#1202</td><td>Ethan Hayes</td><td><span class="rounded-full bg-tdl09-good/12 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-good">Paid</span></td><td>$214.30</td></tr>
            <tr class="group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1201"></td><td>#1201</td><td>Grace Liu</td><td><span class="rounded-full bg-tdl09-warn/18 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-warnink">Pending</span></td><td>$76.80</td></tr>
            <tr class="group-has-[#tdl09-unf:checked]/card:hidden group-has-[#tdl09-unpaid:checked]/card:hidden group-has-[#tdl09-ref:checked]/card:hidden"><td><input type="checkbox" aria-label="Select order 1200"></td><td>#1200</td><td>Oliver Grant</td><td><span class="rounded-full bg-tdl09-ship/11 px-2.5 py-0.75 text-[11px] font-bold text-tdl09-ship">Shipped</span></td><td>$158.40</td></tr>
          </tbody>
        </table>
      </div>
      <div role="toolbar" aria-label="Bulk actions" class="invisible absolute inset-x-3 bottom-2.5 z-20 flex translate-y-[130%] flex-wrap items-center gap-2 rounded-xl bg-tdl09-dark px-3.5 py-2.5 text-white opacity-0 shadow-[0_16px_34px_-14px_var(--color-tdl09-shadow)] transition-[translate,opacity,visibility] duration-300 ease-[cubic-bezier(.2,.7,.2,1)] group-has-[tbody_input:checked]/card:visible group-has-[tbody_input:checked]/card:translate-y-0 group-has-[tbody_input:checked]/card:opacity-100 [&>button]:h-9 [&>button]:cursor-pointer [&>button]:rounded-lg [&>button]:border [&>button]:border-white/20 [&>button]:bg-white/8 [&>button]:px-3 [&>button]:text-xs [&>button]:font-bold [&>button]:transition-colors [&>button:hover]:bg-white/16 [&>button:focus-visible]:outline-2 [&>button:focus-visible]:outline-offset-2 [&>button:focus-visible]:outline-tdl09-acc2">
        <b class="mr-auto text-[13px] after:ml-1 after:font-normal after:text-white/75 after:content-['selected']"><span class="inline-grid min-w-6 place-items-center rounded-md bg-tdl09-acc px-1.5 tabular-nums after:content-[counter(tdl09)]"></span></b>
        <button type="button">Fulfill</button><button type="button">Print labels</button><button type="button" class="border-tdl09-bad/60! bg-tdl09-bad/35! hover:bg-tdl09-bad/55!">Archive</button>
      </div>
    </div>
    <aside aria-label="Quick actions" class="flex min-h-0 flex-col gap-2.25 overflow-y-auto rounded-2xl border border-tdl09-edge bg-tdl09-panel p-4 [&>h2]:text-[11px] [&>h2]:font-bold [&>h2]:tracking-[0.1em] [&>h2]:text-tdl09-mut [&>h2]:uppercase [&>button]:grid [&>button]:min-h-11 [&>button]:cursor-pointer [&>button]:grid-cols-[2rem_minmax(0,1fr)] [&>button]:items-center [&>button]:gap-x-2.5 [&>button]:rounded-xl [&>button]:border [&>button]:border-tdl09-edge [&>button]:bg-tdl09-bg [&>button]:px-3 [&>button]:py-2.5 [&>button]:text-left [&>button]:transition [&>button:hover]:-translate-y-px [&>button:hover]:border-tdl09-acc/50 [&>button:hover]:bg-tdl09-acc/5 [&>button:focus-visible]:outline-2 [&>button:focus-visible]:outline-offset-2 [&>button:focus-visible]:outline-tdl09-acc [&_button_i]:row-span-2 [&_button_i]:grid [&_button_i]:size-8 [&_button_i]:place-items-center [&_button_i]:rounded-lg [&_button_i]:bg-tdl09-acc/12 [&_button_i]:text-sm [&_button_i]:font-bold [&_button_i]:text-tdl09-accink [&_button_i]:not-italic [&_button_b]:text-[13px] [&_button_span]:text-[11px] [&_button_span]:text-tdl09-mut">
      <h2>Quick actions</h2>
      <button type="button"><i aria-hidden="true">＋</i><b>Add product</b><span>Catalog</span></button>
      <button type="button"><i aria-hidden="true">⤓</i><b>Export orders</b><span>CSV · last 30 days</span></button>
      <button type="button"><i aria-hidden="true">%</i><b>Create discount</b><span>Storewide or SKU</span></button>
      <h2 class="mt-2.5">Inventory alerts</h2>
      <ul class="grid gap-2 [&>li]:flex [&>li]:justify-between [&>li]:gap-2 [&>li]:rounded-xl [&>li]:border [&>li]:border-tdl09-warn/35 [&>li]:bg-tdl09-warn/8 [&>li]:px-3 [&>li]:py-2.25 [&>li]:text-xs [&_b]:font-semibold [&_span]:font-bold [&_span]:whitespace-nowrap [&_span]:text-tdl09-warnink">
        <li><b>Canvas Tote — Sand</b><span>3 left</span></li>
        <li><b>Trail Bottle 750ml</b><span>7 left</span></li>
        <li><b>Wool Runner 42</b><span>2 left</span></li>
      </ul>
    </aside>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl09-bg: #faf8f3;
  --color-tdl09-bg: oklch(0.977 0.006 85);
  --color-tdl09-bg2: #f3f0e8;
  --color-tdl09-bg2: oklch(0.955 0.01 85);
  --color-tdl09-panel: #ffffff;
  --color-tdl09-panel: oklch(1 0 0);
  --color-tdl09-zebra: #fcfbf8;
  --color-tdl09-zebra: oklch(0.988 0.004 85);
  --color-tdl09-edge: #e7e2d6;
  --color-tdl09-edge: oklch(0.91 0.015 85);
  --color-tdl09-ink: #2d2620;
  --color-tdl09-ink: oklch(0.27 0.02 60);
  --color-tdl09-mut: #685d52;
  --color-tdl09-mut: oklch(0.49 0.03 60);
  --color-tdl09-acc: #c27519;
  --color-tdl09-acc: oklch(0.62 0.14 62);
  --color-tdl09-accink: #8c4f00;
  --color-tdl09-accink: oklch(0.48 0.12 60);
  --color-tdl09-acc2: #f0b660;
  --color-tdl09-acc2: oklch(0.82 0.12 72);
  --color-tdl09-good: #17804a;
  --color-tdl09-good: oklch(0.52 0.13 155);
  --color-tdl09-warn: #d99a26;
  --color-tdl09-warn: oklch(0.72 0.14 75);
  --color-tdl09-warnink: #875800;
  --color-tdl09-warnink: oklch(0.48 0.1 72);
  --color-tdl09-bad: #c6372d;
  --color-tdl09-bad: oklch(0.56 0.19 27);
  --color-tdl09-ship: #2763c0;
  --color-tdl09-ship: oklch(0.52 0.15 255);
  --color-tdl09-dark: #2f2721;
  --color-tdl09-dark: oklch(0.27 0.025 60);
  --color-tdl09-shadow: #6b5640;
  --color-tdl09-shadow: oklch(0.42 0.05 60 / 0.45);
  --font-tdl09-sans: 'Manrope', system-ui, sans-serif;
}

.tdl-09 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tdl-09 * {
    transition: none !important;
  }
}
```
