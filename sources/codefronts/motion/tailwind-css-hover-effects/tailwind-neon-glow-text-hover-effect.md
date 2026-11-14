---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-neon-glow-text-hover-effect/"
title: "Tailwind Neon Glow Text Hover Effect"
section: "motion"
category: "tailwind-css-hover-effects"
category_name: "Tailwind CSS Hover Effects"
description: "Six electroluminescent text hovers — classic tube, flicker, hue cycle, multi-layer bloom, retro arcade and icy frost."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glow Text Hover Effect
Source: https://codefronts.com/motion/tailwind-css-hover-effects/tailwind-neon-glow-text-hover-effect/

Six electroluminescent text hovers — classic tube, flicker, hue cycle, multi-layer bloom, retro arcade and icy frost. Stacked text-shadow has no utility form and gets none here; what the port gains is that the dim resting glow and the lit hover glow are adjacent, so the pair is edited together.
## HTML
```html
<section class="thv-06 w-full min-h-svh grid place-items-center bg-thv06-bg font-thv06-sans px-6 py-14">
  <div class="w-[min(720px,100%)] flex flex-col gap-3">
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-bold tracking-[0.15em] text-thv06-pink rounded-xs [text-shadow:0_0_4px_#ff00de44] transition-[text-shadow,color] duration-400 hover:text-white hover:[text-shadow:0_0_4px_#fff,0_0_16px_var(--color-thv06-pink),0_0_40px_var(--color-thv06-pink),0_0_80px_var(--color-thv06-pink)] focus-visible:text-white focus-visible:[text-shadow:0_0_4px_#fff,0_0_16px_var(--color-thv06-pink),0_0_40px_var(--color-thv06-pink)] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-pink motion-reduce:transition-none">NEON</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">classic tube glow</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-bold tracking-[0.15em] text-thv06-green rounded-xs transition-[text-shadow,color] duration-300 hover:text-white hover:[text-shadow:0_0_4px_#fff,0_0_18px_var(--color-thv06-green),0_0_50px_var(--color-thv06-green)] hover:animate-thv06-flicker focus-visible:text-white focus-visible:[text-shadow:0_0_4px_#fff,0_0_18px_var(--color-thv06-green),0_0_50px_var(--color-thv06-green)] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-green motion-reduce:hover:animate-none">FLICKER</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">pulsing flicker</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-bold tracking-[0.15em] text-thv06-orange rounded-xs [text-shadow:0_0_4px_#ff440033] transition-[text-shadow,color] duration-400 hover:text-white hover:[text-shadow:0_0_6px_#fff,0_0_20px_var(--color-thv06-orange),0_0_60px_var(--color-thv06-orange)] hover:animate-thv06-hue focus-visible:text-white focus-visible:[text-shadow:0_0_6px_#fff,0_0_20px_var(--color-thv06-orange),0_0_60px_var(--color-thv06-orange)] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-orange motion-reduce:hover:animate-none">SPECTRUM</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">hue-rotate cycle</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-bold tracking-[0.15em] text-thv06-violet rounded-xs [text-shadow:0_0_4px_#7c3aed44] transition-[text-shadow,color] duration-500 ease-[cubic-bezier(.4,0,.2,1)] hover:text-white hover:[text-shadow:0_0_2px_#fff,0_0_8px_#a78bfa,0_0_20px_#7c3aed,0_0_50px_#6d28d9,0_0_100px_#5b21b6,0_0_180px_#4c1d95] focus-visible:text-white focus-visible:[text-shadow:0_0_2px_#fff,0_0_8px_#a78bfa,0_0_20px_#7c3aed,0_0_50px_#6d28d9] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-violet motion-reduce:transition-none">BLOOM</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">multi-layer bloom</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block font-thv06-mono text-[clamp(1.4rem,3.6vw,2.1rem)] font-bold tracking-[0.15em] text-thv06-yellow rounded-xs [text-shadow:0_0_4px_#ffee0044] transition-[text-shadow,color] duration-250 ease-[steps(2)] hover:text-white hover:[text-shadow:2px_2px_0_#ff6600,0_0_10px_var(--color-thv06-yellow),0_0_30px_var(--color-thv06-yellow),0_0_60px_#ff6600] focus-visible:text-white focus-visible:[text-shadow:2px_2px_0_#ff6600,0_0_10px_var(--color-thv06-yellow),0_0_30px_var(--color-thv06-yellow)] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-yellow motion-reduce:transition-none">HI-SCORE</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">retro arcade</span>
    </div>
    <div class="flex flex-wrap items-center justify-between gap-5 px-10 py-8 rounded-xl bg-white/[0.02] border border-white/[0.06]">
      <span tabindex="0" class="inline-block text-[clamp(1.6rem,4vw,2.4rem)] font-bold tracking-[0.15em] text-thv06-ice rounded-xs [text-shadow:0_0_4px_#a5f3fc44] transition-[text-shadow,color,letter-spacing] duration-500 hover:text-white hover:tracking-[0.25em] hover:[text-shadow:0_0_4px_#fff,0_0_16px_var(--color-thv06-ice),0_0_40px_#0ea5e9,0_0_80px_#0369a1] focus-visible:text-white focus-visible:tracking-[0.25em] focus-visible:[text-shadow:0_0_4px_#fff,0_0_16px_var(--color-thv06-ice),0_0_40px_#0ea5e9] focus-visible:outline-2 focus-visible:outline-offset-6 focus-visible:outline-thv06-ice motion-reduce:transition-none">ICE</span>
      <span class="shrink-0 text-[11px] tracking-[0.12em] uppercase text-thv06-dim">icy frost glow</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-thv06-bg: #020204;
  --color-thv06-bg: oklch(0.09 0.01 285);
  --color-thv06-dim: #3a3a4a;
  --color-thv06-dim: oklch(0.37 0.02 285);
  --color-thv06-pink: #ff00de;
  --color-thv06-pink: oklch(0.66 0.35 330);
  --color-thv06-green: #39ff14;
  --color-thv06-green: oklch(0.88 0.29 135);
  --color-thv06-orange: #ff4400;
  --color-thv06-orange: oklch(0.65 0.24 37);
  --color-thv06-violet: #7c3aed;
  --color-thv06-violet: oklch(0.54 0.25 295);
  --color-thv06-yellow: #ffee00;
  --color-thv06-yellow: oklch(0.93 0.2 106);
  --color-thv06-ice: #a5f3fc;
  --color-thv06-ice: oklch(0.9 0.08 200);
  --font-thv06-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-thv06-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-thv06-flicker: thv06-flicker 2s linear infinite;
  --animate-thv06-hue: thv06-hue 3s linear infinite;
}

.thv-06 {
  width: 100%;
  min-height: 100svh;
}

.thv-06 ::selection {
  background: var(--color-thv06-pink);
  color: #fff;
}

@keyframes thv06-flicker {
  0%,
    19%,
    21%,
    23%,
    25%,
    54%,
    56%,
    100% {
    text-shadow: 0 0 4px #fff, 0 0 18px var(--color-thv06-green), 0 0 50px var(--color-thv06-green);
    color: #fff;
  }

  20%,
    24%,
    55% {
    text-shadow: none;
    color: var(--color-thv06-green);
  }
}

@keyframes thv06-hue {
  0% {
    filter: hue-rotate(0deg);
  }

  100% {
    filter: hue-rotate(360deg);
  }
}
```
