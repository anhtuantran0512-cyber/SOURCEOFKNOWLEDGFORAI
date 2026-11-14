---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-sibling-de-emphasis-pricing-grid-has-hover/"
title: "Tailwind Sibling De-emphasis Pricing Grid with has-hover"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Hover one pricing tier and every other tier blurs, dims and shrinks away &mdash; the whole effect is one relational selector, expressed here as…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sibling De-emphasis Pricing Grid with has-hover
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-sibling-de-emphasis-pricing-grid-has-hover/

Hover one pricing tier and every other tier blurs, dims and shrinks away &mdash; the whole effect is one relational selector, expressed here as has-hover:*:not-hover: on the grid. Three cards ship because the pattern only reads with siblings to react against.
## HTML
```html
<section class="tch-05 w-full min-h-svh grid place-items-center bg-tch05-bg bg-[radial-gradient(circle_at_50%_0%,#1a1e29,#0a0b10_70%)] font-tch05-sans p-8">
  <div class="flex flex-wrap justify-center gap-5 *:transition *:duration-400 *:ease-[cubic-bezier(0.16,1,0.3,1)] has-hover:*:not-hover:blur-[3px] has-hover:*:not-hover:opacity-45 has-hover:*:not-hover:scale-97 has-focus-within:*:not-focus-within:blur-[3px] has-focus-within:*:not-focus-within:opacity-45 has-focus-within:*:not-focus-within:scale-97 motion-reduce:*:transition-none motion-reduce:has-hover:*:not-hover:scale-100">
    <article class="relative w-[220px] min-h-[400px] p-[1.8rem] rounded-[20px] bg-tch05-card border border-white/8 flex flex-col text-tch05-ink cursor-pointer hover:-translate-y-3 hover:scale-105 hover:z-2 hover:border-tch05-acc/50 hover:shadow-[0_30px_60px_rgb(0_0_0/0.5)] focus-within:-translate-y-3 focus-within:scale-105 focus-within:z-2 motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
      <span class="text-[0.72rem] tracking-[0.18em] uppercase text-tch05-mut">Starter</span>
      <div class="font-bold text-[2.6rem] leading-none mt-2.5 mb-1">$0<span class="text-[0.9rem] font-normal text-tch05-mut">/mo</span></div>
      <ul class="list-none my-6 p-0 flex flex-col gap-2.5 text-[0.82rem] text-tch05-body *:before:content-['✓'] *:before:mr-2 *:before:font-bold *:before:text-tch05-acc">
        <li>1 project</li><li>Community support</li><li>1 GB storage</li>
      </ul>
      <a href="#" class="mt-auto flex items-center justify-center min-h-11 rounded-[10px] border border-white/15 text-center font-semibold text-[0.85rem] text-tch05-ink no-underline transition-colors duration-200 hover:bg-white/8 focus-visible:outline-2 focus-visible:outline-tch05-acc focus-visible:outline-offset-2">Get started</a>
    </article>

    <article class="relative w-[220px] min-h-[400px] p-[1.8rem] rounded-[20px] bg-tch05-card border border-tch05-acc/30 flex flex-col text-tch05-ink cursor-pointer hover:-translate-y-3 hover:scale-105 hover:z-2 hover:border-tch05-acc/50 hover:shadow-[0_30px_60px_rgb(0_0_0/0.5)] focus-within:-translate-y-3 focus-within:scale-105 focus-within:z-2 motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
      <span class="text-[0.72rem] tracking-[0.18em] uppercase text-tch05-acc">Pro · Popular</span>
      <div class="font-bold text-[2.6rem] leading-none mt-2.5 mb-1">$24<span class="text-[0.9rem] font-normal text-tch05-mut">/mo</span></div>
      <ul class="list-none my-6 p-0 flex flex-col gap-2.5 text-[0.82rem] text-tch05-body *:before:content-['✓'] *:before:mr-2 *:before:font-bold *:before:text-tch05-acc">
        <li>Unlimited projects</li><li>Priority support</li><li>100 GB storage</li><li>Advanced analytics</li>
      </ul>
      <a href="#" class="mt-auto flex items-center justify-center min-h-11 rounded-[10px] bg-linear-to-r from-tch05-acc to-tch05-acc2 text-center font-semibold text-[0.85rem] text-white no-underline transition-[filter] duration-200 hover:brightness-110 focus-visible:outline-2 focus-visible:outline-white focus-visible:outline-offset-2">Start free trial</a>
    </article>

    <article class="relative w-[220px] min-h-[400px] p-[1.8rem] rounded-[20px] bg-tch05-card border border-white/8 flex flex-col text-tch05-ink cursor-pointer hover:-translate-y-3 hover:scale-105 hover:z-2 hover:border-tch05-acc/50 hover:shadow-[0_30px_60px_rgb(0_0_0/0.5)] focus-within:-translate-y-3 focus-within:scale-105 focus-within:z-2 motion-reduce:hover:translate-y-0 motion-reduce:hover:scale-100">
      <span class="text-[0.72rem] tracking-[0.18em] uppercase text-tch05-mut">Team</span>
      <div class="font-bold text-[2.6rem] leading-none mt-2.5 mb-1">$60<span class="text-[0.9rem] font-normal text-tch05-mut">/mo</span></div>
      <ul class="list-none my-6 p-0 flex flex-col gap-2.5 text-[0.82rem] text-tch05-body *:before:content-['✓'] *:before:mr-2 *:before:font-bold *:before:text-tch05-acc">
        <li>Everything in Pro</li><li>SSO &amp; roles</li><li>1 TB storage</li>
      </ul>
      <a href="#" class="mt-auto flex items-center justify-center min-h-11 rounded-[10px] border border-white/15 text-center font-semibold text-[0.85rem] text-tch05-ink no-underline transition-colors duration-200 hover:bg-white/8 focus-visible:outline-2 focus-visible:outline-tch05-acc focus-visible:outline-offset-2">Contact sales</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch05-bg: #0a0b10;
  --color-tch05-bg: oklch(0.11 0.01 265);
  --color-tch05-card: #14171f;
  --color-tch05-card: oklch(0.17 0.012 265);
  --color-tch05-ink: #e6e9f0;
  --color-tch05-ink: oklch(0.92 0.008 265);
  --color-tch05-body: #aab2c4;
  --color-tch05-body: oklch(0.75 0.02 265);
  --color-tch05-mut: #8a93a8;
  --color-tch05-mut: oklch(0.64 0.02 265);
  --color-tch05-acc: #7aa0ff;
  --color-tch05-acc: oklch(0.72 0.15 265);
  --color-tch05-acc2: #7a50ff;
  --color-tch05-acc2: oklch(0.56 0.25 285);
  --font-tch05-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tch-05 {
  width: 100%;
  min-height: 100svh;
}
```
