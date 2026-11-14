---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-dashboard-metric-card/"
title: "Tailwind Minimalist Dashboard Card and Metric"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "Two KPI cards reduced to what a glance needs: label, value, direction, trend, and one way out."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Minimalist Dashboard Card and Metric
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-minimalist-dashboard-metric-card/

Two KPI cards reduced to what a glance needs: label, value, direction, trend, and one way out. The value is set in tabular monospace at a fluid clamp() size, the delta is a pill carrying an arrow and a word so direction never relies on green or red, and the sparkline is a vector-effect: non-scaling-stroke SVG that keeps a crisp 1.75px line at any width.
## HTML
```html
<section class="tmu-15 relative w-full min-h-svh bg-tmu15-bg font-tmu15-ui text-tmu15-ink antialiased" aria-labelledby="tmu15-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu15-theme" type="checkbox" class="peer sr-only">
    <label for="tmu15-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu15-line bg-tmu15-surface text-tmu15-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu15-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu15-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[60rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu15-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu15-ink-2"><span class="tabular-nums text-tmu15-acc">15</span><span aria-hidden="true" class="h-px w-6 bg-tmu15-line"></span>Metric card</p>
      <h2 id="tmu15-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">A number, a direction, a trend &mdash; nothing else</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu15-ink-2 text-pretty">Everything a glance needs and one way to go deeper. Direction is carried by an arrow and a word, never by green and red alone.</p>
    </header>
    <div class="grid gap-5 grid-cols-[repeat(auto-fit,minmax(min(100%,17rem),1fr))]">
      <article aria-labelledby="tmu15-m1" class="group grid min-w-0 content-start gap-3 rounded-2xl border-t border-tmu15-edge bg-tmu15-surface p-6 transition-colors duration-200 hover:bg-tmu15-surface-hi md:p-7 motion-reduce:transition-none">
        <header class="flex min-w-0 items-start justify-between gap-3">
          <div class="grid min-w-0 gap-0.5"><h3 id="tmu15-m1" class="text-[0.8125rem] font-medium uppercase tracking-[0.06em] text-tmu15-ink-2">Monthly recurring revenue</h3><p class="text-xs text-tmu15-ink-2">Meridian &middot; all regions</p></div>
          <p class="inline-flex flex-none items-center gap-1 rounded-full bg-tmu15-up-bg text-tmu15-up px-2 py-1 text-xs font-semibold tabular-nums"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 19V5m0 0-6 6m6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>4.2%<span class="sr-only"> vs last month</span></p>
        </header>
        <p class="font-tmu15-mono text-[clamp(2.25rem,1.7rem+2.4vw,3rem)] font-semibold leading-[1.02] tracking-[-0.03em] tabular-nums">$281,440</p>
        <p class="text-[0.8125rem] text-tmu15-ink-2">vs last month</p>
        <div class="mt-1 aspect-[240/64] min-w-0 text-tmu15-up">
          <svg class="block size-full overflow-visible" viewBox="0 0 240 64" preserveAspectRatio="none" role="img" aria-label="Twelve-month trend, rising from 214,000 to 281,440">
            <path d="M0 52 20 49 40 51 60 44 80 46 100 38 120 34 140 36 160 27 180 22 200 24 220 14 240 10 240 64 0 64Z" fill="currentColor" opacity="0.08"/>
            <path d="M0 52 20 49 40 51 60 44 80 46 100 38 120 34 140 36 160 27 180 22 200 24 220 14 240 10" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
          </svg>
        </div>
        <footer class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tmu15-line pt-3">
          <p class="text-xs text-tmu15-ink-2">Updated 6 min ago</p>
          <a href="#tmu15-title" class="inline-flex min-h-11 items-center gap-1 text-[0.8125rem] font-semibold text-tmu15-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu15-acc motion-reduce:transition-none">Full report<svg class="size-3.5 transition-transform duration-150 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </footer>
      </article>
      <article aria-labelledby="tmu15-m2" class="group grid min-w-0 content-start gap-3 rounded-2xl border-t border-tmu15-edge bg-tmu15-surface p-6 transition-colors duration-200 hover:bg-tmu15-surface-hi md:p-7 motion-reduce:transition-none">
        <header class="flex min-w-0 items-start justify-between gap-3">
          <div class="grid min-w-0 gap-0.5"><h3 id="tmu15-m2" class="text-[0.8125rem] font-medium uppercase tracking-[0.06em] text-tmu15-ink-2">Net revenue retention</h3><p class="text-xs text-tmu15-ink-2">Rolling 12 months</p></div>
          <p class="inline-flex flex-none items-center gap-1 rounded-full bg-tmu15-down-bg text-tmu15-down px-2 py-1 text-xs font-semibold tabular-nums"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14m0 0 6-6m-6 6-6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>0.6pt<span class="sr-only"> vs last quarter</span></p>
        </header>
        <p class="font-tmu15-mono text-[clamp(2.25rem,1.7rem+2.4vw,3rem)] font-semibold leading-[1.02] tracking-[-0.03em] tabular-nums">104.8%</p>
        <p class="text-[0.8125rem] text-tmu15-ink-2">vs last quarter</p>
        <div class="mt-1 aspect-[240/64] min-w-0 text-tmu15-ink-2">
          <svg class="block size-full overflow-visible" viewBox="0 0 240 64" preserveAspectRatio="none" role="img" aria-label="Rolling retention, flat then easing from 106.1 to 104.8 percent">
            <path d="M0 22 20 20 40 24 60 21 80 26 100 24 120 29 140 27 160 33 180 31 200 36 220 34 240 39 240 64 0 64Z" fill="currentColor" opacity="0.08"/>
            <path d="M0 22 20 20 40 24 60 21 80 26 100 24 120 29 140 27 160 33 180 31 200 36 220 34 240 39" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
          </svg>
        </div>
        <footer class="flex flex-wrap items-center justify-between gap-x-4 gap-y-2 border-t border-tmu15-line pt-3">
          <p class="text-xs text-tmu15-ink-2">Cohort model v4</p>
          <a href="#tmu15-title" class="inline-flex min-h-11 items-center gap-1 text-[0.8125rem] font-semibold text-tmu15-acc underline decoration-transparent underline-offset-4 transition-[text-decoration-color] duration-150 hover:decoration-current focus-visible:rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tmu15-acc motion-reduce:transition-none">Full report<svg class="size-3.5 transition-transform duration-150 group-hover:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></a>
        </footer>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu15-bg: light-dark(#f4f5f7, #08090b);
  --color-tmu15-bg: light-dark(oklch(96.5% 0.003 250), oklch(13% 0.004 250));
  --color-tmu15-surface: light-dark(#ffffff, #12151a);
  --color-tmu15-surface: light-dark(oklch(100% 0 0), oklch(19% 0.006 250));
  --color-tmu15-edge: light-dark(#dfe3e7, #262c33);
  --color-tmu15-edge: light-dark(oklch(89% 0.005 250), oklch(27% 0.008 250));
  --color-tmu15-ink: light-dark(#12151a, #f3f5f7);
  --color-tmu15-ink: light-dark(oklch(19% 0.006 250), oklch(96.5% 0.003 250));
  --color-tmu15-ink-2: light-dark(#4e575f, #a2abb3);
  --color-tmu15-ink-2: light-dark(oklch(45% 0.012 250), oklch(74% 0.008 250));
  --color-tmu15-line: light-dark(#e5e8eb, #232a30);
  --color-tmu15-line: light-dark(oklch(92% 0.004 250), oklch(25.5% 0.008 250));
  --color-tmu15-up: light-dark(#14663f, #63d19b);
  --color-tmu15-up: light-dark(oklch(43% 0.11 158), oklch(80% 0.13 158));
  --color-tmu15-down: light-dark(#9c3f1c, #f0a58a);
  --color-tmu15-down: light-dark(oklch(45% 0.13 40), oklch(79% 0.11 40));
  --color-tmu15-acc: light-dark(#144aa8, #7fb4ff);
  --color-tmu15-acc: light-dark(oklch(42% 0.16 262), oklch(79% 0.13 260));
  --color-tmu15-up-bg: color-mix(in oklab, var(--color-tmu15-up) 14%, transparent);
  --color-tmu15-down-bg: color-mix(in oklab, var(--color-tmu15-down) 14%, transparent);
  --color-tmu15-surface-hi: color-mix(in oklab, var(--color-tmu15-surface) 94%, var(--color-tmu15-ink));
  --font-tmu15-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu15-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-15:has(#tmu15-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-15:has(#tmu15-theme:checked) {
    color-scheme: light;
  }
}
```
