---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-blog-pagination-with-newer-and-older-post-links/"
title: "Tailwind Blog Pagination with Newer and Older Post Links"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "Archive pagination is read before it is clicked, so the directional links carry the destination page's headline under a Newer / Older label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Blog Pagination with Newer and Older Post Links
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-blog-pagination-with-newer-and-older-post-links/

Archive pagination is read before it is clicked, so the directional links carry the destination page's headline under a Newer / Older label. An grid-cols-[1fr_auto_1fr] track pins the page numbers to the true centre however long those headlines run, post titles get a baseline-safe burgundy-to-rose-gold underline from bg-[length:0%_2px], the current page is a burgundy wax seal with a rose-gold inner ring,, and the bar re-stacks by its own width with @max-[40rem]:.
## HTML
```html
<section class="tpg-12 w-full min-h-svh grid place-items-center bg-tpg12-bg bg-[radial-gradient(55%_40%_at_90%_0%,var(--color-tpg12-glow),transparent_70%),radial-gradient(45%_35%_at_0%_100%,var(--color-tpg12-glow2),transparent_70%)] px-5 py-14 font-tpg12-sans text-tpg12-ink antialiased" aria-label="Blog pagination with newer and older post links demo">
  <div class="grid w-full max-w-[46rem] justify-items-center gap-8">
    <div class="grid w-full gap-7">
      <header class="grid gap-2">
        <p class="text-xs font-medium tracking-[0.14em] uppercase text-tpg12-acc tabular-nums">Archive &middot; Page 3 of 12</p>
        <h2 class="font-tpg12-serif text-[clamp(2.1rem,5vw,2.9rem)] leading-[1.05] font-medium tracking-[-0.02em]">Writing</h2>
        <p class="max-w-[34rem] text-[15px] leading-relaxed text-tpg12-mut text-pretty">Essays on CSS, performance and the slow craft of interfaces &mdash; roughly one a fortnight.</p>
      </header>

      <ol class="grid divide-y divide-tpg12-line border-y border-tpg12-line" role="list">
        <li class="grid gap-1.5 py-5">
          <p class="flex flex-wrap items-center gap-x-2.5 gap-y-1 text-[13px] text-tpg12-mut tabular-nums"><time datetime="2026-05-14">14 May 2026</time><span aria-hidden="true">&middot;</span><span class="rounded-full bg-tpg12-acc/8 px-2 py-0.5 text-xs font-medium text-tpg12-acc ring-1 ring-tpg12-rg/45">Layout</span><span aria-hidden="true">&middot;</span><span>7 min read</span></p>
          <h3 class="font-tpg12-serif text-[clamp(1.3rem,2.6vw,1.55rem)] leading-snug font-medium tracking-[-0.01em] text-balance"><a href="#tpg-12-container-queries" class="rounded-sm bg-[linear-gradient(90deg,var(--color-tpg12-acc),var(--color-tpg12-rg))] bg-[length:0%_2px] bg-[position:0_100%] bg-no-repeat transition-[background-size,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-[length:100%_2px] hover:text-tpg12-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg12-ring motion-reduce:transition-none">Getting Started with Container Queries</a></h3>
          <p class="max-w-[38rem] text-[15px] leading-[1.65] text-tpg12-mut text-pretty">Why component-level breakpoints replace the global ones you have been maintaining, and how to migrate a card grid in an afternoon.</p>
        </li>
        <li class="grid gap-1.5 py-5">
          <p class="flex flex-wrap items-center gap-x-2.5 gap-y-1 text-[13px] text-tpg12-mut tabular-nums"><time datetime="2026-05-02">2 May 2026</time><span aria-hidden="true">&middot;</span><span class="rounded-full bg-tpg12-acc/8 px-2 py-0.5 text-xs font-medium text-tpg12-acc ring-1 ring-tpg12-rg/45">Performance</span><span aria-hidden="true">&middot;</span><span>11 min read</span></p>
          <h3 class="font-tpg12-serif text-[clamp(1.3rem,2.6vw,1.55rem)] leading-snug font-medium tracking-[-0.01em] text-balance"><a href="#tpg-12-layout-library" class="rounded-sm bg-[linear-gradient(90deg,var(--color-tpg12-acc),var(--color-tpg12-rg))] bg-[length:0%_2px] bg-[position:0_100%] bg-no-repeat transition-[background-size,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-[length:100%_2px] hover:text-tpg12-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg12-ring motion-reduce:transition-none">The Real Cost of a Layout Library</a></h3>
          <p class="max-w-[38rem] text-[15px] leading-[1.65] text-tpg12-mut text-pretty">We measured four grid abstractions against plain CSS grid on a mid-range Android phone. The gap was larger than any of us expected.</p>
        </li>
        <li class="grid gap-1.5 py-5">
          <p class="flex flex-wrap items-center gap-x-2.5 gap-y-1 text-[13px] text-tpg12-mut tabular-nums"><time datetime="2026-04-27">27 Apr 2026</time><span aria-hidden="true">&middot;</span><span class="rounded-full bg-tpg12-acc/8 px-2 py-0.5 text-xs font-medium text-tpg12-acc ring-1 ring-tpg12-rg/45">Accessibility</span><span aria-hidden="true">&middot;</span><span>5 min read</span></p>
          <h3 class="font-tpg12-serif text-[clamp(1.3rem,2.6vw,1.55rem)] leading-snug font-medium tracking-[-0.01em] text-balance"><a href="#tpg-12-focus-order" class="rounded-sm bg-[linear-gradient(90deg,var(--color-tpg12-acc),var(--color-tpg12-rg))] bg-[length:0%_2px] bg-[position:0_100%] bg-no-repeat transition-[background-size,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-[length:100%_2px] hover:text-tpg12-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg12-ring motion-reduce:transition-none">Focus Order Is a Design Decision</a></h3>
          <p class="max-w-[38rem] text-[15px] leading-[1.65] text-tpg12-mut text-pretty">Tab order is not a developer detail. It is reading order, and it belongs in the wireframe next to the visual hierarchy.</p>
        </li>
      </ol>

      <nav class="@container scroll-mt-8" id="tpg-12-archive" aria-label="Pagination">
        <div class="grid grid-cols-[1fr_auto_1fr] items-center gap-4 @max-[40rem]:grid-cols-2 @max-[40rem]:gap-3">
          <a href="#tpg-12-p2" rel="prev" class="group grid min-h-11 content-center gap-1 rounded-2xl p-3.5 ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-tpg12-card hover:shadow-tpg12-card hover:ring-tpg12-rg/55 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring motion-reduce:transition-none">
            <span class="flex items-center gap-1.5 text-xs font-medium tracking-[0.06em] uppercase text-tpg12-mut"><svg class="text-tpg12-rg-ink transition-transform duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover:-translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M13 8H3.5M7.5 3.5 3 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Newer posts</span>
            <span class="line-clamp-2 font-tpg12-serif text-[17px] leading-snug text-pretty">Shipping Web Fonts Without the Flash</span>
          </a>
          <ol class="flex items-center justify-center gap-1 @max-[40rem]:order-first @max-[40rem]:col-span-2" role="list">
            <li><a href="#tpg-12-p1" aria-label="Page 1" class="grid min-h-11 min-w-11 place-items-center rounded-full text-sm font-medium tabular-nums text-tpg12-ink transition-[background-color,color,box-shadow] duration-200 not-aria-[current=page]:hover:bg-tpg12-rg/20 not-aria-[current=page]:hover:text-tpg12-acc not-aria-[current=page]:hover:shadow-tpg12-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring aria-[current=page]:bg-[radial-gradient(circle_at_32%_26%,var(--color-tpg12-seal-hi),var(--color-tpg12-seal)_58%,var(--color-tpg12-seal-lo))] aria-[current=page]:font-semibold aria-[current=page]:text-tpg12-on-seal aria-[current=page]:shadow-tpg12-seal">1</a></li>
            <li aria-hidden="true" class="w-4 text-center text-sm font-semibold text-tpg12-rg-ink">&hellip;</li>
            <li><a href="#tpg-12-p2" aria-label="Page 2" class="grid min-h-11 min-w-11 place-items-center rounded-full text-sm font-medium tabular-nums text-tpg12-ink transition-[background-color,color,box-shadow] duration-200 not-aria-[current=page]:hover:bg-tpg12-rg/20 not-aria-[current=page]:hover:text-tpg12-acc not-aria-[current=page]:hover:shadow-tpg12-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring aria-[current=page]:bg-[radial-gradient(circle_at_32%_26%,var(--color-tpg12-seal-hi),var(--color-tpg12-seal)_58%,var(--color-tpg12-seal-lo))] aria-[current=page]:font-semibold aria-[current=page]:text-tpg12-on-seal aria-[current=page]:shadow-tpg12-seal">2</a></li>
            <li><a href="#tpg-12-p3" aria-current="page" aria-label="Page 3, current page" class="grid min-h-11 min-w-11 place-items-center rounded-full text-sm font-medium tabular-nums text-tpg12-ink transition-[background-color,color,box-shadow] duration-200 not-aria-[current=page]:hover:bg-tpg12-rg/20 not-aria-[current=page]:hover:text-tpg12-acc not-aria-[current=page]:hover:shadow-tpg12-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring aria-[current=page]:bg-[radial-gradient(circle_at_32%_26%,var(--color-tpg12-seal-hi),var(--color-tpg12-seal)_58%,var(--color-tpg12-seal-lo))] aria-[current=page]:font-semibold aria-[current=page]:text-tpg12-on-seal aria-[current=page]:shadow-tpg12-seal">3</a></li>
            <li><a href="#tpg-12-p4" aria-label="Page 4" class="grid min-h-11 min-w-11 place-items-center rounded-full text-sm font-medium tabular-nums text-tpg12-ink transition-[background-color,color,box-shadow] duration-200 not-aria-[current=page]:hover:bg-tpg12-rg/20 not-aria-[current=page]:hover:text-tpg12-acc not-aria-[current=page]:hover:shadow-tpg12-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring aria-[current=page]:bg-[radial-gradient(circle_at_32%_26%,var(--color-tpg12-seal-hi),var(--color-tpg12-seal)_58%,var(--color-tpg12-seal-lo))] aria-[current=page]:font-semibold aria-[current=page]:text-tpg12-on-seal aria-[current=page]:shadow-tpg12-seal">4</a></li>
            <li aria-hidden="true" class="w-4 text-center text-sm font-semibold text-tpg12-rg-ink">&hellip;</li>
            <li><a href="#tpg-12-p12" aria-label="Page 12, oldest posts" class="grid min-h-11 min-w-11 place-items-center rounded-full text-sm font-medium tabular-nums text-tpg12-ink transition-[background-color,color,box-shadow] duration-200 not-aria-[current=page]:hover:bg-tpg12-rg/20 not-aria-[current=page]:hover:text-tpg12-acc not-aria-[current=page]:hover:shadow-tpg12-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring aria-[current=page]:bg-[radial-gradient(circle_at_32%_26%,var(--color-tpg12-seal-hi),var(--color-tpg12-seal)_58%,var(--color-tpg12-seal-lo))] aria-[current=page]:font-semibold aria-[current=page]:text-tpg12-on-seal aria-[current=page]:shadow-tpg12-seal">12</a></li>
          </ol>
          <a href="#tpg-12-p4" rel="next" class="group grid min-h-11 content-center justify-items-end gap-1 rounded-2xl p-3.5 text-right ring-1 ring-transparent transition-[background-color,box-shadow] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-tpg12-card hover:shadow-tpg12-card hover:ring-tpg12-rg/55 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg12-ring motion-reduce:transition-none">
            <span class="flex items-center gap-1.5 text-xs font-medium tracking-[0.06em] uppercase text-tpg12-mut">Older posts<svg class="text-tpg12-rg-ink transition-transform duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M3 8h9.5M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <span class="line-clamp-2 font-tpg12-serif text-[17px] leading-snug text-pretty">A Budget for Third-Party Scripts</span>
          </a>
        </div>
      </nav>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tpg12-card px-3.5 py-2 font-tpg12-mono text-[11.5px] text-tpg12-mut ring-1 ring-tpg12-line">grid-cols-[1fr_auto_1fr] · @max-[40rem]: · rel=prev / next</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg12-bg: #fbf5ef;
  --color-tpg12-bg: oklch(0.973 0.010 68);
  --color-tpg12-glow: #f2d2b8b3;
  --color-tpg12-glow: oklch(0.884 0.050 61 / 0.70);
  --color-tpg12-glow2: #f3d6dc99;
  --color-tpg12-glow2: oklch(0.902 0.033 4 / 0.60);
  --color-tpg12-card: #fffbf7;
  --color-tpg12-card: oklch(0.990 0.007 68);
  --color-tpg12-ink: #2a1418;
  --color-tpg12-ink: oklch(0.224 0.036 9);
  --color-tpg12-mut: #6e4a4c;
  --color-tpg12-mut: oklch(0.450 0.049 16);
  --color-tpg12-line: #ecdcd0;
  --color-tpg12-line: oklch(0.904 0.024 59);
  --color-tpg12-acc: #9f1239;
  --color-tpg12-acc: oklch(0.455 0.171 14);
  --color-tpg12-rg: #d4a373;
  --color-tpg12-rg: oklch(0.750 0.086 65);
  --color-tpg12-rg-ink: #a0683c;
  --color-tpg12-rg-ink: oklch(0.568 0.093 58);
  --color-tpg12-seal: #9f1239;
  --color-tpg12-seal: oklch(0.455 0.171 14);
  --color-tpg12-seal-hi: #be123c;
  --color-tpg12-seal-hi: oklch(0.514 0.198 17);
  --color-tpg12-seal-lo: #6b0f2a;
  --color-tpg12-seal-lo: oklch(0.347 0.125 11);
  --color-tpg12-on-seal: #fff7f0;
  --color-tpg12-on-seal: oklch(0.980 0.013 64);
  --color-tpg12-ring: #9f1239;
  --color-tpg12-ring: oklch(0.455 0.171 14);
  --font-tpg12-serif: 'Newsreader', Georgia, serif;
  --font-tpg12-sans: 'DM Sans', system-ui, sans-serif;
  --font-tpg12-mono: 'DM Mono', ui-monospace, monospace;
  --shadow-tpg12-card: 0 1px 2px oklch(0.4 0.1 20 / 0.06), 0 12px 28px -12px oklch(0.45 0.14 15 / 0.22);
  --shadow-tpg12-hover: inset 0 0 0 1px oklch(0.75 0.08 65 / 0.55);
  --shadow-tpg12-seal: inset 0 0 0 2px oklch(0.42 0.16 12), inset 0 0 0 3.5px oklch(0.77 0.08 65 / 0.95), 0 2px 4px oklch(0.35 0.12 12 / 0.3), 0 10px 22px -8px oklch(0.45 0.17 12 / 0.6);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-12 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme: wine night — the seal flips to rose gold with deep wine ink; same tokens, re-pointed. */

@media (prefers-color-scheme: dark) {
  .tpg-12:not([data-theme="light"]) {
    --color-tpg12-bg: #170b0f;
    --color-tpg12-bg: oklch(0.169 0.022 358);
    --color-tpg12-glow: #5a1a2a99;
    --color-tpg12-glow: oklch(0.326 0.094 9 / 0.60);
    --color-tpg12-glow2: #4a2a1a80;
    --color-tpg12-glow2: oklch(0.322 0.055 47 / 0.50);
    --color-tpg12-card: #22121a;
    --color-tpg12-card: oklch(0.208 0.030 349);
    --color-tpg12-ink: #f7e9e4;
    --color-tpg12-ink: oklch(0.944 0.017 41);
    --color-tpg12-mut: #c9a9ab;
    --color-tpg12-mut: oklch(0.764 0.038 14);
    --color-tpg12-line: #3a2029;
    --color-tpg12-line: oklch(0.281 0.042 358);
    --color-tpg12-acc: #fda4af;
    --color-tpg12-acc: oklch(0.810 0.106 12);
    --color-tpg12-rg: #d4a373;
    --color-tpg12-rg: oklch(0.750 0.086 65);
    --color-tpg12-rg-ink: #e0b48a;
    --color-tpg12-rg-ink: oklch(0.799 0.076 65);
    --color-tpg12-seal: #d4a373;
    --color-tpg12-seal: oklch(0.750 0.086 65);
    --color-tpg12-seal-hi: #f3d3b4;
    --color-tpg12-seal-hi: oklch(0.886 0.055 66);
    --color-tpg12-seal-lo: #b8865a;
    --color-tpg12-seal-lo: oklch(0.659 0.086 62);
    --color-tpg12-on-seal: #2a0d14;
    --color-tpg12-on-seal: oklch(0.209 0.049 7);
    --color-tpg12-ring: #e6b88f;
    --color-tpg12-ring: oklch(0.814 0.076 63);
    --shadow-tpg12-card: 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 14px 30px -14px oklch(0 0 0 / 0.75);
    --shadow-tpg12-hover: inset 0 0 0 1px oklch(0.77 0.08 65 / 0.5);
    --shadow-tpg12-seal: inset 0 0 0 2px oklch(0.77 0.08 65), inset 0 0 0 3.5px oklch(0.25 0.06 10 / 0.9), 0 0 0 1px oklch(0.77 0.08 65 / 0.5), 0 10px 26px -8px oklch(0.77 0.08 65 / 0.5);
  }
}

.tpg-12[data-theme="dark"] {
  --color-tpg12-bg: #170b0f;
  --color-tpg12-bg: oklch(0.169 0.022 358);
  --color-tpg12-glow: #5a1a2a99;
  --color-tpg12-glow: oklch(0.326 0.094 9 / 0.60);
  --color-tpg12-glow2: #4a2a1a80;
  --color-tpg12-glow2: oklch(0.322 0.055 47 / 0.50);
  --color-tpg12-card: #22121a;
  --color-tpg12-card: oklch(0.208 0.030 349);
  --color-tpg12-ink: #f7e9e4;
  --color-tpg12-ink: oklch(0.944 0.017 41);
  --color-tpg12-mut: #c9a9ab;
  --color-tpg12-mut: oklch(0.764 0.038 14);
  --color-tpg12-line: #3a2029;
  --color-tpg12-line: oklch(0.281 0.042 358);
  --color-tpg12-acc: #fda4af;
  --color-tpg12-acc: oklch(0.810 0.106 12);
  --color-tpg12-rg: #d4a373;
  --color-tpg12-rg: oklch(0.750 0.086 65);
  --color-tpg12-rg-ink: #e0b48a;
  --color-tpg12-rg-ink: oklch(0.799 0.076 65);
  --color-tpg12-seal: #d4a373;
  --color-tpg12-seal: oklch(0.750 0.086 65);
  --color-tpg12-seal-hi: #f3d3b4;
  --color-tpg12-seal-hi: oklch(0.886 0.055 66);
  --color-tpg12-seal-lo: #b8865a;
  --color-tpg12-seal-lo: oklch(0.659 0.086 62);
  --color-tpg12-on-seal: #2a0d14;
  --color-tpg12-on-seal: oklch(0.209 0.049 7);
  --color-tpg12-ring: #e6b88f;
  --color-tpg12-ring: oklch(0.814 0.076 63);
  --shadow-tpg12-card: 0 1px 0 oklch(1 0 0 / 0.05) inset, 0 14px 30px -14px oklch(0 0 0 / 0.75);
  --shadow-tpg12-hover: inset 0 0 0 1px oklch(0.77 0.08 65 / 0.5);
  --shadow-tpg12-seal: inset 0 0 0 2px oklch(0.77 0.08 65), inset 0 0 0 3.5px oklch(0.25 0.06 10 / 0.9), 0 0 0 1px oklch(0.77 0.08 65 / 0.5), 0 10px 26px -8px oklch(0.77 0.08 65 / 0.5);
}
```
