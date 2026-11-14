---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-centered-hero-section-serif-headline/"
title: "Centered Hero Section in Tailwind CSS with Serif Headline & Dual CTA"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "The artisanal SaaS hero — pill eyebrow, a tall Instrument Serif headline, prose subhead, a terracotta primary CTA beside a quiet ghost button and a small…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Centered Hero Section in Tailwind CSS with Serif Headline & Dual CTA
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-centered-hero-section-serif-headline/

The artisanal SaaS hero — pill eyebrow, a tall Instrument Serif headline, prose subhead, a terracotta primary CTA beside a quiet ghost button and a small trust row. Sage on warm cream, ported whole into utilities with a zero-JS staggered entrance via starting:.
## HTML
```html
<section class="ths-01 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths01-bg bg-[radial-gradient(60%_80%_at_50%_0%,var(--color-ths01-glow),transparent_70%)] px-5 py-16 font-ths01-sans text-ths01-ink sm:px-14" aria-label="Centered hero section">
  <div class="w-full max-w-[42rem] text-center">
    <p class="inline-flex items-center gap-2.5 rounded-full border border-ths01-ink/12 bg-white/70 px-3.5 py-1.5 font-ths01-mono text-[11px] font-medium tracking-[0.16em] text-ths01-sage uppercase transition duration-700 starting:translate-y-3 starting:opacity-0">
      <span aria-hidden="true" class="size-1.5 rounded-full bg-ths01-acc"></span>A new kind of workspace
    </p>
    <h1 class="mt-6 font-ths01-serif text-[clamp(44px,7.4vw,88px)] leading-[0.98] font-normal tracking-[-0.02em] text-balance text-ths01-ink transition delay-100 duration-700 starting:translate-y-3 starting:opacity-0">Make small things <em class="text-ths01-acc">that matter.</em></h1>
    <p class="mx-auto mt-6 max-w-[30rem] text-[17px] leading-relaxed text-pretty text-ths01-body transition delay-200 duration-700 starting:translate-y-3 starting:opacity-0">The toolkit for craftspeople who treat the work, the customer and the calendar with the same care.</p>
    <div class="mt-9 flex flex-wrap justify-center gap-3 transition delay-300 duration-700 starting:translate-y-3 starting:opacity-0">
      <a href="#start" class="group inline-flex min-h-12 items-center gap-2 rounded-full bg-ths01-acc px-7 text-[15px] font-semibold text-ths01-cream shadow-[0_1px_0_var(--color-ths01-deep),0_14px_28px_-14px_var(--color-ths01-acc)] transition hover:-translate-y-px hover:bg-ths01-deep focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-ths01-acc motion-reduce:transition-none">Start free trial <span aria-hidden="true" class="transition group-hover:translate-x-0.5">→</span></a>
      <a href="#tour" class="inline-flex min-h-12 items-center gap-2.5 rounded-full border border-ths01-ink/25 px-6 text-[15px] font-semibold text-ths01-ink transition hover:border-ths01-ink hover:bg-ths01-ink hover:text-ths01-bg focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-ths01-ink motion-reduce:transition-none"><span aria-hidden="true" class="grid size-5 place-items-center rounded-full bg-ths01-ink/10 text-[9px]">▶</span>Watch the tour</a>
    </div>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-x-4 gap-y-2 font-ths01-mono text-[11.5px] tracking-[0.04em] text-ths01-mut transition delay-500 duration-700 starting:opacity-0">
      <span class="flex -space-x-2" aria-hidden="true">
        <span class="grid size-7 place-items-center rounded-full bg-ths01-sage text-[10px] font-semibold text-ths01-cream ring-2 ring-ths01-bg">AK</span>
        <span class="grid size-7 place-items-center rounded-full bg-ths01-acc text-[10px] font-semibold text-ths01-cream ring-2 ring-ths01-bg">MJ</span>
        <span class="grid size-7 place-items-center rounded-full bg-ths01-ink text-[10px] font-semibold text-ths01-cream ring-2 ring-ths01-bg">RS</span>
      </span>
      <span>Free for 14 days · no card · cancel any time</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths01-bg: #f5f1e6;
  --color-ths01-bg: oklch(0.958 0.015 90.2);
  --color-ths01-glow: #ecd9c2;
  --color-ths01-glow: oklch(0.895 0.037 72.6);
  --color-ths01-cream: #fff8ed;
  --color-ths01-cream: oklch(0.982 0.016 79.4);
  --color-ths01-ink: #1c261b;
  --color-ths01-ink: oklch(0.255 0.025 142.5);
  --color-ths01-body: #465043;
  --color-ths01-body: oklch(0.418 0.025 138.5);
  --color-ths01-mut: #5f6658;
  --color-ths01-mut: oklch(0.5 0.023 129);
  --color-ths01-sage: #566a46;
  --color-ths01-sage: oklch(0.498 0.06 131.9);
  --color-ths01-acc: #b44a31;
  --color-ths01-acc: oklch(0.545 0.144 34.6);
  --color-ths01-deep: #8a3722;
  --color-ths01-deep: oklch(0.448 0.119 35.3);
  --font-ths01-serif: 'Instrument Serif', Georgia, serif;
  --font-ths01-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-ths01-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-01 {
  width: 100%;
  min-height: 100svh;
}
```
