---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-group-with-badges/"
title: "Tailwind Radio Group with Badges"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A conversion-focused plan list where the marketing meta lives inside the choice: each row carries a price and an optional \"Most popular\" or \"Best value\" badge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radio Group with Badges
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-radio-group-with-badges/

A conversion-focused plan list where the marketing meta lives inside the choice: each row carries a price and an optional "Most popular" or "Best value" badge. A four-column grid keeps prices aligned whether or not a row has a badge, and a constant 2px border means the checked swap causes zero layout shift.
## HTML
```html
<section class="trb-06 w-full min-h-svh grid place-items-center bg-trb06-bg px-6 py-14 font-trb06-sans text-trb06-ink" aria-label="Radio option group with badges demo">
  <fieldset class="@container w-full max-w-[28rem]">
    <legend class="text-[26px] font-extrabold tracking-[-0.025em]">Choose a plan</legend>
    <div class="mt-5 grid gap-2.5">
      <label class="group relative grid min-h-[3.75rem] cursor-pointer grid-cols-[auto_auto_1fr_auto] items-center gap-x-3 gap-y-1 rounded-2xl border-2 border-trb06-line bg-white px-[18px] py-3 transition duration-250 hover:border-trb06-acc/40 has-checked:border-trb06-acc has-checked:bg-trb06-acc/4 has-checked:shadow-trb06-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb06-acc motion-reduce:transition-none">
        <input type="radio" name="trb-06" value="basic" class="sr-only">
        <span aria-hidden="true" class="grid size-[21px] place-items-center rounded-full border-2 border-trb06-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb06-spring after:content-[''] group-has-checked:border-trb06-acc group-has-checked:bg-trb06-acc group-has-checked:after:scale-100"></span>
        <span class="text-base font-bold">Basic</span>
        <span></span>
        <span class="text-base font-extrabold tabular-nums">$9<small class="text-xs font-semibold text-trb06-mut">/mo</small></span>
      </label>
      <label class="group relative grid min-h-[3.75rem] cursor-pointer grid-cols-[auto_auto_1fr_auto] items-center gap-x-3 gap-y-1 rounded-2xl border-2 border-trb06-line bg-white px-[18px] py-3 transition duration-250 hover:border-trb06-acc/40 has-checked:border-trb06-acc has-checked:bg-trb06-acc/4 has-checked:shadow-trb06-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb06-acc motion-reduce:transition-none">
        <input type="radio" name="trb-06" value="pro" class="sr-only" checked>
        <span aria-hidden="true" class="grid size-[21px] place-items-center rounded-full border-2 border-trb06-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb06-spring after:content-[''] group-has-checked:border-trb06-acc group-has-checked:bg-trb06-acc group-has-checked:after:scale-100"></span>
        <span class="text-base font-bold">Pro</span>
        <em class="justify-self-start rounded-full bg-trb06-acc/14 px-2.5 py-0.5 text-[11px] font-bold tracking-[0.02em] not-italic whitespace-nowrap text-trb06-acc @max-[22rem]:order-last @max-[22rem]:col-start-2">Most popular</em>
        <span class="text-base font-extrabold tabular-nums">$24<small class="text-xs font-semibold text-trb06-mut">/mo</small></span>
      </label>
      <label class="group relative grid min-h-[3.75rem] cursor-pointer grid-cols-[auto_auto_1fr_auto] items-center gap-x-3 gap-y-1 rounded-2xl border-2 border-trb06-line bg-white px-[18px] py-3 transition duration-250 hover:border-trb06-acc/40 has-checked:border-trb06-acc has-checked:bg-trb06-acc/4 has-checked:shadow-trb06-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-2 has-focus-visible:outline-trb06-acc motion-reduce:transition-none">
        <input type="radio" name="trb-06" value="team" class="sr-only">
        <span aria-hidden="true" class="grid size-[21px] place-items-center rounded-full border-2 border-trb06-ring transition after:size-[9px] after:scale-0 after:rounded-full after:bg-white after:transition-transform after:duration-300 after:ease-trb06-spring after:content-[''] group-has-checked:border-trb06-acc group-has-checked:bg-trb06-acc group-has-checked:after:scale-100"></span>
        <span class="text-base font-bold">Team</span>
        <em class="justify-self-start rounded-full bg-trb06-value-bg px-2.5 py-0.5 text-[11px] font-bold tracking-[0.02em] not-italic whitespace-nowrap text-trb06-value @max-[22rem]:order-last @max-[22rem]:col-start-2">Best value</em>
        <span class="text-base font-extrabold tabular-nums">$59<small class="text-xs font-semibold text-trb06-mut">/mo</small></span>
      </label>
    </div>
    <p class="mt-4 text-[13px] text-trb06-mut">All plans include a 14-day free trial. Prices in USD, excl. tax.</p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb06-bg: #f6f5fa;
  --color-trb06-bg: oklch(0.97 0.006 300);
  --color-trb06-ink: #1e2130;
  --color-trb06-ink: oklch(0.24 0.025 280);
  --color-trb06-mut: #62677a;
  --color-trb06-mut: oklch(0.51 0.025 280);
  --color-trb06-line: #e6e6ef;
  --color-trb06-line: oklch(0.93 0.01 290);
  --color-trb06-ring: #c3c8d9;
  --color-trb06-ring: oklch(0.84 0.02 280);
  --color-trb06-acc: #8a3fd1;
  --color-trb06-acc: oklch(0.52 0.21 300);
  --color-trb06-value: #186a3d;
  --color-trb06-value: oklch(0.45 0.11 155);
  --color-trb06-value-bg: #dcf3e3;
  --color-trb06-value-bg: oklch(0.94 0.05 155);
  --shadow-trb06-lift: 0 10px 24px -16px oklch(0.52 0.21 300 / 0.55);
  --ease-trb06-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --font-trb06-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-06 {
  width: 100%;
  min-height: 100svh;
}
```
