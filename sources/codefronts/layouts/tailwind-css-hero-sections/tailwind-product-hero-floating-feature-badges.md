---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-product-hero-floating-feature-badges/"
title: "Tailwind CSS Product Hero with Floating Feature Badges"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "An Apple-keynote product shot — a CSS-built laptop (lid, lit screen, hinge and base) centred on an ice-blue stage, with three spec badges bobbing around it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Product Hero with Floating Feature Badges
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-product-hero-floating-feature-badges/

An Apple-keynote product shot — a CSS-built laptop (lid, lit screen, hinge and base) centred on an ice-blue stage, with three spec badges bobbing around it. Chrome silver and ice blue on warm white, with price and compare CTAs.
## HTML
```html
<section class="ths-21 grid w-full min-h-svh items-center gap-10 bg-ths21-bg bg-[radial-gradient(circle_at_30%_35%,var(--color-ths21-ice),transparent_50%),radial-gradient(circle_at_80%_70%,var(--color-ths21-mist),transparent_50%)] px-5 py-16 font-ths21-sans text-ths21-ink sm:px-12 lg:grid-cols-[1.2fr_1fr] lg:gap-14" aria-label="Product hero with floating badges">
  <div aria-hidden="true" class="relative grid min-h-[360px] place-items-center">
    <div class="w-[min(340px,78vw)]">
      <div class="relative aspect-[16/10] rounded-[14px] bg-linear-160 from-ths21-silver via-ths21-steel to-ths21-slate p-2 shadow-[0_30px_60px_-18px_rgb(96_112_128/0.55),inset_0_1px_0_rgb(255_255_255/0.6),inset_0_-2px_0_rgb(0_0_0/0.18)]">
        <span class="absolute top-[3px] left-1/2 size-[5px] -translate-x-1/2 rounded-full bg-ths21-ink"></span>
        <div class="size-full overflow-hidden rounded-[7px] bg-linear-135 from-ths21-ink to-ths21-night p-3 shadow-[inset_0_0_0_2px_var(--color-ths21-night)]">
          <div class="flex h-full gap-2">
            <div class="w-1/4 rounded bg-white/8"></div>
            <div class="flex flex-1 flex-col gap-2"><div class="h-1/3 rounded bg-linear-to-r from-ths21-accent/70 to-ths21-silver/30"></div><div class="flex-1 rounded bg-white/6"></div></div>
          </div>
        </div>
      </div>
      <div class="mx-auto h-1.5 w-[104%] -translate-x-[2%] rounded-b-md bg-linear-to-b from-ths21-silver to-ths21-steel"></div>
      <div class="mx-auto h-3 w-[112%] -translate-x-[5%] rounded-b-[14px] bg-linear-to-b from-ths21-steel to-ths21-slate shadow-[0_18px_30px_-12px_rgb(26_40_64/0.45)]"></div>
    </div>
    <span class="absolute top-[8%] left-[2%] flex animate-ths21-bob flex-col gap-0.5 rounded-2xl border border-ths21-line bg-white/90 px-3.5 py-2 text-[11px] shadow-[0_10px_24px_rgb(96_112_128/0.2)] backdrop-blur motion-reduce:animate-none sm:text-xs"><strong class="font-ths21-mono text-[10px] font-semibold text-ths21-label">CHIP</strong>16-core neural</span>
    <span class="absolute top-[38%] right-0 flex animate-ths21-bob flex-col gap-0.5 rounded-2xl border border-ths21-line bg-white/90 px-3.5 py-2 text-[11px] shadow-[0_10px_24px_rgb(96_112_128/0.2)] backdrop-blur [animation-delay:-1.3s] motion-reduce:animate-none sm:text-xs"><strong class="font-ths21-mono text-[10px] font-semibold text-ths21-label">BATTERY</strong>22 hours</span>
    <span class="absolute bottom-[8%] left-[10%] flex animate-ths21-bob flex-col gap-0.5 rounded-2xl border border-ths21-line bg-white/90 px-3.5 py-2 text-[11px] shadow-[0_10px_24px_rgb(96_112_128/0.2)] backdrop-blur [animation-delay:-2.6s] motion-reduce:animate-none sm:text-xs"><strong class="font-ths21-mono text-[10px] font-semibold text-ths21-label">WEIGHT</strong>1.24 kg</span>
  </div>
  <div class="max-w-lg">
    <span class="font-ths21-mono text-xs font-semibold tracking-[0.14em] text-ths21-label uppercase">New · Air Pro 14</span>
    <h1 class="mt-4 text-[clamp(36px,5vw,58px)] leading-[1.03] font-bold tracking-[-0.03em] text-balance">The lightest pro laptop we've ever <em class="bg-linear-to-r from-ths21-label to-ths21-accent bg-clip-text pr-1 font-extrabold text-transparent">shipped.</em></h1>
    <p class="mt-5 text-[17px] leading-relaxed text-ths21-body">All-day battery, a silent fanless chassis and a display tuned for colour work — in 1.24 kg.</p>
    <div class="mt-8 flex flex-wrap items-center gap-3">
      <a href="#buy" class="inline-flex min-h-12 items-center rounded-full bg-ths21-ink px-7 text-[15px] font-semibold text-ths21-bg transition hover:-translate-y-px hover:bg-ths21-night focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths21-ink motion-reduce:transition-none">Buy — from $1,499</a>
      <a href="#compare" class="inline-flex min-h-12 items-center rounded-full px-5 text-[15px] font-semibold text-ths21-ink ring-1 ring-ths21-line transition hover:bg-white hover:ring-ths21-label focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths21-ink">Compare models</a>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths21-bg: #f8fafc;
  --color-ths21-bg: oklch(0.984 0.003 247.9);
  --color-ths21-ice: #d8e8f0;
  --color-ths21-ice: oklch(0.921 0.02 229.1);
  --color-ths21-mist: #e8eef2;
  --color-ths21-mist: oklch(0.946 0.008 236.6);
  --color-ths21-ink: #1a2840;
  --color-ths21-ink: oklch(0.277 0.049 260.7);
  --color-ths21-night: #0a1428;
  --color-ths21-night: oklch(0.194 0.043 262.9);
  --color-ths21-body: #43536b;
  --color-ths21-body: oklch(0.439 0.045 258.3);
  --color-ths21-label: #4f6a8c;
  --color-ths21-label: oklch(0.517 0.063 254.5);
  --color-ths21-accent: #7fa6c9;
  --color-ths21-accent: oklch(0.709 0.067 246);
  --color-ths21-line: #d0d8e0;
  --color-ths21-line: oklch(0.878 0.014 248);
  --color-ths21-silver: #c9d6e2;
  --color-ths21-silver: oklch(0.87 0.022 245.9);
  --color-ths21-steel: #8a9ab0;
  --color-ths21-steel: oklch(0.681 0.037 256.4);
  --color-ths21-slate: #607080;
  --color-ths21-slate: oklch(0.538 0.032 248.4);
  --font-ths21-sans: 'Geist', system-ui, sans-serif;
  --font-ths21-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths21-bob: ths21-bob 4s ease-in-out infinite;

  @keyframes ths21-bob {
    0%,
        100% {
      translate: 0 0;
    }

    50% {
      translate: 0 -6px;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-21 {
  width: 100%;
  min-height: 100svh;
}
```
