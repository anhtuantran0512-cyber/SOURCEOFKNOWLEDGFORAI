---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-skeleton-loading-shimmer/"
title: "Tailwind Pricing Cards with Skeleton Loading Shimmer"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Perceived performance for API-priced products: cards render instantly as shimmering skeletons in the exact final geometry, then real prices crossfade in when…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Skeleton Loading Shimmer
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-skeleton-loading-shimmer/

Perceived performance for API-priced products: cards render instantly as shimmering skeletons in the exact final geometry, then real prices crossfade in when the (simulated) pricing API responds — zero layout shift from first paint. The shimmer is an after:animate-tpt21-sheen sweep on translate; the swap is group-data-ready/g:; and while loading the grid is inert, so no one can click a CTA that isn't there yet.
## HTML
```html
<section class="tpt-21 w-full min-h-svh grid place-items-center bg-tpt21-bg px-5 py-16 font-tpt21-sans text-tpt21-ink antialiased" aria-label="Pricing cards with loading states" data-tpt21-root>
  <div class="grid w-full max-w-5xl gap-8">
    <header class="flex flex-wrap items-center justify-between gap-4">
      <h2 class="text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em]">Live API pricing</h2>
      <button type="button" data-reload class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full border-[1.5px] border-tpt21-acc/35 px-4.5 text-[13px] font-semibold text-tpt21-acc-ink transition-colors hover:bg-tpt21-acc/8 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt21-acc"><svg class="size-3.5" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M13.5 8a5.5 5.5 0 1 1-1.6-3.9M13.5 2.5v3h-3"/></svg>Replay loading</button>
    </header>
    <div data-grid aria-busy="true" inert class="group/g grid gap-5 md:grid-cols-3">
      <article data-plan="0" class="flex flex-col gap-4 rounded-[20px] border border-tpt21-line bg-white p-7">
        <span class="relative block h-[18px]"><span class="relative block h-4 w-1/2 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="name" class="absolute inset-0 text-[13px] font-semibold tracking-[0.08em] text-tpt21-mut uppercase opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-[50px]"><span class="relative block h-11 w-2/5 overflow-hidden rounded-lg bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="price" class="absolute inset-0 text-[42px] leading-[50px] font-bold tracking-[-0.035em] opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100 [&_small]:text-[15px] [&_small]:font-medium [&_small]:tracking-normal [&_small]:text-tpt21-mut"></b></span>
        <span class="relative grid h-[88px] content-start gap-3"><span class="relative block h-3 w-[88%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-[72%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-4/5 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="feats" class="absolute inset-0 text-sm leading-[1.9] font-normal text-tpt21-body opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-11"><span class="absolute inset-0 overflow-hidden rounded-xl bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><a href="#" data-real="cta" class="absolute inset-0 grid place-items-center rounded-xl border-[1.5px] border-tpt21-line text-sm font-semibold text-tpt21-ink no-underline opacity-0 transition-[opacity,border-color] duration-450 hover:border-tpt21-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt21-acc group-data-ready/g:opacity-100"></a></span>
      </article>
      <article data-plan="1" class="flex flex-col gap-4 rounded-[20px] bg-white p-7 ring-2 ring-tpt21-acc [&_*]:[transition-delay:80ms]">
        <span class="relative block h-[18px]"><span class="relative block h-4 w-1/2 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="name" class="absolute inset-0 text-[13px] font-semibold tracking-[0.08em] text-tpt21-acc-ink uppercase opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-[50px]"><span class="relative block h-11 w-2/5 overflow-hidden rounded-lg bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="price" class="absolute inset-0 text-[42px] leading-[50px] font-bold tracking-[-0.035em] opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100 [&_small]:text-[15px] [&_small]:font-medium [&_small]:tracking-normal [&_small]:text-tpt21-mut"></b></span>
        <span class="relative grid h-[88px] content-start gap-3"><span class="relative block h-3 w-[88%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-[72%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-4/5 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="feats" class="absolute inset-0 text-sm leading-[1.9] font-normal text-tpt21-body opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-11"><span class="absolute inset-0 overflow-hidden rounded-xl bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><a href="#" data-real="cta" class="absolute inset-0 grid place-items-center rounded-xl bg-tpt21-acc text-sm font-semibold text-white no-underline opacity-0 transition-[opacity,background-color] duration-450 hover:bg-tpt21-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt21-acc group-data-ready/g:opacity-100"></a></span>
      </article>
      <article data-plan="2" class="flex flex-col gap-4 rounded-[20px] border border-tpt21-line bg-white p-7 [&_*]:[transition-delay:160ms]">
        <span class="relative block h-[18px]"><span class="relative block h-4 w-1/2 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="name" class="absolute inset-0 text-[13px] font-semibold tracking-[0.08em] text-tpt21-mut uppercase opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-[50px]"><span class="relative block h-11 w-2/5 overflow-hidden rounded-lg bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="price" class="absolute inset-0 text-[42px] leading-[50px] font-bold tracking-[-0.035em] opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100 [&_small]:text-[15px] [&_small]:font-medium [&_small]:tracking-normal [&_small]:text-tpt21-mut"></b></span>
        <span class="relative grid h-[88px] content-start gap-3"><span class="relative block h-3 w-[88%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-[72%] overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><span class="relative block h-3 w-4/5 overflow-hidden rounded-md bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><b data-real="feats" class="absolute inset-0 text-sm leading-[1.9] font-normal text-tpt21-body opacity-0 transition-opacity duration-450 group-data-ready/g:opacity-100"></b></span>
        <span class="relative block h-11"><span class="absolute inset-0 overflow-hidden rounded-xl bg-tpt21-bone transition-opacity duration-400 after:absolute after:inset-0 after:-translate-x-full after:animate-tpt21-sheen after:bg-[linear-gradient(100deg,transparent_20%,oklch(1_0_0/0.85)_50%,transparent_80%)] after:content-[''] group-data-ready/g:opacity-0 motion-reduce:after:animate-none"></span><a href="#" data-real="cta" class="absolute inset-0 grid place-items-center rounded-xl border-[1.5px] border-tpt21-line text-sm font-semibold text-tpt21-ink no-underline opacity-0 transition-[opacity,border-color] duration-450 hover:border-tpt21-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt21-acc group-data-ready/g:opacity-100"></a></span>
      </article>
    </div>
    <p aria-hidden="true" class="justify-self-center rounded-full border border-tpt21-line bg-white px-3.5 py-2 font-tpt21-mono text-[11.5px] text-tpt21-mut">after:animate-tpt21-sheen · group-data-ready/g: · aria-busy + inert</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt21-bg: #f5f6f9;
  --color-tpt21-bg: oklch(0.97 0.005 265);
  --color-tpt21-bone: #e7e9f1;
  --color-tpt21-bone: oklch(0.935 0.01 270);
  --color-tpt21-ink: #191c26;
  --color-tpt21-ink: oklch(0.22 0.02 270);
  --color-tpt21-body: #444b66;
  --color-tpt21-body: oklch(0.42 0.04 270);
  --color-tpt21-mut: #5e6680;
  --color-tpt21-mut: oklch(0.5 0.035 270);
  --color-tpt21-line: #e0e3ec;
  --color-tpt21-line: oklch(0.91 0.012 270);
  --color-tpt21-acc: #4c5ee0;
  --color-tpt21-acc: oklch(0.55 0.19 268);
  --color-tpt21-acc-ink: #3a49bd;
  --color-tpt21-acc-ink: oklch(0.47 0.18 268);
  --font-tpt21-sans: 'Geist', system-ui, sans-serif;
  --font-tpt21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt21-sheen: tpt21-sheen 1.4s ease-in-out infinite;

  @keyframes tpt21-sheen {
    from {
      translate: -100% 0;
    }

    to {
      translate: 100% 0;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-21 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-tpt21-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const grid = root.querySelector('[data-grid]');
    const DELAY = 1800;
    const PLANS = [
      { name: 'Metered', price: '$0.04<small>/1k calls</small>', feats: 'Pay as you go<br>No minimums<br>Community support', cta: 'Start free' },
      { name: 'Reserved', price: '$149<small>/mo</small>', feats: '5M calls included<br>Burst capacity<br>Priority support', cta: 'Choose Reserved' },
      { name: 'Dedicated', price: '$890<small>/mo</small>', feats: 'Isolated cluster<br>Custom rate limits<br>Solutions engineer', cta: 'Contact sales' },
    ];
    let t = 0;
    const load = () => {
      clearTimeout(t);
      grid.removeAttribute('data-ready');
      grid.setAttribute('aria-busy', 'true');
      grid.inert = true;
      t = setTimeout(() => {
        grid.querySelectorAll('[data-plan]').forEach((card) => {
          const p = PLANS[+card.dataset.plan];
          card.querySelector('[data-real="name"]').textContent = p.name;
          card.querySelector('[data-real="price"]').innerHTML = p.price;
          card.querySelector('[data-real="feats"]').innerHTML = p.feats;
          card.querySelector('[data-real="cta"]').textContent = p.cta;
        });
        grid.setAttribute('aria-busy', 'false');
        grid.inert = false;
        grid.setAttribute('data-ready', '');
      }, DELAY);
    };
    root.querySelector('[data-reload]').addEventListener('click', load);
    load();
  });
})();
```
