---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-subgrid-cards-aligned-buttons/"
title: "Tailwind Subgrid Cards with Perfectly Aligned Buttons"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A template gallery where titles run to different lengths and descriptions to different depths — yet every badge, title, body and button sits on a shared…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Subgrid Cards with Perfectly Aligned Buttons
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-subgrid-cards-aligned-buttons/

A template gallery where titles run to different lengths and descriptions to different depths — yet every badge, title, body and button sits on a shared line, because each card adopts the parent's row tracks. Flexbox's mt-auto workaround retires here.
## HTML
```html
<section class="tgx-15 w-full min-h-svh bg-tgx15-bg font-tgx15-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-5">
    <div class="flex flex-col gap-1">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx15-mint">Relay · Templates</p>
      <h2 class="text-[1.35rem] font-semibold text-white tracking-[-0.01em]">Start from a workflow</h2>
    </div>
    <p class="text-[0.76rem] text-tgx15-dim">Every card spans the same four rows</p>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(210px,100%),1fr))] auto-rows-auto gap-4">
    <article class="row-span-4 [grid-template-rows:subgrid] grid gap-y-3 rounded-2xl border border-tgx15-edge bg-tgx15-card p-5">
      <p class="text-[0.64rem] tracking-[0.16em] uppercase text-tgx15-mint">Incident response</p>
      <h3 class="text-[1.05rem] leading-[1.3] font-semibold text-white text-balance">On-call triage</h3>
      <p class="text-[0.8rem] leading-[1.6] text-tgx15-dim">Route, acknowledge, escalate. Four steps, one channel.</p>
      <a href="#0" class="self-end justify-self-start inline-flex items-center min-h-11 px-4 rounded-full text-[0.82rem] font-semibold no-underline text-tgx15-ink bg-tgx15-mint transition-colors hover:bg-tgx15-minthover focus-visible:outline-2 focus-visible:outline-tgx15-mint focus-visible:outline-offset-[3px]">Use template</a>
    </article>
    <article class="row-span-4 [grid-template-rows:subgrid] grid gap-y-3 rounded-2xl border border-tgx15-mint bg-tgx15-cardhot p-5">
      <p class="text-[0.64rem] tracking-[0.16em] uppercase text-tgx15-mint">Release · most used</p>
      <h3 class="text-[1.05rem] leading-[1.3] font-semibold text-white text-balance">Progressive rollout with automatic rollback gates</h3>
      <p class="text-[0.8rem] leading-[1.6] text-tgx15-dim">Ship to 5%, watch error budget, promote or revert automatically. The long title above raises the title track for every sibling card — that is subgrid doing its job.</p>
      <a href="#0" class="self-end justify-self-start inline-flex items-center min-h-11 px-4 rounded-full text-[0.82rem] font-semibold no-underline text-tgx15-ink bg-tgx15-mint transition-colors hover:bg-tgx15-minthover focus-visible:outline-2 focus-visible:outline-tgx15-mint focus-visible:outline-offset-[3px]">Use template</a>
    </article>
    <article class="row-span-4 [grid-template-rows:subgrid] grid gap-y-3 rounded-2xl border border-tgx15-edge bg-tgx15-card p-5">
      <p class="text-[0.64rem] tracking-[0.16em] uppercase text-tgx15-mint">Reporting</p>
      <h3 class="text-[1.05rem] leading-[1.3] font-semibold text-white text-balance">Weekly digest</h3>
      <p class="text-[0.8rem] leading-[1.6] text-tgx15-dim">Short title, short copy — and the button still lands level with its neighbours, because the final track is shared rather than pushed down by content.</p>
      <a href="#0" class="self-end justify-self-start inline-flex items-center min-h-11 px-4 rounded-full text-[0.82rem] font-semibold no-underline text-tgx15-ink bg-tgx15-mint transition-colors hover:bg-tgx15-minthover focus-visible:outline-2 focus-visible:outline-tgx15-mint focus-visible:outline-offset-[3px]">Use template</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx15-bg: #1a2724;
  --color-tgx15-bg: oklch(0.24 0.03 175);
  --color-tgx15-card: #20302c;
  --color-tgx15-card: oklch(0.28 0.03 175);
  --color-tgx15-cardhot: #26403a;
  --color-tgx15-cardhot: oklch(0.33 0.05 170);
  --color-tgx15-edge: #395049;
  --color-tgx15-edge: oklch(0.4 0.04 175);
  --color-tgx15-mint: #8fe3c4;
  --color-tgx15-mint: oklch(0.86 0.12 165);
  --color-tgx15-minthover: #a9ecd4;
  --color-tgx15-minthover: oklch(0.9 0.1 165);
  --color-tgx15-ink: #12241f;
  --color-tgx15-ink: oklch(0.22 0.03 175);
  --color-tgx15-dim: #b5c9c2;
  --color-tgx15-dim: oklch(0.8 0.02 175);
  --font-tgx15-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-15 {
  width: 100%;
  min-height: 100svh;
}

@supports not (grid-template-rows: subgrid) {
  .tgx-15 article {
    grid-template-rows: auto auto 1fr auto;
  }
}
```
