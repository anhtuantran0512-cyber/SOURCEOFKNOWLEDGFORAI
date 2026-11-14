---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-pie-chart-navigation-menu-with-conic-gradient/"
title: "Tailwind CSS Pie Chart Navigation Menu with Conic Gradient"
section: "navigation"
category: "tailwind-css-circular-menus"
category_name: "Tailwind CSS Circular Menus"
description: "A pie chart that is the menu: four budget categories drawn as proportional slices, each a real <button> clipped to its wedge, so the chart is clickable,…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pie Chart Navigation Menu with Conic Gradient
Source: https://codefronts.com/navigation/tailwind-css-circular-menus/tailwind-css-pie-chart-navigation-menu-with-conic-gradient/

A pie chart that is the menu: four budget categories drawn as proportional slices, each a real <button> clipped to its wedge, so the chart is clickable, tabbable and announced (&ldquo;Housing, 38 percent of budget&rdquo;). The pressed slice slides out along its bisector with aria-pressed:tcm12-lift, a donut hole carries the total, and the detail panel updates from data attributes.
## HTML
```html
<section class="tcm-12 w-full min-h-svh grid place-items-center bg-tcm12-bg bg-[radial-gradient(55%_50%_at_30%_40%,var(--color-tcm12-glow),transparent_72%)] px-4 py-14 font-tcm12-sans text-tcm12-ink antialiased sm:px-5" aria-label="Pie chart navigation menu demo">
  <div id="tcm-12-budget" class="grid w-full max-w-[46rem] justify-items-center gap-7">
    <header class="grid w-full gap-1">
      <p class="font-tcm12-mono text-[11px] tracking-[0.14em] text-tcm12-mut uppercase">October budget · $4,800</p>
      <h2 class="text-[clamp(1.4rem,3.6vw,1.85rem)] font-semibold tracking-[-0.03em]">Where the money goes</h2>
    </header>
    <div class="grid w-full items-center gap-8 rounded-[1.75rem] bg-tcm12-card p-6 shadow-tcm12-card ring-1 ring-tcm12-line sm:grid-cols-[auto_1fr] sm:p-8">
      <div class="relative mx-auto size-[min(16.5rem,72vw)]" role="group" aria-label="Budget categories">
        <div aria-hidden="true" class="absolute inset-0 rounded-full bg-[conic-gradient(var(--color-tcm12-c1)_0%_38%,var(--color-tcm12-c2)_38%_65%,var(--color-tcm12-c3)_65%_87%,var(--color-tcm12-c4)_87%_100%)] opacity-15 blur-xl"></div>
        <div class="absolute inset-0">
          <button type="button" data-slice data-label="Housing" data-amt="$1,824" data-pct="38" data-c="c1" aria-pressed="true" aria-label="Housing, 38 percent of budget" style="clip-path:polygon(50% 50%,50.0% 0.0%,54.0% 0.2%,57.9% 0.6%,61.8% 1.4%,65.6% 2.5%,69.4% 3.9%,73.0% 5.6%,76.4% 7.6%,79.7% 9.8%,82.8% 12.3%,85.7% 15.0%,88.4% 18.0%,90.8% 21.1%,93.0% 24.5%,94.9% 28.0%,96.5% 31.6%,97.8% 35.3%,98.8% 39.2%,99.5% 43.1%,99.9% 47.1%,100.0% 51.0%,99.7% 55.0%,99.2% 59.0%,98.3% 62.8%,97.1% 66.6%,95.7% 70.3%,93.9% 73.9%,91.9% 77.3%,89.6% 80.6%,87.0% 83.6%,84.2% 86.4%)" class="absolute inset-0 cursor-pointer rounded-full bg-tcm12-c1 [--a:-21.6deg] transition-[translate,filter] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] hover:tcm12-lift-sm aria-pressed:tcm12-lift aria-pressed:drop-shadow-[0_10px_14px_oklch(0.3_0.1_265/0.35)] focus-visible:brightness-110 focus-visible:tcm12-lift-sm motion-reduce:transition-none"></button>
          <button type="button" data-slice data-label="Food &amp; dining" data-amt="$1,296" data-pct="27" data-c="c2" aria-pressed="false" aria-label="Food &amp; dining, 27 percent of budget" style="clip-path:polygon(50% 50%,84.2% 86.4%,82.1% 88.3%,79.9% 90.1%,77.6% 91.7%,75.2% 93.2%,72.7% 94.6%,70.1% 95.8%,67.5% 96.8%,64.9% 97.7%,62.1% 98.5%,59.4% 99.1%,56.6% 99.6%,53.8% 99.9%,50.9% 100.0%,48.1% 100.0%,45.3% 99.8%,42.5% 99.4%,39.7% 98.9%,37.0% 98.3%,34.3% 97.5%,31.6% 96.5%,29.0% 95.4%,26.5% 94.1%,24.0% 92.7%,21.6% 91.2%,19.4% 89.5%,17.2% 87.7%,15.1% 85.8%,13.1% 83.8%,11.3% 81.6%,9.5% 79.4%)" class="absolute inset-0 cursor-pointer rounded-full bg-tcm12-c2 [--a:95.4deg] transition-[translate,filter] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] hover:tcm12-lift-sm aria-pressed:tcm12-lift aria-pressed:drop-shadow-[0_10px_14px_oklch(0.3_0.1_265/0.35)] focus-visible:brightness-110 focus-visible:tcm12-lift-sm motion-reduce:transition-none"></button>
          <button type="button" data-slice data-label="Transport" data-amt="$1,056" data-pct="22" data-c="c3" aria-pressed="false" aria-label="Transport, 22 percent of budget" style="clip-path:polygon(50% 50%,9.5% 79.4%,8.2% 77.5%,7.0% 75.5%,5.9% 73.5%,4.8% 71.5%,3.9% 69.4%,3.1% 67.2%,2.3% 65.1%,1.7% 62.8%,1.1% 60.6%,0.7% 58.3%,0.4% 56.1%,0.1% 53.8%,0.0% 51.5%,0.0% 49.2%,0.1% 46.9%,0.3% 44.6%,0.6% 42.3%,1.0% 40.0%,1.5% 37.8%,2.1% 35.5%,2.9% 33.4%,3.7% 31.2%,4.6% 29.1%,5.6% 27.0%,6.7% 25.0%,7.9% 23.0%,9.2% 21.1%,10.6% 19.3%,12.0% 17.5%,13.6% 15.8%)" class="absolute inset-0 cursor-pointer rounded-full bg-tcm12-c3 [--a:183.6deg] transition-[translate,filter] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] hover:tcm12-lift-sm aria-pressed:tcm12-lift aria-pressed:drop-shadow-[0_10px_14px_oklch(0.3_0.1_265/0.35)] focus-visible:brightness-110 focus-visible:tcm12-lift-sm motion-reduce:transition-none"></button>
          <button type="button" data-slice data-label="Savings" data-amt="$624" data-pct="13" data-c="c4" aria-pressed="false" aria-label="Savings, 13 percent of budget" style="clip-path:polygon(50% 50%,13.6% 15.8%,14.5% 14.8%,15.5% 13.8%,16.5% 12.9%,17.5% 12.0%,18.5% 11.1%,19.6% 10.3%,20.7% 9.5%,21.8% 8.7%,22.9% 8.0%,24.1% 7.2%,25.3% 6.5%,26.5% 5.9%,27.7% 5.3%,28.9% 4.7%,30.1% 4.1%,31.4% 3.6%,32.7% 3.1%,34.0% 2.6%,35.2% 2.2%,36.6% 1.8%,37.9% 1.5%,39.2% 1.2%,40.5% 0.9%,41.9% 0.7%,43.2% 0.5%,44.6% 0.3%,45.9% 0.2%,47.3% 0.1%,48.6% 0.0%,50.0% 0.0%)" class="absolute inset-0 cursor-pointer rounded-full bg-tcm12-c4 [--a:246.6deg] transition-[translate,filter] duration-300 ease-[cubic-bezier(.34,1.45,.5,1)] hover:tcm12-lift-sm aria-pressed:tcm12-lift aria-pressed:drop-shadow-[0_10px_14px_oklch(0.3_0.1_265/0.35)] focus-visible:brightness-110 focus-visible:tcm12-lift-sm motion-reduce:transition-none"></button>
        </div>
        <span aria-hidden="true" class="pointer-events-none absolute inset-[34%] grid place-content-center rounded-full bg-tcm12-card text-center shadow-tcm12-hole"><b class="text-[11px] font-semibold tracking-[0.12em] text-tcm12-mut uppercase">Total</b><b class="text-[17px] tabular-nums">$4,800</b></span>
      </div>
      <aside class="grid gap-5" aria-live="polite">
        <div class="grid gap-1.5">
          <p data-cat class="text-[12px] font-semibold tracking-[0.14em] text-tcm12-mut uppercase">Housing</p>
          <p class="text-[2.4rem] leading-none font-bold tracking-[-0.03em] tabular-nums"><span data-amt>$1,824</span><span class="text-base font-medium text-tcm12-mut">/mo</span></p>
          <p data-share class="text-[13.5px] text-tcm12-mut">38% of monthly budget</p>
          <div class="mt-1.5 h-2 overflow-hidden rounded-full bg-tcm12-sunk"><i data-bar class="block h-full w-[38%] rounded-full bg-tcm12-c1 transition-[width,background-color] duration-500 ease-[cubic-bezier(.16,1,.3,1)]"></i></div>
        </div>
        <ul class="grid gap-2 border-t border-tcm12-line pt-4">
            <li class="flex items-center gap-2.5 text-[13px]"><span aria-hidden="true" class="size-2.5 rounded-full bg-tcm12-c1"></span><span class="flex-1 text-tcm12-mut">Housing</span><span class="font-semibold tabular-nums">38%</span></li>
            <li class="flex items-center gap-2.5 text-[13px]"><span aria-hidden="true" class="size-2.5 rounded-full bg-tcm12-c2"></span><span class="flex-1 text-tcm12-mut">Food &amp; dining</span><span class="font-semibold tabular-nums">27%</span></li>
            <li class="flex items-center gap-2.5 text-[13px]"><span aria-hidden="true" class="size-2.5 rounded-full bg-tcm12-c3"></span><span class="flex-1 text-tcm12-mut">Transport</span><span class="font-semibold tabular-nums">22%</span></li>
            <li class="flex items-center gap-2.5 text-[13px]"><span aria-hidden="true" class="size-2.5 rounded-full bg-tcm12-c4"></span><span class="flex-1 text-tcm12-mut">Savings</span><span class="font-semibold tabular-nums">13%</span></li>
        </ul>
      </aside>
    </div>
    <p aria-hidden="true" class="max-w-full rounded-full bg-tcm12-card px-3.5 py-2 text-center font-tcm12-mono text-[11.5px] text-tcm12-mut ring-1 ring-tcm12-line ">conic-gradient(…) · clip-path:polygon hit slices · aria-pressed:tcm12-lift</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcm12-bg: #f4f5fb;
  --color-tcm12-bg: oklch(0.971 0.008 278.6);
  --color-tcm12-glow: #e0e7ffb3;
  --color-tcm12-glow: oklch(0.93 0.033 272.8 / 0.7);
  --color-tcm12-card: #ffffff;
  --color-tcm12-card: oklch(1 0 0);
  --color-tcm12-sunk: #eef0f7;
  --color-tcm12-sunk: oklch(0.956 0.01 273.4);
  --color-tcm12-ink: #141a33;
  --color-tcm12-ink: oklch(0.226 0.049 271.8);
  --color-tcm12-mut: #565d78;
  --color-tcm12-mut: oklch(0.483 0.044 273.3);
  --color-tcm12-line: #e3e6f1;
  --color-tcm12-line: oklch(0.926 0.015 273.8);
  --color-tcm12-c1: #4f46e5;
  --color-tcm12-c1: oklch(0.511 0.23 277);
  --color-tcm12-c2: #0891b2;
  --color-tcm12-c2: oklch(0.609 0.111 221.7);
  --color-tcm12-c3: #f59e0b;
  --color-tcm12-c3: oklch(0.769 0.165 70.1);
  --color-tcm12-c4: #db2777;
  --color-tcm12-c4: oklch(0.592 0.218 0.6);
  --font-tcm12-sans: 'Geist', system-ui, sans-serif;
  --font-tcm12-mono: 'Geist Mono', ui-monospace, monospace;
  --shadow-tcm12-card: 0 1px 2px oklch(0.3 0.08 270 / 0.06), 0 28px 60px -28px oklch(0.4 0.15 270 / 0.35);
  --shadow-tcm12-hole: 0 0 0 6px oklch(1 0 0 / 0.06), inset 0 2px 8px oklch(0.3 0.08 270 / 0.12);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcm-12 {
  width: 100%;
  min-height: 100svh;
}
/* A slice slides out along its own bisector; --a is set per slice in the markup. */

@utility tcm12-lift {
  translate: calc(cos(var(--a)) * 12px) calc(sin(var(--a)) * 12px);
}

@utility tcm12-lift-sm {
  translate: calc(cos(var(--a)) * 5px) calc(sin(var(--a)) * 5px);
}
/* Dark theme: midnight ledger: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tcm-12:not([data-theme="light"]) {
    color-scheme: dark;
    --color-tcm12-bg: #0b0d18;
    --color-tcm12-bg: oklch(0.163 0.023 275.6);
    --color-tcm12-glow: #312e8166;
    --color-tcm12-glow: oklch(0.359 0.135 278.7 / 0.4);
    --color-tcm12-card: #141728;
    --color-tcm12-card: oklch(0.211 0.034 275.5);
    --color-tcm12-sunk: #1e2238;
    --color-tcm12-sunk: oklch(0.259 0.042 275.2);
    --color-tcm12-ink: #eef0fb;
    --color-tcm12-ink: oklch(0.957 0.015 277.9);
    --color-tcm12-mut: #a5abc8;
    --color-tcm12-mut: oklch(0.746 0.042 276.1);
    --color-tcm12-line: #262b44;
    --color-tcm12-line: oklch(0.297 0.046 274.6);
    --color-tcm12-c1: #818cf8;
    --color-tcm12-c1: oklch(0.68 0.158 276.9);
    --color-tcm12-c2: #22d3ee;
    --color-tcm12-c2: oklch(0.797 0.134 211.5);
    --color-tcm12-c3: #fbbf24;
    --color-tcm12-c3: oklch(0.837 0.164 84.4);
    --color-tcm12-c4: #f472b6;
    --color-tcm12-c4: oklch(0.725 0.175 349.8);
  }
}

.tcm-12[data-theme="dark"] {
  color-scheme: dark;
  --color-tcm12-bg: #0b0d18;
  --color-tcm12-bg: oklch(0.163 0.023 275.6);
  --color-tcm12-glow: #312e8166;
  --color-tcm12-glow: oklch(0.359 0.135 278.7 / 0.4);
  --color-tcm12-card: #141728;
  --color-tcm12-card: oklch(0.211 0.034 275.5);
  --color-tcm12-sunk: #1e2238;
  --color-tcm12-sunk: oklch(0.259 0.042 275.2);
  --color-tcm12-ink: #eef0fb;
  --color-tcm12-ink: oklch(0.957 0.015 277.9);
  --color-tcm12-mut: #a5abc8;
  --color-tcm12-mut: oklch(0.746 0.042 276.1);
  --color-tcm12-line: #262b44;
  --color-tcm12-line: oklch(0.297 0.046 274.6);
  --color-tcm12-c1: #818cf8;
  --color-tcm12-c1: oklch(0.68 0.158 276.9);
  --color-tcm12-c2: #22d3ee;
  --color-tcm12-c2: oklch(0.797 0.134 211.5);
  --color-tcm12-c3: #fbbf24;
  --color-tcm12-c3: oklch(0.837 0.164 84.4);
  --color-tcm12-c4: #f472b6;
  --color-tcm12-c4: oklch(0.725 0.175 349.8);
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('tcm-12-budget');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const slices = [...root.querySelectorAll('[data-slice]')];
  const $ = (s) => root.querySelector(s);
  slices.forEach((b) => b.addEventListener('click', () => {
    slices.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    $('[data-cat]').textContent = b.dataset.label;
    $('[data-amt]').textContent = b.dataset.amt;
    $('[data-share]').textContent = b.dataset.pct + '% of monthly budget';
    const bar = $('[data-bar]');
    bar.style.width = b.dataset.pct + '%';
    bar.style.backgroundColor = 'var(--color-tcm12-' + b.dataset.c + ')';
  }));
})();
```
