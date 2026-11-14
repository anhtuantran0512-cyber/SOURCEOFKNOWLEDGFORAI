---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/glassmorphism-card-with-gradient-text-in-tailwind/"
title: "Glassmorphism Card with Gradient Text in Tailwind"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A frosted-glass article card floating over drifting colour orbs."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Card with Gradient Text in Tailwind
Source: https://codefronts.com/motion/tailwind-css-text-gradient/glassmorphism-card-with-gradient-text-in-tailwind/

A frosted-glass article card floating over drifting colour orbs. Gradient text on glass is a contrast problem &mdash; whatever colour blurs through changes the background under every letter &mdash; so the headline uses high-lightness stops plus a soft drop-shadow, and the glass falls back to a denser fill via supports-[backdrop-filter:blur(1px)]: where blur isn't available.
## HTML
```html
<section class="ttg-11 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-ttg11-bg px-5 py-16 font-ttg11-sans text-ttg11-ink" aria-labelledby="ttg11-title">
  <span aria-hidden="true" class="absolute top-[-8%] left-[-6%] -z-10 size-[24rem] rounded-full bg-ttg11-orb-a opacity-70 blur-3xl animate-ttg11-drift motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="absolute right-[-6%] bottom-[-10%] -z-10 size-[22rem] rounded-full bg-ttg11-orb-b opacity-60 blur-3xl animate-ttg11-drift [animation-delay:-6s] motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="absolute top-[40%] left-[52%] -z-10 size-[15rem] rounded-full bg-ttg11-orb-c opacity-60 blur-3xl animate-ttg11-drift [animation-delay:-12s] motion-reduce:animate-none"></span>
  <article class="w-full max-w-lg rounded-[28px] border border-white/15 bg-white/16 p-10 shadow-[inset_0_1px_0_rgb(255_255_255/0.2),0_30px_60px_-20px_rgb(0_0_0/0.5)] backdrop-blur-2xl supports-[backdrop-filter:blur(1px)]:bg-white/[0.07] max-sm:p-7">
    <p class="inline-flex rounded-full border border-white/15 bg-white/8 px-3 py-1 text-xs font-semibold tracking-[0.08em] text-ttg11-mut uppercase">Featured article</p>
    <h2 id="ttg11-title" class="mt-5 text-[clamp(2rem,5.5vw,3rem)] leading-[1.06] font-bold tracking-[-0.03em]">Design <span class="bg-linear-110 from-ttg11-a via-ttg11-b to-ttg11-c bg-clip-text text-transparent drop-shadow-[0_1px_10px_var(--color-ttg11-shadow)]">systems</span><br>that scale</h2>
    <p class="mt-4 text-[15.5px]/[1.7] text-ttg11-mut text-pretty">Gradient text on translucent surfaces needs careful colour management. Keep every stop bright enough to hold <strong class="font-semibold text-ttg11-ink">4.5 : 1</strong> against any colour that bleeds through the blur.</p>
    <div class="mt-7 flex items-center gap-3 border-t border-white/12 pt-6">
      <span aria-hidden="true" class="grid size-10 place-items-center rounded-full bg-linear-135 from-ttg11-orb-a to-ttg11-orb-b text-sm font-bold text-white ring-2 ring-white/30">JL</span>
      <div class="text-sm"><p class="font-semibold">Julia Lam</p><p class="text-ttg11-mut"><time datetime="2026-06-12">Jun 12</time> · 5 min read</p></div>
      <a href="#" class="ml-auto inline-flex min-h-11 items-center rounded-full bg-white px-5 text-sm font-semibold text-ttg11-bg transition hover:bg-ttg11-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white">Read</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg11-bg: #0a0618;
  --color-ttg11-bg: oklch(0.15 0.045 295);
  --color-ttg11-ink: #fbf7ff;
  --color-ttg11-ink: oklch(0.98 0.01 310);
  --color-ttg11-mut: #e2d6f5;
  --color-ttg11-mut: oklch(0.89 0.04 305);
  --color-ttg11-shadow: #2a0d4d;
  --color-ttg11-shadow: oklch(0.25 0.12 300);
  --color-ttg11-a: #f6b4ff;
  --color-ttg11-a: oklch(0.85 0.13 320);
  --color-ttg11-b: #b7bcff;
  --color-ttg11-b: oklch(0.82 0.1 280);
  --color-ttg11-c: #8fe3ff;
  --color-ttg11-c: oklch(0.87 0.1 220);
  --color-ttg11-orb-a: #9b4dff;
  --color-ttg11-orb-a: oklch(0.6 0.25 300);
  --color-ttg11-orb-b: #ff4fa3;
  --color-ttg11-orb-b: oklch(0.67 0.23 355);
  --color-ttg11-orb-c: #18c6e0;
  --color-ttg11-orb-c: oklch(0.76 0.13 210);
  --font-ttg11-sans: 'Outfit', system-ui, sans-serif;
  --animate-ttg11-drift: ttg11-drift 18s ease-in-out infinite;

  @keyframes ttg11-drift {
    0%,
        100% {
      transform: translate(0, 0) scale(1);
    }

    33% {
      transform: translate(6%, 8%) scale(1.08);
    }

    66% {
      transform: translate(-6%, 3%) scale(0.94);
    }
  }
}

.ttg-11 {
  width: 100%;
  min-height: 100svh;
}
```
