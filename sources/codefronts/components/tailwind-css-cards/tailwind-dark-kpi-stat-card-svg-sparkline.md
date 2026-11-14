---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-dark-kpi-stat-card-svg-sparkline/"
title: "Tailwind Dark KPI Stat Card with SVG Sparkline"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A dark KPI tile: pulsing live dot, a 36px gradient-clipped currency value, a trend pill, a full-bleed SVG sparkline with gradient fill and stroke, a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark KPI Stat Card with SVG Sparkline
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-dark-kpi-stat-card-svg-sparkline/

A dark KPI tile: pulsing live dot, a 36px gradient-clipped currency value, a trend pill, a full-bleed SVG sparkline with gradient fill and stroke, a three-metric strip and a timeframe switcher. The port's win is that everything except the sparkline's geometry becomes utilities &mdash; and the sparkline stays SVG, because a data path is data.
## HTML
```html
<section class="twc-15 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc15-bg [background-image:radial-gradient(ellipse_at_20%_0%,oklch(0.78_0.14_165/0.11),transparent_50%),radial-gradient(ellipse_at_80%_100%,oklch(0.8_0.13_200/0.09),transparent_50%)] font-twc15-sans">

  <article class="relative w-full max-w-[360px] overflow-hidden rounded-[20px] px-5.5 pt-5.5 pb-4.5 border border-white/6 [background:linear-gradient(180deg,oklch(0.78_0.14_165/0.03)_0%,transparent_40%),linear-gradient(160deg,#14151d_0%,#0d0e15_100%)] shadow-[0_30px_60px_-30px_oklch(0_0_0/0.7),inset_0_1px_0_oklch(1_0_0/0.04)]">

    <div aria-hidden="true" class="absolute -top-15 -right-10 size-50 pointer-events-none blur-[20px] [background:radial-gradient(circle,oklch(0.78_0.14_165/0.16)_0%,transparent_60%)]"></div>

    <header class="relative flex items-center justify-between mb-3.5">
      <div class="flex items-center gap-2">
        <span aria-hidden="true" class="size-1.5 rounded-full bg-twc15-acc shadow-[0_0_0_3px_oklch(0.78_0.14_165/0.18),0_0_12px_oklch(0.78_0.14_165/0.6)] animate-twc15-pulse motion-reduce:animate-none"></span>
        <h3 class="m-0 text-xs font-medium text-twc15-dim">Monthly recurring revenue</h3>
      </div>
      <button type="button" aria-label="More options" aria-haspopup="menu" aria-expanded="false" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border-0 text-twc15-faint cursor-pointer transition-[background,color] duration-200 hover:bg-white/5 hover:text-twc15-ink2 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>
      </button>
    </header>

    <div class="relative flex items-end justify-between gap-3 mb-1.5">
      <p class="m-0 text-4xl/[1.05] font-bold tracking-[-0.035em] text-twc15-white [font-variant-numeric:tabular-nums] [background-image:linear-gradient(180deg,#ffffff_0%,#b4b4be_130%)] bg-clip-text text-transparent forced-colors:text-[CanvasText] forced-colors:[-webkit-text-fill-color:CanvasText]"><data value="284712">$284,712</data></p>
      <div class="flex flex-col items-end gap-1 pb-1">
        <span class="inline-flex items-center gap-1 px-2 py-[3px] rounded-full bg-twc15-acc/24 border border-twc15-acc/30 text-xs font-bold text-twc15-acc [font-variant-numeric:tabular-nums]">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg>
          12.4%
        </span>
        <span class="text-[10.5px] tracking-[0.01em] text-twc15-faint [font-variant-numeric:tabular-nums]">vs prev &middot; $253,120</span>
      </div>
    </div>

    <div class="relative h-20 -mx-5.5 px-5.5 mt-1.5 mb-3">
      <svg viewBox="0 0 300 80" preserveAspectRatio="none" role="img" aria-label="Monthly recurring revenue trending up across twelve points, from $253,120 to $284,712" class="block size-full overflow-visible">
        <defs>
          <linearGradient id="twc15-fill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stop-color="#34d399" stop-opacity="0.35"/>
            <stop offset="1" stop-color="#34d399" stop-opacity="0"/>
          </linearGradient>
          <linearGradient id="twc15-line" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0" stop-color="#34d399"/>
            <stop offset="1" stop-color="#22d3ee"/>
          </linearGradient>
        </defs>
        <line x1="0" y1="42" x2="300" y2="42" stroke="oklch(1 0 0 / 0.08)" stroke-width="1" stroke-dasharray="3 4"/>
        <path d="M 0 60 L 25 55 L 50 58 L 75 48 L 100 52 L 125 42 L 150 38 L 175 30 L 200 26 L 225 20 L 250 14 L 275 10 L 300 6 L 300 80 L 0 80 Z" fill="url(#twc15-fill)"/>
        <path d="M 0 60 L 25 55 L 50 58 L 75 48 L 100 52 L 125 42 L 150 38 L 175 30 L 200 26 L 225 20 L 250 14 L 275 10 L 300 6" fill="none" stroke="url(#twc15-line)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="300" cy="6" r="7" fill="#34d399" opacity="0.25"/>
        <circle cx="300" cy="6" r="4" fill="#34d399"/>
      </svg>
    </div>

    <dl class="relative grid grid-cols-3 m-0 mb-3.5 py-3 rounded-xl bg-white/4 border border-white/5">
      <div class="flex flex-col items-center gap-0.5 px-2">
        <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc15-faint">Active users</dt>
        <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc15-ink [font-variant-numeric:tabular-nums]"><data value="12847">12.8k</data></dd>
      </div>
      <div class="flex flex-col items-center gap-0.5 px-2 border-l border-white/6">
        <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc15-faint">ARPU</dt>
        <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc15-ink [font-variant-numeric:tabular-nums]"><data value="22.14">$22.14</data></dd>
      </div>
      <div class="flex flex-col items-center gap-0.5 px-2 border-l border-white/6">
        <dt class="m-0 text-[9.5px] font-semibold tracking-[0.1em] uppercase text-twc15-faint">Churn</dt>
        <dd class="m-0 text-sm font-bold tracking-[-0.01em] text-twc15-warn [font-variant-numeric:tabular-nums]"><data value="2.1">2.1%</data></dd>
      </div>
    </dl>

    <div role="group" aria-label="Timeframe" class="relative grid grid-cols-4 gap-0.5 p-[3px] mb-3 rounded-[10px] bg-white/3 border border-white/5">
      <button type="button" aria-pressed="false" class="min-h-11 rounded-[7px] border-0 bg-transparent text-[11.5px] font-semibold tracking-[0.02em] text-twc15-faint cursor-pointer transition-[background,color] duration-200 hover:text-twc15-ink2 hover:bg-white/3 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">7D</button>
      <button type="button" aria-pressed="true" class="min-h-11 rounded-[7px] border-0 text-[11.5px] font-semibold tracking-[0.02em] text-twc15-btnink cursor-pointer [background:linear-gradient(180deg,#ecfdf5_0%,#a7f3d0_100%)] shadow-[0_2px_8px_oklch(0.78_0.14_165/0.25),0_0_0_1px_oklch(0.78_0.14_165/0.4)] transition-[background,color] duration-200 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">30D</button>
      <button type="button" aria-pressed="false" class="min-h-11 rounded-[7px] border-0 bg-transparent text-[11.5px] font-semibold tracking-[0.02em] text-twc15-faint cursor-pointer transition-[background,color] duration-200 hover:text-twc15-ink2 hover:bg-white/3 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">90D</button>
      <button type="button" aria-pressed="false" class="min-h-11 rounded-[7px] border-0 bg-transparent text-[11.5px] font-semibold tracking-[0.02em] text-twc15-faint cursor-pointer transition-[background,color] duration-200 hover:text-twc15-ink2 hover:bg-white/3 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2 motion-reduce:transition-none">1Y</button>
    </div>

    <footer class="relative flex items-center justify-between pt-3 border-t border-white/5 text-[10.5px]">
      <span class="inline-flex items-center gap-1.5 text-twc15-faint before:size-1 before:rounded-full before:bg-twc15-dot before:content-['']">Updated 2m ago</span>
      <a href="#report" class="inline-flex items-center gap-1 min-h-11 px-1.5 rounded-md no-underline font-semibold text-twc15-dim transition-[color,background] duration-200 hover:text-twc15-acc hover:bg-twc15-acc/8 focus-visible:outline-2 focus-visible:outline-twc15-acc focus-visible:outline-offset-2">
        View full report
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </footer>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc15-bg: #06070c;
  --color-twc15-bg: oklch(0.11 0.01 270);
  --color-twc15-white: #fafafa;
  --color-twc15-white: oklch(0.98 0 0);
  --color-twc15-ink: #f4f4f5;
  --color-twc15-ink: oklch(0.96 0.002 285);
  --color-twc15-ink2: #d4d4d8;
  --color-twc15-ink2: oklch(0.87 0.005 285);
  --color-twc15-dim: #a1a1aa;
  --color-twc15-dim: oklch(0.7 0.01 285);
  --color-twc15-faint: #71717a;
  --color-twc15-faint: oklch(0.54 0.015 285);
  --color-twc15-dot: #52525b;
  --color-twc15-dot: oklch(0.42 0.012 285);
  --color-twc15-acc: #34d399;
  --color-twc15-acc: oklch(0.78 0.14 165);
  --color-twc15-warn: #fbbf24;
  --color-twc15-warn: oklch(0.82 0.16 80);
  --color-twc15-btnink: #06070c;
  --color-twc15-btnink: oklch(0.11 0.01 270);
  --font-twc15-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc15-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc15-pulse: twc15-pulse 2.4s ease-in-out infinite;
}

@keyframes twc15-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 0 3px oklch(0.78 0.14 165 / 0.18), 0 0 12px oklch(0.78 0.14 165 / 0.6);
  }

  50% {
    transform: scale(1.15);
    box-shadow: 0 0 0 5px oklch(0.78 0.14 165 / 0.1), 0 0 16px oklch(0.78 0.14 165 / 0.9);
  }
}

.twc-15 {
  width: 100%;
  min-height: 100svh;
}
```
