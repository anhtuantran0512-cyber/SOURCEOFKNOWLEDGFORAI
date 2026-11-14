---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-button-groups/tailwind-pricing-toggle-monthly-yearly/"
title: "Tailwind Pricing Toggle — Monthly / Yearly Billing Switch (No JS)"
section: "components"
category: "tailwind-css-button-groups"
category_name: "Tailwind CSS Button Groups"
description: "The SaaS pricing switch, solved in markup: two radios drive a sliding pill, the prices on every plan card and the savings line beneath them — all through…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Toggle — Monthly / Yearly Billing Switch (No JS)
Source: https://codefronts.com/components/tailwind-css-button-groups/tailwind-pricing-toggle-monthly-yearly/

The SaaS pricing switch, solved in markup: two radios drive a sliding pill, the prices on every plan card and the savings line beneath them — all through group-has-[#tbg04-y:checked]/card: variants on the elements that change. The inactive price is invisible, not just transparent, so screen readers only ever announce the price you can see. No JavaScript.
## HTML
```html
<section class="tbg-04 w-full min-h-svh grid place-items-center bg-tbg04-bg bg-[radial-gradient(120%_120%_at_50%_0%,var(--color-tbg04-glow),transparent_70%)] px-5 py-14 font-tbg04-sans text-tbg04-ink" aria-label="Monthly yearly pricing toggle demo">
  <div class="group/card @container w-full max-w-[36rem] rounded-3xl bg-white px-6 pt-8 pb-7 shadow-tbg04-card sm:px-8">
    <div role="radiogroup" aria-label="Billing period" class="relative mx-auto mb-7 grid w-fit grid-cols-2 gap-1 rounded-full bg-tbg04-well p-1">
      <label class="relative z-1 flex min-h-11 cursor-pointer items-center justify-center rounded-full px-5 text-[15px] font-semibold whitespace-nowrap text-tbg04-mut transition-colors duration-300 has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg04-acc"><input type="radio" name="tbg04" id="tbg04-m" class="sr-only" checked>Monthly</label>
      <label class="relative z-1 flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-full px-5 text-[15px] font-semibold whitespace-nowrap text-tbg04-mut transition-colors duration-300 has-checked:text-white has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tbg04-acc"><input type="radio" name="tbg04" id="tbg04-y" class="sr-only">Yearly <span class="rounded-full bg-white px-2 py-0.5 text-[11px] font-extrabold text-tbg04-acc-d">Save 20%</span></label>
      <span aria-hidden="true" class="pointer-events-none absolute top-1 bottom-1 left-1 z-0 w-[calc(50%-0.375rem)] rounded-full bg-tbg04-ink shadow-[0_6px_16px_-6px_rgb(6_60_58/0.7)] transition-transform duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tbg04-y:checked]/card:translate-x-[calc(100%+0.25rem)] motion-reduce:transition-none"></span>
    </div>
    <div class="grid grid-cols-2 gap-3.5 @max-md:grid-cols-1">
      <div class="flex flex-col rounded-2xl border-[1.5px] border-tbg04-line p-5">
        <p class="text-[13px] font-extrabold uppercase tracking-[0.1em] text-tbg04-acc-d">Starter</p>
        <p class="relative mt-2 mb-1 grid h-11 text-[15px] text-tbg04-mut">
          <span class="col-start-1 row-start-1 flex items-baseline transition-[opacity,visibility] duration-300 group-has-[#tbg04-y:checked]/card:invisible group-has-[#tbg04-y:checked]/card:opacity-0"><b class="mr-0.5 text-[34px] font-extrabold tracking-[-0.02em] text-tbg04-ink">$12</b>/mo</span>
          <span class="invisible col-start-1 row-start-1 flex items-baseline opacity-0 transition-[opacity,visibility] duration-300 group-has-[#tbg04-y:checked]/card:visible group-has-[#tbg04-y:checked]/card:opacity-100"><b class="mr-0.5 text-[34px] font-extrabold tracking-[-0.02em] text-tbg04-ink">$115</b>/yr</span>
        </p>
        <p class="grid text-[13px] leading-normal text-tbg04-mut"><span class="col-start-1 row-start-1 group-has-[#tbg04-y:checked]/card:invisible">Per seat, billed monthly.</span><span class="invisible col-start-1 row-start-1 font-semibold text-tbg04-acc-d group-has-[#tbg04-y:checked]/card:visible">You save $29 a year.</span></p>
        <button type="button" class="mt-5 min-h-11 cursor-pointer rounded-xl border-[1.5px] border-tbg04-line text-[14.5px] font-bold transition hover:border-tbg04-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg04-acc">Start free trial</button>
      </div>
      <div class="flex flex-col rounded-2xl border-[1.5px] border-tbg04-acc bg-linear-to-b from-tbg04-tint to-white p-5">
        <p class="flex items-center justify-between text-[13px] font-extrabold uppercase tracking-[0.1em] text-tbg04-acc-d">Studio <span class="rounded-full bg-tbg04-ink px-2 py-0.5 text-[10.5px] tracking-[0.06em] text-white">Popular</span></p>
        <p class="relative mt-2 mb-1 grid h-11 text-[15px] text-tbg04-mut">
          <span class="col-start-1 row-start-1 flex items-baseline transition-[opacity,visibility] duration-300 group-has-[#tbg04-y:checked]/card:invisible group-has-[#tbg04-y:checked]/card:opacity-0"><b class="mr-0.5 text-[34px] font-extrabold tracking-[-0.02em] text-tbg04-ink">$29</b>/mo</span>
          <span class="invisible col-start-1 row-start-1 flex items-baseline opacity-0 transition-[opacity,visibility] duration-300 group-has-[#tbg04-y:checked]/card:visible group-has-[#tbg04-y:checked]/card:opacity-100"><b class="mr-0.5 text-[34px] font-extrabold tracking-[-0.02em] text-tbg04-ink">$278</b>/yr</span>
        </p>
        <p class="grid text-[13px] leading-normal text-tbg04-mut"><span class="col-start-1 row-start-1 group-has-[#tbg04-y:checked]/card:invisible">Unlimited projects, billed monthly.</span><span class="invisible col-start-1 row-start-1 font-semibold text-tbg04-acc-d group-has-[#tbg04-y:checked]/card:visible">You save $70 a year.</span></p>
        <button type="button" class="mt-5 min-h-11 cursor-pointer rounded-xl bg-tbg04-ink text-[14.5px] font-bold text-white transition hover:brightness-125 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tbg04-acc">Get Studio</button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbg04-bg: #d6efe9;
  --color-tbg04-glow: #f1fcf9;
  --color-tbg04-well: #e4f1ee;
  --color-tbg04-line: #dbe9e5;
  --color-tbg04-tint: #effaf7;
  --color-tbg04-ink: #0d2b2e;
  --color-tbg04-mut: #4f6c69;
  --color-tbg04-mut: oklch(0.49 0.03 190);
  --color-tbg04-acc: #1fb5b0;
  --color-tbg04-acc: oklch(0.68 0.12 190);
  --color-tbg04-acc-d: #0b7f7c;
  --color-tbg04-acc-d: oklch(0.52 0.09 192);
  --shadow-tbg04-card: 0 30px 70px -40px rgb(6 60 58 / 0.5);
  --font-tbg04-sans: 'Manrope', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, restated so the stage is sized before the browser build compiles. */

.tbg-04 {
  width: 100%;
  min-height: 100svh;
}
```
