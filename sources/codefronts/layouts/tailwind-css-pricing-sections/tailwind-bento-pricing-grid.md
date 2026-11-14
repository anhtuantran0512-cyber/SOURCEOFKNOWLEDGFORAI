---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-bento-pricing-grid/"
title: "Tailwind Bento Pricing Grid"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "A bento canvas instead of a tier row: the Pro tile occupies a 2&times;2 quadrant and free / team / stat / quote tiles fan out around it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Bento Pricing Grid
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-bento-pricing-grid/

A bento canvas instead of a tier row: the Pro tile occupies a 2&times;2 quadrant and free / team / stat / quote tiles fan out around it. The port swaps named grid areas for span utilities &mdash; a real trade, because col-span-2 row-span-2 lives on the tile while grid-template-areas lived in one place and drew the whole map.
## HTML
```html
<section class="tps-07 w-full min-h-svh bg-tps07-bg font-tps07-sans text-tps07-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,36px)]">
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,34px)] font-bold tracking-[-0.02em] text-tps07-head text-pretty">Pricing in tiles, not tiers.</h2>
    <p class="mx-auto my-0 max-w-[480px] text-sm text-tps07-mut">One canvas, three offers, and the proof points that make the choice obvious.</p>
  </header>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5 max-w-[980px] mx-auto">
    <article class="relative overflow-hidden flex flex-col justify-between min-h-32.5 p-5 rounded-2xl border-0 text-tps07-bg bg-linear-[135deg,var(--color-tps07-acc),var(--color-tps07-acc2)] sm:col-span-2 lg:row-span-2 before:content-[''] before:absolute before:-right-10 before:-bottom-10 before:size-40 before:rounded-full before:bg-[radial-gradient(circle,oklch(1_0_0/0.18),transparent_70%)] before:pointer-events-none">
      <div class="relative z-1 flex flex-col items-start">
        <span class="self-start mb-2 px-2.75 py-1.25 rounded-full bg-tps07-bg text-tps07-acc text-[10px] font-bold tracking-[0.1em] uppercase">Recommended</span>
        <h3 class="m-0 mb-1.5 text-[13px] font-bold tracking-[0.1em] uppercase text-tps07-bg">Pro</h3>
        <div class="mb-3 text-[clamp(36px,5vw,56px)] font-extrabold leading-none tracking-[-0.03em]"><em class="align-top pr-0.5 text-[0.5em] not-italic opacity-70">$</em>34<span class="ml-1.5 text-[0.28em] font-medium opacity-70">/mo</span></div>
        <ul class="list-none p-0 m-0 mb-4.5 text-[13px]/[1.9]">
          <li><span class="inline-block w-5 font-bold" aria-hidden="true">&#10003;</span>Unlimited projects</li>
          <li><span class="inline-block w-5 font-bold" aria-hidden="true">&#10003;</span>100 GB storage</li>
          <li><span class="inline-block w-5 font-bold" aria-hidden="true">&#10003;</span>Priority support</li>
          <li><span class="inline-block w-5 font-bold" aria-hidden="true">&#10003;</span>Custom domains</li>
        </ul>
      </div>
      <a href="#pro" class="relative z-1 self-start inline-block px-4 py-2.5 rounded-lg text-[13.5px] font-semibold no-underline bg-tps07-bg text-tps07-acc border border-tps07-bg transition-[background-color,color,border-color] duration-200 hover:bg-transparent hover:text-white hover:border-white focus-visible:outline-2 focus-visible:outline-tps07-ink focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Pro &rarr;</a>
    </article>
    <article class="flex flex-col justify-between min-h-32.5 p-5 rounded-2xl bg-tps07-tile border border-tps07-edge">
      <div>
        <h3 class="m-0 mb-1.5 text-[13px] tracking-[0.1em] uppercase opacity-80">Free</h3>
        <div class="mb-3 text-[clamp(36px,5vw,56px)] font-extrabold leading-none tracking-[-0.03em]"><em class="align-top pr-0.5 text-[0.5em] not-italic opacity-70">$</em>0<span class="ml-1.5 text-[0.28em] font-medium opacity-70">forever</span></div>
        <p class="m-0 mb-3 text-[13px]/snug text-tps07-mut">Build something small, ship it, keep it free.</p>
      </div>
      <a href="#free" class="self-start inline-block px-3.5 py-2 rounded-lg text-[12.5px] font-semibold no-underline text-tps07-acc border border-tps07-ctaedge transition-[background-color,color,border-color] duration-200 hover:bg-tps07-acc hover:text-tps07-bg hover:border-tps07-acc focus-visible:outline-2 focus-visible:outline-tps07-ink focus-visible:outline-offset-3 motion-reduce:transition-none">Start free &rarr;</a>
    </article>
    <article class="flex flex-col justify-between items-start gap-2 min-h-32.5 p-5 rounded-2xl bg-tps07-tile border border-tps07-edge">
      <span class="text-[clamp(36px,5vw,50px)] font-extrabold leading-none tracking-[-0.03em] text-transparent bg-linear-to-b from-tps07-acc3 to-tps07-acc bg-clip-text forced-colors:text-[CanvasText]">14k+</span>
      <span class="text-xs/snug text-tps07-mut">teams pay for Pro every month</span>
    </article>
    <article class="flex flex-col justify-between min-h-32.5 p-5 rounded-2xl bg-tps07-tile border border-tps07-edge">
      <div>
        <h3 class="m-0 mb-1.5 text-[13px] tracking-[0.1em] uppercase opacity-80">Team</h3>
        <div class="mb-3 text-[clamp(36px,5vw,56px)] font-extrabold leading-none tracking-[-0.03em]"><em class="align-top pr-0.5 text-[0.5em] not-italic opacity-70">$</em>99<span class="ml-1.5 text-[0.28em] font-medium opacity-70">/mo</span></div>
        <p class="m-0 mb-3 text-[13px]/snug text-tps07-mut">Roles, billing, and audit logs for growing companies.</p>
      </div>
      <a href="#team" class="self-start inline-block px-3.5 py-2 rounded-lg text-[12.5px] font-semibold no-underline text-tps07-acc border border-tps07-ctaedge transition-[background-color,color,border-color] duration-200 hover:bg-tps07-acc hover:text-tps07-bg hover:border-tps07-acc focus-visible:outline-2 focus-visible:outline-tps07-ink focus-visible:outline-offset-3 motion-reduce:transition-none">Choose Team &rarr;</a>
    </article>
    <blockquote class="flex flex-col justify-between gap-2 min-h-32.5 m-0 p-5 rounded-2xl border-0 text-tps07-bg bg-linear-[135deg,var(--color-tps07-acc2),var(--color-tps07-acc4)]">
      <p class="m-0 text-[13px]/snug font-medium italic opacity-92">&ldquo;We tried five tools. This was the only one priced like a partner, not a tax.&rdquo;</p>
      <cite class="not-italic text-[11px] tracking-[0.05em] opacity-75">&mdash; Lior, CTO at Pulse</cite>
    </blockquote>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps07-bg: #1a0d0d;
  --color-tps07-bg: oklch(0.18 0.03 30);
  --color-tps07-tile: #2a1612;
  --color-tps07-tile: oklch(0.25 0.04 32);
  --color-tps07-edge: #4a2b23;
  --color-tps07-edge: oklch(0.37 0.05 32);
  --color-tps07-ctaedge: #7a4234;
  --color-tps07-ctaedge: oklch(0.5 0.08 32);
  --color-tps07-ink: #ffe7df;
  --color-tps07-ink: oklch(0.94 0.02 30);
  --color-tps07-head: #ffd0bf;
  --color-tps07-head: oklch(0.9 0.05 40);
  --color-tps07-mut: #b89180;
  --color-tps07-mut: oklch(0.72 0.05 40);
  --color-tps07-acc: #ff6b4a;
  --color-tps07-acc: oklch(0.7 0.18 32);
  --color-tps07-acc2: #f43f5e;
  --color-tps07-acc2: oklch(0.65 0.21 15);
  --color-tps07-acc3: #ffb37a;
  --color-tps07-acc3: oklch(0.82 0.11 55);
  --color-tps07-acc4: #be123c;
  --color-tps07-acc4: oklch(0.51 0.2 15);
  --font-tps07-sans: 'Inter', system-ui, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. */

.tps-07 {
  width: 100%;
  min-height: 100svh;
}
```
