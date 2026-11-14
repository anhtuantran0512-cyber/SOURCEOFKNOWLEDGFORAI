---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-pricing-comparison-table-expandable/"
title: "Tailwind CSS Pricing Comparison Table with Expandable Features"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Minimal-first pricing that conversion teams love: three clean cards and one &ldquo;Compare all features&rdquo; toggle that unfolds a real,…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pricing Comparison Table with Expandable Features
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-pricing-comparison-table-expandable/

Minimal-first pricing that conversion teams love: three clean cards and one &ldquo;Compare all features&rdquo; toggle that unfolds a real, screen-reader-friendly <table> beneath. The unfold is v4 arbitrary values — grid-rows-[0fr] to group-has-checked/p:grid-rows-[1fr] — so the matrix animates to its natural height with no measuring.
## HTML
```html
<section class="tpt-03 group/p w-full min-h-svh grid place-items-center bg-tpt03-bg px-5 py-16 font-tpt03-sans text-tpt03-ink antialiased" aria-label="Pricing with expandable feature comparison table">
  <div class="grid w-full max-w-4xl justify-items-center gap-7">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em] text-balance">Start free. Upgrade when it clicks.</h2>
    <div class="grid w-full gap-4 sm:grid-cols-3">
      <article class="flex flex-col items-center gap-1 rounded-2xl border border-tpt03-line bg-white p-7 text-center">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt03-mut uppercase">Basic</h3>
        <p class="text-[42px] font-bold tracking-[-0.035em]">$0</p>
        <span class="mb-5 text-[13px] text-tpt03-mut">forever</span>
        <a href="#" class="grid min-h-11 w-full place-items-center rounded-xl border-[1.5px] border-tpt03-line text-sm font-semibold text-tpt03-ink no-underline transition-colors hover:border-tpt03-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt03-acc">Sign up</a>
      </article>
      <article class="flex flex-col items-center gap-1 rounded-2xl bg-white p-7 text-center shadow-[0_18px_40px_-26px_var(--color-tpt03-acc)] ring-2 ring-tpt03-acc">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt03-acc-ink uppercase">Pro</h3>
        <p class="text-[42px] font-bold tracking-[-0.035em]">$19</p>
        <span class="mb-5 text-[13px] text-tpt03-mut">per user / month</span>
        <a href="#" class="grid min-h-11 w-full place-items-center rounded-xl bg-tpt03-acc text-sm font-semibold text-white no-underline transition-colors hover:bg-tpt03-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt03-acc">Start 14-day trial</a>
      </article>
      <article class="flex flex-col items-center gap-1 rounded-2xl border border-tpt03-line bg-white p-7 text-center">
        <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt03-mut uppercase">Enterprise</h3>
        <p class="text-[42px] font-bold tracking-[-0.035em]">Custom</p>
        <span class="mb-5 text-[13px] text-tpt03-mut">annual contract</span>
        <a href="#" class="grid min-h-11 w-full place-items-center rounded-xl border-[1.5px] border-tpt03-line text-sm font-semibold text-tpt03-ink no-underline transition-colors hover:border-tpt03-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt03-acc">Talk to sales</a>
      </article>
    </div>
    <input type="checkbox" id="tpt03-more" class="peer sr-only" aria-controls="tpt03-matrix">
    <label for="tpt03-more" class="flex min-h-11 cursor-pointer items-center gap-2.5 rounded-full border-[1.5px] border-tpt03-acc/35 px-5 text-sm font-semibold text-tpt03-acc-ink transition-colors hover:bg-tpt03-acc/8 peer-focus-visible:outline-3 peer-focus-visible:outline-offset-2 peer-focus-visible:outline-tpt03-acc">
      <span class="grid">
        <span class="col-start-1 row-start-1 transition-opacity group-has-checked/p:opacity-0">Compare all features</span>
        <span class="col-start-1 row-start-1 opacity-0 transition-opacity group-has-checked/p:opacity-100">Hide comparison</span>
      </span>
      <svg class="size-3.5 transition-transform duration-300 group-has-checked/p:rotate-180 motion-reduce:transition-none" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </label>
    <div id="tpt03-matrix" class="invisible grid w-full grid-rows-[0fr] transition-[grid-template-rows,visibility] duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:visible group-has-checked/p:grid-rows-[1fr] motion-reduce:transition-none">
      <div class="min-h-0 overflow-hidden">
        <div class="overflow-x-auto rounded-2xl border border-tpt03-line bg-white">
          <table class="w-full min-w-[520px] border-collapse text-left text-sm">
            <caption class="sr-only">Feature comparison of Basic, Pro and Enterprise plans</caption>
            <thead class="bg-tpt03-head text-[11.5px] tracking-[0.08em] text-tpt03-mut uppercase">
              <tr><th scope="col" class="sticky left-0 bg-tpt03-head px-4 py-3 font-semibold">Feature</th><th scope="col" class="px-4 py-3 font-semibold">Basic</th><th scope="col" class="bg-tpt03-acc/10 px-4 py-3 font-semibold text-tpt03-acc-ink">Pro</th><th scope="col" class="px-4 py-3 font-semibold">Enterprise</th></tr>
            </thead>
            <tbody class="text-tpt03-body *:border-t *:border-tpt03-line">
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">Projects</th><td class="px-4 py-3">3</td><td class="bg-tpt03-acc/6 px-4 py-3">Unlimited</td><td class="px-4 py-3">Unlimited</td></tr>
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">Storage</th><td class="px-4 py-3">1 GB</td><td class="bg-tpt03-acc/6 px-4 py-3">100 GB</td><td class="px-4 py-3">Unlimited</td></tr>
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">API access</th><td class="px-4 py-3 text-tpt03-mut"><span aria-hidden="true">—</span><span class="sr-only">Not included</span></td><td class="bg-tpt03-acc/6 px-4 py-3 font-bold text-tpt03-acc-ink"><span aria-hidden="true">✓</span><span class="sr-only">Included</span></td><td class="px-4 py-3 font-bold text-tpt03-acc-ink"><span aria-hidden="true">✓</span><span class="sr-only">Included</span></td></tr>
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">SSO / SAML</th><td class="px-4 py-3 text-tpt03-mut"><span aria-hidden="true">—</span><span class="sr-only">Not included</span></td><td class="bg-tpt03-acc/6 px-4 py-3 text-tpt03-mut"><span aria-hidden="true">—</span><span class="sr-only">Not included</span></td><td class="px-4 py-3 font-bold text-tpt03-acc-ink"><span aria-hidden="true">✓</span><span class="sr-only">Included</span></td></tr>
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">Audit log</th><td class="px-4 py-3 text-tpt03-mut"><span aria-hidden="true">—</span><span class="sr-only">Not included</span></td><td class="bg-tpt03-acc/6 px-4 py-3 font-bold text-tpt03-acc-ink"><span aria-hidden="true">✓</span><span class="sr-only">Included</span></td><td class="px-4 py-3 font-bold text-tpt03-acc-ink"><span aria-hidden="true">✓</span><span class="sr-only">Included</span></td></tr>
              <tr><th scope="row" class="sticky left-0 bg-white px-4 py-3 font-medium text-tpt03-ink">Support SLA</th><td class="px-4 py-3">Community</td><td class="bg-tpt03-acc/6 px-4 py-3">24 h</td><td class="px-4 py-3">1 h</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt03-line bg-white px-3.5 py-2 font-tpt03-mono text-[11.5px] text-tpt03-mut">grid-rows-[0fr] → group-has-checked/p:grid-rows-[1fr]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt03-bg: #f8f8f4;
  --color-tpt03-bg: oklch(0.978 0.006 110);
  --color-tpt03-head: #f3f4ee;
  --color-tpt03-head: oklch(0.962 0.008 115);
  --color-tpt03-ink: #1b1f1c;
  --color-tpt03-ink: oklch(0.23 0.01 150);
  --color-tpt03-body: #414842;
  --color-tpt03-body: oklch(0.4 0.012 150);
  --color-tpt03-mut: #5f665f;
  --color-tpt03-mut: oklch(0.5 0.012 150);
  --color-tpt03-line: #e3e5de;
  --color-tpt03-line: oklch(0.915 0.01 120);
  --color-tpt03-acc: #1f9a5b;
  --color-tpt03-acc: oklch(0.6 0.15 155);
  --color-tpt03-acc-ink: #127140;
  --color-tpt03-acc-ink: oklch(0.47 0.12 155);
  --font-tpt03-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpt03-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-03 {
  width: 100%;
  min-height: 100svh;
}
```
