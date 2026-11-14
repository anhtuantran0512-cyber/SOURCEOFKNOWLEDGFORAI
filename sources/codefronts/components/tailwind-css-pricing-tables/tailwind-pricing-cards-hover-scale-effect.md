---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-hover-scale-effect/"
title: "Tailwind Pricing Cards with Hover Scale Effect"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "The classic conversion micro-interaction: hover or keyboard-focus any tier and it lifts, scales and deepens its shadow while its siblings ease back and…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Cards with Hover Scale Effect
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-cards-hover-scale-effect/

The classic conversion micro-interaction: hover or keyboard-focus any tier and it lifts, scales and deepens its shadow while its siblings ease back and desaturate. The sibling logic is v4's variant stacking — group-has-[article:hover]/g:not-hover:scale-96 — read left to right as &ldquo;when any card in the grid is hovered, and this one isn't&rdquo;.
## HTML
```html
<section class="tpt-05 w-full min-h-svh grid place-items-center bg-tpt05-bg bg-[radial-gradient(70%_50%_at_50%_100%,var(--color-tpt05-glow),transparent)] px-5 py-16 font-tpt05-sans text-tpt05-ink antialiased" aria-label="Pricing cards with focus hover effect">
  <div class="grid w-full max-w-5xl justify-items-center gap-11">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">Pick your pace</h2>
    <div class="group/g grid w-full gap-6 md:grid-cols-3">
      <article class="relative flex flex-col rounded-3xl border border-tpt05-line bg-white p-8 transition-[translate,scale,filter,opacity] duration-350 ease-[cubic-bezier(.3,1.2,.3,1)] will-change-transform after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:opacity-0 after:shadow-[0_30px_60px_-22px_var(--color-tpt05-acc)] after:transition-opacity after:duration-350 after:content-[''] hover:z-10 hover:-translate-y-2.5 hover:scale-105 hover:after:opacity-60 focus-within:z-10 focus-within:-translate-y-2.5 focus-within:scale-105 focus-within:after:opacity-60 group-has-[article:hover]/g:not-hover:scale-96 group-has-[article:hover]/g:not-hover:opacity-75 group-has-[article:hover]/g:not-hover:saturate-50 motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt05-mut uppercase">Lite</h3>
        <p class="mt-3 text-[46px] leading-none font-extrabold tracking-[-0.035em]">$15<small class="text-[15px] font-semibold tracking-normal text-tpt05-mut"> / month</small></p>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt05-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt05-acc *:before:content-['✓']"><li>2 seats</li><li>Weekly reports</li><li>Email support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt05-ink text-sm font-bold text-white no-underline transition-colors hover:bg-tpt05-acc focus-visible:bg-tpt05-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt05-acc">Select Lite</a>
      </article>
      <article class="relative flex flex-col rounded-3xl border border-tpt05-acc/40 bg-white p-8 transition-[translate,scale,filter,opacity] duration-350 ease-[cubic-bezier(.3,1.2,.3,1)] will-change-transform after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:opacity-35 after:shadow-[0_30px_60px_-22px_var(--color-tpt05-acc)] after:transition-opacity after:duration-350 after:content-[''] md:scale-[1.03] hover:z-10 hover:-translate-y-2.5 hover:scale-105 hover:after:opacity-60 focus-within:z-10 focus-within:-translate-y-2.5 focus-within:scale-105 focus-within:after:opacity-60 group-has-[article:hover]/g:not-hover:scale-96 group-has-[article:hover]/g:not-hover:opacity-75 group-has-[article:hover]/g:not-hover:saturate-50 group-has-[article:hover]/g:not-hover:after:opacity-0 motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
        <span class="absolute -top-3 left-8 rounded-full bg-tpt05-acc px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase">Recommended</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt05-acc-ink uppercase">Growth</h3>
        <p class="mt-3 text-[46px] leading-none font-extrabold tracking-[-0.035em]">$39<small class="text-[15px] font-semibold tracking-normal text-tpt05-mut"> / month</small></p>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt05-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt05-acc *:before:content-['✓']"><li>10 seats</li><li>Daily reports</li><li>200+ integrations</li><li>Live chat support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt05-acc text-sm font-bold text-white no-underline transition-colors hover:bg-tpt05-acc-ink focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt05-acc">Select Growth</a>
      </article>
      <article class="relative flex flex-col rounded-3xl border border-tpt05-line bg-white p-8 transition-[translate,scale,filter,opacity] duration-350 ease-[cubic-bezier(.3,1.2,.3,1)] will-change-transform after:pointer-events-none after:absolute after:inset-0 after:rounded-[inherit] after:opacity-0 after:shadow-[0_30px_60px_-22px_var(--color-tpt05-acc)] after:transition-opacity after:duration-350 after:content-[''] hover:z-10 hover:-translate-y-2.5 hover:scale-105 hover:after:opacity-60 focus-within:z-10 focus-within:-translate-y-2.5 focus-within:scale-105 focus-within:after:opacity-60 group-has-[article:hover]/g:not-hover:scale-96 group-has-[article:hover]/g:not-hover:opacity-75 group-has-[article:hover]/g:not-hover:saturate-50 motion-reduce:transition-none motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt05-mut uppercase">Scale</h3>
        <p class="mt-3 text-[46px] leading-none font-extrabold tracking-[-0.035em]">$99<small class="text-[15px] font-semibold tracking-normal text-tpt05-mut"> / month</small></p>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt05-body *:flex *:gap-2.5 *:before:font-bold *:before:text-tpt05-acc *:before:content-['✓']"><li>Unlimited seats</li><li>Real-time analytics</li><li>Dedicated manager</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-tpt05-ink text-sm font-bold text-white no-underline transition-colors hover:bg-tpt05-acc focus-visible:bg-tpt05-acc focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-tpt05-acc">Select Scale</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt05-line bg-white/70 px-3.5 py-2 font-tpt05-mono text-[11.5px] text-tpt05-mut">group-has-[article:hover]/g:not-hover:scale-96 · hover:scale-105</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt05-bg: #f2f0f7;
  --color-tpt05-bg: oklch(0.955 0.01 300);
  --color-tpt05-glow: #e6dcfb;
  --color-tpt05-glow: oklch(0.91 0.045 300);
  --color-tpt05-ink: #1d1a26;
  --color-tpt05-ink: oklch(0.22 0.02 295);
  --color-tpt05-body: #4a4460;
  --color-tpt05-body: oklch(0.42 0.04 295);
  --color-tpt05-mut: #686280;
  --color-tpt05-mut: oklch(0.51 0.04 295);
  --color-tpt05-line: #e2dfeb;
  --color-tpt05-line: oklch(0.91 0.012 295);
  --color-tpt05-acc: #8b3fe0;
  --color-tpt05-acc: oklch(0.55 0.22 300);
  --color-tpt05-acc-ink: #6c28b8;
  --color-tpt05-acc-ink: oklch(0.47 0.21 300);
  --font-tpt05-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-tpt05-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-05 {
  width: 100%;
  min-height: 100svh;
}
```
