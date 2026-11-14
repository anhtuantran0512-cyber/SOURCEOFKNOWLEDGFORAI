---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-portfolio-card-css-dashboard-mock/"
title: "Tailwind Portfolio Card with CSS-Drawn Dashboard Mock"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A case-study tile whose thumbnail is a miniature dashboard drawn entirely in grid and flex &mdash; side rail, KPI row, eight-bar chart &mdash; with no image…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Portfolio Card with CSS-Drawn Dashboard Mock
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-portfolio-card-css-dashboard-mock/

A case-study tile whose thumbnail is a miniature dashboard drawn entirely in grid and flex &mdash; side rail, KPI row, eight-bar chart &mdash; with no image at all. The port's win is that the mock's eight bars become a flex row of flex-1 spans whose heights are the only thing that varies.
## HTML
```html
<section class="twc-14 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc14-bg font-twc14-sans">
  <article class="group/card w-full max-w-[340px] overflow-hidden rounded-2xl bg-white border border-black/6 shadow-[0_2px_12px_oklch(0_0_0/0.04)] transition-[transform,box-shadow] duration-250 hover:-translate-y-[3px] hover:shadow-[0_14px_32px_oklch(0.55_0.12_45/0.16)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div class="relative aspect-video overflow-hidden [background:linear-gradient(135deg,#f7edd6,#e8c9a0)]">
      <div aria-hidden="true" class="absolute inset-3.5 overflow-hidden rounded-md bg-white shadow-[0_4px_12px_oklch(0.4_0.08_50/0.16)] transition-transform duration-350 ease-out group-hover/card:scale-104 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
        <div class="h-3 bg-twc14-mockbar border-b border-black/6"></div>
        <div class="grid grid-cols-[40px_1fr] h-[calc(100%-12px)]">
          <div class="flex flex-col gap-[5px] px-1.5 py-2 bg-twc14-mockside">
            <span class="block h-[5px] rounded-sm bg-twc14-acc"></span>
            <span class="block h-[5px] rounded-sm bg-twc14-mockline"></span>
            <span class="block h-[5px] rounded-sm bg-twc14-mockline"></span>
            <span class="block h-[5px] rounded-sm bg-twc14-mockline"></span>
          </div>
          <div class="flex flex-col gap-1.5 p-2">
            <div class="grid grid-cols-3 gap-1">
              <span class="h-5 rounded-[3px] bg-twc14-mockbar"></span>
              <span class="h-5 rounded-[3px] bg-twc14-mockbar"></span>
              <span class="h-5 rounded-[3px] bg-twc14-mockbar"></span>
            </div>
            <div class="flex-1 flex items-end gap-[3px] pt-1">
              <span style="height:35%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:55%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:40%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:70%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:60%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:85%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:50%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
              <span style="height:75%" class="flex-1 rounded-t-sm [background:linear-gradient(180deg,#d97e4a,#b8451f)]"></span>
            </div>
          </div>
        </div>
      </div>
      <div aria-hidden="true" class="absolute inset-0 pointer-events-none transition-opacity duration-300 group-hover/card:opacity-0 [background:linear-gradient(180deg,transparent_60%,oklch(0_0_0/0.05))] motion-reduce:transition-none"></div>
    </div>

    <div class="px-4.5 pt-4 pb-4.5">
      <span class="inline-block mb-2.5 px-2.5 py-1 rounded-full font-twc14-mono text-[10px] font-bold tracking-[0.14em] text-twc14-accink bg-twc14-acc/10">SAAS &middot; DASHBOARD</span>
      <h3 class="m-0 mb-1.5 text-base font-bold tracking-[-0.01em] text-twc14-ink">Meridian Analytics Rebrand</h3>
      <p class="m-0 mb-3 text-[12.5px]/[1.55] text-twc14-muted">Redesigned the analytics dashboard for 12k+ enterprise users &mdash; 41% faster time-to-insight.</p>
      <ul class="flex flex-wrap gap-1.5 list-none m-0 mb-3.5 p-0">
        <li class="px-2 py-[3px] rounded bg-twc14-tag text-[11px] font-semibold text-twc14-muted">Figma</li>
        <li class="px-2 py-[3px] rounded bg-twc14-tag text-[11px] font-semibold text-twc14-muted">Design System</li>
        <li class="px-2 py-[3px] rounded bg-twc14-tag text-[11px] font-semibold text-twc14-muted">Data Viz</li>
      </ul>
      <div class="flex items-center justify-between gap-2 pt-3 border-t border-black/6">
        <span class="text-xs font-semibold text-twc14-muted">Meridian Labs</span>
        <a href="#project" class="inline-flex items-center gap-1.5 min-h-11 rounded-md no-underline text-[12.5px] font-semibold text-twc14-accink transition-colors duration-200 hover:text-twc14-accdark hover:underline hover:underline-offset-[3px] focus-visible:outline-2 focus-visible:outline-twc14-acc focus-visible:outline-offset-[3px]">
          View project
          <span aria-hidden="true" class="inline-flex items-center transition-transform duration-200 ease-out group-hover/card:translate-x-[3px] motion-reduce:transition-none motion-reduce:group-hover/card:translate-x-0">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </span>
        </a>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc14-bg: #f8f7f4;
  --color-twc14-bg: oklch(0.97 0.005 90);
  --color-twc14-ink: #1a1a1a;
  --color-twc14-ink: oklch(0.21 0.005 270);
  --color-twc14-muted: #6b6459;
  --color-twc14-muted: oklch(0.49 0.015 75);
  --color-twc14-acc: #b8613b;
  --color-twc14-acc: oklch(0.55 0.12 45);
  --color-twc14-accink: #9c4e2d;
  --color-twc14-accink: oklch(0.47 0.13 42);
  --color-twc14-accdark: #7c3a1e;
  --color-twc14-accdark: oklch(0.38 0.12 42);
  --color-twc14-tag: #f5f2ec;
  --color-twc14-tag: oklch(0.96 0.008 85);
  --color-twc14-mockbar: #f0eae1;
  --color-twc14-mockbar: oklch(0.93 0.012 80);
  --color-twc14-mockside: #faf7f2;
  --color-twc14-mockside: oklch(0.97 0.008 80);
  --color-twc14-mockline: #e0d5c4;
  --color-twc14-mockline: oklch(0.87 0.02 80);
  --font-twc14-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc14-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
/* The mock dashboard is entirely utilities; the stylesheet is tokens plus
   the root contract. */

.twc-14 {
  width: 100%;
  min-height: 100svh;
}
```
