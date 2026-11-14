---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-tabbed-pricing-table-multiple-products/"
title: "Tailwind Tabbed Pricing Table for Multiple Products"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "For product suites too broad for one grid: Marketing, Sales and Support tabs cross-fade whole pricing panels beneath a sliding pill indicator."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabbed Pricing Table for Multiple Products
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-tabbed-pricing-table-multiple-products/

For product suites too broad for one grid: Marketing, Sales and Support tabs cross-fade whole pricing panels beneath a sliding pill indicator. The indicator moves by its own width — translate-x-full, translate-x-[200%] — so it's correct at any tab width with no breakpoint maths, and the tab bar is an honest radio group that arrow keys drive natively.
## HTML
```html
<section class="tpt-12 group/p w-full min-h-svh grid place-items-center bg-tpt12-bg px-5 py-16 font-tpt12-sans text-tpt12-ink antialiased" aria-label="Pricing by product suite">
  <div class="grid w-full max-w-5xl justify-items-center gap-8">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">One platform, three suites</h2>
    <fieldset class="relative grid w-full max-w-md grid-cols-3 rounded-full bg-tpt12-track p-1 has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tpt12-acc">
      <legend class="sr-only">Product suite</legend>
      <span aria-hidden="true" class="absolute inset-y-1 left-1 w-[calc((100%-8px)/3)] rounded-full bg-white shadow-[0_3px_10px_oklch(0.2_0.03_265/0.14)] transition-transform duration-350 ease-[cubic-bezier(.55,0,.2,1.2)] group-has-[#tpt12-t2:checked]/p:translate-x-full group-has-[#tpt12-t3:checked]/p:translate-x-[200%] motion-reduce:transition-none"></span>
      <label class="relative grid min-h-11 cursor-pointer place-items-center rounded-full text-sm font-bold text-tpt12-mut transition-colors has-checked:text-tpt12-ink"><input type="radio" name="tpt12-tab" id="tpt12-t1" class="sr-only" checked>Marketing</label>
      <label class="relative grid min-h-11 cursor-pointer place-items-center rounded-full text-sm font-bold text-tpt12-mut transition-colors has-checked:text-tpt12-ink"><input type="radio" name="tpt12-tab" id="tpt12-t2" class="sr-only">Sales</label>
      <label class="relative grid min-h-11 cursor-pointer place-items-center rounded-full text-sm font-bold text-tpt12-mut transition-colors has-checked:text-tpt12-ink"><input type="radio" name="tpt12-tab" id="tpt12-t3" class="sr-only">Support</label>
    </fieldset>
    <div class="grid w-full">
      <div class="col-start-1 row-start-1 grid gap-4 transition duration-350 sm:grid-cols-3 invisible translate-y-2.5 opacity-0 group-has-[#tpt12-t1:checked]/p:visible group-has-[#tpt12-t1:checked]/p:translate-y-0 group-has-[#tpt12-t1:checked]/p:opacity-100 group-has-[#tpt12-t1:checked]/p:delay-100 motion-reduce:transition-none" aria-label="Marketing suite plans" role="group">
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">Email</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$15<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/mo</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>10k sends / month</li><li>Template library</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Email</a></article>
        <article class="flex flex-col gap-2 rounded-2xl bg-white p-6 ring-2 ring-tpt12-acc"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-acc uppercase">Omni</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$45<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/mo</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Email + SMS + push</li><li>Customer journeys</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt12-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt12-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Omni</a></article>
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">ABM</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$120<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/mo</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Account targeting</li><li>Intent data</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose ABM</a></article>
      </div>
      <div class="col-start-1 row-start-1 grid gap-4 transition duration-350 sm:grid-cols-3 invisible translate-y-2.5 opacity-0 group-has-[#tpt12-t2:checked]/p:visible group-has-[#tpt12-t2:checked]/p:translate-y-0 group-has-[#tpt12-t2:checked]/p:opacity-100 group-has-[#tpt12-t2:checked]/p:delay-100 motion-reduce:transition-none" aria-label="Sales suite plans" role="group">
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">CRM</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$20<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/seat</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Visual pipeline</li><li>Email sync</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose CRM</a></article>
        <article class="flex flex-col gap-2 rounded-2xl bg-white p-6 ring-2 ring-tpt12-acc"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-acc uppercase">Engage</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$55<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/seat</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Sequences &amp; dialer</li><li>Forecasting</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt12-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt12-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Engage</a></article>
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">Revenue</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$140<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/seat</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Deal intelligence</li><li>Quota planning</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Revenue</a></article>
      </div>
      <div class="col-start-1 row-start-1 grid gap-4 transition duration-350 sm:grid-cols-3 invisible translate-y-2.5 opacity-0 group-has-[#tpt12-t3:checked]/p:visible group-has-[#tpt12-t3:checked]/p:translate-y-0 group-has-[#tpt12-t3:checked]/p:opacity-100 group-has-[#tpt12-t3:checked]/p:delay-100 motion-reduce:transition-none" aria-label="Support suite plans" role="group">
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">Inbox</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$12<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/seat</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Shared inbox</li><li>Macros</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Inbox</a></article>
        <article class="flex flex-col gap-2 rounded-2xl bg-white p-6 ring-2 ring-tpt12-acc"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-acc uppercase">Desk</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$38<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/seat</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>SLAs &amp; routing</li><li>Knowledge base</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt12-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt12-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose Desk</a></article>
        <article class="flex flex-col gap-2 rounded-2xl border border-tpt12-line bg-white p-6"><h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt12-mut uppercase">AI Agent</h3><p class="text-[38px] leading-tight font-extrabold tracking-[-0.035em]">$0.90<small class="text-sm font-semibold tracking-normal text-tpt12-mut">/resolution</small></p><ul class="mt-1 mb-4 grid flex-1 content-start gap-2 text-sm text-tpt12-body *:flex *:gap-2 *:before:font-bold *:before:text-tpt12-acc *:before:content-['✓']"><li>Autonomous replies</li><li>Pay per outcome</li></ul><a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt12-line text-sm font-bold text-tpt12-ink no-underline transition-colors hover:border-tpt12-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt12-acc">Choose AI Agent</a></article>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt12-line bg-white px-3.5 py-2 font-tpt12-mono text-[11.5px] text-tpt12-mut">translate-x-full / [200%] · group-has-[#tpt12-t2:checked]/p:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt12-bg: #f5f6fa;
  --color-tpt12-bg: oklch(0.97 0.006 270);
  --color-tpt12-track: #e5e7f0;
  --color-tpt12-track: oklch(0.925 0.012 270);
  --color-tpt12-ink: #181b28;
  --color-tpt12-ink: oklch(0.22 0.025 270);
  --color-tpt12-body: #454b61;
  --color-tpt12-body: oklch(0.42 0.035 270);
  --color-tpt12-mut: #5c627a;
  --color-tpt12-mut: oklch(0.49 0.035 270);
  --color-tpt12-line: #e0e3ee;
  --color-tpt12-line: oklch(0.91 0.013 270);
  --color-tpt12-acc: #3d4fe0;
  --color-tpt12-acc: oklch(0.52 0.21 268);
  --color-tpt12-acc-ink: #2e3cb5;
  --color-tpt12-acc-ink: oklch(0.44 0.19 268);
  --font-tpt12-sans: 'Manrope', system-ui, sans-serif;
  --font-tpt12-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-12 {
  width: 100%;
  min-height: 100svh;
}
```
