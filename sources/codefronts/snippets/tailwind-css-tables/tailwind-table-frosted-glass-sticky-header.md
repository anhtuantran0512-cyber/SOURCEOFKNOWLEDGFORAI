---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-table-frosted-glass-sticky-header/"
title: "Tailwind Table with Frosted Glass Sticky Header"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "An orders table whose sticky header is a pane of frosted glass: rows blur and saturate as they scroll beneath it, while column titles stay pin-sharp on a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Table with Frosted Glass Sticky Header
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-table-frosted-glass-sticky-header/

An orders table whose sticky header is a pane of frosted glass: rows blur and saturate as they scroll beneath it, while column titles stay pin-sharp on a tinted rim-lit strip. The upgrade adds a matching sticky glass footer with the running total, so the number that matters never scrolls away, and a solid-tint fallback where backdrop-filter is missing.
## HTML
```html
<section class="ttb-13 grid-cols-1 w-full min-h-svh grid place-items-center bg-linear-135 from-[#3a1c71] via-[#d76d77] to-[#ffaf7b] px-5 py-14 font-ttb13-sans text-white" aria-label="Frosted glass sticky header table demo">
  <div class="w-full max-w-xl">
    <header class="mb-4 flex items-end justify-between gap-3">
      <div>
        <h2 class="text-xl font-bold tracking-tight">Recent orders</h2>
        <p class="mt-0.5 text-sm text-white/85">Scroll the table — rows frost beneath the header</p>
      </div>
      <span class="rounded-full bg-white/15 px-3 py-1 text-xs font-semibold ring-1 ring-white/30">Today</span>
    </header>
    <div tabindex="0" role="region" aria-label="Recent orders, scrollable" class="relative max-h-80 overflow-auto rounded-[20px] bg-white/8 shadow-[0_26px_56px_-28px_oklch(0_0_0/0.65)] ring-1 ring-white/30 [scrollbar-color:oklch(1_0_0/0.4)_transparent] [scrollbar-width:thin] focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white">
      <table class="w-full border-collapse text-left text-sm">
        <caption class="sr-only">Recent orders with customer, payment status and total</caption>
        <thead class="[&_th]:sticky [&_th]:top-0 [&_th]:z-10 [&_th]:bg-ttb13-glass [&_th]:px-4 [&_th]:py-3.5 [&_th]:text-[11px] [&_th]:font-bold [&_th]:tracking-[0.08em] [&_th]:uppercase [&_th]:shadow-[inset_0_1px_0_oklch(1_0_0/0.55),inset_0_-1px_0_oklch(1_0_0/0.4)] supports-[backdrop-filter:blur(1px)]:[&_th]:bg-white/20 supports-[backdrop-filter:blur(1px)]:[&_th]:backdrop-blur-md supports-[backdrop-filter:blur(1px)]:[&_th]:backdrop-saturate-[1.8]">
          <tr><th scope="col">Order</th><th scope="col">Customer</th><th scope="col">Status</th><th scope="col" class="text-right">Total</th></tr>
        </thead>
        <tbody class="[&_td]:border-b [&_td]:border-white/14 [&_td]:px-4 [&_td]:py-3 [&_tr]:transition-colors [&_tr:hover]:bg-white/12 [&_tr:nth-child(odd)]:bg-white/6">
          <tr><td class="font-semibold tabular-nums">#10241</td><td>A. Rivera</td><td><span class="rounded-full bg-emerald-500/60 px-2.5 py-0.5 text-xs font-bold">Paid</span></td><td class="text-right font-semibold tabular-nums">$1,204</td></tr>
          <tr><td class="font-semibold tabular-nums">#10240</td><td>M. Chen</td><td><span class="rounded-full bg-amber-400/60 px-2.5 py-0.5 text-xs font-bold text-amber-950">Pending</span></td><td class="text-right font-semibold tabular-nums">$486</td></tr>
          <tr><td class="font-semibold tabular-nums">#10239</td><td>S. Okafor</td><td><span class="rounded-full bg-emerald-500/60 px-2.5 py-0.5 text-xs font-bold">Paid</span></td><td class="text-right font-semibold tabular-nums">$2,940</td></tr>
          <tr><td class="font-semibold tabular-nums">#10238</td><td>J. Nowak</td><td><span class="rounded-full bg-amber-400/60 px-2.5 py-0.5 text-xs font-bold text-amber-950">Pending</span></td><td class="text-right font-semibold tabular-nums">$318</td></tr>
          <tr><td class="font-semibold tabular-nums">#10237</td><td>L. Haddad</td><td><span class="rounded-full bg-emerald-500/60 px-2.5 py-0.5 text-xs font-bold">Paid</span></td><td class="text-right font-semibold tabular-nums">$1,775</td></tr>
          <tr><td class="font-semibold tabular-nums">#10236</td><td>R. Bianchi</td><td><span class="rounded-full bg-white/25 px-2.5 py-0.5 text-xs font-bold">Refunded</span></td><td class="text-right font-semibold text-white/80 line-through tabular-nums">$642</td></tr>
          <tr><td class="font-semibold tabular-nums">#10235</td><td>K. Andersen</td><td><span class="rounded-full bg-amber-400/60 px-2.5 py-0.5 text-xs font-bold text-amber-950">Pending</span></td><td class="text-right font-semibold tabular-nums">$3,510</td></tr>
          <tr><td class="font-semibold tabular-nums">#10234</td><td>T. Mbeki</td><td><span class="rounded-full bg-emerald-500/60 px-2.5 py-0.5 text-xs font-bold">Paid</span></td><td class="text-right font-semibold tabular-nums">$925</td></tr>
        </tbody>
        <tfoot class="[&_td]:sticky [&_td]:bottom-0 [&_td]:z-10 [&_td]:bg-ttb13-glass [&_td]:px-4 [&_td]:py-3.5 [&_td]:font-bold [&_td]:shadow-[inset_0_1px_0_oklch(1_0_0/0.45)] supports-[backdrop-filter:blur(1px)]:[&_td]:bg-white/20 supports-[backdrop-filter:blur(1px)]:[&_td]:backdrop-blur-md supports-[backdrop-filter:blur(1px)]:[&_td]:backdrop-saturate-[1.8]">
          <tr><td colspan="3">8 orders · 7 net</td><td class="text-right text-base tabular-nums">$11,158</td></tr>
        </tfoot>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb13-glass: #8e4a74;
  --color-ttb13-glass: oklch(0.5 0.11 345 / 0.92);
  --font-ttb13-sans: 'Onest', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-13 {
  width: 100%;
  min-height: 100svh;
}
```
