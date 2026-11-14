---
source: "codefronts"
url: "https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-pricing-table/"
title: "Tailwind Liquid Glass Pricing Table"
section: "design-styles"
category: "tailwind-liquid-glass-effects"
category_name: "Tailwind Liquid Glass Effects"
description: "Three tiers where only the Pro card is alive: a conic rim rotates around it and its badge pulses, while the flanking plans stay calm frosted glass."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Glass Pricing Table
Source: https://codefronts.com/design-styles/tailwind-liquid-glass-effects/tailwind-liquid-glass-pricing-table/

Three tiers where only the Pro card is alive: a conic rim rotates around it and its badge pulses, while the flanking plans stay calm frosted glass. The port makes the hierarchy legible as a diff &mdash; all three cards share one class string, and Pro adds exactly four utilities.
## HTML
```html
<section class="lgt-10 grid w-full min-h-svh place-items-center p-15 font-lgt10-sans [background:radial-gradient(circle_at_20%_20%,#3a1f5a,#160f2c_60%),radial-gradient(circle_at_80%_80%,#1f3a5a,#160f2c_60%)]" aria-label="Tailwind liquid glass pricing table">
  <div class="grid w-[min(920px,100%)] items-center gap-5.5 grid-cols-[repeat(auto-fit,minmax(min(240px,100%),1fr))]">

    <article class="relative rounded-[22px] border border-white/20 bg-white/8 px-6.5 py-7.5 text-white backdrop-blur-[18px] backdrop-saturate-160 shadow-[inset_0_1px_0_rgba(255,255,255,.3),0_20px_44px_-26px_rgba(0,0,0,.6)]">
      <h3 class="mb-2.5 text-[15px] font-bold uppercase tracking-[0.06em] text-white/80">Starter</h3>
      <p class="mb-5 text-[15px] text-white/70"><span class="text-[40px] font-black tracking-[-0.02em] text-white">$0</span>/mo</p>
      <ul class="mb-6 flex list-none flex-col gap-2.75 p-0">
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">3 projects</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">Community support</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">1 GB storage</li>
      </ul>
      <button type="button" class="w-full cursor-pointer rounded-[12px] border border-white/30 bg-white/12 py-3.25 text-[15px] font-bold text-white transition-[background-color,transform] duration-200 hover:-translate-y-0.5 hover:bg-white/20 focus-visible:-translate-y-0.5 focus-visible:bg-white/20 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Choose Starter</button>
    </article>

    <article class="relative z-2 -translate-y-3.5 rounded-[22px] border border-white/20 bg-white/15 px-6.5 py-7.5 text-white backdrop-blur-[18px] backdrop-saturate-160 shadow-[inset_0_1px_0_rgba(255,255,255,.3),0_20px_44px_-26px_rgba(0,0,0,.6)] before:pointer-events-none before:absolute before:-inset-[1.5px] before:rounded-[inherit] before:p-[1.5px] before:animate-lgt10-spin before:[background:conic-gradient(from_var(--lgt-10-angle),var(--color-lgt10-pro),oklch(0.72_0.17_200),oklch(0.75_0.18_340),var(--color-lgt10-pro))] before:[mask-image:linear-gradient(#000_0_0),linear-gradient(#000_0_0)] before:[mask-clip:content-box,border-box] before:[mask-composite:exclude] motion-reduce:before:animate-none">
      <span class="absolute -top-3.25 left-1/2 -translate-x-1/2 animate-lgt10-glow rounded-full bg-lgt10-pro px-3.5 py-1.5 text-[11px] font-extrabold uppercase tracking-[0.08em] text-white motion-reduce:animate-none">Most popular</span>
      <h3 class="mb-2.5 text-[15px] font-bold uppercase tracking-[0.06em] text-white/80">Pro</h3>
      <p class="mb-5 text-[15px] text-white/70"><span class="text-[40px] font-black tracking-[-0.02em] text-white">$24</span>/mo</p>
      <ul class="mb-6 flex list-none flex-col gap-2.75 p-0">
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">Unlimited projects</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">Priority support</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">100 GB storage</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">Advanced analytics</li>
      </ul>
      <button type="button" class="w-full cursor-pointer rounded-[12px] border border-lgt10-pro/60 bg-linear-to-b from-lgt10-pro-top to-lgt10-pro py-3.25 text-[15px] font-bold text-white transition-[filter,transform] duration-200 hover:-translate-y-0.5 hover:brightness-110 focus-visible:-translate-y-0.5 focus-visible:brightness-110 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Choose Pro</button>
    </article>

    <article class="relative rounded-[22px] border border-white/20 bg-white/8 px-6.5 py-7.5 text-white backdrop-blur-[18px] backdrop-saturate-160 shadow-[inset_0_1px_0_rgba(255,255,255,.3),0_20px_44px_-26px_rgba(0,0,0,.6)]">
      <h3 class="mb-2.5 text-[15px] font-bold uppercase tracking-[0.06em] text-white/80">Team</h3>
      <p class="mb-5 text-[15px] text-white/70"><span class="text-[40px] font-black tracking-[-0.02em] text-white">$69</span>/mo</p>
      <ul class="mb-6 flex list-none flex-col gap-2.75 p-0">
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">Everything in Pro</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">SSO &amp; roles</li>
        <li class="relative pl-6 text-sm text-white before:absolute before:left-0 before:font-extrabold before:text-lgt10-check before:content-['&#10003;']">1 TB storage</li>
      </ul>
      <button type="button" class="w-full cursor-pointer rounded-[12px] border border-white/30 bg-white/12 py-3.25 text-[15px] font-bold text-white transition-[background-color,transform] duration-200 hover:-translate-y-0.5 hover:bg-white/20 focus-visible:-translate-y-0.5 focus-visible:bg-white/20 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Choose Team</button>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --lgt-10-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

@theme {
  --color-lgt10-pro: #9b5cf0;
  --color-lgt10-pro: oklch(0.66 0.2 300);
  --color-lgt10-pro-top: #b47ef5;
  --color-lgt10-pro-top: oklch(0.72 0.17 300);
  --color-lgt10-check: #6ee7b7;
  --color-lgt10-check: oklch(0.78 0.16 160);
  --font-lgt10-sans: 'Manrope', system-ui, sans-serif;
  --animate-lgt10-spin: lgt-10-spin 5s linear infinite;
  --animate-lgt10-glow: lgt-10-glow 2.4s ease-in-out infinite;
}

@keyframes lgt-10-spin {
  to {
    --lgt-10-angle: 360deg;
  }
}

@keyframes lgt-10-glow {
  0%,
    100% {
    box-shadow: 0 0 0 1px rgb(255 255 255 / 0.3), 0 0 16px 1px color-mix(in oklab, var(--color-lgt10-pro) 60%, transparent);
  }

  50% {
    box-shadow: 0 0 0 1px rgb(255 255 255 / 0.4), 0 0 30px 4px color-mix(in oklab, var(--color-lgt10-pro) 80%, transparent);
  }
}
```
