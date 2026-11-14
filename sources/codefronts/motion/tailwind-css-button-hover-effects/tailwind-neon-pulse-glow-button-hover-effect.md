---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-neon-pulse-glow-button-hover-effect/"
title: "Tailwind Neon Pulse Glow Button Hover Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A glowing CTA whose neon halo breathes: on hover a heavy blurred glow scales gently in and out on a loop, so the button looks like a live light source…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Pulse Glow Button Hover Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-neon-pulse-glow-button-hover-effect/

A glowing CTA whose neon halo breathes: on hover a heavy blurred glow scales gently in and out on a loop, so the button looks like a live light source &mdash; the soft looping counterpart to entry 11's hard snap. The reduced-motion fallback here is the interesting part: a steady mid-glow, not an absence.
## HTML
```html
<div class="tbh-18-group w-full min-h-svh flex flex-wrap">
<section class="tbh-18a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh18-sans bg-tbh18a-stage" aria-label="Neon pulse button">
  <button type="button" class="cursor-pointer rounded-full border-2 border-tbh18a-neon px-10 py-4 text-base font-extrabold uppercase tracking-[0.05em] text-white bg-[color-mix(in_oklab,var(--color-tbh18a-neon)_24%,var(--color-tbh18a-stage))] shadow-[0_0_14px_-2px_color-mix(in_oklab,var(--color-tbh18a-neon)_70%,transparent)] transition-colors duration-200 hover:animate-tbh18a-pulse focus-visible:animate-tbh18a-pulse focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:shadow-[0_0_24px_3px_var(--color-tbh18a-neon)] motion-reduce:focus-visible:shadow-[0_0_24px_3px_var(--color-tbh18a-neon)]">
    Go live
  </button>
</section>
<section class="tbh-18b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh18-sans bg-tbh18b-stage" aria-label="Neon flicker button">
  <button type="button" class="cursor-pointer rounded-lg border-2 border-tbh18b-neon px-[42px] py-4 text-base font-extrabold uppercase tracking-[0.08em] text-tbh18b-neon bg-transparent [text-shadow:0_0_8px_var(--color-tbh18b-neon)] shadow-[0_0_10px_-2px_var(--color-tbh18b-neon),inset_0_0_10px_-4px_var(--color-tbh18b-neon)] transition-colors duration-200 hover:animate-tbh18b-flick focus-visible:animate-tbh18b-flick focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4 motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:shadow-[0_0_22px_-2px_var(--color-tbh18b-neon),inset_0_0_14px_-4px_var(--color-tbh18b-neon)]">
    Open bar
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh18a-neon: #e065c6;
  --color-tbh18a-neon: oklch(0.72 0.2 330);
  --color-tbh18a-stage: #0a0710;
  --color-tbh18a-stage: oklch(0.12 0.02 320);
  --color-tbh18b-neon: #5fdde8;
  --color-tbh18b-neon: oklch(0.78 0.16 195);
  --color-tbh18b-stage: #04100f;
  --color-tbh18b-stage: oklch(0.13 0.02 195);
  --font-tbh18-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh18a-pulse: tbh18a-pulse 1.4s ease-in-out infinite;
  --animate-tbh18b-flick: tbh18b-flick 2.2s steps(1) infinite;
}
/* Stays CSS: both keyframes animate box-shadow, text-shadow and filter — none of which
   has a keyframe-able utility form, and all of which repaint rather than composite. */

@keyframes tbh18a-pulse {
  0%,
    100% {
    box-shadow: 0 0 12px -2px color-mix(in oklab, var(--color-tbh18a-neon) 65%, transparent);
    text-shadow: 0 0 6px color-mix(in oklab, var(--color-tbh18a-neon) 60%, transparent);
    filter: brightness(1);
  }

  50% {
    box-shadow: 0 0 34px 6px var(--color-tbh18a-neon), 0 0 60px 12px color-mix(in oklab, var(--color-tbh18a-neon) 55%, transparent);
    text-shadow: 0 0 16px var(--color-tbh18a-neon);
    filter: brightness(1.25);
  }
}

@keyframes tbh18b-flick {
  0%,
    19%,
    21%,
    23%,
    80%,
    100% {
    opacity: 1;
    box-shadow: 0 0 22px -2px var(--color-tbh18b-neon), inset 0 0 14px -4px var(--color-tbh18b-neon);
  }

  20%,
    22% {
    opacity: 0.5;
    box-shadow: none;
  }
}

.tbh-18-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-18a,
.tbh-18b {
  min-height: 100svh;
}
```
