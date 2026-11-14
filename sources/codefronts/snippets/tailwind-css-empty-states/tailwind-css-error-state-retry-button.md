---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-error-state-retry-button/"
title: "Tailwind CSS Error State with Retry Button"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "One dashboard panel fails while its neighbours stay live — the most common error a product ships and the least designed."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Error State with Retry Button
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-error-state-retry-button/

One dashboard panel fails while its neighbours stay live — the most common error a product ships and the least designed. The panel keeps its exact footprint through error → loading → ok, all three driven by data-state on the panel and read with group-data-[state=…]/p:, so the grid never jumps.
## HTML
```html
<div class="tes-11 w-full min-h-svh bg-tes11-bg font-tes11-sans text-tes11-ink antialiased">
  <div class="mx-auto grid w-full max-w-6xl gap-6 px-[clamp(1rem,4vw,3rem)] py-[clamp(1.5rem,5vw,3.5rem)]">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div class="grid gap-1"><span class="text-xs text-tes11-mut">Warehouse operations</span><h1 class="text-[clamp(1.5rem,3vw,2rem)] font-semibold tracking-tight">Fulfilment health</h1></div>
      <div class="flex gap-2"><button type="button" class="min-h-11 rounded-lg border border-tes11-line bg-tes11-card px-4 text-sm shadow-xs hover:bg-tes11-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes11-acc">Last 7 days</button><button type="button" class="min-h-11 rounded-lg border border-tes11-line bg-tes11-card px-4 text-sm shadow-xs hover:bg-tes11-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes11-acc">Share</button></div>
    </header>
    <div class="grid gap-4 lg:grid-cols-[minmax(0,2fr)_minmax(0,1fr)] lg:grid-rows-2">
      <section id="tes11-panel" data-state="error" aria-labelledby="tes11-pt" class="group/p flex flex-col overflow-hidden rounded-2xl bg-tes11-card ring-1 ring-tes11-line transition-shadow data-[state=error]:ring-tes11-err/30 lg:row-span-2">
        <header class="flex items-center justify-between border-b border-tes11-line px-5 py-3.5">
          <span id="tes11-pt" class="text-sm font-medium">Pick rate by station</span>
          <span id="tes11-tag" role="status" class="inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-xs font-medium group-data-[state=error]/p:bg-tes11-err/10 group-data-[state=error]/p:text-tes11-err group-data-[state=loading]/p:bg-tes11-sunk group-data-[state=loading]/p:text-tes11-mut group-data-[state=ok]/p:bg-tes11-ok/10 group-data-[state=ok]/p:text-tes11-ok"><i aria-hidden="true" class="size-1.5 rounded-full bg-current"></i><span>Failed</span></span>
        </header>
        <div class="relative grid min-h-80 flex-1">
          <div role="alert" class="hidden place-items-center p-6 group-data-[state=error]/p:grid">
            <div aria-hidden="true" class="absolute inset-x-8 bottom-8 flex h-32 items-end gap-3 opacity-40 [mask-image:linear-gradient(transparent,#000)]"><i class="h-[40%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[62%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[48%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[74%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[58%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[80%] flex-1 rounded-t border border-dashed border-tes11-line2"></i><i class="h-[66%] flex-1 rounded-t border border-dashed border-tes11-line2"></i></div>
            <div class="relative grid max-w-sm justify-items-center text-center">
              <span aria-hidden="true" class="grid size-14 place-items-center rounded-2xl bg-tes11-err/10 text-tes11-err ring-1 ring-tes11-err/20"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12.5a7 7 0 0 1 10.6-6M19 11.5a7 7 0 0 1-10.6 6M3 3l18 18"/></svg></span>
              <p class="mt-4 text-base font-semibold">This panel could not load</p>
              <p class="mt-1.5 text-[13px]/5 text-tes11-mut text-pretty">The metrics service answered with a gateway error. The rest of the page is live and unaffected.</p>
              <div class="mt-4 flex w-full flex-wrap justify-center gap-2">
                <button type="button" id="tes11-retry" class="inline-flex min-h-11 items-center gap-2 rounded-lg bg-tes11-ink px-4 text-sm font-medium text-white transition hover:bg-tes11-acc active:scale-[.98] disabled:opacity-50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes11-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M19 12a7 7 0 1 1-2.05-4.95M19 4v4h-4"/></svg>Try again</button>
                <button type="button" class="min-h-11 rounded-lg border border-tes11-line px-4 text-sm hover:bg-tes11-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes11-acc">Report the outage</button>
              </div>
              <dl class="mt-5 flex flex-wrap justify-center gap-x-4 gap-y-1 font-tes11-mono text-[11.5px] text-tes11-mut">
                <div class="flex gap-1"><dt>endpoint</dt><dd class="text-tes11-ink">metrics.pick_rate</dd></div>
                <div class="flex gap-1"><dt>code</dt><dd class="text-tes11-ink">502</dd></div>
                <div class="flex gap-1"><dt>attempt</dt><dd id="tes11-attempt" class="text-tes11-ink">1</dd></div>
              </dl>
            </div>
          </div>
          <div class="hidden flex-col justify-end gap-4 p-6 group-data-[state=loading]/p:flex">
            <div aria-hidden="true" class="flex h-40 items-end gap-3"><i class="h-[45%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk"></i><i class="h-[60%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:100ms]"></i><i class="h-[50%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:200ms]"></i><i class="h-[70%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:300ms]"></i><i class="h-[55%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:400ms]"></i><i class="h-[75%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:500ms]"></i><i class="h-[65%] flex-1 animate-pulse rounded-t-md bg-tes11-sunk [animation-delay:600ms]"></i></div>
            <p class="text-center text-sm text-tes11-mut">Refetching pick rate…</p>
          </div>
          <div class="hidden flex-col justify-end gap-4 p-6 group-data-[state=ok]/p:flex">
            <div aria-hidden="true" class="flex h-48 items-end gap-3 border-b border-tes11-line">
              <i style="--h:42%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc"></i><i style="--h:66%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc2 [animation-delay:60ms]"></i><i style="--h:51%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc [animation-delay:120ms]"></i><i style="--h:78%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc2 [animation-delay:180ms]"></i><i style="--h:63%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc [animation-delay:240ms]"></i><i style="--h:88%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc2 [animation-delay:300ms]"></i><i style="--h:72%" class="h-(--h) flex-1 origin-bottom animate-tes11-rise rounded-t-md bg-tes11-acc [animation-delay:360ms]"></i>
            </div>
            <ul class="flex flex-wrap gap-4 text-xs text-tes11-mut"><li class="flex items-center gap-1.5"><i class="size-2.5 rounded-sm bg-tes11-acc"></i>Station A — Aisle 1 to 4</li><li class="flex items-center gap-1.5"><i class="size-2.5 rounded-sm bg-tes11-acc2"></i>Station B — Aisle 5 to 9</li></ul>
            <button type="button" id="tes11-fail" class="min-h-11 self-start text-xs text-tes11-mut underline-offset-4 hover:text-tes11-ink hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes11-acc">Simulate the failure again</button>
          </div>
        </div>
      </section>
      <section class="rounded-2xl bg-tes11-card ring-1 ring-tes11-line">
        <header class="flex items-center justify-between border-b border-tes11-line px-5 py-3.5"><span class="text-sm font-medium">Open exceptions</span><span class="inline-flex items-center gap-1.5 rounded-full bg-tes11-ok/10 px-2.5 py-1 text-xs font-medium text-tes11-ok"><i class="size-1.5 rounded-full bg-current"></i>Live</span></header>
        <ul class="divide-y divide-tes11-line text-sm">
          <li class="flex justify-between px-5 py-3"><span>Damaged on arrival</span><span class="font-tes11-mono text-xs text-tes11-mut">Aisle 6</span></li>
          <li class="flex justify-between px-5 py-3"><span>Barcode unreadable</span><span class="font-tes11-mono text-xs text-tes11-mut">Aisle 2</span></li>
          <li class="flex justify-between px-5 py-3"><span>Short pick</span><span class="font-tes11-mono text-xs text-tes11-mut">Aisle 9</span></li>
        </ul>
      </section>
      <section class="rounded-2xl bg-tes11-card ring-1 ring-tes11-line">
        <header class="flex items-center justify-between border-b border-tes11-line px-5 py-3.5"><span class="text-sm font-medium">Shift notes</span><span class="inline-flex items-center gap-1.5 rounded-full bg-tes11-ok/10 px-2.5 py-1 text-xs font-medium text-tes11-ok"><i class="size-1.5 rounded-full bg-current"></i>Live</span></header>
        <p class="px-5 py-4 text-sm/6 text-tes11-mut">Night shift reported a jam on the sorter at 02:40. Cleared by 03:05, no packages lost.</p>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes11-bg: #f5f6f8;
  --color-tes11-bg: oklch(0.97 0.004 250);
  --color-tes11-card: #ffffff;
  --color-tes11-card: oklch(1 0 0);
  --color-tes11-sunk: #edeff3;
  --color-tes11-sunk: oklch(0.951 0.006 250);
  --color-tes11-line: #dfe2e8;
  --color-tes11-line: oklch(0.905 0.009 250);
  --color-tes11-line2: #b9bfcb;
  --color-tes11-line2: oklch(0.79 0.016 255);
  --color-tes11-ink: #171b24;
  --color-tes11-ink: oklch(0.21 0.017 260);
  --color-tes11-mut: #586174;
  --color-tes11-mut: oklch(0.47 0.027 260);
  --color-tes11-acc: #2f5bd8;
  --color-tes11-acc: oklch(0.51 0.19 265);
  --color-tes11-acc2: #7ea0f2;
  --color-tes11-acc2: oklch(0.72 0.12 265);
  --color-tes11-ok: #15855a;
  --color-tes11-ok: oklch(0.55 0.12 160);
  --color-tes11-err: #c2362b;
  --color-tes11-err: oklch(0.55 0.19 28);
  --font-tes11-sans: 'Geist', system-ui, sans-serif;
  --font-tes11-mono: 'Geist Mono', ui-monospace, monospace;
  --animate-tes11-rise: tes11-rise 0.6s cubic-bezier(0.2,0.8,0.2,1) both;

  @keyframes tes11-rise {
    from {
      scale: 1 0;
    }

    to {
      scale: 1 1;
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-11 {
  width: 100%;
  min-height: 100svh;
}

.tes-11 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-11');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const panel = $('#tes11-panel'), label = $('#tes11-tag span'), retry = $('#tes11-retry');
  let tries = 1;
  const set = (state, text) => { panel.dataset.state = state; label.textContent = text; };
  retry.addEventListener('click', () => {
    retry.disabled = true;
    set('loading', 'Retrying');
    setTimeout(() => { tries++; $('#tes11-attempt').textContent = tries; retry.disabled = false; set('ok', 'Live'); }, 1500);
  });
  $('#tes11-fail').addEventListener('click', () => { set('error', 'Failed'); retry.focus(); });
})();
```
