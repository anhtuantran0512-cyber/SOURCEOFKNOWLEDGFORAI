---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-rgb-glitch-card-hover-effect/"
title: "Tailwind RGB Channel-Split Glitch Card"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "Three stacked copies of one headline &mdash; red channel, cyan channel, clean white &mdash; desyncing into datamoshed slices on hover, with two drifting scan…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind RGB Channel-Split Glitch Card
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-rgb-glitch-card-hover-effect/

Three stacked copies of one headline &mdash; red channel, cyan channel, clean white &mdash; desyncing into datamoshed slices on hover, with two drifting scan bars. The port keeps all three keyframe sets in CSS (they animate clip-path, which no utility can tween) and applies them from the markup.
## HTML
```html
<section class="tch-20 w-full min-h-svh grid place-items-center bg-tch20-bg font-tch20-mono p-8">
  <article tabindex="0" class="group relative w-[340px] h-[440px] rounded overflow-hidden cursor-pointer outline-none bg-tch20-card border border-tch20-edge focus-visible:outline-2 focus-visible:outline-tch20-cyan focus-visible:outline-offset-4">
    <div class="absolute inset-0 z-3 pointer-events-none opacity-0 group-hover:opacity-100 group-hover:animate-tch20-bars group-focus-visible:opacity-100 motion-reduce:animate-none motion-reduce:group-hover:animate-none before:content-[''] before:absolute before:inset-x-0 before:top-[32%] before:h-0.5 before:bg-tch20-cyan/50 after:content-[''] after:absolute after:inset-x-0 after:top-[68%] after:h-0.5 after:bg-tch20-red/50"></div>
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch20-ink">
      <span class="text-[0.72rem] tracking-[0.25em] text-tch20-cyan">// SIGNAL_LOST</span>
      <h2 class="relative inline-block font-tch20-display text-[4rem] leading-[0.85] uppercase text-white">
        <span aria-hidden="true" class="absolute inset-0 size-full pointer-events-none text-tch20-red opacity-0 transition-opacity duration-200 group-hover:opacity-85 group-hover:animate-tch20-shift-a group-focus-visible:opacity-85 motion-reduce:animate-none motion-reduce:group-hover:animate-none">NULL<br>CITY</span>
        <span aria-hidden="true" class="absolute inset-0 size-full pointer-events-none text-tch20-cyan opacity-0 transition-opacity duration-200 group-hover:opacity-85 group-hover:animate-tch20-shift-b group-focus-visible:opacity-85 motion-reduce:animate-none motion-reduce:group-hover:animate-none">NULL<br>CITY</span>
        <span class="relative z-1 block">NULL<br>CITY</span>
      </h2>
      <p class="text-[0.82rem] leading-[1.6] text-tch20-body">A cyberpunk audio-visual set. Corrupted frames, datamoshed visuals, bass you feel in your teeth.</p>
      <span class="text-[0.72rem] tracking-[0.15em] text-tch20-mut">FRI · WAREHOUSE 7 · 23:00</span>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch20-shift-a {
  0% {
    transform: translate(0,0);
    clip-path: inset(0 0 70% 0);
  }

  50% {
    transform: translate(-4px,2px);
    clip-path: inset(40% 0 20% 0);
  }

  100% {
    transform: translate(3px,-2px);
    clip-path: inset(70% 0 0 0);
  }
}

@keyframes tch20-shift-b {
  0% {
    transform: translate(0,0);
    clip-path: inset(60% 0 10% 0);
  }

  50% {
    transform: translate(4px,-2px);
    clip-path: inset(10% 0 60% 0);
  }

  100% {
    transform: translate(-3px,2px);
    clip-path: inset(30% 0 40% 0);
  }
}

@keyframes tch20-bars {
  0%,
    100% {
    transform: translateX(0);
  }

  50% {
    transform: translateX(6px);
  }
}

@theme {
  --color-tch20-bg: #08080a;
  --color-tch20-bg: oklch(0.1 0.003 285);
  --color-tch20-card: #0f0f12;
  --color-tch20-card: oklch(0.14 0.005 285);
  --color-tch20-edge: #1c1c22;
  --color-tch20-edge: oklch(0.21 0.007 285);
  --color-tch20-ink: #e8e8ee;
  --color-tch20-ink: oklch(0.92 0.004 285);
  --color-tch20-body: #888888;
  --color-tch20-body: oklch(0.62 0 0);
  --color-tch20-mut: #555555;
  --color-tch20-mut: oklch(0.44 0 0);
  --color-tch20-red: #ff003c;
  --color-tch20-red: oklch(0.6 0.28 20);
  --color-tch20-cyan: #00e0ff;
  --color-tch20-cyan: oklch(0.83 0.14 205);
  --font-tch20-mono: 'Space Mono', ui-monospace, monospace;
  --font-tch20-display: 'Anton', system-ui, sans-serif;
  --animate-tch20-shift-a: tch20-shift-a 0.35s steps(2) infinite;
  --animate-tch20-shift-b: tch20-shift-b 0.35s steps(2) infinite;
  --animate-tch20-bars: tch20-bars 0.4s steps(3) infinite;
}

.tch-20 {
  width: 100%;
  min-height: 100svh;
}
```
