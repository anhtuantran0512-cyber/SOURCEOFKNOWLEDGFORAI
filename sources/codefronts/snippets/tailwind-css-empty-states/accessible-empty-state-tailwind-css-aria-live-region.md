---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/accessible-empty-state-tailwind-css-aria-live-region/"
title: "Accessible Empty State in Tailwind CSS (ARIA Live Region)"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "An archive catalogue search built to be heard as well as seen: a skip link revealed with focus:not-sr-only, a visually hidden role=\"status\" region that…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Empty State in Tailwind CSS (ARIA Live Region)
Source: https://codefronts.com/snippets/tailwind-css-empty-states/accessible-empty-state-tailwind-css-aria-live-region/

An archive catalogue search built to be heard as well as seen: a skip link revealed with focus:not-sr-only, a visually hidden role="status" region that announces "No catalogue entries for…" or "3 entries found", focus moved to the results heading, and suggestion chips that re-run the search.
## HTML
```html
<div class="tes-17 w-full min-h-svh bg-tes17-bg font-tes17-sans text-tes17-ink antialiased">
  <a href="#tes17-results" class="sr-only rounded-lg bg-tes17-ink px-4 py-3 text-sm font-medium text-white focus:not-sr-only focus:absolute focus:top-3 focus:left-3 focus:z-10 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">Skip to results</a>
  <header class="flex flex-wrap items-center gap-x-8 gap-y-2 border-b border-tes17-line px-[clamp(1rem,4vw,3rem)] py-4">
    <span class="font-tes17-serif text-2xl">Ordnance Library</span>
    <nav aria-label="Catalogue" class="flex gap-5 text-sm text-tes17-mut"><a href="#" class="py-2 hover:text-tes17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">Maps</a><a href="#" class="py-2 hover:text-tes17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">Surveys</a><a href="#" class="py-2 hover:text-tes17-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">Photographs</a></nav>
  </header>
  <main class="mx-auto grid w-full max-w-3xl gap-8 px-[clamp(1rem,4vw,3rem)] py-[clamp(2rem,6vw,4rem)]">
    <div role="search" class="grid gap-2">
      <label for="tes17-q" class="text-sm font-semibold">Search the catalogue</label>
      <div class="flex min-h-13 items-center gap-2 rounded-xl border-2 border-tes17-line2 bg-tes17-card pr-1.5 pl-4 transition focus-within:border-tes17-acc focus-within:ring-4 focus-within:ring-tes17-acc/20">
        <svg class="size-5 flex-none text-tes17-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg>
        <input type="search" id="tes17-q" value="tidal survey 1974" autocomplete="off" aria-describedby="tes17-hint" aria-controls="tes17-results" class="min-w-0 flex-1 bg-transparent py-2 text-base outline-none">
        <button type="button" id="tes17-go" class="min-h-11 rounded-lg bg-tes17-ink px-5 text-sm font-semibold text-white hover:bg-tes17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">Search</button>
      </div>
      <p id="tes17-hint" class="text-[13px] text-tes17-mut">Type at least two characters. Results update when you press Search or Enter.</p>
    </div>
    <div id="tes17-live" role="status" aria-live="polite" aria-atomic="true" class="sr-only"></div>
    <section id="tes17-results" tabindex="-1" aria-labelledby="tes17-rh" class="grid gap-4 rounded-2xl outline-none focus-visible:ring-4 focus-visible:ring-tes17-acc/25">
      <h2 id="tes17-rh" class="flex items-baseline justify-between border-b border-tes17-line pb-2 text-sm font-semibold">Results<span id="tes17-n" class="font-tes17-mono text-xs font-normal text-tes17-mut">0 entries</span></h2>
      <div id="tes17-empty" class="grid justify-items-start gap-3 rounded-2xl bg-tes17-card p-[clamp(1.25rem,4vw,2rem)] ring-1 ring-tes17-line">
        <span aria-hidden="true" class="grid size-12 place-items-center rounded-xl bg-tes17-acc/10 text-tes17-acc"><svg class="size-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H10l2 2h6.5A1.5 1.5 0 0 1 20 7.5v11a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 18.5z"/><path d="M9.5 13.5h5"/></svg></span>
        <p class="text-lg font-semibold">No catalogue entries for that phrase</p>
        <p class="max-w-[52ch] text-sm/6 text-tes17-mut text-pretty">Sheet numbers are indexed without spaces, and surveys before 1980 are filed by county rather than year.</p>
        <p class="pt-1 text-xs font-medium text-tes17-mut">Try one of these</p>
        <ul class="flex flex-wrap gap-2">
          <li><button type="button" data-q="tidal survey" class="min-h-11 rounded-full border border-tes17-line2 bg-tes17-bg px-4 text-sm hover:border-tes17-acc hover:text-tes17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">tidal survey</button></li>
          <li><button type="button" data-q="devon" class="min-h-11 rounded-full border border-tes17-line2 bg-tes17-bg px-4 text-sm hover:border-tes17-acc hover:text-tes17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">devon</button></li>
          <li><button type="button" data-q="sheet 118" class="min-h-11 rounded-full border border-tes17-line2 bg-tes17-bg px-4 text-sm hover:border-tes17-acc hover:text-tes17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes17-acc">sheet 118</button></li>
        </ul>
      </div>
      <ol id="tes17-list" hidden class="divide-y divide-tes17-line overflow-hidden rounded-2xl bg-tes17-card ring-1 ring-tes17-line"></ol>
    </section>
  </main>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes17-bg: #f7f6f2;
  --color-tes17-bg: oklch(0.973 0.006 95);
  --color-tes17-card: #ffffff;
  --color-tes17-card: oklch(1 0 0);
  --color-tes17-line: #dedbd2;
  --color-tes17-line: oklch(0.89 0.012 95);
  --color-tes17-line2: #a9a596;
  --color-tes17-line2: oklch(0.72 0.02 95);
  --color-tes17-ink: #191914;
  --color-tes17-ink: oklch(0.2 0.008 100);
  --color-tes17-mut: #57564d;
  --color-tes17-mut: oklch(0.44 0.013 100);
  --color-tes17-acc: #1b5fbf;
  --color-tes17-acc: oklch(0.49 0.16 258);
  --font-tes17-sans: 'Geist', system-ui, sans-serif;
  --font-tes17-serif: 'Instrument Serif', Georgia, serif;
  --font-tes17-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-17 {
  width: 100%;
  min-height: 100svh;
}

.tes-17 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-17');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const $ = (s) => root.querySelector(s);
  const input = $('#tes17-q'), live = $('#tes17-live'), empty = $('#tes17-empty'), list = $('#tes17-list'), results = $('#tes17-results'), n = $('#tes17-n');
  const catalogue = [
    ['Tidal survey of the Exe estuary', 'SURV-1974-118 \u00b7 Devon \u00b7 1974'],
    ['Coastal profile, Teignmouth to Dawlish', 'SURV-1974-121 \u00b7 Devon \u00b7 1974'],
    ['Sheet 118, first edition', 'MAP-118-1 \u00b7 Devon \u00b7 1969']
  ];
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const announce = (msg) => { live.textContent = ''; setTimeout(() => { live.textContent = msg; }, 40); };
  const run = (q, focus) => {
    const term = q.trim().toLowerCase();
    const hits = term.length < 2 ? [] : catalogue.filter((r) => (r[0] + ' ' + r[1]).toLowerCase().includes(term));
    empty.hidden = hits.length > 0; list.hidden = !hits.length;
    list.innerHTML = hits.map((r) => '<li class="grid gap-0.5 px-5 py-4"><span class="font-medium">' + r[0] + '</span><span class="font-tes17-mono text-xs text-tes17-mut">' + r[1] + '</span></li>').join('');
    n.textContent = hits.length + (hits.length === 1 ? ' entry' : ' entries');
    announce(hits.length ? hits.length + (hits.length === 1 ? ' entry' : ' entries') + ' found for ' + q : 'No catalogue entries for ' + q + '. Three suggested searches are listed.');
    if (focus) results.focus();
  };
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); run(input.value, true); } });
  $('#tes17-go').addEventListener('click', () => run(input.value, true));
  root.addEventListener('click', (e) => {
    const t = e.target.closest('[data-q]');
    if (!t) return;
    input.value = t.dataset.q; run(t.dataset.q, true);
  });
  run(input.value, false);
})();
```
