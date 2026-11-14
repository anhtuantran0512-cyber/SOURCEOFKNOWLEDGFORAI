---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-bento-grid-hero-section/"
title: "Bento Grid Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "An Apple-style bento hero — one large headline tile with stat, testimonial, rating and download tiles around it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-bento-grid-hero-section/

An Apple-style bento hero — one large headline tile with stat, testimonial, rating and download tiles around it. Matte-ceramic palette: salmon, terracotta, ivory and olive. Tiles lift on hover; whole tiles are clickable where they should be.
## HTML
```html
<section class="ths-19 grid w-full min-h-svh grid-cols-1 gap-3.5 bg-ths19-bg p-4 font-ths19-sans text-ths19-ink [grid-template-areas:'hero'_'stat'_'quote'_'pill'_'cta'] sm:grid-cols-2 sm:p-6 sm:[grid-template-areas:'hero_hero'_'stat_quote'_'pill_cta'] lg:grid-cols-[1.4fr_0.8fr_0.8fr] lg:grid-rows-[1fr_1fr_auto] lg:p-8 lg:[grid-template-areas:'hero_hero_stat'_'hero_hero_quote'_'pill_cta_quote']" aria-label="Bento grid hero">
  <article class="flex min-h-[340px] flex-col justify-between gap-6 rounded-3xl bg-linear-160 from-ths19-salmon to-ths19-terra p-7 [grid-area:hero] sm:p-10">
    <span class="self-start rounded-full bg-ths19-ink px-3 py-1 font-ths19-mono text-[11px] font-bold tracking-[0.16em] text-ths19-bg">V2 — OUT NOW</span>
    <h1 class="max-w-[16ch] font-ths19-serif text-[clamp(38px,5.4vw,68px)] leading-[1.02] font-semibold tracking-[-0.015em] text-balance">The pottery <em class="text-ths19-ox">workbook</em> for serious hands.</h1>
    <div class="flex flex-wrap items-center gap-4">
      <a href="#start" class="inline-flex min-h-12 items-center rounded-full bg-ths19-ink px-6 text-[15px] font-semibold text-ths19-bg transition hover:bg-ths19-ox focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths19-ink motion-reduce:transition-none">Start the kiln →</a>
      <span class="text-sm font-medium text-ths19-ink/80">Free for 30 pieces</span>
    </div>
  </article>
  <article class="flex flex-col justify-between gap-3 rounded-3xl bg-ths19-olive p-6 text-ths19-bg transition hover:-translate-y-1 hover:shadow-[0_18px_30px_-16px_rgb(44_31_21/0.5)] motion-reduce:transition-none [grid-area:stat]">
    <span class="font-ths19-mono text-[11px] tracking-[0.14em] uppercase">Logged this month</span>
    <div><strong class="block font-ths19-serif text-[clamp(48px,5.4vw,72px)] leading-none font-bold">1,400</strong><span class="mt-1 block text-sm">hand-thrown pieces</span></div>
  </article>
  <figure class="flex flex-col justify-between gap-6 rounded-3xl bg-ths19-ink p-6 text-ths19-bg transition hover:-translate-y-1 hover:shadow-[0_18px_30px_-16px_rgb(44_31_21/0.5)] motion-reduce:transition-none [grid-area:quote]">
    <span aria-hidden="true" class="font-ths19-serif text-6xl leading-[0.5] text-ths19-salmon">“</span>
    <blockquote class="font-ths19-serif text-2xl/snug italic">Replaced three notebooks and a chalkboard. My glaze tests finally make sense.</blockquote>
    <figcaption class="flex items-center gap-3 text-xs tracking-[0.04em] text-ths19-bg/80"><span aria-hidden="true" class="grid size-8 place-items-center rounded-full bg-ths19-terra text-[11px] font-bold text-ths19-ink">MR</span>Mireya R. · Studio Verde</figcaption>
  </figure>
  <article class="flex items-center justify-between gap-3 rounded-3xl border-2 border-ths19-ink bg-ths19-bg px-6 py-5 [grid-area:pill]">
    <span><span role="img" aria-label="Rated 4.9 out of 5" class="text-xl font-extrabold text-ths19-gold">★ 4.9</span><span class="block text-xs text-ths19-ink/75">2,310 ratings</span></span>
    <span class="font-ths19-mono text-[11px] tracking-[0.1em] uppercase">App Store</span>
  </article>
  <a href="#android" class="flex min-h-20 items-center justify-between rounded-3xl bg-ths19-terra px-6 text-[15px] font-bold text-ths19-ink transition hover:-translate-y-1 hover:bg-ths19-salmon focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-ths19-ink motion-reduce:transition-none [grid-area:cta]">Get it on Android <span aria-hidden="true" class="grid size-9 place-items-center rounded-full bg-ths19-ink text-ths19-bg">→</span></a>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths19-bg: #f5ebde;
  --color-ths19-bg: oklch(0.944 0.02 74.7);
  --color-ths19-ink: #2c1f15;
  --color-ths19-ink: oklch(0.252 0.027 58.7);
  --color-ths19-salmon: #f4a48b;
  --color-ths19-salmon: oklch(0.791 0.102 38.1);
  --color-ths19-terra: #d97766;
  --color-ths19-terra: oklch(0.675 0.126 31);
  --color-ths19-ox: #6b1f12;
  --color-ths19-ox: oklch(0.359 0.111 32.2);
  --color-ths19-olive: #56702f;
  --color-ths19-olive: oklch(0.509 0.097 127.7);
  --color-ths19-gold: #9c7a2a;
  --color-ths19-gold: oklch(0.598 0.105 85.1);
  --font-ths19-serif: 'Cormorant Garamond', Georgia, serif;
  --font-ths19-sans: 'Geist', system-ui, sans-serif;
  --font-ths19-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-19 {
  width: 100%;
  min-height: 100svh;
}
```
