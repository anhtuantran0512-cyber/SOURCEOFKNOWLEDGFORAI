---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-text-glitch-hover-effect/"
title: "Tailwind Text Glitch Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Four glitch hovers — RGB channel split, scanline flicker, noise slice and VHS chromatic aberration."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Text Glitch Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-text-glitch-hover-effect/

Four glitch hovers — RGB channel split, scanline flicker, noise slice and VHS chromatic aberration. Keyframes stay in the stylesheet (they are motion definitions, not design-scale values), but each becomes an --animate-* token, so firing one is a single hover:before:animate-* utility.
## HTML
```html
<section class="thv-02 w-full min-h-svh grid place-items-center bg-thv02-bg font-thv02-sans px-6 py-14">
  <div class="w-[min(820px,100%)] grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-10">
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="GLITCH" class="group relative inline-block text-[clamp(2rem,6vw,3.5rem)] font-black tracking-[0.08em] text-thv02-text rounded-xs focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-thv02-red before:content-[attr(data-text)] before:absolute before:inset-0 before:left-0.5 before:text-thv02-red before:pointer-events-none after:content-[attr(data-text)] after:absolute after:inset-0 after:-left-0.5 after:text-thv02-blue after:pointer-events-none hover:before:animate-thv02-rgb-b hover:after:animate-thv02-rgb-a focus-visible:before:animate-thv02-rgb-b focus-visible:after:animate-thv02-rgb-a motion-reduce:before:hidden motion-reduce:after:hidden">GLITCH</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv02-dim">RGB Channel Split</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="SCANLINE" class="relative inline-block text-[clamp(1.6rem,5vw,2.6rem)] font-black tracking-[0.08em] text-thv02-green rounded-xs focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-thv02-green before:content-[''] before:absolute before:inset-0 before:opacity-0 before:mix-blend-multiply before:transition-opacity before:duration-200 before:[background:repeating-linear-gradient(0deg,transparent,transparent_2px,rgba(0,0,0,.4)_2px,rgba(0,0,0,.4)_4px)] before:[background-size:100%_4px] after:content-[attr(data-text)] after:absolute after:inset-0 after:left-0.5 after:text-thv02-green after:opacity-0 after:transition-opacity after:duration-200 hover:before:opacity-100 hover:before:animate-thv02-scan hover:after:opacity-70 hover:after:animate-thv02-rgb-b focus-visible:before:opacity-100 focus-visible:after:opacity-70 motion-reduce:before:hidden motion-reduce:after:hidden">SCANLINE</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv02-dim">Scanline Flicker</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="NOISE" class="relative inline-block text-[clamp(2rem,6vw,3.5rem)] font-black tracking-[0.08em] text-thv02-yellow rounded-xs focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-thv02-yellow before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv02-red before:[clip-path:inset(0_0_100%_0)] after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv02-blue after:[clip-path:inset(100%_0_0_0)] hover:before:animate-thv02-slice-t hover:after:animate-thv02-slice-b focus-visible:before:animate-thv02-slice-t focus-visible:after:animate-thv02-slice-b motion-reduce:before:hidden motion-reduce:after:hidden">NOISE</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv02-dim">Noise Slice</span>
    </div>
    <div class="flex flex-col items-center gap-6 px-8 py-14 rounded-xl bg-white/[0.025] border border-white/[0.07]">
      <span tabindex="0" data-text="VHS" class="relative inline-block text-[clamp(2rem,6vw,3.5rem)] font-black tracking-[0.08em] text-white rounded-xs focus-visible:outline-2 focus-visible:outline-offset-8 focus-visible:outline-thv02-blue before:content-[attr(data-text)] before:absolute before:inset-0 before:text-thv02-red before:mix-blend-screen after:content-[attr(data-text)] after:absolute after:inset-0 after:text-thv02-blue after:mix-blend-screen hover:before:animate-thv02-vhs-r hover:after:animate-thv02-vhs-b focus-visible:before:animate-thv02-vhs-r focus-visible:after:animate-thv02-vhs-b motion-reduce:before:hidden motion-reduce:after:hidden">VHS</span>
      <span class="text-[11px] tracking-[0.15em] uppercase text-thv02-dim">VHS Chromatic</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv02-bg: #080810;
  --color-thv02-bg: oklch(0.13 0.02 285);
  --color-thv02-text: #f0f0f0;
  --color-thv02-text: oklch(0.95 0 0);
  --color-thv02-dim: #444444;
  --color-thv02-dim: oklch(0.4 0 0);
  --color-thv02-red: #ff003c;
  --color-thv02-red: oklch(0.62 0.28 17);
  --color-thv02-blue: #00e5ff;
  --color-thv02-blue: oklch(0.83 0.15 203);
  --color-thv02-green: #39ff14;
  --color-thv02-green: oklch(0.88 0.29 135);
  --color-thv02-yellow: #ffe600;
  --color-thv02-yellow: oklch(0.91 0.2 103);
  --font-thv02-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-thv02-rgb-b: thv02-rgb-b .4s steps(2) infinite;
  --animate-thv02-rgb-a: thv02-rgb-a .4s steps(2) .1s infinite;
  --animate-thv02-scan: thv02-scan .8s linear infinite;
  --animate-thv02-slice-t: thv02-slice-t .5s steps(4) infinite;
  --animate-thv02-slice-b: thv02-slice-b .5s steps(4) .15s infinite;
  --animate-thv02-vhs-r: thv02-vhs-r .6s steps(3) infinite;
  --animate-thv02-vhs-b: thv02-vhs-b .6s steps(3) .2s infinite;
}

.thv-02 {
  width: 100%;
  min-height: 100svh;
}

.thv-02 ::selection {
  background: var(--color-thv02-red);
  color: #fff;
}
/* Motion definitions stay in CSS; @theme above mints the animate-* utilities. */

@keyframes thv02-rgb-b {
  0% {
    clip-path: inset(0 0 95% 0);
    transform: translateX(-3px);
  }

  20% {
    clip-path: inset(30% 0 50% 0);
    transform: translateX(3px);
  }

  40% {
    clip-path: inset(60% 0 20% 0);
    transform: translateX(-2px);
  }

  60% {
    clip-path: inset(10% 0 75% 0);
    transform: translateX(4px);
  }

  80% {
    clip-path: inset(80% 0 5% 0);
    transform: translateX(-3px);
  }

  100% {
    clip-path: inset(45% 0 40% 0);
    transform: translateX(2px);
  }
}

@keyframes thv02-rgb-a {
  0% {
    clip-path: inset(50% 0 30% 0);
    transform: translateX(3px);
  }

  25% {
    clip-path: inset(5% 0 80% 0);
    transform: translateX(-4px);
  }

  50% {
    clip-path: inset(70% 0 15% 0);
    transform: translateX(2px);
  }

  75% {
    clip-path: inset(20% 0 60% 0);
    transform: translateX(-3px);
  }

  100% {
    clip-path: inset(40% 0 45% 0);
    transform: translateX(3px);
  }
}

@keyframes thv02-scan {
  0% {
    background-position-y: 0;
  }

  100% {
    background-position-y: 100px;
  }
}

@keyframes thv02-slice-t {
  0% {
    clip-path: inset(0 0 85% 0);
    transform: translateX(6px) skewX(-2deg);
  }

  33% {
    clip-path: inset(25% 0 55% 0);
    transform: translateX(-5px);
  }

  66% {
    clip-path: inset(60% 0 10% 0);
    transform: translateX(4px) skewX(1deg);
  }

  100% {
    clip-path: inset(10% 0 75% 0);
    transform: translateX(-6px);
  }
}

@keyframes thv02-slice-b {
  0% {
    clip-path: inset(80% 0 0 0);
    transform: translateX(-4px);
  }

  33% {
    clip-path: inset(50% 0 20% 0);
    transform: translateX(6px);
  }

  66% {
    clip-path: inset(15% 0 70% 0);
    transform: translateX(-3px) skewX(2deg);
  }

  100% {
    clip-path: inset(65% 0 5% 0);
    transform: translateX(5px);
  }
}

@keyframes thv02-vhs-r {
  0% {
    transform: translateX(-6px);
    clip-path: inset(20% 0 60% 0);
  }

  50% {
    transform: translateX(4px);
    clip-path: inset(55% 0 10% 0);
  }

  100% {
    transform: translateX(-5px);
    clip-path: inset(5% 0 80% 0);
  }
}

@keyframes thv02-vhs-b {
  0% {
    transform: translateX(6px);
    clip-path: inset(40% 0 30% 0);
  }

  50% {
    transform: translateX(-4px);
    clip-path: inset(10% 0 65% 0);
  }

  100% {
    transform: translateX(5px);
    clip-path: inset(70% 0 5% 0);
  }
}
```
