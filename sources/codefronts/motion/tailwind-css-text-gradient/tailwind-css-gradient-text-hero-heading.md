---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-css-gradient-text-hero-heading/"
title: "Tailwind CSS Gradient Text Hero Heading"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "The most-searched gradient-text pattern — a landing-page H1 whose last line is painted with bg-linear-135 from-* via-* to-* bg-clip-text text-transparent."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Gradient Text Hero Heading
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-css-gradient-text-hero-heading/

The most-searched gradient-text pattern — a landing-page H1 whose last line is painted with bg-linear-135 from-* via-* to-* bg-clip-text text-transparent. One class list replaces the original's four-declaration CSS rule, and the same three colour tokens drive the headline, the announcement badge and the primary CTA.
## HTML
```html
<section class="ttg-01 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-ttg01-bg px-6 py-20 font-ttg01-sans text-ttg01-ink" aria-labelledby="ttg01-title">
  <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(60%_50%_at_50%_0%,var(--color-ttg01-glow),transparent_70%)]"></span>
  <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[linear-gradient(var(--color-ttg01-line)_1px,transparent_1px),linear-gradient(90deg,var(--color-ttg01-line)_1px,transparent_1px)] bg-[length:56px_56px] [mask-image:radial-gradient(65%_55%_at_50%_30%,#000,transparent)]"></span>
  <div class="mx-auto w-full max-w-3xl text-center">
    <a href="#" class="group inline-flex min-h-9 items-center gap-2.5 rounded-full border border-white/10 bg-white/5 py-1 pr-4 pl-1 text-[13px] font-medium text-ttg01-mut transition hover:border-white/20 hover:text-ttg01-ink focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg01-c">
      <span class="rounded-full bg-linear-to-r from-ttg01-a to-ttg01-c px-2.5 py-0.5 text-[11px] font-bold tracking-wide text-ttg01-bg">NEW</span>
      Components 2.0 is live
      <span aria-hidden="true" class="transition-transform group-hover:translate-x-0.5 motion-reduce:transition-none">&rarr;</span>
    </a>
    <h1 id="ttg01-title" class="mt-8 font-ttg01-display text-[clamp(2.75rem,7.5vw,5.5rem)] leading-[1.02] font-extrabold tracking-[-0.04em] text-balance">Build products<br><span class="bg-linear-135 from-ttg01-a via-ttg01-b to-ttg01-c bg-clip-text text-transparent">users love.</span></h1>
    <p class="mx-auto mt-6 max-w-xl text-[17px]/[1.7] text-ttg01-mut text-pretty">Design systems, prototypes and production-grade components — in one collaborative workspace your whole team can ship from.</p>
    <div class="mt-9 flex flex-wrap justify-center gap-3">
      <a href="#" class="inline-flex min-h-12 items-center rounded-xl bg-linear-135 from-ttg01-a via-ttg01-b to-ttg01-c px-6 text-[15px] font-semibold text-white shadow-[0_12px_32px_-12px_var(--color-ttg01-b)] transition hover:-translate-y-0.5 hover:shadow-[0_18px_40px_-12px_var(--color-ttg01-b)] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg01-c motion-reduce:transition-none">Start for free</a>
      <a href="#" class="inline-flex min-h-12 items-center gap-2 rounded-xl border border-white/12 bg-white/[0.03] px-6 text-[15px] font-semibold text-ttg01-ink transition hover:bg-white/[0.07] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttg01-c">View live demo <span aria-hidden="true">&rarr;</span></a>
    </div>
    <dl class="mx-auto mt-16 grid max-w-lg grid-cols-3 gap-4 border-t border-white/10 pt-8">
      <div class="flex flex-col-reverse gap-1"><dt class="text-[13px] text-ttg01-mut">Developers</dt><dd class="font-ttg01-display text-2xl font-bold tracking-tight">50K+</dd></div>
      <div class="flex flex-col-reverse gap-1"><dt class="text-[13px] text-ttg01-mut">Average rating</dt><dd class="font-ttg01-display text-2xl font-bold tracking-tight">4.9 / 5</dd></div>
      <div class="flex flex-col-reverse gap-1"><dt class="text-[13px] text-ttg01-mut">Uptime</dt><dd class="font-ttg01-display text-2xl font-bold tracking-tight">99.99%</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg01-bg: #07090f;
  --color-ttg01-bg: oklch(0.15 0.015 265);
  --color-ttg01-ink: #eef1f6;
  --color-ttg01-ink: oklch(0.96 0.008 260);
  --color-ttg01-mut: #a3abba;
  --color-ttg01-mut: oklch(0.75 0.02 260);
  --color-ttg01-line: #ffffff0d;
  --color-ttg01-line: oklch(1 0 0 / 0.05);
  --color-ttg01-glow: #4c2a8a73;
  --color-ttg01-glow: oklch(0.4 0.15 295 / 0.45);
  --color-ttg01-a: #b56cf7;
  --color-ttg01-a: oklch(0.68 0.2 305);
  --color-ttg01-b: #6b6ff2;
  --color-ttg01-b: oklch(0.62 0.19 275);
  --color-ttg01-c: #22c3dc;
  --color-ttg01-c: oklch(0.76 0.13 210);
  --font-ttg01-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ttg01-sans: 'Geist', system-ui, sans-serif;
}
/* Root rule: full-bleed contract, restated so the stage is sized before the browser build compiles. */

.ttg-01 {
  width: 100%;
  min-height: 100svh;
}
```
