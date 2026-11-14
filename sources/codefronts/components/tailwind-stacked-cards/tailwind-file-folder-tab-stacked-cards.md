---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-file-folder-tab-stacked-cards/"
title: "Tailwind File Folder Tab Stacked Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "Manila dividers, done in utilities."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind File Folder Tab Stacked Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-file-folder-tab-stacked-cards/

Manila dividers, done in utilities. The tab silhouette is [clip-path:polygon(8%_0,92%_0,100%_100%,0_100%)] &mdash; a shape with no utility and no need for one &mdash; and the same nesting trick as demo 08 retires six :nth-of-type pairings in favour of plain peer-checked:. Resting folders sit dimmed behind; the checked one comes forward at full strength.
## HTML
```html
<section class="stk-18 w-full min-h-svh flex items-center justify-center px-5 py-15 font-stk18-sans bg-stk18-bg" aria-label="File folder tab stack">
  <div class="relative w-[min(420px,100%)] h-65 pt-9.5">
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-18" id="stk-18-1" checked>
      <label class="absolute top-0 left-[calc(var(--l)*33.3%)] z-5 flex h-10.5 w-[32%] items-center justify-center pb-1.5 bg-stk18-f1 text-sm font-extrabold text-stk18-ink cursor-pointer brightness-82 transition-[filter,transform] duration-250 [clip-path:polygon(8%_0,92%_0,100%_100%,0_100%)] hover:brightness-94 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2 motion-reduce:transition-none" for="stk-18-1" style="--l:0">2024</label>
      <article class="absolute inset-x-0 top-9 z-1 h-55 rounded-[2px_8px_8px_8px] bg-stk18-f1 p-6.5 text-stk18-ink opacity-50 shadow-[0_20px_40px_-24px_rgba(0,0,0,0.7)] transition-opacity duration-300 peer-checked:z-4 peer-checked:opacity-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-2.5 text-2xl font-black tracking-[-0.02em]">FY2024</h3>
        <p class="m-0 max-w-[36ch] text-[15px] leading-relaxed">Revenue $2.1M &middot; 14 clients &middot; 3 new hires. The year we found product&#8209;market fit.</p>
      </article>
    </div>
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-18" id="stk-18-2">
      <label class="absolute top-0 left-[calc(var(--l)*33.3%)] z-5 flex h-10.5 w-[32%] items-center justify-center pb-1.5 bg-stk18-f2 text-sm font-extrabold text-stk18-ink cursor-pointer brightness-82 transition-[filter,transform] duration-250 [clip-path:polygon(8%_0,92%_0,100%_100%,0_100%)] hover:brightness-94 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2 motion-reduce:transition-none" for="stk-18-2" style="--l:1">2025</label>
      <article class="absolute inset-x-0 top-9 z-1 h-55 rounded-[2px_8px_8px_8px] bg-stk18-f2 p-6.5 text-stk18-ink opacity-50 shadow-[0_20px_40px_-24px_rgba(0,0,0,0.7)] transition-opacity duration-300 peer-checked:z-4 peer-checked:opacity-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-2.5 text-2xl font-black tracking-[-0.02em]">FY2025</h3>
        <p class="m-0 max-w-[36ch] text-[15px] leading-relaxed">Revenue $5.4M &middot; 38 clients &middot; shipped the platform rewrite on time.</p>
      </article>
    </div>
    <div class="contents">
      <input class="peer sr-only" type="radio" name="stk-18" id="stk-18-3">
      <label class="absolute top-0 left-[calc(var(--l)*33.3%)] z-5 flex h-10.5 w-[32%] items-center justify-center pb-1.5 bg-stk18-f3 text-sm font-extrabold text-stk18-ink cursor-pointer brightness-82 transition-[filter,transform] duration-250 [clip-path:polygon(8%_0,92%_0,100%_100%,0_100%)] hover:brightness-94 peer-checked:brightness-100 peer-checked:-translate-y-1 peer-focus-visible:outline-3 peer-focus-visible:outline-white peer-focus-visible:outline-offset-2 motion-reduce:transition-none" for="stk-18-3" style="--l:2">2026</label>
      <article class="absolute inset-x-0 top-9 z-1 h-55 rounded-[2px_8px_8px_8px] bg-stk18-f3 p-6.5 text-stk18-ink opacity-50 shadow-[0_20px_40px_-24px_rgba(0,0,0,0.7)] transition-opacity duration-300 peer-checked:z-4 peer-checked:opacity-100 motion-reduce:transition-none">
        <h3 class="m-0 mb-2.5 text-2xl font-black tracking-[-0.02em]">FY2026</h3>
        <p class="m-0 max-w-[36ch] text-[15px] leading-relaxed">Revenue $9.0M projected &middot; expanding to the EU &middot; Series A closed in Q1.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk18-bg: #2a2620;
  --color-stk18-bg: oklch(0.27 0.014 70);
  --color-stk18-ink: #2a2415;
  --color-stk18-ink: oklch(0.26 0.028 85);
  --color-stk18-f1: #e0b96a;
  --color-stk18-f1: oklch(0.80 0.11 75);
  --color-stk18-f2: #7ecaa3;
  --color-stk18-f2: oklch(0.80 0.11 155);
  --color-stk18-f3: #86c2e8;
  --color-stk18-f3: oklch(0.80 0.10 235);
  --font-stk18-sans: 'Archivo', system-ui, sans-serif;
}
```
