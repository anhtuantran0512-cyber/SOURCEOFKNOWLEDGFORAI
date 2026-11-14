---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-pricing-table-monthly-annual-toggle/"
title: "Tailwind CSS Pricing Table with Monthly / Annual Toggle"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "The single most-copied SaaS pattern, ported whole into utilities: a pill switch flips every price on a three-card grid between monthly and discounted annual…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Pricing Table with Monthly / Annual Toggle
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-css-pricing-table-monthly-annual-toggle/

The single most-copied SaaS pattern, ported whole into utilities: a pill switch flips every price on a three-card grid between monthly and discounted annual billing with a vertical roll. The state machine is one role="switch" checkbox read by group-has-checked/p: on every element that changes.
## HTML
```html
<section class="tpt-01 group/p w-full min-h-svh grid place-items-center bg-tpt01-bg bg-[radial-gradient(90%_60%_at_50%_0%,var(--color-tpt01-glow),transparent_70%)] px-5 py-16 font-tpt01-sans text-tpt01-ink antialiased" aria-label="Pricing table with monthly and annual billing toggle">
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <header class="grid justify-items-center gap-5 text-center">
      <h2 class="text-[clamp(28px,4.2vw,44px)] font-extrabold tracking-[-0.03em] text-balance">Simple, honest pricing</h2>
      <div class="flex flex-wrap items-center justify-center gap-3 text-sm font-semibold">
        <span aria-hidden="true" class="text-tpt01-ink transition-colors group-has-checked/p:text-tpt01-mut">Monthly</span>
        <input type="checkbox" id="tpt01-bill" role="switch" class="peer sr-only" aria-label="Bill annually and save 20%">
        <label for="tpt01-bill" aria-hidden="true" class="relative h-7 w-13 cursor-pointer rounded-full bg-tpt01-line transition-colors duration-300 peer-checked:bg-tpt01-acc peer-focus-visible:outline-3 peer-focus-visible:outline-offset-3 peer-focus-visible:outline-tpt01-acc">
          <span class="absolute top-[3px] left-[3px] size-[22px] rounded-full bg-white shadow-[0_2px_6px_oklch(0.2_0.03_265/0.25)] transition-transform duration-300 ease-[cubic-bezier(.5,1.6,.4,1)] group-has-checked/p:translate-x-6"></span>
        </label>
        <span aria-hidden="true" class="text-tpt01-mut transition-colors group-has-checked/p:text-tpt01-ink">Annual</span>
        <span class="rounded-full border border-tpt01-save-ink/30 px-2.5 py-1 text-[11px] font-bold tracking-[0.06em] text-tpt01-save-ink uppercase transition duration-300 group-has-checked/p:border-transparent group-has-checked/p:bg-tpt01-save-bg">Save 20%</span>
      </div>
    </header>
    <div class="grid w-full gap-5 md:grid-cols-3 md:items-stretch">
      <article class="flex flex-col gap-5 rounded-2xl border border-tpt01-line bg-white p-7 shadow-[0_1px_2px_oklch(0.2_0.03_265/0.05)]">
        <div>
          <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt01-mut uppercase">Starter</h3>
          <p class="mt-1 text-sm text-tpt01-body">For side projects and first launches.</p>
        </div>
        <div class="grid h-[76px] overflow-hidden">
          <p class="col-start-1 row-start-1 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:invisible group-has-checked/p:-translate-y-full group-has-checked/p:opacity-0"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$12</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">billed monthly</span></p>
          <p class="invisible col-start-1 row-start-1 translate-y-full opacity-0 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:visible group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$9</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">$108 billed yearly</span></p>
        </div>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt01-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt01-acc *:before:content-['✓']">
          <li>3 projects</li><li>2 GB storage</li><li>Community support</li>
        </ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt01-line text-sm font-bold text-tpt01-ink no-underline transition-colors hover:border-tpt01-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt01-acc">Start free</a>
      </article>
      <article class="relative flex flex-col gap-5 rounded-2xl bg-white p-7 shadow-[0_24px_50px_-24px_oklch(0.55_0.2_264/0.55)] ring-2 ring-tpt01-acc">
        <span class="absolute -top-3 left-7 rounded-full bg-tpt01-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase">Most popular</span>
        <div>
          <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt01-acc-ink uppercase">Pro</h3>
          <p class="mt-1 text-sm text-tpt01-body">For growing products and small teams.</p>
        </div>
        <div class="grid h-[76px] overflow-hidden">
          <p class="col-start-1 row-start-1 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:invisible group-has-checked/p:-translate-y-full group-has-checked/p:opacity-0"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$29</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">billed monthly</span></p>
          <p class="invisible col-start-1 row-start-1 translate-y-full opacity-0 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:visible group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$23</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">$276 billed yearly</span></p>
        </div>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt01-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt01-acc *:before:content-['✓']">
          <li>Unlimited projects</li><li>200 GB storage</li><li>Priority support</li><li>API access</li>
        </ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt01-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt01-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt01-acc">Choose Pro</a>
      </article>
      <article class="flex flex-col gap-5 rounded-2xl border border-tpt01-line bg-white p-7 shadow-[0_1px_2px_oklch(0.2_0.03_265/0.05)]">
        <div>
          <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt01-mut uppercase">Team</h3>
          <p class="mt-1 text-sm text-tpt01-body">For organisations with security needs.</p>
        </div>
        <div class="grid h-[76px] overflow-hidden">
          <p class="col-start-1 row-start-1 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:invisible group-has-checked/p:-translate-y-full group-has-checked/p:opacity-0"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$79</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">billed monthly</span></p>
          <p class="invisible col-start-1 row-start-1 translate-y-full opacity-0 transition duration-500 ease-[cubic-bezier(.6,0,.2,1)] group-has-checked/p:visible group-has-checked/p:translate-y-0 group-has-checked/p:opacity-100"><span class="text-[44px] leading-[52px] font-extrabold tracking-[-0.035em]">$63</span><span class="text-[15px] font-semibold text-tpt01-mut">/mo</span><span class="block text-xs text-tpt01-mut">$756 billed yearly</span></p>
        </div>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt01-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt01-acc *:before:content-['✓']">
          <li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Dedicated success manager</li>
        </ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt01-line text-sm font-bold text-tpt01-ink no-underline transition-colors hover:border-tpt01-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt01-acc">Contact sales</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt01-line bg-white/70 px-3.5 py-2 font-tpt01-mono text-[11.5px] text-tpt01-mut">group-has-checked/p: · peer-checked: · col-start-1 row-start-1</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt01-bg: #f5f6fb;
  --color-tpt01-bg: oklch(0.973 0.007 270);
  --color-tpt01-glow: #e4e7ff;
  --color-tpt01-glow: oklch(0.93 0.035 275);
  --color-tpt01-ink: #171a26;
  --color-tpt01-ink: oklch(0.22 0.025 270);
  --color-tpt01-body: #454b5f;
  --color-tpt01-body: oklch(0.42 0.03 270);
  --color-tpt01-mut: #5a6074;
  --color-tpt01-mut: oklch(0.49 0.03 270);
  --color-tpt01-line: #d8dbe6;
  --color-tpt01-line: oklch(0.89 0.013 270);
  --color-tpt01-acc: #4a5ce8;
  --color-tpt01-acc: oklch(0.55 0.2 268);
  --color-tpt01-acc-ink: #3a47bf;
  --color-tpt01-acc-ink: oklch(0.47 0.19 268);
  --color-tpt01-save-bg: #d9f3df;
  --color-tpt01-save-bg: oklch(0.93 0.05 150);
  --color-tpt01-save-ink: #1f6b37;
  --color-tpt01-save-ink: oklch(0.45 0.12 150);
  --font-tpt01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpt01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-01 {
  width: 100%;
  min-height: 100svh;
}
```
