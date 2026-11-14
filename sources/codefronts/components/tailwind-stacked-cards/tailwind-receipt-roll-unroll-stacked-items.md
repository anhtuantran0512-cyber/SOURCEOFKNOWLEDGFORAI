---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-receipt-roll-unroll-stacked-items/"
title: "Tailwind Receipt Roll Unroll Stacked Items"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "An order summary that unrolls like till paper."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Receipt Roll Unroll Stacked Items
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-receipt-roll-unroll-stacked-items/

An order summary that unrolls like till paper. The reveal is the familiar grid-rows-[0fr] &rarr; 1fr pair, but the memorable part is the perforated edge: one arbitrary [mask:radial-gradient(9px_at_50%_0,transparent_98%,#000)_repeat-x_0_0/18px_12px] cuts the zig-zag out of a plain block, and the direction arrow is a peer-checked:after:content swap rather than two rules.
## HTML
```html
<section class="stk-26 w-full min-h-svh flex items-start justify-center px-5 py-[10vh] font-stk26-sans bg-stk26-desk" aria-label="Unrolling receipt">
  <div class="relative w-[min(300px,100%)] rounded-t-[4px] bg-stk26-paper pb-3.5 shadow-[0_24px_50px_-24px_rgba(0,0,0,0.6)]">
    <input class="peer sr-only" type="checkbox" id="stk-26-t" checked>
    <label class="flex cursor-pointer flex-col items-center gap-1 border-b-2 border-dashed border-stk26-dash px-4 pt-5 pb-3.5 peer-focus-visible:outline-3 peer-focus-visible:outline-stk26-ring peer-focus-visible:outline-offset-2" for="stk-26-t">
      <b class="font-stk26-mono text-[13px] font-bold tracking-[0.06em] text-stk26-ink">CODEFRONTS &middot; Order #2261</b>
      <span class="font-stk26-mono text-[11px] tracking-[0.12em] uppercase text-stk26-faint after:content-['_&#9660;'] peer-checked:after:content-['_&#9650;']">Tap to roll</span>
    </label>
    <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-550 ease-stk26 peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
      <div class="overflow-hidden font-stk26-mono">
        <div class="flex justify-between px-5 py-2.25 text-[13px] text-stk26-body"><span>Stacked Cards Pack</span><span>$29.00</span></div>
        <div class="flex justify-between px-5 py-2.25 text-[13px] text-stk26-body"><span>Carousel Add-on</span><span>$14.00</span></div>
        <div class="flex justify-between px-5 py-2.25 text-[13px] text-stk26-body"><span>Lifetime updates</span><span>$12.00</span></div>
        <div class="mt-1.5 flex justify-between border-t border-dashed border-stk26-dash px-5 py-2.25 text-[13px] text-stk26-body"><span>Subtotal</span><span>$55.00</span></div>
        <div class="flex justify-between px-5 py-2.25 text-[13px] text-stk26-body"><span>Tax</span><span>$4.40</span></div>
        <div class="flex justify-between border-t-2 border-stk26-ink px-5 py-2.25 text-[15px] font-bold text-stk26-ink"><span>Total</span><span>$59.40</span></div>
        <p class="m-0 px-5 pt-3.5 pb-1.5 text-center font-stk26-mono text-xs tracking-[0.1em] text-stk26-faint">&starf; Thank you for your order &starf;</p>
      </div>
    </div>
    <span class="stk-26__perf block h-3 bg-stk26-paper [mask:radial-gradient(9px_at_50%_0,transparent_98%,#000)_repeat-x_0_0/18px_12px]" aria-hidden="true"></span>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk26-desk: #2b2a28;
  --color-stk26-desk: oklch(0.28 0.006 70);
  --color-stk26-paper: #fbfaf5;
  --color-stk26-paper: oklch(0.98 0.006 85);
  --color-stk26-dash: #d8d4c8;
  --color-stk26-dash: oklch(0.86 0.012 85);
  --color-stk26-ink: #2a2620;
  --color-stk26-ink: oklch(0.26 0.010 75);
  --color-stk26-body: #3a352c;
  --color-stk26-body: oklch(0.34 0.012 80);
  --color-stk26-faint: #8a8474;
  --color-stk26-faint: oklch(0.60 0.016 85);
  --color-stk26-ring: #5b78e8;
  --color-stk26-ring: oklch(0.60 0.17 262);
  --font-stk26-sans: 'Archivo', system-ui, sans-serif;
  --font-stk26-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk26: cubic-bezier(0.4, 0.9, 0.3, 1);
}
/* Older Safari and Chrome need the prefixed mask, and one class list cannot
   carry two declarations of the same property. */

.stk-26__perf {
  -webkit-mask: radial-gradient(9px at 50% 0, transparent 98%, #000) repeat-x 0 0 / 18px 12px;
}
```
