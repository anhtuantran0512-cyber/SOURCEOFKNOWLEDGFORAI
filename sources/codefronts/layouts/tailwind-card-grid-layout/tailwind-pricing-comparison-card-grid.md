---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-pricing-comparison-card-grid/"
title: "Tailwind Pricing Comparison Card Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "Three tiers, one featured, and every CTA on the same horizontal axis regardless of how many features a tier lists &mdash; because each card is flex flex-col…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Comparison Card Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-pricing-comparison-card-grid/

Three tiers, one featured, and every CTA on the same horizontal axis regardless of how many features a tier lists &mdash; because each card is flex flex-col with flex-1 on the list and mt-auto on the button. The featured tier's whole identity is five utilities: scale-104, a two-pixel accent border, a shadow, z-1, and max-[860px]:order-first.
## HTML
```html
<section class="tcg-10 w-full min-h-svh flex flex-col items-center justify-center bg-tcg10-bg font-tcg10-sans text-tcg10-ink px-[clamp(20px,3vw,48px)] py-[clamp(32px,4vw,64px)]" aria-label="Pricing comparison card grid demo">

  <header class="max-w-[600px] text-center mb-[clamp(32px,4vw,56px)]">
    <span class="inline-block mb-3.5 px-3 py-1.5 rounded-full text-[.74rem] font-bold tracking-[0.18em] uppercase text-tcg10-accent bg-tcg10-accentsoft">Pricing</span>
    <h2 class="text-[clamp(1.8rem,3.4vw,2.6rem)] font-extrabold tracking-[-0.02em] leading-[1.1]">Simple plans. No surprises.</h2>
    <p class="mt-2.5 text-[clamp(.92rem,1.1vw,1.05rem)] leading-[1.5] text-tcg10-muted text-pretty">Pick a plan that fits. Switch or cancel any time.</p>
  </header>

  <div class="w-full max-w-[1080px] grid grid-cols-3 max-[860px]:grid-cols-1 max-[860px]:max-w-[480px] items-stretch gap-[clamp(16px,2vw,28px)]">

    <article class="relative flex flex-col rounded-2xl border border-tcg10-line bg-tcg10-card p-[clamp(24px,2.4vw,32px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_32px_-16px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <header class="mb-4.5">
        <span class="block text-xl font-extrabold tracking-[-0.01em]">Starter</span>
        <span class="block mt-1 text-[.84rem] text-tcg10-muted">For solo makers</span>
      </header>
      <div class="flex items-baseline gap-0.5 mb-2 leading-none">
        <span class="self-start mt-2 text-[1.4rem] font-bold text-tcg10-muted">$</span>
        <span class="text-tcg10-price font-black tracking-[-0.04em] leading-none tabular-nums">0</span>
        <span class="text-base font-semibold text-tcg10-muted">/mo</span>
      </div>
      <p class="mt-3.5 mb-5.5 text-[.92rem] leading-[1.45] text-tcg10-muted">Everything you need to get going.</p>
      <ul class="flex-1 flex flex-col gap-2.75 mb-6 list-none">
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>1 project</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>10K monthly events</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Community support</li>
        <li class="flex items-center gap-2.75 text-[.94rem] text-tcg10-muted"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-line text-tcg10-muted text-[.72rem] font-extrabold" aria-hidden="true">&#10007;</span>Custom domains</li>
        <li class="flex items-center gap-2.75 text-[.94rem] text-tcg10-muted"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-line text-tcg10-muted text-[.72rem] font-extrabold" aria-hidden="true">&#10007;</span>Team seats</li>
      </ul>
      <a href="#starter" class="mt-auto flex items-center justify-center min-h-11 px-5 py-3.25 rounded-[10px] border-[1.5px] border-tcg10-line text-[.94rem] font-bold text-tcg10-ink no-underline transition-[color,border-color] duration-250 hover:text-tcg10-accent hover:border-tcg10-accent focus-visible:outline-2 focus-visible:outline-tcg10-accent focus-visible:outline-offset-2 motion-reduce:transition-none">Start free</a>
    </article>

    <article class="relative z-1 flex flex-col scale-104 max-[860px]:scale-100 max-[860px]:order-first rounded-2xl border-2 border-tcg10-accent bg-tcg10-card p-[clamp(24px,2.4vw,32px)] shadow-[0_24px_48px_-20px_oklch(0.5_0.24_296/0.32)] transition-[translate,scale,box-shadow] duration-250 hover:-translate-y-1 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-3.5 py-1.5 rounded-full bg-tcg10-accent text-white text-[.7rem] font-bold tracking-[0.14em] uppercase">Most Popular</span>
      <header class="mb-4.5">
        <span class="block text-xl font-extrabold tracking-[-0.01em]">Pro</span>
        <span class="block mt-1 text-[.84rem] text-tcg10-muted">For growing teams</span>
      </header>
      <div class="flex items-baseline gap-0.5 mb-2 leading-none">
        <span class="self-start mt-2 text-[1.4rem] font-bold text-tcg10-muted">$</span>
        <span class="text-tcg10-price font-black tracking-[-0.04em] leading-none tabular-nums">24</span>
        <span class="text-base font-semibold text-tcg10-muted">/mo</span>
      </div>
      <p class="mt-3.5 mb-5.5 text-[.92rem] leading-[1.45] text-tcg10-muted">Everything in Starter, plus the good stuff.</p>
      <ul class="flex-1 flex flex-col gap-2.75 mb-6 list-none">
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Unlimited projects</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>1M monthly events</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Priority support</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Custom domains</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>5 team seats</li>
      </ul>
      <a href="#pro" class="mt-auto flex items-center justify-center min-h-11 px-5 py-3.25 rounded-[10px] bg-tcg10-accent text-[.94rem] font-bold text-white no-underline transition-[background] duration-250 hover:bg-tcg10-accentdeep focus-visible:outline-2 focus-visible:outline-tcg10-ink focus-visible:outline-offset-2 motion-reduce:transition-none">Start 14-day trial &rarr;</a>
    </article>

    <article class="relative flex flex-col rounded-2xl border border-tcg10-line bg-tcg10-card p-[clamp(24px,2.4vw,32px)] transition-[translate,box-shadow] duration-250 hover:-translate-y-1 hover:shadow-[0_18px_32px_-16px_oklch(0.2_0.04_260/0.18)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <header class="mb-4.5">
        <span class="block text-xl font-extrabold tracking-[-0.01em]">Enterprise</span>
        <span class="block mt-1 text-[.84rem] text-tcg10-muted">For scale</span>
      </header>
      <div class="flex items-baseline mb-2 leading-none">
        <span class="text-[clamp(2rem,4vw,2.8rem)] font-black tracking-[-0.02em] leading-none">Custom</span>
      </div>
      <p class="mt-3.5 mb-5.5 text-[.92rem] leading-[1.45] text-tcg10-muted">Everything in Pro, plus SLAs and SSO.</p>
      <ul class="flex-1 flex flex-col gap-2.75 mb-6 list-none">
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Unlimited everything</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Dedicated CSM</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>99.99% SLA</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>SSO + SAML</li>
        <li class="flex items-center gap-2.75 text-[.94rem]"><span class="shrink-0 inline-flex items-center justify-center w-5 h-5 rounded-full bg-tcg10-accent text-white text-[.72rem] font-extrabold" aria-hidden="true">&#10003;</span>Custom contracts</li>
      </ul>
      <a href="#enterprise" class="mt-auto flex items-center justify-center min-h-11 px-5 py-3.25 rounded-[10px] border-[1.5px] border-tcg10-line text-[.94rem] font-bold text-tcg10-ink no-underline transition-[color,border-color] duration-250 hover:text-tcg10-accent hover:border-tcg10-accent focus-visible:outline-2 focus-visible:outline-tcg10-accent focus-visible:outline-offset-2 motion-reduce:transition-none">Contact sales</a>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg10-bg: #fafafa;
  --color-tcg10-bg: oklch(0.98 0 0);
  --color-tcg10-card: #ffffff;
  --color-tcg10-card: oklch(1 0 0);
  --color-tcg10-ink: #0f172a;
  --color-tcg10-ink: oklch(0.21 0.04 260);
  --color-tcg10-muted: #64748b;
  --color-tcg10-muted: oklch(0.55 0.03 257);
  --color-tcg10-line: #e2e8f0;
  --color-tcg10-line: oklch(0.92 0.01 255);
  --color-tcg10-accent: #7c3aed;
  --color-tcg10-accent: oklch(0.54 0.25 296);
  --color-tcg10-accentdeep: #6d28d9;
  --color-tcg10-accentdeep: oklch(0.48 0.24 296);
  --color-tcg10-accentsoft: #ede9fe;
  --color-tcg10-accentsoft: oklch(0.94 0.03 296);
  --font-tcg10-sans: 'Space Grotesk', system-ui, sans-serif;
  --text-tcg10-price: clamp(2.6rem, 5.5vw, 4rem);
}
/* Root rule: the full-bleed contract. */

.tcg-10 {
  width: 100%;
  min-height: 100svh;
}

.tcg-10 ::selection {
  background: #7c3aed;
  color: #fff;
}
```
