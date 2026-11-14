---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-dashboard-no-data-state/"
title: "Tailwind CSS Empty Dashboard / No Data State"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "An analytics dashboard before its first event: four chart cards drawn as quiet ghosts under a frosted \"Connect a source\" panel."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Empty Dashboard / No Data State
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-empty-dashboard-no-data-state/

An analytics dashboard before its first event: four chart cards drawn as quiet ghosts under a frosted "Connect a source" panel. Pick a source and the panel steps aside while every chart animates into real data — bars grow to h-(--h), the line draws via stroke-dashoffset, cohort cells fade up — all from a single data-live attribute.
## HTML
```html
<div class="tes-07 group/root w-full min-h-svh bg-tes07-bg font-tes07-sans text-tes07-ink antialiased">
  <div class="grid min-h-svh md:grid-cols-[13.5rem_minmax(0,1fr)]">
    <aside class="hidden flex-col gap-6 border-r border-tes07-line bg-tes07-card p-4 md:flex">
      <span class="flex items-center gap-2 px-2 pt-1 text-[15px] font-semibold"><span aria-hidden="true" class="size-5 rounded-md bg-[conic-gradient(from_200deg,var(--color-tes07-c1),var(--color-tes07-c2),var(--color-tes07-c3),var(--color-tes07-c1))]"></span>Cadence</span>
      <nav class="grid gap-0.5 text-sm">
        <a href="#" aria-current="page" class="flex min-h-10 items-center rounded-lg bg-tes07-sunk px-3 font-medium focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Overview</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes07-mut hover:bg-tes07-sunk hover:text-tes07-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Funnels</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes07-mut hover:bg-tes07-sunk hover:text-tes07-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Retention</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes07-mut hover:bg-tes07-sunk hover:text-tes07-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Sources</a>
        <a href="#" class="flex min-h-10 items-center rounded-lg px-3 text-tes07-mut hover:bg-tes07-sunk hover:text-tes07-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Settings</a>
      </nav>
      <p class="mt-auto flex items-center gap-2 rounded-lg bg-tes07-sunk px-3 py-2.5 text-xs text-tes07-mut"><i aria-hidden="true" class="size-2 rounded-full bg-tes07-line2 group-data-live/root:bg-tes07-ok group-data-live/root:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tes07-ok)_20%,transparent)]"></i><span id="tes07-status" role="status">No source connected</span></p>
    </aside>
    <main class="relative flex min-w-0 flex-col gap-5 px-[clamp(1rem,4vw,2.5rem)] py-6">
      <header class="flex flex-wrap items-center justify-between gap-3">
        <h1 class="text-2xl font-semibold tracking-tight">Overview</h1>
        <div role="group" aria-label="Date range" class="flex rounded-xl bg-tes07-sunk p-1 text-sm">
          <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3 text-tes07-mut focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">24h</button>
          <button type="button" aria-pressed="true" class="min-h-10 rounded-lg bg-tes07-card px-3 font-medium shadow-xs focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">7d</button>
          <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3 text-tes07-mut focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">30d</button>
          <button type="button" aria-pressed="false" class="min-h-10 rounded-lg px-3 text-tes07-mut focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Quarter</button>
        </div>
      </header>
      <section aria-hidden="true" class="relative grid flex-1 grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <article class="grid gap-3 rounded-2xl bg-tes07-card p-5 ring-1 ring-tes07-line sm:col-span-2">
          <div class="flex items-baseline justify-between"><p class="text-sm text-tes07-mut">Sessions</p><p class="font-tes07-mono text-xl font-medium text-tes07-line2 transition-colors duration-700 group-data-live/root:text-tes07-ink">—<span class="hidden group-data-live/root:inline">12,480</span></p></div>
          <svg viewBox="0 0 320 110" preserveAspectRatio="none" class="h-36 w-full"><path d="M0 100H320" stroke="var(--color-tes07-line)" stroke-dasharray="4 4"/><path d="M0 92 C40 88 60 70 90 74 S140 40 170 48 S220 22 250 30 S300 12 320 8" fill="none" stroke="var(--color-tes07-c1)" stroke-width="2.5" stroke-linecap="round" class="[stroke-dasharray:640] [stroke-dashoffset:640] transition-[stroke-dashoffset] duration-[1400ms] ease-out group-data-live/root:[stroke-dashoffset:0]"/></svg>
        </article>
        <article class="grid gap-3 rounded-2xl bg-tes07-card p-5 ring-1 ring-tes07-line">
          <p class="text-sm text-tes07-mut">Conversion</p>
          <div class="grid place-items-center py-2"><span class="grid size-28 place-items-center rounded-full bg-[conic-gradient(var(--color-tes07-line)_0_100%)] transition-all duration-700 group-data-live/root:bg-[conic-gradient(var(--color-tes07-c2)_0_38%,var(--color-tes07-sunk)_0)]"><span class="grid size-20 place-items-center rounded-full bg-tes07-card font-tes07-mono text-lg text-tes07-line2 group-data-live/root:text-tes07-ink">—<span class="hidden group-data-live/root:inline">3.8%</span></span></span></div>
        </article>
        <article class="grid gap-3 rounded-2xl bg-tes07-card p-5 ring-1 ring-tes07-line">
          <p class="text-sm text-tes07-mut">Top channels</p>
          <div class="flex h-32 items-end gap-3">
            <i style="--h:88%" class="h-[12%] flex-1 rounded-t-md bg-tes07-sunk transition-[height,background-color] duration-700 group-data-live/root:h-(--h) group-data-live/root:bg-tes07-c1"></i>
            <i style="--h:64%" class="h-[12%] flex-1 rounded-t-md bg-tes07-sunk transition-[height,background-color] delay-75 duration-700 group-data-live/root:h-(--h) group-data-live/root:bg-tes07-c1/80"></i>
            <i style="--h:41%" class="h-[12%] flex-1 rounded-t-md bg-tes07-sunk transition-[height,background-color] delay-150 duration-700 group-data-live/root:h-(--h) group-data-live/root:bg-tes07-c1/60"></i>
            <i style="--h:22%" class="h-[12%] flex-1 rounded-t-md bg-tes07-sunk transition-[height,background-color] delay-200 duration-700 group-data-live/root:h-(--h) group-data-live/root:bg-tes07-c1/40"></i>
          </div>
        </article>
        <article class="grid gap-3 rounded-2xl bg-tes07-card p-5 ring-1 ring-tes07-line sm:col-span-2 xl:col-span-4">
          <p class="text-sm text-tes07-mut">Retention cohorts</p>
          <div class="grid grid-cols-6 gap-1.5 sm:grid-cols-12">
            <i style="--o:1" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.86" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.74" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.66" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.58" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.5" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.45" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.4" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.36" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.32" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.29" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i><i style="--o:.26" class="h-9 rounded-md bg-tes07-sunk transition duration-700 group-data-live/root:bg-tes07-c3 group-data-live/root:opacity-(--o)"></i>
          </div>
        </article>
      </section>
      <div class="absolute inset-x-0 top-20 bottom-0 grid place-items-center p-6 transition-[opacity,visibility] duration-500 group-data-live/root:invisible group-data-live/root:opacity-0">
        <div class="grid w-full max-w-md justify-items-center rounded-3xl bg-tes07-card p-7 text-center shadow-[0_30px_80px_-30px_oklch(0.3_0.1_290/0.35)] ring-1 ring-tes07-line supports-[backdrop-filter:blur(1px)]:bg-tes07-card/75 supports-[backdrop-filter:blur(1px)]:backdrop-blur-md">
          <span aria-hidden="true" class="relative grid size-14 place-items-center rounded-2xl bg-tes07-acc text-white"><span class="absolute inset-0 animate-ping rounded-2xl bg-tes07-acc/30 motion-reduce:hidden"></span><svg class="relative size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M8 4v5M16 4v5M6 9h12v3a6 6 0 0 1-12 0zM12 18v3"/></svg></span>
          <h2 id="tes07-ph" class="mt-5 text-xl font-semibold tracking-tight">Nothing to chart yet</h2>
          <p id="tes07-pp" class="mt-2 text-sm/6 text-tes07-mut text-pretty">Connect a source and the first events land in about a minute. Charts fill in as they arrive.</p>
          <div id="tes07-acts" class="mt-5 flex flex-wrap justify-center gap-2.5">
            <button type="button" id="tes07-connect" class="min-h-11 rounded-xl bg-tes07-ink px-5 text-sm font-medium text-white transition hover:bg-tes07-acc active:scale-[.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Connect a source</button>
            <button type="button" class="min-h-11 rounded-xl border border-tes07-line2 px-4 text-sm transition hover:bg-tes07-sunk focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Paste a tracking snippet</button>
          </div>
          <ul id="tes07-sources" hidden class="mt-5 grid w-full grid-cols-2 gap-2">
            <li><button type="button" data-src="Postgres" class="min-h-12 w-full rounded-xl border border-tes07-line text-sm font-medium transition hover:-translate-y-0.5 hover:border-tes07-acc hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Postgres</button></li>
            <li><button type="button" data-src="Stripe" class="min-h-12 w-full rounded-xl border border-tes07-line text-sm font-medium transition hover:-translate-y-0.5 hover:border-tes07-acc hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Stripe</button></li>
            <li><button type="button" data-src="Segment" class="min-h-12 w-full rounded-xl border border-tes07-line text-sm font-medium transition hover:-translate-y-0.5 hover:border-tes07-acc hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Segment</button></li>
            <li><button type="button" data-src="Webhook" class="min-h-12 w-full rounded-xl border border-tes07-line text-sm font-medium transition hover:-translate-y-0.5 hover:border-tes07-acc hover:shadow-md focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Webhook</button></li>
          </ul>
        </div>
      </div>
      <button type="button" id="tes07-reset" class="hidden min-h-11 self-start rounded-lg px-2 text-xs text-tes07-mut underline-offset-4 hover:text-tes07-ink hover:underline group-data-live/root:block focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes07-acc">Disconnect source</button>
    </main>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes07-bg: #f6f5fa;
  --color-tes07-bg: oklch(0.972 0.006 295);
  --color-tes07-card: #ffffff;
  --color-tes07-card: oklch(1 0 0);
  --color-tes07-sunk: #efedf5;
  --color-tes07-sunk: oklch(0.947 0.009 295);
  --color-tes07-line: #e2dfec;
  --color-tes07-line: oklch(0.905 0.014 295);
  --color-tes07-line2: #c3bfd2;
  --color-tes07-line2: oklch(0.81 0.022 295);
  --color-tes07-ink: #1c1828;
  --color-tes07-ink: oklch(0.21 0.025 295);
  --color-tes07-mut: #5f5a70;
  --color-tes07-mut: oklch(0.48 0.028 295);
  --color-tes07-acc: #6c3fe0;
  --color-tes07-acc: oklch(0.5 0.22 290);
  --color-tes07-c1: #6c3fe0;
  --color-tes07-c1: oklch(0.5 0.22 290);
  --color-tes07-c2: #e0457b;
  --color-tes07-c2: oklch(0.62 0.19 5);
  --color-tes07-c3: #2a8fd8;
  --color-tes07-c3: oklch(0.6 0.14 245);
  --color-tes07-ok: #1d9a6c;
  --color-tes07-ok: oklch(0.6 0.13 160);
  --font-tes07-sans: 'Geist', system-ui, sans-serif;
  --font-tes07-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-07 {
  width: 100%;
  min-height: 100svh;
}

.tes-07 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-07');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const sources = $('#tes07-sources');
  const reset = () => {
    root.removeAttribute('data-live');
    sources.hidden = true; $('#tes07-acts').hidden = false;
    $('#tes07-ph').textContent = 'Nothing to chart yet';
    $('#tes07-pp').textContent = 'Connect a source and the first events land in about a minute. Charts fill in as they arrive.';
    $('#tes07-status').textContent = 'No source connected';
  };
  $('#tes07-connect').addEventListener('click', () => {
    sources.hidden = false; $('#tes07-acts').hidden = true;
    $('#tes07-ph').textContent = 'Pick a source';
    $('#tes07-pp').textContent = 'Read-only credentials are enough. You can add more later.';
    sources.querySelector('button').focus();
  });
  sources.addEventListener('click', (e) => {
    const b = e.target.closest('[data-src]');
    if (!b) return;
    $('#tes07-status').textContent = b.dataset.src + ' syncing';
    $('#tes07-ph').textContent = 'First events arriving';
    $('#tes07-pp').textContent = b.dataset.src + ' is connected. Charts fill in as the backfill lands.';
    sources.hidden = true;
    setTimeout(() => { root.setAttribute('data-live', ''); $('#tes07-status').textContent = b.dataset.src + ' live'; $('#tes07-reset').focus(); }, 900);
  });
  $('#tes07-reset').addEventListener('click', reset);
})();
```
