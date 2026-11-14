---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-classic-three-tier-pricing-section/"
title: "Tailwind Classic Three Tier Pricing Section"
section: "layouts"
category: "tailwind-css-pricing-sections"
category_name: "Tailwind CSS Pricing Sections"
description: "The conversion-tested baseline — three equal tiers (Starter / Team / Business) on a forest ground with one emerald accent — ported to utilities."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Classic Three Tier Pricing Section
Source: https://codefronts.com/layouts/tailwind-css-pricing-sections/tailwind-classic-three-tier-pricing-section/

The conversion-tested baseline — three equal tiers (Starter / Team / Business) on a forest ground with one emerald accent — ported to utilities. The whole stylesheet reduces to @theme tokens plus the masked check-mark URL, because minmax(0,1fr), the flex-1 CTA push and the reduced-motion fallback all have utility forms that live on the elements that need them.
## HTML
```html
<section class="tps-01 w-full min-h-svh bg-tps01-bg font-tps01-sans text-tps01-ink px-[clamp(20px,4vw,40px)] py-[clamp(28px,5vw,56px)]" aria-label="Pricing">
  <header class="text-center mb-[clamp(20px,4vw,40px)]">
    <span class="inline-block mb-3 text-xs font-semibold tracking-[0.18em] uppercase text-tps01-acc">Pricing</span>
    <h2 class="m-0 mb-2 text-[clamp(22px,3.4vw,34px)] font-bold tracking-[-0.01em] text-pretty">Pick the plan that fits today.</h2>
    <p class="m-0 text-sm text-tps01-mut">Upgrade, downgrade, or cancel any time. No fine print.</p>
  </header>
  <div class="grid grid-cols-1 md:grid-cols-[repeat(3,minmax(0,1fr))] gap-4 max-w-[460px] md:max-w-[980px] mx-auto">
    <article class="flex flex-col p-5 pt-5.5 rounded-2xl bg-tps01-card border border-tps01-edge transition-[border-color,translate] duration-200 hover:border-tps01-acc hover:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <h3 class="m-0 mb-1 text-[15px] font-bold uppercase tracking-[0.04em] text-tps01-acc">Starter</h3>
      <p class="m-0 mb-4.5 min-h-0 md:min-h-9.5 text-[13px] leading-normal text-tps01-mut">For solo builders shipping their first thing.</p>
      <div class="flex items-baseline gap-1.5 mb-4.5 pb-4.5 border-b border-dashed border-tps01-edge2">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps01-price">$9</span><span class="text-[13px] text-tps01-mut">/ month</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 flex flex-col">
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>1 project</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>2 GB storage</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Community support</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Basic analytics</li>
      </ul>
      <a href="#starter" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline text-tps01-acc bg-tps01-ctabg border border-tps01-ctaedge transition-[background-color,color] duration-200 hover:bg-tps01-acc hover:text-tps01-bg focus-visible:outline-2 focus-visible:outline-tps01-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Start free &rarr;</a>
    </article>
    <article class="flex flex-col p-5 pt-5.5 rounded-2xl bg-tps01-card border border-tps01-edge transition-[border-color,translate] duration-200 hover:border-tps01-acc hover:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <h3 class="m-0 mb-1 text-[15px] font-bold uppercase tracking-[0.04em] text-tps01-acc">Team</h3>
      <p class="m-0 mb-4.5 min-h-0 md:min-h-9.5 text-[13px] leading-normal text-tps01-mut">For small teams who need to ship together.</p>
      <div class="flex items-baseline gap-1.5 mb-4.5 pb-4.5 border-b border-dashed border-tps01-edge2">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps01-price">$29</span><span class="text-[13px] text-tps01-mut">/ month</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 flex flex-col">
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>10 projects</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>50 GB storage</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Email support</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Team analytics</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Role-based access</li>
      </ul>
      <a href="#team" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline text-tps01-acc bg-tps01-ctabg border border-tps01-ctaedge transition-[background-color,color] duration-200 hover:bg-tps01-acc hover:text-tps01-bg focus-visible:outline-2 focus-visible:outline-tps01-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Start 14-day trial &rarr;</a>
    </article>
    <article class="flex flex-col p-5 pt-5.5 rounded-2xl bg-tps01-card border border-tps01-edge transition-[border-color,translate] duration-200 hover:border-tps01-acc hover:-translate-y-0.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <h3 class="m-0 mb-1 text-[15px] font-bold uppercase tracking-[0.04em] text-tps01-acc">Business</h3>
      <p class="m-0 mb-4.5 min-h-0 md:min-h-9.5 text-[13px] leading-normal text-tps01-mut">For growing companies that need governance.</p>
      <div class="flex items-baseline gap-1.5 mb-4.5 pb-4.5 border-b border-dashed border-tps01-edge2">
        <span class="text-[38px] font-extrabold tracking-[-0.02em] text-tps01-price">$79</span><span class="text-[13px] text-tps01-mut">/ month</span>
      </div>
      <ul class="flex-1 list-none p-0 m-0 mb-5.5 flex flex-col">
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Unlimited projects</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>500 GB storage</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Priority support</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>Advanced analytics</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>SSO + audit logs</li>
        <li class="flex items-center gap-2 py-1.5 text-[13.5px] text-tps01-body"><i class="w-3.5 h-3.5 shrink-0 bg-tps01-acc [mask:var(--tps01-check)_center/contain_no-repeat]" aria-hidden="true"></i>SOC 2 ready</li>
      </ul>
      <a href="#business" class="block text-center px-4 py-2.75 rounded-lg text-[13.5px] font-semibold no-underline text-tps01-acc bg-tps01-ctabg border border-tps01-ctaedge transition-[background-color,color] duration-200 hover:bg-tps01-acc hover:text-tps01-bg focus-visible:outline-2 focus-visible:outline-tps01-acc focus-visible:outline-offset-3 motion-reduce:transition-none">Talk to sales &rarr;</a>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tps01-bg: #07120e;
  --color-tps01-bg: oklch(0.16 0.02 160);
  --color-tps01-card: #0d1f18;
  --color-tps01-card: oklch(0.22 0.03 163);
  --color-tps01-edge: #1f4536;
  --color-tps01-edge: oklch(0.36 0.05 163);
  --color-tps01-edge2: #2a5a46;
  --color-tps01-edge2: oklch(0.43 0.06 163);
  --color-tps01-ctabg: #123326;
  --color-tps01-ctabg: oklch(0.27 0.05 163);
  --color-tps01-ctaedge: #276b4f;
  --color-tps01-ctaedge: oklch(0.47 0.08 163);
  --color-tps01-ink: #e7f5ee;
  --color-tps01-ink: oklch(0.95 0.02 163);
  --color-tps01-body: #d2e9dc;
  --color-tps01-body: oklch(0.9 0.03 163);
  --color-tps01-price: #f0fff7;
  --color-tps01-price: oklch(0.98 0.02 163);
  --color-tps01-mut: #9bb5a8;
  --color-tps01-mut: oklch(0.73 0.03 163);
  --color-tps01-acc: #34d399;
  --color-tps01-acc: oklch(0.79 0.16 163);
  --font-tps01-sans: 'Inter', system-ui, -apple-system, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the section is correctly sized in the moment before the
   browser build has compiled its utilities. It also carries the check-mark mask
   source: a data URI cannot survive an arbitrary value's quote and space rules,
   and a mask source is not a design-scale value. */

.tps-01 {
  width: 100%;
  min-height: 100svh;
  --tps01-check: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path fill='black' d='M6.5 11.5 3 8l1-1 2.5 2.5L12 4l1 1z'/></svg>");
}
```
