---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-starfield-background-hero/"
title: "Animated Starfield Background Hero in Tailwind CSS"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "A pure-CSS night sky — three tiled star layers that twinkle out of phase, an occasional shooting star, a warm horizon glow and a constellation-app hero on top."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Starfield Background Hero in Tailwind CSS
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-animated-starfield-background-hero/

A pure-CSS night sky — three tiled star layers that twinkle out of phase, an occasional shooting star, a warm horizon glow and a constellation-app hero on top. No canvas, no per-star DOM, stars that fill any screen size.
## HTML
```html
<section class="ths-28 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-[radial-gradient(ellipse_at_50%_100%,rgb(248_210_72/0.16),transparent_70%),linear-gradient(180deg,var(--color-ths28-space)_0%,var(--color-ths28-navy)_60%,var(--color-ths28-dusk)_100%)] px-5 py-16 font-ths28-sans text-ths28-ink sm:px-14" aria-label="Animated starfield hero">
  <div aria-hidden="true" class="absolute inset-0 -z-10 animate-ths28-twinkle bg-[radial-gradient(1px_1px_at_20px_30px,#fff,transparent),radial-gradient(1px_1px_at_120px_80px,#fff,transparent),radial-gradient(1.5px_1.5px_at_200px_160px,var(--color-ths28-gold),transparent),radial-gradient(1px_1px_at_60px_200px,#fff,transparent),radial-gradient(1px_1px_at_170px_20px,#fff,transparent)] bg-size-[240px_240px] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute inset-0 -z-10 animate-ths28-twinkle bg-[radial-gradient(1px_1px_at_50px_100px,rgb(255_255_255/0.7),transparent),radial-gradient(2px_2px_at_250px_40px,#fff,transparent),radial-gradient(1px_1px_at_300px_260px,rgb(255_255_255/0.6),transparent),radial-gradient(1px_1px_at_140px_300px,var(--color-ths28-gold),transparent)] bg-size-[330px_330px] [animation-delay:-1.5s] [animation-duration:5s] motion-reduce:animate-none"></div>
  <div aria-hidden="true" class="absolute inset-0 -z-10 animate-ths28-twinkle bg-[radial-gradient(1px_1px_at_80px_60px,rgb(255_255_255/0.5),transparent),radial-gradient(1.5px_1.5px_at_400px_200px,rgb(255_255_255/0.8),transparent),radial-gradient(1px_1px_at_220px_420px,rgb(255_255_255/0.5),transparent)] bg-size-[470px_470px] [animation-delay:-3s] [animation-duration:7s] motion-reduce:animate-none"></div>
  <span aria-hidden="true" class="absolute top-[14%] left-[8%] -z-10 h-px w-[120px] animate-ths28-shoot bg-linear-to-l from-white to-transparent opacity-0 motion-reduce:hidden"></span>
  <div class="max-w-[42rem] text-center">
    <span class="font-ths28-mono text-[11.5px] tracking-[0.24em] text-ths28-gold">★ NIGHT SKY ATLAS</span>
    <h1 class="mt-6 font-ths28-serif text-[clamp(38px,6vw,68px)] leading-[1.04] font-bold tracking-[-0.02em] text-balance">Every constellation, <em class="text-ths28-gold">over your back yard tonight.</em></h1>
    <p class="mx-auto mt-5 max-w-md text-[17px] leading-relaxed text-ths28-mut">Point your phone up. We'll tell you which star is where, why it has that name, and when to look again.</p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-4">
      <a href="#download" class="inline-flex min-h-12 items-center bg-ths28-gold px-7 text-[15px] font-bold tracking-[0.04em] text-ths28-space shadow-[0_0_30px_rgb(248_210_72/0.3)] transition hover:bg-white focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-ths28-gold motion-reduce:transition-none">Get the atlas</a>
      <span class="rounded-full border border-white/15 px-4 py-2 font-ths28-mono text-xs text-ths28-mut">Tonight: Perseids peak · 60/hr</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths28-space: #050a1a;
  --color-ths28-space: oklch(0.149 0.036 266.6);
  --color-ths28-navy: #0a1428;
  --color-ths28-navy: oklch(0.194 0.043 262.9);
  --color-ths28-dusk: #1a2840;
  --color-ths28-dusk: oklch(0.277 0.049 260.7);
  --color-ths28-ink: #f0eee0;
  --color-ths28-ink: oklch(0.947 0.019 100.1);
  --color-ths28-mut: #c2bba9;
  --color-ths28-mut: oklch(0.793 0.026 89.2);
  --color-ths28-gold: #f8d248;
  --color-ths28-gold: oklch(0.873 0.155 93.2);
  --font-ths28-serif: 'Playfair Display', Georgia, serif;
  --font-ths28-sans: 'Geist', system-ui, sans-serif;
  --font-ths28-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths28-twinkle: ths28-twinkle 4s ease-in-out infinite alternate;
  --animate-ths28-shoot: ths28-shoot 7s ease-in infinite;

  @keyframes ths28-twinkle {
    from {
      opacity: 0.45;
    }

    to {
      opacity: 1;
    }
  }

  @keyframes ths28-shoot {
    0% {
      opacity: 0;
      transform: translate(0, 0) rotate(-24deg);
    }

    3% {
      opacity: 1;
    }

    15% {
      opacity: 0;
      transform: translate(420px, 190px) rotate(-24deg);
    }

    100% {
      opacity: 0;
      transform: translate(420px, 190px) rotate(-24deg);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-28 {
  width: 100%;
  min-height: 100svh;
}
```
