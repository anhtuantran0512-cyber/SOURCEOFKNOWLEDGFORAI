---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-scrollspy-navbar-highlight-active-section/"
title: "Tailwind Scrollspy Navbar: Highlight Active Section"
section: "navigation"
category: "tailwind-css-sticky-navigations"
category_name: "Tailwind CSS Sticky Navigations"
description: "A one-page landing nav where a solid pill slides to whichever section you're reading."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Scrollspy Navbar: Highlight Active Section
Source: https://codefronts.com/navigation/tailwind-css-sticky-navigations/tailwind-scrollspy-navbar-highlight-active-section/

A one-page landing nav where a solid pill slides to whichever section you're reading. An IntersectionObserver with a thin band at 40% of the viewport decides the active section — no scroll maths — and sets aria-current="location"; the pill reads its position from translate-x-(--tsn23-x) w-(--tsn23-w).
## HTML
```html
<div class="tsn-23 w-full min-h-svh bg-tsn23-bg font-tsn23-sans text-tsn23-ink antialiased" aria-label="Scrollspy navbar demo">
  <a href="#tsn-23-main" class="sr-only focus:not-sr-only focus:fixed focus:left-3 focus:top-3 focus:z-[100] focus:rounded-lg focus:bg-tsn23-ink focus:px-4 focus:py-3 focus:text-sm focus:font-semibold focus:text-tsn23-bg">Skip to content</a>
  <header class="sticky top-0 z-40 flex h-16 items-center gap-4 border-b border-tsn23-line bg-tsn23-bg/85 px-[max(1.25rem,calc((100%-72rem)/2))] backdrop-blur-xl sm:gap-8">
    <a href="#tsn-23-top" class="flex min-h-11 flex-none items-center gap-2 rounded-lg text-lg font-extrabold tracking-[-0.04em] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tsn23-acc">cadence<span aria-hidden="true" class="text-tsn23-acc">/26</span></a>
    <nav data-tsn23-nav aria-label="Sections" style="--tsn23-x:0px;--tsn23-w:0px" class="group/nav relative mx-auto flex min-w-0 gap-1 overflow-x-auto rounded-full border border-tsn23-line p-1 [scrollbar-width:none]">
      <span aria-hidden="true" class="pointer-events-none absolute inset-y-1 left-0 w-(--tsn23-w) translate-x-(--tsn23-x) rounded-full bg-tsn23-acc opacity-0 transition-[translate,width,opacity] duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-data-active/nav:opacity-100 motion-reduce:transition-none"></span>
      <a href="#tsn-23-s1" class="relative inline-flex min-h-10 flex-none items-center rounded-full px-4 text-sm font-semibold text-tsn23-mut transition-colors hover:text-tsn23-ink focus-visible:outline-2 focus-visible:outline-tsn23-acc aria-[current=location]:text-tsn23-bg">Speakers</a>
      <a href="#tsn-23-s2" class="relative inline-flex min-h-10 flex-none items-center rounded-full px-4 text-sm font-semibold text-tsn23-mut transition-colors hover:text-tsn23-ink focus-visible:outline-2 focus-visible:outline-tsn23-acc aria-[current=location]:text-tsn23-bg">Schedule</a>
      <a href="#tsn-23-s3" class="relative inline-flex min-h-10 flex-none items-center rounded-full px-4 text-sm font-semibold text-tsn23-mut transition-colors hover:text-tsn23-ink focus-visible:outline-2 focus-visible:outline-tsn23-acc aria-[current=location]:text-tsn23-bg">Venue</a>
      <a href="#tsn-23-s4" class="relative inline-flex min-h-10 flex-none items-center rounded-full px-4 text-sm font-semibold text-tsn23-mut transition-colors hover:text-tsn23-ink focus-visible:outline-2 focus-visible:outline-tsn23-acc aria-[current=location]:text-tsn23-bg">Tickets</a>
    </nav>
    <a href="#tsn-23-s4" class="inline-flex min-h-11 flex-none items-center rounded-full bg-tsn23-ink px-4 text-sm font-bold text-tsn23-bg hover:bg-tsn23-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsn23-acc max-md:hidden">Get tickets</a>
  </header>
  <div id="tsn-23-top"></div>
  <div class="px-[max(1.25rem,calc((100%-72rem)/2))] pt-[clamp(3rem,8vw,6rem)] pb-[clamp(2rem,5vw,3.5rem)]">
    <p class="font-tsn23-mono text-[11.5px] font-medium uppercase tracking-[0.16em] text-tsn23-acc">Lisbon · 14–16 May 2026</p>
    <h1 class="mt-4 max-w-[18ch] text-[clamp(44px,8vw,104px)] font-extrabold leading-[0.92] tracking-[-0.05em] text-balance">Three days of the web, in rhythm</h1>
    <p class="mt-5 max-w-[54ch] text-[clamp(15px,1.6vw,17px)] leading-relaxed text-tsn23-mut text-pretty">Scroll down. The pill in the nav slides to the section you are reading, driven by an <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">IntersectionObserver</code> band — no scroll maths.</p>
  </div>
  <main id="tsn-23-main" class="px-[max(1.25rem,calc((100%-72rem)/2))] grid gap-5 pb-24">
    <section id="tsn-23-s1" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn23-line bg-tsn23-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-23-h1">
      <p class="font-tsn23-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn23-acc">Speakers</p>
      <h2 id="tsn-23-h1" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">A band, not a threshold</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn23-mut text-pretty">The observer’s root is shrunk to a 5% strip at 40% of the viewport. Exactly one section crosses it at a time, so there is nothing to compare.</p>
    </section>
    <section id="tsn-23-s2" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn23-line bg-tsn23-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-23-h2">
      <p class="font-tsn23-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn23-acc">Schedule</p>
      <h2 id="tsn-23-h2" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">location, not page</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn23-mut text-pretty">In-page position uses <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">aria-current="location"</code>. Screen readers announce “current location”, which is exactly what this is.</p>
    </section>
    <section id="tsn-23-s3" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn23-line bg-tsn23-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-23-h3">
      <p class="font-tsn23-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn23-acc">Venue</p>
      <h2 id="tsn-23-h3" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">The pill measures, Tailwind moves</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn23-mut text-pretty">Two variables on the nav — <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">--tsn23-x</code> and <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">--tsn23-w</code> — drive <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">translate-x-(--tsn23-x)</code> and <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">w-(--tsn23-w)</code>. The label inverts to sit on the pill.</p>
    </section>
    <section id="tsn-23-s4" class="scroll-mt-24 min-h-[44svh] rounded-[1.75rem] border border-tsn23-line bg-tsn23-surface p-[clamp(1.5rem,4vw,3rem)] shadow-[0_1px_2px_rgb(0_0_0/0.04)]" aria-labelledby="tsn-23-h4">
      <p class="font-tsn23-mono text-[11px] font-medium uppercase tracking-[0.16em] text-tsn23-acc">Tickets</p>
      <h2 id="tsn-23-h4" class="mt-3 max-w-[22ch] text-[clamp(24px,3.2vw,36px)] font-semibold leading-[1.1] tracking-[-0.025em] text-balance">Nothing current at the top</h2>
      <p class="mt-4 max-w-[58ch] text-base leading-[1.7] text-tsn23-mut text-pretty">Above the first section no link is current and the pill fades out with <code class="rounded-md bg-tsn23-acc/10 px-1.5 py-0.5 font-tsn23-mono text-[0.86em] text-tsn23-ink">group-data-active/nav:</code>, so the hero never claims to be “Speakers”.</p>
    </section>
  </main>
  <footer class="border-t border-tsn23-line px-[max(1.25rem,calc((100%-72rem)/2))] py-10 font-tsn23-mono text-xs text-tsn23-mut">Tailwind sticky navigation · pattern 23 of 25</footer>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsn23-bg: #0f1222;
  --color-tsn23-bg: oklch(0.19 0.035 275);
  --color-tsn23-surface: #161a2e;
  --color-tsn23-surface: oklch(0.23 0.04 275);
  --color-tsn23-ink: #f3f1ec;
  --color-tsn23-ink: oklch(0.96 0.006 85);
  --color-tsn23-mut: #a9adc4;
  --color-tsn23-mut: oklch(0.76 0.03 275);
  --color-tsn23-acc: #ff8a3d;
  --color-tsn23-acc: oklch(0.75 0.17 50);
  --color-tsn23-line: #f3f1ec1f;
  --color-tsn23-line: oklch(0.96 0.006 85 / 0.12);
  --font-tsn23-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tsn23-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, restated in CSS so the page is sized before the browser build compiles. */

.tsn-23 {
  width: 100%;
  min-height: 100svh;
}
/* Smooth anchor jumps live on <html>, outside the markup, so they stay in CSS. */

@media (prefers-reduced-motion: no-preference) {
  :root:has(.tsn-23) {
    scroll-behavior: smooth;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.tsn-23').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const nav = root.querySelector('[data-tsn23-nav]');
    const links = [...nav.querySelectorAll('a')];
    let active = null;
    const place = () => {
      if (!active) { nav.removeAttribute('data-active'); return; }
      nav.style.setProperty('--tsn23-x', active.offsetLeft + 'px');
      nav.style.setProperty('--tsn23-w', active.offsetWidth + 'px');
      nav.setAttribute('data-active', '');
      nav.scrollTo({ left: active.offsetLeft - nav.clientWidth / 2 + active.offsetWidth / 2, behavior: 'smooth' });
    };
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        active = links.find((a) => a.hash === '#' + e.target.id) || null;
        links.forEach((a) => (a === active ? a.setAttribute('aria-current', 'location') : a.removeAttribute('aria-current')));
        place();
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    links.forEach((a) => { const s = root.querySelector(a.hash); if (s) io.observe(s); });
    const top = root.querySelector('#tsn-23-top');
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) { active = null; links.forEach((a) => a.removeAttribute('aria-current')); place(); }
    }).observe(top);
    new ResizeObserver(place).observe(nav);
  });
})();
```
