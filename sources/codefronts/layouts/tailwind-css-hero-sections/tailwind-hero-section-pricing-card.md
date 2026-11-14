---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-pricing-card/"
title: "Tailwind CSS Hero Section with Pricing Card"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A heritage-banking, pricing-led hero — copy left, a single-tier brass-on-forest pricing card right, now with a zero-JS monthly / yearly toggle built from…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Hero Section with Pricing Card
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-pricing-card/

A heritage-banking, pricing-led hero — copy left, a single-tier brass-on-forest pricing card right, now with a zero-JS monthly / yearly toggle built from radio inputs and group-has-[:checked]. The 37signals one-price pitch with a vintage finance feel.
## HTML
```html
<section class="ths-22 grid w-full min-h-svh items-center gap-12 bg-ths22-bg bg-[radial-gradient(70%_60%_at_100%_50%,var(--color-ths22-glow),transparent_70%)] px-5 py-16 font-ths22-sans text-ths22-forest sm:px-12 lg:grid-cols-[1.05fr_1fr] lg:gap-16" aria-label="Hero with pricing card">
  <div class="max-w-xl">
    <span class="block font-ths22-body text-lg text-ths22-brass italic">— Est. 1924 · still independent</span>
    <h1 class="mt-3 font-ths22-serif text-[clamp(34px,4.8vw,54px)] leading-[1.08] font-bold tracking-[-0.015em] text-balance">One ledger. <em class="text-ths22-brass">One price.</em> One ridiculously responsive team.</h1>
    <p class="mt-5 max-w-md text-base/relaxed text-ths22-body">The bookkeeping software trusted by family-owned businesses since before “SaaS” was a word.</p>
    <p class="mt-8 flex items-center gap-3 text-sm text-ths22-body"><span aria-hidden="true" class="flex -space-x-2"><span class="size-7 rounded-full bg-ths22-brass ring-2 ring-ths22-bg"></span><span class="size-7 rounded-full bg-ths22-forest ring-2 ring-ths22-bg"></span><span class="size-7 rounded-full bg-ths22-moss ring-2 ring-ths22-bg"></span></span>Used by 9,400 family businesses</p>
  </div>
  <article class="group/card w-full max-w-md justify-self-center border-2 border-ths22-brass bg-ths22-forest p-7 text-ths22-bg shadow-[inset_0_0_0_4px_var(--color-ths22-forest),inset_0_0_0_5px_rgb(138_122_58/0.45),0_30px_60px_-30px_rgb(26_51_34/0.6)] sm:p-9 lg:justify-self-end">
    <header class="flex items-center justify-between border-b border-ths22-brass pb-4 font-ths22-serif text-[13px] font-bold tracking-[0.16em] uppercase">
      <span>The Members' Plan</span>
      <span class="border border-ths22-brass px-2 py-0.5 font-ths22-mono text-[10px] tracking-[0.12em] text-ths22-gilt">No tiers</span>
    </header>
    <fieldset class="mt-5 grid grid-cols-2 gap-1 rounded-full border border-ths22-brass/60 p-1 font-ths22-mono text-xs font-bold tracking-[0.08em]">
      <legend class="sr-only">Billing period</legend>
      <label class="flex min-h-10 cursor-pointer items-center justify-center rounded-full text-ths22-gilt transition has-checked:bg-ths22-gilt has-checked:text-ths22-forest has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ths22-gilt"><input type="radio" name="ths22-period" id="ths22-mo" class="sr-only" checked>MONTHLY</label>
      <label class="flex min-h-10 cursor-pointer items-center justify-center gap-1.5 rounded-full text-ths22-gilt transition has-checked:bg-ths22-gilt has-checked:text-ths22-forest has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ths22-gilt"><input type="radio" name="ths22-period" id="ths22-yr" class="sr-only">YEARLY <span class="rounded-full bg-ths22-moss px-1.5 py-0.5 text-[9px] text-white">−20%</span></label>
    </fieldset>
    <div class="mt-6 flex items-baseline gap-1.5 group-has-[#ths22-yr:checked]/card:hidden">
      <span class="text-2xl font-bold text-ths22-gilt">$</span><strong class="font-ths22-serif text-[clamp(60px,6.4vw,84px)] leading-none font-extrabold">49</strong><span class="text-sm text-ths22-gilt">/ month, all in</span>
    </div>
    <div class="mt-6 hidden items-baseline gap-1.5 group-has-[#ths22-yr:checked]/card:flex">
      <span class="text-2xl font-bold text-ths22-gilt">$</span><strong class="font-ths22-serif text-[clamp(60px,6.4vw,84px)] leading-none font-extrabold">39</strong><span class="text-sm text-ths22-gilt">/ month, billed $468 yearly</span>
    </div>
    <ul class="mt-6 space-y-2.5 text-[15px] text-ths22-list">
      <li class="flex gap-2.5 before:font-extrabold before:text-ths22-gilt before:content-['✓']">Unlimited invoices</li>
      <li class="flex gap-2.5 before:font-extrabold before:text-ths22-gilt before:content-['✓']">Multi-entity ledger</li>
      <li class="flex gap-2.5 before:font-extrabold before:text-ths22-gilt before:content-['✓']">Audit-ready exports</li>
      <li class="flex gap-2.5 before:font-extrabold before:text-ths22-gilt before:content-['✓']">A real human for support</li>
    </ul>
    <a href="#join" class="mt-8 flex min-h-12 items-center justify-center bg-ths22-gilt text-[15px] font-extrabold tracking-[0.04em] text-ths22-forest transition hover:bg-ths22-bg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths22-gilt motion-reduce:transition-none">Become a member</a>
    <p class="mt-3 text-center text-xs text-ths22-list">30-day money-back · cancel any time</p>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths22-bg: #f5ecd8;
  --color-ths22-bg: oklch(0.945 0.028 86.6);
  --color-ths22-glow: #e9dcb9;
  --color-ths22-glow: oklch(0.896 0.048 90.1);
  --color-ths22-forest: #1a3322;
  --color-ths22-forest: oklch(0.295 0.044 153.2);
  --color-ths22-moss: #3f6b45;
  --color-ths22-moss: oklch(0.485 0.078 147.5);
  --color-ths22-body: #445442;
  --color-ths22-body: oklch(0.427 0.035 142);
  --color-ths22-brass: #7a6a2e;
  --color-ths22-brass: oklch(0.527 0.082 94.5);
  --color-ths22-gilt: #c9b26a;
  --color-ths22-gilt: oklch(0.768 0.096 92.3);
  --color-ths22-list: #ccd6c8;
  --color-ths22-list: oklch(0.865 0.022 136.6);
  --font-ths22-serif: 'Playfair Display', Georgia, serif;
  --font-ths22-body: 'Cormorant Garamond', Georgia, serif;
  --font-ths22-sans: 'Geist', system-ui, sans-serif;
  --font-ths22-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-22 {
  width: 100%;
  min-height: 100svh;
}
```
