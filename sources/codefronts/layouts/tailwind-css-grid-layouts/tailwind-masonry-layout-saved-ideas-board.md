---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-masonry-layout-saved-ideas-board/"
title: "Tailwind Masonry Layout for a Saved Ideas Board"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A saved-ideas board — the Pinterest pattern — with real photography, per-pin authors and save counts."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Masonry Layout for a Saved Ideas Board
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-masonry-layout-saved-ideas-board/

A saved-ideas board — the Pinterest pattern — with real photography, per-pin authors and save counts. Each pin spans a number of 8px rows that your CMS computes, so the waterfall needs no library and no measuring pass.
## HTML
```html
<section class="tgx-13 w-full min-h-svh bg-tgx13-bg font-tgx13-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-4">
    <div class="flex flex-col gap-1">
      <p class="text-[0.68rem] tracking-[0.18em] uppercase text-tgx13-mut">Board · Slow mornings</p>
      <h2 class="text-[1.35rem] font-semibold text-tgx13-ink tracking-[-0.01em]">148 saved ideas</h2>
    </div>
    <button type="button" class="text-[0.8rem] font-semibold text-white bg-tgx13-accent rounded-full px-4 min-h-11 cursor-pointer transition-colors hover:bg-tgx13-accentdark focus-visible:outline-2 focus-visible:outline-tgx13-accent focus-visible:outline-offset-2">Save all</button>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(168px,100%),1fr))] auto-rows-[8px] grid-flow-dense gap-3">
    <article style="--r:30" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1475924156734-496f6cac6ec1?w=500&h=650&q=80&auto=format&fit=crop" alt="Cup of coffee on a wooden table beside a notebook" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Filter, not machine</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">1.2k</span>
      </div>
    </article>
    <article style="--r:40" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&h=800&q=80&auto=format&fit=crop" alt="Sunlit living room with a low sofa and pale walls" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Low sofa, high windows</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">3.8k</span>
      </div>
    </article>
    <article style="--r:26" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&h=500&q=80&auto=format&fit=crop" alt="Bowl of salad with grains and greens on a plain background" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Ten-minute grain bowl</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">942</span>
      </div>
    </article>
    <article style="--r:34" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=500&h=700&q=80&auto=format&fit=crop" alt="Single wooden chair against a textured plaster wall" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">One good chair</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">2.1k</span>
      </div>
    </article>
    <article style="--r:24" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=500&h=420&q=80&auto=format&fit=crop" alt="Plated dish photographed from above on a dark surface" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Sunday, slowly</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">612</span>
      </div>
    </article>
    <article style="--r:36" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1503602642458-232111445657?w=500&h=750&q=80&auto=format&fit=crop" alt="Minimal reading corner with a lamp and a stack of books" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Reading corner</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">4.4k</span>
      </div>
    </article>
    <article style="--r:28" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?w=500&h=560&q=80&auto=format&fit=crop" alt="Desk with a laptop, notebook and plant in soft daylight" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Desk, reset</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">1.9k</span>
      </div>
    </article>
    <article style="--r:32" class="[grid-row:span_var(--r)] group flex flex-col overflow-hidden rounded-2xl bg-white shadow-[0_8px_20px_-16px_oklch(0.4_0.03_60/0.9)]">
      <div class="flex-1 overflow-hidden bg-tgx13-cell"><img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=500&h=660&q=80&auto=format&fit=crop" alt="Flat sea horizon under a pale sky" loading="lazy" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105 motion-reduce:transition-none motion-reduce:group-hover:scale-100"></div>
      <div class="flex items-center justify-between gap-2 px-3 py-2">
        <p class="text-[0.75rem] font-medium text-tgx13-ink truncate">Nothing to do</p>
        <span class="text-[0.68rem] tabular-nums text-tgx13-mut">7.6k</span>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx13-bg: #f6f2ec;
  --color-tgx13-bg: oklch(0.96 0.008 75);
  --color-tgx13-cell: #e6e0d6;
  --color-tgx13-cell: oklch(0.9 0.012 75);
  --color-tgx13-ink: #3b332b;
  --color-tgx13-ink: oklch(0.33 0.015 70);
  --color-tgx13-mut: #75695c;
  --color-tgx13-mut: oklch(0.52 0.02 70);
  --color-tgx13-accent: #b03a2e;
  --color-tgx13-accent: oklch(0.5 0.16 28);
  --color-tgx13-accentdark: #8d2d23;
  --color-tgx13-accentdark: oklch(0.42 0.15 28);
  --font-tgx13-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-13 {
  width: 100%;
  min-height: 100svh;
}
```
