---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-cards-spread-out-horizontally-on-hover/"
title: "Tailwind Cards Spread Out Horizontally on Hover"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A packed avatar row that springs open the moment you point at it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cards Spread Out Horizontally on Hover
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-cards-spread-out-horizontally-on-hover/

A packed avatar row that springs open the moment you point at it. The overlap is -ml-7 released to group-hover:ml-3.5, the overshoot is a named --ease-* token, and the ripple is a per-card delay-[calc(var(--i)*30ms)] &mdash; so the whole open-and-close lives in one class list rather than four rules and a delay map.
## HTML
```html
<section class="stk-14 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk14-sans bg-stk14-bg" aria-label="Hover-spread avatar pile">
  <div class="group flex rounded-full p-5" aria-label="Project team">
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-a1 text-[17px] font-extrabold text-white cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:0" aria-label="Alex Rivera">AR</button>
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-a2 text-[17px] font-extrabold text-white cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:1" aria-label="Jon Lau">JL</button>
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-a3 text-[17px] font-extrabold text-white cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:2" aria-label="Maya Kirsh">MK</button>
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-a4 text-[17px] font-extrabold text-white cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:3" aria-label="Sasha Vidal">SV</button>
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-a5 text-[17px] font-extrabold text-white cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:4" aria-label="Tomas Nagy">TN</button>
    <button class="size-16 shrink-0 rounded-full border-[3px] border-stk14-bg bg-stk14-more text-[17px] font-extrabold text-stk14-moreink cursor-pointer -ml-7 first:ml-0 shadow-[0_8px_18px_-8px_rgba(0,0,0,0.7)] transition-[margin,transform] duration-450 ease-stk14 delay-[calc(var(--i)*30ms)] group-hover:ml-3.5 group-hover:first:ml-0 group-focus-within:ml-3.5 group-focus-within:first:ml-0 hover:z-5 hover:-translate-y-2 hover:scale-105 focus-visible:z-5 focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-2 motion-reduce:ease-linear motion-reduce:duration-250" type="button" style="--i:5" aria-label="Show six more team members">+6</button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk14-bg: #0f1118;
  --color-stk14-bg: oklch(0.18 0.012 275);
  --color-stk14-a1: #e8836a;
  --color-stk14-a1: oklch(0.68 0.16 20);
  --color-stk14-a2: #c9a33f;
  --color-stk14-a2: oklch(0.70 0.15 90);
  --color-stk14-a3: #48b98a;
  --color-stk14-a3: oklch(0.68 0.15 155);
  --color-stk14-a4: #5296d8;
  --color-stk14-a4: oklch(0.65 0.15 235);
  --color-stk14-a5: #a077d8;
  --color-stk14-a5: oklch(0.63 0.16 300);
  --color-stk14-more: #2a2f40;
  --color-stk14-more: oklch(0.31 0.02 275);
  --color-stk14-moreink: #c3c7de;
  --color-stk14-moreink: oklch(0.83 0.02 275);
  --font-stk14-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk14: cubic-bezier(0.34, 1.56, 0.5, 1);
}
```
