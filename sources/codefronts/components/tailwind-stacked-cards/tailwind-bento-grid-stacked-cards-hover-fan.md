---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-bento-grid-stacked-cards-hover-fan/"
title: "Tailwind Bento Grid Stacked Cards Hover Fan"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A dashboard bento where one tile hides a stacked mini-deck: three channel breakdowns collapsed into a single cell that fans open on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bento Grid Stacked Cards Hover Fan
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-bento-grid-stacked-cards-hover-fan/

A dashboard bento where one tile hides a stacked mini-deck: three channel breakdowns collapsed into a single cell that fans open on hover. This is the demo where Tailwind's grid utilities do the heavy lifting for free &mdash; col-span-2, row-span-2 and a fixed track list replace named grid areas entirely &mdash; while the fan itself is the index pattern one more time.
## HTML
```html
<section class="stk-32 grid w-full min-h-svh place-items-center p-5 font-stk32-sans bg-stk32-bg" aria-label="Analytics dashboard preview">
  <div class="grid grid-cols-[repeat(3,118px)] grid-rows-[repeat(3,118px)] gap-3">
    <div class="group relative z-5 row-span-2 overflow-visible rounded-[18px] border border-stk32-line bg-stk32-tile p-4 transition-colors duration-300 hover:z-20 hover:border-stk32-lineh">
      <span class="text-[0.68rem] tracking-[0.12em] uppercase text-stk32-lbl">Channels</span>
      <div class="absolute inset-x-4 bottom-3.5 h-13.5">
        <div class="pointer-events-none absolute inset-x-0 h-13.5 rounded-xl bg-stk32-m1 px-3 py-2 text-[0.72rem] text-white shadow-[0_8px_18px_rgba(0,0,0,0.55)] [z-index:calc(3-var(--i))] transition-transform duration-450 ease-stk32 group-hover:[transform:translateY(calc(var(--i)*-58px))] motion-reduce:transition-none" style="--i:0">
          <span class="text-[0.68rem] tracking-[0.12em] uppercase text-white/85">Organic</span>
          <b class="mt-0.5 block text-[0.95rem]">62%</b>
        </div>
        <div class="pointer-events-none absolute inset-x-0 h-13.5 rounded-xl bg-stk32-m2 px-3 py-2 text-[0.72rem] text-white shadow-[0_8px_18px_rgba(0,0,0,0.55)] [z-index:calc(3-var(--i))] transition-transform duration-450 ease-stk32 group-hover:[transform:translateY(calc(var(--i)*-58px))] motion-reduce:transition-none" style="--i:1">
          <span class="text-[0.68rem] tracking-[0.12em] uppercase text-white/85">Paid</span>
          <b class="mt-0.5 block text-[0.95rem]">24%</b>
        </div>
        <div class="pointer-events-none absolute inset-x-0 h-13.5 rounded-xl bg-stk32-m3 px-3 py-2 text-[0.72rem] text-white shadow-[0_8px_18px_rgba(0,0,0,0.55)] [z-index:calc(3-var(--i))] transition-transform duration-450 ease-stk32 group-hover:[transform:translateY(calc(var(--i)*-58px))] motion-reduce:transition-none" style="--i:2">
          <span class="text-[0.68rem] tracking-[0.12em] uppercase text-white/85">Referral</span>
          <b class="mt-0.5 block text-[0.95rem]">14%</b>
        </div>
      </div>
    </div>
    <div class="relative col-span-2 overflow-hidden rounded-[18px] border border-stk32-line bg-stk32-tile p-4 transition-colors duration-300 hover:border-stk32-lineh">
      <div class="pointer-events-none absolute -right-8 -top-8 size-24 rounded-full bg-stk32-good opacity-20 blur-2xl" aria-hidden="true"></div>
      <span class="text-[0.68rem] tracking-[0.12em] uppercase text-stk32-lbl">Revenue</span>
      <div class="mt-1 text-[1.6rem] font-bold text-stk32-val">$48.2k <small class="text-[0.8rem] font-semibold text-stk32-good">+12%</small></div>
      <div class="mt-2 flex h-8 items-end gap-1.5" aria-hidden="true">
        <span class="w-2 rounded-t bg-stk32-bar" style="height:40%"></span>
        <span class="w-2 rounded-t bg-stk32-bar" style="height:55%"></span>
        <span class="w-2 rounded-t bg-stk32-bar" style="height:45%"></span>
        <span class="w-2 rounded-t bg-stk32-bar" style="height:70%"></span>
        <span class="w-2 rounded-t bg-stk32-bar" style="height:60%"></span>
        <span class="w-2 rounded-t bg-stk32-bar" style="height:85%"></span>
        <span class="w-2 rounded-t bg-stk32-good" style="height:100%"></span>
      </div>
    </div>
    <div class="relative overflow-hidden rounded-[18px] border border-stk32-line bg-stk32-tile p-4 transition-colors duration-300 hover:border-stk32-lineh">
      <span class="text-[0.68rem] tracking-[0.12em] uppercase text-stk32-lbl">Users</span>
      <div class="mt-1 text-[1.6rem] font-bold text-stk32-val">9.1k</div>
    </div>
    <div class="relative overflow-hidden rounded-[18px] border border-stk32-line bg-stk32-tile p-4 transition-colors duration-300 hover:border-stk32-lineh">
      <span class="text-[0.68rem] tracking-[0.12em] uppercase text-stk32-lbl">Churn</span>
      <div class="mt-1 text-[1.6rem] font-bold text-stk32-bad">1.8%</div>
    </div>
    <div class="relative overflow-hidden rounded-[18px] border border-stk32-line bg-stk32-tile p-4 transition-colors duration-300 hover:border-stk32-lineh">
      <div class="pointer-events-none absolute -left-8 -bottom-8 size-24 rounded-full bg-stk32-m1 opacity-25 blur-2xl" aria-hidden="true"></div>
      <span class="text-[0.68rem] tracking-[0.12em] uppercase text-stk32-lbl">NPS</span>
      <div class="mt-1 text-[1.6rem] font-bold text-stk32-val">72</div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk32-bg: #0e0f13;
  --color-stk32-bg: oklch(0.17 0.008 275);
  --color-stk32-tile: #191b22;
  --color-stk32-tile: oklch(0.23 0.012 275);
  --color-stk32-line: #262934;
  --color-stk32-line: oklch(0.30 0.014 275);
  --color-stk32-lineh: #3a4050;
  --color-stk32-lineh: oklch(0.40 0.018 275);
  --color-stk32-lbl: #8a90a0;
  --color-stk32-lbl: oklch(0.64 0.016 275);
  --color-stk32-val: #f3f4f6;
  --color-stk32-val: oklch(0.97 0.003 275);
  --color-stk32-bar: #4b5162;
  --color-stk32-bar: oklch(0.46 0.020 275);
  --color-stk32-good: #34d399;
  --color-stk32-good: oklch(0.78 0.15 165);
  --color-stk32-bad: #fca5a5;
  --color-stk32-bad: oklch(0.79 0.10 20);
  --color-stk32-m1: #818cf8;
  --color-stk32-m1: oklch(0.68 0.15 280);
  --color-stk32-m2: #f472b6;
  --color-stk32-m2: oklch(0.72 0.17 350);
  --color-stk32-m3: #2dd4bf;
  --color-stk32-m3: oklch(0.79 0.13 180);
  --font-stk32-sans: 'Geist', system-ui, sans-serif;
  --ease-stk32: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
