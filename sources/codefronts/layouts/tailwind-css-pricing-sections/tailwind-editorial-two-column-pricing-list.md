---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-editorial-two-column-pricing-list/"
title: "Tailwind Editorial Two Column Pricing List"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "A print-price-list layout: value-prop copy on the left, two compact tier rows stacked on the right, set in Playfair over cream."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Editorial Two Column Pricing List
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-editorial-two-column-pricing-list/

A print-price-list layout: value-prop copy on the left, two compact tier rows stacked on the right, set in Playfair over cream. The port's quiet win is the hover treatment &mdash; the recommended row's permanent 4px offset shadow and the other row's hover shadow are now the same utility, declared once as a resting state and once behind hover:.
## HTML
```html
<section class="tps-13 w-full min-h-svh bg-tps13-paper font-tps13-sans text-tps13-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <div class="grid grid-cols-1 md:grid-cols-[1.1fr_1fr] items-start gap-8 md:gap-14 max-w-[1040px] mx-auto">
    <div class="pt-1.5">
      <span class="block mb-3.5 font-tps13-mono text-xs tracking-[0.1em] text-tps13-muted">&mdash; Pricing</span>
      <h2 class="m-0 mb-4.5 font-tps13-serif text-[clamp(28px,4.4vw,44px)] font-bold leading-[1.1] tracking-[-0.015em]">Two plans. <em class="italic text-tps13-muted">Pick one,</em> change later.</h2>
      <p class="m-0 mb-3 max-w-[380px] text-[15px]/[1.65] text-tps13-body">We don&rsquo;t play games with feature gating, seat limits, or upsell pop-ups. Pick a plan, get the whole product, and move on with your work.</p>
      <p class="m-0 mb-3 max-w-[380px] pt-3 border-t border-tps13-line text-[13px]/[1.65] text-tps13-muted">All plans include unlimited projects, every integration, and email support. Cancel any time, money back inside 30 days.</p>
      <a href="#compare" class="inline-block mt-3 text-[13px] font-semibold text-tps13-ink underline underline-offset-4 decoration-[1.5px] transition-colors duration-[180ms] hover:text-tps13-muted focus-visible:outline-2 focus-visible:outline-tps13-ink focus-visible:outline-offset-[3px] motion-reduce:transition-none">See the full feature list &rarr;</a>
    </div>
    <div class="flex flex-col gap-3.5">
      <article class="px-[22px] pt-[22px] pb-[18px] rounded-[6px] bg-white border border-tps13-line transition-[border-color,box-shadow] duration-[180ms] hover:border-tps13-ink hover:shadow-[4px_4px_0_0_--theme(--color-tps13-ink)] motion-reduce:transition-none">
        <header class="flex items-baseline justify-between gap-3 pb-3 mb-3 border-b border-dashed border-tps13-line">
          <h3 class="flex items-center gap-2.5 m-0 font-tps13-serif text-[22px] font-bold">Solo</h3>
          <span class="text-[22px] font-extrabold tracking-[-0.02em]">$15<em class="not-italic ml-1 text-[11px] font-medium tracking-normal text-tps13-muted">/ month</em></span>
        </header>
        <p class="m-0 mb-2.5 text-[13.5px]/[1.5] text-tps13-body">For freelancers and indie builders shipping client work.</p>
        <ul class="list-none p-0 m-0 mb-4 text-[13px]/[1.85] text-tps13-body">
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">Single workspace</li>
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">10 GB storage</li>
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">Email support</li>
        </ul>
        <a href="#solo" class="inline-block px-4 py-2.25 rounded-[4px] bg-transparent text-tps13-ink border-[1.5px] border-tps13-ink text-[13px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps13-ink hover:text-tps13-paper focus-visible:outline-2 focus-visible:outline-tps13-ink focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Solo &rarr;</a>
      </article>
      <article class="px-[22px] pt-[22px] pb-[18px] rounded-[6px] bg-white border border-tps13-ink shadow-[4px_4px_0_0_--theme(--color-tps13-ink)]">
        <header class="flex items-baseline justify-between gap-3 pb-3 mb-3 border-b border-dashed border-tps13-line">
          <h3 class="flex items-center gap-2.5 m-0 font-tps13-serif text-[22px] font-bold">Studio <span class="px-2 py-0.75 rounded-[2px] bg-tps13-ink text-tps13-paper font-tps13-mono text-[9.5px] font-bold uppercase tracking-[0.12em]">Recommended</span></h3>
          <span class="text-[22px] font-extrabold tracking-[-0.02em]">$48<em class="not-italic ml-1 text-[11px] font-medium tracking-normal text-tps13-muted">/ month</em></span>
        </header>
        <p class="m-0 mb-2.5 text-[13.5px]/[1.5] text-tps13-body">For small teams who run multiple client engagements.</p>
        <ul class="list-none p-0 m-0 mb-4 text-[13px]/[1.85] text-tps13-body">
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">Unlimited workspaces</li>
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">250 GB storage</li>
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">Priority support &amp; onboarding</li>
          <li class="before:content-['\00B7'] before:inline-block before:w-[18px] before:text-[18px] before:font-extrabold before:leading-[0.5] before:align-middle before:text-tps13-ink">Client billing &amp; white-label</li>
        </ul>
        <a href="#studio" class="inline-block px-4 py-2.25 rounded-[4px] bg-tps13-ink text-tps13-paper border-[1.5px] border-tps13-ink text-[13px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps13-paper hover:text-tps13-ink focus-visible:outline-2 focus-visible:outline-tps13-ink focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Studio &rarr;</a>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps13-paper: #f5f1ea;
  --color-tps13-paper: oklch(0.95 0.015 85);
  --color-tps13-ink: #1c1c1e;
  --color-tps13-ink: oklch(0.22 0.003 285);
  --color-tps13-body: #3d3d40;
  --color-tps13-body: oklch(0.36 0.004 285);
  --color-tps13-muted: #6b6b6e;
  --color-tps13-muted: oklch(0.52 0.004 285);
  --color-tps13-line: #d8d2c5;
  --color-tps13-line: oklch(0.86 0.02 85);
  --font-tps13-serif: 'Playfair Display', Georgia, serif;
  --font-tps13-mono: 'JetBrains Mono', monospace;
  --font-tps13-sans: 'Public Sans', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-13 {
  width: 100%;
  min-height: 100svh;
}
```
