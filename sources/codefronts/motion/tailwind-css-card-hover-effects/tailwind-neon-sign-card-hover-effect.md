---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-neon-sign-card-hover-effect/"
title: "Tailwind Neon Sign Card with Layered Text-Shadow Glow"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A dim brick-wall bar card whose sign ignites into flickering neon on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Sign Card with Layered Text-Shadow Glow
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-neon-sign-card-hover-effect/

A dim brick-wall bar card whose sign ignites into flickering neon on hover. Tailwind has no text-shadow colour scale worth using for four-layer tube glow, so the stacks become --text-shadow-* @theme entries &mdash; and the flicker stays a keyframe, exposed back as animate-tch13-flicker.
## HTML
```html
<section class="tch-13 w-full min-h-svh grid place-items-center bg-[radial-gradient(circle_at_50%_120%,#1a1430_0%,#050308_70%)] font-tch13-sans p-8">
  <article tabindex="0" class="group relative w-[330px] h-[430px] rounded-2xl overflow-hidden cursor-pointer outline-none bg-tch13-card border-2 border-white/4 transition-shadow duration-500 hover:shadow-[0_0_50px_rgb(255_45_149/0.25)] focus-visible:shadow-[0_0_50px_rgb(255_45_149/0.25)] focus-visible:outline-3 focus-visible:outline-tch13-cyan focus-visible:outline-offset-4 before:content-[''] before:absolute before:inset-0 before:opacity-70 before:bg-[linear-gradient(rgb(10_7_18/0.85),rgb(10_7_18/0.92)),repeating-linear-gradient(0deg,#181020_0_24px,transparent_24px_26px),repeating-linear-gradient(90deg,#181020_0_48px,transparent_48px_50px)]">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between items-center text-center">
      <span class="font-tch13-mono text-[0.85rem] tracking-[0.3em] text-tch13-cyan opacity-40 transition-[opacity,text-shadow] duration-400 group-hover:opacity-100 group-hover:text-shadow-tch13-cyan group-focus-visible:opacity-100 group-focus-visible:text-shadow-tch13-cyan">— open till late —</span>
      <h2 class="font-tch13-display text-[3.4rem] leading-[0.95] text-tch13-dead transition-[color,text-shadow] duration-500 group-hover:text-tch13-pink group-hover:text-shadow-tch13-pink group-hover:animate-tch13-flicker group-focus-visible:text-tch13-pink group-focus-visible:text-shadow-tch13-pink motion-reduce:group-hover:animate-none">Lola's</h2>
      <p class="font-tch13-mono text-[1.1rem] text-tch13-dead transition-[color,text-shadow] duration-500 delay-100 group-hover:text-tch13-cyan group-hover:text-shadow-tch13-cyan group-focus-visible:text-tch13-cyan group-focus-visible:text-shadow-tch13-cyan">cocktail bar</p>
      <p class="text-[0.85rem] leading-[1.6] text-tch13-body max-w-[90%]">Hover to light the sign. Hand-bent tubes, mezcal flights, and a back room you have to ask about.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@keyframes tch13-flicker {
  0%,
    18%,
    22%,
    25%,
    53%,
    57%,
    100% {
    opacity: 1;
  }

  20%,
    24%,
    55% {
    opacity: 0.65;
    text-shadow: none;
  }
}

@theme {
  --color-tch13-card: #0a0712;
  --color-tch13-card: oklch(0.12 0.02 295);
  --color-tch13-dead: #2a1a35;
  --color-tch13-dead: oklch(0.25 0.04 305);
  --color-tch13-body: #8a7a9a;
  --color-tch13-body: oklch(0.6 0.04 300);
  --color-tch13-pink: #ff2d95;
  --color-tch13-pink: oklch(0.67 0.26 355);
  --color-tch13-cyan: #29f5ff;
  --color-tch13-cyan: oklch(0.89 0.14 200);
  --font-tch13-sans: 'Oxanium', system-ui, sans-serif;
  --font-tch13-mono: 'Major Mono Display', ui-monospace, monospace;
  --font-tch13-display: 'Monoton', cursive;
  --text-shadow-tch13-pink: 0 0 6px #ff2d95, 0 0 14px #ff2d95, 0 0 30px #ff2d95, 0 0 60px #ff2d95;
  --text-shadow-tch13-cyan: 0 0 6px #29f5ff, 0 0 16px #29f5ff;
  --animate-tch13-flicker: tch13-flicker 3s infinite;
}

.tch-13 {
  width: 100%;
  min-height: 100svh;
}
```
