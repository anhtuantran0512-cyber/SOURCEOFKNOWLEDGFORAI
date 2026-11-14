---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-highlighted-popular-pricing-tier/"
title: "Tailwind Highlighted Popular Pricing Tier"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "The lift pattern: the middle tier scales up, gains a sunset gradient and wears a &ldquo;Most popular&rdquo; pill notched over its top edge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Highlighted Popular Pricing Tier
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-highlighted-popular-pricing-tier/

The lift pattern: the middle tier scales up, gains a sunset gradient and wears a &ldquo;Most popular&rdquo; pill notched over its top edge. In utilities the highlight is not a second component &mdash; it is the same <article> class list plus five overrides, which is the clearest way to show a reviewer exactly what &ldquo;recommended&rdquo; costs.
## HTML
```html
<section class="tps-02 w-full min-h-svh bg-tps02-bg font-tps02-sans text-tps02-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(28px,5vw,48px)]">
    <h2 class="m-0 mb-2.5 text-[clamp(24px,3.6vw,36px)] font-bold tracking-[-0.02em] text-transparent bg-linear-to-r from-tps02-acc to-tps02-acc3 bg-clip-text forced-colors:text-[CanvasText] text-pretty">Simple pricing, no surprises.</h2>
    <p class="m-0 text-sm text-tps02-mut">Three plans. Same product. Pick what you can grow into.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-4.5 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative flex flex-col p-5.5 pt-6.5 rounded-2xl bg-tps02-card border border-tps02-edge">
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps02-acc3">Basic</h3>
      <div class="flex items-baseline gap-0.75 mb-1.5">
        <span class="text-lg font-semibold opacity-70">$</span><span class="text-[44px] font-extrabold tracking-[-0.03em]">12</span><span class="ml-1 text-[13px] opacity-70">/mo</span>
      </div>
      <p class="m-0 mb-4.5 text-[13px] opacity-75">Just the essentials.</p>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[1.9]">
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>3 projects</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>5 GB storage</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Email-only support</li>
      </ul>
      <a href="#basic" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline text-tps02-acc3 border border-current transition-[background-color,color] duration-200 hover:bg-tps02-acc3 hover:text-tps02-bg focus-visible:outline-2 focus-visible:outline-tps02-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Basic</a>
    </article>
    <article class="relative flex flex-col p-5.5 pt-6.5 rounded-2xl border-0 z-2 bg-linear-to-b from-tps02-acc to-tps02-acc2 text-tps02-bg md:scale-105 md:shadow-[0_14px_40px_--theme(--color-tps02-glow)]">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1.25 rounded-full bg-tps02-bg text-tps02-acc text-[11px] font-bold uppercase tracking-[0.08em]" aria-label="Most popular plan">Most popular</span>
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps02-bg">Pro</h3>
      <div class="flex items-baseline gap-0.75 mb-1.5">
        <span class="text-lg font-semibold opacity-70">$</span><span class="text-[44px] font-extrabold tracking-[-0.03em]">36</span><span class="ml-1 text-[13px] opacity-70">/mo</span>
      </div>
      <p class="m-0 mb-4.5 text-[13px] opacity-75">Everything teams actually need.</p>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[1.9]">
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Unlimited projects</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>100 GB storage</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Priority support</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Custom domains</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Team roles</li>
      </ul>
      <a href="#pro" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline bg-tps02-bg text-tps02-acc border border-tps02-bg transition-[background-color,color,border-color] duration-200 hover:bg-tps02-ink hover:text-tps02-bg hover:border-tps02-ink focus-visible:outline-2 focus-visible:outline-tps02-bg focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Pro</a>
    </article>
    <article class="relative flex flex-col p-5.5 pt-6.5 rounded-2xl bg-tps02-card border border-tps02-edge">
      <h3 class="m-0 mb-3.5 text-[15px] font-bold uppercase tracking-[0.06em] text-tps02-acc3">Enterprise</h3>
      <div class="flex items-baseline gap-0.75 mb-1.5">
        <span class="text-lg font-semibold opacity-70">$</span><span class="text-[44px] font-extrabold tracking-[-0.03em]">99</span><span class="ml-1 text-[13px] opacity-70">/mo</span>
      </div>
      <p class="m-0 mb-4.5 text-[13px] opacity-75">Compliance + dedicated success.</p>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 text-[13.5px]/[1.9]">
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>Everything in Pro</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>SSO &amp; SAML</li>
        <li><span class="inline-block w-4.5 font-extrabold opacity-85" aria-hidden="true">&#10003;</span>SLA + dedicated CSM</li>
      </ul>
      <a href="#enterprise" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline text-tps02-acc3 border border-current transition-[background-color,color] duration-200 hover:bg-tps02-acc3 hover:text-tps02-bg focus-visible:outline-2 focus-visible:outline-tps02-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps02-bg: #1a1410;
  --color-tps02-bg: oklch(0.19 0.02 50);
  --color-tps02-card: #261c16;
  --color-tps02-card: oklch(0.25 0.02 50);
  --color-tps02-edge: #4a342a;
  --color-tps02-edge: oklch(0.38 0.04 50);
  --color-tps02-ink: #fef2e6;
  --color-tps02-ink: oklch(0.96 0.02 70);
  --color-tps02-mut: #c9b3a3;
  --color-tps02-mut: oklch(0.79 0.03 60);
  --color-tps02-acc: #ff8b5a;
  --color-tps02-acc: oklch(0.75 0.16 45);
  --color-tps02-acc2: #f56a3a;
  --color-tps02-acc2: oklch(0.68 0.18 40);
  --color-tps02-acc3: #ffb37a;
  --color-tps02-acc3: oklch(0.82 0.11 55);
  --color-tps02-glow: #f56a3a59;
  --color-tps02-glow: oklch(0.68 0.18 40 / 0.35);
  --font-tps02-sans: 'Inter', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-02 {
  width: 100%;
  min-height: 100svh;
}
```
