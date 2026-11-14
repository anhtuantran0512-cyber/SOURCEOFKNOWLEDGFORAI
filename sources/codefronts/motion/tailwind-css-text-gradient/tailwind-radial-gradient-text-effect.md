---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-radial-gradient-text-effect/"
title: "Tailwind Radial Gradient Text Effect"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "Text that glows from within: v4's bg-radial-[circle_at_50%_50%] puts the brightest stop at the centre of each word and fades to a deeper edge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Radial Gradient Text Effect
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-radial-gradient-text-effect/

Text that glows from within: v4's bg-radial-[circle_at_50%_50%] puts the brightest stop at the centre of each word and fades to a deeper edge. Four variants show circle vs ellipse and centred vs off-centre focal points, plus a radial KPI number &mdash; the place radial text earns its keep.
## HTML
```html
<section class="ttg-14 w-full min-h-svh grid place-items-center bg-ttg14-bg bg-[radial-gradient(50%_40%_at_50%_30%,var(--color-ttg14-glow),transparent)] px-5 py-16 font-ttg14-sans text-ttg14-ink" aria-label="Radial gradient text demo">
  <div class="grid w-full max-w-2xl justify-items-center text-center">
    <h1 class="w-fit bg-radial-[circle_at_50%_50%] from-ttg14-amber-c to-ttg14-amber-e to-65% bg-clip-text font-ttg14-display text-[clamp(3.5rem,13vw,7rem)] leading-none font-black tracking-[-0.05em] text-transparent">Radiate</h1>
    <p class="mt-2 w-fit bg-radial-[ellipse_at_35%_60%] from-ttg14-violet-c to-ttg14-violet-e to-75% bg-clip-text font-ttg14-display text-[clamp(1.4rem,4.6vw,2.6rem)] font-bold tracking-[-0.03em] text-transparent">energy outward</p>
    <div class="mt-10 grid w-full gap-4 text-left sm:grid-cols-3">
      <article class="rounded-2xl border border-white/8 bg-white/[0.03] p-5"><h3 class="w-fit bg-radial-[circle_at_50%_40%] from-ttg14-sky-c to-ttg14-sky-e to-80% bg-clip-text font-ttg14-display text-2xl font-extrabold text-transparent">Expand</h3><p class="mt-2 text-[13.5px]/[1.6] text-ttg14-mut">Radial gradients grow from a central point, so text feels lit from within.</p></article>
      <article class="rounded-2xl border border-white/8 bg-white/[0.03] p-5"><h3 class="w-fit bg-radial-[circle_at_50%_40%] from-ttg14-pink-c to-ttg14-pink-e to-80% bg-clip-text font-ttg14-display text-2xl font-extrabold text-transparent">Focus</h3><p class="mt-2 text-[13.5px]/[1.6] text-ttg14-mut">A deeper perimeter draws the eye to the bright centre of the letterforms.</p></article>
      <article class="flex flex-col-reverse justify-end gap-1 rounded-2xl border border-white/8 bg-white/[0.03] p-5"><p class="text-[13.5px] text-ttg14-mut">Weekly active users</p><p class="w-fit bg-radial-[circle_at_50%_45%] from-ttg14-amber-c to-ttg14-amber-e to-70% bg-clip-text font-ttg14-display text-[2.6rem] leading-none font-black tracking-tight text-transparent tabular-nums">48.2K</p></article>
    </div>
    <code class="mt-8 rounded-lg border border-white/10 bg-white/[0.04] px-3 py-1.5 font-ttg14-mono text-[12px] text-ttg14-violet-c">bg-radial-[circle_at_50%_50%] from-… to-… to-65%</code>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg14-bg: #09080f;
  --color-ttg14-bg: oklch(0.14 0.012 290);
  --color-ttg14-glow: #2a1d4a80;
  --color-ttg14-glow: oklch(0.26 0.07 295 / 0.5);
  --color-ttg14-ink: #eceaf3;
  --color-ttg14-ink: oklch(0.94 0.008 290);
  --color-ttg14-mut: #a6a3b5;
  --color-ttg14-mut: oklch(0.74 0.02 290);
  --color-ttg14-amber-c: #fff1b8;
  --color-ttg14-amber-c: oklch(0.96 0.08 95);
  --color-ttg14-amber-e: #f08a0b;
  --color-ttg14-amber-e: oklch(0.72 0.17 60);
  --color-ttg14-violet-c: #d9ccff;
  --color-ttg14-violet-c: oklch(0.87 0.07 295);
  --color-ttg14-violet-e: #7c3aed;
  --color-ttg14-violet-e: oklch(0.54 0.25 293);
  --color-ttg14-sky-c: #c9eeff;
  --color-ttg14-sky-c: oklch(0.93 0.05 225);
  --color-ttg14-sky-e: #2563eb;
  --color-ttg14-sky-e: oklch(0.55 0.22 263);
  --color-ttg14-pink-c: #ffd6ec;
  --color-ttg14-pink-c: oklch(0.91 0.06 350);
  --color-ttg14-pink-e: #d61f7c;
  --color-ttg14-pink-e: oklch(0.58 0.22 355);
  --font-ttg14-display: 'Unbounded', system-ui, sans-serif;
  --font-ttg14-sans: 'Geist', system-ui, sans-serif;
  --font-ttg14-mono: 'Geist Mono', ui-monospace, monospace;
}

.ttg-14 {
  width: 100%;
  min-height: 100svh;
}
```
