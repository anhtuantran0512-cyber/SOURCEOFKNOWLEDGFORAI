---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-faq-accordion-details-summary/"
title: "Tailwind CSS FAQ Accordion with Details and Summary"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "The pricing-page FAQ every SaaS ships, rebuilt as a two-column Tailwind UI section: heading, intro and a contact card on the left, a ringed card of native…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS FAQ Accordion with Details and Summary
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-faq-accordion-details-summary/

The pricing-page FAQ every SaaS ships, rebuilt as a two-column Tailwind UI section: heading, intro and a contact card on the left, a ringed card of native <details> questions on the right. The answers animate open and closed with v4's details-content: variant plus [interpolate-size:allow-keywords], the plus icon spins into a cross, and an indigo rail draws down the open item.
## HTML
```html
<section class="tac-01 w-full min-h-svh grid place-items-center bg-tac01-bg bg-[radial-gradient(80%_60%_at_15%_0%,var(--color-tac01-glow),transparent_70%)] px-5 py-14 font-tac01-sans text-tac01-ink [interpolate-size:allow-keywords] sm:px-8" aria-label="Tailwind FAQ accordion demo">
  <div class="grid w-full max-w-6xl justify-items-center gap-10">
    <div class="grid w-full gap-10 lg:grid-cols-[minmax(0,5fr)_minmax(0,7fr)] lg:gap-14">
      <div class="flex flex-col gap-7 lg:sticky lg:top-10 lg:self-start">
        <div>
          <p class="inline-flex items-center gap-2 rounded-full bg-tac01-card px-3 py-1.5 text-xs font-semibold text-tac01-acc-ink shadow-[0_1px_2px_oklch(0.3_0.05_277/0.08)] ring-1 ring-tac01-acc/15"><span aria-hidden="true" class="size-1.5 rounded-full bg-tac01-acc"></span>Pricing FAQ</p>
          <h2 class="mt-5 text-[clamp(30px,4.2vw,44px)] leading-[1.08] font-extrabold tracking-[-0.035em] text-balance">Questions before you <span class="font-tac01-serif text-[1.12em] font-normal tracking-[-0.01em] text-tac01-acc italic">upgrade?</span></h2>
          <p class="mt-4 max-w-md text-[15.5px] leading-relaxed text-tac01-mut text-pretty">Everything about billing, seats and trials in one place. Every plan includes unlimited projects, SSO-ready auth and a 14-day free trial.</p>
        </div>
        <div class="relative overflow-hidden rounded-2xl bg-tac01-card p-6 shadow-[0_1px_2px_oklch(0.3_0.05_277/0.06),0_18px_40px_-24px_oklch(0.3_0.08_277/0.35)] ring-1 ring-tac01-ink/6">
          <span aria-hidden="true" class="pointer-events-none absolute -top-16 -right-12 size-40 rounded-full bg-tac01-acc/10 blur-2xl"></span>
          <div aria-hidden="true" class="flex -space-x-2.5">
            <span class="grid size-10 place-items-center rounded-full bg-linear-to-br from-[#f6b38e] to-[#d9715a] text-[13px] font-bold text-white ring-[3px] ring-tac01-card">MR</span>
            <span class="grid size-10 place-items-center rounded-full bg-linear-to-br from-[#8fb6ff] to-[#4f63e5] text-[13px] font-bold text-white ring-[3px] ring-tac01-card">AK</span>
            <span class="grid size-10 place-items-center rounded-full bg-linear-to-br from-[#7fdcc0] to-[#2f9c83] text-[13px] font-bold text-white ring-[3px] ring-tac01-card">JL</span>
          </div>
          <h3 class="mt-4 text-[17px] font-bold tracking-[-0.01em]">Still have a question?</h3>
          <p class="mt-1.5 text-sm leading-relaxed text-tac01-mut">Talk to a real person on our billing team. Median first reply: <strong class="font-semibold text-tac01-ink">1>1 h 42 min<nbsp;h>1 h 42 min<nbsp;42>1 h 42 min<nbsp;min</strong>.</p>
          <div class="mt-5 flex flex-wrap gap-2.5">
            <a href="#" class="inline-flex min-h-11 items-center gap-2 rounded-xl bg-tac01-ink px-4.5 text-sm font-semibold text-white shadow-[inset_0_1px_0_oklch(1_0_0/0.15),0_6px_16px_-6px_oklch(0.22_0.04_277/0.6)] transition hover:bg-tac01-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac01-acc motion-reduce:transition-none">Contact sales<svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="M3 8h9M8.5 4.5 12 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
            <a href="#" class="inline-flex min-h-11 items-center rounded-xl px-4 text-sm font-semibold text-tac01-ink ring-1 ring-tac01-ink/12 transition hover:bg-tac01-soft focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac01-acc motion-reduce:transition-none">Read the docs</a>
          </div>
        </div>
      </div>
      <div class="divide-y divide-tac01-line overflow-hidden rounded-3xl bg-tac01-card shadow-[0_1px_2px_oklch(0.3_0.05_277/0.06),0_30px_70px_-40px_oklch(0.3_0.08_277/0.45)] ring-1 ring-tac01-ink/6">
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Can I switch plans or cancel at any time?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>Yes. Upgrades take effect immediately and we prorate the difference to the day. Downgrades and cancellations apply at the end of your billing period, and you keep full access until then &mdash; no exit fees, no retention calls.</p>
          </div>
        </details>
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">What counts as a seat?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>A seat is any member who can edit. Viewers, guests and API tokens are always free, so you only pay for the people actually building &mdash; most teams of 20 need fewer than 8 seats.</p>
          </div>
        </details>
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">What happens when my free trial ends?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>Nothing breaks. If you haven't added a card, your workspace drops to the Free plan: projects stay intact and read-only beyond the free limits, and you can upgrade later to pick up exactly where you left off.</p>
          </div>
        </details>
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Do you offer discounts for startups or nonprofits?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>Startups under two years old with less than $5M raised get <strong class="font-semibold text-tac01-ink">50% off Pro for the first year</strong>. Registered nonprofits and schools get 30% off any plan, permanently. Apply from <span class="rounded-md bg-tac01-soft px-1.5 py-0.5 font-tac01-mono text-[13px] text-tac01-acc-ink">Settings → Billing</span>.</p>
          </div>
        </details>
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Can we pay by invoice instead of card?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>Annual Business and Enterprise plans can be billed by invoice with net-30 terms, in USD, GBP, EUR, CAD or AUD. We also support purchase orders and vendor-onboarding forms.</p>
          </div>
        </details>
        <details class="group relative before:absolute before:inset-y-5 before:left-0 before:w-[3px] before:origin-top before:scale-y-0 before:rounded-r-full before:bg-tac01-acc before:transition-transform before:duration-500 open:before:scale-y-100 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:transition-discrete open:details-content:h-auto motion-reduce:before:transition-none motion-reduce:details-content:transition-none">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 px-6 py-5 text-[16.5px] font-semibold tracking-[-0.01em] transition-colors outline-none hover:text-tac01-acc-ink group-open:text-tac01-acc-ink focus-visible:bg-tac01-soft focus-visible:ring-2 focus-visible:ring-tac01-acc focus-visible:ring-inset sm:px-8 [&::-webkit-details-marker]:hidden">
            <span class="flex-1">Is our data encrypted and where is it stored?</span>
            <span aria-hidden="true" class="grid size-8 flex-none place-items-center rounded-full bg-tac01-soft text-tac01-acc-ink ring-1 ring-tac01-acc/15 transition duration-300 group-open:rotate-45 group-open:bg-tac01-acc group-open:text-white motion-reduce:transition-none"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 3v10M3 8h10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          </summary>
          <div class="px-6 pb-6 text-[15px] leading-[1.7] text-tac01-mut group-open:animate-tac01-in motion-reduce:animate-none sm:px-8 sm:pe-20">
            <p>All data is encrypted with AES-256 at rest and TLS 1.3 in transit. Choose US or EU residency when you create a workspace; we're SOC 2 Type II audited and GDPR-ready, with a DPA available on request.</p>
          </div>
        </details>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full bg-tac01-card/70 px-3.5 py-2 text-center font-tac01-mono text-[11.5px] text-tac01-mut ring-1 ring-tac01-ink/8">details-content:h-0 · open:details-content:h-auto · [interpolate-size:allow-keywords]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac01-bg: #f5f6fb;
  --color-tac01-bg: oklch(0.973 0.007 275);
  --color-tac01-glow: #e3e5ff;
  --color-tac01-glow: oklch(0.925 0.04 278);
  --color-tac01-card: #ffffff;
  --color-tac01-card: oklch(1 0 0);
  --color-tac01-soft: #eef0ff;
  --color-tac01-soft: oklch(0.955 0.022 278);
  --color-tac01-line: #e8eaf2;
  --color-tac01-line: oklch(0.935 0.01 275);
  --color-tac01-ink: #141a2e;
  --color-tac01-ink: oklch(0.22 0.035 272);
  --color-tac01-mut: #535a70;
  --color-tac01-mut: oklch(0.46 0.03 272);
  --color-tac01-acc: #5046e6;
  --color-tac01-acc: oklch(0.52 0.23 277);
  --color-tac01-acc-ink: #4338ca;
  --color-tac01-acc-ink: oklch(0.46 0.21 277);
  --font-tac01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tac01-serif: 'Instrument Serif', Georgia, serif;
  --font-tac01-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tac01-in: tac01-in 0.5s cubic-bezier(0.2, 0.7, 0.2, 1) both;

  @keyframes tac01-in {
    from {
      opacity: 0;
      transform: translateY(-6px);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-01 {
  width: 100%;
  min-height: 100svh;
}
```
