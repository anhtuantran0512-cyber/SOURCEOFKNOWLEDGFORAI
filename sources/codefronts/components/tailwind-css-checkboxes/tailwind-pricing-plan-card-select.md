---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-checkboxes/tailwind-pricing-plan-card-select/"
title: "Tailwind Pricing Plan Card Select — Checkbox-Style Selectable Cards"
section: "components"
category: "tailwind-css-checkboxes"
category_name: "Tailwind CSS Checkboxes"
description: "Selectable pricing cards that lift, outline and badge themselves on selection — all from has-checked: on the card label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Plan Card Select — Checkbox-Style Selectable Cards
Source: https://codefronts.com/components/tailwind-css-checkboxes/tailwind-pricing-plan-card-select/

Selectable pricing cards that lift, outline and badge themselves on selection — all from has-checked: on the card label. Because plans are mutually exclusive, the port quietly swaps the original checkboxes for a named radio group: same look, correct semantics, arrow-key navigation for free.
## HTML
```html
<section class="tcb-03 w-full min-h-svh grid place-items-center bg-tcb03-bg px-5 py-14 font-tcb03-sans text-tcb03-ink selection:bg-tcb03-acc selection:text-white" aria-label="Pricing plan selector">
  <fieldset class="w-full max-w-3xl">
    <legend class="mb-6 w-full text-center text-2xl font-extrabold tracking-[-0.02em]">Pick your plan</legend>
    <div class="grid gap-4 sm:grid-cols-3">
      <label class="group relative flex cursor-pointer flex-col gap-1.5 rounded-2xl border-2 border-tcb03-line bg-white px-5 py-5.5 shadow-tcb03-rest transition duration-300 ease-[cubic-bezier(.2,.8,.2,1)] hover:border-tcb03-hover has-checked:-translate-y-1 has-checked:border-tcb03-acc has-checked:shadow-tcb03-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb03-acc motion-reduce:transition-none motion-reduce:has-checked:translate-y-0"><input type="radio" name="tcb03-plan" class="peer sr-only">
        <span aria-hidden="true" class="absolute right-3.5 top-3.5 grid size-[22px] place-items-center rounded-full border-2 border-tcb03-line bg-white text-white transition-colors duration-200 peer-checked:border-tcb03-acc peer-checked:bg-tcb03-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3 scale-40 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>
        <span class="text-[13px] font-bold uppercase tracking-[0.06em] text-tcb03-mut">Starter</span>
        <span class="text-[32px] font-extrabold tabular-nums tracking-[-0.02em]">$9<span class="text-sm font-semibold text-tcb03-mut">/mo</span></span>
        <span class="mt-0.5 text-[13px] leading-normal text-tcb03-mut">3 projects · 1 seat · community support</span>
      </label>
      <label class="group relative flex cursor-pointer flex-col gap-1.5 rounded-2xl border-2 border-tcb03-line bg-white px-5 py-5.5 shadow-tcb03-rest transition duration-300 ease-[cubic-bezier(.2,.8,.2,1)] hover:border-tcb03-hover has-checked:-translate-y-1 has-checked:border-tcb03-acc has-checked:shadow-tcb03-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb03-acc motion-reduce:transition-none motion-reduce:has-checked:translate-y-0"><input type="radio" name="tcb03-plan" class="peer sr-only" checked>
        <span aria-hidden="true" class="absolute right-3.5 top-3.5 grid size-[22px] place-items-center rounded-full border-2 border-tcb03-line bg-white text-white transition-colors duration-200 peer-checked:border-tcb03-acc peer-checked:bg-tcb03-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3 scale-40 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>
        <span class="absolute -top-2.5 left-5 rounded-full bg-tcb03-acc px-2.5 py-0.5 text-[10.5px] font-bold uppercase tracking-[0.1em] text-white">Popular</span>
        <span class="text-[13px] font-bold uppercase tracking-[0.06em] text-tcb03-mut">Growth</span>
        <span class="text-[32px] font-extrabold tabular-nums tracking-[-0.02em]">$29<span class="text-sm font-semibold text-tcb03-mut">/mo</span></span>
        <span class="mt-0.5 text-[13px] leading-normal text-tcb03-mut">Unlimited projects · 5 seats · priority support</span>
      </label>
      <label class="group relative flex cursor-pointer flex-col gap-1.5 rounded-2xl border-2 border-tcb03-line bg-white px-5 py-5.5 shadow-tcb03-rest transition duration-300 ease-[cubic-bezier(.2,.8,.2,1)] hover:border-tcb03-hover has-checked:-translate-y-1 has-checked:border-tcb03-acc has-checked:shadow-tcb03-lift has-focus-visible:outline-3 has-focus-visible:outline-offset-3 has-focus-visible:outline-tcb03-acc motion-reduce:transition-none motion-reduce:has-checked:translate-y-0"><input type="radio" name="tcb03-plan" class="peer sr-only">
        <span aria-hidden="true" class="absolute right-3.5 top-3.5 grid size-[22px] place-items-center rounded-full border-2 border-tcb03-line bg-white text-white transition-colors duration-200 peer-checked:border-tcb03-acc peer-checked:bg-tcb03-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" class="size-3 scale-40 opacity-0 transition duration-200 group-has-checked:scale-100 group-has-checked:opacity-100"><path d="M20 6 9 17l-5-5"/></svg></span>
        <span class="text-[13px] font-bold uppercase tracking-[0.06em] text-tcb03-mut">Scale</span>
        <span class="text-[32px] font-extrabold tabular-nums tracking-[-0.02em]">$79<span class="text-sm font-semibold text-tcb03-mut">/mo</span></span>
        <span class="mt-0.5 text-[13px] leading-normal text-tcb03-mut">SSO · audit logs · dedicated CSM</span>
      </label>
    </div>
  </fieldset>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcb03-bg: #f5f4f8;
  --color-tcb03-bg: oklch(0.97 0.006 295);
  --color-tcb03-ink: #22203a;
  --color-tcb03-ink: oklch(0.25 0.04 290);
  --color-tcb03-mut: #625f78;
  --color-tcb03-mut: oklch(0.5 0.03 290);
  --color-tcb03-line: #e5e4ee;
  --color-tcb03-line: oklch(0.92 0.01 290);
  --color-tcb03-hover: #c7c4dd;
  --color-tcb03-hover: oklch(0.83 0.03 290);
  --color-tcb03-acc: #6a3fd6;
  --color-tcb03-acc: oklch(0.52 0.2 288);
  --font-tcb03-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --shadow-tcb03-rest: 0 10px 26px -22px rgb(30 20 60 / 0.6);
  --shadow-tcb03-lift: 0 22px 40px -24px rgb(80 40 180 / 0.55);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tcb-03 {
  width: 100%;
  min-height: 100svh;
}
```
