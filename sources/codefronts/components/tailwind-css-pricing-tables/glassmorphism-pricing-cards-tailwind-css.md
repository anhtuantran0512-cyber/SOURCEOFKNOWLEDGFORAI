---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-pricing-tables/glassmorphism-pricing-cards-tailwind-css/"
title: "Glassmorphism Pricing Cards in Tailwind CSS"
section: "components"
category: "tailwind-css-pricing-tables"
category_name: "Tailwind CSS Pricing Tables"
description: "Frosted-glass pricing over slowly drifting colour blobs — the aesthetic AI and fintech launches keep shipping."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Pricing Cards in Tailwind CSS
Source: https://codefronts.com/components/tailwind-css-pricing-tables/glassmorphism-pricing-cards-tailwind-css/

Frosted-glass pricing over slowly drifting colour blobs — the aesthetic AI and fintech launches keep shipping. backdrop-blur-[22px] backdrop-saturate-150 does the frosting, the moving blobs prove the glass is real, and two arbitrary variants handle the edge cases: supports-[backdrop-filter:blur(1px)]: for the enhancement and [@media(prefers-reduced-transparency:reduce)]: for readers who need solid cards.
## HTML
```html
<section class="tpt-15 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-tpt15-bg px-5 py-16 font-tpt15-sans text-tpt15-ink antialiased" aria-label="Frosted glass pricing cards">
  <div aria-hidden="true" class="pointer-events-none absolute -top-[12%] -left-[8%] -z-10 size-[44vmax] animate-tpt15-drift-1 rounded-full bg-[radial-gradient(circle,var(--color-tpt15-blob1),transparent_65%)] opacity-60 blur-[60px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute -right-[6%] -bottom-[18%] -z-10 size-[44vmax] animate-tpt15-drift-2 rounded-full bg-[radial-gradient(circle,var(--color-tpt15-blob2),transparent_65%)] opacity-60 blur-[60px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="pointer-events-none absolute top-[30%] left-[44%] -z-10 size-[40vmax] animate-tpt15-drift-3 rounded-full bg-[radial-gradient(circle,var(--color-tpt15-blob3),transparent_65%)] opacity-50 blur-[60px] motion-reduce:animate-none"></div>
  <div class="grid w-full max-w-5xl justify-items-center gap-10">
    <h2 class="text-center text-[clamp(26px,3.8vw,40px)] font-bold tracking-[-0.03em] text-balance">Clear pricing. Frosted, not foggy.</h2>
    <div class="grid w-full gap-5 md:grid-cols-3">
      <article class="flex flex-col gap-4 rounded-3xl border border-white/16 border-t-white/40 bg-tpt15-solid p-8 shadow-[0_24px_60px_-30px_oklch(0_0_0/0.8)] backdrop-blur-[22px] backdrop-saturate-150 transition-[translate,background-color] duration-300 supports-[backdrop-filter:blur(1px)]:bg-white/8 hover:-translate-y-1.5 supports-[backdrop-filter:blur(1px)]:hover:bg-white/12 [@media(prefers-reduced-transparency:reduce)]:bg-tpt15-solid motion-reduce:hover:translate-y-0">
        <h3 class="text-[13px] font-semibold tracking-[0.1em] text-tpt15-mut uppercase">Glass</h3>
        <p class="text-[46px] leading-none font-bold tracking-[-0.035em]">$18<small class="text-[15px] font-medium tracking-normal text-tpt15-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt15-body *:flex *:gap-2.5 *:before:text-[11px] *:before:leading-5 *:before:text-white/70 *:before:content-['✦']"><li>5 seats</li><li>Core models</li><li>Community support</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-white/25 text-sm font-semibold text-tpt15-ink no-underline transition-colors hover:bg-white/14 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white/85">Choose Glass</a>
      </article>
      <article class="relative flex flex-col gap-4 rounded-3xl border border-white/30 border-t-white/55 bg-tpt15-solid p-8 shadow-[0_24px_60px_-30px_oklch(0_0_0/0.8)] backdrop-blur-[22px] backdrop-saturate-150 transition-[translate,background-color] duration-300 supports-[backdrop-filter:blur(1px)]:bg-white/14 hover:-translate-y-1.5 [@media(prefers-reduced-transparency:reduce)]:bg-tpt15-solid motion-reduce:hover:translate-y-0">
        <span class="absolute -top-3 right-6 rounded-full bg-white px-3 py-1 text-[10.5px] font-bold tracking-[0.1em] text-tpt15-bg uppercase">Popular</span>
        <h3 class="text-[13px] font-semibold tracking-[0.1em] text-tpt15-mut uppercase">Prism</h3>
        <p class="text-[46px] leading-none font-bold tracking-[-0.035em]">$48<small class="text-[15px] font-medium tracking-normal text-tpt15-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt15-body *:flex *:gap-2.5 *:before:text-[11px] *:before:leading-5 *:before:text-white/70 *:before:content-['✦']"><li>20 seats</li><li>All models</li><li>Priority queue</li><li>API access</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl bg-white/92 text-sm font-bold text-tpt15-bg no-underline transition-colors hover:bg-white focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white/85">Choose Prism</a>
      </article>
      <article class="flex flex-col gap-4 rounded-3xl border border-white/16 border-t-white/40 bg-tpt15-solid p-8 shadow-[0_24px_60px_-30px_oklch(0_0_0/0.8)] backdrop-blur-[22px] backdrop-saturate-150 transition-[translate,background-color] duration-300 supports-[backdrop-filter:blur(1px)]:bg-white/8 hover:-translate-y-1.5 supports-[backdrop-filter:blur(1px)]:hover:bg-white/12 [@media(prefers-reduced-transparency:reduce)]:bg-tpt15-solid motion-reduce:hover:translate-y-0">
        <h3 class="text-[13px] font-semibold tracking-[0.1em] text-tpt15-mut uppercase">Aurora</h3>
        <p class="text-[46px] leading-none font-bold tracking-[-0.035em]">$120<small class="text-[15px] font-medium tracking-normal text-tpt15-mut">/mo</small></p>
        <ul class="grid flex-1 content-start gap-2.5 text-sm text-tpt15-body *:flex *:gap-2.5 *:before:text-[11px] *:before:leading-5 *:before:text-white/70 *:before:content-['✦']"><li>Unlimited seats</li><li>Fine-tuning</li><li>Private VPC deploy</li></ul>
        <a href="#" class="grid min-h-11 place-items-center rounded-xl border border-white/25 text-sm font-semibold text-tpt15-ink no-underline transition-colors hover:bg-white/14 focus-visible:outline-3 focus-visible:outline-offset-2 focus-visible:outline-white/85">Choose Aurora</a>
      </article>
    </div>
    <p aria-hidden="true" class="rounded-full border border-white/20 bg-white/6 px-3.5 py-2 font-tpt15-mono text-[11.5px] text-tpt15-mut backdrop-blur-md">backdrop-blur-[22px] · supports-[backdrop-filter:…]: · reduced-transparency</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpt15-bg: #0e1018;
  --color-tpt15-bg: oklch(0.17 0.02 275);
  --color-tpt15-solid: #1c1f30;
  --color-tpt15-solid: oklch(0.24 0.03 275);
  --color-tpt15-ink: #f2f4fb;
  --color-tpt15-ink: oklch(0.965 0.008 275);
  --color-tpt15-body: #dde0ec;
  --color-tpt15-body: oklch(0.9 0.015 275);
  --color-tpt15-mut: #c3c7d8;
  --color-tpt15-mut: oklch(0.83 0.02 275);
  --color-tpt15-blob1: #9b3fe6;
  --color-tpt15-blob1: oklch(0.58 0.23 305);
  --color-tpt15-blob2: #2b8fe0;
  --color-tpt15-blob2: oklch(0.63 0.16 245);
  --color-tpt15-blob3: #f06a52;
  --color-tpt15-blob3: oklch(0.68 0.17 32);
  --font-tpt15-sans: 'Geist', system-ui, sans-serif;
  --font-tpt15-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tpt15-drift-1: tpt15-drift-1 19s ease-in-out infinite alternate;
  --animate-tpt15-drift-2: tpt15-drift-2 23s ease-in-out infinite alternate;
  --animate-tpt15-drift-3: tpt15-drift-3 27s ease-in-out infinite alternate;

  @keyframes tpt15-drift-1 {
    to {
      translate: 14vw 10vh;
      scale: 1.15;
    }
  }

  @keyframes tpt15-drift-2 {
    to {
      translate: -12vw -12vh;
      scale: 0.9;
    }
  }

  @keyframes tpt15-drift-3 {
    to {
      translate: -10vw 8vh;
      scale: 1.2;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities. */

.tpt-15 {
  width: 100%;
  min-height: 100svh;
}
```
