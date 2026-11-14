---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-pricing-table-with-vertical-plan-tabs-and-billing-toggle/"
title: "Tailwind Pricing Table with Vertical Plan Tabs and Billing Toggle"
section: "navigation"
category: "tailwind-css-vertical-tabs"
category_name: "Tailwind CSS Vertical Tabs"
description: "A SaaS pricing card where Starter, Growth and Scale sit in a vertical plan rail and a Monthly/Annual switch re-prices every number on the page &mdash; with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Table with Vertical Plan Tabs and Billing Toggle
Source: https://codefronts.com/navigation/tailwind-css-vertical-tabs/tailwind-pricing-table-with-vertical-plan-tabs-and-billing-toggle/

A SaaS pricing card where Starter, Growth and Scale sit in a vertical plan rail and a Monthly/Annual switch re-prices every number on the page &mdash; with no JavaScript. Two independent radio groups are read from one ancestor with group-has-[#tvt-11-c-yr:checked]/pr:, the plan cards style themselves with has-checked:, and a spring-eased thumb slides under the active billing cycle.
## HTML
```html
<section class="tvt-11 w-full min-h-svh grid place-items-center bg-tvt11-bg bg-[radial-gradient(60%_50%_at_85%_0%,var(--color-tvt11-glow),transparent_70%),radial-gradient(50%_45%_at_0%_100%,var(--color-tvt11-glow2),transparent_70%)] px-4 py-14 font-tvt11-sans text-tvt11-ink antialiased sm:px-6" aria-label="Tailwind pricing table with vertical plan tabs and billing toggle demo">
  <svg width="0" height="0" class="absolute" aria-hidden="true" focusable="false"><defs><linearGradient id="tvt-11-ok" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--color-tvt11-acc)"/><stop offset="1" stop-color="var(--color-tvt11-acc2)"/></linearGradient></defs></svg>
  <div class="group/pr grid w-full max-w-[60rem] justify-items-center gap-8">
    <header class="grid justify-items-center gap-3 text-center">
      <p class="rounded-full bg-tvt11-acc/10 px-3 py-1.5 font-tvt11-mono text-[11.5px] font-medium text-tvt11-acc-ink ring-1 ring-tvt11-acc/20 ring-inset">Pricing</p>
      <h2 class="text-[clamp(30px,4.6vw,46px)] leading-[1.04] font-bold tracking-[-0.04em] text-balance">Plans that grow <span class="bg-linear-to-r from-tvt11-hl to-tvt11-hl2 bg-clip-text pe-1 text-transparent">with your team</span></h2>
      <p class="max-w-[44ch] text-[15px] leading-relaxed text-tvt11-mut text-pretty">Pick a plan on the left, flip the billing cycle, and every price on the page follows &mdash; two radio groups, zero JavaScript.</p>
    </header>

    <div class="@container w-full">
    <div class="grid w-full grid-cols-[minmax(17rem,22rem)_minmax(0,1fr)] overflow-hidden rounded-[26px] bg-tvt11-card shadow-tvt11-card ring-1 ring-tvt11-line starting:translate-y-3 starting:opacity-0 transition-[opacity,translate] duration-700 ease-[cubic-bezier(.16,1,.3,1)] motion-reduce:transition-none @max-[46rem]:grid-cols-1">
      <div class="flex flex-col gap-3 border-e border-tvt11-line bg-tvt11-rail p-4 sm:p-5 @max-[46rem]:border-e-0 @max-[46rem]:border-b">
        <div role="radiogroup" aria-label="Billing cycle" class="relative grid grid-cols-2 rounded-2xl bg-tvt11-card p-1 ring-1 ring-tvt11-line before:absolute before:inset-y-1 before:start-1 before:w-[calc(50%-0.25rem)] before:rounded-xl before:bg-linear-to-br before:from-tvt11-acc before:to-tvt11-acc2 before:shadow-tvt11-cta before:transition-transform before:duration-300 before:ease-[cubic-bezier(.34,1.3,.5,1)] group-has-[#tvt-11-c-yr:checked]/pr:before:translate-x-full motion-reduce:before:transition-none rtl:group-has-[#tvt-11-c-yr:checked]/pr:before:-translate-x-full">
          <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center rounded-xl text-[13.5px] font-semibold text-tvt11-mut transition-colors duration-200 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt11-ring"><input type="radio" name="tvt-11-cycle" id="tvt-11-c-mo" class="sr-only" checked>Monthly</label>
          <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center gap-1.5 rounded-xl text-[13.5px] font-semibold text-tvt11-mut transition-colors duration-200 has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt11-ring"><input type="radio" name="tvt-11-cycle" id="tvt-11-c-yr" class="sr-only">Annual<span class="rounded-full bg-tvt11-ok/15 px-1.5 py-0.5 font-tvt11-mono text-[9.5px] tracking-[0.04em] text-tvt11-ok uppercase transition-colors group-has-[#tvt-11-c-yr:checked]/pr:bg-white/20 group-has-[#tvt-11-c-yr:checked]/pr:text-white">−2 mo</span></label>
        </div>
        <p class="px-1 pt-2 font-tvt11-mono text-[10.5px] tracking-[0.16em] text-tvt11-mut uppercase">Choose a plan</p>
        <div role="radiogroup" aria-label="Plan" class="grid gap-2.5">

          <label class="group/tab relative flex min-h-[4.5rem] cursor-pointer items-center gap-3.5 rounded-2xl bg-tvt11-card/60 px-4 py-3 ring-1 ring-tvt11-line transition-[background-color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tvt11-card hover:shadow-tvt11-lift has-checked:bg-tvt11-card has-checked:shadow-tvt11-sel has-checked:ring-2 has-checked:ring-tvt11-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <input type="radio" name="tvt-11-plan" id="tvt-11-t1" class="sr-only">
            <span aria-hidden="true" class="grid size-5 shrink-0 place-items-center rounded-full ring-2 ring-tvt11-line transition-[box-shadow,background-color] duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt11-acc group-has-checked/tab:to-tvt11-acc2 group-has-checked/tab:ring-transparent"><span class="size-2 scale-0 rounded-full bg-white transition-transform duration-200 group-has-checked/tab:scale-100 motion-reduce:transition-none"></span></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="text-[15px] font-bold tracking-[-0.01em]">Starter</b><span class="truncate text-[12.5px] text-tvt11-mut">Solo builders & side projects</span></span>
            <span class="text-end leading-tight"><b class="block text-[17px] font-bold tracking-[-0.02em] tabular-nums group-has-checked/tab:text-tvt11-acc-ink"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">$12</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">$120</span></b><span class="font-tvt11-mono text-[10.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year</span></span></span>
          </label>

          <label class="group/tab relative flex min-h-[4.5rem] cursor-pointer items-center gap-3.5 rounded-2xl bg-tvt11-card/60 px-4 py-3 ring-1 ring-tvt11-line transition-[background-color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tvt11-card hover:shadow-tvt11-lift has-checked:bg-tvt11-card has-checked:shadow-tvt11-sel has-checked:ring-2 has-checked:ring-tvt11-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <input type="radio" name="tvt-11-plan" id="tvt-11-t2" class="sr-only" checked>
            <span class="absolute -top-2.5 end-4 rounded-full bg-linear-to-r from-tvt11-acc to-tvt11-acc2 px-2.5 py-0.5 font-tvt11-mono text-[9.5px] font-semibold tracking-[0.1em] text-white uppercase shadow-tvt11-cta">Popular</span>
            <span aria-hidden="true" class="grid size-5 shrink-0 place-items-center rounded-full ring-2 ring-tvt11-line transition-[box-shadow,background-color] duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt11-acc group-has-checked/tab:to-tvt11-acc2 group-has-checked/tab:ring-transparent"><span class="size-2 scale-0 rounded-full bg-white transition-transform duration-200 group-has-checked/tab:scale-100 motion-reduce:transition-none"></span></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="text-[15px] font-bold tracking-[-0.01em]">Growth</b><span class="truncate text-[12.5px] text-tvt11-mut">Small teams shipping weekly</span></span>
            <span class="text-end leading-tight"><b class="block text-[17px] font-bold tracking-[-0.02em] tabular-nums group-has-checked/tab:text-tvt11-acc-ink"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">$29</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">$290</span></b><span class="font-tvt11-mono text-[10.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year</span></span></span>
          </label>

          <label class="group/tab relative flex min-h-[4.5rem] cursor-pointer items-center gap-3.5 rounded-2xl bg-tvt11-card/60 px-4 py-3 ring-1 ring-tvt11-line transition-[background-color,box-shadow,translate] duration-200 ease-[cubic-bezier(.16,1,.3,1)] hover:-translate-y-px hover:bg-tvt11-card hover:shadow-tvt11-lift has-checked:bg-tvt11-card has-checked:shadow-tvt11-sel has-checked:ring-2 has-checked:ring-tvt11-acc has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tvt11-ring motion-reduce:transition-none motion-reduce:hover:translate-y-0">
            <input type="radio" name="tvt-11-plan" id="tvt-11-t3" class="sr-only">
            <span aria-hidden="true" class="grid size-5 shrink-0 place-items-center rounded-full ring-2 ring-tvt11-line transition-[box-shadow,background-color] duration-200 group-has-checked/tab:bg-linear-to-br group-has-checked/tab:from-tvt11-acc group-has-checked/tab:to-tvt11-acc2 group-has-checked/tab:ring-transparent"><span class="size-2 scale-0 rounded-full bg-white transition-transform duration-200 group-has-checked/tab:scale-100 motion-reduce:transition-none"></span></span>
            <span class="grid min-w-0 flex-1 gap-0.5"><b class="text-[15px] font-bold tracking-[-0.01em]">Scale</b><span class="truncate text-[12.5px] text-tvt11-mut">Orgs with compliance needs</span></span>
            <span class="text-end leading-tight"><b class="block text-[17px] font-bold tracking-[-0.02em] tabular-nums group-has-checked/tab:text-tvt11-acc-ink"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">$79</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">$790</span></b><span class="font-tvt11-mono text-[10.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year</span></span></span>
          </label>
        </div>
        <p class="mt-auto flex items-center gap-2 px-1 pt-3 text-[12.5px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true" focusable="false" class="shrink-0"><path d="M10 2.5 16 5v4.5c0 3.8-2.6 6.6-6 8-3.4-1.4-6-4.2-6-8V5Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="m7.3 10 1.9 1.9 3.6-3.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>30-day money-back guarantee</p>
      </div>

      <div class="grid p-6 sm:p-9">

          <article aria-label="Starter plan details" class="invisible col-start-1 row-start-1 flex translate-y-2 flex-col opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-11-t1:checked]/pr:visible group-has-[#tvt-11-t1:checked]/pr:translate-y-0 group-has-[#tvt-11-t1:checked]/pr:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center gap-2">
              <h3 class="font-tvt11-mono text-[12px] font-semibold tracking-[0.16em] text-tvt11-acc-ink uppercase">Starter</h3>
              <span class="hidden rounded-full bg-tvt11-ok/12 px-2.5 py-0.5 text-[11.5px] font-semibold text-tvt11-ok group-has-[#tvt-11-c-yr:checked]/pr:inline-flex">Save $24 a year</span>
            </div>
            <p class="mt-1.5 text-[14.5px] text-tvt11-mut">Everything one person needs to launch and iterate.</p>
            <p class="mt-5 flex items-baseline gap-1.5 tabular-nums">
              <span class="self-start pt-2 text-[22px] font-semibold text-tvt11-mut">$</span>
              <b class="text-[clamp(48px,7vw,64px)] leading-none font-extrabold tracking-[-0.05em]"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">12</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">120</span></b>
              <span class="text-[13.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month, billed monthly</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year, billed annually</span></span>
            </p>
            <div class="my-6 h-px bg-linear-to-r from-tvt11-line via-tvt11-acc/30 to-tvt11-line"></div>
            <ul class="grid gap-3 sm:grid-cols-2">
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>3 projects<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>1 team seat<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Community support<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="9.25" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="line-through decoration-tvt11-mut/40">SSO &amp; SAML</span><span class="sr-only">, not included</span></li>
              <li class="flex items-center gap-2.5 text-[14px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="9.25" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="line-through decoration-tvt11-mut/40">Audit log</span><span class="sr-only">, not included</span></li>
              <li class="flex items-center gap-2.5 text-[14px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="9.25" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="line-through decoration-tvt11-mut/40">Dedicated CSM</span><span class="sr-only">, not included</span></li>
            </ul>
            <div class="mt-auto flex flex-wrap items-center gap-x-4 gap-y-2 pt-7">
              <button type="button" class="inline-flex min-h-12 items-center gap-2 rounded-xl bg-tvt11-card px-5 text-[14.5px] font-semibold text-tvt11-ink ring-1 ring-tvt11-line transition-[translate,box-shadow] duration-200 hover:-translate-y-0.5 hover:ring-tvt11-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt11-ring active:translate-y-0 motion-reduce:transition-none">Start free trial</button>
              <p class="text-[12.5px] text-tvt11-mut">No card required · Cancel anytime</p>
            </div>
          </article>

          <article aria-label="Growth plan details" class="invisible col-start-1 row-start-1 flex translate-y-2 flex-col opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-11-t2:checked]/pr:visible group-has-[#tvt-11-t2:checked]/pr:translate-y-0 group-has-[#tvt-11-t2:checked]/pr:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center gap-2">
              <h3 class="font-tvt11-mono text-[12px] font-semibold tracking-[0.16em] text-tvt11-acc-ink uppercase">Growth</h3>
              <span class="hidden rounded-full bg-tvt11-ok/12 px-2.5 py-0.5 text-[11.5px] font-semibold text-tvt11-ok group-has-[#tvt-11-c-yr:checked]/pr:inline-flex">Save $58 a year</span>
            </div>
            <p class="mt-1.5 text-[14.5px] text-tvt11-mut">For teams that review, ship and measure together.</p>
            <p class="mt-5 flex items-baseline gap-1.5 tabular-nums">
              <span class="self-start pt-2 text-[22px] font-semibold text-tvt11-mut">$</span>
              <b class="text-[clamp(48px,7vw,64px)] leading-none font-extrabold tracking-[-0.05em]"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">29</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">290</span></b>
              <span class="text-[13.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month, billed monthly</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year, billed annually</span></span>
            </p>
            <div class="my-6 h-px bg-linear-to-r from-tvt11-line via-tvt11-acc/30 to-tvt11-line"></div>
            <ul class="grid gap-3 sm:grid-cols-2">
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited projects<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Up to 10 seats<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Priority support<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>SSO &amp; SAML<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="9.25" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="line-through decoration-tvt11-mut/40">Audit log</span><span class="sr-only">, not included</span></li>
              <li class="flex items-center gap-2.5 text-[14px] text-tvt11-mut"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="9.25" fill="none" stroke="currentColor" stroke-opacity=".4" stroke-width="1.5"/><path d="M7 10h6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span class="line-through decoration-tvt11-mut/40">Dedicated CSM</span><span class="sr-only">, not included</span></li>
            </ul>
            <div class="mt-auto flex flex-wrap items-center gap-x-4 gap-y-2 pt-7">
              <button type="button" class="inline-flex min-h-12 items-center gap-2 rounded-xl bg-linear-to-br from-tvt11-acc to-tvt11-acc2 px-5 text-[14.5px] font-semibold text-white shadow-tvt11-cta transition-[translate,box-shadow] duration-200 hover:-translate-y-0.5 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt11-ring active:translate-y-0 motion-reduce:transition-none">Start 14-day trial<svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4 10h11m-4-4.5L15.5 10 11 14.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
              <p class="text-[12.5px] text-tvt11-mut">No card required · Cancel anytime</p>
            </div>
          </article>

          <article aria-label="Scale plan details" class="invisible col-start-1 row-start-1 flex translate-y-2 flex-col opacity-0 transition-[opacity,translate,visibility] duration-300 ease-[cubic-bezier(.32,.72,.3,1)] group-has-[#tvt-11-t3:checked]/pr:visible group-has-[#tvt-11-t3:checked]/pr:translate-y-0 group-has-[#tvt-11-t3:checked]/pr:opacity-100 motion-reduce:transition-none">
            <div class="flex flex-wrap items-center gap-2">
              <h3 class="font-tvt11-mono text-[12px] font-semibold tracking-[0.16em] text-tvt11-acc-ink uppercase">Scale</h3>
              <span class="hidden rounded-full bg-tvt11-ok/12 px-2.5 py-0.5 text-[11.5px] font-semibold text-tvt11-ok group-has-[#tvt-11-c-yr:checked]/pr:inline-flex">Save $158 a year</span>
            </div>
            <p class="mt-1.5 text-[14.5px] text-tvt11-mut">Security reviews, procurement and a named human.</p>
            <p class="mt-5 flex items-baseline gap-1.5 tabular-nums">
              <span class="self-start pt-2 text-[22px] font-semibold text-tvt11-mut">$</span>
              <b class="text-[clamp(48px,7vw,64px)] leading-none font-extrabold tracking-[-0.05em]"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">79</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">790</span></b>
              <span class="text-[13.5px] text-tvt11-mut"><span class="group-has-[#tvt-11-c-yr:checked]/pr:hidden">/month, billed monthly</span><span class="hidden group-has-[#tvt-11-c-yr:checked]/pr:inline">/year, billed annually</span></span>
            </p>
            <div class="my-6 h-px bg-linear-to-r from-tvt11-line via-tvt11-acc/30 to-tvt11-line"></div>
            <ul class="grid gap-3 sm:grid-cols-2">
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited projects<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Unlimited seats<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>24/7 priority support<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>SSO &amp; SAML<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Audit log<span class="sr-only">, included</span></li>
              <li class="flex items-center gap-2.5 text-[14px]"><svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true" focusable="false" class="shrink-0"><circle cx="10" cy="10" r="10" fill="url(#tvt-11-ok)"/><path d="m6 10.2 2.6 2.6L14 7.5" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>Dedicated CSM<span class="sr-only">, included</span></li>
            </ul>
            <div class="mt-auto flex flex-wrap items-center gap-x-4 gap-y-2 pt-7">
              <button type="button" class="inline-flex min-h-12 items-center gap-2 rounded-xl bg-tvt11-card px-5 text-[14.5px] font-semibold text-tvt11-ink ring-1 ring-tvt11-line transition-[translate,box-shadow] duration-200 hover:-translate-y-0.5 hover:ring-tvt11-acc/50 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tvt11-ring active:translate-y-0 motion-reduce:transition-none">Talk to sales</button>
              <p class="text-[12.5px] text-tvt11-mut">No card required · Cancel anytime</p>
            </div>
          </article>
      </div>
    </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tvt11-card px-3.5 py-2 text-center font-tvt11-mono text-[11.5px] text-tvt11-mut ring-1 ring-tvt11-line">has-checked: · group-has-[#c-yr:checked]/pr: · tabular-nums</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tvt11-bg: #fbf1fa;
  --color-tvt11-bg: oklch(0.968 0.016 330);
  --color-tvt11-glow: #f7bbe9a6;
  --color-tvt11-glow: oklch(0.86 0.09 335 / 0.65);
  --color-tvt11-glow2: #deceff99;
  --color-tvt11-glow2: oklch(0.88 0.07 300 / 0.6);
  --color-tvt11-card: #fffdff;
  --color-tvt11-card: oklch(0.997 0.004 330);
  --color-tvt11-rail: #fcf4fb;
  --color-tvt11-rail: oklch(0.975 0.012 330);
  --color-tvt11-ink: #2c162a;
  --color-tvt11-ink: oklch(0.24 0.05 330);
  --color-tvt11-mut: #6d556a;
  --color-tvt11-mut: oklch(0.48 0.045 330);
  --color-tvt11-line: #e8d8e6;
  --color-tvt11-line: oklch(0.9 0.025 330);
  --color-tvt11-acc: #c2009c;
  --color-tvt11-acc: oklch(0.55 0.24 340);
  --color-tvt11-acc2: #822cc4;
  --color-tvt11-acc2: oklch(0.5 0.22 305);
  --color-tvt11-acc-ink: #a20081;
  --color-tvt11-acc-ink: oklch(0.48 0.21 340);
  --color-tvt11-hl: #ca0093;
  --color-tvt11-hl: oklch(0.56 0.25 345);
  --color-tvt11-hl2: #7a31ca;
  --color-tvt11-hl2: oklch(0.5 0.22 300);
  --color-tvt11-ring: #b229ad;
  --color-tvt11-ring: oklch(0.55 0.22 330);
  --color-tvt11-ok: #007654;
  --color-tvt11-ok: oklch(0.5 0.13 165);
  --font-tvt11-sans: 'Sora', system-ui, sans-serif;
  --font-tvt11-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --shadow-tvt11-card: 0 1px 2px oklch(0.3 0.1 330 / 0.06), 0 34px 80px -34px oklch(0.4 0.2 335 / 0.42);
  --shadow-tvt11-lift: 0 10px 24px -14px oklch(0.4 0.18 335 / 0.4);
  --shadow-tvt11-sel: 0 16px 34px -16px oklch(0.5 0.24 340 / 0.55), inset 0 1px 0 oklch(1 0 0 / 0.5);
  --shadow-tvt11-cta: 0 12px 26px -10px oklch(0.55 0.25 340 / 0.65), inset 0 1px 0 oklch(1 0 0 / 0.25);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tvt-11 {
  width: 100%;
  min-height: 100svh;
}
/* Dark palette: the same tokens re-pointed, so every utility (and every /opacity modifier) follows. */

@media (prefers-color-scheme: dark) {
  .tvt-11:not([data-theme="light"]) {
    --color-tvt11-bg: #160615;
    --color-tvt11-bg: oklch(0.16 0.04 330);
    --color-tvt11-glow: #60104c80;
    --color-tvt11-glow: oklch(0.34 0.13 340 / 0.5);
    --color-tvt11-glow2: #371b5b73;
    --color-tvt11-glow2: oklch(0.3 0.11 300 / 0.45);
    --color-tvt11-card: #220f21;
    --color-tvt11-card: oklch(0.205 0.045 330);
    --color-tvt11-rail: #1c0c1b;
    --color-tvt11-rail: oklch(0.185 0.04 330);
    --color-tvt11-ink: #f8f1f7;
    --color-tvt11-ink: oklch(0.965 0.012 330);
    --color-tvt11-mut: #c4abc1;
    --color-tvt11-mut: oklch(0.77 0.04 330);
    --color-tvt11-line: #442741;
    --color-tvt11-line: oklch(0.32 0.06 330);
    --color-tvt11-acc: #cc239f;
    --color-tvt11-acc: oklch(0.58 0.23 342);
    --color-tvt11-acc2: #8639c7;
    --color-tvt11-acc2: oklch(0.52 0.21 305);
    --color-tvt11-acc-ink: #fca2df;
    --color-tvt11-acc-ink: oklch(0.82 0.13 340);
    --color-tvt11-hl: #fd97d2;
    --color-tvt11-hl: oklch(0.8 0.14 345);
    --color-tvt11-hl2: #c4a4fe;
    --color-tvt11-hl2: oklch(0.78 0.13 300);
    --color-tvt11-ring: #f190dd;
    --color-tvt11-ring: oklch(0.78 0.15 335);
    --color-tvt11-ok: #5ed99e;
    --color-tvt11-ok: oklch(0.8 0.14 160);
  }
}

.tvt-11[data-theme="dark"] {
  --color-tvt11-bg: #160615;
  --color-tvt11-bg: oklch(0.16 0.04 330);
  --color-tvt11-glow: #60104c80;
  --color-tvt11-glow: oklch(0.34 0.13 340 / 0.5);
  --color-tvt11-glow2: #371b5b73;
  --color-tvt11-glow2: oklch(0.3 0.11 300 / 0.45);
  --color-tvt11-card: #220f21;
  --color-tvt11-card: oklch(0.205 0.045 330);
  --color-tvt11-rail: #1c0c1b;
  --color-tvt11-rail: oklch(0.185 0.04 330);
  --color-tvt11-ink: #f8f1f7;
  --color-tvt11-ink: oklch(0.965 0.012 330);
  --color-tvt11-mut: #c4abc1;
  --color-tvt11-mut: oklch(0.77 0.04 330);
  --color-tvt11-line: #442741;
  --color-tvt11-line: oklch(0.32 0.06 330);
  --color-tvt11-acc: #cc239f;
  --color-tvt11-acc: oklch(0.58 0.23 342);
  --color-tvt11-acc2: #8639c7;
  --color-tvt11-acc2: oklch(0.52 0.21 305);
  --color-tvt11-acc-ink: #fca2df;
  --color-tvt11-acc-ink: oklch(0.82 0.13 340);
  --color-tvt11-hl: #fd97d2;
  --color-tvt11-hl: oklch(0.8 0.14 345);
  --color-tvt11-hl2: #c4a4fe;
  --color-tvt11-hl2: oklch(0.78 0.13 300);
  --color-tvt11-ring: #f190dd;
  --color-tvt11-ring: oklch(0.78 0.15 335);
  --color-tvt11-ok: #5ed99e;
  --color-tvt11-ok: oklch(0.8 0.14 160);
}
```
