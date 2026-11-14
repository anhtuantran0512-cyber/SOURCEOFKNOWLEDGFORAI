---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-inline-micro-empty-state-component/"
title: "Tailwind CSS Inline Micro Empty State Component"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "Not every empty state deserves a hero."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Inline Micro Empty State Component
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-inline-micro-empty-state-component/

Not every empty state deserves a hero. This finance dashboard shows one micro component in four homes — a sidebar rail, a feed card, a narrow budget tile and inside a table — and each adapts to its container, not the viewport, with @container and @max-2xs:. One icon, one line, one action, every time.
## HTML
```html
<div class="tes-20 w-full min-h-svh bg-tes20-bg font-tes20-sans text-tes20-ink antialiased">
  <div class="grid min-h-svh md:grid-cols-[15rem_minmax(0,1fr)]">
    <aside class="hidden flex-col gap-6 border-r border-tes20-line bg-tes20-card p-4 md:flex">
      <span class="flex items-center gap-2 px-2 font-semibold"><span aria-hidden="true" class="size-5 rounded-full border-[5px] border-tes20-acc"></span>Runway</span>
      <nav class="grid gap-0.5 text-sm">
        <a href="#" aria-current="page" class="flex min-h-10 items-center rounded-lg bg-tes20-sunk px-3 font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Today</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes20-mut hover:bg-tes20-sunk hover:text-tes20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Spend</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes20-mut hover:bg-tes20-sunk hover:text-tes20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Vendors</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes20-mut hover:bg-tes20-sunk hover:text-tes20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Approvals</a>
      </nav>
      <div class="grid gap-2">
        <p class="px-2 text-[11px] font-semibold tracking-[0.12em] text-tes20-mut uppercase">Starred reports</p>
        <div class="@container rounded-xl border border-dashed border-tes20-line2 p-3">
          <div class="flex items-center gap-3 @max-2xs:flex-col @max-2xs:items-start @max-2xs:gap-2">
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-tes20-warn/12 text-tes20-warn"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m12 4 2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 9.7l5.4-.8z"/></svg></span>
            <span class="grid min-w-0 flex-1"><span class="text-[13px] font-semibold">No starred reports</span><span class="text-xs text-tes20-mut text-pretty">Star one to pin it to this rail.</span></span>
            <button type="button" class="min-h-11 rounded-lg px-2 text-xs font-medium text-tes20-acc hover:underline @max-2xs:min-h-9 @max-2xs:px-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Browse</button>
          </div>
        </div>
      </div>
    </aside>
    <main class="flex min-w-0 flex-col gap-6 px-[clamp(1rem,4vw,2.5rem)] py-6">
      <header class="flex flex-wrap items-center justify-between gap-3">
        <h1 class="text-2xl font-semibold tracking-tight">Today</h1>
        <div class="flex items-center gap-2">
          <button type="button" class="min-h-11 rounded-lg border border-tes20-line bg-tes20-card px-3.5 text-sm hover:bg-tes20-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">This month</button>
          <button type="button" class="min-h-11 rounded-lg border border-tes20-line bg-tes20-card px-3.5 text-sm hover:bg-tes20-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Quarter</button>
          <button type="button" aria-label="Account" class="grid size-11 place-items-center rounded-full bg-tes20-ink text-xs font-semibold text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">EM</button>
        </div>
      </header>
      <div class="grid gap-4 lg:grid-cols-[minmax(0,2fr)_minmax(0,1fr)]">
        <section aria-labelledby="tes20-ta" class="grid content-start gap-3 rounded-2xl bg-tes20-card p-4 ring-1 ring-tes20-line">
          <p id="tes20-ta" class="text-sm font-medium">Team activity</p>
          <div class="@container rounded-xl border border-dashed border-tes20-line2 p-4">
            <div class="flex items-center gap-3 @max-2xs:flex-col @max-2xs:items-start">
              <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-tes20-acc/10 text-tes20-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 5h14v10H9l-4 4z"/></svg></span>
              <span class="grid min-w-0 flex-1"><span class="text-[13px] font-semibold">No activity today</span><span class="text-xs text-tes20-mut text-pretty">Comments, mentions and status changes from your team appear here.</span></span>
              <button type="button" class="min-h-11 flex-none rounded-lg px-2 text-xs font-medium text-tes20-acc hover:underline @min-sm:border @min-sm:border-tes20-line @min-sm:bg-tes20-card @min-sm:px-3.5 @min-sm:hover:bg-tes20-sunk @min-sm:hover:no-underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Follow a project</button>
            </div>
          </div>
        </section>
        <section aria-labelledby="tes20-bu" class="grid content-start gap-3 rounded-2xl bg-tes20-card p-4 ring-1 ring-tes20-line">
          <p id="tes20-bu" class="text-sm font-medium">Budget</p>
          <div class="@container rounded-xl border border-dashed border-tes20-line2 p-4">
            <div class="flex items-center gap-3 @max-2xs:flex-col @max-2xs:items-start">
              <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-tes20-ok/12 text-tes20-ok"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8"/><path d="M12 7.5v9M14.5 9.5c-.4-.9-1.4-1.5-2.5-1.5-1.4 0-2.5.8-2.5 2s1.1 1.6 2.5 2 2.5.8 2.5 2-1.1 2-2.5 2c-1.1 0-2.1-.6-2.5-1.5"/></svg></span>
              <span class="grid min-w-0 flex-1"><span class="text-[13px] font-semibold">No spend yet</span><span class="text-xs text-tes20-mut text-pretty">Usage is billed monthly.</span></span>
              <button type="button" class="min-h-11 flex-none rounded-lg px-2 text-xs font-medium text-tes20-acc hover:underline @min-sm:border @min-sm:border-tes20-line @min-sm:px-3.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Set a budget</button>
            </div>
          </div>
        </section>
        <section aria-labelledby="tes20-vi" class="grid content-start gap-3 rounded-2xl bg-tes20-card p-4 ring-1 ring-tes20-line lg:col-span-2">
          <p id="tes20-vi" class="text-sm font-medium">Vendor invoices</p>
          <div role="table" aria-label="Vendor invoices" class="overflow-hidden rounded-xl border border-tes20-line">
            <div role="row" class="grid grid-cols-3 bg-tes20-sunk px-4 py-2.5 text-xs text-tes20-mut"><span role="columnheader">Vendor</span><span role="columnheader">Terms</span><span role="columnheader">Next charge</span></div>
            <div role="row" class="@container px-4 py-5">
              <div role="cell" class="flex items-center justify-center gap-3 @max-xs:flex-col @max-xs:text-center">
                <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-lg bg-tes20-sunk text-tes20-mut"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 3.5h7l4 4V19a1.5 1.5 0 0 1-1.5 1.5h-9.5A1.5 1.5 0 0 1 5.5 19V5A1.5 1.5 0 0 1 7 3.5zM9 12h6M9 15.5h4"/></svg></span>
                <span class="grid"><span class="text-[13px] font-semibold">No invoices this month</span><span class="text-xs text-tes20-mut text-pretty">Vendors on annual terms will not appear until renewal.</span></span>
                <button type="button" class="min-h-11 rounded-lg border border-tes20-line px-3.5 text-xs font-medium hover:bg-tes20-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes20-acc">Add a vendor</button>
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes20-bg: #f6f7f8;
  --color-tes20-bg: oklch(0.973 0.003 240);
  --color-tes20-card: #ffffff;
  --color-tes20-card: oklch(1 0 0);
  --color-tes20-sunk: #eef0f2;
  --color-tes20-sunk: oklch(0.951 0.004 240);
  --color-tes20-line: #e0e3e7;
  --color-tes20-line: oklch(0.908 0.007 240);
  --color-tes20-line2: #c6cbd2;
  --color-tes20-line2: oklch(0.83 0.012 245);
  --color-tes20-ink: #171a1f;
  --color-tes20-ink: oklch(0.21 0.01 250);
  --color-tes20-mut: #586070;
  --color-tes20-mut: oklch(0.47 0.023 255);
  --color-tes20-acc: #1f5fd6;
  --color-tes20-acc: oklch(0.51 0.18 260);
  --color-tes20-ok: #13845a;
  --color-tes20-ok: oklch(0.54 0.12 160);
  --color-tes20-warn: #b06a0a;
  --color-tes20-warn: oklch(0.59 0.13 68);
  --font-tes20-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-20 {
  width: 100%;
  min-height: 100svh;
}

.tes-20 [hidden] {
  display: none !important;
}
```
