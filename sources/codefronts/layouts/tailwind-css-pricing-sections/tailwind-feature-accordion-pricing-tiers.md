---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-feature-accordion-pricing-tiers/"
title: "Tailwind Feature Accordion Pricing Tiers"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Three tiers whose full feature lists live inside native <details> elements &mdash; short page, deep detail on demand, keyboard-accessible for free."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Accordion Pricing Tiers
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-feature-accordion-pricing-tiers/

Three tiers whose full feature lists live inside native <details> elements &mdash; short page, deep detail on demand, keyboard-accessible for free. The port's neat bit is v4's open: variant: the chevron rotation and the extra open-state padding are stated on the elements, so the disclosure's whole visual behaviour is one class list.
## HTML
```html
<section class="tps-19 w-full min-h-svh bg-tps19-bg bg-[radial-gradient(60%_60%_at_50%_0%,--alpha(--color-tps19-violet/16),transparent_60%)] font-tps19-sans text-tps19-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,32px)] font-bold tracking-[-0.02em] text-white">Pricing without the wall of checkmarks.</h2>
    <p class="m-0 text-sm text-tps19-muted">Open any tier to read the full feature list. Tap to collapse.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-start gap-4 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps19-card border border-tps19-violet/20">
      <h3 class="m-0 mb-1.5 text-[15px] font-bold uppercase tracking-[0.08em] text-tps19-lilac">Indie</h3>
      <div class="flex items-baseline gap-1 mb-1.5 text-[36px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>11<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <p class="m-0 mb-4 min-h-0 md:min-h-9 text-[13px]/[1.5] text-tps19-muted">For solo developers shipping side projects.</p>
      <details class="group mb-4 px-3.5 rounded-[8px] bg-tps19-violet/5 border border-tps19-violet/18 open:pb-1">
        <summary class="flex items-center justify-between py-2.75 list-none [&amp;::-webkit-details-marker]:hidden cursor-pointer outline-0 text-[13px] font-semibold text-tps19-lilac focus-visible:outline-2 focus-visible:outline-tps19-violet focus-visible:outline-offset-[3px] focus-visible:rounded-[4px]">See all features <span class="inline-block text-sm transition-transform duration-[250ms] group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true">&#8964;</span></summary>
        <ul class="list-none p-0 pt-2.5 m-0 mb-2 border-t border-dashed border-tps19-violet/18 text-[12.5px]/[1.95] text-tps19-list">
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">1 project workspace</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">10 GB storage</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Community forum support</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Public deploys with auto-SSL</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">50K monthly visitor cap</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">1-year version history</li>
        </ul>
      </details>
      <a href="#indie" class="block mt-auto text-center px-4 py-2.75 rounded-[8px] bg-tps19-violet/12 text-tps19-lilac border border-tps19-violet/30 text-[13.5px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps19-violet/28 hover:text-white focus-visible:outline-2 focus-visible:outline-tps19-fuchsia focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Indie &rarr;</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-linear-180 from-tps19-card-hi to-tps19-card border border-tps19-violet shadow-[inset_0_0_0_1px_--theme(--color-tps19-violet),0_16px_40px_--alpha(--color-tps19-violet/22)]">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-2.75 py-1 rounded-full bg-linear-135 from-tps19-violet to-tps19-fuchsia text-tps19-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Recommended</span>
      <h3 class="m-0 mb-1.5 text-[15px] font-bold uppercase tracking-[0.08em] text-tps19-lilac">Studio</h3>
      <div class="flex items-baseline gap-1 mb-1.5 text-[36px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>34<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <p class="m-0 mb-4 min-h-0 md:min-h-9 text-[13px]/[1.5] text-tps19-muted">For small teams shipping to real users.</p>
      <details class="group mb-4 px-3.5 rounded-[8px] bg-tps19-violet/5 border border-tps19-violet/18 open:pb-1" open>
        <summary class="flex items-center justify-between py-2.75 list-none [&amp;::-webkit-details-marker]:hidden cursor-pointer outline-0 text-[13px] font-semibold text-tps19-lilac focus-visible:outline-2 focus-visible:outline-tps19-violet focus-visible:outline-offset-[3px] focus-visible:rounded-[4px]">See all features <span class="inline-block text-sm transition-transform duration-[250ms] group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true">&#8964;</span></summary>
        <ul class="list-none p-0 pt-2.5 m-0 mb-2 border-t border-dashed border-tps19-violet/18 text-[12.5px]/[1.95] text-tps19-list">
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Unlimited project workspaces</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">100 GB storage</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Priority email + chat support</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Custom domains with auto-SSL</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">500K monthly visitor cap</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">3-year version history</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Team roles &amp; permissions</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Slack, GitHub, Linear sync</li>
        </ul>
      </details>
      <a href="#studio" class="block mt-auto text-center px-4 py-2.75 rounded-[8px] bg-linear-135 from-tps19-violet to-tps19-fuchsia text-tps19-bg border border-transparent text-[13.5px] font-semibold no-underline transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps19-fuchsia focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Studio &rarr;</a>
    </article>
    <article class="relative flex flex-col px-[22px] pt-6 pb-5 rounded-[14px] bg-tps19-card border border-tps19-violet/20">
      <h3 class="m-0 mb-1.5 text-[15px] font-bold uppercase tracking-[0.08em] text-tps19-lilac">Org</h3>
      <div class="flex items-baseline gap-1 mb-1.5 text-[36px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>96<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <p class="m-0 mb-4 min-h-0 md:min-h-9 text-[13px]/[1.5] text-tps19-muted">For organisations with compliance requirements.</p>
      <details class="group mb-4 px-3.5 rounded-[8px] bg-tps19-violet/5 border border-tps19-violet/18 open:pb-1">
        <summary class="flex items-center justify-between py-2.75 list-none [&amp;::-webkit-details-marker]:hidden cursor-pointer outline-0 text-[13px] font-semibold text-tps19-lilac focus-visible:outline-2 focus-visible:outline-tps19-violet focus-visible:outline-offset-[3px] focus-visible:rounded-[4px]">See all features <span class="inline-block text-sm transition-transform duration-[250ms] group-open:rotate-180 motion-reduce:transition-none" aria-hidden="true">&#8964;</span></summary>
        <ul class="list-none p-0 pt-2.5 m-0 mb-2 border-t border-dashed border-tps19-violet/18 text-[12.5px]/[1.95] text-tps19-list">
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Everything in Studio</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">SAML SSO &amp; SCIM provisioning</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Audit logs (90-day retention)</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Unlimited monthly visitors</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Forever version history</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">SOC 2 + DPA on file</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">SLA 99.99% with credits</li>
          <li class="before:content-['\2713'] before:inline-block before:w-[18px] before:font-bold before:text-tps19-fuchsia">Dedicated CSM &amp; quarterly review</li>
        </ul>
      </details>
      <a href="#org" class="block mt-auto text-center px-4 py-2.75 rounded-[8px] bg-tps19-violet/12 text-tps19-lilac border border-tps19-violet/30 text-[13.5px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps19-violet/28 hover:text-white focus-visible:outline-2 focus-visible:outline-tps19-fuchsia focus-visible:outline-offset-[3px] motion-reduce:transition-none">Talk to sales &rarr;</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps19-bg: #15071f;
  --color-tps19-bg: oklch(0.17 0.06 305);
  --color-tps19-card: #281033;
  --color-tps19-card: oklch(0.24 0.08 305);
  --color-tps19-card-hi: #3b1554;
  --color-tps19-card-hi: oklch(0.29 0.12 305);
  --color-tps19-body: #f3e8ff;
  --color-tps19-body: oklch(0.95 0.03 305);
  --color-tps19-list: #d8c8e8;
  --color-tps19-list: oklch(0.85 0.04 305);
  --color-tps19-muted: #c4a8d6;
  --color-tps19-muted: oklch(0.77 0.06 305);
  --color-tps19-lilac: #d8b4fe;
  --color-tps19-lilac: oklch(0.83 0.11 300);
  --color-tps19-violet: #a855f7;
  --color-tps19-violet: oklch(0.63 0.24 304);
  --color-tps19-fuchsia: #d946ef;
  --color-tps19-fuchsia: oklch(0.67 0.27 322);
  --font-tps19-sans: 'Figtree', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-19 {
  width: 100%;
  min-height: 100svh;
}
```
