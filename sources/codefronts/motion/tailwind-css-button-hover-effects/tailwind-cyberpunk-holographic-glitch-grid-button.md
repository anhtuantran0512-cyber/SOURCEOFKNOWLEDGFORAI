---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-cyberpunk-holographic-glitch-grid-button/"
title: "Tailwind Cyberpunk Holographic Glitch Grid Button"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A neon sci-fi CTA for gaming, web3 and dev-tool pages: a holographic grid sits behind the label and, on hover, tears with a hard stepped glitch while a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Cyberpunk Holographic Glitch Grid Button
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-cyberpunk-holographic-glitch-grid-button/

A neon sci-fi CTA for gaming, web3 and dev-tool pages: a holographic grid sits behind the label and, on hover, tears with a hard stepped glitch while a magenta/cyan chromatic split flickers over the text. Four @keyframes stay CSS; every trigger, every layer and every reduced-motion fallback becomes a class.
## HTML
```html
<div class="tbh-02-group w-full min-h-svh flex flex-wrap">
<section class="tbh-02a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh02-display bg-tbh02a-bg" aria-label="Cyberpunk glitch grid button">
  <button type="button" data-text="Enter grid" class="group/btn relative isolate overflow-hidden cursor-pointer rounded border border-tbh02a-cyan px-10 py-[18px] text-base font-bold uppercase tracking-[0.22em] text-tbh02a-ink bg-tbh02a-panel shadow-[0_0_0_1px_color-mix(in_oklab,var(--color-tbh02a-cyan)_20%,transparent),0_0_24px_-8px_var(--color-tbh02a-cyan)] transition-shadow duration-300 hover:shadow-[0_0_0_1px_var(--color-tbh02a-cyan),0_0_34px_-6px_var(--color-tbh02a-cyan),0_0_34px_-6px_var(--color-tbh02a-mag)] focus-visible:shadow-[0_0_0_1px_var(--color-tbh02a-cyan),0_0_34px_-6px_var(--color-tbh02a-cyan)] focus-visible:outline-3 focus-visible:outline-tbh02a-cyan focus-visible:outline-offset-[3px] after:content-[attr(data-text)] after:absolute after:inset-0 after:grid after:place-items-center after:font-[inherit] after:tracking-[0.22em] after:text-tbh02a-ink after:z-[2] after:opacity-0 after:pointer-events-none after:[text-shadow:2px_0_var(--color-tbh02a-mag),-2px_0_var(--color-tbh02a-cyan)] after:[clip-path:inset(0_0_55%_0)] hover:after:opacity-90 hover:after:animate-tbh02a-glitch motion-reduce:hover:after:animate-none motion-reduce:hover:after:opacity-0">
    <span aria-hidden="true" class="absolute inset-0 -z-10 opacity-50 bg-[repeating-linear-gradient(90deg,color-mix(in_oklab,var(--color-tbh02a-cyan)_16%,transparent)_0_1px,transparent_1px_22px),repeating-linear-gradient(0deg,color-mix(in_oklab,var(--color-tbh02a-mag)_14%,transparent)_0_1px,transparent_1px_22px)] transition-opacity duration-300 group-hover/btn:opacity-95 group-hover/btn:animate-tbh02a-tear motion-reduce:group-hover/btn:animate-none"></span>
    <span class="relative z-[1]">Enter grid</span>
  </button>
</section>
<section class="tbh-02b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh02-mono bg-tbh02b-bg" aria-label="Cyberpunk scanline button">
  <button type="button" class="group/btn relative isolate overflow-hidden cursor-pointer rounded border border-tbh02b-grn px-10 py-[18px] text-base font-bold uppercase tracking-[0.2em] text-tbh02b-grn bg-tbh02b-panel shadow-[0_0_20px_-8px_var(--color-tbh02b-grn)] transition-shadow duration-300 hover:shadow-[0_0_30px_-4px_var(--color-tbh02b-grn),inset_0_0_20px_-6px_var(--color-tbh02b-grn)] focus-visible:shadow-[0_0_30px_-4px_var(--color-tbh02b-grn)] focus-visible:outline-3 focus-visible:outline-tbh02b-grn focus-visible:outline-offset-[3px]">
    <span aria-hidden="true" class="absolute inset-0 z-0 opacity-40 bg-[repeating-linear-gradient(0deg,color-mix(in_oklab,var(--color-tbh02b-grn)_14%,transparent)_0_2px,transparent_2px_4px)] transition-opacity duration-300 group-hover/btn:opacity-90 group-hover/btn:animate-tbh02b-roll motion-reduce:group-hover/btn:animate-none"></span>
    <span class="relative z-[1] group-hover/btn:animate-tbh02b-jit motion-reduce:group-hover/btn:animate-none">Jack in</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh02a-cyan: #22e3ff;
  --color-tbh02a-cyan: oklch(0.85 0.15 210);
  --color-tbh02a-mag: #ff2bd6;
  --color-tbh02a-mag: oklch(0.7 0.28 330);
  --color-tbh02a-ink: #eafcff;
  --color-tbh02a-ink: oklch(0.97 0.02 210);
  --color-tbh02a-bg: #07060f;
  --color-tbh02a-bg: oklch(0.12 0.02 285);
  --color-tbh02a-panel: #0d0b1f;
  --color-tbh02a-panel: oklch(0.17 0.04 285);
  --color-tbh02b-grn: #39ff88;
  --color-tbh02b-grn: oklch(0.88 0.22 150);
  --color-tbh02b-bg: #04100a;
  --color-tbh02b-bg: oklch(0.13 0.03 155);
  --color-tbh02b-panel: #07160e;
  --color-tbh02b-panel: oklch(0.16 0.04 155);
  --font-tbh02-display: 'Chakra Petch', ui-monospace, monospace;
  --font-tbh02-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-tbh02a-tear: tbh02a-tear 0.5s steps(5) infinite;
  --animate-tbh02a-glitch: tbh02a-glitch 0.45s steps(4) infinite;
  --animate-tbh02b-roll: tbh02b-roll 0.6s steps(6) infinite;
  --animate-tbh02b-jit: tbh02b-jit 0.3s steps(3) infinite;
}
/* Stays CSS: four keyframe sets, the one part of this demo with no utility form. */

@keyframes tbh02a-tear {
  0% {
    background-position: 0 0, 0 0;
  }

  40% {
    background-position: 6px -4px, -5px 3px;
  }

  70% {
    background-position: -4px 5px, 7px -6px;
  }

  100% {
    background-position: 0 0, 0 0;
  }
}

@keyframes tbh02a-glitch {
  0% {
    translate: 0 0;
    clip-path: inset(0 0 60% 0);
  }

  30% {
    translate: -3px 1px;
    clip-path: inset(50% 0 10% 0);
  }

  60% {
    translate: 3px -1px;
    clip-path: inset(20% 0 40% 0);
  }

  100% {
    translate: 0 0;
    clip-path: inset(0 0 60% 0);
  }
}

@keyframes tbh02b-roll {
  to {
    background-position: 0 8px;
  }
}

@keyframes tbh02b-jit {
  0%,
    100% {
    translate: 0 0;
  }

  50% {
    translate: 1.5px 0;
  }
}

.tbh-02-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-02a,
.tbh-02b {
  min-height: 100svh;
}
```
