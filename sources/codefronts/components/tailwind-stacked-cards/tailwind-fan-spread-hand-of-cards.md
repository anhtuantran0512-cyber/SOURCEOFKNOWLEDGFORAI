---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-fan-spread-hand-of-cards/"
title: "Tailwind Fan Spread Hand of Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A poker hand, fanned from one anchor."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Fan Spread Hand of Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-fan-spread-hand-of-cards/

A poker hand, fanned from one anchor. Each card carries its own --a and every state repeats that angle: rest is [transform:rotate(var(--a))], raised is hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)]. Because the pivot is shared and low, spacing stays even however many cards you deal &mdash; adding a sixth is one angle, not a new rule.
## HTML
```html
<section class="stk-11 w-full min-h-svh flex items-end justify-center px-5 pt-15 pb-[22vh] font-stk11-sans bg-stk11-felt [background-image:radial-gradient(circle_at_50%_120%,var(--color-stk11-glow),transparent_70%)]" aria-label="Fanned hand of cards">
  <div class="relative w-50 h-50">
    <button class="absolute left-1/2 bottom-0 -ml-15 flex h-42.5 w-30 flex-col items-start justify-between border-0 cursor-pointer rounded-[14px] bg-white px-4 py-3.5 text-3xl font-extrabold text-stk11-s1 shadow-[0_14px_30px_-14px_rgba(0,0,0,0.7)] [transform-origin:50%_130%] [transform:rotate(var(--a))] transition-[transform,box-shadow] duration-350 ease-stk11 hover:z-10 hover:shadow-[0_26px_44px_-18px_rgba(0,0,0,0.8)] hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk11-ring),0_26px_44px_-18px_rgba(0,0,0,0.8)] focus-visible:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] motion-reduce:hover:[transform:rotate(var(--a))_translateY(-40px)] motion-reduce:focus-visible:[transform:rotate(var(--a))_translateY(-40px)]" type="button" style="--a:-10deg">A<small class="self-end text-[28px]">&spades;</small></button>
    <button class="absolute left-1/2 bottom-0 -ml-15 flex h-42.5 w-30 flex-col items-start justify-between border-0 cursor-pointer rounded-[14px] bg-white px-4 py-3.5 text-3xl font-extrabold text-stk11-s2 shadow-[0_14px_30px_-14px_rgba(0,0,0,0.7)] [transform-origin:50%_130%] [transform:rotate(var(--a))] transition-[transform,box-shadow] duration-350 ease-stk11 hover:z-10 hover:shadow-[0_26px_44px_-18px_rgba(0,0,0,0.8)] hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk11-ring),0_26px_44px_-18px_rgba(0,0,0,0.8)] focus-visible:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] motion-reduce:hover:[transform:rotate(var(--a))_translateY(-40px)] motion-reduce:focus-visible:[transform:rotate(var(--a))_translateY(-40px)]" type="button" style="--a:-5deg">K<small class="self-end text-[28px]">&hearts;</small></button>
    <button class="absolute left-1/2 bottom-0 -ml-15 flex h-42.5 w-30 flex-col items-start justify-between border-0 cursor-pointer rounded-[14px] bg-white px-4 py-3.5 text-3xl font-extrabold text-stk11-s3 shadow-[0_14px_30px_-14px_rgba(0,0,0,0.7)] [transform-origin:50%_130%] [transform:rotate(var(--a))] transition-[transform,box-shadow] duration-350 ease-stk11 hover:z-10 hover:shadow-[0_26px_44px_-18px_rgba(0,0,0,0.8)] hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk11-ring),0_26px_44px_-18px_rgba(0,0,0,0.8)] focus-visible:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] motion-reduce:hover:[transform:rotate(var(--a))_translateY(-40px)] motion-reduce:focus-visible:[transform:rotate(var(--a))_translateY(-40px)]" type="button" style="--a:0deg">Q<small class="self-end text-[28px]">&diams;</small></button>
    <button class="absolute left-1/2 bottom-0 -ml-15 flex h-42.5 w-30 flex-col items-start justify-between border-0 cursor-pointer rounded-[14px] bg-white px-4 py-3.5 text-3xl font-extrabold text-stk11-s4 shadow-[0_14px_30px_-14px_rgba(0,0,0,0.7)] [transform-origin:50%_130%] [transform:rotate(var(--a))] transition-[transform,box-shadow] duration-350 ease-stk11 hover:z-10 hover:shadow-[0_26px_44px_-18px_rgba(0,0,0,0.8)] hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk11-ring),0_26px_44px_-18px_rgba(0,0,0,0.8)] focus-visible:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] motion-reduce:hover:[transform:rotate(var(--a))_translateY(-40px)] motion-reduce:focus-visible:[transform:rotate(var(--a))_translateY(-40px)]" type="button" style="--a:5deg">J<small class="self-end text-[28px]">&clubs;</small></button>
    <button class="absolute left-1/2 bottom-0 -ml-15 flex h-42.5 w-30 flex-col items-start justify-between border-0 cursor-pointer rounded-[14px] bg-white px-4 py-3.5 text-3xl font-extrabold text-stk11-s5 shadow-[0_14px_30px_-14px_rgba(0,0,0,0.7)] [transform-origin:50%_130%] [transform:rotate(var(--a))] transition-[transform,box-shadow] duration-350 ease-stk11 hover:z-10 hover:shadow-[0_26px_44px_-18px_rgba(0,0,0,0.8)] hover:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] focus-visible:z-10 focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_var(--color-stk11-ring),0_26px_44px_-18px_rgba(0,0,0,0.8)] focus-visible:[transform:rotate(var(--a))_translateY(-40px)_scale(1.05)] motion-reduce:hover:[transform:rotate(var(--a))_translateY(-40px)] motion-reduce:focus-visible:[transform:rotate(var(--a))_translateY(-40px)]" type="button" style="--a:10deg">10<small class="self-end text-[28px]">&starf;</small></button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk11-felt: #0d281c;
  --color-stk11-felt: oklch(0.26 0.055 155);
  --color-stk11-glow: #1f5136;
  --color-stk11-glow: oklch(0.38 0.075 155);
  --color-stk11-ring: #e6c65a;
  --color-stk11-ring: oklch(0.83 0.14 90);
  --color-stk11-s1: #cf5f4b;
  --color-stk11-s1: oklch(0.62 0.16 20);
  --color-stk11-s2: #c98a30;
  --color-stk11-s2: oklch(0.64 0.15 60);
  --color-stk11-s3: #45a878;
  --color-stk11-s3: oklch(0.64 0.15 150);
  --color-stk11-s4: #4a86cf;
  --color-stk11-s4: oklch(0.60 0.16 235);
  --color-stk11-s5: #9468cc;
  --color-stk11-s5: oklch(0.60 0.16 300);
  --font-stk11-sans: 'Archivo', system-ui, sans-serif;
  --ease-stk11: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
