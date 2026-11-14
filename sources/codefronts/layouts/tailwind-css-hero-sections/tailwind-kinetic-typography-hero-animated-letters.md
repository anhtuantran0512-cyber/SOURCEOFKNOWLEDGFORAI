---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-kinetic-typography-hero-animated-letters/"
title: "Kinetic Typography Hero in Tailwind CSS with Animated Letters"
section: "layouts"
category: "tailwind-css-hero-sections"
category_name: "Tailwind CSS Hero Sections"
description: "Rave-poster kinetic type — every letter of FULL BASS MODE jitters, tilts and scales on its own delay over a pulsing acid-green / magenta haze."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Kinetic Typography Hero in Tailwind CSS with Animated Letters
Source: https://codefronts.com/layouts/tailwind-css-hero-sections/tailwind-kinetic-typography-hero-animated-letters/

Rave-poster kinetic type — every letter of FULL BASS MODE jitters, tilts and scales on its own delay over a pulsing acid-green / magenta haze. Accessible: the headline reads as words, not letters, and a zero-JS toggle pauses the motion.
## HTML
```html
<section class="ths-18 relative isolate grid w-full min-h-svh place-items-center overflow-hidden bg-ths18-bg px-5 py-16 text-center font-ths18-sans text-white sm:px-14 has-[#ths18-still:checked]:[&_*]:[animation-play-state:paused]" aria-label="Kinetic typography hero">
  <div aria-hidden="true" class="absolute inset-0 -z-10 animate-ths18-pulse bg-[radial-gradient(60%_50%_at_30%_30%,rgb(196_255_82/0.2),transparent_60%),radial-gradient(50%_50%_at_80%_70%,rgb(238_82_206/0.22),transparent_60%)] motion-reduce:animate-none"></div>
  <div class="max-w-5xl">
    <span class="font-ths18-mono text-[11px] tracking-[0.3em] text-ths18-lime">SAT · WAREHOUSE 9 · 23:00 → 07:00</span>
    <h1 aria-label="Full bass mode" class="mt-6 font-ths18-display text-[clamp(52px,10vw,128px)] leading-[0.9] font-black tracking-[-0.04em] uppercase [font-stretch:120%]">
      <span aria-hidden="true" class="flex flex-wrap justify-center gap-x-[0.3em]">
        <span class="whitespace-nowrap text-ths18-lime [text-shadow:0_0_30px_rgb(196_255_82/0.35)]"><span class="inline-block animate-ths18-jitter motion-reduce:animate-none">F</span><span class="inline-block animate-ths18-jitter [animation-delay:60ms] motion-reduce:animate-none">U</span><span class="inline-block animate-ths18-jitter [animation-delay:120ms] motion-reduce:animate-none">L</span><span class="inline-block animate-ths18-jitter [animation-delay:180ms] motion-reduce:animate-none">L</span></span>
        <span class="whitespace-nowrap"><span class="inline-block animate-ths18-jitter [animation-delay:240ms] motion-reduce:animate-none">B</span><span class="inline-block animate-ths18-jitter [animation-delay:300ms] motion-reduce:animate-none">A</span><span class="inline-block animate-ths18-jitter [animation-delay:360ms] motion-reduce:animate-none">S</span><span class="inline-block animate-ths18-jitter [animation-delay:420ms] motion-reduce:animate-none">S</span></span>
        <em class="whitespace-nowrap text-ths18-pink [text-shadow:0_0_30px_rgb(238_82_206/0.45)]"><span class="inline-block animate-ths18-jitter [animation-delay:480ms] motion-reduce:animate-none">M</span><span class="inline-block animate-ths18-jitter [animation-delay:540ms] motion-reduce:animate-none">O</span><span class="inline-block animate-ths18-jitter [animation-delay:600ms] motion-reduce:animate-none">D</span><span class="inline-block animate-ths18-jitter [animation-delay:660ms] motion-reduce:animate-none">E</span></em>
      </span>
    </h1>
    <p class="mx-auto mt-6 max-w-md text-[17px] leading-relaxed text-ths18-mut">A booking app for warehouse parties. The line is the door, not the website.</p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-5">
      <a href="#tickets" class="inline-flex min-h-12 items-center bg-ths18-lime px-8 text-[15px] font-bold tracking-[0.06em] text-ths18-bg uppercase shadow-[0_0_28px_rgb(196_255_82/0.45)] transition hover:bg-ths18-pink hover:text-white hover:shadow-[0_0_28px_rgb(238_82_206/0.55)] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-white motion-reduce:transition-none">Get tickets ⚡</a>
      <label class="inline-flex min-h-11 cursor-pointer items-center gap-2 font-ths18-mono text-xs text-ths18-mut select-none has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-white">
        <input id="ths18-still" type="checkbox" class="peer sr-only">
        <span aria-hidden="true" class="relative h-5 w-9 rounded-full bg-white/20 transition after:absolute after:top-0.5 after:left-0.5 after:size-4 after:rounded-full after:bg-white after:transition after:content-[''] peer-checked:bg-ths18-pink peer-checked:after:translate-x-4"></span>
        Stop motion
      </label>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ths18-bg: #0a0a0a;
  --color-ths18-bg: oklch(0.145 0 0);
  --color-ths18-mut: #a8a8a8;
  --color-ths18-mut: oklch(0.732 0 0);
  --color-ths18-lime: #c4ff52;
  --color-ths18-lime: oklch(0.929 0.205 126.5);
  --color-ths18-pink: #ee52ce;
  --color-ths18-pink: oklch(0.69 0.231 337);
  --font-ths18-display: 'Archivo', system-ui, sans-serif;
  --font-ths18-sans: 'Geist', system-ui, sans-serif;
  --font-ths18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ths18-jitter: ths18-jitter 2s ease-in-out infinite;
  --animate-ths18-pulse: ths18-pulse 2.4s ease-in-out infinite alternate;

  @keyframes ths18-jitter {
    0%,
        100% {
      transform: translateY(0) rotate(0deg) scale(1);
    }

    25% {
      transform: translateY(-8px) rotate(-2deg) scale(1.04);
    }

    50% {
      transform: translateY(0) rotate(2deg) scale(0.98);
    }

    75% {
      transform: translateY(6px) rotate(-1deg) scale(1.02);
    }
  }

  @keyframes ths18-pulse {
    from {
      opacity: 0.6;
    }

    to {
      opacity: 1;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ths-18 {
  width: 100%;
  min-height: 100svh;
}
```
