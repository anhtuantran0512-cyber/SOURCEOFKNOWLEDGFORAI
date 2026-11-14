---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-liquid-fill-button-animation/"
title: "Tailwind Liquid Fill Button with Animated Wave Crest"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Liquid rises to fill the button on hover, its surface undulating while it sits there."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Liquid Fill Button with Animated Wave Crest
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-liquid-fill-button-animation/

Liquid rises to fill the button on hover, its surface undulating while it sits there. Two motions, two mechanisms: a transition for the rise and a keyframe for the wave &mdash; and the port makes the split explicit, since the rise is a utility pair and the wave is hover:before:animate-tab06-wave.
## HTML
```html
<section class="tab-06 w-full min-h-svh grid place-items-center bg-tab06-bg font-tab06-sans px-6 py-10">
  <div class="flex flex-col items-center gap-10">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab06-mut m-0">Hover to fill</p>
    <div class="flex flex-wrap justify-center gap-5">
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-base font-bold tracking-[0.03em] text-tab06-cyan-ink bg-transparent border-2 border-tab06-cyan-edge rounded-[10px] cursor-pointer transition-colors duration-[400ms] hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab06-cyan-edge focus-visible:text-white before:content-[''] before:absolute before:bottom-0 before:-left-1/4 before:w-[150%] before:h-[200%] before:bg-tab06-cyan before:[border-radius:45%_55%_0_0/25%_25%_0_0] before:translate-y-full before:transition-transform before:duration-[650ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:before:translate-y-[5%] hover:before:animate-tab06-wave focus-visible:before:translate-y-[5%] motion-reduce:before:transition-none motion-reduce:hover:before:animate-none"><span class="relative z-10">Explore</span></button>
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-base font-bold tracking-[0.03em] text-tab06-violet-ink bg-transparent border-2 border-tab06-violet-edge rounded-[10px] cursor-pointer transition-colors duration-[400ms] hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab06-violet-edge focus-visible:text-white before:content-[''] before:absolute before:bottom-0 before:-left-1/4 before:w-[150%] before:h-[200%] before:bg-tab06-violet before:[border-radius:45%_55%_0_0/25%_25%_0_0] before:translate-y-full before:transition-transform before:duration-[650ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:before:translate-y-[5%] hover:before:animate-tab06-wave focus-visible:before:translate-y-[5%] motion-reduce:before:transition-none motion-reduce:hover:before:animate-none"><span class="relative z-10">Subscribe</span></button>
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-base font-bold tracking-[0.03em] text-tab06-amber-ink bg-transparent border-2 border-tab06-amber-edge rounded-[10px] cursor-pointer transition-colors duration-[400ms] hover:text-white focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab06-amber-edge focus-visible:text-white before:content-[''] before:absolute before:bottom-0 before:-left-1/4 before:w-[150%] before:h-[200%] before:bg-tab06-amber before:[border-radius:45%_55%_0_0/25%_25%_0_0] before:translate-y-full before:transition-transform before:duration-[650ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:before:translate-y-[5%] hover:before:animate-tab06-wave focus-visible:before:translate-y-[5%] motion-reduce:before:transition-none motion-reduce:hover:before:animate-none"><span class="relative z-10">Upgrade</span></button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab06-bg: #0f172a;
  --color-tab06-bg: oklch(0.21 0.04 258);
  --color-tab06-mut: #94a3b8;
  --color-tab06-mut: oklch(0.72 0.03 255);
  --color-tab06-cyan: #0e7490;
  --color-tab06-cyan: oklch(0.48 0.1 221);
  --color-tab06-cyan-edge: #22d3ee;
  --color-tab06-cyan-edge: oklch(0.79 0.14 202);
  --color-tab06-cyan-ink: #a5f3fc;
  --color-tab06-cyan-ink: oklch(0.9 0.08 202);
  --color-tab06-violet: #6d28d9;
  --color-tab06-violet: oklch(0.47 0.24 295);
  --color-tab06-violet-edge: #a78bfa;
  --color-tab06-violet-edge: oklch(0.74 0.15 292);
  --color-tab06-violet-ink: #ddd6fe;
  --color-tab06-violet-ink: oklch(0.89 0.06 292);
  --color-tab06-amber: #b45309;
  --color-tab06-amber: oklch(0.53 0.15 62);
  --color-tab06-amber-edge: #fbbf24;
  --color-tab06-amber-edge: oklch(0.84 0.16 84);
  --color-tab06-amber-ink: #fef3c7;
  --color-tab06-amber-ink: oklch(0.95 0.05 90);
  --font-tab06-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab06-wave: tab06-wave 2.5s ease-in-out infinite 0.65s;
}

@keyframes tab06-wave {
  0%,
    100% {
    border-radius: 45% 55% 0 0 / 25% 25% 0 0;
  }

  50% {
    border-radius: 55% 45% 0 0 / 20% 30% 0 0;
  }
}

.tab-06 {
  width: 100%;
  min-height: 100svh;
}

.tab-06 ::selection {
  background: var(--color-tab06-cyan-edge);
  color: #0b1220;
}
```
