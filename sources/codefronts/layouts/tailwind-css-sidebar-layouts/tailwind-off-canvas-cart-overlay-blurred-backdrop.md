---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-off-canvas-cart-overlay-blurred-backdrop/"
title: "Tailwind Off-Canvas Cart Overlay with Blurred Backdrop Scrim"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The modal-grade overlay drawer: content dims and blurs behind a scrim, the panel lifts on a shadow that fades in with the slide, and pointer-events…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Off-Canvas Cart Overlay with Blurred Backdrop Scrim
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-off-canvas-cart-overlay-blurred-backdrop/

The modal-grade overlay drawer: content dims and blurs behind a scrim, the panel lifts on a shadow that fades in with the slide, and pointer-events discipline keeps the dimmed page genuinely inert. A cart, because that is the pattern's home.
## HTML
```html
<section class="tsl-19 relative w-full h-svh min-h-svh grid grid-rows-[auto_1fr] overflow-hidden font-tsl19-sans bg-tsl19-bg text-tsl19-ink">
  <input type="checkbox" id="tsl19-o" class="sr-only peer">
  <header class="flex items-center justify-between h-14 px-5 bg-white border-b border-tsl19-line text-[15px] font-bold">
    <strong>Alpine Supply Co.</strong>
    <label for="tsl19-o" class="inline-flex items-center gap-2.5 min-h-11 px-3.5 rounded-[10px] border border-tsl19-line text-[13px] font-semibold cursor-pointer transition-colors duration-200 hover:bg-tsl19-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[17px] h-[17px] fill-none stroke-current stroke-[1.9] [stroke-linecap:round] [stroke-linejoin:round]"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>Cart &middot; 2</label>
  </header>
  <main class="p-[26px] overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="mb-[18px] text-[21px] font-bold leading-tight">New arrivals</h1>
    <div class="grid grid-cols-[repeat(auto-fill,minmax(140px,1fr))] gap-3.5">
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
      <div class="aspect-[3/4] rounded-xl bg-[linear-gradient(150deg,oklch(0.93_0.01_145),oklch(0.87_0.015_145))]"></div>
    </div>
  </main>
  <label for="tsl19-o" aria-hidden="true" class="tsl-19-scrim absolute inset-0 z-[3] bg-[oklch(0_0_0/0.45)] backdrop-blur-[4px] opacity-0 pointer-events-none transition-opacity duration-300 motion-reduce:transition-none"></label>
  <aside aria-label="Shopping cart" class="tsl-19-cart absolute inset-y-0 right-0 z-[4] flex flex-col w-[min(340px,92vw)] p-[18px] bg-white border-l border-tsl19-line translate-x-full transition-[translate,box-shadow] duration-[320ms] ease-[cubic-bezier(.4,0,.2,1)] motion-reduce:transition-none">
    <div class="flex items-center justify-between pb-4">
      <h2 class="text-base font-bold">Your cart</h2>
      <label for="tsl19-o" aria-label="Close cart" class="grid place-items-center w-11 h-11 rounded-[9px] text-tsl19-mut cursor-pointer transition-colors duration-200 hover:text-tsl19-ink hover:bg-tsl19-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-[17px] h-[17px] fill-none stroke-current stroke-[1.9] [stroke-linecap:round]"><path d="M6 6l12 12M18 6 6 18"/></svg></label>
    </div>
    <div class="grid grid-cols-[auto_1fr_auto] gap-3 items-center py-3 border-t border-tsl19-line"><span aria-hidden="true" class="w-[52px] h-[52px] rounded-[10px] bg-[linear-gradient(150deg,oklch(0.9_0.012_145),oklch(0.84_0.018_145))]"></span><span><strong class="block text-[13.5px] font-semibold leading-snug">Ridge shell jacket</strong><small class="text-xs leading-snug text-tsl19-mut">Moss &middot; M</small></span><data class="text-[13.5px] font-semibold tabular-nums">$168</data></div>
    <div class="grid grid-cols-[auto_1fr_auto] gap-3 items-center py-3 border-t border-tsl19-line"><span aria-hidden="true" class="w-[52px] h-[52px] rounded-[10px] bg-[linear-gradient(150deg,oklch(0.9_0.012_145),oklch(0.84_0.018_145))]"></span><span><strong class="block text-[13.5px] font-semibold leading-snug">Trail merino crew</strong><small class="text-xs leading-snug text-tsl19-mut">Ash &middot; L</small></span><data class="text-[13.5px] font-semibold tabular-nums">$74</data></div>
    <div class="mt-auto grid grid-cols-[1fr_auto] items-center gap-3.5 pt-4 border-t border-tsl19-line text-sm font-medium text-tsl19-mut">
      <span>Subtotal</span><data class="text-[13.5px] font-semibold tabular-nums text-tsl19-ink">$242</data>
      <button type="button" class="col-span-full min-h-12 rounded-[11px] border-0 bg-tsl19-accent text-white text-sm font-bold cursor-pointer transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tsl19-accent focus-visible:outline-offset-2">Checkout</button>
    </div>
  </aside>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl19-bg: #f8faf7;
  --color-tsl19-bg: oklch(0.975 0.004 120);
  --color-tsl19-ink: #383f3a;
  --color-tsl19-ink: oklch(0.26 0.015 145);
  --color-tsl19-mut: #767e78;
  --color-tsl19-mut: oklch(0.52 0.012 145);
  --color-tsl19-line: #e0e5e1;
  --color-tsl19-line: oklch(0.9 0.008 145);
  --color-tsl19-accent: #2f7a52;
  --color-tsl19-accent: oklch(0.45 0.12 150);
  --color-tsl19-hover: rgb(56 63 58 / 0.05);
  --color-tsl19-hover: color-mix(in oklab, oklch(0.26 0.015 145) 5%, transparent);
  --font-tsl19-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}

.tsl-19 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: light;
}
/* STATE — opacity transitions, pointer-events flips instantly, so a
   half-faded scrim is never clickable. */

#tsl19-o:checked ~ .tsl-19-scrim {
  opacity: 1;
  pointer-events: auto;
}

#tsl19-o:checked ~ .tsl-19-cart {
  translate: 0;
  box-shadow: -16px 0 48px oklch(0 0 0 / 0.18);
}

#tsl19-o:focus-visible ~ header label[for="tsl19-o"] {
  outline: 2px solid var(--color-tsl19-accent);
  outline-offset: 2px;
}
```
