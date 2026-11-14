---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-sub-navigation-bar-under-main-header/"
title: "Tailwind Sticky Sub-Navigation Bar Under Main Header"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The product-page pattern: a slim global header at top-0 and a local sub-nav that scrolls with the page until it locks under it at top-14."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Sub-Navigation Bar Under Main Header
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-sub-navigation-bar-under-main-header/

The product-page pattern: a slim global header at top-0 and a local sub-nav that scrolls with the page until it locks under it at top-14. Once stuck, the sub-nav gains a shadow and reveals the price and a Buy button; while you read, a scrollspy marks the section you're in with aria-current.
## HTML
```html
<div class="tsn-19 w-full min-h-svh bg-tsn19-bg font-tsn19-sans text-tsn19-ink antialiased" aria-label="Sticky sub-navigation under main header demo">
  <a href="#tsn-19-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn19-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn19-bg">Skip to content</a>
  <header class="sticky top-0 z-50 flex h-14 items-center gap-6 bg-black/85 px-[max(1.25rem,calc((100%-72rem)/2))] text-white backdrop-blur-xl">
    <a href="#tsn-19-hero" class="flex min-h-11 flex-none items-center gap-2 rounded text-sm font-semibold tracking-[0.12em] uppercase focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn19-acc">Aero</a>
    <nav aria-label="Global" class="flex min-w-0 flex-1 justify-center gap-1 overflow-x-auto [scrollbar-width:none] max-sm:justify-start">
      <a href="#tsn-19-hero" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn19-acc">Store</a>
      <a href="#tsn-19-hero" aria-current="page" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn19-acc aria-[current=page]:text-white">Audio</a>
      <a href="#tsn-19-hero" class="inline-flex min-h-11 flex-none items-center px-3 text-[13px] text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-tsn19-acc">Support</a>
    </nav>
    <a href="#tsn-19-s4" class="grid size-11 flex-none place-items-center rounded-full text-white/85 hover:bg-white/10 focus-visible:outline-2 focus-visible:outline-tsn19-acc"><span class="sr-only">Bag</span><svg class="size-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6"/><circle cx="10" cy="20" r="1.3"/><circle cx="17" cy="20" r="1.3"/></svg></a>
  </header>
  <section id="tsn-19-hero" aria-labelledby="tsn-19-title" class="relative isolate grid min-h-[78svh] scroll-mt-14 place-items-center overflow-hidden px-5 py-20 text-center">
    <div aria-hidden="true" class="absolute left-1/2 top-1/2 -z-10 size-[min(80vw,40rem)] -translate-x-1/2 -translate-y-1/2 rounded-full bg-[radial-gradient(circle,var(--color-tsn19-acc)_0%,transparent_65%)] opacity-35 blur-2xl"></div>
    <div>
      <p class="font-tsn19-mono text-[11.5px] uppercase tracking-[0.18em] text-tsn19-acc">sticky top-14 · data-stuck</p>
      <h1 id="tsn-19-title" class="mt-4 text-[clamp(56px,11vw,140px)] font-semibold leading-[0.9] tracking-[-0.05em]">Aero One</h1>
      <p class="mx-auto mt-5 max-w-[40ch] text-lg text-tsn19-mut">Scroll: the bar below locks under the header, then offers the price and a Buy button.</p>
    </div>
  </section>
  <span data-tsn19-sentinel aria-hidden="true" class="block h-px"></span>
  <div data-tsn19-sub class="group/sub sticky top-14 z-40 border-y border-tsn19-line bg-tsn19-bg/85 backdrop-blur-xl transition-shadow data-stuck:shadow-[0_18px_30px_-18px_rgb(0_0_0/0.8)]">
    <div class="flex h-13 items-center gap-4 px-[max(1.25rem,calc((100%-72rem)/2))]">
      <p class="flex-none text-[15px] font-semibold tracking-tight max-sm:hidden">Aero One</p>
      <nav data-tsn19-nav aria-label="Product sections" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none] sm:justify-center">
        <a href="#tsn-19-s1" aria-current="true" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[13px] font-medium text-tsn19-mut transition-colors hover:text-tsn19-ink focus-visible:outline-2 focus-visible:outline-tsn19-acc aria-[current=true]:bg-tsn19-ink/10 aria-[current=true]:text-tsn19-ink">Overview</a>
        <a href="#tsn-19-s2" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[13px] font-medium text-tsn19-mut transition-colors hover:text-tsn19-ink focus-visible:outline-2 focus-visible:outline-tsn19-acc aria-[current=true]:bg-tsn19-ink/10 aria-[current=true]:text-tsn19-ink">Design</a>
        <a href="#tsn-19-s3" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[13px] font-medium text-tsn19-mut transition-colors hover:text-tsn19-ink focus-visible:outline-2 focus-visible:outline-tsn19-acc aria-[current=true]:bg-tsn19-ink/10 aria-[current=true]:text-tsn19-ink">Specs</a>
        <a href="#tsn-19-s4" class="inline-flex min-h-11 flex-none items-center rounded-full px-3.5 text-[13px] font-medium text-tsn19-mut transition-colors hover:text-tsn19-ink focus-visible:outline-2 focus-visible:outline-tsn19-acc aria-[current=true]:bg-tsn19-ink/10 aria-[current=true]:text-tsn19-ink">Reviews</a>
      </nav>
      <div data-tsn19-buy inert class="flex flex-none translate-y-1 items-center gap-3 opacity-0 transition duration-300 group-data-stuck/sub:translate-y-0 group-data-stuck/sub:opacity-100 motion-reduce:transition-none">
        <p class="text-sm tabular-nums text-tsn19-mut max-md:hidden">From <span class="font-semibold text-tsn19-ink">$349</span></p>
        <a href="#tsn-19-s4" class="inline-flex min-h-9 items-center rounded-full bg-tsn19-acc px-4 text-[13px] font-semibold text-black hover:brightness-110 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn19-acc">Buy</a>
      </div>
    </div>
  </div>
  <main id="tsn-19-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pt-[clamp(2rem,5vw,3.5rem)] pb-24">
    <section id="tsn-19-s1" class="scroll-mt-32 min-h-[44svh] rounded-[1.75rem] border border-tsn19-line bg-tsn19-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-19-h1">
      <p class="font-tsn19-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn19-acc">Overview</p>
      <h2 id="tsn-19-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A lock within a lock</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn19-mut text-pretty">The global header is <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">sticky top-0 h-14</code>. The sub-nav is <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">sticky top-14</code>: it scrolls with the page, then locks exactly under the header.</p>
    </section>
    <section id="tsn-19-s2" class="scroll-mt-32 min-h-[44svh] rounded-[1.75rem] border border-tsn19-line bg-tsn19-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-19-h2">
      <p class="font-tsn19-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn19-acc">Design</p>
      <h2 id="tsn-19-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Knowing it’s stuck</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn19-mut text-pretty">CSS can’t report pinned state, but a 1px sentinel before the sub-nav can. When it passes the header line, an observer sets <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">data-stuck</code>.</p>
    </section>
    <section id="tsn-19-s3" class="scroll-mt-32 min-h-[44svh] rounded-[1.75rem] border border-tsn19-line bg-tsn19-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-19-h3">
      <p class="font-tsn19-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn19-acc">Specs</p>
      <h2 id="tsn-19-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Buy, only when it helps</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn19-mut text-pretty">Price and Buy are present from the start but <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">inert</code> and transparent. Once the bar locks, <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">group-data-stuck/sub:</code> reveals them and the script lifts <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">inert</code>.</p>
    </section>
    <section id="tsn-19-s4" class="scroll-mt-32 min-h-[44svh] rounded-[1.75rem] border border-tsn19-line bg-tsn19-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-19-h4">
      <p class="font-tsn19-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn19-acc">Reviews</p>
      <h2 id="tsn-19-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">You are here</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn19-mut text-pretty">A second observer watches the sections through a band just under both bars and moves <code class="rounded-md bg-tsn19-acc/10 px-1.5 py-0.5 font-tsn19-mono text-[0.86em] text-tsn19-ink">aria-current</code> as you read.</p>
    </section>
  </main>
  <footer class="border-t border-tsn19-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn19-mono text-xs text-tsn19-mut">Tailwind sticky navigation · pattern 19 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn19-bg: #0a0a0b;
  --color-tsn19-bg: oklch(0.145 0.002 285);
  --color-tsn19-surface: #141416;
  --color-tsn19-surface: oklch(0.19 0.004 285);
  --color-tsn19-ink: #f5f5f7;
  --color-tsn19-ink: oklch(0.97 0.003 285);
  --color-tsn19-mut: #a1a1a8;
  --color-tsn19-mut: oklch(0.72 0.008 285);
  --color-tsn19-acc: #7dd3fc;
  --color-tsn19-acc: oklch(0.84 0.1 225);
  --color-tsn19-line: #f5f5f71a;
  --color-tsn19-line: oklch(0.97 0.003 285 / 0.1);
  --font-tsn19-sans: 'Geist', system-ui, sans-serif;
  --font-tsn19-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-19 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-19) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-19').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const sub = root.querySelector('[data-tsn19-sub]');
    const buy = root.querySelector('[data-tsn19-buy]');
    const sentinel = root.querySelector('[data-tsn19-sentinel]');
    const links = [...root.querySelectorAll('[data-tsn19-nav] a')];
    new IntersectionObserver(([e]) => {
      const stuck = !e.isIntersecting && e.boundingClientRect.top < 80;
      sub.toggleAttribute('data-stuck', stuck);
      buy.inert = !stuck;
    }, { rootMargin: '-57px 0px 0px 0px' }).observe(sentinel);
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.setAttribute('aria-current', String(a.hash === '#' + e.target.id)));
      });
    }, { rootMargin: '-120px 0px -55% 0px' });
    links.forEach((a) => { const s = root.querySelector(a.hash); if (s) spy.observe(s); });
  });
})();
```
