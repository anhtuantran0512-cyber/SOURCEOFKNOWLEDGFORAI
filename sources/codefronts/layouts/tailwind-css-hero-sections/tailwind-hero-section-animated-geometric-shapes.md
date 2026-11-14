---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-animated-geometric-shapes/"
title: "Tailwind Hero Section with Animated Geometric Shapes Background"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A Memphis-modern alternative to a video background — circle, triangle, pill and square float in a loop behind cobalt-on-bone copy with a lemon neo-brutalist…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Hero Section with Animated Geometric Shapes Background
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-hero-section-animated-geometric-shapes/

A Memphis-modern alternative to a video background — circle, triangle, pill and square float in a loop behind cobalt-on-bone copy with a lemon neo-brutalist CTA. No video file, no licensing, no layout shift.
## HTML
```html
<section class="ths-06 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths06-bg px-5 py-16 font-ths06-sans text-ths06-ink sm:px-14 has-[#ths06-pause:checked]:[&_[data-shape]]:[animation-play-state:paused]" aria-label="Hero with animated geometric shapes">
  <div aria-hidden="true" class="pointer-events-none absolute inset-0 -z-10">
    <span data-shape class="absolute top-[8%] left-[6%] size-[clamp(64px,10vw,110px)] animate-ths06-float rounded-full bg-ths06-ink motion-reduce:animate-none"></span>
    <span data-shape class="absolute top-[12%] right-[10%] h-[clamp(70px,11vw,120px)] w-[clamp(80px,13vw,140px)] animate-ths06-float bg-ths06-lemon [animation-delay:-3s] [animation-direction:alternate-reverse] [clip-path:polygon(50%_0,100%_100%,0_100%)] motion-reduce:animate-none"></span>
    <span data-shape class="absolute bottom-[10%] left-[12%] h-[clamp(34px,5vw,50px)] w-[clamp(96px,14vw,140px)] rotate-[-12deg] animate-ths06-float rounded-full bg-ths06-coral [animation-delay:-5s] motion-reduce:animate-none"></span>
    <span data-shape class="absolute right-[8%] bottom-[8%] size-[clamp(56px,9vw,90px)] rotate-[15deg] animate-ths06-float rounded-xl border-[3px] border-ths06-ink bg-ths06-sky [animation-delay:-7s] motion-reduce:animate-none"></span>
    <span data-shape class="absolute top-[46%] left-[3%] size-6 animate-ths06-float rounded-full border-[3px] border-ths06-coral [animation-delay:-2s] motion-reduce:animate-none"></span>
  </div>
  <div class="max-w-[40rem] text-center">
    <span class="inline-flex items-center gap-2 bg-ths06-ink px-3 py-1 font-ths06-mono text-[11px] font-bold tracking-[0.18em] text-ths06-lemon">▸ NOW PLAYING</span>
    <h1 class="mt-6 font-ths06-display text-[clamp(42px,7vw,80px)] leading-[0.96] font-extrabold tracking-[-0.035em] text-balance">Your portfolio, <em class="text-ths06-coral">animated.</em></h1>
    <p class="mx-auto mt-5 max-w-[29rem] text-[17px] leading-relaxed text-ths06-body">Drop in your projects. We turn them into the kind of motion reel that gets the call back.</p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-5">
      <a href="#start" class="inline-flex min-h-12 items-center rounded border-[3px] border-ths06-ink bg-ths06-lemon px-7 text-[15px] font-extrabold text-ths06-ink shadow-[6px_6px_0_var(--color-ths06-ink)] transition hover:translate-x-0.5 hover:translate-y-0.5 hover:shadow-[3px_3px_0_var(--color-ths06-ink)] active:translate-x-1.5 active:translate-y-1.5 active:shadow-none focus-visible:outline-3 focus-visible:outline-offset-4 focus-visible:outline-ths06-coral motion-reduce:transition-none">Play with it</a>
      <label class="inline-flex min-h-11 cursor-pointer items-center gap-2 font-ths06-mono text-xs font-medium text-ths06-body select-none has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-ths06-ink">
        <input id="ths06-pause" type="checkbox" class="peer sr-only">
        <span aria-hidden="true" class="relative h-5 w-9 rounded-full bg-ths06-ink/20 transition after:absolute after:top-0.5 after:left-0.5 after:size-4 after:rounded-full after:bg-white after:transition after:content-[''] peer-checked:bg-ths06-ink peer-checked:after:translate-x-4"></span>
        Pause motion
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths06-bg: #f4f1ea;
  --color-ths06-bg: oklch(0.959 0.01 87.5);
  --color-ths06-ink: #0b1f4a;
  --color-ths06-ink: oklch(0.253 0.084 263);
  --color-ths06-body: #3f4d6d;
  --color-ths06-body: oklch(0.422 0.057 265.9);
  --color-ths06-lemon: #f5d028;
  --color-ths06-lemon: oklch(0.864 0.169 95.2);
  --color-ths06-coral: #e0474a;
  --color-ths06-coral: oklch(0.616 0.19 23.6);
  --color-ths06-sky: #8fd3f4;
  --color-ths06-sky: oklch(0.833 0.083 229.9);
  --font-ths06-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-ths06-sans: 'Geist', system-ui, sans-serif;
  --font-ths06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths06-float: ths06-float 8s ease-in-out infinite alternate;

  @keyframes ths06-float {
    0% {
      transform: translate(0, 0);
    }

    100% {
      transform: translate(20px, -16px) rotate(8deg);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-06 {
  width: 100%;
  min-height: 100svh;
}
```
