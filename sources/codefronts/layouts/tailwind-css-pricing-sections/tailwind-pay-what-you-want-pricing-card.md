---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-pay-what-you-want-pricing-card/"
title: "Tailwind Pay What You Want Pricing Card"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Five preset amount chips, the selected one lifting into a mint gradient, and a CTA whose label changes with the choice &mdash; all from five radios and no…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pay What You Want Pricing Card
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-pay-what-you-want-pricing-card/

Five preset amount chips, the selected one lifting into a mint gradient, and a CTA whose label changes with the choice &mdash; all from five radios and no JavaScript. The port replaces eight :has() rules at the bottom of the stylesheet with group-has-[#tps-16-5:checked]: variants sitting on the spans they actually control.
## HTML
```html
<section class="tps-16 group w-full min-h-svh flex items-center justify-center bg-tps16-bg bg-[radial-gradient(50%_50%_at_50%_0%,--alpha(--color-tps16-mint/16),transparent_60%)] font-tps16-sans text-tps16-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pay what you want">
  <div class="w-full max-w-[560px] p-[clamp(26px,4vw,38px)] rounded-[18px] bg-linear-180 from-tps16-card to-tps16-bg border border-tps16-mint/30 shadow-[0_24px_60px_--alpha(--color-tps16-mint/12)]">
    <header class="text-center mb-6">
      <span class="inline-block mb-3.5 px-3 py-1 rounded-full bg-tps16-aqua/12 text-[11px] font-bold uppercase tracking-[0.16em] text-tps16-aqua">Pay what you want</span>
      <h2 class="m-0 mb-2.5 text-[clamp(22px,3.6vw,30px)] font-bold tracking-[-0.02em] text-white">Support the project &mdash; <em class="italic text-tps16-aqua">name your price.</em></h2>
      <p class="m-0 mx-auto max-w-[420px] text-sm/[1.6] text-tps16-muted">The full product is yours regardless of the amount. Pay more if it helps, pay less if it&rsquo;s tight. We trust you.</p>
    </header>
    <fieldset class="border-0 p-0 m-0 mb-5 grid grid-cols-3 sm:grid-cols-5 gap-2">
      <legend class="sr-only">Choose an amount</legend>
      <input type="radio" name="tps-16" id="tps-16-5" class="peer/a5 sr-only">
      <label for="tps-16-5" class="flex flex-col items-center justify-center text-center min-h-16 px-1.5 py-3.5 rounded-[10px] bg-tps16-aqua/6 border-[1.5px] border-tps16-aqua/18 cursor-pointer transition-[border-color,background-color,translate] duration-[180ms] hover:border-tps16-aqua/50 hover:bg-tps16-aqua/10 peer-checked/a5:bg-linear-135 peer-checked/a5:from-tps16-mint peer-checked/a5:to-tps16-aqua peer-checked/a5:border-tps16-aqua peer-checked/a5:-translate-y-0.5 peer-checked/a5:shadow-[0_6px_18px_--alpha(--color-tps16-mint/40)] peer-checked/a5:[&amp;_strong]:text-tps16-bg peer-checked/a5:[&amp;_span]:text-tps16-bg/70 peer-focus-visible/a5:outline-2 peer-focus-visible/a5:outline-tps16-aqua peer-focus-visible/a5:outline-offset-[3px] motion-reduce:transition-none motion-reduce:peer-checked/a5:translate-y-0"><strong class="text-base font-extrabold tracking-[-0.01em] text-white">$5</strong><span class="block mt-0.5 text-[10.5px] font-semibold uppercase tracking-[0.06em] text-tps16-aqua">Coffee</span></label>
      <input type="radio" name="tps-16" id="tps-16-10" class="peer/a10 sr-only" checked>
      <label for="tps-16-10" class="flex flex-col items-center justify-center text-center min-h-16 px-1.5 py-3.5 rounded-[10px] bg-tps16-aqua/6 border-[1.5px] border-tps16-aqua/18 cursor-pointer transition-[border-color,background-color,translate] duration-[180ms] hover:border-tps16-aqua/50 hover:bg-tps16-aqua/10 peer-checked/a10:bg-linear-135 peer-checked/a10:from-tps16-mint peer-checked/a10:to-tps16-aqua peer-checked/a10:border-tps16-aqua peer-checked/a10:-translate-y-0.5 peer-checked/a10:shadow-[0_6px_18px_--alpha(--color-tps16-mint/40)] peer-checked/a10:[&amp;_strong]:text-tps16-bg peer-checked/a10:[&amp;_span]:text-tps16-bg/70 peer-focus-visible/a10:outline-2 peer-focus-visible/a10:outline-tps16-aqua peer-focus-visible/a10:outline-offset-[3px] motion-reduce:transition-none motion-reduce:peer-checked/a10:translate-y-0"><strong class="text-base font-extrabold tracking-[-0.01em] text-white">$10</strong><span class="block mt-0.5 text-[10.5px] font-semibold uppercase tracking-[0.06em] text-tps16-aqua">Average</span></label>
      <input type="radio" name="tps-16" id="tps-16-25" class="peer/a25 sr-only">
      <label for="tps-16-25" class="flex flex-col items-center justify-center text-center min-h-16 px-1.5 py-3.5 rounded-[10px] bg-tps16-aqua/6 border-[1.5px] border-tps16-aqua/18 cursor-pointer transition-[border-color,background-color,translate] duration-[180ms] hover:border-tps16-aqua/50 hover:bg-tps16-aqua/10 peer-checked/a25:bg-linear-135 peer-checked/a25:from-tps16-mint peer-checked/a25:to-tps16-aqua peer-checked/a25:border-tps16-aqua peer-checked/a25:-translate-y-0.5 peer-checked/a25:shadow-[0_6px_18px_--alpha(--color-tps16-mint/40)] peer-checked/a25:[&amp;_strong]:text-tps16-bg peer-checked/a25:[&amp;_span]:text-tps16-bg/70 peer-focus-visible/a25:outline-2 peer-focus-visible/a25:outline-tps16-aqua peer-focus-visible/a25:outline-offset-[3px] motion-reduce:transition-none motion-reduce:peer-checked/a25:translate-y-0"><strong class="text-base font-extrabold tracking-[-0.01em] text-white">$25</strong><span class="block mt-0.5 text-[10.5px] font-semibold uppercase tracking-[0.06em] text-tps16-aqua">Generous</span></label>
      <input type="radio" name="tps-16" id="tps-16-50" class="peer/a50 sr-only">
      <label for="tps-16-50" class="flex flex-col items-center justify-center text-center min-h-16 px-1.5 py-3.5 rounded-[10px] bg-tps16-aqua/6 border-[1.5px] border-tps16-aqua/18 cursor-pointer transition-[border-color,background-color,translate] duration-[180ms] hover:border-tps16-aqua/50 hover:bg-tps16-aqua/10 peer-checked/a50:bg-linear-135 peer-checked/a50:from-tps16-mint peer-checked/a50:to-tps16-aqua peer-checked/a50:border-tps16-aqua peer-checked/a50:-translate-y-0.5 peer-checked/a50:shadow-[0_6px_18px_--alpha(--color-tps16-mint/40)] peer-checked/a50:[&amp;_strong]:text-tps16-bg peer-checked/a50:[&amp;_span]:text-tps16-bg/70 peer-focus-visible/a50:outline-2 peer-focus-visible/a50:outline-tps16-aqua peer-focus-visible/a50:outline-offset-[3px] motion-reduce:transition-none motion-reduce:peer-checked/a50:translate-y-0"><strong class="text-base font-extrabold tracking-[-0.01em] text-white">$50</strong><span class="block mt-0.5 text-[10.5px] font-semibold uppercase tracking-[0.06em] text-tps16-aqua">Sponsor</span></label>
      <input type="radio" name="tps-16" id="tps-16-x" class="peer/ax sr-only">
      <label for="tps-16-x" class="flex flex-col items-center justify-center text-center min-h-16 px-1.5 py-3.5 rounded-[10px] bg-tps16-aqua/6 border-[1.5px] border-tps16-aqua/18 cursor-pointer transition-[border-color,background-color,translate] duration-[180ms] hover:border-tps16-aqua/50 hover:bg-tps16-aqua/10 peer-checked/ax:bg-linear-135 peer-checked/ax:from-tps16-mint peer-checked/ax:to-tps16-aqua peer-checked/ax:border-tps16-aqua peer-checked/ax:-translate-y-0.5 peer-checked/ax:shadow-[0_6px_18px_--alpha(--color-tps16-mint/40)] peer-checked/ax:[&amp;_strong]:text-tps16-bg peer-checked/ax:[&amp;_span]:text-tps16-bg/70 peer-focus-visible/ax:outline-2 peer-focus-visible/ax:outline-tps16-aqua peer-focus-visible/ax:outline-offset-[3px] motion-reduce:transition-none motion-reduce:peer-checked/ax:translate-y-0"><strong class="text-base font-extrabold tracking-[-0.01em] text-white">Custom</strong><span class="block mt-0.5 text-[10.5px] font-semibold uppercase tracking-[0.06em] text-tps16-aqua">You decide</span></label>
    </fieldset>
    <ul class="list-none p-0 m-0 mb-5 text-[13px]/[1.95] text-tps16-list">
      <li class="before:content-['\2713'] before:inline-block before:w-[22px] before:font-bold before:text-tps16-aqua">Lifetime access to the full product</li>
      <li class="before:content-['\2713'] before:inline-block before:w-[22px] before:font-bold before:text-tps16-aqua">All future updates included</li>
      <li class="before:content-['\2713'] before:inline-block before:w-[22px] before:font-bold before:text-tps16-aqua">Source files + commercial use rights</li>
    </ul>
    <a href="#pay" class="block text-center mb-3 px-4.5 py-3.5 rounded-[10px] bg-linear-135 from-tps16-mint to-tps16-aqua text-tps16-bg no-underline text-sm font-bold tracking-[0.01em] shadow-[0_10px_24px_--alpha(--color-tps16-mint/30)] transition-[translate] duration-[180ms] hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-tps16-aqua focus-visible:outline-offset-[3px] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="block group-has-[#tps-16-5:checked]:hidden group-has-[#tps-16-25:checked]:hidden group-has-[#tps-16-50:checked]:hidden group-has-[#tps-16-x:checked]:hidden">Pay $10 &mdash; get it now</span>
      <span class="hidden group-has-[#tps-16-5:checked]:block">Pay $5 &mdash; get it now</span>
      <span class="hidden group-has-[#tps-16-25:checked]:block">Pay $25 &mdash; get it now</span>
      <span class="hidden group-has-[#tps-16-50:checked]:block">Pay $50 &mdash; get it now</span>
      <span class="hidden group-has-[#tps-16-x:checked]:block">Enter custom amount &rarr;</span>
    </a>
    <p class="m-0 text-center text-[11.5px] text-tps16-fine">No questions asked refund inside 14 days. Powered by Stripe.</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps16-bg: #06181a;
  --color-tps16-bg: oklch(0.2 0.03 192);
  --color-tps16-card: #0d2326;
  --color-tps16-card: oklch(0.26 0.03 195);
  --color-tps16-body: #d4f5ee;
  --color-tps16-body: oklch(0.94 0.04 175);
  --color-tps16-list: #b8d6cf;
  --color-tps16-list: oklch(0.84 0.03 175);
  --color-tps16-muted: #92b8b1;
  --color-tps16-muted: oklch(0.74 0.03 175);
  --color-tps16-fine: #87a5a0;
  --color-tps16-fine: oklch(0.67 0.02 178);
  --color-tps16-mint: #2dd4bf;
  --color-tps16-mint: oklch(0.78 0.13 182);
  --color-tps16-aqua: #5eead4;
  --color-tps16-aqua: oklch(0.85 0.12 178);
  --font-tps16-sans: 'Be Vietnam Pro', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-16 {
  width: 100%;
  min-height: 100svh;
}
```
