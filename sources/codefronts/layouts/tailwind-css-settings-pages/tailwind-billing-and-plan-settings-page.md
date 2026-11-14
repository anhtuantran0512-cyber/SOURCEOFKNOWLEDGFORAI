---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-billing-and-plan-settings-page/"
title: "Tailwind Billing and Plan Settings Page"
section: "layouts"
category: "tailwind-css-settings-pages"
category_name: "Tailwind CSS Settings Pages"
description: "A zero-JavaScript billing page: a dark current-plan card with seat maths and a billing-period bar, a Monthly / Annual segmented toggle whose thumb slides…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Billing and Plan Settings Page
Source: https://codefronts.com/layouts/tailwind-css-settings-pages/tailwind-billing-and-plan-settings-page/

A zero-JavaScript billing page: a dark current-plan card with seat maths and a billing-period bar, a Monthly / Annual segmented toggle whose thumb slides under the active option, three selectable plan cards whose prices swap with the cycle, and a change summary that rewrites itself for every plan × cycle combination.
## HTML
```html
<section class="tsp-02 group/bill w-full min-h-svh bg-tsp02-bg px-4 py-10 font-tsp02-sans text-tsp02-ink antialiased sm:px-8 sm:py-14" aria-labelledby="tsp-02-h">
  <form class="mx-auto grid w-full max-w-5xl gap-8">
    <header class="flex flex-wrap items-end justify-between gap-4">
      <div><h1 id="tsp-02-h" class="text-3xl font-extrabold tracking-tight">Billing &amp; plan</h1><p class="mt-1 text-tsp02-mut">Change plans any time. Upgrades apply now; downgrades at renewal.</p></div>
      <fieldset class="relative grid w-fit grid-cols-2 rounded-full border border-tsp02-line bg-white p-1 shadow-xs">
        <legend class="sr-only">Billing cycle</legend>
        <span aria-hidden="true" class="absolute inset-y-1 left-1 w-[calc(50%-0.25rem)] rounded-full bg-tsp02-ink shadow-md transition-transform duration-300 ease-out group-has-[#tsp-02-year:checked]/bill:translate-x-full motion-reduce:transition-none"></span>
        <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center rounded-full px-5 text-sm font-bold text-tsp02-mut transition has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp02-acc"><input type="radio" name="tsp-02-cycle" id="tsp-02-month" class="sr-only" checked>Monthly</label>
        <label class="relative z-10 flex min-h-11 cursor-pointer items-center justify-center gap-2 rounded-full px-5 text-sm font-bold text-tsp02-mut transition has-checked:text-white has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tsp02-acc"><input type="radio" name="tsp-02-cycle" id="tsp-02-year" class="sr-only">Annual<span class="rounded-full bg-emerald-400/20 px-2 py-0.5 text-[11px] font-extrabold text-emerald-600 group-has-[#tsp-02-year:checked]/bill:text-emerald-300">−20%</span></label>
      </fieldset>
    </header>

    <div class="relative overflow-hidden rounded-3xl bg-tsp02-ink p-6 text-white shadow-[0_30px_60px_-30px_rgb(15_23_42/0.6)] sm:p-8">
      <div aria-hidden="true" class="pointer-events-none absolute -right-20 -top-28 size-80 rounded-full bg-tsp02-acc/45 blur-3xl"></div>
      <div aria-hidden="true" class="pointer-events-none absolute -bottom-32 left-1/3 size-72 rounded-full bg-tsp02-acc2/25 blur-3xl"></div>
      <div class="relative grid gap-6 md:grid-cols-[minmax(0,1fr)_auto] md:items-end">
        <div>
          <p class="inline-flex items-center gap-2 rounded-full bg-white/10 px-2.5 py-1 text-xs font-bold ring-1 ring-white/15"><span class="size-1.5 rounded-full bg-emerald-400"></span>Current plan</p>
          <h2 class="mt-4 text-3xl font-extrabold tracking-tight">Pro · Monthly</h2>
          <p class="mt-1 text-white/70">12 seats × $24 = <strong class="text-white">$288 / month</strong> · renews Oct 30, 2026</p>
        </div>
        <dl class="grid grid-cols-[auto_auto] gap-x-8 gap-y-1.5 text-sm">
          <dt class="text-white/60">Next invoice</dt><dd class="text-right font-bold tabular-nums">$288.00</dd>
          <dt class="text-white/60">Payment</dt><dd class="text-right font-bold">Visa •• 4242</dd>
          <dt class="text-white/60">Seats used</dt><dd class="text-right font-bold tabular-nums">9 / 12</dd>
        </dl>
      </div>
      <div class="relative mt-7">
        <div class="flex justify-between text-xs font-semibold text-white/60"><span>Oct 1</span><span class="text-white">Day 18 of 30</span><span>Oct 30</span></div>
        <div class="mt-2 h-1.5 rounded-full bg-white/10"><div class="h-full w-[60%] rounded-full bg-linear-to-r from-tsp02-acc to-tsp02-acc2"></div></div>
      </div>
    </div>

    <fieldset class="grid gap-4 md:grid-cols-3">
      <legend class="mb-4 text-lg font-extrabold tracking-tight">Choose a plan</legend>
      <label class="group/plan relative grid cursor-pointer content-start gap-4 rounded-3xl border border-tsp02-line bg-white p-6 shadow-xs transition hover:-translate-y-0.5 hover:border-tsp02-acc/40 has-checked:border-transparent has-checked:ring-2 has-checked:ring-tsp02-acc has-checked:shadow-[0_24px_50px_-28px_var(--color-tsp02-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp02-acc motion-reduce:transition-none">
        <input type="radio" name="tsp-02-plan" id="tsp-02-p-starter" class="sr-only">
        <span class="flex items-center justify-between"><span class="font-extrabold">Starter</span><span class="grid size-5 place-items-center rounded-full border-2 border-tsp02-line transition group-has-checked/plan:border-tsp02-acc group-has-checked/plan:bg-tsp02-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/plan:opacity-100"></span></span></span>
        <span class="flex items-baseline gap-1"><span class="text-4xl font-extrabold tracking-tight tabular-nums"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">$12</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$10</span></span><span class="text-sm text-tsp02-mut">/ seat / mo</span></span>
        <span class="text-xs font-semibold text-tsp02-mut"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">Billed monthly</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$120 per seat, billed yearly</span></span>
        <span class="grid gap-2 border-t border-tsp02-line pt-4 text-sm text-tsp02-mut"><span>Up to 5 projects</span><span>Community support</span><span>7-day history</span></span>
      </label>
      <label class="group/plan relative grid cursor-pointer content-start gap-4 rounded-3xl border border-tsp02-line bg-white p-6 shadow-xs transition hover:-translate-y-0.5 hover:border-tsp02-acc/40 has-checked:border-transparent has-checked:ring-2 has-checked:ring-tsp02-acc has-checked:shadow-[0_24px_50px_-28px_var(--color-tsp02-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp02-acc motion-reduce:transition-none">
        <input type="radio" name="tsp-02-plan" id="tsp-02-p-pro" class="sr-only" checked>
        <span class="flex items-center justify-between"><span class="flex items-center gap-2 font-extrabold">Pro <span class="rounded-full bg-tsp02-acc/10 px-2 py-0.5 text-[11px] font-bold text-tsp02-acc">Current</span></span><span class="grid size-5 place-items-center rounded-full border-2 border-tsp02-line transition group-has-checked/plan:border-tsp02-acc group-has-checked/plan:bg-tsp02-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/plan:opacity-100"></span></span></span>
        <span class="flex items-baseline gap-1"><span class="text-4xl font-extrabold tracking-tight tabular-nums"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">$24</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$19</span></span><span class="text-sm text-tsp02-mut">/ seat / mo</span></span>
        <span class="text-xs font-semibold text-tsp02-mut"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">Billed monthly</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$228 per seat, billed yearly</span></span>
        <span class="grid gap-2 border-t border-tsp02-line pt-4 text-sm text-tsp02-mut"><span>Unlimited projects</span><span>Priority email support</span><span>90-day history &amp; SSO</span></span>
      </label>
      <label class="group/plan relative grid cursor-pointer content-start gap-4 rounded-3xl border border-tsp02-line bg-white p-6 shadow-xs transition hover:-translate-y-0.5 hover:border-tsp02-acc/40 has-checked:border-transparent has-checked:ring-2 has-checked:ring-tsp02-acc has-checked:shadow-[0_24px_50px_-28px_var(--color-tsp02-acc)] has-focus-visible:outline-2 has-focus-visible:outline-offset-4 has-focus-visible:outline-tsp02-acc motion-reduce:transition-none">
        <input type="radio" name="tsp-02-plan" id="tsp-02-p-business" class="sr-only">
        <span class="flex items-center justify-between"><span class="flex items-center gap-2 font-extrabold">Business <span class="rounded-full bg-amber-100 px-2 py-0.5 text-[11px] font-bold text-amber-700">Popular</span></span><span class="grid size-5 place-items-center rounded-full border-2 border-tsp02-line transition group-has-checked/plan:border-tsp02-acc group-has-checked/plan:bg-tsp02-acc"><span class="size-1.5 rounded-full bg-white opacity-0 group-has-checked/plan:opacity-100"></span></span></span>
        <span class="flex items-baseline gap-1"><span class="text-4xl font-extrabold tracking-tight tabular-nums"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">$39</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$31</span></span><span class="text-sm text-tsp02-mut">/ seat / mo</span></span>
        <span class="text-xs font-semibold text-tsp02-mut"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">Billed monthly</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">$372 per seat, billed yearly</span></span>
        <span class="grid gap-2 border-t border-tsp02-line pt-4 text-sm text-tsp02-mut"><span>Everything in Pro</span><span>SAML, SCIM &amp; audit log</span><span>Dedicated success manager</span></span>
      </label>
    </fieldset>

    <div class="sticky bottom-4 flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-tsp02-line bg-white/90 p-4 shadow-[0_20px_40px_-24px_rgb(15_23_42/0.35)] backdrop-blur sm:p-5" aria-live="polite">
      <div class="grid gap-0.5">
        <p class="text-sm font-extrabold">
          <span class="hidden group-has-[#tsp-02-p-starter:checked]/bill:inline">Downgrade to Starter</span>
          <span class="hidden group-has-[#tsp-02-p-pro:checked]/bill:inline"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">This is your current plan</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">Switch Pro to annual billing</span></span>
          <span class="hidden group-has-[#tsp-02-p-business:checked]/bill:inline">Upgrade to Business</span>
          <span class="ml-2 hidden rounded-full bg-emerald-100 px-2 py-0.5 text-[11px] font-bold text-emerald-700 group-has-[#tsp-02-year:checked]/bill:inline">You save 20%</span>
        </p>
        <p class="text-sm tabular-nums text-tsp02-mut">
          <span class="hidden group-has-[#tsp-02-p-starter:checked]/bill:inline"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">12 seats × $12 = $144 / month · from Oct 30</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">12 seats × $120 = $1,440 / year · from Oct 30</span></span>
          <span class="hidden group-has-[#tsp-02-p-pro:checked]/bill:inline"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">12 seats × $24 = $288 / month</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">12 seats × $228 = $2,736 / year · credit of $115.20 applied</span></span>
          <span class="hidden group-has-[#tsp-02-p-business:checked]/bill:inline"><span class="group-has-[#tsp-02-year:checked]/bill:hidden">12 seats × $39 = $468 / month · $72.00 prorated today</span><span class="hidden group-has-[#tsp-02-year:checked]/bill:inline">12 seats × $372 = $4,464 / year · credit of $115.20 applied</span></span>
        </p>
      </div>
      <button type="button" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tsp02-ink px-5 text-sm font-bold text-white shadow-sm transition hover:bg-tsp02-ink/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tsp02-acc group-has-[#tsp-02-p-pro:checked]/bill:group-has-[#tsp-02-month:checked]/bill:pointer-events-none group-has-[#tsp-02-p-pro:checked]/bill:group-has-[#tsp-02-month:checked]/bill:opacity-40">Confirm change<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </div>
  </form>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tsp02-bg: #f5f6f8;
  --color-tsp02-bg: oklch(0.972 0.004 265);
  --color-tsp02-ink: #111827;
  --color-tsp02-ink: oklch(0.21 0.032 265);
  --color-tsp02-mut: #5b6475;
  --color-tsp02-mut: oklch(0.5 0.03 262);
  --color-tsp02-line: #e3e6ec;
  --color-tsp02-line: oklch(0.92 0.009 262);
  --color-tsp02-acc: #2563eb;
  --color-tsp02-acc: oklch(0.546 0.215 263);
  --color-tsp02-acc2: #06b6d4;
  --color-tsp02-acc2: oklch(0.715 0.126 215);
  --font-tsp02-sans: 'Manrope', system-ui, sans-serif;
}

.tsp-02 {
  width: 100%;
  min-height: 100svh;
}
```
