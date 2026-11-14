---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-grayscale-palette-contrast-ratio/"
title: "Tailwind Grayscale Palette with Enough Contrast"
section: "design-styles"
category: "tailwind-css-minimalist-ui"
category_name: "Tailwind CSS Minimalist UI"
description: "A ten-step neutral ramp with its measured contrast ratio printed against the active surface, and a verdict per step."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Grayscale Palette with Enough Contrast
Source: https://codefronts.com/design-styles/tailwind-css-minimalist-ui/tailwind-grayscale-palette-contrast-ratio/

A ten-step neutral ramp with its measured contrast ratio printed against the active surface, and a verdict per step. Flip the theme and every ratio, verdict and the 4.5:1 floor marker swaps &mdash; driven by a custom tmu10-dark: variant that knows about both the OS preference and the toggle, so the table is honest in all four combinations.
## HTML
```html
<section class="tmu-10 relative w-full min-h-svh bg-tmu10-bg font-tmu10-ui text-tmu10-ink antialiased" aria-labelledby="tmu10-title">
  <div class="absolute top-4 right-4 z-10">
    <input id="tmu10-theme" type="checkbox" class="peer sr-only">
    <label for="tmu10-theme" class="grid size-11 cursor-pointer place-items-center rounded-full border border-tmu10-line bg-tmu10-bg text-tmu10-ink-2 shadow-[0_1px_2px_rgb(0_0_0/0.06)] transition-[color,rotate] duration-300 hover:text-tmu10-ink peer-checked:rotate-180 peer-focus-visible:outline-2 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tmu10-acc motion-reduce:transition-none">
      <svg class="size-5" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="sr-only">Switch colour theme</span>
    </label>
  </div>
  <div class="mx-auto grid max-w-[64rem] gap-10 px-5 pt-20 pb-20 md:px-12">
    <header class="grid max-w-[62ch] gap-3">
      <p class="inline-flex items-center gap-2.5 font-tmu10-mono text-xs font-medium uppercase tracking-[0.14em] text-tmu10-ink-2"><span class="tabular-nums text-tmu10-acc">10</span><span aria-hidden="true" class="h-px w-6 bg-tmu10-line"></span>Contrast</p>
      <h2 id="tmu10-title" class="text-[clamp(1.75rem,1.2rem+2vw,2.75rem)] font-semibold leading-[1.08] tracking-[-0.03em] text-balance">A grey is only minimal if it can be read</h2>
      <p class="text-[1.0625rem] leading-relaxed text-tmu10-ink-2 text-pretty">Every step of the ramp, measured against the surface you are looking at right now. Switch the theme &mdash; the ratios, verdicts and the floor move with it.</p>
    </header>
    <div role="table" aria-labelledby="tmu10-cap" class="grid min-w-0 border-t border-tmu10-line">
      <p id="tmu10-cap" class="py-3 font-tmu10-mono text-xs text-tmu10-ink-2"><span class="tmu10-dark:hidden">Ratios against the light surface #ffffff</span><span class="hidden tmu10-dark:inline">Ratios against the dark surface #14171a</span></p>
      <div role="row" class="grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-2.5 font-tmu10-mono text-[0.6875rem] uppercase tracking-[0.1em] text-tmu10-ink-2">
        <span role="columnheader">Step</span><span role="columnheader">Swatch</span><span role="columnheader">Sample</span><span role="columnheader" class="text-right">Ratio</span><span role="columnheader" class="col-[3/-1] sm:col-auto sm:justify-self-end">Verdict</span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">050</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t050"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t050">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">1.07:1</b><b class="hidden font-medium tmu10-dark:inline">16.28:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Surface only</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Headings</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">100</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t100"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t100">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">1.22:1</b><b class="hidden font-medium tmu10-dark:inline">13.49:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Surface only</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Primary text</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">200</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t200"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t200">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">1.51:1</b><b class="hidden font-medium tmu10-dark:inline">10.36:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Decorative rule</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Secondary text</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">300</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t300"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t300">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">2.12:1</b><b class="hidden font-medium tmu10-dark:inline">7.20:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-bad-bg px-2 py-0.5 font-semibold text-tmu10-bad"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Fails 1.4.11</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Secondary text</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none tmu10-dark:border-t-2 tmu10-dark:border-t-tmu10-ink">
        <span class="absolute -top-2.5 right-0 hidden rounded-full bg-tmu10-ink px-2 font-tmu10-mono text-[0.625rem] font-semibold uppercase leading-[1.25rem] tracking-[0.08em] text-tmu10-bg tmu10-dark:inline">4.5:1 floor</span><span role="cell" class="font-tmu10-mono font-medium tabular-nums">400</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t400"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t400">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">2.96:1</b><b class="hidden font-medium tmu10-dark:inline">4.98:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-bad-bg px-2 py-0.5 font-semibold text-tmu10-bad"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>The classic fail</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Body text floor</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">500</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t500"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t500">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">4.07:1</b><b class="hidden font-medium tmu10-dark:inline">3.55:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Large text / borders</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Large text / borders</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none border-t-2 border-t-tmu10-ink tmu10-dark:border-t-0">
        <span class="absolute -top-2.5 right-0 rounded-full bg-tmu10-ink px-2 font-tmu10-mono text-[0.625rem] font-semibold uppercase leading-[1.25rem] tracking-[0.08em] text-tmu10-bg tmu10-dark:hidden">4.5:1 floor</span><span role="cell" class="font-tmu10-mono font-medium tabular-nums">600</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t600"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t600">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">5.85:1</b><b class="hidden font-medium tmu10-dark:inline">2.75:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Body text floor</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-bad-bg px-2 py-0.5 font-semibold text-tmu10-bad"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>The classic fail</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">700</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t700"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t700">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">8.60:1</b><b class="hidden font-medium tmu10-dark:inline">1.95:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Secondary text</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-bad-bg px-2 py-0.5 font-semibold text-tmu10-bad"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Fails 1.4.11</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">800</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t800"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t800">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">12.99:1</b><b class="hidden font-medium tmu10-dark:inline">1.42:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Primary text</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Surface only</span></span></span>
      </div>
      <div role="row" class="relative grid min-w-0 grid-cols-[2.75rem_3rem_minmax(0,1fr)_4.75rem] items-center gap-x-3 gap-y-2 sm:grid-cols-[3rem_4rem_minmax(0,1fr)_5rem_minmax(0,12rem)] border-b border-tmu10-line py-3 text-[0.8125rem] transition-colors duration-150 hover:bg-tmu10-t050/40 motion-reduce:transition-none">
        <span role="cell" class="font-tmu10-mono font-medium tabular-nums">900</span>
        <span role="cell"><i class="block h-7 w-full rounded-md border border-tmu10-line bg-tmu10-t900"></i></span>
        <span role="cell" class="text-lg font-medium tracking-[-0.01em] text-tmu10-t900">Aa</span>
        <span role="cell" class="text-right font-tmu10-mono font-medium tabular-nums"><b class="font-medium tmu10-dark:hidden">17.65:1</b><b class="hidden font-medium tmu10-dark:inline">1.18:1</b></span>
        <span role="cell" class="col-[3/-1] min-w-0 text-xs sm:col-auto sm:justify-self-end"><span class="tmu10-dark:hidden"><span class="inline-flex items-center gap-1.5 rounded-full bg-tmu10-ok-bg px-2 py-0.5 font-semibold text-tmu10-ok"><svg class="size-3.5 flex-none" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>Headings</span></span><span class="hidden tmu10-dark:inline"><span class="inline-flex items-center px-2 py-0.5 text-tmu10-ink-2">Surface only</span></span></span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmu10-ground: light-dark(#ffffff, #14171a);
  --color-tmu10-ground: light-dark(oklch(100% 0 0), oklch(19% 0.005 250));
  --color-tmu10-bg: light-dark(#ffffff, #14171a);
  --color-tmu10-bg: light-dark(oklch(100% 0 0), oklch(19% 0.005 250));
  --color-tmu10-ink: light-dark(#16191c, #e9ecee);
  --color-tmu10-ink: light-dark(oklch(20% 0.006 250), oklch(93.5% 0.003 250));
  --color-tmu10-ink-2: light-dark(#5d666e, #a1a9b0);
  --color-tmu10-ink-2: light-dark(oklch(48% 0.012 250), oklch(73% 0.008 250));
  --color-tmu10-line: light-dark(#cfd3d7, #343b41);
  --color-tmu10-line: light-dark(oklch(85.5% 0.005 250), oklch(33.5% 0.009 250));
  --color-tmu10-ok: light-dark(#16663d, #62c78f);
  --color-tmu10-ok: light-dark(oklch(44% 0.11 155), oklch(78% 0.12 155));
  --color-tmu10-bad: light-dark(#a32020, #f08a8a);
  --color-tmu10-bad: light-dark(oklch(45% 0.18 25), oklch(74% 0.14 25));
  --color-tmu10-acc: light-dark(#16191c, #e9ecee);
  --color-tmu10-acc: light-dark(oklch(20% 0.006 250), oklch(93.5% 0.003 250));
  --color-tmu10-t050: light-dark(#f6f7f8, #eef1f3);
  --color-tmu10-t100: light-dark(#e7e9eb, #d8dde0);
  --color-tmu10-t200: light-dark(#cfd3d7, #bcc3c8);
  --color-tmu10-t300: light-dark(#adb3b9, #9aa3aa);
  --color-tmu10-t400: light-dark(#8f979e, #7d868d);
  --color-tmu10-t500: light-dark(#767f87, #656e75);
  --color-tmu10-t600: light-dark(#5d666e, #545d64);
  --color-tmu10-t700: light-dark(#454d54, #3f474d);
  --color-tmu10-t800: light-dark(#2b3238, #2b3238);
  --color-tmu10-t900: light-dark(#16191c, #1e2429);
  --color-tmu10-ok-bg: color-mix(in oklab, var(--color-tmu10-ok) 12%, transparent);
  --color-tmu10-bad-bg: color-mix(in oklab, var(--color-tmu10-bad) 12%, transparent);
  --font-tmu10-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-tmu10-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build
   compiles. color-scheme drives every light-dark() token above. */

.tmu-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  color-scheme: light dark;
}
/* Theme toggle: flip the scheme and every token follows. Mirrored for a dark OS. */

.tmu-10:has(#tmu10-theme:checked) {
  color-scheme: dark;
}

@media (prefers-color-scheme: dark) {
  .tmu-10:has(#tmu10-theme:checked) {
    color-scheme: light;
  }
}
/* "Effective dark": dark OS without the toggle, or light OS with it. One variant for both. */

@custom-variant tmu10-dark {
  @media (prefers-color-scheme: dark) {
    .tmu-10:not(:has(#tmu10-theme:checked)) & {
      @slot;
    }
  }

  @media (prefers-color-scheme: light) {
    .tmu-10:has(#tmu10-theme:checked) & {
      @slot;
    }
  }
}
```
