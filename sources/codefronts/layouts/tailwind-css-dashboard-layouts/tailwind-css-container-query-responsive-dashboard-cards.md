---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-container-query-responsive-dashboard-cards/"
title: "Tailwind CSS Container Query Responsive Dashboard Cards"
section: "layouts"
category: "tailwind-css-dashboard-layouts"
category_name: "Tailwind CSS Dashboard Layouts"
description: "The same widget markup in three slots &mdash; a narrow card, a medium card and one you drag &mdash; renders three layouts: stacked, value-beside-chart, and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Container Query Responsive Dashboard Cards
Source: https://codefronts.com/layouts/tailwind-css-dashboard-layouts/tailwind-css-container-query-responsive-dashboard-cards/

The same widget markup in three slots &mdash; a narrow card, a medium card and one you drag &mdash; renders three layouts: stacked, value-beside-chart, and full analytics with a legend rail. In v4, container queries are built in: @container/w on the slot, @min-[21.25rem]/w: and @min-[32.5rem]/w: on the widget. A live badge on every card names the layout it is currently in.
## HTML
```html
<section class="tdl-08 w-full min-h-svh bg-tdl08-bg bg-linear-175 from-tdl08-bg to-tdl08-bg2 font-tdl08-sans text-tdl08-ink antialiased" aria-label="Container query widget demo">
  <div class="mx-auto grid min-h-svh w-full max-w-6xl content-center gap-5 p-4 sm:p-6">
    <div class="flex flex-wrap gap-4">
      <div class="@container/w grid min-w-0 flex-[0_0_16.25rem] content-start gap-2.25 max-sm:flex-auto">
        <p class="text-[10.5px] font-bold tracking-[0.09em] text-tdl08-mut uppercase">16.25rem slot</p>
        <div class="grid gap-3.5 rounded-2xl border border-tdl08-edge bg-tdl08-panel p-4.5 shadow-[0_10px_26px_-20px_var(--color-tdl08-shadow)] @min-[21.25rem]/w:grid-cols-[auto_minmax(0,1fr)] @min-[21.25rem]/w:items-end @min-[32.5rem]/w:grid-cols-[auto_minmax(0,1fr)_9rem]">
          <div class="@min-[21.25rem]/w:self-center @min-[21.25rem]/w:pr-2"><h3 class="flex items-center gap-2 text-[11px] font-semibold tracking-[0.11em] text-tdl08-mut uppercase">Bandwidth<span class="rounded-full bg-tdl08-c1/12 px-1.75 py-0.5 text-[9.5px] tracking-[0.06em] text-tdl08-c1"><span class="@min-[21.25rem]/w:hidden">Stacked</span><span class="hidden @min-[21.25rem]/w:inline @min-[32.5rem]/w:hidden">Split</span><span class="hidden @min-[32.5rem]/w:inline">Full</span></span></h3><p class="mt-1 mb-0.5 text-[clamp(26px,10cqi,42px)]/[1.1] font-bold tracking-[-0.02em] tabular-nums">4.6<small class="ml-0.5 text-[0.5em] font-semibold text-tdl08-mut">TB</small></p><span class="text-[11.5px] font-bold text-tdl08-good">▲ 18% this week</span></div>
          <div aria-hidden="true" class="flex h-16 min-w-0 items-end gap-1.5 *:h-(--h) *:flex-1 *:rounded-t-[4px] *:bg-linear-to-t *:from-tdl08-c1/30 *:to-tdl08-c1"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
          <div class="hidden content-center gap-2 @min-[32.5rem]/w:grid"><div aria-hidden="true" class="flex h-1.5 overflow-hidden rounded-full"><i class="w-[62%] bg-tdl08-c1"></i><i class="w-[27%] bg-tdl08-c2"></i><i class="w-[11%] bg-tdl08-c3"></i></div><ul class="grid gap-1.5 text-xs font-semibold text-tdl08-mut [&_i]:size-2.5 [&_i]:rounded-[3px] [&>li]:flex [&>li]:items-center [&>li]:gap-2"><li><i class="bg-tdl08-c1" aria-hidden="true"></i>CDN 62%</li><li><i class="bg-tdl08-c2" aria-hidden="true"></i>API 27%</li><li><i class="bg-tdl08-c3" aria-hidden="true"></i>Media 11%</li></ul></div>
        </div>
      </div>
      <div class="@container/w grid min-w-0 flex-[1_1_19rem] content-start gap-2.25">
        <p class="text-[10.5px] font-bold tracking-[0.09em] text-tdl08-mut uppercase">Fluid slot</p>
        <div class="grid gap-3.5 rounded-2xl border border-tdl08-edge bg-tdl08-panel p-4.5 shadow-[0_10px_26px_-20px_var(--color-tdl08-shadow)] @min-[21.25rem]/w:grid-cols-[auto_minmax(0,1fr)] @min-[21.25rem]/w:items-end @min-[32.5rem]/w:grid-cols-[auto_minmax(0,1fr)_9rem]">
          <div class="@min-[21.25rem]/w:self-center @min-[21.25rem]/w:pr-2"><h3 class="flex items-center gap-2 text-[11px] font-semibold tracking-[0.11em] text-tdl08-mut uppercase">Bandwidth<span class="rounded-full bg-tdl08-c1/12 px-1.75 py-0.5 text-[9.5px] tracking-[0.06em] text-tdl08-c1"><span class="@min-[21.25rem]/w:hidden">Stacked</span><span class="hidden @min-[21.25rem]/w:inline @min-[32.5rem]/w:hidden">Split</span><span class="hidden @min-[32.5rem]/w:inline">Full</span></span></h3><p class="mt-1 mb-0.5 text-[clamp(26px,10cqi,42px)]/[1.1] font-bold tracking-[-0.02em] tabular-nums">4.6<small class="ml-0.5 text-[0.5em] font-semibold text-tdl08-mut">TB</small></p><span class="text-[11.5px] font-bold text-tdl08-good">▲ 18% this week</span></div>
          <div aria-hidden="true" class="flex h-16 min-w-0 items-end gap-1.5 *:h-(--h) *:flex-1 *:rounded-t-[4px] *:bg-linear-to-t *:from-tdl08-c1/30 *:to-tdl08-c1"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
          <div class="hidden content-center gap-2 @min-[32.5rem]/w:grid"><div aria-hidden="true" class="flex h-1.5 overflow-hidden rounded-full"><i class="w-[62%] bg-tdl08-c1"></i><i class="w-[27%] bg-tdl08-c2"></i><i class="w-[11%] bg-tdl08-c3"></i></div><ul class="grid gap-1.5 text-xs font-semibold text-tdl08-mut [&_i]:size-2.5 [&_i]:rounded-[3px] [&>li]:flex [&>li]:items-center [&>li]:gap-2"><li><i class="bg-tdl08-c1" aria-hidden="true"></i>CDN 62%</li><li><i class="bg-tdl08-c2" aria-hidden="true"></i>API 27%</li><li><i class="bg-tdl08-c3" aria-hidden="true"></i>Media 11%</li></ul></div>
        </div>
      </div>
    </div>
    <div class="@container/w grid w-full max-w-full min-w-60 resize-x content-start gap-2.25 overflow-auto rounded-xl border-r-2 border-dashed border-tdl08-c1/45 pr-3.5 pb-1.5">
      <p class="flex items-center gap-2 text-[10.5px] font-bold tracking-[0.09em] text-tdl08-c1 uppercase"><span aria-hidden="true">⤡</span>Drag my bottom-right corner · breakpoints at 21.25rem and 32.5rem</p>
      <div class="grid gap-3.5 rounded-2xl border border-tdl08-edge bg-tdl08-panel p-4.5 shadow-[0_10px_26px_-20px_var(--color-tdl08-shadow)] @min-[21.25rem]/w:grid-cols-[auto_minmax(0,1fr)] @min-[21.25rem]/w:items-end @min-[32.5rem]/w:grid-cols-[auto_minmax(0,1fr)_9rem]">
        <div class="@min-[21.25rem]/w:self-center @min-[21.25rem]/w:pr-2"><h3 class="flex items-center gap-2 text-[11px] font-semibold tracking-[0.11em] text-tdl08-mut uppercase">Bandwidth<span class="rounded-full bg-tdl08-c1/12 px-1.75 py-0.5 text-[9.5px] tracking-[0.06em] text-tdl08-c1"><span class="@min-[21.25rem]/w:hidden">Stacked</span><span class="hidden @min-[21.25rem]/w:inline @min-[32.5rem]/w:hidden">Split</span><span class="hidden @min-[32.5rem]/w:inline">Full</span></span></h3><p class="mt-1 mb-0.5 text-[clamp(26px,10cqi,42px)]/[1.1] font-bold tracking-[-0.02em] tabular-nums">4.6<small class="ml-0.5 text-[0.5em] font-semibold text-tdl08-mut">TB</small></p><span class="text-[11.5px] font-bold text-tdl08-good">▲ 18% this week</span></div>
        <div aria-hidden="true" class="flex h-16 min-w-0 items-end gap-1.5 *:h-(--h) *:flex-1 *:rounded-t-[4px] *:bg-linear-to-t *:from-tdl08-c1/30 *:to-tdl08-c1"><i style="--h:35%"></i><i style="--h:55%"></i><i style="--h:42%"></i><i style="--h:68%"></i><i style="--h:58%"></i><i style="--h:80%"></i><i style="--h:72%"></i><i style="--h:95%"></i></div>
        <div class="hidden content-center gap-2 @min-[32.5rem]/w:grid"><div aria-hidden="true" class="flex h-1.5 overflow-hidden rounded-full"><i class="w-[62%] bg-tdl08-c1"></i><i class="w-[27%] bg-tdl08-c2"></i><i class="w-[11%] bg-tdl08-c3"></i></div><ul class="grid gap-1.5 text-xs font-semibold text-tdl08-mut [&_i]:size-2.5 [&_i]:rounded-[3px] [&>li]:flex [&>li]:items-center [&>li]:gap-2"><li><i class="bg-tdl08-c1" aria-hidden="true"></i>CDN 62%</li><li><i class="bg-tdl08-c2" aria-hidden="true"></i>API 27%</li><li><i class="bg-tdl08-c3" aria-hidden="true"></i>Media 11%</li></ul></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdl08-bg: #f7f6fb;
  --color-tdl08-bg: oklch(0.975 0.006 290);
  --color-tdl08-bg2: #eeedf6;
  --color-tdl08-bg2: oklch(0.95 0.01 290);
  --color-tdl08-panel: #ffffff;
  --color-tdl08-panel: oklch(1 0 0);
  --color-tdl08-edge: #e2e0ec;
  --color-tdl08-edge: oklch(0.91 0.012 290);
  --color-tdl08-ink: #27243a;
  --color-tdl08-ink: oklch(0.27 0.03 290);
  --color-tdl08-mut: #5d5a70;
  --color-tdl08-mut: oklch(0.49 0.03 290);
  --color-tdl08-c1: #7046d8;
  --color-tdl08-c1: oklch(0.53 0.2 292);
  --color-tdl08-c2: #3aa3d6;
  --color-tdl08-c2: oklch(0.68 0.12 230);
  --color-tdl08-c3: #e2b93a;
  --color-tdl08-c3: oklch(0.8 0.14 90);
  --color-tdl08-good: #187d4b;
  --color-tdl08-good: oklch(0.52 0.13 155);
  --color-tdl08-shadow: #6a5aa0;
  --color-tdl08-shadow: oklch(0.45 0.08 290 / 0.55);
  --font-tdl08-sans: 'Sora', system-ui, sans-serif;
}

.tdl-08 {
  width: 100%;
  min-height: 100svh;
}
```
