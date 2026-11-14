---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-animated-gradient-text-moving-gradient/"
title: "Tailwind Animated Gradient Text (Moving Gradient)"
section: "motion"
category: "tailwind-css-text-gradient"
category_name: "Tailwind CSS Text Gradient"
description: "A hero where colour flows through one word on a perfectly seamless loop."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Gradient Text (Moving Gradient)
Source: https://codefronts.com/motion/tailwind-css-text-gradient/tailwind-animated-gradient-text-moving-gradient/

A hero where colour flows through one word on a perfectly seamless loop. The gradient is a repeating tile twice the element's width, and animate-ttg08-flow moves it exactly one tile per cycle &mdash; fixing the visible jump the CSS original had at the end of every loop. Hover to pause.
## HTML
```html
<section class="ttg-08 relative isolate w-full min-h-svh grid place-items-center overflow-hidden bg-ttg08-bg px-6 py-20 font-ttg08-sans text-ttg08-ink" aria-labelledby="ttg08-title">
  <span aria-hidden="true" class="absolute inset-x-0 top-0 -z-10 h-2/3 bg-[radial-gradient(50%_60%_at_50%_0%,var(--color-ttg08-glow),transparent)]"></span>
  <div class="max-w-3xl text-center">
    <p class="inline-flex items-center gap-2 rounded-full border border-white/10 px-3.5 py-1.5 text-xs font-medium tracking-[0.08em] text-ttg08-mut uppercase"><span aria-hidden="true" class="size-1.5 rounded-full bg-ttg08-c3"></span>Season 3 — now streaming</p>
    <h1 id="ttg08-title" class="mt-7 font-ttg08-display text-[clamp(2.75rem,9vw,6rem)] leading-[1] font-extrabold tracking-[-0.045em]">The future of<br><span class="bg-[linear-gradient(90deg,var(--color-ttg08-c1),var(--color-ttg08-c2),var(--color-ttg08-c3),var(--color-ttg08-c4),var(--color-ttg08-c1))] bg-[length:200%_100%] bg-clip-text pr-[0.04em] text-transparent animate-ttg08-flow hover:[animation-play-state:paused] motion-reduce:animate-none">interface</span> design</h1>
    <p class="mx-auto mt-7 max-w-lg text-[17px]/[1.7] text-ttg08-mut text-pretty">Shifting gradients bring motion and energy to a headline without a single line of JavaScript. Hover the word to freeze it.</p>
    <p aria-hidden="true" class="mt-10 font-mono text-[11.5px] text-ttg08-mut/80">bg-[length:200%_100%] · animate-ttg08-flow · hover:[animation-play-state:paused]</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttg08-bg: #08080f;
  --color-ttg08-bg: oklch(0.14 0.015 285);
  --color-ttg08-glow: #3b2a6e80;
  --color-ttg08-glow: oklch(0.35 0.11 290 / 0.5);
  --color-ttg08-ink: #f6f7fb;
  --color-ttg08-ink: oklch(0.975 0.005 270);
  --color-ttg08-mut: #a7adbb;
  --color-ttg08-mut: oklch(0.76 0.018 270);
  --color-ttg08-c1: #f39cf5;
  --color-ttg08-c1: oklch(0.8 0.16 325);
  --color-ttg08-c2: #8a8ff9;
  --color-ttg08-c2: oklch(0.69 0.16 280);
  --color-ttg08-c3: #3cc4f5;
  --color-ttg08-c3: oklch(0.77 0.14 225);
  --color-ttg08-c4: #3fdca2;
  --color-ttg08-c4: oklch(0.81 0.15 165);
  --font-ttg08-display: 'Syne', system-ui, sans-serif;
  --font-ttg08-sans: 'Geist', system-ui, sans-serif;
  --animate-ttg08-flow: ttg08-flow 6s linear infinite;

  @keyframes ttg08-flow {
    from {
      background-position: 0% 50%;
    }

    to {
      background-position: 200% 50%;
    }
  }
}

.ttg-08 {
  width: 100%;
  min-height: 100svh;
}
```
