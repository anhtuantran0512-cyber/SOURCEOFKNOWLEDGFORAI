---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-overlapping-card-hero-case-study/"
title: "Tailwind Overlapping Card Hero for a Case Study"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "An agency case-study teaser where the results card overlaps the project photograph — the composition every studio site uses, built from shared grid cells…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Overlapping Card Hero for a Case Study
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-overlapping-card-hero-case-study/

An agency case-study teaser where the results card overlaps the project photograph — the composition every studio site uses, built from shared grid cells instead of absolute offsets, so it scales instead of drifting.
## HTML
```html
<section class="tgx-06 w-full min-h-svh bg-tgx06-bg font-tgx06-sans px-6 py-10 grid place-items-center">
  <div class="grid grid-cols-12 grid-rows-[repeat(8,minmax(30px,auto))] w-[min(660px,100%)]">
    <figure class="col-start-1 col-end-9 row-start-1 row-end-7 z-10 overflow-hidden rounded-2xl bg-tgx06-shade shadow-[0_24px_50px_-24px_oklch(0.25_0.04_260/0.5)]">
      <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=900&h=700&q=80&auto=format&fit=crop" alt="Two designers reviewing screens together at a shared desk" loading="lazy" class="w-full h-full object-cover">
    </figure>
    <article class="col-start-6 col-end-13 row-start-4 row-end-9 max-sm:col-start-2 max-sm:col-end-12 z-20 flex flex-col gap-3 rounded-2xl bg-white p-6 shadow-[0_20px_44px_-20px_oklch(0.25_0.04_260/0.45)]">
      <p class="text-[0.66rem] font-semibold tracking-[0.16em] uppercase text-tgx06-accent">Case study · Northwind</p>
      <h3 class="text-[clamp(1.1rem,2.6vw,1.4rem)] leading-[1.22] font-semibold text-tgx06-ink text-balance">Rebuilding a freight console around one grid system</h3>
      <p class="text-[0.85rem] leading-[1.6] text-tgx06-mut">Six screens, one track vocabulary. Support tickets about "the table pushing the sidebar off" went to zero in the first week.</p>
      <dl class="grid grid-cols-3 gap-3 pt-1 border-t border-tgx06-line mt-1">
        <div class="flex flex-col gap-0.5"><dt class="text-[0.62rem] uppercase tracking-[0.1em] text-tgx06-mut">Ship time</dt><dd class="text-[1.05rem] font-semibold tabular-nums text-tgx06-ink">9 wks</dd></div>
        <div class="flex flex-col gap-0.5"><dt class="text-[0.62rem] uppercase tracking-[0.1em] text-tgx06-mut">CLS</dt><dd class="text-[1.05rem] font-semibold tabular-nums text-tgx06-ink">0.00</dd></div>
        <div class="flex flex-col gap-0.5"><dt class="text-[0.62rem] uppercase tracking-[0.1em] text-tgx06-mut">CSS cut</dt><dd class="text-[1.05rem] font-semibold tabular-nums text-tgx06-accent">−62%</dd></div>
      </dl>
      <a href="#0" class="mt-auto inline-flex items-center gap-1.5 min-h-11 text-[0.83rem] font-semibold text-tgx06-accent no-underline hover:underline underline-offset-4 focus-visible:outline-2 focus-visible:outline-tgx06-accent focus-visible:outline-offset-2 rounded">Read the case study <span aria-hidden="true">→</span></a>
    </article>
    <p class="col-start-2 col-end-6 row-start-6 row-end-7 z-30 self-center justify-self-start font-tgx06-mono text-[0.68rem] font-medium text-white bg-black/45 backdrop-blur-sm border border-white/25 rounded-full px-3 py-1.5">6 screens · 1 grid</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx06-bg: #eceaf4;
  --color-tgx06-bg: oklch(0.93 0.015 285);
  --color-tgx06-shade: #d9d6e6;
  --color-tgx06-shade: oklch(0.87 0.02 285);
  --color-tgx06-ink: #22202e;
  --color-tgx06-ink: oklch(0.24 0.02 285);
  --color-tgx06-mut: #5c586e;
  --color-tgx06-mut: oklch(0.46 0.025 285);
  --color-tgx06-line: #e0dde9;
  --color-tgx06-line: oklch(0.9 0.012 285);
  --color-tgx06-accent: #5a3ec8;
  --color-tgx06-accent: oklch(0.46 0.19 285);
  --font-tgx06-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx06-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-06 {
  width: 100%;
  min-height: 100svh;
}
/* Safari < 16.4 backdrop-filter prefix for the badge. */

.tgx-06 p.backdrop-blur-sm {
  -webkit-backdrop-filter: blur(8px);
}
```
