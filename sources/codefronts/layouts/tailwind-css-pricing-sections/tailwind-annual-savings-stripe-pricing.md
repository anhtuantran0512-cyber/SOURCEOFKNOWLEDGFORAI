---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-annual-savings-stripe-pricing/"
title: "Tailwind Annual Savings Stripe Pricing"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "The anchor-and-discount pattern, stated plainly: the monthly price struck through in orange, the yearly-equivalent price beneath it, and a \"Save $84/yr\" tab…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Annual Savings Stripe Pricing
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-annual-savings-stripe-pricing/

The anchor-and-discount pattern, stated plainly: the monthly price struck through in orange, the yearly-equivalent price beneath it, and a "Save $84/yr" tab under both. The port's small pleasure is line-through decoration-tps21-orange decoration-2 &mdash; the struck price's whole treatment in three utilities, where CSS needs three separate text-decoration-* declarations.
## HTML
```html
<section class="tps-21 w-full min-h-svh bg-tps21-bg bg-[radial-gradient(60%_60%_at_50%_0%,--alpha(--color-tps21-green-dark/20),transparent_60%)] font-tps21-sans text-tps21-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <h2 class="m-0 mb-2 text-[clamp(24px,3.6vw,36px)] font-bold tracking-[-0.02em] text-white">Pay yearly, save real money.</h2>
    <p class="m-0 text-sm text-tps21-muted">Same product, two months free when you commit to a year.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-4 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps21-card border border-tps21-green/22">
      <h3 class="m-0 mb-3.5 text-sm font-bold uppercase tracking-[0.1em] text-tps21-mint">Seedling</h3>
      <div class="flex flex-col gap-1 mb-2">
        <span class="text-sm text-tps21-muted line-through decoration-tps21-orange decoration-2" aria-label="Monthly price, was">$15<em class="not-italic text-xs opacity-80">/mo</em></span>
        <span class="flex items-baseline gap-1.5"><strong class="text-[38px] font-extrabold tracking-[-0.03em] text-white">$12</strong><em class="not-italic text-xs text-tps21-muted">/mo billed yearly</em></span>
      </div>
      <span class="self-start mb-[18px] px-2.5 py-0.75 rounded-[4px] bg-tps21-orange text-tps21-bg text-[11px] font-bold tracking-[0.04em]" aria-label="Yearly savings">Save $36/yr</span>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps21-list">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">1 garden</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">30 plant slots</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Care reminders</li>
      </ul>
      <a href="#seedling" class="block text-center px-4 py-2.75 rounded-[8px] bg-tps21-green/14 text-tps21-mint border border-tps21-green/32 text-[13.5px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps21-green hover:text-tps21-bg focus-visible:outline-2 focus-visible:outline-tps21-green focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Seedling</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-linear-180 from-tps21-card-hi to-tps21-card border border-tps21-green md:scale-[1.04] shadow-[inset_0_0_0_1px_--theme(--color-tps21-green),0_14px_36px_--alpha(--color-tps21-green/20)]">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-2.75 py-1 rounded-full bg-tps21-green text-tps21-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Recommended</span>
      <h3 class="m-0 mb-3.5 text-sm font-bold uppercase tracking-[0.1em] text-tps21-mint">Greenhouse</h3>
      <div class="flex flex-col gap-1 mb-2">
        <span class="text-sm text-tps21-muted line-through decoration-tps21-orange decoration-2" aria-label="Monthly price, was">$36<em class="not-italic text-xs opacity-80">/mo</em></span>
        <span class="flex items-baseline gap-1.5"><strong class="text-[38px] font-extrabold tracking-[-0.03em] text-white">$29</strong><em class="not-italic text-xs text-tps21-muted">/mo billed yearly</em></span>
      </div>
      <span class="self-start mb-[18px] px-2.5 py-0.75 rounded-[4px] bg-tps21-orange text-tps21-bg text-[11px] font-bold tracking-[0.04em]" aria-label="Yearly savings">Save $84/yr</span>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps21-list">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">10 gardens</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Unlimited slots</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Disease alerts</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Soil data sync</li>
      </ul>
      <a href="#greenhouse" class="block text-center px-4 py-2.75 rounded-[8px] bg-tps21-green text-tps21-bg border border-tps21-green text-[13.5px] font-semibold no-underline transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps21-green focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Greenhouse</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps21-card border border-tps21-green/22">
      <h3 class="m-0 mb-3.5 text-sm font-bold uppercase tracking-[0.1em] text-tps21-mint">Estate</h3>
      <div class="flex flex-col gap-1 mb-2">
        <span class="text-sm text-tps21-muted line-through decoration-tps21-orange decoration-2" aria-label="Monthly price, was">$96<em class="not-italic text-xs opacity-80">/mo</em></span>
        <span class="flex items-baseline gap-1.5"><strong class="text-[38px] font-extrabold tracking-[-0.03em] text-white">$79</strong><em class="not-italic text-xs text-tps21-muted">/mo billed yearly</em></span>
      </div>
      <span class="self-start mb-[18px] px-2.5 py-0.75 rounded-[4px] bg-tps21-orange text-tps21-bg text-[11px] font-bold tracking-[0.04em]" aria-label="Yearly savings">Save $204/yr</span>
      <ul class="list-none p-0 m-0 mb-5 flex-1 text-[13.5px]/[1.95] text-tps21-list">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Multi-property</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Pro APIs</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps21-emerald">Phone support</li>
      </ul>
      <a href="#estate" class="block text-center px-4 py-2.75 rounded-[8px] bg-tps21-green/14 text-tps21-mint border border-tps21-green/32 text-[13.5px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps21-green hover:text-tps21-bg focus-visible:outline-2 focus-visible:outline-tps21-green focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Estate</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps21-bg: #07140e;
  --color-tps21-bg: oklch(0.17 0.03 160);
  --color-tps21-card: #0d2018;
  --color-tps21-card: oklch(0.23 0.04 160);
  --color-tps21-card-hi: #14301f;
  --color-tps21-card-hi: oklch(0.28 0.06 152);
  --color-tps21-body: #e7f5ee;
  --color-tps21-body: oklch(0.95 0.02 160);
  --color-tps21-list: #c8e0d3;
  --color-tps21-list: oklch(0.87 0.03 158);
  --color-tps21-muted: #94b5a3;
  --color-tps21-muted: oklch(0.73 0.04 158);
  --color-tps21-mint: #6ee7b7;
  --color-tps21-mint: oklch(0.86 0.14 165);
  --color-tps21-emerald: #34d399;
  --color-tps21-emerald: oklch(0.78 0.15 163);
  --color-tps21-green: #34996c;
  --color-tps21-green: oklch(0.6 0.11 158);
  --color-tps21-green-dark: #226b48;
  --color-tps21-green-dark: oklch(0.46 0.1 158);
  --color-tps21-orange: #f97316;
  --color-tps21-orange: oklch(0.7 0.19 45);
  --font-tps21-sans: 'Sora', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-21 {
  width: 100%;
  min-height: 100svh;
}
```
