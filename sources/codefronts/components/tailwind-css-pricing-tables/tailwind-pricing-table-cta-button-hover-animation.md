---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-table-cta-button-hover-animation/"
title: "Tailwind Pricing Table CTA Button Hover Animation"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Conversion-grade CTA choreography: hover any plan's button and colour sweeps in from the left, the padding breathes and an arrow slides in beside the label."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pricing Table CTA Button Hover Animation
Source: https://codefronts.com/components/tailwind-css-pricing-tables/tailwind-pricing-table-cta-button-hover-animation/

Conversion-grade CTA choreography: hover any plan's button and colour sweeps in from the left, the padding breathes and an arrow slides in beside the label. Each button sets one arbitrary property — [--tpt08-fill:var(--color-tpt08-seed)] — and v4's before:bg-(--tpt08-fill) shorthand paints the sweep, so one class list powers three differently coloured CTAs.
## HTML
```html
<section class="tpt-08 w-full min-h-svh grid place-items-center bg-tpt08-bg px-5 py-16 font-tpt08-sans text-tpt08-ink antialiased" aria-label="Pricing with animated call-to-action buttons">
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-extrabold tracking-[-0.03em]">Grow your list, not your bill</h2>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article class="flex flex-col rounded-[20px] border border-tpt08-line bg-white p-7 [--tpt08-fill:var(--color-tpt08-seed)]">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt08-mut uppercase">Seed</h3>
        <p class="mt-3 text-[44px] leading-none font-extrabold tracking-[-0.035em]">$19</p>
        <span class="mt-1.5 text-[13px] text-tpt08-mut">per month</span>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt08-body *:flex *:gap-2.5 *:before:font-bold *:before:text-(--tpt08-fill) *:before:content-['✓']"><li>5k contacts</li><li>Email campaigns</li><li>Signup forms</li></ul>
        <a href="#" class="group/cta relative flex min-h-12 items-center justify-center overflow-hidden rounded-xl border-[1.5px] border-tpt08-line px-5 text-sm font-bold text-tpt08-ink no-underline transition-[color,border-color,padding,scale] duration-300 before:absolute before:inset-0 before:origin-left before:scale-x-0 before:bg-(--tpt08-fill) before:transition-transform before:duration-350 before:ease-[cubic-bezier(.6,0,.2,1)] before:content-[''] hover:border-(--tpt08-fill) hover:px-6 hover:text-white hover:before:scale-x-100 focus-visible:border-(--tpt08-fill) focus-visible:text-white focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-(--tpt08-fill) focus-visible:before:scale-x-100 active:scale-[.98] motion-reduce:transition-none motion-reduce:before:transition-none"><span class="relative">Choose Seed</span><span aria-hidden="true" class="relative inline-block w-0 translate-x-2 opacity-0 transition-[width,opacity,translate] duration-300 group-hover/cta:w-5 group-hover/cta:translate-x-1.5 group-hover/cta:opacity-100 group-focus-visible/cta:w-5 group-focus-visible/cta:translate-x-1.5 group-focus-visible/cta:opacity-100">→</span></a>
      </article>
      <article class="relative flex flex-col rounded-[20px] bg-white p-7 shadow-[0_20px_44px_-28px_var(--color-tpt08-bloom)] ring-2 ring-tpt08-bloom [--tpt08-fill:var(--color-tpt08-bloom)]">
        <span class="absolute -top-3 left-7 rounded-full bg-tpt08-bloom px-3 py-1 text-[10.5px] font-bold tracking-[0.08em] text-white uppercase">Most popular</span>
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt08-bloom uppercase">Bloom</h3>
        <p class="mt-3 text-[44px] leading-none font-extrabold tracking-[-0.035em]">$49</p>
        <span class="mt-1.5 text-[13px] text-tpt08-mut">per month</span>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt08-body *:flex *:gap-2.5 *:before:font-bold *:before:text-(--tpt08-fill) *:before:content-['✓']"><li>50k contacts</li><li>Automations</li><li>A/B testing</li><li>Landing pages</li></ul>
        <a href="#" class="group/cta relative flex min-h-12 items-center justify-center overflow-hidden rounded-xl border-[1.5px] border-(--tpt08-fill) px-5 text-sm font-bold text-(--tpt08-fill) no-underline transition-[color,border-color,padding,scale] duration-300 before:absolute before:inset-0 before:origin-left before:scale-x-0 before:bg-(--tpt08-fill) before:transition-transform before:duration-350 before:ease-[cubic-bezier(.6,0,.2,1)] before:content-[''] hover:px-6 hover:text-white hover:before:scale-x-100 focus-visible:text-white focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-(--tpt08-fill) focus-visible:before:scale-x-100 active:scale-[.98] motion-reduce:transition-none motion-reduce:before:transition-none"><span class="relative">Choose Bloom</span><span aria-hidden="true" class="relative inline-block w-0 translate-x-2 opacity-0 transition-[width,opacity,translate] duration-300 group-hover/cta:w-5 group-hover/cta:translate-x-1.5 group-hover/cta:opacity-100 group-focus-visible/cta:w-5 group-focus-visible/cta:translate-x-1.5 group-focus-visible/cta:opacity-100">→</span></a>
      </article>
      <article class="flex flex-col rounded-[20px] border border-tpt08-line bg-white p-7 [--tpt08-fill:var(--color-tpt08-forest)]">
        <h3 class="text-[13px] font-bold tracking-[0.08em] text-tpt08-mut uppercase">Forest</h3>
        <p class="mt-3 text-[44px] leading-none font-extrabold tracking-[-0.035em]">$129</p>
        <span class="mt-1.5 text-[13px] text-tpt08-mut">per month</span>
        <ul class="mt-6 mb-7 grid flex-1 content-start gap-2.5 text-sm text-tpt08-body *:flex *:gap-2.5 *:before:font-bold *:before:text-(--tpt08-fill) *:before:content-['✓']"><li>Unlimited contacts</li><li>Multivariate testing</li><li>Dedicated IP</li></ul>
        <a href="#" class="group/cta relative flex min-h-12 items-center justify-center overflow-hidden rounded-xl border-[1.5px] border-tpt08-line px-5 text-sm font-bold text-tpt08-ink no-underline transition-[color,border-color,padding,scale] duration-300 before:absolute before:inset-0 before:origin-left before:scale-x-0 before:bg-(--tpt08-fill) before:transition-transform before:duration-350 before:ease-[cubic-bezier(.6,0,.2,1)] before:content-[''] hover:border-(--tpt08-fill) hover:px-6 hover:text-white hover:before:scale-x-100 focus-visible:border-(--tpt08-fill) focus-visible:text-white focus-visible:outline-3 focus-visible:outline-offset-3 focus-visible:outline-(--tpt08-fill) focus-visible:before:scale-x-100 active:scale-[.98] motion-reduce:transition-none motion-reduce:before:transition-none"><span class="relative">Choose Forest</span><span aria-hidden="true" class="relative inline-block w-0 translate-x-2 opacity-0 transition-[width,opacity,translate] duration-300 group-hover/cta:w-5 group-hover/cta:translate-x-1.5 group-hover/cta:opacity-100 group-focus-visible/cta:w-5 group-focus-visible/cta:translate-x-1.5 group-focus-visible/cta:opacity-100">→</span></a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-tpt08-line bg-white px-3.5 py-2 font-tpt08-mono text-[11.5px] text-tpt08-mut">[--tpt08-fill:…] · before:bg-(--tpt08-fill) · before:scale-x-0 → 100</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt08-bg: #f6f8f6;
  --color-tpt08-bg: oklch(0.977 0.004 150);
  --color-tpt08-ink: #181c19;
  --color-tpt08-ink: oklch(0.22 0.01 150);
  --color-tpt08-body: #464c47;
  --color-tpt08-body: oklch(0.42 0.01 150);
  --color-tpt08-mut: #636963;
  --color-tpt08-mut: oklch(0.51 0.01 150);
  --color-tpt08-line: #dde2dd;
  --color-tpt08-line: oklch(0.9 0.008 150);
  --color-tpt08-seed: #0f8a68;
  --color-tpt08-seed: oklch(0.55 0.12 170);
  --color-tpt08-bloom: #6a3ce0;
  --color-tpt08-bloom: oklch(0.52 0.21 288);
  --color-tpt08-forest: #1f5aa8;
  --color-tpt08-forest: oklch(0.48 0.14 255);
  --font-tpt08-sans: 'Manrope', system-ui, sans-serif;
  --font-tpt08-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-08 {
  width: 100%;
  min-height: 100svh;
}
```
