---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/responsive-tailwind-pricing-table-accordion/"
title: "Responsive Tailwind Pricing Table that Stacks into an Accordion"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "One component, two personalities: wide, it's a three-column comparison; squeezed into a narrow container, each plan collapses into a tappable accordion with…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Tailwind Pricing Table that Stacks into an Accordion
Source: https://codefronts.com/components/tailwind-css-pricing-tables/responsive-tailwind-pricing-table-accordion/

One component, two personalities: wide, it's a three-column comparison; squeezed into a narrow container, each plan collapses into a tappable accordion with price and CTA always visible. It's driven by v4's built-in container variants — @container on the wrapper, @max-[40rem]: on every element that changes — so it adapts in a sidebar, a modal or a phone alike.
## HTML
```html
<section class="tpt-20 w-full min-h-svh grid place-items-center bg-tpt20-bg px-5 py-16 font-tpt20-sans text-tpt20-ink antialiased" aria-label="Responsive pricing that stacks into accordions">
  <div class="@container grid w-full max-w-5xl justify-items-center gap-9">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em] text-balance">Plans that fit any screen</h2>
    <div class="grid w-full grid-cols-3 gap-4 @max-[40rem]:grid-cols-1 @max-[40rem]:gap-3">
      <article class="group/c flex flex-col gap-3 rounded-[20px] border-[1.5px] border-tpt20-line bg-white p-6 @max-[40rem]:has-focus-visible:outline-3 @max-[40rem]:has-focus-visible:outline-offset-2 @max-[40rem]:has-focus-visible:outline-tpt20-acc">
        <input type="checkbox" id="tpt20-a" class="sr-only @min-[40rem]:hidden" aria-controls="tpt20-fa" aria-label="Show Solo plan features">
        <label for="tpt20-a" class="flex items-center justify-between @max-[40rem]:min-h-11 @max-[40rem]:cursor-pointer">
          <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt20-mut uppercase">Solo</h3>
          <span class="hidden items-center gap-2 text-xs font-medium text-tpt20-mut @max-[40rem]:flex"><span class="group-has-checked/c:hidden">4 features</span><svg class="size-3.5 transition-transform duration-300 group-has-checked/c:rotate-180 motion-reduce:transition-none" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
        </label>
        <p class="text-[40px] leading-none font-bold tracking-[-0.035em]">$9<small class="text-sm font-medium tracking-normal text-tpt20-mut">/mo</small></p>
        <div id="tpt20-fa" class="grid grid-rows-[1fr] transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.6,0,.2,1)] @max-[40rem]:invisible @max-[40rem]:grid-rows-[0fr] @max-[40rem]:group-has-checked/c:visible @max-[40rem]:group-has-checked/c:grid-rows-[1fr] motion-reduce:transition-none">
          <ul class="grid min-h-0 content-start gap-2.5 overflow-hidden text-sm text-tpt20-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt20-acc *:before:content-['✓']"><li>1 user</li><li>5 GB storage</li><li>Email support</li><li>Mobile app</li></ul>
        </div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt20-line text-sm font-semibold text-tpt20-ink no-underline transition-colors hover:border-tpt20-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt20-acc">Choose Solo</a>
      </article>
      <article class="group/c flex flex-col gap-3 rounded-[20px] border-[1.5px] border-tpt20-acc bg-white p-6 shadow-[0_16px_40px_-26px_var(--color-tpt20-acc)] @max-[40rem]:has-focus-visible:outline-3 @max-[40rem]:has-focus-visible:outline-offset-2 @max-[40rem]:has-focus-visible:outline-tpt20-acc">
        <input type="checkbox" id="tpt20-b" class="sr-only @min-[40rem]:hidden" aria-controls="tpt20-fb" aria-label="Show Team plan features" checked>
        <label for="tpt20-b" class="flex items-center justify-between @max-[40rem]:min-h-11 @max-[40rem]:cursor-pointer">
          <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt20-acc-ink uppercase">Team <span class="ml-1.5 rounded-full bg-tpt20-acc px-2 py-0.5 text-[10px] tracking-[0.06em] text-white">Popular</span></h3>
          <span class="hidden items-center gap-2 text-xs font-medium text-tpt20-mut @max-[40rem]:flex"><span class="group-has-checked/c:hidden">5 features</span><svg class="size-3.5 transition-transform duration-300 group-has-checked/c:rotate-180 motion-reduce:transition-none" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
        </label>
        <p class="text-[40px] leading-none font-bold tracking-[-0.035em]">$29<small class="text-sm font-medium tracking-normal text-tpt20-mut">/mo</small></p>
        <div id="tpt20-fb" class="grid grid-rows-[1fr] transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.6,0,.2,1)] @max-[40rem]:invisible @max-[40rem]:grid-rows-[0fr] @max-[40rem]:group-has-checked/c:visible @max-[40rem]:group-has-checked/c:grid-rows-[1fr] motion-reduce:transition-none">
          <ul class="grid min-h-0 content-start gap-2.5 overflow-hidden text-sm text-tpt20-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt20-acc *:before:content-['✓']"><li>10 users</li><li>500 GB storage</li><li>Priority support</li><li>Admin console</li><li>Guest access</li></ul>
        </div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl bg-tpt20-acc text-sm font-semibold text-white no-underline transition-colors hover:bg-tpt20-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt20-acc">Choose Team</a>
      </article>
      <article class="group/c flex flex-col gap-3 rounded-[20px] border-[1.5px] border-tpt20-line bg-white p-6 @max-[40rem]:has-focus-visible:outline-3 @max-[40rem]:has-focus-visible:outline-offset-2 @max-[40rem]:has-focus-visible:outline-tpt20-acc">
        <input type="checkbox" id="tpt20-c" class="sr-only @min-[40rem]:hidden" aria-controls="tpt20-fc" aria-label="Show Org plan features">
        <label for="tpt20-c" class="flex items-center justify-between @max-[40rem]:min-h-11 @max-[40rem]:cursor-pointer">
          <h3 class="text-[13px] font-semibold tracking-[0.08em] text-tpt20-mut uppercase">Org</h3>
          <span class="hidden items-center gap-2 text-xs font-medium text-tpt20-mut @max-[40rem]:flex"><span class="group-has-checked/c:hidden">5 features</span><svg class="size-3.5 transition-transform duration-300 group-has-checked/c:rotate-180 motion-reduce:transition-none" viewBox="0 0 14 14" aria-hidden="true"><path d="M2 5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
        </label>
        <p class="text-[40px] leading-none font-bold tracking-[-0.035em]">$79<small class="text-sm font-medium tracking-normal text-tpt20-mut">/mo</small></p>
        <div id="tpt20-fc" class="grid grid-rows-[1fr] transition-[grid-template-rows,visibility] duration-400 ease-[cubic-bezier(.6,0,.2,1)] @max-[40rem]:invisible @max-[40rem]:grid-rows-[0fr] @max-[40rem]:group-has-checked/c:visible @max-[40rem]:group-has-checked/c:grid-rows-[1fr] motion-reduce:transition-none">
          <ul class="grid min-h-0 content-start gap-2.5 overflow-hidden text-sm text-tpt20-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt20-acc *:before:content-['✓']"><li>Unlimited users</li><li>Unlimited storage</li><li>SSO / SCIM</li><li>Audit log</li><li>99.9% uptime SLA</li></ul>
        </div>
        <a href="#" class="mt-auto grid min-h-11 place-items-center rounded-xl border-[1.5px] border-tpt20-line text-sm font-semibold text-tpt20-ink no-underline transition-colors hover:border-tpt20-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt20-acc">Choose Org</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt20-line bg-white px-3.5 py-2 font-tpt20-mono text-[11.5px] text-tpt20-mut">@container · @max-[40rem]:grid-rows-[0fr] · group-has-checked/c:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt20-bg: #f1f6f5;
  --color-tpt20-bg: oklch(0.97 0.008 180);
  --color-tpt20-ink: #152220;
  --color-tpt20-ink: oklch(0.24 0.02 180);
  --color-tpt20-body: #3b4e4a;
  --color-tpt20-body: oklch(0.41 0.025 180);
  --color-tpt20-mut: #556a66;
  --color-tpt20-mut: oklch(0.5 0.025 180);
  --color-tpt20-line: #dce7e4;
  --color-tpt20-line: oklch(0.915 0.012 180);
  --color-tpt20-acc: #0f9a8a;
  --color-tpt20-acc: oklch(0.6 0.12 180);
  --color-tpt20-acc-ink: #0a7266;
  --color-tpt20-acc-ink: oklch(0.49 0.1 180);
  --font-tpt20-sans: 'Instrument Sans', system-ui, sans-serif;
  --font-tpt20-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-20 {
  width: 100%;
  min-height: 100svh;
}
```
