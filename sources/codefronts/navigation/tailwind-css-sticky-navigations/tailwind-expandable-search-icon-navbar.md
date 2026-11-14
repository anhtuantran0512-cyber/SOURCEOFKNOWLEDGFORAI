---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-expandable-search-icon-navbar/"
title: "Tailwind Expandable Search Icon Navbar"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A search icon that unfolds into a full search field across the header — the nav fades aside, the input grows from 44px to 36rem, focus lands in it, and live…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Expandable Search Icon Navbar
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-expandable-search-icon-navbar/

A search icon that unfolds into a full search field across the header — the nav fades aside, the input grows from 44px to 36rem, focus lands in it, and live suggestions filter as you type with the match highlighted. Esc, the close button or clicking away collapses it and returns focus to the icon. When collapsed, the field is inert.
## HTML
```html
<div class="tsn-20 w-full min-h-svh bg-tsn20-bg font-tsn20-sans text-tsn20-ink antialiased" aria-label="Expandable search icon navbar demo">
  <header data-tsn20-header class="group/hdr sticky top-0 z-40 border-b border-tsn20-line bg-tsn20-bg/85 backdrop-blur-xl">
    <div class="relative flex h-16 items-center gap-6 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <a href="#tsn-20-s1" class="flex min-h-11 flex-none items-center gap-2 rounded-lg font-bold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn20-acc"><span aria-hidden="true" class="grid size-8 place-items-center rounded-[10px] bg-tsn20-acc text-white"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>Lattice</a>
      <nav aria-label="Primary" class="flex min-w-0 gap-1 overflow-x-auto pr-14 transition-[opacity,visibility] duration-300 [scrollbar-width:none] group-data-search/hdr:invisible group-data-search/hdr:opacity-0">
        <a href="#tsn-20-s1" aria-current="page" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn20-mut hover:text-tsn20-ink focus-visible:outline-2 focus-visible:outline-tsn20-acc aria-[current=page]:text-tsn20-acc">Library</a>
        <a href="#tsn-20-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn20-mut hover:text-tsn20-ink focus-visible:outline-2 focus-visible:outline-tsn20-acc">Kits</a>
        <a href="#tsn-20-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-sm font-semibold text-tsn20-mut hover:text-tsn20-ink focus-visible:outline-2 focus-visible:outline-tsn20-acc">Community</a>
      </nav>
      <div class="pointer-events-none absolute inset-y-0 right-[max(1.25rem,calc((100%-72rem)/2))] left-[max(1.25rem,calc((100%-72rem)/2))] flex items-center justify-end">
        <div data-tsn20-box class="pointer-events-auto relative h-11 w-11 rounded-full border border-tsn20-line bg-tsn20-surface shadow-[0_1px_2px_rgb(0_0_0/0.05)] transition-[width,box-shadow,border-color] duration-500 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-data-search/hdr:w-full group-data-search/hdr:border-tsn20-acc group-data-search/hdr:shadow-[0_0_0_4px_color-mix(in_oklab,var(--color-tsn20-acc)_15%,transparent)] md:group-data-search/hdr:w-[36rem] motion-reduce:transition-none">
          <button type="button" data-tsn20-open aria-expanded="false" aria-controls="tsn-20-panel" class="absolute left-0 top-0 grid size-[42px] place-items-center rounded-full text-tsn20-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn20-acc"><span class="sr-only">Open search</span><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></button>
          <div id="tsn-20-panel" data-tsn20-panel inert class="absolute inset-0 opacity-0 transition-opacity delay-150 duration-200 group-data-search/hdr:opacity-100">
            <input data-tsn20-input type="search" placeholder="Search components, kits, people…" aria-label="Search" autocomplete="off" class="h-full w-full rounded-full bg-transparent pl-11 pr-12 text-[15px] outline-none placeholder:text-tsn20-mut [&::-webkit-search-cancel-button]:hidden">
            <button type="button" data-tsn20-close class="absolute right-0.5 top-0 grid size-[42px] place-items-center rounded-full text-tsn20-mut hover:text-tsn20-ink focus-visible:outline-2 focus-visible:outline-tsn20-acc"><span class="sr-only">Close search</span><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
            <div class="absolute inset-x-0 top-[calc(100%+0.5rem)] overflow-hidden rounded-2xl border border-tsn20-line bg-tsn20-surface p-2 shadow-[0_24px_48px_-24px_rgb(60_40_80/0.35)]">
              <p class="px-3 pb-1 pt-2 font-tsn20-mono text-[11px] uppercase tracking-[0.14em] text-tsn20-mut" data-tsn20-label>Popular</p>
              <ul data-tsn20-list class="grid">
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Design tokens"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Design tokens</span></a></li>
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Grid layouts"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Grid layouts</span></a></li>
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Typography scale"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Typography scale</span></a></li>
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Colour palettes"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Colour palettes</span></a></li>
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Icon sets"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Icon sets</span></a></li>
                <li><a href="#tsn-20-s2" class="flex min-h-11 items-center gap-3 rounded-xl px-3 text-sm hover:bg-tsn20-acc/8 focus-visible:bg-tsn20-acc/8 focus-visible:outline-none" data-label="Motion presets"><svg class="size-4 text-tsn20-mut" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span>Motion presets</span></a></li>
              </ul>
              <p data-tsn20-none hidden class="px-3 py-4 text-sm text-tsn20-mut">No matches — press Enter to search everything.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn20-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn20-acc">w-11 → w-[36rem] · inert</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(34px,5.6vw,64px)] font-semibold leading-[1.02] tracking-[-0.035em] text-balance">Search that makes room for itself</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn20-mut text-pretty">Click the magnifier. The nav steps aside, the field unfolds, focus lands inside, and suggestions narrow as you type. Escape puts everything back.</p>
  </div>
  <main id="tsn-20-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-20-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn20-line bg-tsn20-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-20-h1">
      <p class="font-tsn20-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn20-acc">Library</p>
      <h2 id="tsn-20-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">One attribute, a choreography</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn20-mut text-pretty"><code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">data-search</code> on the header widens the box, fades the nav, rings the field in the accent and delays the input’s fade by 150ms so it appears as the box opens.</p>
    </section>
    <section id="tsn-20-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn20-line bg-tsn20-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-20-h2">
      <p class="font-tsn20-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn20-acc">Kits</p>
      <h2 id="tsn-20-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Invisible, not just transparent</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn20-mut text-pretty">The nav gets <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">invisible</code> as well as <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">opacity-0</code>, so it can’t catch clicks through the open field. The closed field is <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">inert</code> for the same reason in reverse.</p>
    </section>
    <section id="tsn-20-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn20-line bg-tsn20-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-20-h3">
      <p class="font-tsn20-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn20-acc">Community</p>
      <h2 id="tsn-20-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Focus is the feature</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn20-mut text-pretty">Opening focuses the input with <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">preventScroll</code>; closing returns focus to the magnifier. Keyboard users never lose their place.</p>
    </section>
    <section id="tsn-20-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn20-line bg-tsn20-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-20-h4">
      <p class="font-tsn20-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn20-acc">Results</p>
      <h2 id="tsn-20-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Highlight safely</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn20-mut text-pretty">Matches are wrapped in <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">&lt;mark&gt;</code> using text nodes, never <code class="rounded-md bg-tsn20-acc/10 px-1.5 py-0.5 font-tsn20-mono text-[0.86em] text-tsn20-ink">innerHTML</code>, so a typed angle bracket stays text.</p>
    </section>
  </main>
  <footer class="border-t border-tsn20-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn20-mono text-xs text-tsn20-mut">Tailwind sticky navigation · pattern 20 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn20-bg: #fbf6f3;
  --color-tsn20-bg: oklch(0.975 0.01 50);
  --color-tsn20-surface: #ffffff;
  --color-tsn20-surface: oklch(1 0 0);
  --color-tsn20-ink: #221a2b;
  --color-tsn20-ink: oklch(0.23 0.03 305);
  --color-tsn20-mut: #625870;
  --color-tsn20-mut: oklch(0.48 0.035 305);
  --color-tsn20-acc: #7c3aed;
  --color-tsn20-acc: oklch(0.54 0.24 293);
  --color-tsn20-line: #221a2b1a;
  --color-tsn20-line: oklch(0.23 0.03 305 / 0.1);
  --font-tsn20-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tsn20-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-20 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-20) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-20').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const hdr = root.querySelector('[data-tsn20-header]');
    const openBtn = root.querySelector('[data-tsn20-open]');
    const panel = root.querySelector('[data-tsn20-panel]');
    const input = root.querySelector('[data-tsn20-input]');
    const box = root.querySelector('[data-tsn20-box]');
    const links = [...root.querySelectorAll('[data-tsn20-list] a')];
    const none = root.querySelector('[data-tsn20-none]');
    const label = root.querySelector('[data-tsn20-label]');
    const set = (open) => {
      hdr.toggleAttribute('data-search', open);
      openBtn.setAttribute('aria-expanded', String(open));
      panel.inert = !open;
      if (open) setTimeout(() => input.focus({ preventScroll: true }), 60);
      else { input.value = ''; filter(); openBtn.focus(); }
    };
    const filter = () => {
      const term = input.value.trim().toLowerCase();
      let shown = 0;
      links.forEach((a) => {
        const text = a.dataset.label, i = text.toLowerCase().indexOf(term);
        const ok = !term || i > -1;
        a.parentElement.hidden = !ok;
        const span = a.querySelector('span');
        span.textContent = '';
        if (ok && term) {
          const mark = document.createElement('mark');
          mark.className = 'rounded bg-tsn20-acc/20 text-inherit';
          mark.textContent = text.slice(i, i + term.length);
          span.append(text.slice(0, i), mark, text.slice(i + term.length));
        } else span.textContent = text;
        if (ok) shown++;
      });
      none.hidden = shown > 0;
      label.textContent = term ? 'Suggestions' : 'Popular';
    };
    openBtn.addEventListener('click', () => hdr.hasAttribute('data-search') ? input.focus() : set(true));
    root.querySelector('[data-tsn20-close]').addEventListener('click', () => set(false));
    input.addEventListener('input', filter);
    links.forEach((a) => a.addEventListener('click', () => set(false)));
    root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && hdr.hasAttribute('data-search')) set(false); });
    document.addEventListener('pointerdown', (e) => { if (hdr.hasAttribute('data-search') && !box.contains(e.target)) set(false); });
  });
})();
```
