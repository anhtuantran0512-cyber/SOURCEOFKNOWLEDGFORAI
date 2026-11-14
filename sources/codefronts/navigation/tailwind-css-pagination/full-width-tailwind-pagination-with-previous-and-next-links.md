---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/full-width-tailwind-pagination-with-previous-and-next-links/"
title: "Full-Width Tailwind Pagination with Previous and Next Links"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "The documentation-footer pattern: the previous chapter pinned left, the next chapter pinned right, chapter numbers dead centre."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Width Tailwind Pagination with Previous and Next Links
Source: https://codefronts.com/navigation/tailwind-css-pagination/full-width-tailwind-pagination-with-previous-and-next-links/

The documentation-footer pattern: the previous chapter pinned left, the next chapter pinned right, chapter numbers dead centre. A grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] track keeps the numbers on the true centre line no matter how long either title runs, and a @container query folds the bar into a numbers-on-top, two-card layout when the column &mdash; not the viewport &mdash; gets narrow.
## HTML
```html
<section class="tpg-18 w-full min-h-svh grid place-items-center bg-tpg18-bg bg-[radial-gradient(60%_50%_at_15%_0%,var(--color-tpg18-glow),transparent_70%),radial-gradient(50%_45%_at_90%_100%,var(--color-tpg18-glow2),transparent_70%)] px-4 py-14 font-tpg18-sans text-tpg18-ink antialiased sm:px-5" aria-label="Full-width previous and next pagination demo">
  <div class="grid w-full justify-items-center gap-7">
    <article class="@container w-full max-w-[64rem] rounded-2xl bg-tpg18-card px-5 pt-8 pb-6 shadow-tpg18-card ring-1 ring-tpg18-line sm:px-10 sm:pt-10">
      <p class="font-tpg18-mono text-xs text-tpg18-hl">Guides / Layout / Chapter 7</p>
      <h2 class="mt-2 text-2xl font-semibold tracking-[-0.025em] sm:text-[1.75rem]">Container queries in practice</h2>
      <p class="mt-3 max-w-[44rem] text-[15px] leading-relaxed text-pretty text-tpg18-mut">That is the whole pattern: mark the wrapper with <code class="rounded-md bg-tpg18-raise px-1.5 py-0.5 font-tpg18-mono text-[13px] text-tpg18-ink">@container</code>, then let each child decide how it folds. In the next chapter we use the same idea to place tooltips with anchor positioning.</p>
      <div class="mt-8 flex flex-wrap items-center justify-between gap-x-6 gap-y-3 border-t border-tpg18-line pt-5 text-[13px] text-tpg18-mut">
        <p class="tabular-nums">Last updated <time datetime="2026-10-09">Oct 9, 2026</time></p>
        <a href="#tpg-18-edit" class="-mx-2 inline-flex min-h-11 items-center gap-1.5 rounded-lg px-2 font-medium text-tpg18-ink underline decoration-tpg18-sky/50 underline-offset-4 transition-colors hover:text-tpg18-hl hover:decoration-tpg18-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">Edit this page<svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M5.5 3.5h7v7M12.5 3.5 4 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>
      <nav aria-label="Pagination" class="mt-5 grid grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] items-center gap-4 @max-[44rem]:grid-cols-2 @max-[44rem]:items-stretch @max-[44rem]:gap-3">
        <a href="#tpg-18-ch6" rel="prev" class="group flex min-h-16 min-w-0 items-center gap-3 rounded-xl px-4 py-3 @max-[44rem]:items-start @max-[44rem]:px-3.5 relative bg-tpg18-card ring-1 ring-tpg18-line transition duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:bg-tpg18-raise hover:shadow-tpg18-lift hover:ring-transparent motion-reduce:hover:translate-y-0 before:pointer-events-none before:absolute before:inset-0 before:rounded-[inherit] before:bg-linear-to-br before:from-tpg18-acc before:to-tpg18-sky before:p-px before:opacity-0 before:transition-opacity before:duration-300 before:[-webkit-mask-composite:xor] before:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask:linear-gradient(#000_0_0)_content-box_exclude,linear-gradient(#000_0_0)] hover:before:opacity-100 focus-visible:before:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">
          <svg class="flex-none text-tpg18-mut @max-[44rem]:hidden transition-transform duration-200 group-hover:-translate-x-0.5 group-hover:text-tpg18-hl motion-reduce:transition-none" viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="grid min-w-0 gap-0.5"><span class="text-xs text-tpg18-mut"><span aria-hidden="true" class="hidden @max-[44rem]:inline">&larr; </span>Previous</span><span class="truncate text-[15px] font-medium tracking-[-0.01em] @max-[44rem]:line-clamp-2 @max-[44rem]:text-sm @max-[44rem]:whitespace-normal">Styling native form controls with accent-color</span></span>
        </a>
        <ol class="flex items-center justify-center gap-1 @max-[44rem]:order-first @max-[44rem]:col-span-2">
          <li><a href="#tpg-18-ch1" aria-label="Chapter 1" class="grid min-h-11 min-w-11 place-items-center rounded-lg px-2 text-sm font-medium text-tpg18-mut tabular-nums transition-colors hover:bg-tpg18-acc/10 hover:text-tpg18-hl focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">1</a></li>
          <li aria-hidden="true" class="grid min-h-11 w-6 place-items-center text-sm font-bold tracking-widest text-tpg18-sky">&hellip;</li>
          <li><a href="#tpg-18-ch6" aria-label="Chapter 6" class="grid min-h-11 min-w-11 place-items-center rounded-lg px-2 text-sm font-medium text-tpg18-mut tabular-nums transition-colors hover:bg-tpg18-acc/10 hover:text-tpg18-hl focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">6</a></li>
          <li><a href="#tpg-18-ch7" aria-label="Chapter 7" aria-current="page" class="relative grid min-h-11 min-w-11 place-items-center rounded-lg bg-linear-to-br from-tpg18-acc to-tpg18-acc2 px-2 text-sm font-semibold text-white tabular-nums shadow-tpg18-on after:absolute after:inset-x-2.5 after:-bottom-2 after:h-0.5 after:rounded-full after:bg-linear-to-r after:from-tpg18-acc after:to-tpg18-sky focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">7</a></li>
          <li><a href="#tpg-18-ch8" aria-label="Chapter 8" class="grid min-h-11 min-w-11 place-items-center rounded-lg px-2 text-sm font-medium text-tpg18-mut tabular-nums transition-colors hover:bg-tpg18-acc/10 hover:text-tpg18-hl focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">8</a></li>
          <li aria-hidden="true" class="grid min-h-11 w-6 place-items-center text-sm font-bold tracking-widest text-tpg18-sky">&hellip;</li>
          <li><a href="#tpg-18-ch14" aria-label="Chapter 14" class="grid min-h-11 min-w-11 place-items-center rounded-lg px-2 text-sm font-medium text-tpg18-mut tabular-nums transition-colors hover:bg-tpg18-acc/10 hover:text-tpg18-hl focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">14</a></li>
        </ol>
        <a href="#tpg-18-ch8" rel="next" class="group flex min-h-16 min-w-0 items-center justify-end gap-3 rounded-xl px-4 py-3 @max-[44rem]:items-start @max-[44rem]:px-3.5 text-right relative bg-tpg18-card ring-1 ring-tpg18-line transition duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-0.5 hover:bg-tpg18-raise hover:shadow-tpg18-lift hover:ring-transparent motion-reduce:hover:translate-y-0 before:pointer-events-none before:absolute before:inset-0 before:rounded-[inherit] before:bg-linear-to-br before:from-tpg18-acc before:to-tpg18-sky before:p-px before:opacity-0 before:transition-opacity before:duration-300 before:[-webkit-mask-composite:xor] before:[-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] before:[mask:linear-gradient(#000_0_0)_content-box_exclude,linear-gradient(#000_0_0)] hover:before:opacity-100 focus-visible:before:opacity-100 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg18-ring">
          <span class="grid min-w-0 gap-0.5"><span class="text-xs text-tpg18-mut">Next<span aria-hidden="true" class="hidden @max-[44rem]:inline"> &rarr;</span></span><span class="truncate text-[15px] font-medium tracking-[-0.01em] @max-[44rem]:line-clamp-2 @max-[44rem]:text-sm @max-[44rem]:whitespace-normal">Anchor positioning</span></span>
          <svg class="flex-none text-tpg18-mut @max-[44rem]:hidden transition-transform duration-200 group-hover:translate-x-0.5 group-hover:text-tpg18-hl motion-reduce:transition-none" viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
      </nav>
    </article>
    <p aria-hidden="true" class="max-w-full rounded-2xl px-3.5 py-2 text-center font-tpg18-mono text-[11.5px] text-tpg18-mut ring-1 ring-tpg18-line">grid-cols-[minmax(0,1fr)_auto_minmax(0,1fr)] &middot; truncate &middot; @max-[44rem]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg18-bg: #f1f2fd;
  --color-tpg18-bg: oklch(0.965 0.017 275);
  --color-tpg18-glow: #c7d2fe99;
  --color-tpg18-glow: oklch(0.87 0.065 275 / 0.6);
  --color-tpg18-glow2: #bae6fd80;
  --color-tpg18-glow2: oklch(0.9 0.06 230 / 0.5);
  --color-tpg18-card: #fdfdff;
  --color-tpg18-card: oklch(0.995 0.004 275);
  --color-tpg18-raise: #eef0fe;
  --color-tpg18-raise: oklch(0.955 0.022 275);
  --color-tpg18-ink: #161a33;
  --color-tpg18-ink: oklch(0.23 0.045 275);
  --color-tpg18-mut: #535a7a;
  --color-tpg18-mut: oklch(0.48 0.05 275);
  --color-tpg18-line: #e0e3f6;
  --color-tpg18-line: oklch(0.915 0.025 275);
  --color-tpg18-hl: #4338ca;
  --color-tpg18-hl: oklch(0.457 0.24 277);
  --color-tpg18-acc: #4f46e5;
  --color-tpg18-acc: oklch(0.511 0.262 277);
  --color-tpg18-acc2: #0369a1;
  --color-tpg18-acc2: oklch(0.5 0.134 242.7);
  --color-tpg18-sky: #0ea5e9;
  --color-tpg18-sky: oklch(0.685 0.169 237.3);
  --color-tpg18-ring: #4f46e5;
  --color-tpg18-ring: oklch(0.511 0.262 277);
  --font-tpg18-sans: 'Geist', system-ui, sans-serif;
  --font-tpg18-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tpg18-card: 0 1px 2px oklch(0.3 0.1 276 / 0.06), 0 22px 50px -22px oklch(0.45 0.2 276 / 0.32);
  --shadow-tpg18-on: 0 8px 20px -6px oklch(0.51 0.26 277 / 0.6), inset 0 1px 0 oklch(1 0 0 / 0.25);
  --shadow-tpg18-lift: 0 12px 28px -16px oklch(0.51 0.26 277 / 0.55);
}

@media (prefers-color-scheme: dark) {
  .tpg-18:not([data-theme="light"]) {
    --color-tpg18-bg: #0b0d24;
    --color-tpg18-bg: oklch(0.17 0.045 275);
    --color-tpg18-glow: #312e8166;
    --color-tpg18-glow: oklch(0.35 0.14 277 / 0.4);
    --color-tpg18-glow2: #0c4a6e59;
    --color-tpg18-glow2: oklch(0.39 0.09 240 / 0.35);
    --color-tpg18-card: #12152e;
    --color-tpg18-card: oklch(0.205 0.05 276);
    --color-tpg18-raise: #1b1f42;
    --color-tpg18-raise: oklch(0.255 0.065 276);
    --color-tpg18-ink: #eef0ff;
    --color-tpg18-ink: oklch(0.96 0.02 276);
    --color-tpg18-mut: #a3a9cf;
    --color-tpg18-mut: oklch(0.75 0.05 276);
    --color-tpg18-line: #262b52;
    --color-tpg18-line: oklch(0.3 0.07 276);
    --color-tpg18-hl: #a5b4fc;
    --color-tpg18-hl: oklch(0.785 0.115 274.7);
    --color-tpg18-ring: #818cf8;
    --color-tpg18-ring: oklch(0.673 0.182 276.9);
  }
}

.tpg-18[data-theme="dark"] {
  --color-tpg18-bg: #0b0d24;
  --color-tpg18-bg: oklch(0.17 0.045 275);
  --color-tpg18-glow: #312e8166;
  --color-tpg18-glow: oklch(0.35 0.14 277 / 0.4);
  --color-tpg18-glow2: #0c4a6e59;
  --color-tpg18-glow2: oklch(0.39 0.09 240 / 0.35);
  --color-tpg18-card: #12152e;
  --color-tpg18-card: oklch(0.205 0.05 276);
  --color-tpg18-raise: #1b1f42;
  --color-tpg18-raise: oklch(0.255 0.065 276);
  --color-tpg18-ink: #eef0ff;
  --color-tpg18-ink: oklch(0.96 0.02 276);
  --color-tpg18-mut: #a3a9cf;
  --color-tpg18-mut: oklch(0.75 0.05 276);
  --color-tpg18-line: #262b52;
  --color-tpg18-line: oklch(0.3 0.07 276);
  --color-tpg18-hl: #a5b4fc;
  --color-tpg18-hl: oklch(0.785 0.115 274.7);
  --color-tpg18-ring: #818cf8;
  --color-tpg18-ring: oklch(0.673 0.182 276.9);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-18 {
  width: 100%;
  min-height: 100svh;
}
```
