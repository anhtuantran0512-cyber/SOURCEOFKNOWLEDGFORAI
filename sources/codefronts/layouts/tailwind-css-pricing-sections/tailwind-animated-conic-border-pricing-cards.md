---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-animated-conic-border-pricing-cards/"
title: "Tailwind Animated Conic Border Pricing Cards"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "Three cards wearing a conic-gradient border that rotates forever, driven by an @property-registered angle."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Conic Border Pricing Cards
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-animated-conic-border-pricing-cards/

Three cards wearing a conic-gradient border that rotates forever, driven by an @property-registered angle. The port is honest about its limits: the registration, the mask-composite ring and the keyframes stay in CSS &mdash; but the angle's value, the two gradient recipes and every other pixel become utilities, and the reduced-motion fallback moves onto the element where you can see it.
## HTML
```html
<section class="tps-12 w-full min-h-svh bg-tps12-bg font-tps12-sans text-tps12-body px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(24px,4vw,40px)]">
    <span class="inline-block mb-3.5 px-3 py-1.25 rounded-full bg-tps12-label/10 border border-tps12-label/25 text-[11px] font-bold uppercase tracking-[0.18em] text-tps12-label">Plans</span>
    <h2 class="m-0 text-[clamp(22px,3.4vw,34px)] font-bold tracking-[-0.02em] text-white">Built for builders. Priced for shipping.</h2>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] gap-4 max-w-[380px] md:max-w-[980px] mx-auto">
    <article class="relative p-[1.5px] rounded-[16px] bg-white/4">
      <span class="absolute inset-0 p-[1.5px] rounded-[16px] bg-[conic-gradient(from_var(--tps12-ang),--theme(--color-tps12-ring-a),--theme(--color-tps12-ring-b),--theme(--color-tps12-ring-a))] [-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [-webkit-mask-composite:xor] [mask-composite:exclude] animate-tps12-spin motion-reduce:animate-none motion-reduce:bg-linear-135 motion-reduce:from-tps12-ring-b motion-reduce:to-tps12-ring-a" aria-hidden="true"></span>
      <div class="relative flex flex-col h-full px-5 pt-[22px] pb-5 rounded-[14.5px] bg-tps12-body-bg">
        <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps12-label">Starter</h3>
        <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>14<span class="ml-1.5 text-[0.34em] font-medium opacity-65">/mo</span></div>
        <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.95] text-tps12-body">
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">3 projects</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">10 GB storage</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">Community support</li>
        </ul>
        <a href="#starter" class="block text-center px-4 py-2.75 rounded-[9px] bg-tps12-label/8 text-tps12-label no-underline text-[13.5px] font-semibold border border-tps12-label/25 transition-[background-color,color] duration-[180ms] hover:bg-tps12-label/18 hover:text-white focus-visible:outline-2 focus-visible:outline-tps12-label focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Starter</a>
      </div>
    </article>
    <article class="relative p-[1.5px] rounded-[16px] bg-white/4">
      <span class="absolute inset-0 p-[1.5px] rounded-[16px] bg-[conic-gradient(from_var(--tps12-ang),--theme(--color-tps12-indigo),--theme(--color-tps12-cyan),--theme(--color-tps12-violet),--theme(--color-tps12-indigo))] [-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [-webkit-mask-composite:xor] [mask-composite:exclude] animate-tps12-spin motion-reduce:animate-none motion-reduce:bg-linear-135 motion-reduce:from-tps12-indigo motion-reduce:to-tps12-cyan" aria-hidden="true"></span>
      <div class="relative flex flex-col h-full px-5 pt-[22px] pb-5 rounded-[14.5px] bg-tps12-body-bg">
        <span class="self-start mb-2.5 px-2.5 py-1 rounded-full bg-linear-135 from-tps12-indigo to-tps12-cyan text-tps12-bg text-[10.5px] font-bold uppercase tracking-[0.08em]">Recommended</span>
        <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps12-label">Builder</h3>
        <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>32<span class="ml-1.5 text-[0.34em] font-medium opacity-65">/mo</span></div>
        <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.95] text-tps12-body">
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">Unlimited projects</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">100 GB storage</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">Priority support</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">API + webhooks</li>
        </ul>
        <a href="#builder" class="block text-center px-4 py-2.75 rounded-[9px] bg-linear-135 from-tps12-indigo to-tps12-cyan text-tps12-bg no-underline text-[13.5px] font-semibold border border-transparent transition-[filter] duration-[180ms] hover:brightness-110 focus-visible:outline-2 focus-visible:outline-tps12-label focus-visible:outline-offset-[3px] motion-reduce:transition-none">Choose Builder</a>
      </div>
    </article>
    <article class="relative p-[1.5px] rounded-[16px] bg-white/4">
      <span class="absolute inset-0 p-[1.5px] rounded-[16px] bg-[conic-gradient(from_var(--tps12-ang),--theme(--color-tps12-ring-a),--theme(--color-tps12-ring-b),--theme(--color-tps12-ring-a))] [-webkit-mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [mask:linear-gradient(#000_0_0)_content-box,linear-gradient(#000_0_0)] [-webkit-mask-composite:xor] [mask-composite:exclude] animate-tps12-spin motion-reduce:animate-none motion-reduce:bg-linear-135 motion-reduce:from-tps12-ring-b motion-reduce:to-tps12-ring-a" aria-hidden="true"></span>
      <div class="relative flex flex-col h-full px-5 pt-[22px] pb-5 rounded-[14.5px] bg-tps12-body-bg">
        <h3 class="m-0 mb-3 text-sm font-bold uppercase tracking-[0.1em] text-tps12-label">Scale</h3>
        <div class="flex items-baseline gap-1 mb-[18px] text-[38px] font-extrabold tracking-[-0.03em] text-white"><em class="not-italic text-[0.5em] pr-0.5 opacity-70">$</em>89<span class="ml-1.5 text-[0.34em] font-medium opacity-65">/mo</span></div>
        <ul class="list-none p-0 m-0 mb-[22px] flex-1 text-[13.5px]/[1.95] text-tps12-body">
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">Everything in Builder</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">SSO + audit logs</li>
          <li class="before:content-['\2713'] before:inline-block before:w-5 before:font-bold before:text-tps12-label">SLA + CSM</li>
        </ul>
        <a href="#scale" class="block text-center px-4 py-2.75 rounded-[9px] bg-tps12-label/8 text-tps12-label no-underline text-[13.5px] font-semibold border border-tps12-label/25 transition-[background-color,color] duration-[180ms] hover:bg-tps12-label/18 hover:text-white focus-visible:outline-2 focus-visible:outline-tps12-label focus-visible:outline-offset-[3px] motion-reduce:transition-none">Talk to sales</a>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";
/* Not a utility, and cannot be: an unregistered custom property has no type,
   so the browser has nothing to interpolate and the rotation does nothing. */

@property --tps12-ang {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@theme {
  --color-tps12-bg: #0a0d1a;
  --color-tps12-bg: oklch(0.16 0.03 265);
  --color-tps12-body-bg: #0f1224;
  --color-tps12-body-bg: oklch(0.2 0.04 270);
  --color-tps12-body: #b8bfd8;
  --color-tps12-body: oklch(0.81 0.03 280);
  --color-tps12-label: #c7d2fe;
  --color-tps12-label: oklch(0.87 0.06 280);
  --color-tps12-ring-a: #1e293b;
  --color-tps12-ring-a: oklch(0.28 0.04 260);
  --color-tps12-ring-b: #475569;
  --color-tps12-ring-b: oklch(0.45 0.04 260);
  --color-tps12-indigo: #6366f1;
  --color-tps12-indigo: oklch(0.59 0.21 277);
  --color-tps12-cyan: #22d3ee;
  --color-tps12-cyan: oklch(0.79 0.14 202);
  --color-tps12-violet: #a855f7;
  --color-tps12-violet: oklch(0.63 0.24 304);
  --font-tps12-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tps12-spin: tps12-spin 6s linear infinite;
}
/* The keyframe body has no utility form; the shorthand above does
   (--animate-tps12-spin → animate-tps12-spin). */

@keyframes tps12-spin {
  to {
    --tps12-ang: 360deg;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is sized correctly in the moment before the
   browser build has compiled its utilities. */

.tps-12 {
  width: 100%;
  min-height: 100svh;
}
```
