---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/accessible-tailwind-pagination-with-aria-and-wcag-2-2-focus-states/"
title: "Accessible Tailwind Pagination with ARIA and WCAG 2.2 Focus States"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "The pagination to copy when accessibility is the requirement: a labelled <nav>, real links with real URLs, aria-current=\"page\" styled through…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tailwind Pagination with ARIA and WCAG 2.2 Focus States
Source: https://codefronts.com/navigation/tailwind-css-pagination/accessible-tailwind-pagination-with-aria-and-wcag-2-2-focus-states/

The pagination to copy when accessibility is the requirement: a labelled <nav>, real links with real URLs, aria-current="page" styled through aria-[current=page]:, a 3px focus-visible: outline that clears every neighbour, a non-colour bar under the current page and a forced-colors: fallback for Windows High Contrast. A small script turns it into a client-side pager that moves focus to the results heading after each page change &mdash; the step most pagers skip.
## HTML
```html
<section class="tpg-09 w-full min-h-svh grid place-items-center bg-tpg09-bg bg-[radial-gradient(55%_45%_at_80%_10%,var(--color-tpg09-glow),transparent_70%),radial-gradient(70%_60%_at_15%_90%,var(--color-tpg09-glow2),transparent_70%)] px-5 py-14 font-tpg09-sans text-tpg09-ink antialiased" aria-label="Accessible pagination with ARIA and WCAG 2.2 focus states demo">
  <div id="tpg-09-search" class="grid w-full max-w-[42rem] gap-6">
    <div class="rounded-2xl bg-tpg09-card shadow-tpg09-card ring-1 ring-tpg09-acc/15 transition duration-700 ease-[cubic-bezier(.16,1,.3,1)] starting:translate-y-3 starting:opacity-0 motion-reduce:transition-none">
      <header class="border-b border-tpg09-line px-5 pt-5 pb-4 sm:px-7">
        <p class="text-[13px] text-tpg09-mut">Search results for <b class="font-semibold text-tpg09-ink">“pagination”</b></p>
        <h2 id="tpg-09-heading" data-heading tabindex="-1" class="mt-1.5 scroll-mt-6 rounded-md text-[19px] font-bold tracking-[-0.01em] tabular-nums focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-tpg09-ring">Page 5 of 12, results 13–15</h2>
      </header>

      <ol data-results start="13" aria-labelledby="tpg-09-heading" class="divide-y divide-tpg09-line px-5 sm:px-7">
        <li class="grid grid-cols-1 gap-1 py-4"><h3 data-title class="text-[16px] font-semibold text-tpg09-ink">Target size: why 24px is the WCAG 2.2 floor</h3><p data-meta class="truncate font-tpg09-mono text-[12.5px] text-tpg09-mut">a11y.guide/target-size · 6 min read</p></li>
        <li class="grid grid-cols-1 gap-1 py-4"><h3 data-title class="text-[16px] font-semibold text-tpg09-ink">Focus management after client-side navigation</h3><p data-meta class="truncate font-tpg09-mono text-[12.5px] text-tpg09-mut">a11y.guide/focus-management · 8 min read</p></li>
        <li class="grid grid-cols-1 gap-1 py-4"><h3 data-title class="text-[16px] font-semibold text-tpg09-ink">Forced colors: testing in Windows High Contrast</h3><p data-meta class="truncate font-tpg09-mono text-[12.5px] text-tpg09-mut">a11y.guide/forced-colors · 5 min read</p></li>
      </ol>

      <nav aria-label="Search results pagination" class="border-t border-tpg09-line px-3 py-4 sm:px-7">
        <ol class="flex items-center justify-center gap-1.5 sm:justify-between">
          <li class="sm:me-auto"><a data-prev href="?q=pagination&amp;page=4" rel="prev" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 rounded-lg px-3 text-[15px] font-semibold text-tpg09-ink ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow] duration-200 hover:bg-tpg09-acc/8 hover:text-tpg09-acc-ink hover:ring-tpg09-acc-ink focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-disabled:cursor-not-allowed aria-disabled:text-tpg09-mut aria-disabled:ring-tpg09-line aria-disabled:hover:bg-transparent motion-reduce:transition-none"><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 5L7.5 10l5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="max-sm:sr-only">Previous<span class="sr-only"> page</span></span></a></li>
          <li data-far class="max-sm:hidden"><a data-page href="?q=pagination&amp;page=1" aria-label="Page 1" class="relative inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg px-2 text-[15px] font-semibold text-tpg09-ink tabular-nums ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow,translate] duration-200 not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg09-acc/8 not-aria-[current=page]:hover:text-tpg09-acc-ink not-aria-[current=page]:hover:ring-tpg09-acc-ink motion-reduce:hover:translate-y-0 after:absolute after:inset-x-3 after:-bottom-2 after:h-[3px] after:rounded-full focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg09-acc aria-[current=page]:to-tpg09-acc2 aria-[current=page]:text-tpg09-on aria-[current=page]:ring-tpg09-acc2 aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.22),0_8px_20px_-8px_var(--color-tpg09-acc)] aria-[current=page]:after:bg-tpg09-gold aria-[current=page]:after:shadow-[0_0_10px_var(--color-tpg09-gold)] forced-colors:aria-[current=page]:bg-none forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none">1</a></li>
          <li data-far data-gap="l" aria-hidden="true" class="grid min-h-11 min-w-6 max-sm:hidden place-items-center font-bold tracking-widest text-tpg09-gold-ink">…</li>
          <li><a data-page href="?q=pagination&amp;page=4" aria-label="Page 4" class="relative inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg px-2 text-[15px] font-semibold text-tpg09-ink tabular-nums ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow,translate] duration-200 not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg09-acc/8 not-aria-[current=page]:hover:text-tpg09-acc-ink not-aria-[current=page]:hover:ring-tpg09-acc-ink motion-reduce:hover:translate-y-0 after:absolute after:inset-x-3 after:-bottom-2 after:h-[3px] after:rounded-full focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg09-acc aria-[current=page]:to-tpg09-acc2 aria-[current=page]:text-tpg09-on aria-[current=page]:ring-tpg09-acc2 aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.22),0_8px_20px_-8px_var(--color-tpg09-acc)] aria-[current=page]:after:bg-tpg09-gold aria-[current=page]:after:shadow-[0_0_10px_var(--color-tpg09-gold)] forced-colors:aria-[current=page]:bg-none forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none">4</a></li>
          <li><a data-page href="?q=pagination&amp;page=5" aria-label="Page 5" aria-current="page" class="relative inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg px-2 text-[15px] font-semibold text-tpg09-ink tabular-nums ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow,translate] duration-200 not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg09-acc/8 not-aria-[current=page]:hover:text-tpg09-acc-ink not-aria-[current=page]:hover:ring-tpg09-acc-ink motion-reduce:hover:translate-y-0 after:absolute after:inset-x-3 after:-bottom-2 after:h-[3px] after:rounded-full focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg09-acc aria-[current=page]:to-tpg09-acc2 aria-[current=page]:text-tpg09-on aria-[current=page]:ring-tpg09-acc2 aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.22),0_8px_20px_-8px_var(--color-tpg09-acc)] aria-[current=page]:after:bg-tpg09-gold aria-[current=page]:after:shadow-[0_0_10px_var(--color-tpg09-gold)] forced-colors:aria-[current=page]:bg-none forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none">5</a></li>
          <li><a data-page href="?q=pagination&amp;page=6" aria-label="Page 6" class="relative inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg px-2 text-[15px] font-semibold text-tpg09-ink tabular-nums ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow,translate] duration-200 not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg09-acc/8 not-aria-[current=page]:hover:text-tpg09-acc-ink not-aria-[current=page]:hover:ring-tpg09-acc-ink motion-reduce:hover:translate-y-0 after:absolute after:inset-x-3 after:-bottom-2 after:h-[3px] after:rounded-full focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg09-acc aria-[current=page]:to-tpg09-acc2 aria-[current=page]:text-tpg09-on aria-[current=page]:ring-tpg09-acc2 aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.22),0_8px_20px_-8px_var(--color-tpg09-acc)] aria-[current=page]:after:bg-tpg09-gold aria-[current=page]:after:shadow-[0_0_10px_var(--color-tpg09-gold)] forced-colors:aria-[current=page]:bg-none forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none">6</a></li>
          <li data-far data-gap="r" aria-hidden="true" class="grid min-h-11 min-w-6 max-sm:hidden place-items-center font-bold tracking-widest text-tpg09-gold-ink">…</li>
          <li data-far class="max-sm:hidden"><a data-page href="?q=pagination&amp;page=12" aria-label="Page 12" class="relative inline-flex min-h-11 min-w-11 items-center justify-center rounded-lg px-2 text-[15px] font-semibold text-tpg09-ink tabular-nums ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow,translate] duration-200 not-aria-[current=page]:hover:-translate-y-px not-aria-[current=page]:hover:bg-tpg09-acc/8 not-aria-[current=page]:hover:text-tpg09-acc-ink not-aria-[current=page]:hover:ring-tpg09-acc-ink motion-reduce:hover:translate-y-0 after:absolute after:inset-x-3 after:-bottom-2 after:h-[3px] after:rounded-full focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-[current=page]:bg-linear-to-b aria-[current=page]:from-tpg09-acc aria-[current=page]:to-tpg09-acc2 aria-[current=page]:text-tpg09-on aria-[current=page]:ring-tpg09-acc2 aria-[current=page]:shadow-[inset_0_1px_0_oklch(1_0_0/0.22),0_8px_20px_-8px_var(--color-tpg09-acc)] aria-[current=page]:after:bg-tpg09-gold aria-[current=page]:after:shadow-[0_0_10px_var(--color-tpg09-gold)] forced-colors:aria-[current=page]:bg-none forced-colors:aria-[current=page]:bg-[Highlight] forced-colors:aria-[current=page]:text-[HighlightText] forced-colors:aria-[current=page]:forced-color-adjust-none motion-reduce:transition-none">12</a></li>
          <li class="sm:ms-auto"><a data-next href="?q=pagination&amp;page=6" rel="next" class="relative inline-flex min-h-11 min-w-11 items-center justify-center gap-1.5 rounded-lg px-3 text-[15px] font-semibold text-tpg09-ink ring-1 ring-tpg09-ctl transition-[background-color,color,box-shadow] duration-200 hover:bg-tpg09-acc/8 hover:text-tpg09-acc-ink hover:ring-tpg09-acc-ink focus-visible:z-10 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpg09-ring aria-disabled:cursor-not-allowed aria-disabled:text-tpg09-mut aria-disabled:ring-tpg09-line aria-disabled:hover:bg-transparent motion-reduce:transition-none"><span class="max-sm:sr-only">Next<span class="sr-only"> page</span></span><svg class="size-4" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a></li>
        </ol>
      </nav>
    </div>

    <ul class="flex flex-wrap justify-center gap-2 font-tpg09-mono text-[12px] text-tpg09-mut" aria-label="WCAG 2.2 success criteria covered">
      <li class="rounded-full bg-tpg09-card px-3 py-1.5 ring-1 ring-tpg09-acc/15"><b class="font-semibold text-tpg09-gold-ink">2.4.7</b> Focus Visible</li>
      <li class="rounded-full bg-tpg09-card px-3 py-1.5 ring-1 ring-tpg09-acc/15"><b class="font-semibold text-tpg09-gold-ink">2.4.11</b> Focus Not Obscured</li>
      <li class="rounded-full bg-tpg09-card px-3 py-1.5 ring-1 ring-tpg09-acc/15"><b class="font-semibold text-tpg09-gold-ink">2.5.8</b> Target Size</li>
      <li class="rounded-full bg-tpg09-card px-3 py-1.5 ring-1 ring-tpg09-acc/15"><b class="font-semibold text-tpg09-gold-ink">1.4.11</b> Non-text Contrast</li>
      <li class="rounded-full bg-tpg09-card px-3 py-1.5 ring-1 ring-tpg09-acc/15"><b class="font-semibold text-tpg09-gold-ink">2.5.3</b> Label in Name</li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg09-bg: #f1f7ff;
  --color-tpg09-bg: oklch(0.975 0.012 255);
  --color-tpg09-glow: #f7e7bb99;
  --color-tpg09-glow: oklch(0.93 0.06 90 / 0.6);
  --color-tpg09-glow2: #cbdfff99;
  --color-tpg09-glow2: oklch(0.9 0.05 260 / 0.6);
  --color-tpg09-card: #fdfeff;
  --color-tpg09-card: oklch(0.997 0.003 255);
  --color-tpg09-sunk: #edf4fd;
  --color-tpg09-sunk: oklch(0.965 0.014 255);
  --color-tpg09-ink: #0f1932;
  --color-tpg09-ink: oklch(0.22 0.05 265);
  --color-tpg09-mut: #4a556c;
  --color-tpg09-mut: oklch(0.45 0.04 265);
  --color-tpg09-line: #d3dbe8;
  --color-tpg09-line: oklch(0.89 0.02 260);
  --color-tpg09-ctl: #697a9f;
  --color-tpg09-ctl: oklch(0.58 0.06 265);
  --color-tpg09-acc: #1d40af;
  --color-tpg09-acc: oklch(0.424 0.181 265.5);
  --color-tpg09-acc2: #1b2f8f;
  --color-tpg09-acc2: oklch(0.36 0.16 268);
  --color-tpg09-acc-ink: #1d40af;
  --color-tpg09-acc-ink: oklch(0.424 0.181 265.5);
  --color-tpg09-on: #ffffff;
  --color-tpg09-on: oklch(1 0 0);
  --color-tpg09-gold: #ad7300;
  --color-tpg09-gold: oklch(0.6 0.13 75);
  --color-tpg09-gold-ink: #986603;
  --color-tpg09-gold-ink: oklch(0.55 0.115 75);
  --color-tpg09-ring: #ad7300;
  --color-tpg09-ring: oklch(0.6 0.13 75);
  --font-tpg09-sans: 'Atkinson Hyperlegible Next', system-ui, sans-serif;
  --font-tpg09-mono: 'Atkinson Hyperlegible Mono', ui-monospace, monospace;
  --shadow-tpg09-card: 0 1px 2px oklch(0.3 0.1 265 / 0.08), 0 26px 54px -26px oklch(0.35 0.16 265 / 0.38);
}
/* Dark "navy with gold": every token re-pointed. The sapphire key lightens so white digits still
   clear 5.7:1, and the gold focus ring sits at 11.5:1 against the card. */

@media (prefers-color-scheme: dark) {
  .tpg-09:not([data-theme="light"]) {
    --color-tpg09-bg: #050e25;
    --color-tpg09-bg: oklch(0.17 0.05 265);
    --color-tpg09-glow: #facc161f;
    --color-tpg09-glow: oklch(0.861 0.173 92 / 0.12);
    --color-tpg09-glow2: #2e5bda40;
    --color-tpg09-glow2: oklch(0.52 0.2 265 / 0.25);
    --color-tpg09-card: #0d1833;
    --color-tpg09-card: oklch(0.215 0.055 265);
    --color-tpg09-sunk: #142140;
    --color-tpg09-sunk: oklch(0.255 0.06 265);
    --color-tpg09-ink: #eef2f9;
    --color-tpg09-ink: oklch(0.96 0.01 265);
    --color-tpg09-mut: #b4bed2;
    --color-tpg09-mut: oklch(0.8 0.03 265);
    --color-tpg09-line: #2b3a5a;
    --color-tpg09-line: oklch(0.35 0.06 265);
    --color-tpg09-ctl: #7486ab;
    --color-tpg09-ctl: oklch(0.62 0.06 265);
    --color-tpg09-acc: #2e5bda;
    --color-tpg09-acc: oklch(0.52 0.2 265);
    --color-tpg09-acc2: #2841b9;
    --color-tpg09-acc2: oklch(0.44 0.19 268);
    --color-tpg09-acc-ink: #8dc1ff;
    --color-tpg09-acc-ink: oklch(0.8 0.11 255);
    --color-tpg09-on: #ffffff;
    --color-tpg09-on: oklch(1 0 0);
    --color-tpg09-gold: #facc16;
    --color-tpg09-gold: oklch(0.861 0.173 92);
    --color-tpg09-gold-ink: #facc16;
    --color-tpg09-gold-ink: oklch(0.861 0.173 92);
    --color-tpg09-ring: #facc16;
    --color-tpg09-ring: oklch(0.861 0.173 92);
  }
}

.tpg-09[data-theme="dark"] {
  --color-tpg09-bg: #050e25;
  --color-tpg09-bg: oklch(0.17 0.05 265);
  --color-tpg09-glow: #facc161f;
  --color-tpg09-glow: oklch(0.861 0.173 92 / 0.12);
  --color-tpg09-glow2: #2e5bda40;
  --color-tpg09-glow2: oklch(0.52 0.2 265 / 0.25);
  --color-tpg09-card: #0d1833;
  --color-tpg09-card: oklch(0.215 0.055 265);
  --color-tpg09-sunk: #142140;
  --color-tpg09-sunk: oklch(0.255 0.06 265);
  --color-tpg09-ink: #eef2f9;
  --color-tpg09-ink: oklch(0.96 0.01 265);
  --color-tpg09-mut: #b4bed2;
  --color-tpg09-mut: oklch(0.8 0.03 265);
  --color-tpg09-line: #2b3a5a;
  --color-tpg09-line: oklch(0.35 0.06 265);
  --color-tpg09-ctl: #7486ab;
  --color-tpg09-ctl: oklch(0.62 0.06 265);
  --color-tpg09-acc: #2e5bda;
  --color-tpg09-acc: oklch(0.52 0.2 265);
  --color-tpg09-acc2: #2841b9;
  --color-tpg09-acc2: oklch(0.44 0.19 268);
  --color-tpg09-acc-ink: #8dc1ff;
  --color-tpg09-acc-ink: oklch(0.8 0.11 255);
  --color-tpg09-on: #ffffff;
  --color-tpg09-on: oklch(1 0 0);
  --color-tpg09-gold: #facc16;
  --color-tpg09-gold: oklch(0.861 0.173 92);
  --color-tpg09-gold-ink: #facc16;
  --color-tpg09-gold-ink: oklch(0.861 0.173 92);
  --color-tpg09-ring: #facc16;
  --color-tpg09-ring: oklch(0.861 0.173 92);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-09 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tpg-09-search');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const N = 12, PER = 3, TOTAL = 36;
  const titles = ['Designing pagination for screen reader users', 'When infinite scroll beats numbered pages', 'aria-current: one attribute, many states', 'Target size: why 24px is the WCAG 2.2 floor', 'Focus management after client-side navigation', 'Forced colors: testing in Windows High Contrast', 'Accessible names that match visible labels'];
  const heading = root.querySelector('[data-heading]'), list = root.querySelector('[data-results]');
  const links = [...root.querySelectorAll('[data-page]')];
  const gaps = root.querySelectorAll('[data-gap]');
  const prev = root.querySelector('[data-prev]'), next = root.querySelector('[data-next]');
  const url = (n) => '?q=pagination&page=' + n;
  const edge = (a, n, off) => {
    if (off) { a.removeAttribute('href'); a.setAttribute('aria-disabled', 'true'); }
    else { a.href = url(n); a.removeAttribute('aria-disabled'); }
  };
  const render = (p) => {
    const s = Math.min(Math.max(p - 1, 1), N - 2);
    [1, s, s + 1, s + 2, N].forEach((n, k) => {
      const a = links[k];
      a.textContent = n; a.href = url(n); a.setAttribute('aria-label', 'Page ' + n);
      if (n === p) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    links[0].parentElement.hidden = s === 1;
    links[4].parentElement.hidden = s + 2 === N;
    gaps[0].hidden = s <= 2;
    gaps[1].hidden = s + 2 >= N - 1;
    edge(prev, p - 1, p === 1);
    edge(next, p + 1, p === N);
    const from = (p - 1) * PER + 1;
    list.start = from;
    [...list.children].forEach((li, k) => {
      const t = titles[(from + k) % titles.length];
      li.querySelector('[data-title]').textContent = t;
      li.querySelector('[data-meta]').textContent = 'a11y.guide/' + t.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') + ' · ' + (4 + (from + k) % 6) + ' min read';
    });
    heading.textContent = 'Page ' + p + ' of ' + N + ', results ' + from + '–' + (from + PER - 1);
    root.dataset.page = p;
  };
  root.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a || !root.contains(a)) return;
    e.preventDefault();
    render(Number(new URL(a.href, location.href).searchParams.get('page')));
    heading.focus();
  });
  render(5);
})();
```
