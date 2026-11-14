---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-expand-accordion-on-click/"
title: "Tailwind Stacked Cards Expand Accordion on Click"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A pile resting on its bottom edges that opens by animating grid rows, no JS."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Cards Expand Accordion on Click
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-expand-accordion-on-click/

A pile resting on its bottom edges that opens by animating grid rows, no JS. The 0fr &rarr; 1fr reveal is grid-rows-[0fr] with peer-checked:grid-rows-[1fr] &mdash; a real utility pair, not an arbitrary property. The open card lifts clear via has-checked:, which is exactly the :has() rule the CSS version needs, only typed on the panel it applies to.
## HTML
```html
<section class="stk-04 w-full min-h-svh flex items-center justify-center px-5 py-12 font-stk04-sans bg-stk04-bg" aria-label="Stacked expansion accordion">
  <div class="w-[min(440px,100%)]">
    <div class="relative -mt-3 first:mt-0 rounded-2xl border border-stk04-line bg-stk04-card shadow-[0_14px_30px_-22px_rgba(0,0,0,0.8)] transition-[margin,box-shadow,border-color] duration-350 has-checked:mt-3.5 first:has-checked:mt-0 has-checked:z-2 has-checked:border-stk04-accent has-checked:shadow-[0_22px_46px_-26px_var(--color-stk04-accent)] motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-04" id="stk-04-1" checked>
      <label class="flex items-center gap-3 px-5 py-4.5 cursor-pointer rounded-2xl text-[15px] font-bold text-stk04-dim peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-stk04-accent peer-focus-visible:-outline-offset-3" for="stk-04-1">
        <span class="size-2 shrink-0 rounded-full bg-stk04-line transition-colors duration-300 peer-checked:bg-stk04-accent"></span>
        Dimensions &amp; weight
        <span class="ml-auto font-stk04-mono text-2xl leading-none text-stk04-muted transition-[transform,color] duration-300 peer-checked:rotate-90 peer-checked:text-stk04-accent motion-reduce:transition-none" aria-hidden="true">&rsaquo;</span>
      </label>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-stk04 peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-sm leading-relaxed text-stk04-muted">142 &times; 68 &times; 7.4 mm &middot; 168 g. Aerospace-grade aluminium frame with a matte bead-blast finish.</p></div>
      </div>
    </div>
    <div class="relative -mt-3 rounded-2xl border border-stk04-line bg-stk04-card shadow-[0_14px_30px_-22px_rgba(0,0,0,0.8)] transition-[margin,box-shadow,border-color] duration-350 has-checked:mt-3.5 has-checked:z-2 has-checked:border-stk04-accent has-checked:shadow-[0_22px_46px_-26px_var(--color-stk04-accent)] motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-04" id="stk-04-2">
      <label class="flex items-center gap-3 px-5 py-4.5 cursor-pointer rounded-2xl text-[15px] font-bold text-stk04-dim peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-stk04-accent peer-focus-visible:-outline-offset-3" for="stk-04-2">
        <span class="size-2 shrink-0 rounded-full bg-stk04-line transition-colors duration-300 peer-checked:bg-stk04-accent"></span>
        Display
        <span class="ml-auto font-stk04-mono text-2xl leading-none text-stk04-muted transition-[transform,color] duration-300 peer-checked:rotate-90 peer-checked:text-stk04-accent motion-reduce:transition-none" aria-hidden="true">&rsaquo;</span>
      </label>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-stk04 peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-sm leading-relaxed text-stk04-muted">6.3&Prime; LTPO OLED, 1&ndash;120 Hz adaptive, 2600 nits peak, Dolby Vision, hardened glass.</p></div>
      </div>
    </div>
    <div class="relative -mt-3 rounded-2xl border border-stk04-line bg-stk04-card shadow-[0_14px_30px_-22px_rgba(0,0,0,0.8)] transition-[margin,box-shadow,border-color] duration-350 has-checked:mt-3.5 has-checked:z-2 has-checked:border-stk04-accent has-checked:shadow-[0_22px_46px_-26px_var(--color-stk04-accent)] motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-04" id="stk-04-3">
      <label class="flex items-center gap-3 px-5 py-4.5 cursor-pointer rounded-2xl text-[15px] font-bold text-stk04-dim peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-stk04-accent peer-focus-visible:-outline-offset-3" for="stk-04-3">
        <span class="size-2 shrink-0 rounded-full bg-stk04-line transition-colors duration-300 peer-checked:bg-stk04-accent"></span>
        Battery &amp; charging
        <span class="ml-auto font-stk04-mono text-2xl leading-none text-stk04-muted transition-[transform,color] duration-300 peer-checked:rotate-90 peer-checked:text-stk04-accent motion-reduce:transition-none" aria-hidden="true">&rsaquo;</span>
      </label>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-stk04 peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-sm leading-relaxed text-stk04-muted">4,800 mAh &middot; 80 W wired to 50% in 12 min &middot; 30 W wireless &middot; USB-C 3.2.</p></div>
      </div>
    </div>
    <div class="relative -mt-3 rounded-2xl border border-stk04-line bg-stk04-card shadow-[0_14px_30px_-22px_rgba(0,0,0,0.8)] transition-[margin,box-shadow,border-color] duration-350 has-checked:mt-3.5 has-checked:z-2 has-checked:border-stk04-accent has-checked:shadow-[0_22px_46px_-26px_var(--color-stk04-accent)] motion-reduce:transition-none">
      <input class="peer sr-only" type="radio" name="stk-04" id="stk-04-4">
      <label class="flex items-center gap-3 px-5 py-4.5 cursor-pointer rounded-2xl text-[15px] font-bold text-stk04-dim peer-checked:text-white peer-focus-visible:outline-3 peer-focus-visible:outline-stk04-accent peer-focus-visible:-outline-offset-3" for="stk-04-4">
        <span class="size-2 shrink-0 rounded-full bg-stk04-line transition-colors duration-300 peer-checked:bg-stk04-accent"></span>
        In the box
        <span class="ml-auto font-stk04-mono text-2xl leading-none text-stk04-muted transition-[transform,color] duration-300 peer-checked:rotate-90 peer-checked:text-stk04-accent motion-reduce:transition-none" aria-hidden="true">&rsaquo;</span>
      </label>
      <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-stk04 peer-checked:grid-rows-[1fr] motion-reduce:transition-none">
        <div class="overflow-hidden"><p class="px-5 pb-5 text-sm leading-relaxed text-stk04-muted">Device, braided USB-C cable, SIM tool, quick-start guide. Adapter sold separately.</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk04-bg: #111319;
  --color-stk04-bg: oklch(0.20 0.012 265);
  --color-stk04-card: #1c1f28;
  --color-stk04-card: oklch(0.25 0.014 265);
  --color-stk04-line: #2a2e3a;
  --color-stk04-line: oklch(0.32 0.016 265);
  --color-stk04-dim: #eef0f6;
  --color-stk04-dim: oklch(0.94 0.006 265);
  --color-stk04-muted: #aab0c0;
  --color-stk04-muted: oklch(0.75 0.018 265);
  --color-stk04-accent: #6a7bf0;
  --color-stk04-accent: oklch(0.60 0.16 265);
  --font-stk04-sans: 'Archivo', system-ui, sans-serif;
  --font-stk04-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk04: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
