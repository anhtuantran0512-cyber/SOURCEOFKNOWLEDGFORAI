---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-ecommerce-header-search-bar-cart-badge/"
title: "Tailwind E-Commerce Header with Search Bar and Cart Badge"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A working storefront header: a live search that filters the product grid as you type (press / to focus, Esc to clear), category chips under it, and a cart…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind E-Commerce Header with Search Bar and Cart Badge
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-ecommerce-header-search-bar-cart-badge/

A working storefront header: a live search that filters the product grid as you type (press / to focus, Esc to clear), category chips under it, and a cart badge that bumps every time you add a plant — announced to screen readers through a polite live region. The clear button shows itself with peer-placeholder-shown:hidden, no script needed.
## HTML
```html
<div class="tsn-17 w-full min-h-svh bg-tsn17-bg font-tsn17-sans text-tsn17-ink antialiased" aria-label="E-commerce header with search and cart badge demo">
  <header class="sticky top-0 z-40 border-b border-tsn17-line bg-tsn17-bg/90 backdrop-blur-xl">
    <div class="flex h-16 items-center gap-3 px-[max(1.25rem,calc((100%-72rem)/2))] sm:gap-6">
      <a href="#tsn-17-main" class="flex min-h-11 flex-none items-center gap-2 rounded-lg text-lg font-semibold tracking-[-0.02em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn17-acc"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-tsn17-acc text-white"><svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg></span><span class="max-sm:sr-only">Verdant</span></a>
      <div class="relative flex min-w-0 max-w-xl flex-1 items-center">
        <span aria-hidden="true" class="pointer-events-none absolute left-3.5 text-tsn17-mut"><svg class="size-[18px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></span>
        <input data-tsn17-q type="search" placeholder="Search plants" aria-label="Search plants" autocomplete="off" class="peer h-11 w-full rounded-full border border-tsn17-line bg-tsn17-surface pl-10 pr-20 text-[15px] outline-none transition placeholder:text-tsn17-mut focus:border-tsn17-acc focus:ring-4 focus:ring-tsn17-acc/15 [&::-webkit-search-cancel-button]:hidden">
        <kbd aria-hidden="true" class="pointer-events-none absolute right-3 rounded-md border border-tsn17-line px-1.5 py-0.5 font-tsn17-mono text-[11px] text-tsn17-mut peer-focus:hidden peer-[:not(:placeholder-shown)]:hidden max-sm:hidden">/</kbd>
        <button type="button" data-tsn17-clear class="absolute right-1.5 inline-flex min-h-8 items-center rounded-full px-3 text-xs font-semibold text-tsn17-mut hover:bg-tsn17-ink/5 hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc peer-placeholder-shown:hidden">Clear</button>
      </div>
      <a href="#tsn-17-main" class="grid size-11 flex-none place-items-center rounded-full hover:bg-tsn17-ink/5 focus-visible:outline-2 focus-visible:outline-tsn17-acc max-sm:hidden"><span class="sr-only">Account</span><svg class="size-[22px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></a>
      <button type="button" class="relative grid size-11 flex-none place-items-center rounded-full bg-tsn17-ink text-tsn17-bg hover:bg-tsn17-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc">
        <span class="sr-only">Cart, <span data-tsn17-count-sr>0</span> items</span><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/></svg>
        <span data-tsn17-badge aria-hidden="true" class="absolute -right-1 -top-1 grid h-5 min-w-5 scale-0 place-items-center rounded-full bg-tsn17-hot px-1 text-[11px] font-bold text-white ring-2 ring-tsn17-bg transition-transform data-has:scale-100 data-bump:animate-tsn17-bump motion-reduce:animate-none">0</span>
      </button>
    </div>
    <nav aria-label="Categories" class="flex gap-1 overflow-x-auto pb-2.5 px-[max(1.25rem,calc((100%-72rem)/2))] [scrollbar-width:none]">
      <button type="button" data-tsn17-cat="All" aria-pressed="true" class="inline-flex min-h-9 flex-none items-center rounded-full px-3.5 text-[13px] font-semibold text-tsn17-mut transition-colors hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc aria-pressed:bg-tsn17-ink aria-pressed:text-tsn17-bg">All</button>
      <button type="button" data-tsn17-cat="Tropical" aria-pressed="false" class="inline-flex min-h-9 flex-none items-center rounded-full px-3.5 text-[13px] font-semibold text-tsn17-mut transition-colors hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc aria-pressed:bg-tsn17-ink aria-pressed:text-tsn17-bg">Tropical</button>
      <button type="button" data-tsn17-cat="Trees" aria-pressed="false" class="inline-flex min-h-9 flex-none items-center rounded-full px-3.5 text-[13px] font-semibold text-tsn17-mut transition-colors hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc aria-pressed:bg-tsn17-ink aria-pressed:text-tsn17-bg">Trees</button>
      <button type="button" data-tsn17-cat="Low light" aria-pressed="false" class="inline-flex min-h-9 flex-none items-center rounded-full px-3.5 text-[13px] font-semibold text-tsn17-mut transition-colors hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc aria-pressed:bg-tsn17-ink aria-pressed:text-tsn17-bg">Low light</button>
      <button type="button" data-tsn17-cat="Trailing" aria-pressed="false" class="inline-flex min-h-9 flex-none items-center rounded-full px-3.5 text-[13px] font-semibold text-tsn17-mut transition-colors hover:text-tsn17-ink focus-visible:outline-2 focus-visible:outline-tsn17-acc aria-pressed:bg-tsn17-ink aria-pressed:text-tsn17-bg">Trailing</button>
    </nav>
  </header>
  <main id="tsn-17-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] pb-24 pt-8">
    <div class="flex flex-wrap items-end justify-between gap-3">
      <div>
        <p class="font-tsn17-mono text-[11.5px] uppercase tracking-[0.16em] text-tsn17-acc">peer-placeholder-shown · data-bump</p>
        <h1 class="mt-2 text-[clamp(30px,4.6vw,48px)] font-semibold leading-[1.05] tracking-[-0.03em]">Plants that forgive you</h1>
      </div>
      <p data-tsn17-status class="text-sm text-tsn17-mut" aria-live="polite">Showing 8 plants</p>
    </div>
    <ul class="mt-8 grid grid-cols-[repeat(auto-fill,minmax(min(100%,14rem),1fr))] gap-x-5 gap-y-9">
      <li data-tsn17-item data-name="monstera deliciosa" data-cat="Tropical" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1614594975525-e45190c55d0b?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Tropical</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Monstera Deliciosa</h3><p class="text-sm text-tsn17-mut">$48.00</p></div>
          <button type="button" data-tsn17-add data-name="Monstera Deliciosa" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Monstera Deliciosa to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="fiddle leaf fig" data-cat="Trees" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1597055181300-e3633a207519?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Trees</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Fiddle Leaf Fig</h3><p class="text-sm text-tsn17-mut">$64.00</p></div>
          <button type="button" data-tsn17-add data-name="Fiddle Leaf Fig" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Fiddle Leaf Fig to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="snake plant" data-cat="Low light" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1593482892290-f54927ae1bb6?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Low light</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Snake Plant</h3><p class="text-sm text-tsn17-mut">$32.00</p></div>
          <button type="button" data-tsn17-add data-name="Snake Plant" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Snake Plant to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="pothos golden" data-cat="Trailing" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1600411833196-7c1f6b1a8b90?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Trailing</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Pothos Golden</h3><p class="text-sm text-tsn17-mut">$22.00</p></div>
          <button type="button" data-tsn17-add data-name="Pothos Golden" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Pothos Golden to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="calathea orbifolia" data-cat="Tropical" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1616500163246-0ffbb872f4de?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Tropical</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Calathea Orbifolia</h3><p class="text-sm text-tsn17-mut">$38.00</p></div>
          <button type="button" data-tsn17-add data-name="Calathea Orbifolia" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Calathea Orbifolia to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="zz plant" data-cat="Low light" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1632207691143-643e2a9a9361?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Low light</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">ZZ Plant</h3><p class="text-sm text-tsn17-mut">$36.00</p></div>
          <button type="button" data-tsn17-add data-name="ZZ Plant" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add ZZ Plant to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="olive tree" data-cat="Trees" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1599598425947-5202edd56bdb?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Trees</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">Olive Tree</h3><p class="text-sm text-tsn17-mut">$89.00</p></div>
          <button type="button" data-tsn17-add data-name="Olive Tree" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add Olive Tree to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
      <li data-tsn17-item data-name="string of pearls" data-cat="Trailing" class="group/p grid gap-3">
        <div class="relative aspect-[4/5] overflow-hidden rounded-2xl bg-[linear-gradient(160deg,var(--color-tsn17-soft),var(--color-tsn17-acc))]">
          <img src="https://images.unsplash.com/photo-1621512367176-03782e847fa2?auto=format&fit=crop&w=700&q=70" alt="" loading="lazy" class="size-full object-cover transition-transform duration-700 group-hover/p:scale-105 motion-reduce:transition-none">
          <span class="absolute left-3 top-3 rounded-full bg-tsn17-surface/90 px-2.5 py-1 text-[11px] font-semibold text-tsn17-ink backdrop-blur">Trailing</span>
        </div>
        <div class="flex items-start justify-between gap-3">
          <div><h3 class="font-semibold">String of Pearls</h3><p class="text-sm text-tsn17-mut">$26.00</p></div>
          <button type="button" data-tsn17-add data-name="String of Pearls" class="inline-flex min-h-11 flex-none items-center gap-1.5 rounded-full border border-tsn17-line px-3.5 text-sm font-semibold transition hover:border-tsn17-acc hover:bg-tsn17-acc hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn17-acc active:scale-95"><span class="sr-only">Add String of Pearls to cart</span><span aria-hidden="true">Add</span></button>
        </div>
      </li>
    </ul>
    <p data-tsn17-empty hidden class="mt-10 rounded-2xl border border-dashed border-tsn17-line p-10 text-center text-tsn17-mut">No plants match that search. Try “fig” or “low light”.</p>
  </main>
  <footer class="border-t border-tsn17-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn17-mono text-xs text-tsn17-mut">Tailwind sticky navigation · pattern 17 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn17-bg: #f6f5ef;
  --color-tsn17-bg: oklch(0.967 0.01 105);
  --color-tsn17-surface: #ffffff;
  --color-tsn17-surface: oklch(1 0 0);
  --color-tsn17-ink: #18241b;
  --color-tsn17-ink: oklch(0.24 0.025 150);
  --color-tsn17-mut: #566258;
  --color-tsn17-mut: oklch(0.47 0.02 150);
  --color-tsn17-acc: #2f7d4a;
  --color-tsn17-acc: oklch(0.52 0.12 150);
  --color-tsn17-soft: #cfe3cf;
  --color-tsn17-soft: oklch(0.89 0.04 145);
  --color-tsn17-hot: #e5484d;
  --color-tsn17-hot: oklch(0.62 0.21 25);
  --color-tsn17-line: #18241b1f;
  --color-tsn17-line: oklch(0.24 0.025 150 / 0.12);
  --font-tsn17-sans: 'Outfit', system-ui, sans-serif;
  --font-tsn17-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tsn17-bump: tsn17-bump 0.45s cubic-bezier(0.3,1.6,0.5,1);

  @keyframes tsn17-bump {
    0% {
      transform: scale(1);
    }

    40% {
      transform: scale(1.45);
    }

    100% {
      transform: scale(1);
    }
  }
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-17 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-17').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const q = root.querySelector('[data-tsn17-q]');
    const items = [...root.querySelectorAll('[data-tsn17-item]')];
    const cats = [...root.querySelectorAll('[data-tsn17-cat]')];
    const status = root.querySelector('[data-tsn17-status]');
    const empty = root.querySelector('[data-tsn17-empty]');
    const badge = root.querySelector('[data-tsn17-badge]');
    const countSr = root.querySelector('[data-tsn17-count-sr]');
    root.querySelectorAll('img').forEach((img) => {
      const drop = () => img.remove();
      if (img.complete && !img.naturalWidth) drop(); else img.addEventListener('error', drop);
    });
    let cat = 'All', count = 0;
    const apply = () => {
      const term = q.value.trim().toLowerCase();
      let shown = 0;
      items.forEach((li) => {
        const ok = (cat === 'All' || li.dataset.cat === cat) && (!term || li.dataset.name.includes(term) || li.dataset.cat.toLowerCase().includes(term));
        li.hidden = !ok;
        if (ok) shown++;
      });
      empty.hidden = shown > 0;
      status.textContent = 'Showing ' + shown + (shown === 1 ? ' plant' : ' plants');
    };
    q.addEventListener('input', apply);
    q.addEventListener('keydown', (e) => { if (e.key === 'Escape') { q.value = ''; apply(); } });
    root.querySelector('[data-tsn17-clear]').addEventListener('click', () => { q.value = ''; apply(); q.focus(); });
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { e.preventDefault(); q.focus(); }
    });
    cats.forEach((b) => b.addEventListener('click', () => {
      cat = b.dataset.tsn17Cat;
      cats.forEach((c) => c.setAttribute('aria-pressed', String(c === b)));
      apply();
    }));
    root.querySelectorAll('[data-tsn17-add]').forEach((b) => b.addEventListener('click', () => {
      count++;
      badge.textContent = count > 99 ? '99+' : String(count);
      countSr.textContent = String(count);
      badge.setAttribute('data-has', '');
      badge.removeAttribute('data-bump');
      void badge.offsetWidth;
      badge.setAttribute('data-bump', '');
      status.textContent = 'Added ' + b.dataset.name + ' · ' + count + (count === 1 ? ' item' : ' items') + ' in cart';
    }));
  });
})();
```
