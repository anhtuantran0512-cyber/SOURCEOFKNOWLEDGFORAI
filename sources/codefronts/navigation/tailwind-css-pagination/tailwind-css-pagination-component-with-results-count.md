---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-component-with-results-count/"
title: "Tailwind CSS Pagination Component with Results Count"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "The canonical card-footer pagination: \"Showing 21 to 30 of 97 results\" on the left, a full numbered bar with an ellipsis on the right, and a thumb-sized…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pagination Component with Results Count
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-css-pagination-component-with-results-count/

The canonical card-footer pagination: "Showing 21 to 30 of 97 results" on the left, a full numbered bar with an ellipsis on the right, and a thumb-sized Previous / Next pair that replaces it on phones. The forty-utility button string is defined once as a Tailwind v4 @utility tpg07-page &mdash; the modern replacement for an @layer components + @apply class &mdash; so every page link in the markup reads as one word.
## HTML
```html
<section class="tpg-07 w-full min-h-svh grid place-items-center bg-tpg07-bg bg-[radial-gradient(70%_60%_at_50%_20%,var(--color-tpg07-glow),transparent_72%)] px-5 py-14 font-tpg07-sans text-tpg07-ink antialiased" aria-label="Tailwind CSS pagination component with results count demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[48rem] overflow-hidden rounded-2xl bg-tpg07-card shadow-tpg07-card ring-1 ring-tpg07-acc/15 transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <header class="flex items-center justify-between gap-4 px-4 py-4 sm:px-6">
        <div>
          <h2 class="text-[15px] font-semibold tracking-[-0.01em]">Customers</h2>
          <p class="mt-0.5 text-[13px] text-tpg07-mut">Active subscriptions, sorted by monthly revenue</p>
        </div>
        <span class="hidden rounded-md bg-tpg07-acc/8 px-2 py-1 font-tpg07-mono text-[11px] text-tpg07-acc-ink ring-1 ring-tpg07-acc/20 ring-inset sm:inline">sort: mrr desc</span>
      </header>

      <ul class="divide-y divide-tpg07-line border-y border-tpg07-line" aria-label="Customers, page 3">
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-6">
          <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-to-br from-tpg07-acc/18 to-tpg07-acc2/18 text-[12px] font-semibold text-tpg07-acc-ink ring-1 ring-tpg07-acc/20">LM</span>
          <div class="min-w-0 flex-1"><p class="truncate text-sm font-medium">Lena Marsh</p><p class="truncate text-[13px] text-tpg07-mut">[email protected]</p></div>
          <span class="rounded-md bg-tpg07-acc/8 px-2 py-0.5 text-xs font-medium text-tpg07-acc-ink ring-1 ring-tpg07-acc/20 ring-inset max-sm:hidden">Team</span>
          <p class="w-20 text-right font-tpg07-mono text-[13px] font-medium tabular-nums">$1,240</p>
        </li>
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-6">
          <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-to-br from-tpg07-acc/18 to-tpg07-acc2/18 text-[12px] font-semibold text-tpg07-acc-ink ring-1 ring-tpg07-acc/20">DK</span>
          <div class="min-w-0 flex-1"><p class="truncate text-sm font-medium">Dev Kapoor</p><p class="truncate text-[13px] text-tpg07-mut">[email protected]</p></div>
          <span class="rounded-md bg-tpg07-acc/8 px-2 py-0.5 text-xs font-medium text-tpg07-acc-ink ring-1 ring-tpg07-acc/20 ring-inset max-sm:hidden">Business</span>
          <p class="w-20 text-right font-tpg07-mono text-[13px] font-medium tabular-nums">$1,180</p>
        </li>
        <li class="flex items-center gap-3.5 px-4 py-3.5 sm:px-6">
          <span aria-hidden="true" class="grid size-9 flex-none place-items-center rounded-full bg-linear-to-br from-tpg07-acc/18 to-tpg07-acc2/18 text-[12px] font-semibold text-tpg07-acc-ink ring-1 ring-tpg07-acc/20">SO</span>
          <div class="min-w-0 flex-1"><p class="truncate text-sm font-medium">Sofia Ortega</p><p class="truncate text-[13px] text-tpg07-mut">[email protected]</p></div>
          <span class="rounded-md bg-tpg07-acc/8 px-2 py-0.5 text-xs font-medium text-tpg07-acc-ink ring-1 ring-tpg07-acc/20 ring-inset max-sm:hidden">Team</span>
          <p class="w-20 text-right font-tpg07-mono text-[13px] font-medium tabular-nums">$1,095</p>
        </li>
      </ul>

      <div class="flex items-center justify-between gap-4 bg-tpg07-sunk/60 px-4 py-3 sm:px-6">
        <p class="text-[13px] text-tpg07-mut tabular-nums max-sm:hidden">Showing <b class="font-semibold text-tpg07-ink">21</b> to <b class="font-semibold text-tpg07-ink">30</b> of <b class="font-semibold text-tpg07-ink">97</b> results</p>
        <nav aria-label="Pagination" class="max-sm:w-full">
          <ul class="flex items-center justify-between gap-3 sm:hidden">
            <li><a href="?page=2" rel="prev" class="tpg07-page gap-1.5 bg-tpg07-card px-3.5 shadow-[0_1px_2px_oklch(0.35_0.1_305/0.08)] ring-1 ring-tpg07-acc/20"><svg class="size-4 text-tpg07-acc-ink" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>Previous</a></li>
            <li class="text-[13px] text-tpg07-mut tabular-nums"><b class="me-0.5 inline-block rounded-md bg-linear-to-br from-tpg07-acc to-tpg07-acc2 px-2 py-1 font-semibold text-tpg07-on shadow-[inset_0_1px_0_oklch(1_0_0/0.28),0_6px_16px_-6px_var(--color-tpg07-acc2)]">21–30</b> of 97</li>
            <li><a href="?page=4" rel="next" class="tpg07-page gap-1.5 bg-tpg07-card px-3.5 shadow-[0_1px_2px_oklch(0.35_0.1_305/0.08)] ring-1 ring-tpg07-acc/20">Next<svg class="size-4 text-tpg07-acc-ink" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ul>
          <ol class="flex items-center gap-1 rounded-xl bg-tpg07-card p-1 shadow-[0_1px_2px_oklch(0.35_0.1_305/0.08)] ring-1 ring-tpg07-acc/20 max-sm:hidden">
            <li><a href="?page=2" rel="prev" aria-label="Previous page" class="tpg07-page px-2.5"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
            <li><a href="?page=1" class="tpg07-page">1</a></li>
            <li><a href="?page=2" class="tpg07-page">2</a></li>
            <li><a href="?page=3" aria-current="page" class="tpg07-page">3</a></li>
            <li><a href="?page=4" class="tpg07-page">4</a></li>
            <li aria-hidden="true" class="grid min-w-8 place-items-center text-sm font-bold tracking-widest text-tpg07-acc-ink/70">…</li>
            <li><a href="?page=9" class="tpg07-page">9</a></li>
            <li><a href="?page=10" class="tpg07-page">10</a></li>
            <li><a href="?page=4" rel="next" aria-label="Next page" class="tpg07-page px-2.5"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
          </ol>
        </nav>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg07-card px-3.5 py-2 text-center font-tpg07-mono text-[11.5px] text-tpg07-acc-ink ring-1 ring-tpg07-acc/20">@utility tpg07-page · aria-[current=page]:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg07-bg: #f9f5fd;
  --color-tpg07-bg: oklch(0.975 0.012 310);
  --color-tpg07-glow: #f4d9ffb3;
  --color-tpg07-glow: oklch(0.92 0.06 315 / 0.7);
  --color-tpg07-card: #fffdff;
  --color-tpg07-card: oklch(0.997 0.004 310);
  --color-tpg07-sunk: #f6f1fb;
  --color-tpg07-sunk: oklch(0.965 0.015 310);
  --color-tpg07-ink: #20182d;
  --color-tpg07-ink: oklch(0.23 0.04 300);
  --color-tpg07-mut: #665b73;
  --color-tpg07-mut: oklch(0.49 0.04 305);
  --color-tpg07-line: #e6ddee;
  --color-tpg07-line: oklch(0.91 0.025 310);
  --color-tpg07-acc: #7c3aed;
  --color-tpg07-acc: oklch(0.541 0.247 293);
  --color-tpg07-acc2: #a11db1;
  --color-tpg07-acc2: oklch(0.518 0.226 323);
  --color-tpg07-acc-ink: #7330d4;
  --color-tpg07-acc-ink: oklch(0.5 0.23 295);
  --color-tpg07-on: #ffffff;
  --color-tpg07-on: oklch(1 0 0);
  --font-tpg07-sans: 'Geist', system-ui, sans-serif;
  --font-tpg07-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tpg07-card: 0 1px 2px oklch(0.35 0.1 305 / 0.08), 0 28px 56px -26px oklch(0.45 0.2 305 / 0.38);
}
/* The reusable page link: one @utility instead of forty classes on every <a>.
   It sorts and layers like a built-in utility and still accepts variants in markup.
   Current page: violet -> fuchsia gradient, inner top highlight and an orchid glow. */

@utility tpg07-page {
  @apply relative inline-flex min-h-11 min-w-11 cursor-pointer items-center justify-center rounded-lg px-3 text-sm font-medium text-tpg07-ink tabular-nums no-underline transition-[background-color,color,box-shadow,translate,scale] duration-200 ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg07-acc/10 not-aria-[current=page]:hover:text-tpg07-acc-ink active:scale-[0.96] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg07-acc aria-[current=page]:bg-linear-to-br aria-[current=page]:from-tpg07-acc aria-[current=page]:to-tpg07-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-tpg07-on aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.28),0_8px_22px_-6px_var(--color-tpg07-acc2)] motion-reduce:transition-none motion-reduce:hover:translate-y-0;
}
/* Dark "plum night": re-point the same tokens; the utility above follows automatically.
   The gradient turns pastel and the digit turns deep plum, so it stays above 9:1. */

@media (prefers-color-scheme: dark) {
  .tpg-07:not([data-theme="light"]) {
    --color-tpg07-bg: #14091b;
    --color-tpg07-bg: oklch(0.165 0.04 310);
    --color-tpg07-glow: #42165380;
    --color-tpg07-glow: oklch(0.3 0.11 315 / 0.5);
    --color-tpg07-card: #1f1228;
    --color-tpg07-card: oklch(0.21 0.045 310);
    --color-tpg07-sunk: #291a33;
    --color-tpg07-sunk: oklch(0.25 0.05 310);
    --color-tpg07-ink: #f4f0f7;
    --color-tpg07-ink: oklch(0.96 0.01 310);
    --color-tpg07-mut: #bfb1cb;
    --color-tpg07-mut: oklch(0.78 0.04 310);
    --color-tpg07-line: #3f2c4c;
    --color-tpg07-line: oklch(0.33 0.06 310);
    --color-tpg07-acc: #c1afff;
    --color-tpg07-acc: oklch(0.8 0.12 293);
    --color-tpg07-acc2: #eca9ef;
    --color-tpg07-acc2: oklch(0.82 0.12 325);
    --color-tpg07-acc-ink: #c1afff;
    --color-tpg07-acc-ink: oklch(0.8 0.12 293);
    --color-tpg07-on: #1c0d2b;
    --color-tpg07-on: oklch(0.2 0.06 305);
  }
}

.tpg-07[data-theme="dark"] {
  --color-tpg07-bg: #14091b;
  --color-tpg07-bg: oklch(0.165 0.04 310);
  --color-tpg07-glow: #42165380;
  --color-tpg07-glow: oklch(0.3 0.11 315 / 0.5);
  --color-tpg07-card: #1f1228;
  --color-tpg07-card: oklch(0.21 0.045 310);
  --color-tpg07-sunk: #291a33;
  --color-tpg07-sunk: oklch(0.25 0.05 310);
  --color-tpg07-ink: #f4f0f7;
  --color-tpg07-ink: oklch(0.96 0.01 310);
  --color-tpg07-mut: #bfb1cb;
  --color-tpg07-mut: oklch(0.78 0.04 310);
  --color-tpg07-line: #3f2c4c;
  --color-tpg07-line: oklch(0.33 0.06 310);
  --color-tpg07-acc: #c1afff;
  --color-tpg07-acc: oklch(0.8 0.12 293);
  --color-tpg07-acc2: #eca9ef;
  --color-tpg07-acc2: oklch(0.82 0.12 325);
  --color-tpg07-acc-ink: #c1afff;
  --color-tpg07-acc-ink: oklch(0.8 0.12 293);
  --color-tpg07-on: #1c0d2b;
  --color-tpg07-on: oklch(0.2 0.06 305);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-07 {
  width: 100%;
  min-height: 100svh;
}
```
