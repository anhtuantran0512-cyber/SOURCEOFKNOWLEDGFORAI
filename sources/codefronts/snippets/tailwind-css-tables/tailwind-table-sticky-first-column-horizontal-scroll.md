---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-table-sticky-first-column-horizontal-scroll/"
title: "Tailwind Table with Sticky First Column & Horizontal Scroll"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A wide FY 2025 revenue sheet whose product column stays pinned with sticky left-0 while fifteen month and quarter columns scroll beneath it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Table with Sticky First Column & Horizontal Scroll
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-table-sticky-first-column-horizontal-scroll/

A wide FY 2025 revenue sheet whose product column stays pinned with sticky left-0 while fifteen month and quarter columns scroll beneath it. The upgrade: the separating shadow is now scroll-driven — invisible at rest, fading in only once content actually slides under the column — with a static shadow fallback for engines without animation-timeline.
## HTML
```html
<section class="ttb-07 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb07-bg px-5 py-14 font-ttb07-sans text-ttb07-ink" aria-label="Sticky first column table demo">
  <div class="w-full max-w-5xl">
    <header class="mb-5 flex flex-wrap items-end justify-between gap-3">
      <div>
        <p class="font-ttb07-mono text-[11px] tracking-[0.18em] text-ttb07-blue uppercase">Finance · FY 2025</p>
        <h2 class="mt-1 text-lg font-semibold">Revenue by product line</h2>
      </div>
      <p class="flex items-center gap-2 text-xs text-ttb07-mut"><kbd class="rounded-md bg-ttb07-surface2 px-2 py-1 font-ttb07-mono text-[11px] ring-1 ring-ttb07-line">⇠ ⇢</kbd>Scroll horizontally</p>
    </header>
    <div tabindex="0" role="region" aria-label="Revenue table, scrolls horizontally" class="relative overflow-x-auto rounded-2xl ring-1 ring-ttb07-line [scrollbar-color:var(--color-ttb07-line)_transparent] [scrollbar-width:thin] focus-visible:outline-2 focus-visible:outline-ttb07-blue">
      <table class="w-max min-w-full border-collapse font-ttb07-mono text-[13px] tabular-nums">
        <caption class="sr-only">Monthly and quarterly revenue per product line, year to date, and variance versus target</caption>
        <thead class="bg-ttb07-surface2 [&_th]:px-4 [&_th]:py-3 [&_th]:text-right [&_th]:font-ttb07-sans [&_th]:text-[10.5px] [&_th]:font-semibold [&_th]:tracking-[0.12em] [&_th]:whitespace-nowrap [&_th]:text-ttb07-head [&_th]:uppercase [&_th]:shadow-[inset_0_-1px_0_var(--color-ttb07-line)]">
          <tr>
            <th scope="col" data-sticky class="sticky left-0 z-20 min-w-44 bg-ttb07-surface2 text-left! shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Product line</th>
            <th scope="col">Jan</th><th scope="col">Feb</th><th scope="col">Mar</th><th scope="col" class="bg-ttb07-blue/10 text-ttb07-blue!">Q1</th>
            <th scope="col">Apr</th><th scope="col">May</th><th scope="col">Jun</th><th scope="col" class="bg-ttb07-blue/10 text-ttb07-blue!">Q2</th>
            <th scope="col">Jul</th><th scope="col">Aug</th><th scope="col">Sep</th><th scope="col" class="bg-ttb07-blue/10 text-ttb07-blue!">Q3</th>
            <th scope="col">YTD</th><th scope="col">vs. target</th>
          </tr>
        </thead>
        <tbody class="bg-ttb07-surface [&_td]:px-4 [&_td]:py-3.5 [&_td]:text-right [&_td]:whitespace-nowrap [&_td]:transition-colors [&_tr]:border-b [&_tr]:border-ttb07-line [&_tr:hover_td]:bg-ttb07-hover [&_tr:hover_th]:bg-ttb07-fixed-hover [&_th]:transition-colors">
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-fixed px-4 py-3.5 text-left font-ttb07-sans font-semibold text-ttb07-ink shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Cloud Storage API</th>
            <td>$148K</td><td>$162K</td><td>$178K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$488K</td>
            <td>$195K</td><td>$210K</td><td>$224K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$629K</td>
            <td>$238K</td><td>$251K</td><td>$267K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$756K</td>
            <td class="font-bold">$1.87M</td><td><span class="rounded-md bg-ttb07-green/12 px-2 py-0.5 text-xs font-bold text-ttb07-green">+12%</span></td>
          </tr>
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-fixed px-4 py-3.5 text-left font-ttb07-sans font-semibold text-ttb07-ink shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">AI Inference Engine</th>
            <td>$82K</td><td>$94K</td><td>$110K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$286K</td>
            <td>$128K</td><td>$145K</td><td>$162K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$435K</td>
            <td>$180K</td><td>$198K</td><td>$220K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$598K</td>
            <td class="font-bold">$1.32M</td><td><span class="rounded-md bg-ttb07-green/12 px-2 py-0.5 text-xs font-bold text-ttb07-green">+34%</span></td>
          </tr>
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-fixed px-4 py-3.5 text-left font-ttb07-sans font-semibold text-ttb07-ink shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Analytics Dashboard</th>
            <td>$61K</td><td>$59K</td><td>$63K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$183K</td>
            <td>$58K</td><td>$60K</td><td>$55K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$173K</td>
            <td>$49K</td><td>$52K</td><td>$48K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$149K</td>
            <td class="font-bold">$505K</td><td><span class="rounded-md bg-ttb07-red/12 px-2 py-0.5 text-xs font-bold text-ttb07-red">−8%</span></td>
          </tr>
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-fixed px-4 py-3.5 text-left font-ttb07-sans font-semibold text-ttb07-ink shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Auth &amp; Identity</th>
            <td>$40K</td><td>$42K</td><td>$45K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$127K</td>
            <td>$47K</td><td>$50K</td><td>$53K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$150K</td>
            <td>$55K</td><td>$58K</td><td>$61K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$174K</td>
            <td class="font-bold">$451K</td><td><span class="rounded-md bg-ttb07-green/12 px-2 py-0.5 text-xs font-bold text-ttb07-green">+5%</span></td>
          </tr>
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-fixed px-4 py-3.5 text-left font-ttb07-sans font-semibold text-ttb07-ink shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Edge CDN</th>
            <td>$32K</td><td>$29K</td><td>$31K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$92K</td>
            <td>$33K</td><td>$31K</td><td>$28K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$92K</td>
            <td>$26K</td><td>$24K</td><td>$22K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/8 font-bold">$72K</td>
            <td class="font-bold">$256K</td><td><span class="rounded-md bg-ttb07-red/12 px-2 py-0.5 text-xs font-bold text-ttb07-red">−18%</span></td>
          </tr>
        </tbody>
        <tfoot class="bg-ttb07-surface2 [&_td]:px-4 [&_td]:py-3.5 [&_td]:text-right [&_td]:font-bold [&_td]:whitespace-nowrap">
          <tr>
            <th scope="row" data-sticky class="sticky left-0 z-10 min-w-44 bg-ttb07-surface2 px-4 py-3.5 text-left font-ttb07-sans text-[11px] font-bold tracking-[0.12em] text-ttb07-head uppercase shadow-[1px_0_0_var(--color-ttb07-line),12px_0_18px_-8px_oklch(0_0_0/0.75)]">Grand total</th>
            <td>$363K</td><td>$386K</td><td>$427K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/10">$1.18M</td>
            <td>$461K</td><td>$496K</td><td>$522K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/10">$1.48M</td>
            <td>$548K</td><td>$583K</td><td>$618K</td><td class="border-l-2 border-ttb07-blue/25 bg-ttb07-blue/10">$1.75M</td>
            <td class="text-[14px] text-ttb07-blue">$4.40M</td><td><span class="rounded-md bg-ttb07-green/12 px-2 py-0.5 text-xs font-bold text-ttb07-green">+11%</span></td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb07-bg: #0a0e1a;
  --color-ttb07-bg: oklch(0.16 0.025 265);
  --color-ttb07-surface: #0f1624;
  --color-ttb07-surface: oklch(0.19 0.025 260);
  --color-ttb07-surface2: #151d2e;
  --color-ttb07-surface2: oklch(0.23 0.03 260);
  --color-ttb07-fixed: #0d1525;
  --color-ttb07-fixed: oklch(0.19 0.03 260);
  --color-ttb07-fixed-hover: #142039;
  --color-ttb07-fixed-hover: oklch(0.235 0.045 260);
  --color-ttb07-hover: #3b82f60f;
  --color-ttb07-hover: oklch(0.62 0.19 260 / 0.06);
  --color-ttb07-line: #1e2d42;
  --color-ttb07-line: oklch(0.3 0.04 255);
  --color-ttb07-ink: #dbe5f1;
  --color-ttb07-ink: oklch(0.91 0.02 250);
  --color-ttb07-head: #9fb3cb;
  --color-ttb07-head: oklch(0.76 0.04 250);
  --color-ttb07-mut: #8396ae;
  --color-ttb07-mut: oklch(0.67 0.04 250);
  --color-ttb07-blue: #60a5fa;
  --color-ttb07-blue: oklch(0.71 0.14 255);
  --color-ttb07-green: #34d399;
  --color-ttb07-green: oklch(0.78 0.15 165);
  --color-ttb07-red: #f87171;
  --color-ttb07-red: oklch(0.71 0.17 22);
  --font-ttb07-sans: 'Geist', system-ui, sans-serif;
  --font-ttb07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-07 {
  width: 100%;
  min-height: 100svh;
}
/* Scroll-driven edge shadow. Kept in CSS because animation-timeline must follow the animation
   shorthand, and utilities cannot guarantee declaration order. Unsupported engines keep the
   static shadow utility in the markup. */

@keyframes ttb07-edge {
  from {
    box-shadow: 1px 0 0 var(--color-ttb07-line);
  }

  to {
    box-shadow: 1px 0 0 var(--color-ttb07-line), 12px 0 18px -8px oklch(0 0 0 / 0.75);
  }
}

@supports (animation-timeline: scroll()) {
  .ttb-07 [data-sticky] {
    animation: ttb07-edge linear both;
    animation-timeline: scroll(nearest inline);
    animation-range: 0 64px;
  }
}
```
