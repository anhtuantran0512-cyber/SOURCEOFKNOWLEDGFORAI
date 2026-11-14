---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-no-search-results-empty-state/"
title: "Tailwind CSS No Search Results Empty State"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A zero-result search inside a dark issue tracker, ported to utilities: removable filter chips, a scope tab bar and an empty block that names which filter…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS No Search Results Empty State
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-no-search-results-empty-state/

A zero-result search inside a dark issue tracker, ported to utilities: removable filter chips, a scope tab bar and an empty block that names which filter caused the miss. The page state lives in one data-state attribute on the root, and group-data-[state=found]/root: swaps the empty block for the result list — the script never touches a class.
## HTML
```html
<div class="tes-01 group/root w-full min-h-svh bg-tes01-bg font-tes01-sans text-tes01-ink antialiased [color-scheme:dark]" data-state="empty">
  <div class="grid min-h-svh grid-cols-[4.25rem_minmax(0,1fr)]">
    <nav aria-label="Workspace" class="flex flex-col items-center gap-1.5 border-r border-tes01-line bg-linear-to-b from-tes01-panel to-tes01-bg px-3 pt-4 pb-5">
      <span aria-hidden="true" class="mb-3 grid size-9 place-items-center rounded-[11px] bg-tes01-ink text-tes01-bg"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 17.5 12 4l7 13.5M8.4 17.5h7.2"/></svg></span>
      <button type="button" aria-label="Issues" aria-current="page" class="grid size-11 place-items-center rounded-xl border border-tes01-line2 bg-tes01-panel2 text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="7.5"/><path d="M12 8.4v4.2M12 15.5h.01"/></svg></button>
      <button type="button" aria-label="Pull requests" class="grid size-11 place-items-center rounded-xl text-tes01-faint transition-colors hover:bg-tes01-panel2 hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="7" cy="6.5" r="2.3"/><circle cx="7" cy="17.5" r="2.3"/><circle cx="17" cy="17.5" r="2.3"/><path d="M7 8.8v6.4M9.3 6.5h5.2a2.5 2.5 0 0 1 2.5 2.5v6.2"/></svg></button>
      <button type="button" aria-label="Deployments" class="grid size-11 place-items-center rounded-xl text-tes01-faint transition-colors hover:bg-tes01-panel2 hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 15.5 12 4l8 11.5M4.5 19.5h15"/></svg></button>
      <button type="button" aria-label="Insights" class="grid size-11 place-items-center rounded-xl text-tes01-faint transition-colors hover:bg-tes01-panel2 hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc"><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 19V6M20 19H4M8 15.5V11M12.5 15.5V8M17 15.5v-3"/></svg></button>
      <span aria-hidden="true" class="mt-auto grid size-8 place-items-center rounded-full bg-linear-to-br from-tes01-acc to-tes01-open font-tes01-mono text-[11px] font-semibold text-tes01-bg">AR</span>
    </nav>
    <div class="flex min-w-0 flex-col">
      <header class="grid gap-3 border-b border-tes01-line px-[clamp(1rem,3vw,2rem)] pt-4">
        <div class="flex h-12 items-center gap-2.5 rounded-xl border border-tes01-line2 bg-tes01-panel pr-1.5 pl-3.5 shadow-[inset_0_1px_0_rgb(255_255_255/0.04)]">
          <svg class="size-[18px] flex-none text-tes01-faint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg>
          <span id="tes01-query" class="min-w-0 flex-1 truncate font-tes01-mono text-[13px]">is:open label:regression owner:platform</span>
          <kbd class="hidden rounded-md border border-tes01-line2 px-1.5 py-0.5 font-tes01-mono text-[11px] text-tes01-faint sm:block">/</kbd>
          <button type="button" data-act="clear" aria-label="Clear search" class="grid size-9 place-items-center rounded-lg text-tes01-faint transition-colors hover:bg-tes01-panel2 hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></button>
        </div>
        <div class="flex items-end justify-between gap-4">
          <div role="tablist" aria-label="Search scope" class="-mb-px flex gap-1 overflow-x-auto">
            <button type="button" role="tab" aria-selected="true" class="min-h-11 border-b-2 border-tes01-acc px-3 text-[13px] font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Issues</button>
            <button type="button" role="tab" aria-selected="false" class="min-h-11 border-b-2 border-transparent px-3 text-[13px] text-tes01-mut transition-colors hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Pull requests</button>
            <button type="button" role="tab" aria-selected="false" class="min-h-11 border-b-2 border-transparent px-3 text-[13px] text-tes01-mut transition-colors hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Discussions</button>
          </div>
          <p id="tes01-count" role="status" class="flex-none pb-3 font-tes01-mono text-xs text-tes01-faint">0 results</p>
        </div>
      </header>
      <div class="flex flex-wrap items-center gap-2 px-[clamp(1rem,3vw,2rem)] py-3.5">
        <span class="mr-1 text-xs text-tes01-faint">Filters</span>
        <button type="button" data-chip="is:open" data-drop="is:open" aria-label="Remove filter is:open" class="relative inline-flex h-9 items-center gap-1.5 rounded-full border border-tes01-line2 bg-tes01-panel pr-2 pl-3 font-tes01-mono text-xs transition after:absolute after:-inset-1 hover:border-tes01-acc/60 hover:bg-tes01-panel2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">is:open<svg class="size-3.5 text-tes01-faint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></button>
        <button type="button" data-chip="label:regression" data-drop="label:regression" aria-label="Remove filter label:regression" class="relative inline-flex h-9 items-center gap-1.5 rounded-full border border-tes01-warn/40 bg-tes01-warn/10 pr-2 pl-3 font-tes01-mono text-xs text-tes01-warn transition after:absolute after:-inset-1 hover:border-tes01-warn/70 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">label:regression<svg class="size-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></button>
        <button type="button" data-chip="owner:platform" data-drop="owner:platform" aria-label="Remove filter owner:platform" class="relative inline-flex h-9 items-center gap-1.5 rounded-full border border-tes01-line2 bg-tes01-panel pr-2 pl-3 font-tes01-mono text-xs transition after:absolute after:-inset-1 hover:border-tes01-acc/60 hover:bg-tes01-panel2 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">owner:platform<svg class="size-3.5 text-tes01-faint" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17"/></svg></button>
      </div>
      <section aria-label="Results" class="flex flex-1 flex-col px-[clamp(1rem,3vw,2rem)] pb-10">
        <div class="grid flex-1 place-items-center py-12 group-data-[state=found]/root:hidden">
          <div class="relative grid max-w-md justify-items-center text-center">
            <span aria-hidden="true" class="pointer-events-none absolute -top-20 left-1/2 h-72 w-[min(34rem,90vw)] -translate-x-1/2 bg-[radial-gradient(var(--color-tes01-line2)_1px,transparent_1.5px)] bg-size-[16px_16px] [mask-image:radial-gradient(closest-side,#000,transparent)]"></span>
            <span aria-hidden="true" class="relative grid size-18 place-items-center rounded-2xl border border-tes01-line2 bg-linear-to-b from-tes01-panel2 to-tes01-panel text-tes01-acc shadow-[0_0_0_6px_var(--color-tes01-bg),0_24px_60px_-12px_color-mix(in_oklab,var(--color-tes01-acc)_50%,transparent)]"><svg class="size-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.4"/><path d="m15.4 15.4 4.1 4.1M8 10.5h5"/></svg></span>
            <h1 class="relative mt-7 text-xl font-semibold tracking-tight text-balance">No issues match all three filters</h1>
            <p class="relative mt-2 text-sm/6 text-tes01-mut text-pretty">Platform has nothing open labelled <code class="rounded bg-tes01-warn/10 px-1 font-tes01-mono text-[12.5px] text-tes01-warn">regression</code>. Loosen one filter to widen the search.</p>
            <div class="relative mt-7 flex flex-wrap justify-center gap-2.5">
              <button type="button" data-drop="label:regression" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tes01-ink px-4 text-sm font-medium text-tes01-bg transition hover:bg-white active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Drop label:regression<span class="rounded-md bg-tes01-bg/10 px-1.5 py-0.5 font-tes01-mono text-[11px]">3</span></button>
              <button type="button" data-act="clear" class="min-h-11 rounded-xl border border-tes01-line2 px-4 text-sm transition hover:bg-tes01-panel2 active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Search every repository</button>
            </div>
            <p class="relative mt-7 text-xs text-tes01-faint">Press <kbd class="rounded border border-tes01-line2 px-1 font-tes01-mono">/</kbd> to edit the query · <a href="#" class="text-tes01-mut underline decoration-tes01-line2 underline-offset-4 hover:text-tes01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Search syntax</a></p>
          </div>
        </div>
        <div class="hidden group-data-[state=found]/root:block">
          <div class="flex items-center justify-between gap-3 pb-2">
            <p class="text-xs text-tes01-faint">Showing matches with fewer filters</p>
            <button type="button" data-act="restore" class="min-h-11 rounded-lg px-2 text-xs font-medium text-tes01-acc hover:underline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes01-acc">Restore all filters</button>
          </div>
          <ol class="divide-y divide-tes01-line overflow-hidden rounded-xl border border-tes01-line bg-tes01-panel">
            <li class="flex items-center gap-3.5 px-4 py-3.5 transition-[opacity,translate] duration-300 hover:bg-tes01-panel2 starting:translate-y-1 starting:opacity-0">
              <span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tes01-open shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tes01-open)_18%,transparent)]"></span>
              <span class="grid min-w-0 flex-1 gap-0.5"><span class="truncate text-sm font-medium">Retry storm when the queue drains mid-deploy</span><span class="truncate font-tes01-mono text-xs text-tes01-faint">platform/edge-router · #4821 · opened by dcheng</span></span>
              <span class="hidden flex-none rounded-full border border-tes01-warn/40 px-2.5 py-1 text-[11px] text-tes01-warn sm:block">needs triage</span>
            </li>
            <li class="flex items-center gap-3.5 px-4 py-3.5 transition-[opacity,translate] delay-75 duration-300 hover:bg-tes01-panel2 starting:translate-y-1 starting:opacity-0">
              <span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tes01-open shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tes01-open)_18%,transparent)]"></span>
              <span class="grid min-w-0 flex-1 gap-0.5"><span class="truncate text-sm font-medium">Token refresh drops the websocket session</span><span class="truncate font-tes01-mono text-xs text-tes01-faint">platform/auth · #4804 · opened by mira.k</span></span>
              <span class="hidden flex-none rounded-full border border-tes01-acc/40 px-2.5 py-1 text-[11px] text-tes01-acc sm:block">in review</span>
            </li>
            <li class="flex items-center gap-3.5 px-4 py-3.5 transition-[opacity,translate] delay-150 duration-300 hover:bg-tes01-panel2 starting:translate-y-1 starting:opacity-0">
              <span aria-hidden="true" class="size-2.5 flex-none rounded-full bg-tes01-faint"></span>
              <span class="grid min-w-0 flex-1 gap-0.5"><span class="truncate text-sm font-medium text-tes01-mut">Cold start regression on the image pipeline</span><span class="truncate font-tes01-mono text-xs text-tes01-faint">platform/media · #4790 · opened by t.oyelaran</span></span>
              <span class="hidden flex-none rounded-full border border-tes01-line2 px-2.5 py-1 text-[11px] text-tes01-faint sm:block">closed</span>
            </li>
          </ol>
        </div>
      </section>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes01-bg: #101217;
  --color-tes01-bg: oklch(0.16 0.011 265);
  --color-tes01-panel: #161920;
  --color-tes01-panel: oklch(0.203 0.013 265);
  --color-tes01-panel2: #1c2029;
  --color-tes01-panel2: oklch(0.235 0.015 265);
  --color-tes01-line: #272b34;
  --color-tes01-line: oklch(0.29 0.014 265);
  --color-tes01-line2: #333945;
  --color-tes01-line2: oklch(0.345 0.016 265);
  --color-tes01-ink: #f1f3f7;
  --color-tes01-ink: oklch(0.965 0.004 265);
  --color-tes01-mut: #a6adbd;
  --color-tes01-mut: oklch(0.75 0.021 265);
  --color-tes01-faint: #808898;
  --color-tes01-faint: oklch(0.63 0.021 265);
  --color-tes01-acc: #8db0ff;
  --color-tes01-acc: oklch(0.775 0.115 262);
  --color-tes01-open: #4ade80;
  --color-tes01-open: oklch(0.82 0.17 152);
  --color-tes01-warn: #f5b661;
  --color-tes01-warn: oklch(0.82 0.11 72);
  --font-tes01-sans: 'Geist', system-ui, sans-serif;
  --font-tes01-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-01 {
  width: 100%;
  min-height: 100svh;
}

.tes-01 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-01');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const base = ['is:open', 'label:regression', 'owner:platform'];
  const query = root.querySelector('#tes01-query');
  const count = root.querySelector('#tes01-count');
  let live = base.slice();
  const paint = () => {
    root.querySelectorAll('[data-chip]').forEach((c) => { c.hidden = !live.includes(c.dataset.chip); });
    query.textContent = live.length ? live.join(' ') : 'all repositories';
    const found = live.length < 3;
    root.dataset.state = found ? 'found' : 'empty';
    count.textContent = found ? '3 results' : '0 results';
  };
  root.addEventListener('click', (e) => {
    const drop = e.target.closest('[data-drop]');
    const act = e.target.closest('[data-act]');
    if (drop) live = live.filter((t) => t !== drop.dataset.drop);
    else if (act) live = act.dataset.act === 'restore' ? base.slice() : [];
    else return;
    paint();
  });
  paint();
})();
```
