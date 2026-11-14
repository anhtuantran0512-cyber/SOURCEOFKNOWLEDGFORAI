---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/bootstrap-5-style-pagination-in-tailwind-css/"
title: "Bootstrap 5 Style Pagination in Tailwind CSS"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A migration guide you can paste: Bootstrap 5's joined .pagination / .page-item / .page-link bar, rebuilt in Tailwind v4 with the same mental model. .active…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Style Pagination in Tailwind CSS
Source: https://codefronts.com/navigation/tailwind-css-pagination/bootstrap-5-style-pagination-in-tailwind-css/

A migration guide you can paste: Bootstrap 5's joined .pagination / .page-item / .page-link bar, rebuilt in Tailwind v4 with the same mental model. .active becomes aria-[current=page]:, .disabled becomes aria-disabled:, the shared borders collapse with not-first:-ms-px, and the end caps round themselves with first:*:rounded-s-xl &mdash; plus a side-by-side table of every class you are replacing.
## HTML
```html
<section class="tpg-08 w-full min-h-svh grid place-items-center bg-tpg08-bg bg-[radial-gradient(65%_50%_at_50%_35%,var(--color-tpg08-glow),transparent_72%)] px-5 py-14 font-tpg08-sans text-tpg08-ink antialiased" aria-label="Bootstrap 5 style pagination in Tailwind CSS demo">
  <div class="grid w-full max-w-[44rem] gap-6">
    <header class="transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-2 starting:opacity-0 motion-reduce:transition-none">
      <p class="inline-flex items-center gap-2 rounded-full bg-tpg08-acc/8 px-2.5 py-1 font-tpg08-mono text-[11px] font-medium text-tpg08-mut ring-1 ring-tpg08-acc/20"><span class="text-tpg08-acc-ink">.pagination</span> <span aria-hidden="true">→</span> utilities</p>
      <h2 class="mt-3 text-[clamp(1.4rem,3.4vw,1.85rem)] leading-tight font-semibold tracking-[-0.025em] text-balance">Bootstrap pagination, rebuilt in Tailwind CSS</h2>
      <p class="mt-2 max-w-[36rem] text-[15px] leading-relaxed text-pretty text-tpg08-mut">Same joined bar, same active and disabled states &mdash; now driven by <code class="whitespace-nowrap font-tpg08-mono text-[13px] text-tpg08-ink">aria-current</code> and <code class="whitespace-nowrap font-tpg08-mono text-[13px] text-tpg08-ink">aria-disabled</code> instead of extra classes.</p>
    </header>

    <div class="grid justify-items-center rounded-2xl bg-tpg08-card px-4 py-9 shadow-tpg08-card ring-1 ring-tpg08-acc/15 transition delay-75 duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <nav aria-label="Pagination">
        <ul class="flex">
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a role="link" aria-disabled="true" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc aria-disabled:pointer-events-none aria-disabled:bg-tpg08-sunk aria-disabled:text-tpg08-mut aria-disabled:border-tpg08-line sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Previous</span></a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=1" aria-current="page" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc aria-[current=page]:z-10 aria-[current=page]:border-transparent aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg08-acc aria-[current=page]:to-tpg08-acc2 aria-[current=page]:font-semibold aria-[current=page]:text-tpg08-on aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.3),inset_0_-2px_0_oklch(0_0_0/0.18),0_10px_24px_-8px_var(--color-tpg08-acc2)] sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none">1</a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=2" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none">2</a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=3" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none">3</a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=4" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none">4</a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=5" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none">5</a></li>
          <li class="not-first:-ms-px first:*:rounded-s-xl last:*:rounded-e-xl"><a href="?page=2" rel="next" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 border border-tpg08-acc/20 bg-tpg08-card px-3 text-sm font-medium text-tpg08-acc-ink tabular-nums transition-colors duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:z-10 not-aria-[current=page]:hover:border-tpg08-acc/45 not-aria-[current=page]:hover:bg-tpg08-acc/8 after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-0.5 after:origin-left after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg08-acc after:to-tpg08-acc2 after:transition-transform after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] not-aria-[current=page]:hover:after:scale-x-100 aria-disabled:after:hidden motion-reduce:after:transition-none focus-visible:z-20 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg08-acc sm:min-h-12 sm:px-4 sm:text-[15px] motion-reduce:transition-none"><span class="max-sm:sr-only">Next</span><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
        </ul>
      </nav>
      <p class="mt-4 text-[13px] text-tpg08-mut tabular-nums">Page 1 of 5 · Previous is disabled on the first page</p>
    </div>

    <div class="overflow-hidden rounded-2xl bg-tpg08-card shadow-[0_12px_32px_-20px_oklch(0.4_0.2_268/0.35)] ring-1 ring-tpg08-acc/15 transition delay-150 duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <div class="grid gap-4 border-b border-tpg08-acc/15 bg-linear-to-r from-tpg08-acc/10 to-tpg08-acc2/10 px-5 py-2.5 text-[11px] font-semibold sm:grid-cols-2 tracking-[0.12em] text-tpg08-mut uppercase">
        <p>Bootstrap 5<span class="sm:hidden"> &rarr; Tailwind v4</span></p><p class="max-sm:hidden">Tailwind v4</p>
      </div>
      <dl class="divide-y divide-tpg08-acc/12 font-tpg08-mono text-[12.5px] leading-relaxed">
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">.pagination</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">&lt;nav aria-label&gt; + flex</dd></div>
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">.page-item</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">not-first:-ms-px first:*:rounded-s-xl</dd></div>
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">.page-item.active</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">aria-[current=page]:bg-linear-to-b</dd></div>
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">.page-item.disabled</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">aria-disabled:pointer-events-none</dd></div>
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">.pagination-lg</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">sm:min-h-12 sm:px-4 sm:text-[15px]</dd></div>
        <div class="grid gap-x-4 gap-y-1 px-5 py-3 sm:grid-cols-2"><dt class="text-tpg08-acc-ink">--bs-pagination-active-bg</dt><dd class="text-tpg08-ink max-sm:before:text-tpg08-mut max-sm:before:content-['→_']">--color-tpg08-acc in @theme</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg08-bg: #f0f5ff;
  --color-tpg08-bg: oklch(0.97 0.015 265);
  --color-tpg08-glow: #ceddffb3;
  --color-tpg08-glow: oklch(0.9 0.06 270 / 0.7);
  --color-tpg08-card: #fcfdff;
  --color-tpg08-card: oklch(0.995 0.004 265);
  --color-tpg08-sunk: #ecf2fe;
  --color-tpg08-sunk: oklch(0.96 0.018 265);
  --color-tpg08-ink: #131e37;
  --color-tpg08-ink: oklch(0.24 0.05 265);
  --color-tpg08-mut: #535e75;
  --color-tpg08-mut: oklch(0.48 0.04 265);
  --color-tpg08-line: #cfd7ec;
  --color-tpg08-line: oklch(0.88 0.03 268);
  --color-tpg08-acc: #1b4ed8;
  --color-tpg08-acc: oklch(0.488 0.217 264);
  --color-tpg08-acc2: #4f39f6;
  --color-tpg08-acc2: oklch(0.511 0.262 277);
  --color-tpg08-acc-ink: #1745c2;
  --color-tpg08-acc-ink: oklch(0.45 0.2 264);
  --color-tpg08-on: #ffffff;
  --color-tpg08-on: oklch(1 0 0);
  --font-tpg08-sans: 'DM Sans', system-ui, sans-serif;
  --font-tpg08-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tpg08-card: 0 1px 2px oklch(0.3 0.1 265 / 0.08), 0 28px 56px -26px oklch(0.4 0.2 268 / 0.38);
}
/* Dark "navy": the same job [data-bs-theme="dark"] does in Bootstrap, as a token re-point.
   The gradient brightens and the digit turns deep navy, so it stays above 7:1. */

@media (prefers-color-scheme: dark) {
  .tpg-08:not([data-theme="light"]) {
    --color-tpg08-bg: #050c20;
    --color-tpg08-bg: oklch(0.16 0.045 265);
    --color-tpg08-glow: #18246980;
    --color-tpg08-glow: oklch(0.3 0.12 270 / 0.5);
    --color-tpg08-card: #0c162e;
    --color-tpg08-card: oklch(0.205 0.05 265);
    --color-tpg08-sunk: #131f3b;
    --color-tpg08-sunk: oklch(0.245 0.055 265);
    --color-tpg08-ink: #eaeff9;
    --color-tpg08-ink: oklch(0.95 0.015 265);
    --color-tpg08-mut: #abb8d2;
    --color-tpg08-mut: oklch(0.78 0.04 265);
    --color-tpg08-line: #263454;
    --color-tpg08-line: oklch(0.33 0.06 265);
    --color-tpg08-acc: #6ba4ff;
    --color-tpg08-acc: oklch(0.72 0.15 260);
    --color-tpg08-acc2: #9296ff;
    --color-tpg08-acc2: oklch(0.72 0.16 280);
    --color-tpg08-acc-ink: #94bfff;
    --color-tpg08-acc-ink: oklch(0.8 0.11 260);
    --color-tpg08-on: #050e25;
    --color-tpg08-on: oklch(0.17 0.05 265);
  }
}

.tpg-08[data-theme="dark"] {
  --color-tpg08-bg: #050c20;
  --color-tpg08-bg: oklch(0.16 0.045 265);
  --color-tpg08-glow: #18246980;
  --color-tpg08-glow: oklch(0.3 0.12 270 / 0.5);
  --color-tpg08-card: #0c162e;
  --color-tpg08-card: oklch(0.205 0.05 265);
  --color-tpg08-sunk: #131f3b;
  --color-tpg08-sunk: oklch(0.245 0.055 265);
  --color-tpg08-ink: #eaeff9;
  --color-tpg08-ink: oklch(0.95 0.015 265);
  --color-tpg08-mut: #abb8d2;
  --color-tpg08-mut: oklch(0.78 0.04 265);
  --color-tpg08-line: #263454;
  --color-tpg08-line: oklch(0.33 0.06 265);
  --color-tpg08-acc: #6ba4ff;
  --color-tpg08-acc: oklch(0.72 0.15 260);
  --color-tpg08-acc2: #9296ff;
  --color-tpg08-acc2: oklch(0.72 0.16 280);
  --color-tpg08-acc-ink: #94bfff;
  --color-tpg08-acc-ink: oklch(0.8 0.11 260);
  --color-tpg08-on: #050e25;
  --color-tpg08-on: oklch(0.17 0.05 265);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-08 {
  width: 100%;
  min-height: 100svh;
}
```
