---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-dashboard-cards/"
title: "Tailwind Dark Mode Dashboard Cards with Sparklines"
section: "design-styles"
category: "tailwind-css-dark-mode-ui"
category_name: "Tailwind CSS Dark Mode UI"
description: "Six metric cards — MRR, signups, churn, active users, response time, uptime — with SVG sparklines, tabular-figure readouts and delta chips that pair an arrow…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dark Mode Dashboard Cards with Sparklines
Source: https://codefronts.com/design-styles/tailwind-css-dark-mode-ui/tailwind-dark-mode-dashboard-cards/

Six metric cards — MRR, signups, churn, active users, response time, uptime — with SVG sparklines, tabular-figure readouts and delta chips that pair an arrow with colour so status never rests on hue alone. Cards sit on a radial wash between two surface tokens, which is what stops a dark dashboard reading as one flat black rectangle. Range selector and theme toggle, both pure CSS.
## HTML
```html
<div class="tdm-06 scheme-light-dark has-[#tdm-06-toggle:checked]:scheme-dark dark:has-[#tdm-06-toggle:checked]:scheme-light w-full min-h-svh bg-tdm06-bg bg-[radial-gradient(110%_80%_at_50%_-20%,var(--color-tdm06-glow),transparent_62%)] font-tdm06-sans text-tdm06-ink antialiased transition-colors duration-300">
  <div class="mx-auto grid min-h-svh max-w-6xl content-center gap-6 px-4 py-12 sm:px-8">
    <header class="flex flex-wrap items-center justify-between gap-4">
      <div><h1 class="text-[clamp(1.6rem,3vw,2.2rem)] font-semibold tracking-[-0.035em]">Growth</h1><p class="mt-1 font-tdm06-mono text-xs text-tdm06-mut">Production · updated 2 min ago</p></div>
      <div class="flex items-center gap-2.5">
        <fieldset class="flex gap-1 rounded-xl border border-tdm06-line bg-tdm06-surface p-1">
          <legend class="sr-only">Date range</legend>
          <label class="grid min-h-9 min-w-11 cursor-pointer place-items-center rounded-lg px-2.5 font-tdm06-mono text-xs text-tdm06-mut transition hover:text-tdm06-ink has-checked:bg-tdm06-acc has-checked:text-tdm06-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm06-focus"><input type="radio" name="tdm-06-range" class="sr-only">7d</label>
          <label class="grid min-h-9 min-w-11 cursor-pointer place-items-center rounded-lg px-2.5 font-tdm06-mono text-xs text-tdm06-mut transition hover:text-tdm06-ink has-checked:bg-tdm06-acc has-checked:text-tdm06-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm06-focus"><input type="radio" name="tdm-06-range" class="sr-only" checked>30d</label>
          <label class="grid min-h-9 min-w-11 cursor-pointer place-items-center rounded-lg px-2.5 font-tdm06-mono text-xs text-tdm06-mut transition hover:text-tdm06-ink has-checked:bg-tdm06-acc has-checked:text-tdm06-acc-ink has-focus-visible:outline-2 has-focus-visible:outline-tdm06-focus"><input type="radio" name="tdm-06-range" class="sr-only">90d</label>
        </fieldset>
        <label class="relative grid size-11 flex-none cursor-pointer place-items-center rounded-xl border border-tdm06-line bg-tdm06-surface transition duration-200 hover:-translate-y-px hover:border-tdm06-acc/60 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tdm06-focus motion-reduce:transition-none ">
        <input id="tdm-06-toggle" type="checkbox" class="sr-only">
        <span class="sr-only">Toggle light and dark theme</span>
        <svg class="col-start-1 row-start-1 size-5 text-tdm06-sun transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></svg>
        <svg class="col-start-1 row-start-1 size-5 text-tdm06-moon transition-colors duration-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.2A8.5 8.5 0 1 1 9.8 3.5a6.8 6.8 0 0 0 10.7 10.7Z"/></svg>
      </label>
      </div>
    </header>
    <div class="grid grid-cols-[repeat(auto-fit,minmax(16.5rem,1fr))] gap-4">
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">MRR</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-good/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-good"><svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>12.4% up</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">$148,920</p>
        <svg class="h-12 w-full text-tdm06-acc" viewBox="0 0 120 36" preserveAspectRatio="none" aria-hidden="true"><path d="M0.0,32.0 L10.9,28.7 L21.8,29.5 L32.7,24.6 L43.6,25.8 L54.5,20.5 L65.5,18.8 L76.4,19.6 L87.3,13.9 L98.2,11.4 L109.1,8.1 L120.0,4.0 L120,36 L0,36 Z" fill="currentColor" opacity=".12"/><path d="M0.0,32.0 L10.9,28.7 L21.8,29.5 L32.7,24.6 L43.6,25.8 L54.5,20.5 L65.5,18.8 L76.4,19.6 L87.3,13.9 L98.2,11.4 L109.1,8.1 L120.0,4.0" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">$16.4k added this month</p>
      </article>
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">Signups</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-good/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-good"><svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>8.1% up</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">3,284</p>
        <svg class="h-12 w-full text-tdm06-acc" viewBox="0 0 120 36" preserveAspectRatio="none" aria-hidden="true"><path d="M0.0,29.1 L10.9,32.0 L21.8,24.6 L32.7,28.0 L43.6,20.6 L54.5,23.4 L65.5,16.6 L76.4,18.9 L87.3,9.1 L98.2,13.1 L109.1,6.3 L120.0,4.0 L120,36 L0,36 Z" fill="currentColor" opacity=".12"/><path d="M0.0,29.1 L10.9,32.0 L21.8,24.6 L32.7,28.0 L43.6,20.6 L54.5,23.4 L65.5,16.6 L76.4,18.9 L87.3,9.1 L98.2,13.1 L109.1,6.3 L120.0,4.0" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">412 from the launch post</p>
      </article>
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">Churn</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-good/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-good"><svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 7l10 10M17 9v8H9"/></svg>0.4pt down</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">2.1%</p>
        <svg class="h-12 w-full text-tdm06-acc" viewBox="0 0 120 36" preserveAspectRatio="none" aria-hidden="true"><path d="M0.0,4.0 L10.9,6.5 L21.8,5.3 L32.7,10.4 L43.6,12.9 L54.5,14.2 L65.5,18.0 L76.4,19.9 L87.3,23.1 L98.2,26.9 L109.1,29.5 L120.0,32.0 L120,36 L0,36 Z" fill="currentColor" opacity=".12"/><path d="M0.0,4.0 L10.9,6.5 L21.8,5.3 L32.7,10.4 L43.6,12.9 L54.5,14.2 L65.5,18.0 L76.4,19.9 L87.3,23.1 L98.2,26.9 L109.1,29.5 L120.0,32.0" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">Lowest since March</p>
      </article>
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">Active users</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-good/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-good"><svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>3.6% up</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">21,905</p>
        <svg class="h-12 w-full text-tdm06-acc" viewBox="0 0 120 36" preserveAspectRatio="none" aria-hidden="true"><path d="M0.0,32.0 L10.9,29.2 L21.8,30.6 L32.7,26.4 L43.6,27.8 L54.5,25.0 L65.5,23.6 L76.4,24.3 L87.3,20.8 L98.2,22.2 L109.1,18.0 L120.0,16.6 L120,36 L0,36 Z" fill="currentColor" opacity=".12"/><path d="M0.0,32.0 L10.9,29.2 L21.8,30.6 L32.7,26.4 L43.6,27.8 L54.5,25.0 L65.5,23.6 L76.4,24.3 L87.3,20.8 L98.2,22.2 L109.1,18.0 L120.0,16.6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">7-day rolling average</p>
      </article>
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">Response time</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-flat/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-flat">holding flat</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">142<span class="text-sm font-normal tracking-normal text-tdm06-mut">ms p95</span></p>
        <svg class="h-12 w-full text-tdm06-flat" viewBox="0 0 120 36" preserveAspectRatio="none" aria-hidden="true"><path d="M0.0,29.2 L10.9,32.0 L21.8,27.1 L32.7,30.6 L43.6,28.5 L54.5,31.3 L65.5,27.8 L76.4,29.9 L87.3,30.6 L98.2,28.5 L109.1,31.3 L120.0,29.2 L120,36 L0,36 Z" fill="currentColor" opacity=".12"/><path d="M0.0,29.2 L10.9,32.0 L21.8,27.1 L32.7,30.6 L43.6,28.5 L54.5,31.3 L65.5,27.8 L76.4,29.9 L87.3,30.6 L98.2,28.5 L109.1,31.3 L120.0,29.2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">iad1 · fra1 · syd1</p>
      </article>
      <article class="@container group/card grid gap-3 rounded-[22px] border border-tdm06-line bg-tdm06-surface p-5 inset-shadow-[0_1px_0_var(--color-tdm06-sheen)] transition duration-300 hover:-translate-y-0.5 hover:border-tdm06-acc/40 motion-reduce:transition-none forced-colors:border-[CanvasText]">
        <div class="flex items-center justify-between gap-2">
          <h2 class="text-[13px] font-medium text-tdm06-mut">Uptime</h2>
          <span class="inline-flex items-center gap-1 rounded-full bg-tdm06-good/12 px-2 py-1 font-tdm06-mono text-[11px] font-medium text-tdm06-good"><svg class="size-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>on target</span>
        </div>
        <p class="flex items-baseline gap-1.5 text-[clamp(1.7rem,4cqi,2.1rem)] font-semibold tracking-[-0.04em] tabular-nums">99.98%</p>
        <div class="flex h-12 items-end gap-[3px]" aria-hidden="true"><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-1/2 bg-tdm06-bad"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i><i class="flex-1 rounded-sm h-full bg-tdm06-good/70"></i></div>
        <p class="border-t border-tdm06-line pt-3 text-[13px] text-tdm06-mut @max-[15rem]:text-xs">One 4-minute degradation</p>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdm06-bg: light-dark(#f2f3f6, #07070a);
  --color-tdm06-glow: light-dark(rgb(3 105 161 / .1), rgb(125 211 252 / .09));
  --color-tdm06-surface: light-dark(#ffffff, #101015);
  --color-tdm06-ink: light-dark(#0b0b12, #f5f5f7);
  --color-tdm06-mut: light-dark(#5a606e, #9696a4);
  --color-tdm06-line: light-dark(#e2e5ec, #22222d);
  --color-tdm06-sheen: light-dark(rgb(255 255 255 / 1), rgb(255 255 255 / .06));
  --color-tdm06-acc: light-dark(#0369a1, #7dd3fc);
  --color-tdm06-acc-ink: light-dark(#ffffff, #031c27);
  --color-tdm06-focus: light-dark(#0369a1, #bae6fd);
  --color-tdm06-good: light-dark(#15803d, #4ade80);
  --color-tdm06-bad: light-dark(#c2410c, #fb923c);
  --color-tdm06-flat: light-dark(#52525b, #a1a1aa);
  --color-tdm06-sun: light-dark(#b45309, transparent);
  --color-tdm06-moon: light-dark(transparent, #bae6fd);
  --font-tdm06-sans: 'Geist', ui-sans-serif, system-ui, sans-serif;
  --font-tdm06-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is sized
   in the moment before the browser build has compiled. */

.tdm-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
}
```
