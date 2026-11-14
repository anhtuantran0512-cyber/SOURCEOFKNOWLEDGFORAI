---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-headline-hero-staggered-word-reveal/"
title: "Tailwind CSS Animated Headline Hero with Staggered Word Reveal"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A 1950s-diner hero where each word lifts out of a mask with a staggered delay — coral and ivory on jet black, with a neon-outline CTA that glows on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Animated Headline Hero with Staggered Word Reveal
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-headline-hero-staggered-word-reveal/

A 1950s-diner hero where each word lifts out of a mask with a staggered delay — coral and ivory on jet black, with a neon-outline CTA that glows on hover. Words rise from behind a clip, not just fade, for a crisper editorial reveal.
## HTML
```html
<section class="ths-08 grid w-full min-h-svh place-items-center bg-ths08-bg bg-[radial-gradient(60%_50%_at_50%_100%,var(--color-ths08-glow),transparent_70%)] px-5 py-16 font-ths08-sans text-ths08-ivory sm:px-14" aria-label="Animated headline hero">
  <div class="max-w-[46rem] text-center">
    <span class="inline-block font-ths08-mono text-xs tracking-[0.28em] text-ths08-coral">— OPEN 24 HRS —</span>
    <h1 class="mt-7 font-ths08-serif text-[clamp(42px,7vw,84px)] leading-[1.02] font-bold tracking-[-0.015em]">
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><span class="inline-block animate-ths08-rise motion-reduce:animate-none">Late</span></span>
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><span class="inline-block animate-ths08-rise [animation-delay:120ms] motion-reduce:animate-none">night</span></span>
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><span class="inline-block animate-ths08-rise [animation-delay:240ms] motion-reduce:animate-none">tunes,</span></span>
      <br>
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><span class="inline-block animate-ths08-rise [animation-delay:360ms] motion-reduce:animate-none">made</span></span>
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><span class="inline-block animate-ths08-rise [animation-delay:480ms] motion-reduce:animate-none">for</span></span>
      <span class="inline-block overflow-hidden pb-[0.12em] align-bottom"><em class="inline-block animate-ths08-rise text-ths08-coral [animation-delay:600ms] motion-reduce:animate-none">cruising.</em></span>
    </h1>
    <p class="mx-auto mt-6 max-w-[27rem] animate-ths08-fade text-base/relaxed text-ths08-mut [animation-delay:850ms] motion-reduce:animate-none">A radio station that never sleeps and never sells you anything.</p>
    <div class="mt-9 flex animate-ths08-fade flex-wrap items-center justify-center gap-5 [animation-delay:1050ms] motion-reduce:animate-none">
      <a href="#tune" class="inline-flex min-h-12 items-center gap-2.5 rounded-full border-2 border-ths08-coral px-7 text-sm font-semibold tracking-[0.08em] text-ths08-coral uppercase transition hover:bg-ths08-coral hover:text-ths08-bg hover:shadow-[0_0_28px_rgb(255_116_97/0.55)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths08-coral motion-reduce:transition-none"><span aria-hidden="true" class="size-2 animate-pulse rounded-full bg-current"></span>Tune in live</a>
      <span class="font-ths08-mono text-xs text-ths08-mut">2,184 listening now</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths08-bg: #0d0d0d;
  --color-ths08-bg: oklch(0.159 0 0);
  --color-ths08-glow: #3a1410;
  --color-ths08-glow: oklch(0.25 0.061 28.3);
  --color-ths08-ivory: #fdf3e0;
  --color-ths08-ivory: oklch(0.967 0.027 83.5);
  --color-ths08-mut: #c2b39b;
  --color-ths08-mut: oklch(0.773 0.037 79.6);
  --color-ths08-coral: #ff7461;
  --color-ths08-coral: oklch(0.722 0.173 29.8);
  --font-ths08-serif: 'Playfair Display', Georgia, serif;
  --font-ths08-sans: 'Geist', system-ui, sans-serif;
  --font-ths08-mono: 'Courier Prime', 'Courier New', monospace;
  --animate-ths08-rise: ths08-rise 0.8s cubic-bezier(0.22, 1, 0.36, 1) both;
  --animate-ths08-fade: ths08-fade 0.7s cubic-bezier(0.22, 1, 0.36, 1) both;

  @keyframes ths08-rise {
    from {
      transform: translateY(110%);
    }

    to {
      transform: translateY(0);
    }
  }

  @keyframes ths08-fade {
    from {
      opacity: 0;
      transform: translateY(16px);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-08 {
  width: 100%;
  min-height: 100svh;
}
```
