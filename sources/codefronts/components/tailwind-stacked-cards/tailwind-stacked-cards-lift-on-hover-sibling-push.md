---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-lift-on-hover-sibling-push/"
title: "Tailwind Stacked Cards Lift on Hover Sibling Push"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "The parting-of-the-waters stack: hover a card and every card below it slides down."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stacked Cards Lift on Hover Sibling Push
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-stacked-cards-lift-on-hover-sibling-push/

The parting-of-the-waters stack: hover a card and every card below it slides down. This is the demo where Tailwind runs out of variants &mdash; there is no hover ~ sibling family &mdash; so the whole effect rides one arbitrary variant, [&:hover~*]:translate-y-[30px], typed on each card. Worth knowing precisely because it is the exception rather than the rule.
## HTML
```html
<section class="stk-15 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk15-sans bg-stk15-bg" aria-label="Cascade-lift card stack">
  <div class="w-[min(320px,100%)]">
    <a class="flex flex-col gap-1.25 -mt-4 first:mt-0 rounded-2xl bg-stk15-c1 px-6 py-5 text-white no-underline shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] transition-[transform,box-shadow] duration-350 ease-stk15 hover:z-5 hover:-translate-y-[18px] hover:scale-[1.03] hover:shadow-[0_26px_44px_-20px_rgba(0,0,0,0.9)] focus-visible:z-5 focus-visible:outline-none focus-visible:-translate-y-[18px] focus-visible:scale-[1.03] focus-visible:shadow-[0_0_0_3px_#fff,0_26px_44px_-20px_rgba(0,0,0,0.9)] [&:hover~*]:translate-y-[30px] [&:focus-visible~*]:translate-y-[30px] motion-reduce:transition-[box-shadow]" href="#">
      <b class="text-lg font-extrabold tracking-[-0.02em]">Espresso</b>
      <span class="font-stk15-mono text-[13px] opacity-90">Single origin &middot; 30&thinsp;ml</span>
    </a>
    <a class="flex flex-col gap-1.25 -mt-4 rounded-2xl bg-stk15-c2 px-6 py-5 text-white no-underline shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] transition-[transform,box-shadow] duration-350 ease-stk15 hover:z-5 hover:-translate-y-[18px] hover:scale-[1.03] hover:shadow-[0_26px_44px_-20px_rgba(0,0,0,0.9)] focus-visible:z-5 focus-visible:outline-none focus-visible:-translate-y-[18px] focus-visible:scale-[1.03] focus-visible:shadow-[0_0_0_3px_#fff,0_26px_44px_-20px_rgba(0,0,0,0.9)] [&:hover~*]:translate-y-[30px] [&:focus-visible~*]:translate-y-[30px] motion-reduce:transition-[box-shadow]" href="#">
      <b class="text-lg font-extrabold tracking-[-0.02em]">Cortado</b>
      <span class="font-stk15-mono text-[13px] opacity-90">Equal parts &middot; 90&thinsp;ml</span>
    </a>
    <a class="flex flex-col gap-1.25 -mt-4 rounded-2xl bg-stk15-c3 px-6 py-5 text-white no-underline shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] transition-[transform,box-shadow] duration-350 ease-stk15 hover:z-5 hover:-translate-y-[18px] hover:scale-[1.03] hover:shadow-[0_26px_44px_-20px_rgba(0,0,0,0.9)] focus-visible:z-5 focus-visible:outline-none focus-visible:-translate-y-[18px] focus-visible:scale-[1.03] focus-visible:shadow-[0_0_0_3px_#fff,0_26px_44px_-20px_rgba(0,0,0,0.9)] [&:hover~*]:translate-y-[30px] [&:focus-visible~*]:translate-y-[30px] motion-reduce:transition-[box-shadow]" href="#">
      <b class="text-lg font-extrabold tracking-[-0.02em]">Flat white</b>
      <span class="font-stk15-mono text-[13px] opacity-90">Micro-foam &middot; 160&thinsp;ml</span>
    </a>
    <a class="flex flex-col gap-1.25 -mt-4 rounded-2xl bg-stk15-c4 px-6 py-5 text-white no-underline shadow-[0_14px_30px_-18px_rgba(0,0,0,0.8)] transition-[transform,box-shadow] duration-350 ease-stk15 hover:z-5 hover:-translate-y-[18px] hover:scale-[1.03] hover:shadow-[0_26px_44px_-20px_rgba(0,0,0,0.9)] focus-visible:z-5 focus-visible:outline-none focus-visible:-translate-y-[18px] focus-visible:scale-[1.03] focus-visible:shadow-[0_0_0_3px_#fff,0_26px_44px_-20px_rgba(0,0,0,0.9)] [&:hover~*]:translate-y-[30px] [&:focus-visible~*]:translate-y-[30px] motion-reduce:transition-[box-shadow]" href="#">
      <b class="text-lg font-extrabold tracking-[-0.02em]">Cold brew</b>
      <span class="font-stk15-mono text-[13px] opacity-90">18&thinsp;h steep &middot; 240&thinsp;ml</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk15-bg: #161310;
  --color-stk15-bg: oklch(0.20 0.012 60);
  --color-stk15-c1: #cf5f4b;
  --color-stk15-c1: oklch(0.62 0.16 20);
  --color-stk15-c2: #bd7440;
  --color-stk15-c2: oklch(0.60 0.14 50);
  --color-stk15-c3: #a38434;
  --color-stk15-c3: oklch(0.58 0.12 80);
  --color-stk15-c4: #859030;
  --color-stk15-c4: oklch(0.58 0.10 110);
  --font-stk15-sans: 'Archivo', system-ui, sans-serif;
  --font-stk15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-stk15: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
