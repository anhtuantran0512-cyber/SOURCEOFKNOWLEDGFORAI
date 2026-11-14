---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-monthly-yearly-billing-toggle-pricing/"
title: "Tailwind Monthly Yearly Billing Toggle Pricing"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "A zero-JS billing switch: two hidden radios, a sliding gradient thumb and every price in the section swapping at once."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Monthly Yearly Billing Toggle Pricing
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-monthly-yearly-billing-toggle-pricing/

A zero-JS billing switch: two hidden radios, a sliding gradient thumb and every price in the section swapping at once. The CSS version needs four :has() blocks written far from the elements; the Tailwind version needs peer-checked/y: for the switch's own chrome and one group-has-[#tps04-y:checked]: pair on each price &mdash; and the swap rule now sits on the numbers that swap.
## HTML
```html
<section class="tps-04 group w-full min-h-svh bg-tps04-bg font-tps04-sans text-tps04-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,40px)]">
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,34px)] font-bold tracking-[-0.02em] text-transparent bg-linear-to-r from-tps04-acc to-tps04-acc2 bg-clip-text forced-colors:text-[CanvasText] text-pretty">Pay how it suits you.</h2>
    <p class="m-0 mb-5.5 text-sm text-tps04-mut">Switch billing &mdash; no contracts, no negotiation.</p>
    <fieldset class="relative inline-grid grid-cols-2 gap-0 m-0 p-1 rounded-full bg-tps04-card border border-tps04-edge">
      <legend class="sr-only">Billing cycle</legend>
      <input type="radio" name="tps04-cycle" id="tps04-m" class="peer/m sr-only" checked>
      <label for="tps04-m" class="relative z-1 inline-flex items-center justify-center gap-1.5 px-5.5 py-2 rounded-full text-[13px] font-semibold text-tps04-mut whitespace-nowrap cursor-pointer transition-colors duration-200 peer-checked/m:text-tps04-bg peer-focus-visible/m:outline-2 peer-focus-visible/m:outline-tps04-acc2 peer-focus-visible/m:outline-offset-3 motion-reduce:transition-none">Monthly</label>
      <input type="radio" name="tps04-cycle" id="tps04-y" class="peer/y sr-only">
      <label for="tps04-y" class="relative z-1 inline-flex items-center justify-center gap-1.5 px-5.5 py-2 rounded-full text-[13px] font-semibold text-tps04-mut whitespace-nowrap cursor-pointer transition-colors duration-200 peer-checked/y:text-tps04-bg peer-focus-visible/y:outline-2 peer-focus-visible/y:outline-tps04-acc2 peer-focus-visible/y:outline-offset-3 motion-reduce:transition-none">Yearly <span class="px-1.5 py-0.5 rounded-md bg-tps04-chip text-tps04-acc2 text-[10px] font-bold group-has-[#tps04-y:checked]:bg-tps04-badgeon group-has-[#tps04-y:checked]:text-tps04-bg">&minus;20%</span></label>
      <span class="absolute top-1 left-1 z-0 w-[calc(50%-4px)] h-[calc(100%-8px)] rounded-full bg-linear-[135deg,var(--color-tps04-acc),var(--color-tps04-acc2)] shadow-[0_4px_14px_--theme(--color-tps04-glow)] transition-transform duration-300 ease-tps04 peer-checked/y:translate-x-full motion-reduce:transition-none" aria-hidden="true"></span>
    </fieldset>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] gap-4 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative flex flex-col p-5.5 pt-6 rounded-2xl bg-tps04-card border border-tps04-edge">
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps04-acc2">Hobby</h3>
      <div class="flex items-baseline gap-2 mb-4.5">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:hidden">$0</span><span class="hidden text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:inline">$0</span><span class="text-[13px] text-tps04-mut">forever</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[2] text-tps04-body">
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>1 site</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Public projects</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Community</li>
      </ul>
      <a href="#hobby" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline bg-tps04-chip text-tps04-acc2 border border-tps04-ctaedge transition-[background-color,color] duration-200 hover:bg-tps04-acc2 hover:text-tps04-bg focus-visible:outline-2 focus-visible:outline-tps04-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Start free</a>
    </article>
    <article class="relative flex flex-col p-5.5 pt-6 rounded-2xl bg-tps04-card border border-tps04-acc2 shadow-[inset_0_0_0_1px_--theme(--color-tps04-acc2)]">
      <span class="absolute -top-2.5 right-4 px-2.5 py-1 rounded-md bg-tps04-acc2 text-tps04-bg text-[10px] font-bold uppercase tracking-[0.08em]">Best value</span>
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps04-acc2">Studio</h3>
      <div class="flex items-baseline gap-2 mb-4.5">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:hidden">$19</span><span class="hidden text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:inline">$15</span><span class="text-[13px] text-tps04-mut">/ month</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[2] text-tps04-body">
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Unlimited sites</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Custom domains</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Email support</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Form submissions</li>
      </ul>
      <a href="#studio" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline bg-tps04-acc2 text-tps04-bg border border-tps04-acc2 transition-[background-color,color] duration-200 hover:bg-tps04-acc hover:text-tps04-bg focus-visible:outline-2 focus-visible:outline-tps04-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Start trial</a>
    </article>
    <article class="relative flex flex-col p-5.5 pt-6 rounded-2xl bg-tps04-card border border-tps04-edge">
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps04-acc2">Agency</h3>
      <div class="flex items-baseline gap-2 mb-4.5">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:hidden">$59</span><span class="hidden text-[38px] font-extrabold tracking-[-0.02em] text-tps04-price group-has-[#tps04-y:checked]:inline">$47</span><span class="text-[13px] text-tps04-mut">/ month</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[2] text-tps04-body">
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Everything in Studio</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Client billing</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Workspace switcher</li>
        <li><span class="inline-block w-5 font-bold text-tps04-acc2" aria-hidden="true">&#10003;</span>Priority support</li>
      </ul>
      <a href="#agency" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline bg-tps04-chip text-tps04-acc2 border border-tps04-ctaedge transition-[background-color,color] duration-200 hover:bg-tps04-acc2 hover:text-tps04-bg focus-visible:outline-2 focus-visible:outline-tps04-acc2 focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Agency</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps04-bg: #062021;
  --color-tps04-bg: oklch(0.2 0.03 190);
  --color-tps04-card: #0d2f30;
  --color-tps04-card: oklch(0.27 0.035 190);
  --color-tps04-edge: #1d4a4b;
  --color-tps04-edge: oklch(0.38 0.04 190);
  --color-tps04-ctaedge: #2a6a68;
  --color-tps04-ctaedge: oklch(0.48 0.06 185);
  --color-tps04-chip: #10403f;
  --color-tps04-chip: oklch(0.33 0.05 187);
  --color-tps04-badgeon: #a7f3e4;
  --color-tps04-badgeon: oklch(0.92 0.08 175);
  --color-tps04-ink: #e0fafa;
  --color-tps04-ink: oklch(0.96 0.02 190);
  --color-tps04-body: #c8eaea;
  --color-tps04-body: oklch(0.91 0.03 190);
  --color-tps04-price: #f0fff7;
  --color-tps04-price: oklch(0.98 0.02 170);
  --color-tps04-mut: #7ea7a4;
  --color-tps04-mut: oklch(0.7 0.04 185);
  --color-tps04-acc: #14b8a6;
  --color-tps04-acc: oklch(0.7 0.13 180);
  --color-tps04-acc2: #5eead4;
  --color-tps04-acc2: oklch(0.87 0.12 175);
  --color-tps04-glow: #14b8a64d;
  --color-tps04-glow: oklch(0.7 0.13 180 / 0.3);
  --font-tps04-sans: 'Inter', system-ui, sans-serif;
  --ease-tps04: cubic-bezier(0.4, 0, 0.2, 1);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-04 {
  width: 100%;
  min-height: 100svh;
}
```
