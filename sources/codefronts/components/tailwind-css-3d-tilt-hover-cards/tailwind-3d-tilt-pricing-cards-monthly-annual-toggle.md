---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-pricing-cards-monthly-annual-toggle/"
title: "Tailwind 3D Tilt Pricing Cards with Monthly / Annual Toggle"
section: "components"
category: "tailwind-css-3d-tilt-hover-cards"
category_name: "Tailwind CSS 3D Tilt Hover Cards"
description: "A three-tier SaaS pricing row where every card tilts toward the cursor and the featured Pro tier adds a scale boost and a violet glow."
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Tilt Pricing Cards with Monthly / Annual Toggle
Source: https://codefronts.com/components/tailwind-css-3d-tilt-hover-cards/tailwind-3d-tilt-pricing-cards-monthly-annual-toggle/

A three-tier SaaS pricing row where every card tilts toward the cursor and the featured Pro tier adds a scale boost and a violet glow. The port finishes what the CSS original only promised: a working monthly/annual toggle whose prices swap through group-data-annual/root: variants, with tabular-nums keeping the digits rock-steady.
## HTML
```html
<section data-ttc03-root class="ttc-03 group/root w-full min-h-svh grid place-items-center bg-ttc03-bg bg-[radial-gradient(90%_100%_at_50%_0%,var(--color-ttc03-lobe),transparent_60%)] px-5 py-14 font-ttc03-sans text-ttc03-ink" aria-label="3D tilt pricing cards demo">
  <div class="grid w-full max-w-3xl justify-items-center gap-9">
    <div class="grid justify-items-center gap-2">
      <div role="group" aria-label="Billing period" class="inline-flex rounded-full bg-white/5 p-1 ring-1 ring-white/10">
        <button type="button" data-period="monthly" aria-pressed="true" class="min-h-11 cursor-pointer rounded-full px-5 text-sm font-semibold text-ttc03-mut transition-colors aria-pressed:bg-white aria-pressed:text-ttc03-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttc03-glow">Monthly</button>
        <button type="button" data-period="annual" aria-pressed="false" class="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-5 text-sm font-semibold text-ttc03-mut transition-colors aria-pressed:bg-white aria-pressed:text-ttc03-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttc03-glow">Annual <span class="rounded-full bg-ttc03-glow/25 px-2 py-0.5 text-[11px] text-ttc03-badge">−20%</span></button>
      </div>
      <p aria-live="polite" class="text-xs text-ttc03-mut"><span class="group-data-annual/root:hidden">Billed monthly. Cancel anytime.</span><span class="hidden group-data-annual/root:inline">Billed yearly — two months free.</span></p>
    </div>
    <div class="flex w-full flex-wrap justify-center gap-5">
      <article data-ttc03-card class="relative flex-[1_1_13rem] max-w-60 rounded-[20px] border border-white/10 bg-linear-165 from-ttc03-card1 to-ttc03-card2 p-6 shadow-[0_20px_44px_-26px_oklch(0_0_0/0.8)] [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))_scale(var(--pop,1))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none">
        <h3 class="text-[15px] font-semibold text-ttc03-mut">Starter</h3>
        <p class="mt-2 tabular-nums"><strong class="text-[38px] font-extrabold tracking-[-0.03em]"><span class="group-data-annual/root:hidden">$12</span><span class="hidden group-data-annual/root:inline">$10</span></strong><span class="text-sm text-ttc03-mut">/mo</span></p>
        <ul class="mt-4 grid gap-2.5 text-[13.5px] text-ttc03-mut">
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>3 projects</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Community support</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>1 GB storage</li>
        </ul>
        <button type="button" class="mt-6 min-h-11 w-full cursor-pointer rounded-xl border border-white/25 text-sm font-semibold transition-colors hover:bg-white/8 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Choose Starter</button>
      </article>
      <article data-ttc03-card data-featured class="relative flex-[1_1_13rem] max-w-60 rounded-[20px] border border-ttc03-glow/55 bg-linear-165 from-ttc03-card1 to-ttc03-card2 p-6 shadow-[0_20px_50px_-22px_var(--color-ttc03-glowsoft)] [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))_scale(var(--pop,1))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear data-live:[--pop:1.045] data-live:shadow-[0_28px_64px_-20px_var(--color-ttc03-glow)] motion-reduce:transition-none">
        <span class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-linear-120 from-ttc03-glow to-ttc03-glow2 px-3 py-1.5 text-[10px] leading-none font-bold tracking-[0.12em] whitespace-nowrap text-white">MOST POPULAR</span>
        <h3 class="text-[15px] font-semibold text-ttc03-mut">Pro</h3>
        <p class="mt-2 tabular-nums"><strong class="text-[38px] font-extrabold tracking-[-0.03em]"><span class="group-data-annual/root:hidden">$29</span><span class="hidden group-data-annual/root:inline">$23</span></strong><span class="text-sm text-ttc03-mut">/mo</span></p>
        <ul class="mt-4 grid gap-2.5 text-[13.5px] text-ttc03-mut">
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited projects</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Priority support</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>100 GB storage</li>
        </ul>
        <button type="button" class="mt-6 min-h-11 w-full cursor-pointer rounded-xl bg-linear-120 from-ttc03-glow to-ttc03-glow2 text-sm font-semibold text-white transition-[filter] hover:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Choose Pro</button>
      </article>
      <article data-ttc03-card class="relative flex-[1_1_13rem] max-w-60 rounded-[20px] border border-white/10 bg-linear-165 from-ttc03-card1 to-ttc03-card2 p-6 shadow-[0_20px_44px_-26px_oklch(0_0_0/0.8)] [transform:perspective(1000px)_rotateX(var(--rx,0deg))_rotateY(var(--ry,0deg))_scale(var(--pop,1))] transition-[transform,box-shadow] duration-550 ease-[cubic-bezier(0.2,0.9,0.3,1.1)] data-live:duration-80 data-live:ease-linear motion-reduce:transition-none">
        <h3 class="text-[15px] font-semibold text-ttc03-mut">Team</h3>
        <p class="mt-2 tabular-nums"><strong class="text-[38px] font-extrabold tracking-[-0.03em]"><span class="group-data-annual/root:hidden">$79</span><span class="hidden group-data-annual/root:inline">$63</span></strong><span class="text-sm text-ttc03-mut">/mo</span></p>
        <ul class="mt-4 grid gap-2.5 text-[13.5px] text-ttc03-mut">
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Everything in Pro</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>SSO &amp; audit log</li>
          <li class="flex gap-2.5"><svg aria-hidden="true" viewBox="0 0 16 16" class="mt-0.5 size-4 flex-none text-ttc03-glow"><path d="M3 8.5l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited storage</li>
        </ul>
        <button type="button" class="mt-6 min-h-11 w-full cursor-pointer rounded-xl border border-white/25 text-sm font-semibold transition-colors hover:bg-white/8 focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-white">Choose Team</button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttc03-bg: #0e0c17;
  --color-ttc03-bg: oklch(0.15 0.02 285);
  --color-ttc03-lobe: #2c1d4dcc;
  --color-ttc03-lobe: oklch(0.24 0.06 295 / 0.8);
  --color-ttc03-card1: #1f1b2b;
  --color-ttc03-card1: oklch(0.22 0.03 290);
  --color-ttc03-card2: #16131f;
  --color-ttc03-card2: oklch(0.18 0.025 285);
  --color-ttc03-ink: #eeedf6;
  --color-ttc03-ink: oklch(0.95 0.01 280);
  --color-ttc03-mut: #bdb9cc;
  --color-ttc03-mut: oklch(0.8 0.02 285);
  --color-ttc03-glow: #8a5cf0;
  --color-ttc03-glow: oklch(0.62 0.21 295);
  --color-ttc03-glowsoft: #8a5cf08c;
  --color-ttc03-glowsoft: oklch(0.62 0.21 295 / 0.55);
  --color-ttc03-glow2: #b048c0;
  --color-ttc03-glow2: oklch(0.56 0.2 330);
  --color-ttc03-badge: #d9c8ff;
  --color-ttc03-badge: oklch(0.86 0.08 295);
  --font-ttc03-sans: 'Geist', system-ui, sans-serif;
  --font-ttc03-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttc-03 {
  width: 100%;
  min-height: 100svh;
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('[data-ttc03-root]').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    // Billing toggle: one attribute on the root, aria-pressed on the buttons. Prices swap in CSS.
    const btns = root.querySelectorAll('[data-period]');
    btns.forEach((b) => b.addEventListener('click', () => {
      const annual = b.dataset.period === 'annual';
      root.toggleAttribute('data-annual', annual);
      btns.forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    }));
    if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const MAX = 9;
    root.querySelectorAll('[data-ttc03-card]').forEach((card) => { // adding a 4th tier is pure HTML
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
        card.style.setProperty('--rx', ((0.5 - py) * MAX).toFixed(2) + 'deg');
        card.style.setProperty('--ry', ((px - 0.5) * MAX).toFixed(2) + 'deg');
        card.setAttribute('data-live', ''); // featured card also picks up --pop here
      });
      card.addEventListener('pointerleave', () => {
        card.removeAttribute('data-live');
        card.style.setProperty('--rx', '0deg');
        card.style.setProperty('--ry', '0deg');
      });
    });
  });
})();
```
