---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pricing-plan-radio-cards/"
title: "Tailwind Pricing Plan Radio Cards"
section: "components"
category: "tailwind-css-radio-buttons"
category_name: "Tailwind CSS Radio Buttons"
description: "A complete pricing-table selector: three plan cards with price, features and a \"Recommended\" crown — each card a radio, so the whole table is one submittable…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Plan Radio Cards
Source: https://codefronts.com/components/tailwind-css-radio-buttons/tailwind-pricing-plan-radio-cards/

A complete pricing-table selector: three plan cards with price, features and a "Recommended" crown — each card a radio, so the whole table is one submittable form control. The Select / Selected ✓ pill is two spans stacked with [grid-area:1/1] and cross-faded by group-has-checked:; the summary line under the table follows the value.
## HTML
```html
<section class="trb-17 w-full min-h-svh grid place-items-center bg-trb17-bg px-6 py-14 font-trb17-sans text-trb17-ink" aria-label="Subscription pricing plan cards demo">
  <fieldset class="group/plans grid justify-items-center">
    <legend class="text-center text-[28px] font-extrabold tracking-[-0.025em]">Pick your plan</legend>
    <div class="mt-8 flex flex-wrap justify-center gap-[18px]">
      <label class="group relative grid w-[14.5rem] cursor-pointer content-start gap-1.5 rounded-[18px] border-2 border-trb17-line bg-white px-[22px] pt-7 pb-[22px] transition duration-250 hover:border-trb17-acc/45 has-checked:border-trb17-acc has-checked:shadow-trb17-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb17-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-1 motion-reduce:transition-none">
        <input type="radio" name="trb-17" value="starter" class="sr-only">
        <span class="text-sm font-bold tracking-[0.08em] text-trb17-mut uppercase">Starter</span>
        <span class="text-[34px] font-extrabold tracking-[-0.03em] tabular-nums">$0<small class="text-sm font-semibold tracking-normal text-trb17-mut">/mo</small></span>
        <ul class="mt-2.5 grid gap-[7px] *:relative *:pl-5 *:text-[13.5px] *:text-trb17-body *:before:absolute *:before:top-[5px] *:before:left-0 *:before:h-1.5 *:before:w-2.5 *:before:-rotate-45 *:before:border-b-2 *:before:border-l-2 *:before:border-trb17-acc *:before:content-['']"><li>3 projects</li><li>Community support</li><li>1 GB storage</li></ul>
        <span class="mt-[18px] grid min-h-11 place-items-center overflow-hidden rounded-[10px] border-[1.5px] border-trb17-pill text-sm font-bold text-trb17-body transition-colors duration-250 *:[grid-area:1/1] *:transition-[opacity,translate] *:duration-250 group-has-checked:border-trb17-acc group-has-checked:bg-trb17-acc"><span class="group-has-checked:-translate-y-1.5 group-has-checked:opacity-0">Select</span><span class="translate-y-1.5 text-white opacity-0 group-has-checked:translate-y-0 group-has-checked:opacity-100">Selected ✓</span></span>
      </label>
      <label class="group relative grid w-[14.5rem] cursor-pointer content-start gap-1.5 rounded-[18px] border-2 border-trb17-acc/35 bg-white px-[22px] pt-7 pb-[22px] transition duration-250 hover:border-trb17-acc/45 has-checked:border-trb17-acc has-checked:shadow-trb17-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb17-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-1 motion-reduce:transition-none">
        <input type="radio" name="trb-17" value="pro" class="sr-only" checked>
        <span class="absolute -top-[11px] left-1/2 -translate-x-1/2 rounded-full bg-trb17-acc px-3 py-[3px] text-[11px] font-bold tracking-[0.04em] whitespace-nowrap text-white">Recommended</span>
        <span class="text-sm font-bold tracking-[0.08em] text-trb17-mut uppercase">Pro</span>
        <span class="text-[34px] font-extrabold tracking-[-0.03em] tabular-nums">$19<small class="text-sm font-semibold tracking-normal text-trb17-mut">/mo</small></span>
        <ul class="mt-2.5 grid gap-[7px] *:relative *:pl-5 *:text-[13.5px] *:text-trb17-body *:before:absolute *:before:top-[5px] *:before:left-0 *:before:h-1.5 *:before:w-2.5 *:before:-rotate-45 *:before:border-b-2 *:before:border-l-2 *:before:border-trb17-acc *:before:content-['']"><li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li></ul>
        <span class="mt-[18px] grid min-h-11 place-items-center overflow-hidden rounded-[10px] border-[1.5px] border-trb17-pill text-sm font-bold text-trb17-body transition-colors duration-250 *:[grid-area:1/1] *:transition-[opacity,translate] *:duration-250 group-has-checked:border-trb17-acc group-has-checked:bg-trb17-acc"><span class="group-has-checked:-translate-y-1.5 group-has-checked:opacity-0">Select</span><span class="translate-y-1.5 text-white opacity-0 group-has-checked:translate-y-0 group-has-checked:opacity-100">Selected ✓</span></span>
      </label>
      <label class="group relative grid w-[14.5rem] cursor-pointer content-start gap-1.5 rounded-[18px] border-2 border-trb17-line bg-white px-[22px] pt-7 pb-[22px] transition duration-250 hover:border-trb17-acc/45 has-checked:border-trb17-acc has-checked:shadow-trb17-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-trb17-acc motion-safe:hover:-translate-y-0.5 motion-safe:has-checked:-translate-y-1 motion-reduce:transition-none">
        <input type="radio" name="trb-17" value="team" class="sr-only">
        <span class="text-sm font-bold tracking-[0.08em] text-trb17-mut uppercase">Team</span>
        <span class="text-[34px] font-extrabold tracking-[-0.03em] tabular-nums">$49<small class="text-sm font-semibold tracking-normal text-trb17-mut">/mo</small></span>
        <ul class="mt-2.5 grid gap-[7px] *:relative *:pl-5 *:text-[13.5px] *:text-trb17-body *:before:absolute *:before:top-[5px] *:before:left-0 *:before:h-1.5 *:before:w-2.5 *:before:-rotate-45 *:before:border-b-2 *:before:border-l-2 *:before:border-trb17-acc *:before:content-['']"><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Unlimited storage</li></ul>
        <span class="mt-[18px] grid min-h-11 place-items-center overflow-hidden rounded-[10px] border-[1.5px] border-trb17-pill text-sm font-bold text-trb17-body transition-colors duration-250 *:[grid-area:1/1] *:transition-[opacity,translate] *:duration-250 group-has-checked:border-trb17-acc group-has-checked:bg-trb17-acc"><span class="group-has-checked:-translate-y-1.5 group-has-checked:opacity-0">Select</span><span class="translate-y-1.5 text-white opacity-0 group-has-checked:translate-y-0 group-has-checked:opacity-100">Selected ✓</span></span>
      </label>
    </div>
    <p class="mt-6 flex min-h-11 items-center gap-2.5 rounded-full bg-white px-5 text-sm text-trb17-body shadow-trb17-sum ring-1 ring-trb17-line">
      <span aria-hidden="true" class="size-2 rounded-full bg-trb17-acc"></span>
      <span class="hidden group-has-[[value=starter]:checked]/plans:inline"><strong class="font-bold text-trb17-ink">Starter</strong> — free forever, upgrade anytime.</span>
      <span class="hidden group-has-[[value=pro]:checked]/plans:inline"><strong class="font-bold text-trb17-ink">Pro</strong> — 14-day free trial, cancel anytime.</span>
      <span class="hidden group-has-[[value=team]:checked]/plans:inline"><strong class="font-bold text-trb17-ink">Team</strong> — includes onboarding for your whole org.</span>
    </p>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-trb17-bg: #f4f5f9;
  --color-trb17-bg: oklch(0.968 0.006 270);
  --color-trb17-ink: #1c2130;
  --color-trb17-ink: oklch(0.24 0.03 270);
  --color-trb17-body: #4f5569;
  --color-trb17-body: oklch(0.45 0.03 270);
  --color-trb17-mut: #5f6579;
  --color-trb17-mut: oklch(0.5 0.025 270);
  --color-trb17-line: #e5e7f0;
  --color-trb17-line: oklch(0.93 0.01 275);
  --color-trb17-pill: #d7dae6;
  --color-trb17-pill: oklch(0.89 0.015 275);
  --color-trb17-acc: #3d5fe0;
  --color-trb17-acc: oklch(0.55 0.2 262);
  --shadow-trb17-lift: 0 22px 44px -20px oklch(0.55 0.2 262 / 0.55);
  --shadow-trb17-sum: 0 8px 20px -14px oklch(0.25 0.03 270 / 0.25);
  --font-trb17-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.trb-17 {
  width: 100%;
  min-height: 100svh;
}
```
