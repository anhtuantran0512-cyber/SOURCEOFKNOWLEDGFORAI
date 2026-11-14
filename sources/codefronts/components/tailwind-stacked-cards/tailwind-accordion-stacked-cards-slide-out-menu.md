---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-accordion-stacked-cards-slide-out-menu/"
title: "Tailwind Accordion Stacked Cards Slide Out Menu"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "One checkbox unfurls a packed pile into a spaced menu."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion Stacked Cards Slide Out Menu
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-accordion-stacked-cards-slide-out-menu/

One checkbox unfurls a packed pile into a spaced menu. The reveal is the grid-rows-[0fr] &rarr; 1fr pattern again, but the interesting part is reaching the items: peer-* stops at siblings, so the links are addressed with peer-checked:[&_a]:opacity-100 &mdash; the child-selector bolt-on that is the single most common Tailwind port bug.
## HTML
```html
<section class="stk-16 w-full min-h-svh flex items-start justify-center px-5 py-[12vh] font-stk16-sans bg-stk16-bg" aria-label="Accordion-spread menu">
  <div class="w-[min(300px,100%)]">
    <input class="peer sr-only" type="checkbox" id="stk-16-t">
    <label class="relative z-10 flex items-center justify-between rounded-[14px] bg-stk16-accent px-5 py-4 text-base font-extrabold text-white cursor-pointer shadow-[0_14px_30px_-16px_rgba(0,0,0,0.7)] peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-3 peer-checked:[&_i]:rotate-180" for="stk-16-t">
      <span>Menu</span>
      <i class="text-xl not-italic leading-none transition-transform duration-350 motion-reduce:transition-none" aria-hidden="true">&#8964;</i>
    </label>
    <div class="grid grid-rows-[0fr] transition-[grid-template-rows] duration-400 ease-stk16 peer-checked:grid-rows-[1fr] peer-checked:[&_a]:opacity-100 peer-checked:[&_a]:translate-y-0 motion-reduce:transition-none">
      <nav class="flex flex-col gap-2 overflow-hidden pt-2" aria-label="Main">
        <a class="rounded-xl bg-stk16-item px-5 py-3.75 text-[15px] font-semibold text-stk16-ink no-underline opacity-0 -translate-y-2 shadow-[0_10px_22px_-14px_rgba(0,0,0,0.8)] transition-[opacity,transform] duration-300 delay-[calc(var(--n)*40ms)] hover:bg-stk16-itemh hover:text-white focus-visible:opacity-100 focus-visible:outline-3 focus-visible:outline-stk16-accent focus-visible:outline-offset-2 motion-reduce:delay-0!" href="#" style="--n:0">Dashboard</a>
        <a class="rounded-xl bg-stk16-item px-5 py-3.75 text-[15px] font-semibold text-stk16-ink no-underline opacity-0 -translate-y-2 shadow-[0_10px_22px_-14px_rgba(0,0,0,0.8)] transition-[opacity,transform] duration-300 delay-[calc(var(--n)*40ms)] hover:bg-stk16-itemh hover:text-white focus-visible:opacity-100 focus-visible:outline-3 focus-visible:outline-stk16-accent focus-visible:outline-offset-2 motion-reduce:delay-0!" href="#" style="--n:1">Projects</a>
        <a class="rounded-xl bg-stk16-item px-5 py-3.75 text-[15px] font-semibold text-stk16-ink no-underline opacity-0 -translate-y-2 shadow-[0_10px_22px_-14px_rgba(0,0,0,0.8)] transition-[opacity,transform] duration-300 delay-[calc(var(--n)*40ms)] hover:bg-stk16-itemh hover:text-white focus-visible:opacity-100 focus-visible:outline-3 focus-visible:outline-stk16-accent focus-visible:outline-offset-2 motion-reduce:delay-0!" href="#" style="--n:2">Team</a>
        <a class="rounded-xl bg-stk16-item px-5 py-3.75 text-[15px] font-semibold text-stk16-ink no-underline opacity-0 -translate-y-2 shadow-[0_10px_22px_-14px_rgba(0,0,0,0.8)] transition-[opacity,transform] duration-300 delay-[calc(var(--n)*40ms)] hover:bg-stk16-itemh hover:text-white focus-visible:opacity-100 focus-visible:outline-3 focus-visible:outline-stk16-accent focus-visible:outline-offset-2 motion-reduce:delay-0!" href="#" style="--n:3">Billing</a>
        <a class="rounded-xl bg-stk16-item px-5 py-3.75 text-[15px] font-semibold text-stk16-ink no-underline opacity-0 -translate-y-2 shadow-[0_10px_22px_-14px_rgba(0,0,0,0.8)] transition-[opacity,transform] duration-300 delay-[calc(var(--n)*40ms)] hover:bg-stk16-itemh hover:text-white focus-visible:opacity-100 focus-visible:outline-3 focus-visible:outline-stk16-accent focus-visible:outline-offset-2 motion-reduce:delay-0!" href="#" style="--n:4">Settings</a>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk16-bg: #101018;
  --color-stk16-bg: oklch(0.18 0.012 285);
  --color-stk16-item: #1c1e2a;
  --color-stk16-item: oklch(0.25 0.016 285);
  --color-stk16-itemh: #262a3a;
  --color-stk16-itemh: oklch(0.31 0.018 285);
  --color-stk16-ink: #c9cde0;
  --color-stk16-ink: oklch(0.85 0.018 285);
  --color-stk16-accent: #7b5fe0;
  --color-stk16-accent: oklch(0.64 0.17 285);
  --font-stk16-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk16: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
