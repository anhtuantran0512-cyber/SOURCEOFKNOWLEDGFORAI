---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-tabbed-card-stack-bring-to-front/"
title: "Tailwind Tabbed Card Stack Bring to Front"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A filing-cabinet deck where clicking a tab brings its card to the absolute front."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabbed Card Stack Bring to Front
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-tabbed-card-stack-bring-to-front/

A filing-cabinet deck where clicking a tab brings its card to the absolute front. The CSS version needs eight :nth-of-type pairings to connect radio n to tab n; the port throws all of them away by nesting each radio, tab and card together and using plain peer-checked:. Restructuring the markup is the port &mdash; and the result is shorter, flatter and far easier to extend.
## HTML
```html
<section class="stk-08 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk08-sans bg-stk08-bg" aria-label="Tabbed card deck">
  <div class="relative w-[min(400px,100%)] h-75 pt-11">
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-08" id="stk-08-1" checked>
      <label class="absolute top-0 left-[calc(var(--l)*25%)] z-5 flex h-10 w-[24%] items-center justify-center rounded-t-xl bg-stk08-c1 text-[13px] font-bold text-white cursor-pointer brightness-80 transition-[filter,transform] duration-250 hover:brightness-95 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-3 motion-reduce:transition-none" for="stk-08-1" style="--l:0">Overview</label>
      <article class="absolute inset-x-0 top-10 z-1 h-62.5 rounded-b-2xl rounded-tr-2xl bg-stk08-c1 p-7 text-white shadow-[0_26px_50px_-28px_rgba(0,0,0,0.7)] translate-y-6 scale-[0.94] transition-transform duration-450 ease-stk08 peer-checked:z-4 peer-checked:translate-y-0 peer-checked:scale-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-3 text-2xl font-extrabold tracking-[-0.02em]">Overview</h3>
        <p class="m-0 max-w-[34ch] text-[15px] leading-relaxed">One deck, four surfaces. Click a tab and its card comes to the very front.</p>
      </article>
    </div>
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-08" id="stk-08-2">
      <label class="absolute top-0 left-[calc(var(--l)*25%)] z-5 flex h-10 w-[24%] items-center justify-center rounded-t-xl bg-stk08-c2 text-[13px] font-bold text-white cursor-pointer brightness-80 transition-[filter,transform] duration-250 hover:brightness-95 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-3 motion-reduce:transition-none" for="stk-08-2" style="--l:1">Pricing</label>
      <article class="absolute inset-x-0 top-10 z-1 h-62.5 rounded-b-2xl rounded-tr-2xl bg-stk08-c2 p-7 text-white shadow-[0_26px_50px_-28px_rgba(0,0,0,0.7)] translate-y-6 scale-[0.94] transition-transform duration-450 ease-stk08 peer-checked:z-4 peer-checked:translate-y-0 peer-checked:scale-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-3 text-2xl font-extrabold tracking-[-0.02em]">Pricing</h3>
        <p class="m-0 max-w-[34ch] text-[15px] leading-relaxed">Flat monthly tiers, no seats, cancel anytime. Start free, upgrade when it pays off.</p>
      </article>
    </div>
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-08" id="stk-08-3">
      <label class="absolute top-0 left-[calc(var(--l)*25%)] z-5 flex h-10 w-[24%] items-center justify-center rounded-t-xl bg-stk08-c3 text-[13px] font-bold text-white cursor-pointer brightness-80 transition-[filter,transform] duration-250 hover:brightness-95 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-3 motion-reduce:transition-none" for="stk-08-3" style="--l:2">Docs</label>
      <article class="absolute inset-x-0 top-10 z-1 h-62.5 rounded-b-2xl rounded-tr-2xl bg-stk08-c3 p-7 text-white shadow-[0_26px_50px_-28px_rgba(0,0,0,0.7)] translate-y-6 scale-[0.94] transition-transform duration-450 ease-stk08 peer-checked:z-4 peer-checked:translate-y-0 peer-checked:scale-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-3 text-2xl font-extrabold tracking-[-0.02em]">Docs</h3>
        <p class="m-0 max-w-[34ch] text-[15px] leading-relaxed">Copy-paste snippets, live playgrounds and a searchable API. Zero setup to try.</p>
      </article>
    </div>
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-08" id="stk-08-4">
      <label class="absolute top-0 left-[calc(var(--l)*25%)] z-5 flex h-10 w-[24%] items-center justify-center rounded-t-xl bg-stk08-c4 text-[13px] font-bold text-white cursor-pointer brightness-80 transition-[filter,transform] duration-250 hover:brightness-95 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-3 motion-reduce:transition-none" for="stk-08-4" style="--l:3">Support</label>
      <article class="absolute inset-x-0 top-10 z-1 h-62.5 rounded-b-2xl rounded-tr-2xl bg-stk08-c4 p-7 text-white shadow-[0_26px_50px_-28px_rgba(0,0,0,0.7)] translate-y-6 scale-[0.94] transition-transform duration-450 ease-stk08 peer-checked:z-4 peer-checked:translate-y-0 peer-checked:scale-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-3 text-2xl font-extrabold tracking-[-0.02em]">Support</h3>
        <p class="m-0 max-w-[34ch] text-[15px] leading-relaxed">Real humans, weekday chat, and a status page that actually stays current.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk08-bg: #20222c;
  --color-stk08-bg: oklch(0.26 0.012 275);
  --color-stk08-c1: #d9694f;
  --color-stk08-c1: oklch(0.62 0.17 25);
  --color-stk08-c2: #3fa774;
  --color-stk08-c2: oklch(0.62 0.16 145);
  --color-stk08-c3: #4a8fd4;
  --color-stk08-c3: oklch(0.60 0.15 235);
  --color-stk08-c4: #9a6fd0;
  --color-stk08-c4: oklch(0.60 0.16 300);
  --font-stk08-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk08: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
