---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-product-cards/tailwind-subscription-pricing-card-billing-switch/"
title: "Tailwind Subscription Pricing Card with Billing Switch"
section: "components"
category: "tailwind-css-product-cards"
category_name: "Tailwind CSS Product Cards"
description: "The featured pricing tier: a 'Most Popular' banner, an accent border, a lifted card and a ticked feature list — plus the monthly/annual switch the CSS…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Subscription Pricing Card with Billing Switch
Source: https://codefronts.com/components/tailwind-css-product-cards/tailwind-subscription-pricing-card-billing-switch/

The featured pricing tier: a 'Most Popular' banner, an accent border, a lifted card and a ticked feature list — plus the monthly/annual switch the CSS original left as a suggestion. Two sr-only radios drive it through group-has-[#tpc18-yr:checked]:, so both prices and the segmented control's own state are pure CSS.
## HTML
```html
<section class="tpc-18 w-full min-h-svh grid place-items-center bg-tpc18-bg font-tpc18-sans px-5 py-12" aria-label="Subscription pricing card demo">
  <article class="group/bill relative w-[min(340px,100%)] px-7 pt-8 pb-7 rounded-[20px] bg-tpc18-card border-2 border-tpc18-acc -translate-y-1.5 shadow-[0_30px_60px_-28px_color-mix(in_oklch,var(--color-tpc18-acc)_55%,transparent)]">
    <span class="absolute -top-3.25 left-7 px-3.5 py-1.5 rounded-full bg-tpc18-acc text-tpc18-onacc text-[11px] font-bold tracking-[0.06em] uppercase shadow-[0_8px_18px_-8px_var(--color-tpc18-acc)]">Most Popular</span>

    <input type="radio" name="tpc18-bill" id="tpc18-mo" class="sr-only" checked>
    <input type="radio" name="tpc18-bill" id="tpc18-yr" class="sr-only">

    <p class="text-[12px] font-medium tracking-[0.2em] uppercase text-tpc18-acc">Pro</p>

    <div role="group" aria-label="Billing interval" class="mt-3.5 inline-flex p-1 rounded-full bg-tpc18-seg">
      <label for="tpc18-mo" class="grid place-items-center min-h-11 px-4.5 rounded-full cursor-pointer text-[13px] font-semibold text-tpc18-mut transition-colors duration-200 group-has-[#tpc18-mo:checked]/bill:bg-tpc18-card group-has-[#tpc18-mo:checked]/bill:text-tpc18-ink group-has-[#tpc18-mo:checked]/bill:shadow-[0_2px_8px_-3px_oklch(0.2_0.04_290/0.3)] motion-reduce:transition-none">Monthly</label>
      <label for="tpc18-yr" class="grid place-items-center min-h-11 px-4.5 rounded-full cursor-pointer text-[13px] font-semibold text-tpc18-mut transition-colors duration-200 group-has-[#tpc18-yr:checked]/bill:bg-tpc18-card group-has-[#tpc18-yr:checked]/bill:text-tpc18-ink group-has-[#tpc18-yr:checked]/bill:shadow-[0_2px_8px_-3px_oklch(0.2_0.04_290/0.3)] motion-reduce:transition-none">Annual</label>
    </div>

    <p class="mt-4 flex items-baseline gap-1">
      <span class="text-[52px] font-bold leading-none tracking-[-0.02em] text-tpc18-ink tabular-nums group-has-[#tpc18-yr:checked]/bill:hidden">$24</span>
      <span class="hidden text-[52px] font-bold leading-none tracking-[-0.02em] text-tpc18-ink tabular-nums group-has-[#tpc18-yr:checked]/bill:inline">$19</span>
      <span class="text-[17px] font-semibold text-tpc18-mut">/mo</span>
    </p>
    <p class="mt-2 text-[13px] text-tpc18-mut">
      <span class="group-has-[#tpc18-yr:checked]/bill:hidden">billed monthly &middot; cancel anytime</span>
      <span class="hidden group-has-[#tpc18-yr:checked]/bill:inline">billed annually &middot; save 20%</span>
    </p>

    <ul class="mt-5.5 mb-6 flex flex-col gap-3 list-none">
      <li class="relative pl-7.5 text-[14.5px] leading-[1.4] text-tpc18-body before:content-['&#10003;'] before:absolute before:left-0 before:top-0 before:size-5 before:rounded-full before:grid before:place-items-center before:text-[12px] before:font-extrabold before:text-tpc18-onacc before:bg-tpc18-acc">Unlimited projects</li>
      <li class="relative pl-7.5 text-[14.5px] leading-[1.4] text-tpc18-body before:content-['&#10003;'] before:absolute before:left-0 before:top-0 before:size-5 before:rounded-full before:grid before:place-items-center before:text-[12px] before:font-extrabold before:text-tpc18-onacc before:bg-tpc18-acc">Advanced analytics</li>
      <li class="relative pl-7.5 text-[14.5px] leading-[1.4] text-tpc18-body before:content-['&#10003;'] before:absolute before:left-0 before:top-0 before:size-5 before:rounded-full before:grid before:place-items-center before:text-[12px] before:font-extrabold before:text-tpc18-onacc before:bg-tpc18-acc">Priority support</li>
      <li class="relative pl-7.5 text-[14.5px] leading-[1.4] text-tpc18-body before:content-['&#10003;'] before:absolute before:left-0 before:top-0 before:size-5 before:rounded-full before:grid before:place-items-center before:text-[12px] before:font-extrabold before:text-tpc18-onacc before:bg-tpc18-acc">Team roles &amp; permissions</li>
      <li class="relative pl-7.5 text-[14.5px] leading-[1.4] text-tpc18-body before:content-['&#10003;'] before:absolute before:left-0 before:top-0 before:size-5 before:rounded-full before:grid before:place-items-center before:text-[12px] before:font-extrabold before:text-tpc18-onacc before:bg-tpc18-acc">API access</li>
    </ul>

    <div class="mb-4.5 flex items-center gap-3">
      <ul class="flex list-none pl-0" aria-hidden="true">
        <li class="size-8 rounded-full bg-tpc18-seg bg-[url('https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop&q=70')] bg-cover bg-center shadow-[0_0_0_2px_var(--color-tpc18-card)]"></li>
        <li class="-ml-2.5 size-8 rounded-full bg-tpc18-seg bg-[url('https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&h=120&fit=crop&q=70')] bg-cover bg-center shadow-[0_0_0_2px_var(--color-tpc18-card)]"></li>
        <li class="-ml-2.5 size-8 rounded-full bg-tpc18-seg bg-[url('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&q=70')] bg-cover bg-center shadow-[0_0_0_2px_var(--color-tpc18-card)]"></li>
      </ul>
      <p class="text-[12.5px] leading-[1.35] text-tpc18-mut">Trusted by <b class="font-semibold text-tpc18-body tabular-nums">2,400+</b> product teams</p>
    </div>
    <button type="button" class="w-full min-h-11 h-12.5 rounded-[13px] border-0 cursor-pointer bg-tpc18-acc text-tpc18-onacc text-[15px] font-bold shadow-[0_12px_26px_-12px_var(--color-tpc18-acc)] transition-colors duration-150 hover:bg-tpc18-acc2 focus-visible:outline-3 focus-visible:outline-tpc18-ring focus-visible:outline-offset-2 motion-reduce:transition-none">Start free trial</button>
    <p class="mt-3 text-center text-[12px] text-tpc18-mut">14-day trial &middot; no card required</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpc18-bg: #f1f0f7;
  --color-tpc18-bg: oklch(0.95 0.008 290);
  --color-tpc18-card: #ffffff;
  --color-tpc18-card: oklch(1 0 0);
  --color-tpc18-ink: #1a1430;
  --color-tpc18-ink: oklch(0.23 0.04 295);
  --color-tpc18-body: #3a3355;
  --color-tpc18-body: oklch(0.36 0.04 295);
  --color-tpc18-mut: #5f5880;
  --color-tpc18-mut: oklch(0.48 0.04 295);
  --color-tpc18-seg: #efedf7;
  --color-tpc18-seg: oklch(0.95 0.012 295);
  --color-tpc18-acc: #5b3fc4;
  --color-tpc18-acc: oklch(0.48 0.19 292);
  --color-tpc18-acc2: #4c34a6;
  --color-tpc18-acc2: oklch(0.42 0.18 292);
  --color-tpc18-ring: #bda6f0;
  --color-tpc18-ring: oklch(0.78 0.11 292);
  --color-tpc18-onacc: #ffffff;
  --color-tpc18-onacc: oklch(1 0 0);
  --font-tpc18-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tpc-18 {
  width: 100%;
  min-height: 100svh;
}

.tpc-18 ::selection {
  background: var(--color-tpc18-acc);
  color: #fff;
}
```
