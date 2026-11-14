---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-mobile-bottom-navigation-bar-safe-area/"
title: "Tailwind Mobile Bottom Navigation Bar with Safe Area"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "An app-style bottom tab bar pinned with sticky bottom-0 inside a phone shell, padded with pb-[max(env(safe-area-inset-bottom),1.25rem)] so it clears the…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Mobile Bottom Navigation Bar with Safe Area
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-mobile-bottom-navigation-bar-safe-area/

An app-style bottom tab bar pinned with sticky bottom-0 inside a phone shell, padded with pb-[max(env(safe-area-inset-bottom),1.25rem)] so it clears the iPhone home indicator on real devices and still breathes everywhere else. Four working tabs swap their panels, the active tab gets a Material-style pill, and the Inbox badge clears when you visit it.
## HTML
```html
<div class="tsn-22 grid w-full min-h-svh place-items-center bg-tsn22-stage bg-[radial-gradient(60%_50%_at_50%_0%,color-mix(in_oklab,var(--color-tsn22-acc)_25%,transparent),transparent)] p-4 font-tsn22-sans text-tsn22-ink antialiased" aria-label="Mobile bottom tab bar with safe area demo">
  <div class="relative h-[min(800px,calc(100svh-2rem))] w-[min(390px,100%)] overflow-hidden rounded-[3rem] border-[10px] border-[#050506] bg-tsn22-bg shadow-[0_40px_80px_-30px_rgb(0_0_0/0.8),0_0_0_1px_rgb(255_255_255/0.08)]">
    <span aria-hidden="true" class="absolute left-1/2 top-2.5 z-50 h-7 w-28 -translate-x-1/2 rounded-full bg-black"></span>
    <div data-tsn22-scroller class="h-full overflow-y-auto overscroll-contain [scrollbar-width:none]">
      <div class="flex min-h-full flex-col">
        <header class="sticky top-0 z-20 bg-tsn22-bg/80 px-5 pb-3 pt-14 backdrop-blur-xl">
          <p class="font-tsn22-mono text-[10.5px] uppercase tracking-[0.16em] text-tsn22-acc">sticky bottom-0 · env(safe-area)</p>
          <h1 data-tsn22-title class="mt-1 text-[30px] font-semibold tracking-[-0.03em]">Home</h1>
        </header>
        <main class="flex-1 px-4 pb-6">
          <section data-tsn22-panel="home" class="grid gap-4">
            <article class="overflow-hidden rounded-3xl bg-tsn22-card">
              <div aria-hidden="true" class="aspect-[16/10] bg-[linear-gradient(135deg,#ff8a5b,#ff3d77)]"></div>
              <div class="p-4"><h3 class="font-semibold">Morning focus mix</h3><p class="mt-1 text-sm text-tsn22-mut">42 min · Updated today</p></div>
            </article>
            <article class="overflow-hidden rounded-3xl bg-tsn22-card">
              <div aria-hidden="true" class="aspect-[16/10] bg-[linear-gradient(135deg,#6a5cff,#2bd2ff)]"></div>
              <div class="p-4"><h3 class="font-semibold">Deep work, no lyrics</h3><p class="mt-1 text-sm text-tsn22-mut">1 h 18 min · 12 tracks</p></div>
            </article>
            <article class="overflow-hidden rounded-3xl bg-tsn22-card">
              <div aria-hidden="true" class="aspect-[16/10] bg-[linear-gradient(135deg,#22c55e,#0ea5a4)]"></div>
              <div class="p-4"><h3 class="font-semibold">Long run tempo</h3><p class="mt-1 text-sm text-tsn22-mut">55 min · 168 bpm</p></div>
            </article>
            <article class="overflow-hidden rounded-3xl bg-tsn22-card">
              <div aria-hidden="true" class="aspect-[16/10] bg-[linear-gradient(135deg,#f59e0b,#ef4444)]"></div>
              <div class="p-4"><h3 class="font-semibold">Wind-down</h3><p class="mt-1 text-sm text-tsn22-mut">30 min · Ambient</p></div>
            </article>
          </section>
          <section data-tsn22-panel="explore" hidden class="grid grid-cols-2 gap-3">
            <a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Focus</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Running</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Sleep</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Jazz</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Lo-fi</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Classical</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">Podcasts</a><a href="#" class="grid aspect-square content-end rounded-3xl bg-tsn22-card p-4 text-lg font-semibold">New</a>
          </section>
          <section data-tsn22-panel="inbox" hidden class="grid gap-2">
            <div class="flex items-center gap-3 rounded-2xl bg-tsn22-card p-3"><span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-tsn22-acc/20 font-semibold text-tsn22-acc">M</span><div class="min-w-0"><p class="font-semibold">Maya</p><p class="truncate text-sm text-tsn22-mut">Shared “Deep work” with you</p></div></div><div class="flex items-center gap-3 rounded-2xl bg-tsn22-card p-3"><span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-tsn22-acc/20 font-semibold text-tsn22-acc">L</span><div class="min-w-0"><p class="font-semibold">Leo</p><p class="truncate text-sm text-tsn22-mut">Started following you</p></div></div><div class="flex items-center gap-3 rounded-2xl bg-tsn22-card p-3"><span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-tsn22-acc/20 font-semibold text-tsn22-acc">W</span><div class="min-w-0"><p class="font-semibold">Weekly mix</p><p class="truncate text-sm text-tsn22-mut">Your new mix is ready</p></div></div><div class="flex items-center gap-3 rounded-2xl bg-tsn22-card p-3"><span aria-hidden="true" class="grid size-11 flex-none place-items-center rounded-full bg-tsn22-acc/20 font-semibold text-tsn22-acc">A</span><div class="min-w-0"><p class="font-semibold">Ari</p><p class="truncate text-sm text-tsn22-mut">Liked your playlist</p></div></div>
          </section>
          <section data-tsn22-panel="profile" hidden class="grid justify-items-center gap-3 rounded-3xl bg-tsn22-card p-8 text-center">
            <span aria-hidden="true" class="size-20 rounded-full bg-[linear-gradient(135deg,var(--color-tsn22-acc),var(--color-tsn22-hot))]"></span>
            <p class="text-xl font-semibold">Sam Rivera</p><p class="text-sm text-tsn22-mut">128 playlists · 2.4k followers</p>
          </section>
          <p class="mt-6 text-center text-[13px] leading-relaxed text-tsn22-mut">The bar below is <code class="font-tsn22-mono text-tsn22-ink">sticky bottom-0</code> inside this scroller, padded by <code class="font-tsn22-mono text-tsn22-ink">max(env(safe-area-inset-bottom), 1.25rem)</code>.</p>
        </main>
        <nav aria-label="Tabs" class="sticky bottom-0 z-20 border-t border-tsn22-line bg-tsn22-bar/90 px-2 pt-2 pb-[max(env(safe-area-inset-bottom),1.25rem)] backdrop-blur-xl">
          <div class="flex">
            <button type="button" data-tsn22-tab="home" aria-current="page" class="group/t relative grid min-h-14 flex-1 place-items-center content-center gap-1 rounded-2xl text-[11px] font-semibold text-tsn22-mut transition-colors hover:text-tsn22-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsn22-acc aria-[current=page]:text-tsn22-ink">
              <span class="relative grid h-8 w-14 place-items-center rounded-full transition-colors group-aria-[current=page]/t:bg-tsn22-acc/20 group-aria-[current=page]/t:text-tsn22-acc"><svg class="size-[22px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg></span>Home
            </button>
            <button type="button" data-tsn22-tab="explore" class="group/t relative grid min-h-14 flex-1 place-items-center content-center gap-1 rounded-2xl text-[11px] font-semibold text-tsn22-mut transition-colors hover:text-tsn22-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsn22-acc aria-[current=page]:text-tsn22-ink">
              <span class="relative grid h-8 w-14 place-items-center rounded-full transition-colors group-aria-[current=page]/t:bg-tsn22-acc/20 group-aria-[current=page]/t:text-tsn22-acc"><svg class="size-[22px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></span>Explore
            </button>
            <button type="button" data-tsn22-tab="inbox" class="group/t relative grid min-h-14 flex-1 place-items-center content-center gap-1 rounded-2xl text-[11px] font-semibold text-tsn22-mut transition-colors hover:text-tsn22-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsn22-acc aria-[current=page]:text-tsn22-ink">
              <span class="relative grid h-8 w-14 place-items-center rounded-full transition-colors group-aria-[current=page]/t:bg-tsn22-acc/20 group-aria-[current=page]/t:text-tsn22-acc"><svg class="size-[22px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></svg><span data-tsn22-badge class="absolute right-2.5 top-0.5 grid h-4 min-w-4 place-items-center rounded-full bg-tsn22-hot px-1 text-[10px] font-bold text-white ring-2 ring-tsn22-bar">3</span></span>Inbox
            </button>
            <button type="button" data-tsn22-tab="profile" class="group/t relative grid min-h-14 flex-1 place-items-center content-center gap-1 rounded-2xl text-[11px] font-semibold text-tsn22-mut transition-colors hover:text-tsn22-ink focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsn22-acc aria-[current=page]:text-tsn22-ink">
              <span class="relative grid h-8 w-14 place-items-center rounded-full transition-colors group-aria-[current=page]/t:bg-tsn22-acc/20 group-aria-[current=page]/t:text-tsn22-acc"><svg class="size-[22px]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></span>Profile
            </button>
          </div>
          <span aria-hidden="true" class="absolute bottom-1.5 left-1/2 h-1 w-32 -translate-x-1/2 rounded-full bg-tsn22-ink/80"></span>
        </nav>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn22-stage: #08080a;
  --color-tsn22-stage: oklch(0.13 0.004 285);
  --color-tsn22-bg: #0f0f12;
  --color-tsn22-bg: oklch(0.17 0.006 285);
  --color-tsn22-bar: #16161b;
  --color-tsn22-bar: oklch(0.2 0.008 285);
  --color-tsn22-card: #1c1c22;
  --color-tsn22-card: oklch(0.23 0.01 285);
  --color-tsn22-ink: #f4f4f6;
  --color-tsn22-ink: oklch(0.96 0.004 285);
  --color-tsn22-mut: #a3a3ad;
  --color-tsn22-mut: oklch(0.73 0.01 285);
  --color-tsn22-acc: #a3e635;
  --color-tsn22-acc: oklch(0.86 0.2 128);
  --color-tsn22-hot: #f43f5e;
  --color-tsn22-hot: oklch(0.64 0.22 15);
  --color-tsn22-line: #f4f4f61a;
  --color-tsn22-line: oklch(0.96 0.004 285 / 0.1);
  --font-tsn22-sans: 'Outfit', system-ui, sans-serif;
  --font-tsn22-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-22 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-22').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const tabs = [...root.querySelectorAll('[data-tsn22-tab]')];
    const panels = [...root.querySelectorAll('[data-tsn22-panel]')];
    const title = root.querySelector('[data-tsn22-title]');
    const scroller = root.querySelector('[data-tsn22-scroller]');
    tabs.forEach((t) => t.addEventListener('click', () => {
      const id = t.dataset.tsn22Tab;
      tabs.forEach((x) => (x === t ? x.setAttribute('aria-current', 'page') : x.removeAttribute('aria-current')));
      panels.forEach((p) => { p.hidden = p.dataset.tsn22Panel !== id; });
      title.textContent = t.textContent.trim();
      scroller.scrollTo({ top: 0 });
      if (id === 'inbox') { const b = root.querySelector('[data-tsn22-badge]'); if (b) b.remove(); }
    }));
    root.querySelectorAll('[data-tsn22-panel] a[href="#"]').forEach((a) => a.addEventListener('click', (e) => e.preventDefault()));
  });
})();
```
