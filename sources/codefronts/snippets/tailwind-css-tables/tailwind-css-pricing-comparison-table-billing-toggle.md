---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/tailwind-css-pricing-comparison-table-billing-toggle/"
title: "Tailwind CSS Pricing Comparison Table with Billing Toggle"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "A three-tier SaaS feature matrix with a lifted, glowing Pro column — upgraded with a working monthly / yearly billing toggle in zero JavaScript."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pricing Comparison Table with Billing Toggle
Source: https://codefronts.com/snippets/tailwind-css-tables/tailwind-css-pricing-comparison-table-billing-toggle/

A three-tier SaaS feature matrix with a lifted, glowing Pro column — upgraded with a working monthly / yearly billing toggle in zero JavaScript. Two radio inputs drive every price on the table through group-has-[#ttb02-yearly:checked]/pricing:, and feature rows are grouped under section headings so the matrix scans like Stripe's, not like a spreadsheet.
## HTML
```html
<section class="ttb-02 grid-cols-1 group/pricing w-full min-h-svh grid place-items-center bg-ttb02-bg bg-[radial-gradient(70%_50%_at_60%_0%,var(--color-ttb02-glow),transparent_70%)] px-5 py-14 font-ttb02-sans text-ttb02-ink" aria-label="SaaS pricing comparison table demo">
  <div class="w-full max-w-4xl">
    <header class="mb-10 grid justify-items-center gap-4 text-center">
      <span class="rounded-full border border-ttb02-pro/30 bg-ttb02-pro/10 px-3.5 py-1 font-ttb02-mono text-[11px] font-medium tracking-[0.18em] text-ttb02-pro-ink uppercase">Pricing</span>
      <h2 class="text-[clamp(28px,4vw,40px)] leading-tight font-bold tracking-[-0.03em] text-balance">Choose your power level</h2>
      <p class="max-w-md text-[15px] text-ttb02-mut text-pretty">Scale from indie hacker to enterprise without friction. Switch plans anytime.</p>
      <fieldset class="mt-2 inline-flex rounded-full bg-white/6 p-1 ring-1 ring-white/10">
        <legend class="sr-only">Billing period</legend>
        <label class="flex min-h-11 cursor-pointer items-center rounded-full px-5 text-sm font-semibold text-ttb02-mut transition has-checked:bg-white has-checked:text-ttb02-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb02-pro">
          <input class="sr-only" type="radio" name="ttb02-billing" id="ttb02-monthly" checked>Monthly
        </label>
        <label class="flex min-h-11 cursor-pointer items-center gap-2 rounded-full px-5 text-sm font-semibold text-ttb02-mut transition has-checked:bg-white has-checked:text-ttb02-bg has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ttb02-pro">
          <input class="sr-only" type="radio" name="ttb02-billing" id="ttb02-yearly">Yearly
          <span class="rounded-full bg-emerald-400/15 px-2 py-0.5 text-[11px] font-bold text-emerald-300">−20%</span>
        </label>
      </fieldset>
    </header>
    <div class="relative overflow-x-auto pt-4">
      <table class="w-full min-w-[640px] border-separate border-spacing-0 text-left text-sm">
        <caption class="sr-only">Feature comparison of Basic, Pro and Enterprise plans</caption>
        <colgroup><col class="w-[34%]"><col class="w-[22%]"><col class="w-[22%]"><col class="w-[22%]"></colgroup>
        <thead>
          <tr class="align-top">
            <td></td>
            <th scope="col" class="px-5 pt-6 pb-6">
              <div class="text-base font-semibold text-ttb02-basic">Basic</div>
              <div class="mt-2 flex items-baseline gap-1"><span class="text-[32px] font-bold tracking-tight tabular-nums"><span class="group-has-[#ttb02-yearly:checked]/pricing:hidden">$9</span><span class="hidden group-has-[#ttb02-yearly:checked]/pricing:inline">$7</span></span><span class="text-ttb02-mut">/mo</span></div>
              <p class="mt-1 text-xs font-normal text-ttb02-mut"><span class="group-has-[#ttb02-yearly:checked]/pricing:hidden">Billed monthly</span><span class="hidden group-has-[#ttb02-yearly:checked]/pricing:inline">$84 billed yearly</span></p>
            </th>
            <th scope="col" class="relative rounded-t-2xl bg-linear-to-b from-ttb02-pro/20 to-ttb02-pro/6 px-5 pt-6 pb-6 shadow-[0_-12px_40px_-12px_var(--color-ttb02-pro)] ring-1 ring-ttb02-pro/50 ring-inset">
              <span class="absolute -top-3 left-5 rounded-full bg-linear-to-r from-ttb02-pro to-ttb02-pro2 px-2.5 py-1 text-[10px] font-bold tracking-[0.14em] text-white uppercase shadow-[0_6px_20px_-4px_var(--color-ttb02-pro)]">Most popular</span>
              <div class="text-base font-semibold text-ttb02-pro-ink">Pro</div>
              <div class="mt-2 flex items-baseline gap-1"><span class="text-[32px] font-bold tracking-tight tabular-nums"><span class="group-has-[#ttb02-yearly:checked]/pricing:hidden">$29</span><span class="hidden group-has-[#ttb02-yearly:checked]/pricing:inline">$23</span></span><span class="text-ttb02-mut">/mo</span></div>
              <p class="mt-1 text-xs font-normal text-ttb02-mut"><span class="group-has-[#ttb02-yearly:checked]/pricing:hidden">Billed monthly</span><span class="hidden group-has-[#ttb02-yearly:checked]/pricing:inline">$276 billed yearly</span></p>
            </th>
            <th scope="col" class="px-5 pt-6 pb-6">
              <div class="text-base font-semibold text-ttb02-ent">Enterprise</div>
              <div class="mt-2 text-[32px] font-bold tracking-tight">Custom</div>
              <p class="mt-1 text-xs font-normal text-ttb02-mut">Volume pricing &amp; SSO</p>
            </th>
          </tr>
        </thead>
        <tbody class="[&_td]:border-b [&_td]:border-ttb02-line [&_td]:px-5 [&_td]:py-3.5 [&_th]:border-b [&_th]:border-ttb02-line [&_td:nth-child(3)]:border-x [&_td:nth-child(3)]:border-x-ttb02-pro/30 [&_td:nth-child(3)]:bg-ttb02-pro/6 [&_tr:hover_td]:bg-white/[0.025] [&_tr:hover_td:nth-child(3)]:bg-ttb02-pro/10">
          <tr><th scope="colgroup" colspan="4" class="px-5 pt-6 pb-2.5 text-left font-ttb02-mono text-[11px] font-medium tracking-[0.16em] text-ttb02-mut uppercase">Usage</th></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">AI requests / month</th><td class="tabular-nums">500</td><td class="font-semibold text-ttb02-pro-ink tabular-nums">10,000</td><td>Unlimited</td></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">Team seats</th><td>1</td><td class="font-semibold text-ttb02-pro-ink">Up to 10</td><td>Unlimited</td></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">Analytics dashboard</th><td>Basic</td><td class="font-semibold text-ttb02-pro-ink">Advanced</td><td>Custom</td></tr>
          <tr><th scope="colgroup" colspan="4" class="px-5 pt-7 pb-2.5 text-left font-ttb02-mono text-[11px] font-medium tracking-[0.16em] text-ttb02-mut uppercase">Platform &amp; support</th></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">Custom integrations</th><td><span aria-hidden="true" class="text-ttb02-dim">—</span><span class="sr-only">Not included</span></td><td><svg class="size-5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Included</span></td><td><svg class="size-5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Included</span></td></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">Priority support</th><td><span aria-hidden="true" class="text-ttb02-dim">—</span><span class="sr-only">Not included</span></td><td><svg class="size-5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Included</span></td><td><svg class="size-5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg><span class="sr-only">Included</span></td></tr>
          <tr><th scope="row" class="px-5 py-3.5 font-medium text-ttb02-mut">SLA guarantee</th><td><span aria-hidden="true" class="text-ttb02-dim">—</span><span class="sr-only">Not included</span></td><td><span aria-hidden="true" class="text-ttb02-dim">—</span><span class="sr-only">Not included</span></td><td class="font-semibold text-emerald-300">99.99% uptime</td></tr>
          <tr class="[&_td]:border-b-0 [&_td]:pt-6 [&_td]:pb-7 [&_td]:bg-transparent!">
            <td></td>
            <td><a href="#" class="flex min-h-11 items-center justify-center rounded-xl text-sm font-semibold text-ttb02-basic ring-1 ring-ttb02-basic/40 transition ring-inset hover:bg-ttb02-basic hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb02-basic">Start free</a></td>
            <td class="rounded-b-2xl border-b! border-ttb02-pro/30! bg-ttb02-pro/6!"><a href="#" class="flex min-h-11 items-center justify-center gap-1.5 rounded-xl bg-linear-to-r from-ttb02-pro to-ttb02-pro2 text-sm font-semibold text-white shadow-[0_8px_24px_-8px_var(--color-ttb02-pro)] transition hover:-translate-y-px hover:shadow-[0_12px_30px_-8px_var(--color-ttb02-pro)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb02-pro2 motion-reduce:transition-none">Get Pro <span aria-hidden="true">→</span></a></td>
            <td><a href="#" class="flex min-h-11 items-center justify-center rounded-xl text-sm font-semibold text-ttb02-ent ring-1 ring-ttb02-ent/40 transition ring-inset hover:bg-ttb02-ent hover:text-ttb02-bg focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttb02-ent">Contact sales</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb02-bg: #07070f;
  --color-ttb02-bg: oklch(0.12 0.015 285);
  --color-ttb02-glow: #2b1a4d;
  --color-ttb02-glow: oklch(0.26 0.09 300 / 0.75);
  --color-ttb02-line: #1f1f36;
  --color-ttb02-line: oklch(0.25 0.035 285);
  --color-ttb02-ink: #ececfb;
  --color-ttb02-ink: oklch(0.94 0.015 285);
  --color-ttb02-mut: #a1a1bd;
  --color-ttb02-mut: oklch(0.73 0.03 285);
  --color-ttb02-dim: #55556e;
  --color-ttb02-dim: oklch(0.46 0.03 285);
  --color-ttb02-pro: #a855f7;
  --color-ttb02-pro: oklch(0.63 0.25 304);
  --color-ttb02-pro-ink: #d4b2ff;
  --color-ttb02-pro-ink: oklch(0.82 0.11 304);
  --color-ttb02-pro2: #06b6d4;
  --color-ttb02-pro2: oklch(0.72 0.13 215);
  --color-ttb02-basic: #60a5fa;
  --color-ttb02-basic: oklch(0.71 0.14 255);
  --color-ttb02-ent: #f5b041;
  --color-ttb02-ent: oklch(0.8 0.14 75);
  --font-ttb02-sans: 'Geist', system-ui, sans-serif;
  --font-ttb02-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-02 {
  width: 100%;
  min-height: 100svh;
}
```
