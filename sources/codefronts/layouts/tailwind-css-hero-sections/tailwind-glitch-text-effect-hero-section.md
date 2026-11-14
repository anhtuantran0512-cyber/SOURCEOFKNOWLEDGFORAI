---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-glitch-text-effect-hero-section/"
title: "Glitch Text Effect Hero Section in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A VHS-glitch hero — RGB-split copies of the headline tear through clipped bands in short bursts, over tape static and scanlines, with a blinking REC counter."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Text Effect Hero Section in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-glitch-text-effect-hero-section/

A VHS-glitch hero — RGB-split copies of the headline tear through clipped bands in short bursts, over tape static and scanlines, with a blinking REC counter. The glitch fires in bursts instead of constantly, so the headline stays readable.
## HTML
```html
<section class="ths-29 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths29-bg px-5 py-16 font-ths29-mono text-ths29-ink sm:px-14" aria-label="Glitch text hero">
  <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 animate-ths29-static bg-[radial-gradient(rgb(255_255_255/0.05)_1px,transparent_1px),radial-gradient(rgb(255_255_255/0.035)_1px,transparent_1px)] bg-size-[3px_3px,5px_5px] bg-position-[0_0,1px_1px] motion-reduce:animate-none"></span>
  <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[repeating-linear-gradient(180deg,transparent_0_2px,rgb(0_0_0/0.2)_2px_3px)]"></span>
  <span aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_center,transparent_55%,rgb(0_0_0/0.6))]"></span>
  <div class="max-w-[46rem] text-center">
    <div class="flex items-center justify-center gap-3 text-[11px] font-bold tracking-[0.18em]">
      <span class="animate-ths29-blink bg-ths29-red px-2.5 py-1 text-white motion-reduce:animate-none">REC ● 00:42:18</span>
      <span class="text-ths29-mut">SP · CH 03</span>
    </div>
    <h1 data-text="LOST &amp; FOUND" class="relative mt-6 font-ths29-display text-[clamp(52px,10vw,120px)] leading-[0.92] font-black tracking-[-0.04em] text-ths29-paper [font-stretch:120%] before:pointer-events-none before:absolute before:inset-0 before:animate-ths29-burst before:text-ths29-red before:mix-blend-screen before:content-[attr(data-text)_/_''] before:[clip-path:polygon(0_12%,100%_12%,100%_38%,0_38%)] after:pointer-events-none after:absolute after:inset-0 after:animate-ths29-burst after:text-ths29-cyan after:mix-blend-screen after:content-[attr(data-text)_/_''] after:[animation-direction:reverse] after:[clip-path:polygon(0_58%,100%_58%,100%_86%,0_86%)] motion-reduce:before:animate-none motion-reduce:after:animate-none">LOST &amp; FOUND</h1>
    <p class="mx-auto mt-6 max-w-md text-sm leading-relaxed text-ths29-mut">A search engine for VHS-era ephemera. Public-access TV, mall demos, regional news. The forgotten internet of the 80s.</p>
    <form action="#search" role="search" class="mx-auto mt-8 flex max-w-md border-2 border-ths29-cyan focus-within:shadow-[0_0_0_3px_rgb(56_184_214/0.35)]">
      <label for="ths29-q" class="sr-only">Search the tapes</label>
      <input id="ths29-q" type="search" placeholder="e.g. mall demo 1987" class="min-h-12 min-w-0 flex-1 bg-transparent px-4 text-sm text-ths29-paper placeholder:text-ths29-mut/70 focus:outline-none">
      <button type="submit" class="min-h-12 bg-ths29-cyan px-5 text-xs font-extrabold tracking-[0.16em] text-ths29-bg uppercase transition hover:bg-ths29-red hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white motion-reduce:transition-none">Search →</button>
    </form>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths29-bg: #1a1818;
  --color-ths29-bg: oklch(0.211 0.003 17.4);
  --color-ths29-ink: #d8d4c8;
  --color-ths29-ink: oklch(0.87 0.017 91.6);
  --color-ths29-paper: #f0eee0;
  --color-ths29-paper: oklch(0.947 0.019 100.1);
  --color-ths29-mut: #a8a49b;
  --color-ths29-mut: oklch(0.719 0.014 86.8);
  --color-ths29-red: #d63838;
  --color-ths29-red: oklch(0.582 0.195 25.7);
  --color-ths29-cyan: #38b8d6;
  --color-ths29-cyan: oklch(0.727 0.115 217.2);
  --font-ths29-display: 'Archivo', system-ui, sans-serif;
  --font-ths29-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths29-static: ths29-static 0.2s steps(2) infinite;
  --animate-ths29-blink: ths29-blink 1.4s steps(2) infinite;
  --animate-ths29-burst: ths29-burst 3.2s steps(1) infinite;

  @keyframes ths29-static {
    50% {
      transform: translate(-1px, 1px);
    }

    100% {
      transform: translate(1px, -1px);
    }
  }

  @keyframes ths29-blink {
    to {
      opacity: 0.5;
    }
  }

  @keyframes ths29-burst {
    0%,
        84% {
      transform: translate(-2px, 0);
    }

    86% {
      transform: translate(5px, -2px);
    }

    88% {
      transform: translate(-6px, 2px);
    }

    90% {
      transform: translate(3px, 1px);
    }

    92% {
      transform: translate(-4px, -1px);
    }

    95% {
      transform: translate(6px, 2px);
    }

    100% {
      transform: translate(-2px, 0);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-29 {
  width: 100%;
  min-height: 100svh;
}
```
