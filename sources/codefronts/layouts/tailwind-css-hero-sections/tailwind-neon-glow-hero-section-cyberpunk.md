---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-neon-glow-hero-section-cyberpunk/"
title: "Neon Glow Hero Section in Tailwind CSS (Cyberpunk)"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Tokyo-cyberpunk night market — a synthwave perspective grid scrolling toward the horizon, neon-pink and electric-cyan glows, and a single breathing CTA."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow Hero Section in Tailwind CSS (Cyberpunk)
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-neon-glow-hero-section-cyberpunk/

Tokyo-cyberpunk night market — a synthwave perspective grid scrolling toward the horizon, neon-pink and electric-cyan glows, and a single breathing CTA. The conversion-focused neon pattern, with a moving floor instead of a static one.
## HTML
```html
<section class="ths-24 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths24-bg bg-[radial-gradient(60%_40%_at_50%_58%,rgb(238_82_206/0.18),transparent_70%)] px-5 py-16 font-ths24-sans text-white sm:px-14" aria-label="Neon cyberpunk hero">
  <span aria-hidden="true" class="pointer-events-none absolute bottom-0 left-1/2 -z-10 h-1/2 w-[220%] -translate-x-1/2 origin-top animate-ths24-floor bg-[repeating-linear-gradient(0deg,transparent_0_24px,rgb(238_82_206/0.4)_24px_25px),repeating-linear-gradient(90deg,transparent_0_24px,rgb(34_211_238/0.35)_24px_25px)] [mask-image:linear-gradient(180deg,transparent,#000_45%)] [transform:perspective(800px)_rotateX(60deg)] motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="pointer-events-none absolute inset-x-0 top-1/2 -z-10 h-px bg-ths24-pink/70 shadow-[0_0_24px_4px_rgb(238_82_206/0.5)]"></span>
  <div class="max-w-[46rem] text-center">
    <span class="inline-block border border-ths24-cyan px-3.5 py-1 font-ths24-mono text-[11.5px] tracking-[0.24em] text-ths24-cyan [text-shadow:0_0_10px_rgb(34_211_238/0.6)] shadow-[0_0_14px_rgb(34_211_238/0.25)]">/ ENTER THE NIGHT MARKET</span>
    <h1 class="mt-6 font-ths24-display text-[clamp(40px,6.6vw,76px)] leading-[1.02] font-bold tracking-[-0.025em] text-balance [text-shadow:0_0_30px_rgb(238_82_206/0.4)]">Order ramen at <em class="text-ths24-pink [text-shadow:0_0_18px_rgb(238_82_206/0.75)]">3 a.m.</em> like the locals do.</h1>
    <p class="mx-auto mt-5 max-w-md text-[17px] leading-relaxed text-ths24-mut">50 Tokyo back-alley vendors. One delivery app. One foreigner-friendly menu.</p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-6">
      <a href="#order" class="inline-flex min-h-12 animate-ths24-breathe items-center border-2 border-ths24-pink px-9 text-[15px] font-bold tracking-[0.12em] text-ths24-pink uppercase transition-colors hover:bg-ths24-pink hover:text-ths24-bg focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths24-cyan motion-reduce:animate-none motion-reduce:shadow-[0_0_18px_rgb(238_82_206/0.5)]">Open the menu</a>
      <span class="flex items-center gap-2 font-ths24-mono text-xs text-ths24-cyan"><span aria-hidden="true" class="size-2 rounded-full bg-ths24-cyan shadow-[0_0_8px_var(--color-ths24-cyan)]"></span>37 stalls open now</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths24-bg: #0a0014;
  --color-ths24-bg: oklch(0.113 0.057 308.8);
  --color-ths24-mut: #b8a2d6;
  --color-ths24-mut: oklch(0.749 0.077 303.9);
  --color-ths24-pink: #ee52ce;
  --color-ths24-pink: oklch(0.69 0.231 337);
  --color-ths24-cyan: #22d3ee;
  --color-ths24-cyan: oklch(0.797 0.134 211.5);
  --font-ths24-display: 'Space Grotesk', system-ui, sans-serif;
  --font-ths24-sans: 'Geist', system-ui, sans-serif;
  --font-ths24-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths24-floor: ths24-floor 1.6s linear infinite;
  --animate-ths24-breathe: ths24-breathe 2.4s ease-in-out infinite alternate;

  @keyframes ths24-floor {
    to {
      background-position: 0 25px, 0 0;
    }
  }

  @keyframes ths24-breathe {
    from {
      box-shadow: 0 0 14px rgb(238 82 206 / 0.4), inset 0 0 14px rgb(238 82 206 / 0.14);
    }

    to {
      box-shadow: 0 0 30px rgb(238 82 206 / 0.75), inset 0 0 24px rgb(238 82 206 / 0.3);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-24 {
  width: 100%;
  min-height: 100svh;
}
```
