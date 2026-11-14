---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-pricing-table-subgrid-featured-plan/"
title: "Tailwind Pricing Table with Subgrid and a Featured Plan"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "Three plans with genuinely different feature counts, and CTAs that still land on one line."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Table with Subgrid and a Featured Plan
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-pricing-table-subgrid-featured-plan/

Three plans with genuinely different feature counts, and CTAs that still land on one line. The featured plan lifts with scale-105 — a transform, so its tracks stay locked to its siblings — and prices sit in <data> with tabular figures.
## HTML
```html
<section class="tgx-17 w-full min-h-svh bg-[linear-gradient(180deg,oklch(0.97_0.01_300),oklch(0.93_0.02_295))] font-tgx17-sans px-6 py-10">
  <header class="flex flex-col items-center gap-2 text-center mb-8">
    <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx17-violet">Relay · Pricing</p>
    <h2 class="text-[1.6rem] font-semibold text-tgx17-ink tracking-[-0.015em]">Pay for seats, not for uptime</h2>
    <p class="text-[0.86rem] leading-[1.6] text-tgx17-mut max-w-[46ch]">Every plan includes unlimited incidents, full history and the API. Annual billing saves two months.</p>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(200px,100%),1fr))] auto-rows-auto gap-5 w-[min(760px,100%)] mx-auto">
    <article class="row-span-5 [grid-template-rows:subgrid] grid gap-y-3.5 rounded-[18px] border border-tgx17-edge bg-white p-6">
      <p class="text-[0.62rem] tracking-[0.14em] uppercase font-bold text-tgx17-violet">&nbsp;</p>
      <div class="flex flex-col gap-1"><h3 class="text-[1.1rem] font-semibold text-tgx17-ink">Hobby</h3><p class="text-[0.76rem] text-tgx17-mut">For a side project and one pager.</p></div>
      <p class="flex items-baseline gap-1"><data value="9" class="text-[2.2rem] font-extrabold tabular-nums tracking-[-0.02em] text-tgx17-ink">$9</data><span class="text-[0.8rem] text-tgx17-mut">/mo</span></p>
      <ul class="list-disc list-inside marker:text-tgx17-violet flex flex-col gap-2 content-start text-[0.8rem] leading-[1.5] text-tgx17-mut"><li>3 services</li><li>Community support</li><li>7-day history</li></ul>
      <a href="#0" class="self-end grid items-center text-center min-h-11 px-4 rounded-full text-[0.85rem] font-semibold no-underline text-tgx17-violet border-[1.5px] border-tgx17-violet transition-colors hover:bg-tgx17-violettint focus-visible:outline-2 focus-visible:outline-tgx17-violet focus-visible:outline-offset-[3px]">Start free</a>
    </article>
    <article class="row-span-5 [grid-template-rows:subgrid] grid gap-y-3.5 rounded-[18px] border border-tgx17-violet bg-white p-6 scale-105 z-10 shadow-[0_24px_48px_-24px_color-mix(in_oklab,var(--color-tgx17-violet)_50%,transparent)]">
      <p class="text-[0.62rem] tracking-[0.14em] uppercase font-bold text-tgx17-violet">Most popular</p>
      <div class="flex flex-col gap-1"><h3 class="text-[1.1rem] font-semibold text-tgx17-ink">Pro</h3><p class="text-[0.76rem] text-tgx17-mut">For a team that ships on Fridays.</p></div>
      <p class="flex items-baseline gap-1"><data value="29" class="text-[2.2rem] font-extrabold tabular-nums tracking-[-0.02em] text-tgx17-ink">$29</data><span class="text-[0.8rem] text-tgx17-mut">/seat/mo</span></p>
      <ul class="list-disc list-inside marker:text-tgx17-violet flex flex-col gap-2 content-start text-[0.8rem] leading-[1.5] text-tgx17-mut"><li>Unlimited services</li><li>On-call rotations</li><li>90-day history</li><li>Slack &amp; PagerDuty</li><li>Priority support</li></ul>
      <a href="#0" class="self-end grid items-center text-center min-h-11 px-4 rounded-full text-[0.85rem] font-semibold no-underline text-white bg-tgx17-violet transition-colors hover:bg-tgx17-violetdark focus-visible:outline-2 focus-visible:outline-tgx17-violet focus-visible:outline-offset-[3px]">Start 14-day trial</a>
    </article>
    <article class="row-span-5 [grid-template-rows:subgrid] grid gap-y-3.5 rounded-[18px] border border-tgx17-edge bg-white p-6">
      <p class="text-[0.62rem] tracking-[0.14em] uppercase font-bold text-tgx17-violet">&nbsp;</p>
      <div class="flex flex-col gap-1"><h3 class="text-[1.1rem] font-semibold text-tgx17-ink">Enterprise</h3><p class="text-[0.76rem] text-tgx17-mut">For regulated and multi-region teams.</p></div>
      <p class="flex items-baseline gap-1"><data value="99" class="text-[2.2rem] font-extrabold tabular-nums tracking-[-0.02em] text-tgx17-ink">$99</data><span class="text-[0.8rem] text-tgx17-mut">/seat/mo</span></p>
      <ul class="list-disc list-inside marker:text-tgx17-violet flex flex-col gap-2 content-start text-[0.8rem] leading-[1.5] text-tgx17-mut"><li>Everything in Pro</li><li>SSO &amp; audit log</li><li>Data residency</li><li>99.9% SLA</li></ul>
      <a href="#0" class="self-end grid items-center text-center min-h-11 px-4 rounded-full text-[0.85rem] font-semibold no-underline text-tgx17-violet border-[1.5px] border-tgx17-violet transition-colors hover:bg-tgx17-violettint focus-visible:outline-2 focus-visible:outline-tgx17-violet focus-visible:outline-offset-[3px]">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx17-violet: #5b35c4;
  --color-tgx17-violet: oklch(0.45 0.21 295);
  --color-tgx17-violetdark: #47259f;
  --color-tgx17-violetdark: oklch(0.38 0.2 295);
  --color-tgx17-violettint: #f0eafc;
  --color-tgx17-violettint: oklch(0.95 0.02 295);
  --color-tgx17-edge: #ddd6ef;
  --color-tgx17-edge: oklch(0.88 0.03 295);
  --color-tgx17-ink: #241d3b;
  --color-tgx17-ink: oklch(0.25 0.04 295);
  --color-tgx17-mut: #56506b;
  --color-tgx17-mut: oklch(0.45 0.03 295);
  --font-tgx17-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-17 {
  width: 100%;
  min-height: 100svh;
}

@supports not (grid-template-rows: subgrid) {
  .tgx-17 article {
    grid-template-rows: auto auto auto 1fr auto;
  }
}
```
