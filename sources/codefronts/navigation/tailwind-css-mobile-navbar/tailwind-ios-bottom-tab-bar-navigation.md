---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-ios-bottom-tab-bar-navigation/"
title: "Tailwind CSS iOS Bottom Tab Bar Navigation"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "An iOS-style bottom tab bar with four real pages, a frosted backdrop-blur-xl bar, filled-on-active SVG icons and a working notification badge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS iOS Bottom Tab Bar Navigation
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-ios-bottom-tab-bar-navigation/

An iOS-style bottom tab bar with four real pages, a frosted backdrop-blur-xl bar, filled-on-active SVG icons and a working notification badge. Radios hold the state; every page and tab reads it through group-has-[#id:checked]:. Zero JavaScript.
## HTML
```html
<section class="tmn-03 w-full min-h-svh grid place-items-center bg-tmn03-stage px-4 py-6 font-tmn03-sans antialiased" aria-label="Tailwind iOS bottom tab bar demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn03-bg text-tmn03-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.7)]">
    <input type="radio" name="tmn-03-tab" id="tmn-03-home" class="sr-only" checked>
    <input type="radio" name="tmn-03-tab" id="tmn-03-search" class="sr-only">
    <input type="radio" name="tmn-03-tab" id="tmn-03-alerts" class="sr-only">
    <input type="radio" name="tmn-03-tab" id="tmn-03-profile" class="sr-only">

    <div class="flex h-11 items-center justify-between px-7 text-[15px] font-semibold">
      <span>9:41</span>
      <span aria-hidden="true" class="flex items-center gap-1.5">
        <span class="flex items-end gap-px"><span class="h-1 w-[3px] rounded-[1px] bg-current"></span><span class="h-1.5 w-[3px] rounded-[1px] bg-current"></span><span class="h-2 w-[3px] rounded-[1px] bg-current"></span><span class="h-2.5 w-[3px] rounded-[1px] bg-current"></span></span>
        <span class="relative h-3 w-6 rounded-[4px] border border-current/40 p-px after:absolute after:top-1/2 after:-right-[3px] after:h-1 after:w-[1.5px] after:-translate-y-1/2 after:rounded-r after:bg-current/40 after:content-['']"><span class="block h-full w-4/5 rounded-[2px] bg-current"></span></span>
      </span>
    </div>

    <div class="absolute inset-x-0 top-11 bottom-[83px]">
      <div class="invisible absolute inset-0 scale-[.98] overflow-y-auto px-4 pt-3 opacity-0 transition duration-300 group-has-[#tmn-03-home:checked]:visible group-has-[#tmn-03-home:checked]:scale-100 group-has-[#tmn-03-home:checked]:opacity-100">
        <h2 class="mb-1 text-[32px] font-bold tracking-[-0.02em]">Home</h2>
        <p class="mb-5 text-sm text-tmn03-mut">Total balance <strong class="text-tmn03-ink">$24,860.12</strong></p>
        <div class="divide-y divide-black/6 overflow-hidden rounded-2xl bg-white">
          <a href="#" class="flex min-h-15 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-emerald-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="m3 17 6-6 4 4 8-8M15 7h6v6"/></svg></span><span class="flex-1"><span class="block text-[15px] font-medium">Portfolio value</span><span class="block text-[13px] text-emerald-700">+2.4% today</span></span><svg viewBox="0 0 24 24" class="size-4 text-tmn03-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
          <a href="#" class="flex min-h-15 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-tmn03-acc text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg></span><span class="flex-1"><span class="block text-[15px] font-medium">Spending</span><span class="block text-[13px] text-tmn03-mut">$342 this week</span></span><svg viewBox="0 0 24 24" class="size-4 text-tmn03-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
          <a href="#" class="flex min-h-15 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-pink-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg></span><span class="flex-1"><span class="block text-[15px] font-medium">Savings goal</span><span class="mt-1.5 block h-1 overflow-hidden rounded-full bg-black/8"><span class="block h-full w-[68%] rounded-full bg-pink-500"></span></span></span><span class="text-[13px] text-tmn03-mut">68%</span></a>
        </div>
      </div>

      <div class="invisible absolute inset-0 scale-[.98] overflow-y-auto px-4 pt-3 opacity-0 transition duration-300 group-has-[#tmn-03-search:checked]:visible group-has-[#tmn-03-search:checked]:scale-100 group-has-[#tmn-03-search:checked]:opacity-100">
        <h2 class="mb-4 text-[32px] font-bold tracking-[-0.02em]">Search</h2>
        <label class="mb-5 flex h-10 items-center gap-2 rounded-xl bg-black/6 px-3 text-tmn03-mut"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Transactions, people…" class="w-full bg-transparent text-[15px] text-tmn03-ink placeholder:text-tmn03-mut focus:outline-none"></label>
        <p class="mb-2 px-1 text-[13px] font-semibold text-tmn03-mut uppercase">Recent</p>
        <div class="divide-y divide-black/6 overflow-hidden rounded-2xl bg-white">
          <div class="flex min-h-15 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-orange-500 text-sm font-bold text-white">G</span><span class="flex-1"><span class="block text-[15px] font-medium">Groceries</span><span class="block text-[13px] text-tmn03-mut">Yesterday</span></span><span class="text-[15px] tabular-nums">−$48.20</span></div>
          <div class="flex min-h-15 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-emerald-500 text-sm font-bold text-white">T</span><span class="flex-1"><span class="block text-[15px] font-medium">Transfer received</span><span class="block text-[13px] text-tmn03-mut">2 days ago</span></span><span class="text-[15px] text-emerald-700 tabular-nums">+$200.00</span></div>
        </div>
      </div>

      <div class="invisible absolute inset-0 scale-[.98] overflow-y-auto px-4 pt-3 opacity-0 transition duration-300 group-has-[#tmn-03-alerts:checked]:visible group-has-[#tmn-03-alerts:checked]:scale-100 group-has-[#tmn-03-alerts:checked]:opacity-100">
        <h2 class="mb-4 text-[32px] font-bold tracking-[-0.02em]">Alerts</h2>
        <div class="divide-y divide-black/6 overflow-hidden rounded-2xl bg-white">
          <div class="flex items-start gap-3.5 p-4"><span class="grid size-8 flex-none place-items-center rounded-lg bg-amber-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg></span><span><span class="block text-[15px] font-medium">Unusual spend detected</span><span class="block text-[13px] text-tmn03-mut">$340 at Electronics Hub · 2m</span></span></div>
          <div class="flex items-start gap-3.5 p-4"><span class="grid size-8 flex-none place-items-center rounded-lg bg-emerald-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg></span><span><span class="block text-[15px] font-medium">Payment cleared</span><span class="block text-[13px] text-tmn03-mut">Rent payment confirmed · 1h</span></span></div>
        </div>
      </div>

      <div class="invisible absolute inset-0 scale-[.98] overflow-y-auto px-4 pt-3 opacity-0 transition duration-300 group-has-[#tmn-03-profile:checked]:visible group-has-[#tmn-03-profile:checked]:scale-100 group-has-[#tmn-03-profile:checked]:opacity-100">
        <div class="mb-3 flex flex-col items-center rounded-2xl bg-white px-4 py-6">
          <span class="mb-3 grid size-18 place-items-center rounded-full bg-linear-135 from-tmn03-acc to-violet-500 text-2xl font-bold text-white">JB</span>
          <p class="text-lg font-semibold">Jordan Blake</p>
          <p class="text-[13px] text-tmn03-mut">Premium member</p>
        </div>
        <div class="divide-y divide-black/6 overflow-hidden rounded-2xl bg-white">
          <a href="#" class="flex min-h-13 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-violet-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></span><span class="flex-1 text-[15px] font-medium">Security</span><svg viewBox="0 0 24 24" class="size-4 text-tmn03-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
          <a href="#" class="flex min-h-13 items-center gap-3.5 px-4"><span class="grid size-8 place-items-center rounded-lg bg-red-500 text-white"><svg viewBox="0 0 24 24" class="size-4.5" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></span><span class="flex-1 text-[15px] font-medium">Notifications</span><svg viewBox="0 0 24 24" class="size-4 text-tmn03-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
        </div>
      </div>
    </div>

    <nav aria-label="Tabs" class="absolute inset-x-0 bottom-0 z-10 flex h-[83px] items-start border-t border-black/10 bg-white/80 px-2 pt-1.5 pb-[max(env(safe-area-inset-bottom),8px)] backdrop-blur-xl backdrop-saturate-150">
      <label for="tmn-03-home" class="flex flex-1 cursor-pointer flex-col items-center gap-0.5 rounded-xl py-1 text-tmn03-mut transition-colors group-has-[#tmn-03-home:checked]:text-tmn03-acc group-has-[#tmn-03-home:focus-visible]:ring-2 group-has-[#tmn-03-home:focus-visible]:ring-tmn03-acc">
        <svg viewBox="0 0 24 24" class="size-7 transition-transform duration-200 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-03-home:checked]:scale-105 group-has-[#tmn-03-home:checked]:fill-tmn03-acc/15" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg>
        <span class="text-[10px] font-semibold">Home</span>
      </label>
      <label for="tmn-03-search" class="flex flex-1 cursor-pointer flex-col items-center gap-0.5 rounded-xl py-1 text-tmn03-mut transition-colors group-has-[#tmn-03-search:checked]:text-tmn03-acc group-has-[#tmn-03-search:focus-visible]:ring-2 group-has-[#tmn-03-search:focus-visible]:ring-tmn03-acc">
        <svg viewBox="0 0 24 24" class="size-7 transition-transform duration-200 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-03-search:checked]:scale-105 group-has-[#tmn-03-search:checked]:fill-tmn03-acc/15" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <span class="text-[10px] font-semibold">Search</span>
      </label>
      <label for="tmn-03-alerts" class="flex flex-1 cursor-pointer flex-col items-center gap-0.5 rounded-xl py-1 text-tmn03-mut transition-colors group-has-[#tmn-03-alerts:checked]:text-tmn03-acc group-has-[#tmn-03-alerts:focus-visible]:ring-2 group-has-[#tmn-03-alerts:focus-visible]:ring-tmn03-acc">
        <span class="relative">
          <svg viewBox="0 0 24 24" class="size-7 transition-transform duration-200 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-03-alerts:checked]:scale-105 group-has-[#tmn-03-alerts:checked]:fill-tmn03-acc/15" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>
          <span class="absolute -top-1 -right-2 grid h-4.5 min-w-4.5 place-items-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white ring-2 ring-white">2<span class="sr-only"> unread</span></span>
        </span>
        <span class="text-[10px] font-semibold">Alerts</span>
      </label>
      <label for="tmn-03-profile" class="flex flex-1 cursor-pointer flex-col items-center gap-0.5 rounded-xl py-1 text-tmn03-mut transition-colors group-has-[#tmn-03-profile:checked]:text-tmn03-acc group-has-[#tmn-03-profile:focus-visible]:ring-2 group-has-[#tmn-03-profile:focus-visible]:ring-tmn03-acc">
        <svg viewBox="0 0 24 24" class="size-7 transition-transform duration-200 ease-[cubic-bezier(.34,1.56,.64,1)] group-has-[#tmn-03-profile:checked]:scale-105 group-has-[#tmn-03-profile:checked]:fill-tmn03-acc/15" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>
        <span class="text-[10px] font-semibold">Profile</span>
      </label>
      <span aria-hidden="true" class="absolute bottom-2 left-1/2 h-[5px] w-[134px] -translate-x-1/2 rounded-full bg-tmn03-ink"></span>
    </nav>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn03-stage: #dfe3ea;
  --color-tmn03-stage: oklch(0.91 0.01 260);
  --color-tmn03-bg: #f2f2f7;
  --color-tmn03-bg: oklch(0.96 0.005 285);
  --color-tmn03-ink: #1c1c1e;
  --color-tmn03-ink: oklch(0.22 0.003 285);
  --color-tmn03-mut: #6e6e73;
  --color-tmn03-mut: oklch(0.53 0.006 285);
  --color-tmn03-acc: #007aff;
  --color-tmn03-acc: oklch(0.6 0.22 257);
  --font-tmn03-sans: 'Figtree', -apple-system, system-ui, sans-serif;
}
/* Icon base: utilities (fill-*, text-*) still win because this sits in the base layer. */

@layer base {
  .tmn-03 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-03 {
  width: 100%;
  min-height: 100svh;
}
```
