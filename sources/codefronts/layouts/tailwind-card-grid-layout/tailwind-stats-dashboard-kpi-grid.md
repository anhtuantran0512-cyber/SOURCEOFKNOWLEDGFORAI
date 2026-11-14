---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-stats-dashboard-kpi-grid/"
title: "Tailwind Stats Dashboard KPI Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "Six SaaS KPI cards — MRR, active users, churn, NPS, deploys, uptime — each with its metric, its delta and a sparkline drawn from flex-1 divs, no chart…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stats Dashboard KPI Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-stats-dashboard-kpi-grid/

Six SaaS KPI cards — MRR, active users, churn, NPS, deploys, uptime — each with its metric, its delta and a sparkline drawn from flex-1 divs, no chart library and no SVG. The port's move is the per-card accent: style="--accent:#7c3aed" stays an inline custom property, and the accent bar, the border-on-hover and every sparkline bar read it back through bg-[var(--accent)].
## HTML
```html
<section class="tcg-13 w-full min-h-svh bg-tcg13-bg font-tcg13-sans text-tcg13-ink px-[clamp(20px,3vw,40px)] py-[clamp(28px,3.4vw,48px)]" aria-label="Stats dashboard KPI card grid demo">

  <header class="max-w-[1200px] mx-auto mb-[clamp(20px,2.5vw,32px)] flex flex-wrap items-center max-[760px]:items-start justify-between gap-3.5">
    <div>
      <h2 class="text-[clamp(1.5rem,2.6vw,2rem)] font-extrabold tracking-[-0.02em] leading-none">Dashboard</h2>
      <span class="block mt-1.5 text-[.84rem] font-medium text-tcg13-muted">Last 30 days &middot; Updated 2 min ago</span>
    </div>
    <div class="flex gap-0.5 p-1 rounded-[10px] border border-tcg13-line bg-tcg13-card" role="group" aria-label="Date range">
      <button type="button" class="min-h-11 px-3 rounded-[7px] font-tcg13-sans text-[.76rem] font-bold tracking-[0.04em] text-tcg13-muted cursor-pointer transition-[background,color] duration-200 hover:text-tcg13-ink focus-visible:outline-2 focus-visible:outline-tcg13-ink focus-visible:outline-offset-2 motion-reduce:transition-none">7D</button>
      <button type="button" aria-pressed="true" class="min-h-11 px-3 rounded-[7px] font-tcg13-sans text-[.76rem] font-bold tracking-[0.04em] bg-tcg13-ink text-white cursor-pointer focus-visible:outline-2 focus-visible:outline-tcg13-ink focus-visible:outline-offset-2">30D</button>
      <button type="button" class="min-h-11 px-3 rounded-[7px] font-tcg13-sans text-[.76rem] font-bold tracking-[0.04em] text-tcg13-muted cursor-pointer transition-[background,color] duration-200 hover:text-tcg13-ink focus-visible:outline-2 focus-visible:outline-tcg13-ink focus-visible:outline-offset-2 motion-reduce:transition-none">90D</button>
      <button type="button" class="min-h-11 px-3 rounded-[7px] font-tcg13-sans text-[.76rem] font-bold tracking-[0.04em] text-tcg13-muted cursor-pointer transition-[background,color] duration-200 hover:text-tcg13-ink focus-visible:outline-2 focus-visible:outline-tcg13-ink focus-visible:outline-offset-2 motion-reduce:transition-none">1Y</button>
    </div>
  </header>

  <div class="max-w-[1200px] mx-auto grid [grid-template-columns:repeat(auto-fit,minmax(220px,1fr))] gap-[clamp(12px,1.4vw,18px)]">

    <article style="--accent:#7c3aed" class="group relative col-span-2 max-[760px]:col-span-1 flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">Monthly Recurring Revenue</span>
      <div class="flex flex-wrap items-baseline gap-3.5">
        <span class="text-[clamp(2.4rem,4.2vw,3.4rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">$847.2K</span>
        <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-up">&#9650; 12.4%</span>
      </div>
      <p class="mt-1 text-[.86rem] leading-[1.45] text-tcg13-muted text-pretty">+$93.4K vs last 30 days. On track for $1M MRR by Q4.</p>
      <div class="flex items-end gap-[3px] h-18 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:32%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:48%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:42%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:58%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:52%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:68%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:76%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:90%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

    <article style="--accent:#0ea5e9" class="group relative flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">Active Users</span>
      <span class="text-[clamp(1.8rem,3vw,2.6rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">12,418</span>
      <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-up">&#9650; 8.1%</span>
      <div class="flex items-end gap-[3px] h-12 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:48%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:52%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:46%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:62%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:58%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:72%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:68%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:84%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

    <article style="--accent:#ef4444" class="group relative flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">Churn Rate</span>
      <span class="text-[clamp(1.8rem,3vw,2.6rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">2.1%</span>
      <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-down">&#9660; 0.4%</span>
      <div class="flex items-end gap-[3px] h-12 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:64%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:58%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:62%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:48%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:42%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:38%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:34%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:28%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

    <article style="--accent:#10b981" class="group relative flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">NPS Score</span>
      <span class="text-[clamp(1.8rem,3vw,2.6rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">+72</span>
      <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-up">&#9650; 4 pts</span>
      <div class="flex items-end gap-[3px] h-12 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:58%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:60%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:55%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:65%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:62%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:72%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:68%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:78%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

    <article style="--accent:#f59e0b" class="group relative flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">Deploys / week</span>
      <span class="text-[clamp(1.8rem,3vw,2.6rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">147</span>
      <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-up">&#9650; 22</span>
      <div class="flex items-end gap-[3px] h-12 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:42%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:52%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:48%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:64%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:58%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:72%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:78%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:88%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

    <article style="--accent:#06b6d4" class="group relative flex flex-col gap-1.5 overflow-hidden rounded-[14px] border border-tcg13-line bg-tcg13-card p-[clamp(18px,2vw,22px)] transition-[translate,box-shadow,border-color] duration-250 hover:-translate-y-0.5 hover:border-[var(--accent)] hover:shadow-[0_14px_28px_-16px_oklch(0.2_0.04_260/0.14)] before:absolute before:inset-x-0 before:top-0 before:h-[3px] before:bg-[var(--accent)] before:opacity-0 before:transition-opacity before:duration-250 hover:before:opacity-100 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="text-[.74rem] font-bold tracking-[0.1em] uppercase text-tcg13-muted">Uptime</span>
      <span class="text-[clamp(1.8rem,3vw,2.6rem)] font-black tracking-[-0.025em] leading-[1.05] tabular-nums">99.98%</span>
      <span class="inline-flex items-center gap-1 text-[.86rem] font-bold tabular-nums text-tcg13-muted">&mdash; flat</span>
      <div class="flex items-end gap-[3px] h-12 mt-auto pt-3.5" aria-hidden="true">
        <i style="height:88%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:90%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:86%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:92%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:88%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:94%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:90%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
        <i style="height:92%" class="flex-1 block min-h-1.5 rounded-t-sm bg-linear-[180deg,var(--accent),transparent_130%]"></i>
      </div>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg13-bg: #f8fafc;
  --color-tcg13-bg: oklch(0.98 0.004 250);
  --color-tcg13-card: #ffffff;
  --color-tcg13-card: oklch(1 0 0);
  --color-tcg13-ink: #0f172a;
  --color-tcg13-ink: oklch(0.21 0.04 260);
  --color-tcg13-muted: #64748b;
  --color-tcg13-muted: oklch(0.55 0.03 257);
  --color-tcg13-line: #e2e8f0;
  --color-tcg13-line: oklch(0.92 0.01 255);
  --color-tcg13-up: #10b981;
  --color-tcg13-up: oklch(0.7 0.15 162);
  --color-tcg13-down: #ef4444;
  --color-tcg13-down: oklch(0.64 0.21 25);
  --font-tcg13-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tcg13-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh. It scopes the demo, and it holds the stage at full height in the
   moment before the browser build has compiled its utilities. */

.tcg-13 {
  width: 100%;
  min-height: 100svh;
}
/* No variant form: a scoped selection colour. */

.tcg-13 ::selection {
  background: #0f172a;
  color: #fff;
}
```
