---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-kanban-board-scroll-snap-columns/"
title: "Tailwind Kanban Board with Scroll Snap Columns"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A sprint board with avatars, labels, estimate chips and WIP limits."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Kanban Board with Scroll Snap Columns
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-kanban-board-scroll-snap-columns/

A sprint board with avatars, labels, estimate chips and WIP limits. Columns are implicit — append a <section> and you have a new list — and each stack scrolls under its own pinned header.
## HTML
```html
<section class="tgx-18 w-full min-h-svh bg-tgx18-bg font-tgx18-sans p-5">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-4">
    <div class="flex flex-col gap-1">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx18-dim">Sprint 42 · ends Friday</p>
      <h2 class="text-[1.25rem] font-semibold text-tgx18-ink tracking-[-0.01em]">Platform board</h2>
    </div>
    <div class="flex -space-x-2" aria-label="4 assignees on this board">
      <span class="size-7 rounded-full grid place-items-center text-[0.62rem] font-semibold bg-tgx18-a1 text-tgx18-bg ring-2 ring-tgx18-bg">AR</span>
      <span class="size-7 rounded-full grid place-items-center text-[0.62rem] font-semibold bg-tgx18-a2 text-tgx18-bg ring-2 ring-tgx18-bg">TK</span>
      <span class="size-7 rounded-full grid place-items-center text-[0.62rem] font-semibold bg-tgx18-a3 text-tgx18-bg ring-2 ring-tgx18-bg">MC</span>
      <span class="size-7 rounded-full grid place-items-center text-[0.62rem] font-semibold bg-tgx18-card text-tgx18-dim ring-2 ring-tgx18-bg">+5</span>
    </div>
  </header>
  <div role="list" aria-label="Board columns" class="grid grid-flow-col auto-cols-[clamp(240px,28vw,300px)] gap-3 h-[360px] overflow-x-auto overscroll-x-contain snap-x snap-proximity scroll-pl-1 pb-2">
    <section role="listitem" class="snap-start grid grid-rows-[auto_minmax(0,1fr)] rounded-2xl border border-tgx18-line bg-tgx18-col overflow-hidden">
      <header class="flex justify-between items-center px-3.5 py-3 border-b border-tgx18-line"><h3 class="text-[0.82rem] font-semibold text-tgx18-ink">Backlog</h3><span class="text-[0.66rem] tabular-nums text-tgx18-dim bg-tgx18-bg rounded-full px-2 py-0.5">4</span></header>
      <div class="overflow-y-auto p-2.5 flex flex-col gap-2">
        <article style="--p:oklch(0.78 0.12 250)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Refactor token refresh flow</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">API</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">5pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a1 text-tgx18-bg">AR</span></span></div></article>
        <article style="--p:oklch(0.82 0.13 150)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Empty states for the board view</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">Design</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">3pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a2 text-tgx18-bg">TK</span></span></div></article>
        <article style="--p:oklch(0.78 0.12 250)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Rate-limit webhook retries</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">API</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">8pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a3 text-tgx18-bg">MC</span></span></div></article>
        <article style="--p:oklch(0.84 0.13 85)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Quickstart rewrite</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">Docs</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">2pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a2 text-tgx18-bg">TK</span></span></div></article>
      </div>
    </section>
    <section role="listitem" class="snap-start grid grid-rows-[auto_minmax(0,1fr)] rounded-2xl border border-tgx18-line bg-tgx18-col overflow-hidden">
      <header class="flex justify-between items-center px-3.5 py-3 border-b border-tgx18-line"><h3 class="text-[0.82rem] font-semibold text-tgx18-ink">In progress</h3><span class="text-[0.66rem] tabular-nums text-tgx18-warn bg-tgx18-warntint rounded-full px-2 py-0.5">2 / 2 WIP</span></header>
      <div class="overflow-y-auto p-2.5 flex flex-col gap-2">
        <article style="--p:oklch(0.76 0.17 25)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Dunning emails firing twice</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">Urgent</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">3pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a1 text-tgx18-bg">AR</span></span></div></article>
        <article style="--p:oklch(0.82 0.13 150)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Grid layout collection, v2</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">Design</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">13pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a3 text-tgx18-bg">MC</span></span></div></article>
      </div>
    </section>
    <section role="listitem" class="snap-start grid grid-rows-[auto_minmax(0,1fr)] rounded-2xl border border-tgx18-line bg-tgx18-col overflow-hidden">
      <header class="flex justify-between items-center px-3.5 py-3 border-b border-tgx18-line"><h3 class="text-[0.82rem] font-semibold text-tgx18-ink">In review</h3><span class="text-[0.66rem] tabular-nums text-tgx18-dim bg-tgx18-bg rounded-full px-2 py-0.5">1</span></header>
      <div class="overflow-y-auto p-2.5 flex flex-col gap-2">
        <article style="--p:oklch(0.78 0.12 250)" class="rounded-lg border border-tgx18-line border-l-[3px] border-l-[var(--p)] bg-tgx18-card p-3 flex flex-col gap-2 transition-colors hover:border-tgx18-hover"><p class="text-[0.8rem] leading-[1.4] text-tgx18-ink">Subgrid pricing table</p><div class="flex items-center justify-between gap-2"><em class="not-italic text-[0.62rem] tracking-[0.04em] text-[var(--p)] bg-[color-mix(in_oklab,var(--p)_18%,transparent)] rounded px-1.5 py-0.5">API</em><span class="flex items-center gap-1.5"><span class="text-[0.62rem] tabular-nums text-tgx18-dim">5pt</span><span class="size-5 rounded-full grid place-items-center text-[0.55rem] font-semibold bg-tgx18-a2 text-tgx18-bg">TK</span></span></div></article>
      </div>
    </section>
    <section role="listitem" class="snap-start grid grid-rows-[auto_minmax(0,1fr)] rounded-2xl border border-tgx18-line bg-tgx18-col overflow-hidden">
      <header class="flex justify-between items-center px-3.5 py-3 border-b border-tgx18-line"><h3 class="text-[0.82rem] font-semibold text-tgx18-ink">Done</h3><span class="text-[0.66rem] tabular-nums text-tgx18-ok bg-tgx18-oktint rounded-full px-2 py-0.5">3</span></header>
      <div class="overflow-y-auto p-2.5 flex flex-col gap-2">
        <article class="rounded-lg border border-tgx18-line border-l-[3px] border-l-tgx18-done bg-tgx18-card p-3 flex flex-col gap-2"><p class="text-[0.8rem] leading-[1.4] text-tgx18-dim line-through">Dark mode tokens</p><div class="flex items-center justify-between gap-2"><em class="not-italic no-underline text-[0.62rem] text-tgx18-dim bg-tgx18-bg rounded px-1.5 py-0.5">Design</em><span class="text-[0.62rem] tabular-nums text-tgx18-dim">2pt</span></div></article>
        <article class="rounded-lg border border-tgx18-line border-l-[3px] border-l-tgx18-done bg-tgx18-card p-3 flex flex-col gap-2"><p class="text-[0.8rem] leading-[1.4] text-tgx18-dim line-through">Onboarding checklist</p><div class="flex items-center justify-between gap-2"><em class="not-italic no-underline text-[0.62rem] text-tgx18-dim bg-tgx18-bg rounded px-1.5 py-0.5">Growth</em><span class="text-[0.62rem] tabular-nums text-tgx18-dim">3pt</span></div></article>
        <article class="rounded-lg border border-tgx18-line border-l-[3px] border-l-tgx18-done bg-tgx18-card p-3 flex flex-col gap-2"><p class="text-[0.8rem] leading-[1.4] text-tgx18-dim line-through">CDN migration</p><div class="flex items-center justify-between gap-2"><em class="not-italic no-underline text-[0.62rem] text-tgx18-dim bg-tgx18-bg rounded px-1.5 py-0.5">Infra</em><span class="text-[0.62rem] tabular-nums text-tgx18-dim">8pt</span></div></article>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx18-bg: #1c1e2a;
  --color-tgx18-bg: oklch(0.21 0.02 270);
  --color-tgx18-col: #232634;
  --color-tgx18-col: oklch(0.25 0.025 270);
  --color-tgx18-card: #2b2f3f;
  --color-tgx18-card: oklch(0.3 0.025 270);
  --color-tgx18-line: #3a3f52;
  --color-tgx18-line: oklch(0.38 0.03 270);
  --color-tgx18-hover: #5b6280;
  --color-tgx18-hover: oklch(0.55 0.05 270);
  --color-tgx18-ink: #e9eaf1;
  --color-tgx18-ink: oklch(0.93 0.01 270);
  --color-tgx18-dim: #a8acbd;
  --color-tgx18-dim: oklch(0.74 0.02 270);
  --color-tgx18-done: #767b91;
  --color-tgx18-done: oklch(0.6 0.02 270);
  --color-tgx18-ok: #8ce0ae;
  --color-tgx18-ok: oklch(0.85 0.14 150);
  --color-tgx18-oktint: #29382f;
  --color-tgx18-oktint: oklch(0.31 0.04 150);
  --color-tgx18-warn: #f0cc72;
  --color-tgx18-warn: oklch(0.86 0.14 85);
  --color-tgx18-warntint: #3a3423;
  --color-tgx18-warntint: oklch(0.32 0.04 85);
  --color-tgx18-a1: #8ab4f8;
  --color-tgx18-a1: oklch(0.78 0.11 250);
  --color-tgx18-a2: #f0a68a;
  --color-tgx18-a2: oklch(0.79 0.12 40);
  --color-tgx18-a3: #9ee0c0;
  --color-tgx18-a3: oklch(0.86 0.11 160);
  --font-tgx18-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-18 {
  width: 100%;
  min-height: 100svh;
}
```
