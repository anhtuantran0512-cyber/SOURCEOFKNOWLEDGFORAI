---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-stat-counters/"
title: "Tailwind Feature Section with Stat Counters"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A dark metrics band: four stat cards whose numbers count up the first time they scroll into view, each paired with a one-line feature claim and a sparkline."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Section with Stat Counters
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-stat-counters/

A dark metrics band: four stat cards whose numbers count up the first time they scroll into view, each paired with a one-line feature claim and a sparkline. Numbers ship in the HTML at their final value, so with no JS, reduced motion or a screen reader the real figure is always there — the script only animates from zero.
## HTML
```html
<section class="tfs-03 relative w-full min-h-svh overflow-hidden bg-tfs03-bg px-5 py-20 font-tfs03-sans text-white antialiased sm:py-28" aria-labelledby="tfs-03-h" data-tfs03 data-ms="1400">
  <div aria-hidden="true" class="pointer-events-none absolute left-1/2 top-0 h-[28rem] w-[60rem] -translate-x-1/2 rounded-full bg-tfs03-acc/20 blur-[120px]"></div>
  <div class="relative mx-auto grid w-full max-w-6xl gap-14">
    <header class="grid gap-5 lg:grid-cols-[1fr_auto] lg:items-end">
      <div class="grid max-w-2xl gap-4">
        <p class="font-tfs03-mono text-xs uppercase tracking-[0.2em] text-tfs03-acc">Nova by the numbers</p>
        <h2 id="tfs-03-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Built for the scale you're about to hit</h2>
      </div>
      <p class="max-w-sm text-pretty text-tfs03-mut">Live figures from the Nova edge network, refreshed hourly.</p>
    </header>
    <ul class="grid gap-px overflow-hidden rounded-3xl border border-white/10 bg-white/10 sm:grid-cols-2 lg:grid-cols-4">
      <li class="group relative grid gap-6 bg-tfs03-card p-7 transition hover:bg-tfs03-card2">
        <span class="grid size-10 place-items-center rounded-xl bg-tfs03-acc/15 text-tfs03-acc ring-1 ring-tfs03-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg></span>
        <p><span aria-hidden="true" class="block text-5xl font-semibold tabular-nums tracking-tight" data-to="12.4" data-dec="1" data-suffix="M">12.4M</span><span class="sr-only">12.4 million</span><span class="mt-1 block text-sm font-medium text-white">requests per second at peak</span></p>
        <svg aria-hidden="true" viewBox="0 0 120 32" class="h-8 w-full text-tfs03-acc" fill="none"><path d="M0 28 L20 24 L40 26 L60 16 L80 18 L100 8 L120 4" stroke="currentColor" stroke-width="2"/></svg>
        <p class="text-sm text-tfs03-mut">Autoscaling absorbs launch-day spikes without a pager.</p>
      </li>
      <li class="group relative grid gap-6 bg-tfs03-card p-7 transition hover:bg-tfs03-card2">
        <span class="grid size-10 place-items-center rounded-xl bg-tfs03-acc/15 text-tfs03-acc ring-1 ring-tfs03-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20zM12 6v6l4 2"/></svg></span>
        <p><span aria-hidden="true" class="block text-5xl font-semibold tabular-nums tracking-tight" data-to="38" data-suffix="ms">38ms</span><span class="sr-only">38 milliseconds</span><span class="mt-1 block text-sm font-medium text-white">global p95 latency</span></p>
        <svg aria-hidden="true" viewBox="0 0 120 32" class="h-8 w-full text-tfs03-acc" fill="none"><path d="M0 6 L20 10 L40 8 L60 16 L80 20 L100 22 L120 26" stroke="currentColor" stroke-width="2"/></svg>
        <p class="text-sm text-tfs03-mut">Requests terminate at the nearest of 310 edge PoPs.</p>
      </li>
      <li class="group relative grid gap-6 bg-tfs03-card p-7 transition hover:bg-tfs03-card2">
        <span class="grid size-10 place-items-center rounded-xl bg-tfs03-acc/15 text-tfs03-acc ring-1 ring-tfs03-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span>
        <p><span aria-hidden="true" class="block text-5xl font-semibold tabular-nums tracking-tight" data-to="99.999" data-dec="3" data-suffix="%">99.999%</span><span class="sr-only">99.999 percent</span><span class="mt-1 block text-sm font-medium text-white">uptime, last 12 months</span></p>
        <svg aria-hidden="true" viewBox="0 0 120 32" class="h-8 w-full text-tfs03-acc" fill="none"><path d="M0 8 L120 8" stroke="currentColor" stroke-width="2"/><path d="M0 8 L120 8" stroke="currentColor" stroke-opacity=".2" stroke-width="10"/></svg>
        <p class="text-sm text-tfs03-mut">Multi-region failover in under four seconds.</p>
      </li>
      <li class="group relative grid gap-6 bg-tfs03-card p-7 transition hover:bg-tfs03-card2">
        <span class="grid size-10 place-items-center rounded-xl bg-tfs03-acc/15 text-tfs03-acc ring-1 ring-tfs03-acc/30"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span>
        <p><span aria-hidden="true" class="block text-5xl font-semibold tabular-nums tracking-tight" data-to="4200" data-suffix="+">4,200+</span><span class="sr-only">more than 4,200</span><span class="mt-1 block text-sm font-medium text-white">engineering teams</span></p>
        <svg aria-hidden="true" viewBox="0 0 120 32" class="h-8 w-full text-tfs03-acc" fill="none"><path d="M0 30 L20 27 L40 24 L60 19 L80 14 L100 9 L120 2" stroke="currentColor" stroke-width="2"/></svg>
        <p class="text-sm text-tfs03-mut">From two-person startups to the Fortune 100.</p>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs03-bg: #07090f;
  --color-tfs03-bg: oklch(0.14 0.014 268);
  --color-tfs03-card: #0d111b;
  --color-tfs03-card: oklch(0.179 0.022 267);
  --color-tfs03-card2: #121827;
  --color-tfs03-card2: oklch(0.211 0.031 267);
  --color-tfs03-mut: #a3acc2;
  --color-tfs03-mut: oklch(0.744 0.033 268);
  --color-tfs03-acc: #38e1c4;
  --color-tfs03-acc: oklch(0.82 0.139 178);
  --font-tfs03-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tfs03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tfs03]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const ms = +root.dataset.ms || 1400;
    const fmt = (n, dec) => n.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
    const run = (el) => {
      const to = +el.dataset.to, dec = +(el.dataset.dec || 0), suf = el.dataset.suffix || '';
      const t0 = performance.now();
      const tick = (t) => {
        const p = Math.min(1, (t - t0) / ms);
        const e = p === 1 ? 1 : 1 - Math.pow(2, -10 * p);
        el.textContent = fmt(to * e, dec) + suf;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        en.target.querySelectorAll('[data-to]').forEach(run);
        io.unobserve(en.target);
      });
    }, { threshold: 0.4 });
    root.querySelectorAll('li').forEach((li) => io.observe(li));
  });
})();
```
