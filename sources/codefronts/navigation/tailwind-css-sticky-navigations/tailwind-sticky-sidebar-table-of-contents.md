---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-sidebar-table-of-contents/"
title: "Tailwind Sticky Sidebar Table of Contents"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "The documentation layout: a two-column grid whose sidebar table of contents uses sticky top-20 self-start to follow a long article, highlights the section…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Sidebar Table of Contents
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-sticky-sidebar-table-of-contents/

The documentation layout: a two-column grid whose sidebar table of contents uses sticky top-20 self-start to follow a long article, highlights the section you're reading, and fills a progress rail alongside the links. On narrow screens the sidebar becomes a sticky “On this page” disclosure under the header that always names your current section.
## HTML
```html
<div class="tsn-21 w-full min-h-svh bg-tsn21-bg font-tsn21-sans text-tsn21-ink antialiased" aria-label="Sticky sidebar table of contents demo">
  <a href="#tsn-21-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn21-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn21-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-14 items-center gap-6 border-b border-tsn21-line bg-tsn21-bg/90 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl">
    <a href="#tsn-21-top" class="flex min-h-11 flex-none items-center gap-2 rounded font-semibold tracking-tight focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn21-acc"><span aria-hidden="true" class="font-tsn21-mono text-tsn21-acc">{}</span>Edgebook</a>
    <nav aria-label="Primary" class="flex min-w-0 flex-1 gap-1 overflow-x-auto [scrollbar-width:none]">
      <a href="#tsn-21-top" aria-current="page" class="inline-flex min-h-11 flex-none items-center px-3 text-sm text-tsn21-mut hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=page]:font-medium aria-[current=page]:text-tsn21-ink">Guides</a>
      <a href="#tsn-21-top" class="inline-flex min-h-11 flex-none items-center px-3 text-sm text-tsn21-mut hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc">Reference</a>
      <a href="#tsn-21-top" class="inline-flex min-h-11 flex-none items-center px-3 text-sm text-tsn21-mut hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc">Changelog</a>
    </nav>
  </header>
  <details data-tsn21-mtoc class="group/m sticky top-14 z-30 border-b border-tsn21-line bg-tsn21-bg/95 backdrop-blur-xl lg:hidden">
    <summary class="flex min-h-12 cursor-pointer list-none items-center gap-2 px-[max(1.25rem,calc((100%-72rem)/2))] text-sm focus-visible:outline-2 focus-visible:-outline-offset-2 focus-visible:outline-tsn21-acc [&::-webkit-details-marker]:hidden"><span class="text-tsn21-mut">On this page:</span><span data-tsn21-current class="truncate font-medium">What edge caching actually caches</span><svg class="ms-auto size-4 flex-none transition-transform group-open/m:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6"/></svg></summary>
    <nav aria-label="On this page (mobile)" class="grid px-[max(1.25rem,calc((100%-72rem)/2))] pb-3">
      <a href="#tsn-21-caching" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">What edge caching actually caches</a>
      <a href="#tsn-21-keys" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">Cache keys decide everything</a>
      <a href="#tsn-21-headers" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">Cache-Control, line by line</a>
      <a href="#tsn-21-purge" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">Purging without panic</a>
      <a href="#tsn-21-personal" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">Personalised pages at the edge</a>
      <a href="#tsn-21-measure" class="flex min-h-11 items-center border-l-2 border-tsn21-line pl-3 text-sm text-tsn21-mut aria-[current=true]:border-tsn21-acc aria-[current=true]:text-tsn21-ink">Measuring the hit rate</a>
    </nav>
  </details>
  <div id="tsn-21-top" class="grid scroll-mt-20 gap-14 px-[max(1.25rem,calc((100%-72rem)/2))] pb-24 pt-12 lg:grid-cols-[14rem_minmax(0,1fr)]">
    <aside class="sticky top-20 self-start max-h-[calc(100svh-6rem)] overflow-y-auto max-lg:hidden">
      <p class="font-tsn21-mono text-[11px] font-medium uppercase tracking-[0.14em] text-tsn21-mut">On this page</p>
      <div class="relative mt-4">
        <span aria-hidden="true" class="absolute inset-y-0 left-0 w-0.5 rounded-full bg-tsn21-line"></span>
        <span data-tsn21-rail aria-hidden="true" style="--tsn21-p:0" class="absolute inset-y-0 left-0 w-0.5 origin-top scale-y-(--tsn21-p) rounded-full bg-tsn21-acc/35"></span>
        <nav data-tsn21-toc aria-label="On this page" class="relative grid">
          <a href="#tsn-21-caching" aria-current="true" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">What edge caching actually caches</a>
          <a href="#tsn-21-keys" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">Cache keys decide everything</a>
          <a href="#tsn-21-headers" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">Cache-Control, line by line</a>
          <a href="#tsn-21-purge" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">Purging without panic</a>
          <a href="#tsn-21-personal" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">Personalised pages at the edge</a>
          <a href="#tsn-21-measure" class="-ml-px flex min-h-10 items-center border-l-2 border-transparent py-1.5 pl-4 text-[13.5px] leading-snug text-tsn21-mut transition-colors hover:text-tsn21-ink focus-visible:outline-2 focus-visible:outline-tsn21-acc aria-[current=true]:border-tsn21-acc aria-[current=true]:font-medium aria-[current=true]:text-tsn21-ink">Measuring the hit rate</a>
        </nav>
      </div>
      <a href="#tsn-21-top" class="mt-6 inline-flex min-h-11 items-center gap-1.5 text-[13px] text-tsn21-mut hover:text-tsn21-acc focus-visible:outline-2 focus-visible:outline-tsn21-acc">Back to top ↑</a>
    </aside>
    <article data-tsn21-article id="tsn-21-main" class="min-w-0 max-w-[44rem]">
      <p class="font-tsn21-mono text-[11.5px] uppercase tracking-[0.16em] text-tsn21-acc">sticky top-20 · self-start</p>
      <h1 class="mt-3 text-[clamp(32px,5vw,52px)] font-semibold leading-[1.05] tracking-[-0.035em] text-balance">A field guide to edge caching</h1>
      <p class="mt-4 text-[17px] leading-relaxed text-tsn21-mut text-pretty">Scroll the article. The contents panel follows you, marks the section you are in and fills its rail as you read. Narrow the window and it becomes a sticky disclosure.</p>
      <section id="tsn-21-caching" aria-labelledby="tsn-21-h1" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h1" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">01</span>What edge caching actually caches</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty">An edge cache stores responses in data centres close to your users, so repeat requests never travel to your origin. The win is latency and origin load; the risk is serving something stale.</p>
        
      </section>
      <section id="tsn-21-keys" aria-labelledby="tsn-21-h2" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h2" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">02</span>Cache keys decide everything</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty">Two requests share a cached response only if their keys match. By default that is the URL; add headers or cookies to the key and your hit rate can fall off a cliff.</p>
        
      </section>
      <section id="tsn-21-headers" aria-labelledby="tsn-21-h3" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h3" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">03</span>Cache-Control, line by line</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty"><code class="rounded-md bg-tsn21-acc/10 px-1.5 py-0.5 font-tsn21-mono text-[0.86em] text-tsn21-ink">s-maxage</code> governs shared caches, <code class="rounded-md bg-tsn21-acc/10 px-1.5 py-0.5 font-tsn21-mono text-[0.86em] text-tsn21-ink">max-age</code> the browser, and <code class="rounded-md bg-tsn21-acc/10 px-1.5 py-0.5 font-tsn21-mono text-[0.86em] text-tsn21-ink">stale-while-revalidate</code> lets the edge answer instantly while it refreshes in the background.</p>
        <pre class="mt-6 overflow-x-auto rounded-xl border border-tsn21-line bg-tsn21-ink p-5 font-tsn21-mono text-[13px] leading-relaxed text-tsn21-bg"><code>Cache-Control: public, s-maxage=600,
  stale-while-revalidate=86400</code></pre>
      </section>
      <section id="tsn-21-purge" aria-labelledby="tsn-21-h4" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h4" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">04</span>Purging without panic</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty">Tag responses with surrogate keys at write time, then purge by tag. Purging by URL works until the day one product appears on forty pages.</p>
        
      </section>
      <section id="tsn-21-personal" aria-labelledby="tsn-21-h5" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h5" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">05</span>Personalised pages at the edge</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty">Cache the shell, not the person. Serve a shared HTML document and hydrate the signed-in parts client-side, or vary on a small, coarse cookie.</p>
        
      </section>
      <section id="tsn-21-measure" aria-labelledby="tsn-21-h6" class="mt-14 min-h-[56svh] scroll-mt-32 border-t border-tsn21-line pt-10 lg:scroll-mt-20">
        <h2 id="tsn-21-h6" class="text-[clamp(22px,2.8vw,30px)] font-semibold tracking-[-0.02em]"><span class="mr-2 font-tsn21-mono text-base text-tsn21-acc">06</span>Measuring the hit rate</h2>
        <p class="mt-4 text-base leading-[1.75] text-tsn21-mut text-pretty">Track hit ratio per route, not globally. A 92% average can hide a checkout page at 3% that quietly costs more than everything else combined.</p>
        
      </section>
    </article>
  </div>
  <footer class="border-t border-tsn21-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn21-mono text-xs text-tsn21-mut">Tailwind sticky navigation · pattern 21 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn21-bg: #fbfbfa;
  --color-tsn21-bg: oklch(0.986 0.002 100);
  --color-tsn21-surface: #ffffff;
  --color-tsn21-surface: oklch(1 0 0);
  --color-tsn21-ink: #161a19;
  --color-tsn21-ink: oklch(0.21 0.008 170);
  --color-tsn21-mut: #59605e;
  --color-tsn21-mut: oklch(0.47 0.01 170);
  --color-tsn21-acc: #0f8f63;
  --color-tsn21-acc: oklch(0.56 0.12 160);
  --color-tsn21-line: #161a191a;
  --color-tsn21-line: oklch(0.21 0.008 170 / 0.1);
  --font-tsn21-sans: 'Geist', system-ui, sans-serif;
  --font-tsn21-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-21 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-21) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-21').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const links = [...root.querySelectorAll('[data-tsn21-toc] a, [data-tsn21-mtoc] nav a')];
    const current = root.querySelector('[data-tsn21-current]');
    const mtoc = root.querySelector('[data-tsn21-mtoc]');
    const rail = root.querySelector('[data-tsn21-rail]');
    const art = root.querySelector('[data-tsn21-article]');
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const hash = '#' + e.target.id;
        links.forEach((a) => a.setAttribute('aria-current', String(a.hash === hash)));
        const a = links.find((l) => l.hash === hash);
        if (a) current.textContent = a.textContent;
      });
    }, { rootMargin: '-110px 0px -60% 0px' });
    root.querySelectorAll('section[id]').forEach((s) => spy.observe(s));
    mtoc.addEventListener('click', (e) => { if (e.target.closest('nav a')) mtoc.open = false; });
    let queued = false;
    const tick = () => {
      queued = false;
      const r = art.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (80 - r.top) / Math.max(1, r.height - innerHeight + 80)));
      rail.style.setProperty('--tsn21-p', p.toFixed(4));
    };
    window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(tick); } }, { passive: true });
    tick();
  });
})();
```
