---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-analytics-dashboard-layout-grid-app-shell/"
title: "Tailwind Analytics Dashboard Layout with Grid App Shell"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A revenue dashboard with the frame real apps need: pinned rail, toolbar with search and account, four KPIs with deltas, a chart card and an activity feed —…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Analytics Dashboard Layout with Grid App Shell
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-analytics-dashboard-layout-grid-app-shell/

A revenue dashboard with the frame real apps need: pinned rail, toolbar with search and account, four KPIs with deltas, a chart card and an activity feed — and exactly one scroll region, so the chrome never moves.
## HTML
```html
<section class="tgx-16 w-full min-h-svh bg-tgx16-bg text-tgx16-ink font-tgx16-sans p-5">
  <div class="grid [grid-template-areas:'rail_top'_'rail_body'] grid-cols-[180px_minmax(0,1fr)] grid-rows-[auto_minmax(0,1fr)] h-[440px] rounded-2xl border border-tgx16-line overflow-hidden max-md:[grid-template-areas:'top'_'body'] max-md:grid-cols-[minmax(0,1fr)]">
    <nav aria-label="Main" class="[grid-area:rail] max-md:hidden bg-tgx16-rail border-r border-tgx16-line p-4 flex flex-col gap-1">
      <strong class="flex items-center gap-2 text-[0.92rem] text-white mb-4"><span aria-hidden="true" class="size-6 grid place-items-center rounded-md bg-tgx16-blue text-tgx16-bg text-[0.72rem] font-bold">V</span>Vantage</strong>
      <a href="#0" aria-current="page" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx16-dim transition-colors hover:text-tgx16-ink hover:bg-tgx16-panel aria-[current=page]:text-white aria-[current=page]:bg-tgx16-sel aria-[current=page]:font-medium focus-visible:outline-2 focus-visible:outline-tgx16-blue focus-visible:outline-offset-2">Overview</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx16-dim transition-colors hover:text-tgx16-ink hover:bg-tgx16-panel focus-visible:outline-2 focus-visible:outline-tgx16-blue focus-visible:outline-offset-2">Revenue</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx16-dim transition-colors hover:text-tgx16-ink hover:bg-tgx16-panel focus-visible:outline-2 focus-visible:outline-tgx16-blue focus-visible:outline-offset-2">Customers</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx16-dim transition-colors hover:text-tgx16-ink hover:bg-tgx16-panel focus-visible:outline-2 focus-visible:outline-tgx16-blue focus-visible:outline-offset-2">Retention</a>
      <a href="#0" class="mt-auto text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx16-dim transition-colors hover:text-tgx16-ink hover:bg-tgx16-panel focus-visible:outline-2 focus-visible:outline-tgx16-blue focus-visible:outline-offset-2">Settings</a>
    </nav>
    <header class="[grid-area:top] flex items-center justify-between gap-4 px-4 py-3 border-b border-tgx16-line bg-tgx16-panel">
      <div class="flex items-center gap-3 min-w-0">
        <h2 class="text-[0.92rem] font-semibold truncate">Overview</h2>
        <span class="text-[0.7rem] px-2 py-0.5 rounded-full bg-tgx16-sel text-tgx16-blue">Last 30 days</span>
      </div>
      <div class="flex items-center gap-2.5">
        <span class="text-[0.76rem] text-tgx16-dim bg-tgx16-bg border border-tgx16-line rounded-lg px-3 py-1.5 max-sm:hidden">⌕ Search metrics</span>
        <span aria-label="Account: A. Rivera" class="size-8 rounded-full grid place-items-center text-[0.68rem] font-bold bg-tgx16-blue text-tgx16-bg">AR</span>
      </div>
    </header>
    <main class="[grid-area:body] overflow-y-auto p-4 flex flex-col gap-3">
      <div class="grid grid-cols-[repeat(auto-fit,minmax(min(130px,100%),1fr))] gap-2.5">
        <article class="flex flex-col gap-1 rounded-xl border border-tgx16-line bg-tgx16-panel px-3.5 py-3"><span class="text-[0.64rem] tracking-[0.1em] uppercase text-tgx16-dim">MRR</span><strong class="text-[1.3rem] tabular-nums leading-none">$84.2k</strong><em class="not-italic text-[0.7rem] text-tgx16-up">▲ 6.1% vs Aug</em></article>
        <article class="flex flex-col gap-1 rounded-xl border border-tgx16-line bg-tgx16-panel px-3.5 py-3"><span class="text-[0.64rem] tracking-[0.1em] uppercase text-tgx16-dim">Active</span><strong class="text-[1.3rem] tabular-nums leading-none">12,406</strong><em class="not-italic text-[0.7rem] text-tgx16-up">▲ 2.4%</em></article>
        <article class="flex flex-col gap-1 rounded-xl border border-tgx16-line bg-tgx16-panel px-3.5 py-3"><span class="text-[0.64rem] tracking-[0.1em] uppercase text-tgx16-dim">Churn</span><strong class="text-[1.3rem] tabular-nums leading-none">1.9%</strong><em class="not-italic text-[0.7rem] text-tgx16-down">▼ 0.3pt</em></article>
        <article class="flex flex-col gap-1 rounded-xl border border-tgx16-line bg-tgx16-panel px-3.5 py-3"><span class="text-[0.64rem] tracking-[0.1em] uppercase text-tgx16-dim">NPS</span><strong class="text-[1.3rem] tabular-nums leading-none">61</strong><em class="not-italic text-[0.7rem] text-tgx16-up">▲ 4</em></article>
      </div>
      <div class="grid grid-cols-[minmax(0,2fr)_minmax(0,1fr)] max-md:grid-cols-[minmax(0,1fr)] gap-2.5">
        <article class="rounded-xl border border-tgx16-line bg-tgx16-panel p-4">
          <div class="flex items-baseline justify-between gap-3 mb-3">
            <h3 class="text-[0.85rem] font-semibold">Weekly revenue</h3>
            <span class="text-[0.72rem] tabular-nums text-tgx16-dim">12 weeks · target $96k</span>
          </div>
          <div role="img" aria-label="Bar chart: weekly revenue climbing from 35% to 96% of target across 12 weeks" class="grid grid-cols-12 items-end gap-[5px] h-[120px]">
            <i style="--v:35%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:48%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:42%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:60%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:55%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:70%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:64%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:78%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:72%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:88%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:82%" class="h-[var(--v)] rounded-t bg-[linear-gradient(180deg,var(--color-tgx16-blue),color-mix(in_oklab,var(--color-tgx16-blue)_40%,var(--color-tgx16-panel)))]"></i>
            <i style="--v:96%" class="h-[var(--v)] rounded-t bg-tgx16-blue"></i>
          </div>
        </article>
        <aside class="rounded-xl border border-tgx16-line bg-tgx16-panel p-4 flex flex-col gap-3">
          <h3 class="text-[0.85rem] font-semibold">Activity</h3>
          <ul class="flex flex-col gap-2.5 list-none m-0 p-0">
            <li class="grid grid-cols-[8px_minmax(0,1fr)] gap-2.5 items-start"><span class="mt-1.5 size-2 rounded-full bg-tgx16-up"></span><span class="text-[0.75rem] leading-[1.45] text-tgx16-dim"><strong class="text-tgx16-ink font-medium">Enterprise plan</strong> upgraded — Brightfold Ltd</span></li>
            <li class="grid grid-cols-[8px_minmax(0,1fr)] gap-2.5 items-start"><span class="mt-1.5 size-2 rounded-full bg-tgx16-blue"></span><span class="text-[0.75rem] leading-[1.45] text-tgx16-dim"><strong class="text-tgx16-ink font-medium">38 seats</strong> added across 4 accounts</span></li>
            <li class="grid grid-cols-[8px_minmax(0,1fr)] gap-2.5 items-start"><span class="mt-1.5 size-2 rounded-full bg-tgx16-down"></span><span class="text-[0.75rem] leading-[1.45] text-tgx16-dim"><strong class="text-tgx16-ink font-medium">Payment failed</strong> — Halcyon Group</span></li>
            <li class="grid grid-cols-[8px_minmax(0,1fr)] gap-2.5 items-start"><span class="mt-1.5 size-2 rounded-full bg-tgx16-up"></span><span class="text-[0.75rem] leading-[1.45] text-tgx16-dim"><strong class="text-tgx16-ink font-medium">Q3 report</strong> exported by A. Rivera</span></li>
          </ul>
        </aside>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx16-bg: #171b24;
  --color-tgx16-bg: oklch(0.19 0.02 255);
  --color-tgx16-rail: #131720;
  --color-tgx16-rail: oklch(0.16 0.02 255);
  --color-tgx16-panel: #1e2430;
  --color-tgx16-panel: oklch(0.23 0.025 255);
  --color-tgx16-sel: #2a3a55;
  --color-tgx16-sel: oklch(0.32 0.06 255);
  --color-tgx16-line: #333b4b;
  --color-tgx16-line: oklch(0.34 0.03 255);
  --color-tgx16-ink: #e9edf4;
  --color-tgx16-ink: oklch(0.94 0.01 250);
  --color-tgx16-dim: #a8b1c2;
  --color-tgx16-dim: oklch(0.75 0.02 250);
  --color-tgx16-blue: #83b4f5;
  --color-tgx16-blue: oklch(0.76 0.12 250);
  --color-tgx16-up: #8ce0ae;
  --color-tgx16-up: oklch(0.85 0.14 150);
  --color-tgx16-down: #f0937e;
  --color-tgx16-down: oklch(0.76 0.15 30);
  --font-tgx16-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx16-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tgx-16 {
  width: 100%;
  min-height: 100svh;
}
```
