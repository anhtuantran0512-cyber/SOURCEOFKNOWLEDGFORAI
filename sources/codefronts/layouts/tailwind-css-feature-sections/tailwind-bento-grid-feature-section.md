---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-bento-grid-feature-section/"
title: "Tailwind Bento Grid Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "An asymmetric bento of five features on a 4×2 grid: a hero tile spanning two by two with a live chart, a tall tile, a wide tile and two squares — each…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bento Grid Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-bento-grid-feature-section/

An asymmetric bento of five features on a 4×2 grid: a hero tile spanning two by two with a live chart, a tall tile, a wide tile and two squares — each holding a small drawn product moment. Spans are utilities (lg:col-span-2 lg:row-span-2); on phones it collapses to a clean single column.
## HTML
```html
<section class="tfs-14 w-full min-h-svh bg-tfs14-bg px-5 py-20 font-tfs14-sans text-tfs14-ink antialiased sm:py-28" aria-labelledby="tfs-14-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12">
    <header class="grid max-w-2xl gap-4">
      <p class="text-sm font-semibold text-tfs14-acc">Talon for finance teams</p>
      <h2 id="tfs-14-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Close the books <span class="font-tfs14-serif font-normal italic text-tfs14-acc">in days,</span> not weeks</h2>
    </header>
    <div class="grid gap-4 lg:grid-cols-4 lg:grid-rows-[repeat(2,minmax(17rem,auto))]">
      <article class="relative grid overflow-hidden rounded-3xl bg-tfs14-ink p-8 text-white lg:col-span-2 lg:row-span-2">
        <div class="relative z-10 grid max-w-sm gap-3"><h3 class="text-2xl font-semibold">Real-time cash position</h3><p class="text-pretty text-white/70">Every account, every currency, reconciled the moment a transaction lands.</p></div>
        <div aria-hidden="true" class="mt-8 self-end rounded-2xl bg-white/5 p-5 ring-1 ring-white/10">
          <div class="flex items-baseline justify-between"><p class="text-sm text-white/70">Total cash</p><p class="rounded-full bg-emerald-400/15 px-2 py-0.5 text-xs font-semibold text-emerald-300">+8.2%</p></div>
          <p class="mt-1 text-4xl font-semibold tabular-nums">$14,820,400</p>
          <svg viewBox="0 0 300 90" class="mt-4 w-full" fill="none"><defs><linearGradient id="tfs14g" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="currentColor" stop-opacity=".45"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs><path d="M0 70 C40 60 60 72 90 55 S150 30 180 38 S240 12 300 8 V90 H0Z" fill="url(#tfs14g)" class="text-tfs14-acc"/><path d="M0 70 C40 60 60 72 90 55 S150 30 180 38 S240 12 300 8" stroke="currentColor" stroke-width="2.5" class="text-tfs14-acc"/></svg>
        </div>
      </article>
      <article class="grid content-start gap-3 overflow-hidden rounded-3xl bg-white p-7 ring-1 ring-tfs14-line lg:row-span-2">
        <h3 class="text-lg font-semibold">Auto-matching</h3><p class="text-sm text-tfs14-mut">97% of transactions matched without a human.</p>
        <ul aria-hidden="true" class="mt-4 grid gap-2 mask-b-from-60%"><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>Stripe payout</span><span class="grid size-5 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></li><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>AWS invoice</span><span class="grid size-5 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></li><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>Gusto payroll</span><span class="grid size-5 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></li><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>Brex card</span><span class="grid size-5 place-items-center rounded-full bg-amber-100 text-amber-700">!</span></li><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>Wise transfer</span><span class="grid size-5 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></li><li class="flex items-center justify-between rounded-xl bg-tfs14-bg px-3 py-2.5 text-sm"><span>Ramp bill</span><span class="grid size-5 place-items-center rounded-full bg-emerald-100 text-emerald-700"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3"><path d="M20 6 9 17l-5-5"/></svg></span></li></ul>
      </article>
      <article class="grid content-start gap-3 rounded-3xl bg-tfs14-acc p-7 text-white">
        <span class="grid size-10 place-items-center rounded-xl bg-white/15"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2"/></svg></span>
        <p class="mt-auto text-5xl font-semibold tracking-tight tabular-nums">3.2<span class="text-2xl"> days</span></p><h3 class="font-medium text-white/90">Average month-end close</h3>
      </article>
      <article class="grid content-start gap-3 rounded-3xl bg-white p-7 ring-1 ring-tfs14-line">
        <span class="grid size-10 place-items-center rounded-xl bg-tfs14-acc/10 text-tfs14-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg></span>
        <h3 class="mt-auto text-lg font-semibold">42 currencies</h3><p class="text-sm text-tfs14-mut">FX revalued nightly at mid-market.</p>
      </article>
      <article class="grid items-center gap-6 rounded-3xl bg-white p-7 ring-1 ring-tfs14-line sm:grid-cols-[1fr_auto] lg:col-span-4">
        <div class="grid gap-2"><h3 class="text-lg font-semibold">Audit-ready by default</h3><p class="text-pretty text-sm text-tfs14-mut">Every entry links to its source document, approver and timestamp — export the full trail in one click.</p></div>
        <div aria-hidden="true" class="flex -space-x-3"><span class="grid size-11 place-items-center rounded-full bg-sky-200 text-xs font-bold ring-4 ring-white">AC</span><span class="grid size-11 place-items-center rounded-full bg-rose-200 text-xs font-bold ring-4 ring-white">PS</span><span class="grid size-11 place-items-center rounded-full bg-amber-200 text-xs font-bold ring-4 ring-white">JL</span><span class="grid size-11 place-items-center rounded-full bg-emerald-200 text-xs font-bold ring-4 ring-white">SR</span></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs14-bg: #f4f4f2;
  --color-tfs14-bg: oklch(0.967 0.003 106);
  --color-tfs14-ink: #141414;
  --color-tfs14-ink: oklch(0.191 0 0);
  --color-tfs14-mut: #55554f;
  --color-tfs14-mut: oklch(0.448 0.01 107);
  --color-tfs14-line: #e5e5e0;
  --color-tfs14-line: oklch(0.921 0.007 107);
  --color-tfs14-acc: #7c3aed;
  --color-tfs14-acc: oklch(0.541 0.247 293);
  --font-tfs14-sans: 'Geist', system-ui, sans-serif;
  --font-tfs14-serif: 'Instrument Serif', Georgia, serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-14 {
  width: 100%;
  min-height: 100svh;
}
```
