---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-social-proof-marquee-pricing/"
title: "Tailwind Social Proof Marquee Pricing"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "A seamless logo marquee above the tiers &mdash; social proof first, decision second &mdash; on slate with a lime accent."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Social Proof Marquee Pricing
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-social-proof-marquee-pricing/

A seamless logo marquee above the tiers &mdash; social proof first, decision second &mdash; on slate with a lime accent. The port's interesting part is not the animation but the containment: the marquee's w-max track will grow the whole section to 2000px unless the wrapper is explicitly bounded, and in utilities that bound is three classes you can actually see.
## HTML
```html
<section class="tps-18 relative w-full min-h-svh overflow-hidden [contain:layout_paint] bg-tps18-bg font-tps18-sans text-tps18-body px-[clamp(20px,4vw,40px)] pt-[clamp(20px,4vw,36px)] pb-[clamp(28px,5vw,48px)]" aria-label="Pricing">
  <div class="relative overflow-hidden [contain:layout_paint] min-w-0 max-w-screen -mx-[clamp(20px,4vw,40px)] mb-[clamp(20px,4vw,32px)] py-3.5 bg-tps18-bg/60 border-y border-tps18-lime/18 mask-x-from-88% mask-x-to-100%" aria-label="Customers using this product">
    <div class="flex w-max gap-14 whitespace-nowrap will-change-transform animate-tps18-roll motion-reduce:animate-none">
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#9671; NORTHWIND</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#9650; APEX.IO</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#9733; PULSE</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#11043; HEXLAB</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#9711; ORBITA</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#9700; FLINT</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo">&#11042; MERIDIAN</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#9671; NORTHWIND</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#9650; APEX.IO</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#9733; PULSE</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#11043; HEXLAB</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#9711; ORBITA</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#9700; FLINT</span>
      <span class="shrink-0 font-tps18-mono text-sm font-bold tracking-[0.18em] text-tps18-logo" aria-hidden="true">&#11042; MERIDIAN</span>
    </div>
  </div>
  <header class="text-center mb-[clamp(20px,4vw,32px)]">
    <span class="inline-block mb-2.5 text-xs font-semibold tracking-[0.08em] text-tps18-lime" aria-label="Rated 4.9 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733; 4.9 from 12,400 teams</span>
    <h2 class="m-0 text-[clamp(24px,3.6vw,36px)] font-bold tracking-[-0.02em] text-white">Pricing teams actually pay for.</h2>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] items-center gap-3.5 max-w-[360px] md:max-w-[940px] mx-auto">
    <article class="relative flex flex-col px-5 pt-[22px] pb-[18px] rounded-[12px] bg-tps18-card border border-tps18-lime/12">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps18-head">Free</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>0<span class="ml-1.5 text-[0.32em] font-medium opacity-65">forever</span></div>
      <ul class="list-none p-0 m-0 mb-[18px] flex-1 text-[13px]/[1.95] text-tps18-body">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">1 project</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">5 GB storage</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">Community</li>
      </ul>
      <a href="#free" class="block text-center px-4 py-2.5 rounded-[8px] bg-tps18-lime/10 text-tps18-lime border border-tps18-lime/28 text-[13px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps18-lime hover:text-tps18-bg focus-visible:outline-2 focus-visible:outline-tps18-lime focus-visible:outline-offset-[3px] motion-reduce:transition-none">Start free</a>
    </article>
    <article class="relative flex flex-col px-5 pt-[22px] pb-[18px] rounded-[12px] bg-linear-180 from-tps18-card to-tps18-moss border border-tps18-lime shadow-[inset_0_0_0_1px_--theme(--color-tps18-lime),0_14px_36px_--alpha(--color-tps18-lime/18)]">
      <span class="absolute -top-[11px] left-1/2 -translate-x-1/2 whitespace-nowrap px-2.75 py-1 rounded-full bg-tps18-lime text-tps18-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Most teams pick this</span>
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps18-lime-pale">Team</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>32<span class="ml-1.5 text-[0.32em] font-medium opacity-65">/mo</span></div>
      <ul class="list-none p-0 m-0 mb-[18px] flex-1 text-[13px]/[1.95] text-tps18-body">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">Unlimited projects</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">Priority support</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">SSO + roles</li>
      </ul>
      <a href="#team" class="block text-center px-4 py-2.5 rounded-[8px] bg-tps18-lime text-tps18-bg border border-tps18-lime text-[13px] font-semibold no-underline transition-[background-color] duration-[180ms] hover:bg-tps18-lime-pale focus-visible:outline-2 focus-visible:outline-tps18-lime focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Team</a>
    </article>
    <article class="relative flex flex-col px-5 pt-[22px] pb-[18px] rounded-[12px] bg-tps18-card border border-tps18-lime/12">
      <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps18-head">Enterprise</h3>
      <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>0<span class="ml-1.5 text-[0.32em] font-medium opacity-65">custom</span></div>
      <ul class="list-none p-0 m-0 mb-[18px] flex-1 text-[13px]/[1.95] text-tps18-body">
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">Everything in Team</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">Dedicated CSM</li>
        <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps18-lime">SLA 99.99%</li>
      </ul>
      <a href="#ent" class="block text-center px-4 py-2.5 rounded-[8px] bg-tps18-lime/10 text-tps18-lime border border-tps18-lime/28 text-[13px] font-semibold no-underline transition-[background-color,color] duration-[180ms] hover:bg-tps18-lime hover:text-tps18-bg focus-visible:outline-2 focus-visible:outline-tps18-lime focus-visible:outline-offset-[3px] motion-reduce:transition-none">Talk to sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps18-bg: #0f172a;
  --color-tps18-bg: oklch(0.21 0.04 265);
  --color-tps18-card: #1e293b;
  --color-tps18-card: oklch(0.28 0.04 264);
  --color-tps18-moss: #243f1a;
  --color-tps18-moss: oklch(0.32 0.08 135);
  --color-tps18-body: #b8c1d1;
  --color-tps18-body: oklch(0.81 0.02 265);
  --color-tps18-head: #cbd5e1;
  --color-tps18-head: oklch(0.87 0.02 262);
  --color-tps18-logo: #94a3b8;
  --color-tps18-logo: oklch(0.71 0.03 258);
  --color-tps18-lime: #a3e635;
  --color-tps18-lime: oklch(0.85 0.2 128);
  --color-tps18-lime-pale: #d9f99d;
  --color-tps18-lime-pale: oklch(0.94 0.12 124);
  --font-tps18-mono: 'JetBrains Mono', monospace;
  --font-tps18-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-tps18-roll: tps18-roll 28s linear infinite;
}
/* Keyframes have no utility form — the shorthand is a theme token
   (--animate-tps18-roll → animate-tps18-roll), the body lives here.
   The -50% travel is what makes the duplicated track loop seamlessly. */

@keyframes tps18-roll {
  to {
    transform: translateX(-50%);
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-18 {
  width: 100%;
  min-height: 100svh;
}
```
