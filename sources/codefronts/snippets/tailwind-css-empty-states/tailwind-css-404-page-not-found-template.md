---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-404-page-not-found-template/"
title: "Tailwind CSS 404 Page Not Found Template"
section: "snippets"
category: "tailwind-css-empty-states"
category_name: "Tailwind CSS Empty States"
description: "A newspaper's 404 that apologises like an editor: a tall serif numeral, an explanation of why the link broke (the archive rebuild), live archive search with…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS 404 Page Not Found Template
Source: https://codefronts.com/snippets/tailwind-css-empty-states/tailwind-css-404-page-not-found-template/

A newspaper's 404 that apologises like an editor: a tall serif numeral, an explanation of why the link broke (the archive rebuild), live archive search with highlighted matches, and a numbered "Most read" list. The list numbers come from a CSS counter in utilities — [counter-increment:tes14] before:content-[counter(tes14,decimal-leading-zero)].
## HTML
```html
<div class="tes-14 flex w-full min-h-svh flex-col bg-tes14-bg font-tes14-sans text-tes14-ink antialiased">
  <header class="flex flex-wrap items-center gap-x-8 gap-y-2 border-b-2 border-tes14-ink px-[clamp(1rem,4vw,3rem)] py-4">
    <a href="#" class="font-tes14-serif text-[1.7rem] leading-none tracking-tight focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">The Long Field</a>
    <nav aria-label="Sections" class="order-3 flex w-full gap-5 overflow-x-auto text-sm text-tes14-mut sm:order-none sm:w-auto sm:flex-1">
      <a href="#" class="py-2 hover:text-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Reporting</a><a href="#" class="py-2 hover:text-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Essays</a><a href="#" class="py-2 hover:text-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Interviews</a><a href="#" class="py-2 hover:text-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Archive</a>
    </nav>
    <a href="#" class="ml-auto inline-flex min-h-10 items-center rounded-full bg-tes14-acc px-4 text-sm font-medium text-white hover:bg-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Subscribe</a>
  </header>
  <main class="mx-auto grid w-full max-w-6xl flex-1 gap-12 px-[clamp(1rem,4vw,3rem)] py-[clamp(2rem,6vw,4.5rem)] lg:grid-cols-[minmax(0,1.5fr)_minmax(0,1fr)]">
    <div class="grid content-start gap-5">
      <p aria-hidden="true" class="bg-[linear-gradient(180deg,var(--color-tes14-ink)_30%,var(--color-tes14-acc))] bg-clip-text font-tes14-serif text-[clamp(6rem,20vw,12rem)] leading-[0.8] tracking-[-0.04em] text-transparent">404</p>
      <h1 class="font-tes14-serif text-[clamp(2rem,4.5vw,3rem)] leading-[1.05] tracking-tight text-balance">This page has been <em>unwritten</em></h1>
      <p class="max-w-[54ch] text-[15px]/7 text-tes14-mut text-pretty">The link you followed points at something we moved during the archive rebuild. The writing still exists — it just lives at a different address now.</p>
      <div role="search" class="grid max-w-xl gap-2 pt-2">
        <label for="tes14-input" class="text-sm font-medium">Search the archive</label>
        <div class="flex min-h-12 items-center gap-2 rounded-full border border-tes14-line2 bg-tes14-card pr-1.5 pl-4 transition focus-within:border-tes14-ink focus-within:ring-4 focus-within:ring-tes14-acc/15">
          <svg class="size-4.5 flex-none text-tes14-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4 4"/></svg>
          <input type="search" id="tes14-input" placeholder="A title, a name, a year" autocomplete="off" aria-controls="tes14-sugg" class="min-w-0 flex-1 bg-transparent py-2 text-[15px] outline-none placeholder:text-tes14-mut">
          <button type="button" id="tes14-go" class="min-h-10 rounded-full bg-tes14-ink px-4 text-sm font-medium text-white hover:bg-tes14-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Search</button>
        </div>
        <ul id="tes14-sugg" hidden aria-live="polite" class="divide-y divide-tes14-line overflow-hidden rounded-2xl border border-tes14-line bg-tes14-card"></ul>
      </div>
    </div>
    <aside aria-labelledby="tes14-mr" class="grid content-start gap-2 lg:border-l lg:border-tes14-line lg:pl-10">
      <p id="tes14-mr" class="border-b border-tes14-ink pb-2 text-xs font-semibold tracking-[0.16em] uppercase">Most read this month</p>
      <ol class="[counter-reset:tes14]">
        <li class="border-b border-tes14-line [counter-increment:tes14]"><a href="#" class="group flex gap-4 py-4 before:font-tes14-serif before:text-3xl before:leading-none before:text-tes14-acc before:content-[counter(tes14,decimal-leading-zero)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc"><span class="grid gap-1"><span class="text-[11px] font-semibold tracking-[0.14em] text-tes14-mut uppercase">Reporting</span><span class="font-tes14-serif text-xl leading-snug group-hover:underline group-hover:decoration-tes14-acc group-hover:underline-offset-4">The village that bought its own grid</span></span></a></li>
        <li class="border-b border-tes14-line [counter-increment:tes14]"><a href="#" class="group flex gap-4 py-4 before:font-tes14-serif before:text-3xl before:leading-none before:text-tes14-acc before:content-[counter(tes14,decimal-leading-zero)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc"><span class="grid gap-1"><span class="text-[11px] font-semibold tracking-[0.14em] text-tes14-mut uppercase">Essay</span><span class="font-tes14-serif text-xl leading-snug group-hover:underline group-hover:decoration-tes14-acc group-hover:underline-offset-4">In defence of the slow newsroom</span></span></a></li>
        <li class="border-b border-tes14-line [counter-increment:tes14]"><a href="#" class="group flex gap-4 py-4 before:font-tes14-serif before:text-3xl before:leading-none before:text-tes14-acc before:content-[counter(tes14,decimal-leading-zero)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc"><span class="grid gap-1"><span class="text-[11px] font-semibold tracking-[0.14em] text-tes14-mut uppercase">Interview</span><span class="font-tes14-serif text-xl leading-snug group-hover:underline group-hover:decoration-tes14-acc group-hover:underline-offset-4">Forty years of tidal charts, by hand</span></span></a></li>
        <li class="[counter-increment:tes14]"><a href="#" class="group flex gap-4 py-4 before:font-tes14-serif before:text-3xl before:leading-none before:text-tes14-acc before:content-[counter(tes14,decimal-leading-zero)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc"><span class="grid gap-1"><span class="text-[11px] font-semibold tracking-[0.14em] text-tes14-mut uppercase">Archive</span><span class="font-tes14-serif text-xl leading-snug group-hover:underline group-hover:decoration-tes14-acc group-hover:underline-offset-4">What the 1998 floods taught the coast</span></span></a></li>
      </ol>
    </aside>
  </main>
  <footer class="flex flex-wrap justify-between gap-2 border-t border-tes14-line px-[clamp(1rem,4vw,3rem)] py-4 text-xs text-tes14-mut"><span>Established 1974</span><a href="#" class="hover:text-tes14-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tes14-acc">Contact the desk</a></footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tes14-bg: #f6f2ea;
  --color-tes14-bg: oklch(0.962 0.012 85);
  --color-tes14-card: #fffcf6;
  --color-tes14-card: oklch(0.992 0.008 85);
  --color-tes14-line: #ddd5c6;
  --color-tes14-line: oklch(0.876 0.02 85);
  --color-tes14-line2: #bfb4a0;
  --color-tes14-line2: oklch(0.77 0.03 85);
  --color-tes14-ink: #191712;
  --color-tes14-ink: oklch(0.2 0.01 85);
  --color-tes14-mut: #5e584c;
  --color-tes14-mut: oklch(0.46 0.018 85);
  --color-tes14-acc: #b3261e;
  --color-tes14-acc: oklch(0.52 0.19 28);
  --font-tes14-sans: 'Geist', system-ui, sans-serif;
  --font-tes14-serif: 'Instrument Serif', Georgia, serif;
}
/* Root rule: the full-bleed contract, restated in CSS so the stage is sized before the browser
   build compiles, plus a guard so the hidden attribute always beats display utilities. */

.tes-14 {
  width: 100%;
  min-height: 100svh;
}

.tes-14 [hidden] {
  display: none !important;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.tes-14');
  if (!root || root.dataset.wired) return;
  root.dataset.wired = '1';
  const input = root.querySelector('#tes14-input'), sugg = root.querySelector('#tes14-sugg');
  const index = [
    ['The village that bought its own grid', 'Reporting, 2026'],
    ['In defence of the slow newsroom', 'Essay, 2025'],
    ['Forty years of tidal charts, by hand', 'Interview, 2024'],
    ['What the 1998 floods taught the coast', 'Archive, 1998'],
    ['The last printing press in the county', 'Reporting, 2023']
  ];
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const mark = (text, term) => {
    const i = text.toLowerCase().indexOf(term);
    if (i < 0) return esc(text);
    return esc(text.slice(0, i)) + '<mark class="rounded-sm bg-tes14-acc/15 text-tes14-ink">' + esc(text.slice(i, i + term.length)) + '</mark>' + esc(text.slice(i + term.length));
  };
  const row = (a, b) => '<li><a href="#" class="grid gap-0.5 px-4 py-3 hover:bg-tes14-bg"><b class="font-tes14-serif text-lg font-normal">' + a + '</b><span class="text-xs text-tes14-mut">' + b + '</span></a></li>';
  const render = () => {
    const term = input.value.trim().toLowerCase();
    if (!term) { sugg.hidden = true; sugg.innerHTML = ''; return; }
    const hits = index.filter((r) => (r[0] + ' ' + r[1]).toLowerCase().includes(term));
    sugg.hidden = false;
    sugg.innerHTML = hits.length
      ? hits.map((r) => row(mark(r[0], term), mark(r[1], term))).join('')
      : '<li class="px-4 py-3"><b class="block text-sm font-medium">Nothing in the archive matches \u201c' + esc(input.value.trim()) + '\u201d</b><span class="text-xs text-tes14-mut">Try a year, or a reporter\u2019s name</span></li>';
  };
  input.addEventListener('input', render);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); render(); } });
  root.querySelector('#tes14-go').addEventListener('click', () => { render(); input.focus(); });
})();
```
