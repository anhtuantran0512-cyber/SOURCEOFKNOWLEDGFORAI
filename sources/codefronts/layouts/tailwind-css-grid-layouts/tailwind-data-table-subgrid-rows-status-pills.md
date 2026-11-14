---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-data-table-subgrid-rows-status-pills/"
title: "Tailwind Data Table with Subgrid Rows and Status Pills"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A service-health table from an observability console: sparkline per service, tabular figures that line up by digit, status pills that never squash, and one…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Data Table with Subgrid Rows and Status Pills
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-data-table-subgrid-rows-status-pills/

A service-health table from an observability console: sparkline per service, tabular figures that line up by digit, status pills that never squash, and one master track list every row inherits with [grid-template-columns:subgrid].
## HTML
```html
<section class="tgx-05 w-full min-h-svh bg-tgx05-bg font-tgx05-sans text-tgx05-ink p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-4">
    <div class="flex flex-col gap-1">
      <p class="font-tgx05-mono text-[0.68rem] tracking-[0.1em] uppercase text-tgx05-dim">Vantage · Observability</p>
      <h2 class="text-[1.25rem] font-semibold tracking-[-0.01em]">Service health — last 24h</h2>
    </div>
    <div class="flex items-center gap-2 text-[0.72rem] text-tgx05-dim">
      <span class="inline-flex items-center gap-1.5 rounded-full border border-tgx05-line px-2.5 py-1"><span class="size-1.5 rounded-full bg-tgx05-ok"></span>3 healthy</span>
      <span class="inline-flex items-center gap-1.5 rounded-full border border-tgx05-line px-2.5 py-1"><span class="size-1.5 rounded-full bg-tgx05-down"></span>1 failing</span>
    </div>
  </header>
  <div role="table" aria-label="Service health" class="grid grid-cols-[minmax(150px,1.6fr)_minmax(86px,0.8fr)_minmax(80px,0.7fr)_minmax(80px,0.7fr)_minmax(90px,0.8fr)_minmax(84px,max-content)] max-sm:grid-cols-[minmax(120px,1.6fr)_minmax(80px,1fr)_minmax(84px,max-content)] rounded-xl border border-tgx05-line overflow-hidden bg-tgx05-panel">
    <div role="row" class="col-span-full [grid-template-columns:subgrid] grid items-center gap-x-4 px-4 py-2.5 bg-tgx05-head text-[0.66rem] tracking-[0.12em] uppercase text-tgx05-dim">
      <span role="columnheader">Service</span>
      <span role="columnheader" class="max-sm:hidden">Trend</span>
      <span role="columnheader" class="text-right max-sm:hidden">Requests</span>
      <span role="columnheader" class="text-right max-sm:hidden">p95</span>
      <span role="columnheader" class="text-right">Errors</span>
      <span role="columnheader">Status</span>
    </div>
    <div role="row" class="col-span-full [grid-template-columns:subgrid] grid items-center gap-x-4 px-4 py-3 border-t border-tgx05-line text-[0.84rem] transition-colors hover:bg-tgx05-hover">
      <span role="cell" class="flex flex-col"><span class="font-medium">edge-gateway</span><span class="text-[0.7rem] text-tgx05-dim">eu-west-1 · 12 pods</span></span>
      <span role="cell" class="max-sm:hidden"><span class="grid grid-cols-8 items-end gap-[2px] h-5" role="img" aria-label="Stable traffic across 8 intervals"><i style="--v:55%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:62%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:58%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:70%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:66%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:74%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:69%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:78%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok"></i></span></span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">1,204,118</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">184ms</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim">0.02%</span>
      <span role="cell"><em class="not-italic text-[0.68rem] px-2 py-0.5 rounded-full border border-tgx05-ok/50 text-tgx05-ok bg-tgx05-ok/15">Healthy</em></span>
    </div>
    <div role="row" class="col-span-full [grid-template-columns:subgrid] grid items-center gap-x-4 px-4 py-3 border-t border-tgx05-line text-[0.84rem] transition-colors hover:bg-tgx05-hover">
      <span role="cell" class="flex flex-col"><span class="font-medium">auth-service</span><span class="text-[0.7rem] text-tgx05-dim">eu-west-1 · 6 pods</span></span>
      <span role="cell" class="max-sm:hidden"><span class="grid grid-cols-8 items-end gap-[2px] h-5" role="img" aria-label="Latency climbing across 8 intervals"><i style="--v:40%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:44%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:52%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:58%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:67%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:75%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:84%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn/60"></i><i style="--v:92%" class="h-[var(--v)] rounded-[1px] bg-tgx05-warn"></i></span></span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">386,402</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-warn max-sm:hidden">312ms</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim">0.14%</span>
      <span role="cell"><em class="not-italic text-[0.68rem] px-2 py-0.5 rounded-full border border-tgx05-warn/50 text-tgx05-warn bg-tgx05-warn/15">Degraded</em></span>
    </div>
    <div role="row" class="col-span-full [grid-template-columns:subgrid] grid items-center gap-x-4 px-4 py-3 border-t border-tgx05-line text-[0.84rem] transition-colors hover:bg-tgx05-hover">
      <span role="cell" class="flex flex-col"><span class="font-medium">billing-worker</span><span class="text-[0.7rem] text-tgx05-dim">us-east-1 · 4 pods</span></span>
      <span role="cell" class="max-sm:hidden"><span class="grid grid-cols-8 items-end gap-[2px] h-5" role="img" aria-label="Flat, low traffic across 8 intervals"><i style="--v:30%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:34%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:31%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:38%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:35%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:40%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:37%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok/60"></i><i style="--v:42%" class="h-[var(--v)] rounded-[1px] bg-tgx05-ok"></i></span></span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">92,377</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">96ms</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim">0.00%</span>
      <span role="cell"><em class="not-italic text-[0.68rem] px-2 py-0.5 rounded-full border border-tgx05-ok/50 text-tgx05-ok bg-tgx05-ok/15">Healthy</em></span>
    </div>
    <div role="row" class="col-span-full [grid-template-columns:subgrid] grid items-center gap-x-4 px-4 py-3 border-t border-tgx05-line text-[0.84rem] transition-colors hover:bg-tgx05-hover">
      <span role="cell" class="flex flex-col"><span class="font-medium">search-indexer</span><span class="text-[0.7rem] text-tgx05-dim">us-east-1 · 2 pods</span></span>
      <span role="cell" class="max-sm:hidden"><span class="grid grid-cols-8 items-end gap-[2px] h-5" role="img" aria-label="Sharp drop in throughput over 8 intervals"><i style="--v:88%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:80%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:62%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:48%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:30%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:22%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:14%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down/60"></i><i style="--v:9%" class="h-[var(--v)] rounded-[1px] bg-tgx05-down"></i></span></span>
      <span role="cell" class="text-right tabular-nums text-tgx05-dim max-sm:hidden">14,051</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-down max-sm:hidden">1,240ms</span>
      <span role="cell" class="text-right tabular-nums text-tgx05-down">2.31%</span>
      <span role="cell"><em class="not-italic text-[0.68rem] px-2 py-0.5 rounded-full border border-tgx05-down/50 text-tgx05-down bg-tgx05-down/15">Failing</em></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx05-bg: #10161a;
  --color-tgx05-bg: oklch(0.17 0.015 210);
  --color-tgx05-panel: #151d22;
  --color-tgx05-panel: oklch(0.21 0.02 210);
  --color-tgx05-head: #1a242a;
  --color-tgx05-head: oklch(0.25 0.02 210);
  --color-tgx05-hover: #1d282f;
  --color-tgx05-hover: oklch(0.27 0.02 210);
  --color-tgx05-line: #31424a;
  --color-tgx05-line: oklch(0.36 0.025 210);
  --color-tgx05-ink: #e8f0f3;
  --color-tgx05-ink: oklch(0.94 0.01 210);
  --color-tgx05-dim: #a6b8bf;
  --color-tgx05-dim: oklch(0.76 0.015 210);
  --color-tgx05-ok: #7fe3b0;
  --color-tgx05-ok: oklch(0.85 0.14 155);
  --color-tgx05-warn: #f0cc72;
  --color-tgx05-warn: oklch(0.86 0.14 85);
  --color-tgx05-down: #f4998a;
  --color-tgx05-down: oklch(0.78 0.14 25);
  --font-tgx05-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx05-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-05 {
  width: 100%;
  min-height: 100svh;
}

@supports not (grid-template-columns: subgrid) {
  .tgx-05 [role="row"] {
    grid-template-columns: minmax(150px, 1.6fr) minmax(86px, 0.8fr) minmax(80px, 0.7fr) minmax(80px, 0.7fr) minmax(90px, 0.8fr) minmax(84px, max-content);
  }
}
```
