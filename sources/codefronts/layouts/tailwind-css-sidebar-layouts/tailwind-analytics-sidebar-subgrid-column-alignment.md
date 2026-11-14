---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-analytics-sidebar-subgrid-column-alignment/"
title: "Tailwind Analytics Sidebar with CSS Subgrid Column Alignment"
section: "layouts"
category: "tailwind-css-sidebar-layouts"
category_name: "Tailwind CSS Sidebar Layouts"
description: "The alignment problem every metrics rail has &mdash; icons, labels of wildly different lengths, live values and status badges drifting out of column &mdash;…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Analytics Sidebar with CSS Subgrid Column Alignment
Source: https://codefronts.com/layouts/tailwind-css-sidebar-layouts/tailwind-analytics-sidebar-subgrid-column-alignment/

The alignment problem every metrics rail has &mdash; icons, labels of wildly different lengths, live values and status badges drifting out of column &mdash; solved with grid-template-columns: subgrid. Every row borrows the same four tracks from the list, so no width is ever hard-coded.
## HTML
```html
<section class="tsl-05 w-full h-svh min-h-svh grid grid-cols-[288px_1fr] font-tsl05-sans bg-tsl05-bg text-tsl05-ink">
  <aside aria-label="Service metrics" class="bg-tsl05-panel border-r border-tsl05-line px-3.5 py-5 overflow-y-auto [scrollbar-gutter:stable]">
    <h2 class="px-2 pt-0.5 pb-[18px] font-tsl05-mono text-[15px] font-bold">ops<span class="text-tsl05-mut">/grid</span></h2>
    <ul class="list-none m-0 p-0 grid grid-cols-[auto_1fr_auto_auto] gap-y-0.5">
      <li class="col-span-full px-2 pt-4 pb-2 text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl05-mut">Core services</li>
      <li class="col-span-full grid [grid-template-columns:subgrid] items-center gap-x-[11px] min-h-11 px-2 rounded-[9px] transition-colors duration-150 hover:bg-tsl05-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl05-mut stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]"><rect x="3" y="5" width="18" height="6" rx="1.5"/><rect x="3" y="13" width="18" height="6" rx="1.5"/><path d="M6.5 8h.01M6.5 16h.01"/></svg><a href="#" class="text-[13.5px] font-medium text-tsl05-ink no-underline truncate rounded-sm focus-visible:outline-2 focus-visible:outline-tsl05-ok focus-visible:outline-offset-[3px]">API gateway</a><data value="99.98" class="font-tsl05-mono text-[12.5px] font-medium tabular-nums text-end text-tsl05-mut">99.98%</data><span title="Healthy" class="w-2 h-2 rounded-full justify-self-center bg-tsl05-ok shadow-[0_0_8px_var(--color-tsl05-okglow)]"></span></li>
      <li class="col-span-full grid [grid-template-columns:subgrid] items-center gap-x-[11px] min-h-11 px-2 rounded-[9px] transition-colors duration-150 hover:bg-tsl05-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl05-mut stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg><a href="#" class="text-[13.5px] font-medium text-tsl05-ink no-underline truncate rounded-sm focus-visible:outline-2 focus-visible:outline-tsl05-ok focus-visible:outline-offset-[3px]">Postgres primary</a><data value="12" class="font-tsl05-mono text-[12.5px] font-medium tabular-nums text-end text-tsl05-mut">12ms</data><span title="Healthy" class="w-2 h-2 rounded-full justify-self-center bg-tsl05-ok shadow-[0_0_8px_var(--color-tsl05-okglow)]"></span></li>
      <li class="col-span-full grid [grid-template-columns:subgrid] items-center gap-x-[11px] min-h-11 px-2 rounded-[9px] transition-colors duration-150 hover:bg-tsl05-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl05-mut stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M13 3 4 14h6l-1 7 9-11h-6z"/></svg><a href="#" class="text-[13.5px] font-medium text-tsl05-ink no-underline truncate rounded-sm focus-visible:outline-2 focus-visible:outline-tsl05-ok focus-visible:outline-offset-[3px]">Job queue</a><data value="1482" class="font-tsl05-mono text-[12.5px] font-medium tabular-nums text-end text-tsl05-mut">1,482</data><span title="Degraded" class="w-2 h-2 rounded-full justify-self-center bg-tsl05-warn shadow-[0_0_8px_var(--color-tsl05-warnglow)]"></span></li>
      <li class="col-span-full px-2 pt-4 pb-2 text-[10.5px] font-semibold uppercase tracking-[0.09em] text-tsl05-mut">Observability</li>
      <li class="col-span-full grid [grid-template-columns:subgrid] items-center gap-x-[11px] min-h-11 px-2 rounded-[9px] transition-colors duration-150 hover:bg-tsl05-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl05-mut stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><a href="#" class="text-[13.5px] font-medium text-tsl05-ink no-underline truncate rounded-sm focus-visible:outline-2 focus-visible:outline-tsl05-ok focus-visible:outline-offset-[3px]">Error rate</a><data value="0.42" class="font-tsl05-mono text-[12.5px] font-medium tabular-nums text-end text-tsl05-mut">0.42%</data><span title="Healthy" class="w-2 h-2 rounded-full justify-self-center bg-tsl05-ok shadow-[0_0_8px_var(--color-tsl05-okglow)]"></span></li>
      <li class="col-span-full grid [grid-template-columns:subgrid] items-center gap-x-[11px] min-h-11 px-2 rounded-[9px] transition-colors duration-150 hover:bg-tsl05-hover"><svg viewBox="0 0 24 24" aria-hidden="true" class="w-4 h-4 fill-none stroke-tsl05-mut stroke-[1.7] [stroke-linecap:round] [stroke-linejoin:round]"><path d="M18 8a6 6 0 1 0-12 0c0 7-3 8-3 8h18s-3-1-3-8m-4.3 11a2 2 0 0 1-3.4 0"/></svg><a href="#" class="text-[13.5px] font-medium text-tsl05-ink no-underline truncate rounded-sm focus-visible:outline-2 focus-visible:outline-tsl05-ok focus-visible:outline-offset-[3px]">Open alerts</a><data value="4" class="font-tsl05-mono text-[12.5px] font-medium tabular-nums text-end text-tsl05-mut">4</data><span title="Critical" class="w-2 h-2 rounded-full justify-self-center bg-tsl05-crit shadow-[0_0_8px_var(--color-tsl05-critglow)]"></span></li>
    </ul>
  </aside>
  <main class="p-8 overflow-y-auto [scrollbar-gutter:stable]">
    <h1 class="text-[22px] font-semibold leading-tight mb-2.5">Infrastructure</h1>
    <p class="max-w-[48ch] text-sm leading-relaxed text-tsl05-mut text-pretty">Labels, values and badges align on shared subgrid rails &mdash; inspect the value column: no fixed widths anywhere.</p>
  </main>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsl05-bg: #111418;
  --color-tsl05-bg: oklch(0.13 0.012 260);
  --color-tsl05-panel: #181b20;
  --color-tsl05-panel: oklch(0.16 0.015 260);
  --color-tsl05-ink: #e9ebee;
  --color-tsl05-ink: oklch(0.93 0.005 260);
  --color-tsl05-mut: #8f939b;
  --color-tsl05-mut: oklch(0.62 0.012 260);
  --color-tsl05-line: #373a41;
  --color-tsl05-line: oklch(0.27 0.015 260);
  --color-tsl05-ok: #4fd39a;
  --color-tsl05-ok: oklch(0.75 0.17 155);
  --color-tsl05-warn: #e0b64a;
  --color-tsl05-warn: oklch(0.8 0.15 85);
  --color-tsl05-crit: #e2603f;
  --color-tsl05-crit: oklch(0.66 0.21 25);
  --color-tsl05-okglow: rgb(79 211 154 / 0.6);
  --color-tsl05-okglow: color-mix(in oklab, oklch(0.75 0.17 155) 60%, transparent);
  --color-tsl05-warnglow: rgb(224 182 74 / 0.6);
  --color-tsl05-warnglow: color-mix(in oklab, oklch(0.8 0.15 85) 60%, transparent);
  --color-tsl05-critglow: rgb(226 96 63 / 0.6);
  --color-tsl05-critglow: color-mix(in oklab, oklch(0.66 0.21 25) 60%, transparent);
  --color-tsl05-hover: rgb(233 235 238 / 0.06);
  --color-tsl05-hover: color-mix(in oklab, oklch(0.93 0.005 260) 6%, transparent);
  --font-tsl05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsl05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tsl-05 {
  width: 100%;
  height: 100svh;
  min-height: 100svh;
  color-scheme: dark;
}
```
