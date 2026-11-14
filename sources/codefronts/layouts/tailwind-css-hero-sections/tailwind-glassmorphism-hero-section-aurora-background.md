---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-glassmorphism-hero-section-aurora-background/"
title: "Glassmorphism Hero Section in Tailwind CSS with Aurora Background"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A frosted-glass card floating over a slowly rotating spa aurora — pale mint, champagne gold and soft rose."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Hero Section in Tailwind CSS with Aurora Background
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-glassmorphism-hero-section-aurora-background/

A frosted-glass card floating over a slowly rotating spa aurora — pale mint, champagne gold and soft rose. Wellness / luxury beauty editorial, with a solid-card fallback via supports-[backdrop-filter]: so it never turns illegible.
## HTML
```html
<section class="ths-04 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths04-bg bg-[radial-gradient(circle_at_20%_20%,var(--color-ths04-mint),transparent_50%),radial-gradient(circle_at_85%_30%,var(--color-ths04-rose),transparent_55%),radial-gradient(circle_at_50%_90%,var(--color-ths04-champ),transparent_50%)] px-5 py-16 font-ths04-sans text-ths04-ink sm:px-14" aria-label="Glassmorphism hero over aurora">
  <div aria-hidden="true" class="absolute -inset-[10%] -z-10 animate-ths04-spin bg-[conic-gradient(from_90deg,var(--color-ths04-mint),var(--color-ths04-rose),var(--color-ths04-champ),var(--color-ths04-mint))] opacity-60 blur-[56px] motion-reduce:animate-none"></div>
  <article class="w-full max-w-[34rem] rounded-[28px] border border-white/90 bg-white/85 p-8 text-center shadow-[inset_0_1px_0_white,0_30px_70px_-20px_rgb(160_110_80/0.35)] backdrop-blur-xl backdrop-saturate-150 transition duration-700 starting:translate-y-4 starting:opacity-0 supports-[backdrop-filter:blur(1px)]:bg-white/50 sm:p-12">
    <span class="font-ths04-serif text-base text-ths04-gold italic">A daily ritual</span>
    <h1 class="mt-3 font-ths04-serif text-[clamp(36px,5.6vw,58px)] leading-[1.02] font-medium tracking-[-0.015em] text-balance">Skincare without <em class="font-semibold text-ths04-gold">the homework.</em></h1>
    <p class="mx-auto mt-5 max-w-[24rem] text-[15px] leading-relaxed text-ths04-body">Three minutes. Two products. One routine that fits the life you actually live.</p>
    <a href="#start" class="mt-8 inline-flex min-h-12 items-center rounded-full bg-ths04-ink px-8 text-sm font-semibold tracking-[0.04em] text-ths04-bg transition hover:bg-ths04-gold focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths04-ink motion-reduce:transition-none">Find your routine</a>
    <ul class="mt-8 flex flex-wrap justify-center gap-x-5 gap-y-2 border-t border-ths04-ink/10 pt-6 text-xs font-medium text-ths04-body">
      <li class="flex items-center gap-1.5"><span aria-hidden="true" class="text-ths04-gold">✦</span>Dermatologist-tested</li>
      <li class="flex items-center gap-1.5"><span aria-hidden="true" class="text-ths04-gold">✦</span>Fragrance-free</li>
      <li class="flex items-center gap-1.5"><span aria-hidden="true" class="text-ths04-gold">✦</span>Refillable</li>
    </ul>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths04-bg: #faf6ed;
  --color-ths04-bg: oklch(0.974 0.013 86.8);
  --color-ths04-mint: #d6f0e0;
  --color-ths04-mint: oklch(0.932 0.035 158.7);
  --color-ths04-rose: #f9d4c8;
  --color-ths04-rose: oklch(0.898 0.045 38.8);
  --color-ths04-champ: #f3e3c0;
  --color-ths04-champ: oklch(0.92 0.049 86.3);
  --color-ths04-ink: #2a2818;
  --color-ths04-ink: oklch(0.274 0.028 101.9);
  --color-ths04-body: #5c5846;
  --color-ths04-body: oklch(0.459 0.028 96.9);
  --color-ths04-gold: #946f40;
  --color-ths04-gold: oklch(0.568 0.079 71.7);
  --font-ths04-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --animate-ths04-spin: ths04-spin 30s linear infinite;

  @keyframes ths04-spin {
    to {
      transform: rotate(360deg);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-04 {
  width: 100%;
  min-height: 100svh;
}
```
