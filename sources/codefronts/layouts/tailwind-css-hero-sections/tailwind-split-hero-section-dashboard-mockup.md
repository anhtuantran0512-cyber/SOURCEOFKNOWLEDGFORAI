---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-split-hero-section-dashboard-mockup/"
title: "Tailwind CSS Split Hero Section with Dashboard Mockup"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Two-column hero — copy left, a pure-HTML analytics dashboard right, with KPI tiles, bars that grow on load and an SVG trend line that draws itself."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Split Hero Section with Dashboard Mockup
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-split-hero-section-dashboard-mockup/

Two-column hero — copy left, a pure-HTML analytics dashboard right, with KPI tiles, bars that grow on load and an SVG trend line that draws itself. Rust and ochre on deep workshop brown with hard offset shadows. No images, no JS.
## HTML
```html
<section class="ths-02 grid w-full min-h-svh items-center gap-12 bg-ths02-bg bg-[radial-gradient(70%_60%_at_100%_0%,var(--color-ths02-glow),transparent_70%)] px-5 py-16 font-ths02-sans text-ths02-ink sm:px-12 lg:grid-cols-[1.05fr_1fr] lg:gap-16" aria-label="Split hero with dashboard mockup">
  <div class="max-w-xl">
    <span class="inline-block border border-ths02-acc px-2.5 py-1 font-ths02-mono text-[11px] font-bold tracking-[0.2em] text-ths02-acc">EST. 2024</span>
    <h1 class="mt-5 font-ths02-serif text-[clamp(36px,5.4vw,62px)] leading-[1.02] font-extrabold tracking-[-0.02em] text-balance text-ths02-cream">Inventory that <em class="font-bold text-ths02-acc">actually adds up.</em></h1>
    <p class="mt-5 max-w-md text-base/relaxed text-ths02-body">Stock, batches, suppliers — one ledger, no spreadsheets, no Sundays at the laptop.</p>
    <div class="mt-8 flex flex-wrap items-center gap-5">
      <a href="#start" class="inline-flex min-h-12 items-center gap-2 bg-ths02-acc px-6 text-sm font-bold text-ths02-bg shadow-[4px_4px_0_var(--color-ths02-deep)] transition hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[2px_2px_0_var(--color-ths02-deep)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths02-acc motion-reduce:transition-none">Get started →</a>
      <a href="#demo" class="inline-flex min-h-11 items-center text-sm font-semibold text-ths02-cream underline decoration-ths02-acc decoration-2 underline-offset-[6px] hover:text-ths02-acc focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths02-acc">Book a demo</a>
    </div>
    <dl class="mt-10 flex gap-8 border-t border-dashed border-ths02-line pt-6 font-ths02-mono text-xs text-ths02-body">
      <div><dt>SKUs tracked</dt><dd class="mt-1 text-xl font-bold text-ths02-cream">1.2M</dd></div>
      <div><dt>Avg. setup</dt><dd class="mt-1 text-xl font-bold text-ths02-cream">11 min</dd></div>
    </dl>
  </div>
  <div aria-hidden="true" class="rounded-md border-2 border-ths02-line bg-ths02-panel p-4 shadow-[8px_8px_0_var(--color-ths02-acc)] sm:p-5">
    <div class="flex items-center gap-1.5 border-b border-dashed border-ths02-line pb-3">
      <span class="size-2.5 rounded-full bg-ths02-acc"></span><span class="size-2.5 rounded-full bg-ths02-ochre"></span><span class="size-2.5 rounded-full bg-ths02-line"></span>
      <span class="ml-auto font-ths02-mono text-[10px] tracking-[0.14em] text-ths02-body">LEDGER / Q3</span>
    </div>
    <div class="mt-4 grid grid-cols-3 gap-2.5">
      <div class="rounded-sm border border-ths02-line p-2.5"><p class="font-ths02-mono text-[10px] text-ths02-body">On hand</p><p class="mt-1 text-lg font-bold text-ths02-cream">8,412</p></div>
      <div class="rounded-sm border border-ths02-line p-2.5"><p class="font-ths02-mono text-[10px] text-ths02-body">Reorder</p><p class="mt-1 text-lg font-bold text-ths02-acc">23</p></div>
      <div class="rounded-sm border border-ths02-line p-2.5"><p class="font-ths02-mono text-[10px] text-ths02-body">Margin</p><p class="mt-1 text-lg font-bold text-ths02-ochre">+18%</p></div>
    </div>
    <div class="mt-4 grid h-36 grid-cols-6 items-end gap-2">
      <span class="h-[32%] rounded-t-sm bg-linear-to-b from-ths02-acc to-ths02-deep transition-[height] duration-700 starting:h-0"></span>
      <span class="h-[64%] rounded-t-sm bg-linear-to-b from-ths02-ochre to-ths02-olive transition-[height] delay-75 duration-700 starting:h-0"></span>
      <span class="h-[48%] rounded-t-sm bg-linear-to-b from-ths02-acc to-ths02-deep transition-[height] delay-150 duration-700 starting:h-0"></span>
      <span class="h-[88%] rounded-t-sm bg-linear-to-b from-ths02-ochre to-ths02-olive transition-[height] delay-200 duration-700 starting:h-0"></span>
      <span class="h-[56%] rounded-t-sm bg-linear-to-b from-ths02-acc to-ths02-deep transition-[height] delay-300 duration-700 starting:h-0"></span>
      <span class="h-[72%] rounded-t-sm bg-linear-to-b from-ths02-ochre to-ths02-olive transition-[height] delay-500 duration-700 starting:h-0"></span>
    </div>
    <svg viewBox="0 0 200 60" preserveAspectRatio="none" class="mt-3 h-16 w-full"><path d="M0,40 Q40,20 80,30 T160,15 T200,20" fill="none" stroke="currentColor" stroke-width="2.5" vector-effect="non-scaling-stroke" class="text-ths02-acc [stroke-dasharray:400] [stroke-dashoffset:0] transition-[stroke-dashoffset] delay-300 duration-[1600ms] ease-out starting:[stroke-dashoffset:400] motion-reduce:transition-none"/></svg>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths02-bg: #2c1f15;
  --color-ths02-bg: oklch(0.252 0.027 58.7);
  --color-ths02-glow: #4a2c18;
  --color-ths02-glow: oklch(0.326 0.055 53.3);
  --color-ths02-panel: #1a120a;
  --color-ths02-panel: oklch(0.19 0.02 66.1);
  --color-ths02-ink: #f5e6d3;
  --color-ths02-ink: oklch(0.932 0.03 73.9);
  --color-ths02-cream: #fff8ed;
  --color-ths02-cream: oklch(0.982 0.016 79.4);
  --color-ths02-body: #cdb9a4;
  --color-ths02-body: oklch(0.797 0.037 68.6);
  --color-ths02-line: #6b4427;
  --color-ths02-line: oklch(0.425 0.069 56.2);
  --color-ths02-acc: #d97742;
  --color-ths02-acc: oklch(0.67 0.14 47.4);
  --color-ths02-deep: #8a4520;
  --color-ths02-deep: oklch(0.47 0.106 46.5);
  --color-ths02-ochre: #c9a24a;
  --color-ths02-ochre: oklch(0.731 0.115 85.2);
  --color-ths02-olive: #8a6c1f;
  --color-ths02-olive: oklch(0.547 0.099 86.4);
  --font-ths02-serif: 'Playfair Display', Georgia, serif;
  --font-ths02-sans: 'Geist', system-ui, sans-serif;
  --font-ths02-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-02 {
  width: 100%;
  min-height: 100svh;
}
```
