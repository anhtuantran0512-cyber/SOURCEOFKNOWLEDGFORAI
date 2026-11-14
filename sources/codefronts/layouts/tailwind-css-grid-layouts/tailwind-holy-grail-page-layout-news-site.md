---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-holy-grail-page-layout-news-site/"
title: "Tailwind Holy Grail Page Layout for a News Site"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "Header, section nav, story column, trending rail, footer — the layout every publication still ships, written as an ASCII map you can read in the class list…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Holy Grail Page Layout for a News Site
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-holy-grail-page-layout-news-site/

Header, section nav, story column, trending rail, footer — the layout every publication still ships, written as an ASCII map you can read in the class list and restacked on mobile by one variant on the same element.
## HTML
```html
<section class="tgx-04 w-full min-h-svh bg-tgx04-bg text-tgx04-ink font-tgx04-sans p-5">
  <div class="grid gap-3 min-h-[420px] [grid-template-areas:'masthead_masthead_masthead'_'nav_main_rail'_'footer_footer_footer'] grid-cols-[minmax(140px,180px)_minmax(0,1fr)_minmax(150px,220px)] grid-rows-[auto_1fr_auto] max-md:[grid-template-areas:'masthead'_'nav'_'main'_'rail'_'footer'] max-md:grid-cols-1 max-md:grid-rows-none">
    <header class="[grid-area:masthead] flex items-center justify-between gap-4 flex-wrap rounded-xl bg-tgx04-panel border border-tgx04-line px-4 py-3">
      <div class="flex items-baseline gap-3">
        <strong class="font-tgx04-serif text-[1.25rem] tracking-[-0.01em]">The Ledger</strong>
        <span class="text-[0.7rem] text-tgx04-dim tabular-nums">Monday, 21 September</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-[0.72rem] text-tgx04-dim bg-tgx04-bg border border-tgx04-line rounded-lg px-3 py-1.5">⌕ Search</span>
        <button type="button" class="text-[0.75rem] font-semibold text-white bg-tgx04-accent rounded-lg px-3 min-h-9 cursor-pointer transition-colors hover:bg-tgx04-accentdark focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Subscribe</button>
      </div>
    </header>
    <nav aria-label="Sections" class="[grid-area:nav] flex flex-col gap-0.5 rounded-xl bg-tgx04-panel border border-tgx04-line p-2.5">
      <p class="text-[0.62rem] tracking-[0.16em] uppercase text-tgx04-dim px-2 pb-1.5">Sections</p>
      <a href="#0" aria-current="page" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx04-dim transition-colors hover:text-tgx04-ink hover:bg-tgx04-hover aria-[current=page]:text-tgx04-accent aria-[current=page]:bg-tgx04-accenttint aria-[current=page]:font-semibold focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Markets</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx04-dim transition-colors hover:text-tgx04-ink hover:bg-tgx04-hover focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Policy</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx04-dim transition-colors hover:text-tgx04-ink hover:bg-tgx04-hover focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Energy</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx04-dim transition-colors hover:text-tgx04-ink hover:bg-tgx04-hover focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Opinion</a>
      <a href="#0" class="text-[0.82rem] no-underline rounded-lg px-2.5 min-h-9 flex items-center text-tgx04-dim transition-colors hover:text-tgx04-ink hover:bg-tgx04-hover focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2">Data</a>
    </nav>
    <main class="[grid-area:main] min-w-0 rounded-xl bg-tgx04-panel border border-tgx04-line p-4 flex flex-col gap-4">
      <article class="flex flex-col gap-2 pb-4 border-b border-tgx04-line">
        <p class="text-[0.66rem] font-semibold tracking-[0.14em] uppercase text-tgx04-accent">Markets · Live</p>
        <h2 class="font-tgx04-serif text-[clamp(1.3rem,2.6vw,1.75rem)] leading-[1.15] tracking-[-0.01em] text-balance">Freight rates slip for a fourth week as North Sea capacity returns</h2>
        <p class="text-[0.86rem] leading-[1.65] text-tgx04-dim">Spot prices on the Rotterdam–Felixstowe corridor fell 3.1% overnight, the longest run of declines since spring, as three delayed vessels re-entered service.</p>
        <p class="text-[0.72rem] text-tgx04-dim">Priya Raman · 6 min read</p>
      </article>
      <article class="flex flex-col gap-1.5">
        <h3 class="font-tgx04-serif text-[1.02rem] leading-[1.3]">Regulator opens consultation on port fee transparency</h3>
        <p class="text-[0.84rem] leading-[1.6] text-tgx04-dim">Operators would publish surcharge schedules quarterly under the draft rule.</p>
      </article>
      <article class="flex flex-col gap-1.5">
        <h3 class="font-tgx04-serif text-[1.02rem] leading-[1.3]">Battery imports hit a monthly record</h3>
        <p class="text-[0.84rem] leading-[1.6] text-tgx04-dim">Volume rose 18% year on year, concentrated in two terminals.</p>
      </article>
    </main>
    <aside class="[grid-area:rail] rounded-xl bg-tgx04-panel border border-tgx04-line p-3.5 flex flex-col gap-3">
      <p class="text-[0.62rem] tracking-[0.16em] uppercase text-tgx04-dim">Most read</p>
      <ol class="flex flex-col gap-2.5 list-none m-0 p-0">
        <li class="grid grid-cols-[1.2rem_minmax(0,1fr)] gap-2 items-start"><span class="font-tgx04-serif text-[0.9rem] text-tgx04-accent tabular-nums">1</span><a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx04-ink hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2 rounded">The quiet consolidation of regional ports</a></li>
        <li class="grid grid-cols-[1.2rem_minmax(0,1fr)] gap-2 items-start"><span class="font-tgx04-serif text-[0.9rem] text-tgx04-accent tabular-nums">2</span><a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx04-ink hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2 rounded">What a 3% rate slide does to Q4 guidance</a></li>
        <li class="grid grid-cols-[1.2rem_minmax(0,1fr)] gap-2 items-start"><span class="font-tgx04-serif text-[0.9rem] text-tgx04-accent tabular-nums">3</span><a href="#0" class="text-[0.8rem] leading-[1.4] no-underline text-tgx04-ink hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx04-accent focus-visible:outline-offset-2 rounded">Inside the new customs data feed</a></li>
      </ol>
    </aside>
    <footer class="[grid-area:footer] flex items-center justify-between gap-4 flex-wrap rounded-xl bg-tgx04-panel border border-tgx04-line px-4 py-3 text-[0.74rem] text-tgx04-dim">
      <span>© 2026 The Ledger · Registered in England</span>
      <span class="font-tgx04-mono">grid-rows: auto · 1fr · auto</span>
    </footer>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx04-bg: #f4f2ee;
  --color-tgx04-bg: oklch(0.95 0.005 80);
  --color-tgx04-panel: #ffffff;
  --color-tgx04-panel: oklch(1 0 0);
  --color-tgx04-hover: #f0eeea;
  --color-tgx04-hover: oklch(0.94 0.005 80);
  --color-tgx04-line: #ddd9d2;
  --color-tgx04-line: oklch(0.88 0.008 80);
  --color-tgx04-ink: #23201c;
  --color-tgx04-ink: oklch(0.24 0.01 70);
  --color-tgx04-dim: #6b655d;
  --color-tgx04-dim: oklch(0.5 0.01 75);
  --color-tgx04-accent: #9c2f1f;
  --color-tgx04-accent: oklch(0.45 0.16 30);
  --color-tgx04-accentdark: #7d2517;
  --color-tgx04-accentdark: oklch(0.38 0.15 30);
  --color-tgx04-accenttint: #f8e9e5;
  --color-tgx04-accenttint: oklch(0.94 0.025 30);
  --font-tgx04-sans: 'Inter Tight', system-ui, sans-serif;
  --font-tgx04-serif: 'Fraunces', Georgia, serif;
  --font-tgx04-mono: ui-monospace, Menlo, monospace;
}

.tgx-04 {
  width: 100%;
  min-height: 100svh;
}
```
