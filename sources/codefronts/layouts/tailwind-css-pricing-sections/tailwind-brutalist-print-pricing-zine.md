---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-brutalist-print-pricing-zine/"
title: "Tailwind Brutalist Print Pricing Zine"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Black on cream, mono type, hard 8px shadows and three cards sitting askew on graph paper."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Brutalist Print Pricing Zine
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-brutalist-print-pricing-zine/

Black on cream, mono type, hard 8px shadows and three cards sitting askew on graph paper. The port lands on a genuinely better mechanism than the CSS: because Tailwind compiles rotate-* and translate-* to the individual rotate and translate properties, the hover nudge no longer wipes out each card's tilt &mdash; which in the CSS version needs the rotation repeated inside every hover rule.
## HTML
```html
<section class="tps-09 w-full min-h-svh bg-tps09-paper bg-[repeating-linear-gradient(0deg,transparent_0,transparent_23px,var(--color-tps09-rule)_23px,var(--color-tps09-rule)_24px),repeating-linear-gradient(90deg,transparent_0,transparent_23px,var(--color-tps09-rule)_23px,var(--color-tps09-rule)_24px)] font-tps09-mono text-tps09-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="mb-[clamp(24px,4vw,36px)]">
    <span class="inline-block mb-3 px-2.5 py-1 bg-tps09-ink text-tps09-paper text-[11px] tracking-[0.18em] uppercase">issue &#8470;07 &middot; pricing</span>
    <h2 class="m-0 text-[clamp(28px,5vw,44px)] font-extrabold uppercase leading-[1.1] tracking-[-0.02em]">Three sizes. One product. Pick.</h2>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] gap-8 md:gap-6 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative p-5 pt-5.5 bg-tps09-paper border-2 border-tps09-ink shadow-[8px_8px_0_0_--theme(--color-tps09-ink)] transition-[translate,box-shadow] duration-150 ease-linear md:rotate-[-1.2deg] hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[6px_6px_0_0_--theme(--color-tps09-ink)] motion-reduce:transition-none motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0 motion-reduce:hover:shadow-[8px_8px_0_0_--theme(--color-tps09-ink)]">
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Plan</span><strong class="text-sm font-bold">Solo</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Cost</span><strong class="text-[22px] font-extrabold">$8/mo</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Built for</span><strong class="text-sm font-bold">Indie devs</strong></div>
      <hr class="border-0 border-t-2 border-tps09-ink mt-3.5 mb-3">
      <ul class="list-none p-0 m-0 mb-4.5 text-[12.5px]/[1.7]">
        <li><span aria-hidden="true">&#9656; </span>1 site, 1 admin</li>
        <li><span aria-hidden="true">&#9656; </span>5 GB storage</li>
        <li><span aria-hidden="true">&#9656; </span>Forum support</li>
      </ul>
      <a href="#solo" class="block text-center px-4 py-2.75 bg-tps09-paper text-tps09-ink border-2 border-tps09-ink text-[13px] font-bold uppercase tracking-[0.06em] no-underline transition-[background-color,color] duration-150 ease-linear hover:bg-tps09-ink hover:text-tps09-acc focus-visible:outline-[3px] focus-visible:outline-tps09-focus focus-visible:outline-offset-2 motion-reduce:transition-none">[ Buy Solo ]</a>
    </article>
    <article class="relative p-5 pt-5.5 bg-tps09-acc border-2 border-tps09-ink shadow-[8px_8px_0_0_--theme(--color-tps09-ink)] transition-[translate,box-shadow] duration-150 ease-linear md:rotate-[0.8deg] hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[6px_6px_0_0_--theme(--color-tps09-ink)] motion-reduce:transition-none motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0 motion-reduce:hover:shadow-[8px_8px_0_0_--theme(--color-tps09-ink)]">
      <span class="absolute -top-3.5 -right-2.5 px-3 py-1.25 bg-tps09-ink text-tps09-acc text-[11px] font-bold uppercase tracking-[0.12em] rotate-[4deg]">&#9733; POPULAR</span>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Plan</span><strong class="text-sm font-bold">Studio</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Cost</span><strong class="text-[22px] font-extrabold">$24/mo</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Built for</span><strong class="text-sm font-bold">Small studios</strong></div>
      <hr class="border-0 border-t-2 border-tps09-ink mt-3.5 mb-3">
      <ul class="list-none p-0 m-0 mb-4.5 text-[12.5px]/[1.7]">
        <li><span aria-hidden="true">&#9656; </span>10 sites, 5 admins</li>
        <li><span aria-hidden="true">&#9656; </span>50 GB storage</li>
        <li><span aria-hidden="true">&#9656; </span>Email support</li>
        <li><span aria-hidden="true">&#9656; </span>Custom domain</li>
      </ul>
      <a href="#studio" class="block text-center px-4 py-2.75 bg-tps09-ink text-tps09-acc border-2 border-tps09-ink text-[13px] font-bold uppercase tracking-[0.06em] no-underline transition-[background-color,color] duration-150 ease-linear hover:bg-tps09-acc hover:text-tps09-ink focus-visible:outline-[3px] focus-visible:outline-tps09-focus focus-visible:outline-offset-2 motion-reduce:transition-none">[ Buy Studio ]</a>
    </article>
    <article class="relative p-5 pt-5.5 bg-tps09-paper border-2 border-tps09-ink shadow-[8px_8px_0_0_--theme(--color-tps09-ink)] transition-[translate,box-shadow] duration-150 ease-linear md:rotate-[-0.6deg] hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[6px_6px_0_0_--theme(--color-tps09-ink)] motion-reduce:transition-none motion-reduce:hover:translate-x-0 motion-reduce:hover:translate-y-0 motion-reduce:hover:shadow-[8px_8px_0_0_--theme(--color-tps09-ink)]">
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Plan</span><strong class="text-sm font-bold">Shop</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Cost</span><strong class="text-[22px] font-extrabold">$60/mo</strong></div>
      <div class="flex justify-between items-baseline py-1 text-xs border-b border-dotted border-tps09-dot"><span class="uppercase tracking-[0.06em] opacity-70">Built for</span><strong class="text-sm font-bold">Agencies</strong></div>
      <hr class="border-0 border-t-2 border-tps09-ink mt-3.5 mb-3">
      <ul class="list-none p-0 m-0 mb-4.5 text-[12.5px]/[1.7]">
        <li><span aria-hidden="true">&#9656; </span>Unlimited sites</li>
        <li><span aria-hidden="true">&#9656; </span>500 GB storage</li>
        <li><span aria-hidden="true">&#9656; </span>Priority support</li>
        <li><span aria-hidden="true">&#9656; </span>White-label</li>
      </ul>
      <a href="#shop" class="block text-center px-4 py-2.75 bg-tps09-paper text-tps09-ink border-2 border-tps09-ink text-[13px] font-bold uppercase tracking-[0.06em] no-underline transition-[background-color,color] duration-150 ease-linear hover:bg-tps09-ink hover:text-tps09-acc focus-visible:outline-[3px] focus-visible:outline-tps09-focus focus-visible:outline-offset-2 motion-reduce:transition-none">[ Buy Shop ]</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps09-paper: #f4eccc;
  --color-tps09-paper: oklch(0.93 0.04 90);
  --color-tps09-ink: #0e0e0e;
  --color-tps09-ink: oklch(0.15 0 0);
  --color-tps09-acc: #facc15;
  --color-tps09-acc: oklch(0.86 0.17 92);
  --color-tps09-focus: #ff5e5e;
  --color-tps09-focus: oklch(0.7 0.2 25);
  --color-tps09-dot: #0e0e0e40;
  --color-tps09-dot: oklch(0.15 0 0 / 0.25);
  --color-tps09-rule: #0e0e0e0a;
  --color-tps09-rule: oklch(0.15 0 0 / 0.04);
  --font-tps09-mono: 'JetBrains Mono', 'Courier New', monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-09 {
  width: 100%;
  min-height: 100svh;
}
```
