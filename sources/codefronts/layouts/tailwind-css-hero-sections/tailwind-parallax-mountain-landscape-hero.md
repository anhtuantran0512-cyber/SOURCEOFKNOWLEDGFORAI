---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-parallax-mountain-landscape-hero/"
title: "Parallax Mountain Landscape Hero in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Three SVG ridgelines drift at different speeds in front of a glacier-blue sky with a low sun, drifting clouds and valley fog — the outdoor / travel-brand…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Mountain Landscape Hero in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-parallax-mountain-landscape-hero/

Three SVG ridgelines drift at different speeds in front of a glacier-blue sky with a low sun, drifting clouds and valley fog — the outdoor / travel-brand parallax landscape, with a lodge booking strip under the headline.
## HTML
```html
<section class="ths-25 relative isolate w-full min-h-svh overflow-hidden bg-linear-to-b from-ths25-sky via-ths25-sky2 to-ths25-ridge3 font-ths25-sans text-ths25-ink" aria-label="Parallax mountain hero">
  <div aria-hidden="true" class="absolute inset-0 -z-10 bg-[radial-gradient(50%_70%_at_80%_30%,rgb(255_240_210/0.45),transparent_70%)]"></div>
  <span aria-hidden="true" class="absolute top-[18%] right-[18%] -z-10 size-20 rounded-full bg-ths25-sun shadow-[0_0_80px_rgb(249_240_214/0.8)]"></span>
  <span aria-hidden="true" class="absolute top-[8%] left-[62%] -z-10 h-6 w-40 animate-ths25-cloud rounded-full bg-white/60 blur-[2px] motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="absolute top-[34%] left-[72%] -z-10 h-4 w-28 animate-ths25-cloud rounded-full bg-white/45 blur-[2px] [animation-delay:-20s] motion-reduce:animate-none"></span>
  <svg aria-hidden="true" viewBox="0 0 1200 320" preserveAspectRatio="none" class="absolute bottom-0 left-0 -z-10 h-[65%] w-[104%] animate-ths25-drift text-ths25-ridge3 [animation-delay:-4s] [animation-duration:16s] motion-reduce:animate-none"><path fill="currentColor" d="M0,320 L0,180 L120,80 L240,140 L360,60 L480,120 L600,40 L720,110 L840,70 L960,130 L1080,90 L1200,150 L1200,320 Z"/></svg>
  <div aria-hidden="true" class="absolute inset-x-0 bottom-[22%] -z-10 h-[20%] bg-linear-to-t from-white/35 to-transparent"></div>
  <svg aria-hidden="true" viewBox="0 0 1200 320" preserveAspectRatio="none" class="absolute bottom-0 left-0 -z-10 h-1/2 w-[104%] animate-ths25-drift text-ths25-ridge2 [animation-delay:-2s] [animation-duration:12s] motion-reduce:animate-none"><path fill="currentColor" d="M0,320 L0,220 L100,140 L200,200 L320,120 L440,180 L560,100 L680,170 L800,130 L920,200 L1040,150 L1200,200 L1200,320 Z"/></svg>
  <svg aria-hidden="true" viewBox="0 0 1200 320" preserveAspectRatio="none" class="absolute bottom-0 left-0 -z-10 h-[38%] w-[104%] animate-ths25-drift text-ths25-ridge1 [animation-duration:8s] motion-reduce:animate-none"><path fill="currentColor" d="M0,320 L0,260 L120,200 L240,240 L360,180 L480,220 L600,160 L720,210 L840,170 L960,230 L1080,190 L1200,240 L1200,320 Z"/></svg>
  <div class="max-w-xl px-5 pt-[clamp(48px,10vh,120px)] sm:px-14">
    <span class="font-ths25-mono text-[11px] tracking-[0.18em] text-ths25-ridge1">— EST. 1958 · LAKE COUNTRY</span>
    <h1 class="mt-4 font-ths25-serif text-[clamp(40px,6vw,68px)] leading-[1.02] font-bold tracking-[-0.02em] text-balance">Trails that <em class="text-ths25-ridge1">earn the silence.</em></h1>
    <p class="mt-5 max-w-md text-[17px] leading-relaxed text-ths25-body">Six lodges. One ridge. The mountains your grandfather wrote home about.</p>
    <div class="mt-8 flex flex-wrap items-center gap-4">
      <a href="#book" class="inline-flex min-h-12 items-center border-2 border-ths25-ridge1 bg-ths25-sun px-6 font-ths25-mono text-[13px] font-bold tracking-[0.12em] text-ths25-ridge1 transition hover:bg-ths25-ridge1 hover:text-ths25-sun focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths25-ridge1 motion-reduce:transition-none">Reserve a cabin →</a>
      <span class="font-ths25-mono text-xs text-ths25-ridge1">from $210 / night · 4.9 ★</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths25-sky: #d8e8f0;
  --color-ths25-sky: oklch(0.921 0.02 229.1);
  --color-ths25-sky2: #a8c8d8;
  --color-ths25-sky2: oklch(0.814 0.041 229.5);
  --color-ths25-sun: #f9f0d6;
  --color-ths25-sun: oklch(0.955 0.035 91.1);
  --color-ths25-ink: #0d2030;
  --color-ths25-ink: oklch(0.236 0.04 246);
  --color-ths25-body: #22404f;
  --color-ths25-body: oklch(0.355 0.044 231.6);
  --color-ths25-ridge1: #1f3a4a;
  --color-ths25-ridge1: oklch(0.334 0.043 236.1);
  --color-ths25-ridge2: #3a5868;
  --color-ths25-ridge2: oklch(0.443 0.044 232.4);
  --color-ths25-ridge3: #5a7a8a;
  --color-ths25-ridge3: oklch(0.561 0.044 230.1);
  --font-ths25-serif: 'Playfair Display', Georgia, serif;
  --font-ths25-sans: 'Geist', system-ui, sans-serif;
  --font-ths25-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths25-drift: ths25-drift 12s ease-in-out infinite alternate;
  --animate-ths25-cloud: ths25-cloud 60s linear infinite;

  @keyframes ths25-drift {
    to {
      transform: translateX(-2%);
    }
  }

  @keyframes ths25-cloud {
    from {
      transform: translateX(-30vw);
    }

    to {
      transform: translateX(60vw);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-25 {
  width: 100%;
  min-height: 100svh;
}
```
