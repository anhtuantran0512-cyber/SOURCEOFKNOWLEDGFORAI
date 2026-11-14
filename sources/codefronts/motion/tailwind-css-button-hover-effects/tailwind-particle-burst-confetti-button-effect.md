---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-particle-burst-confetti-button-effect/"
title: "Tailwind Particle Burst Confetti Button Effect"
section: "motion"
category: "tailwind-css-button-hover-effects"
category_name: "Tailwind CSS Button Hover Effects"
description: "A celebratory CTA that scatters particles outward on hover &mdash; confetti-style points fly out and fade."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Particle Burst Confetti Button Effect
Source: https://codefronts.com/motion/tailwind-css-button-hover-effects/tailwind-particle-burst-confetti-button-effect/

A celebratory CTA that scatters particles outward on hover &mdash; confetti-style points fly out and fade. Every particle is a box-shadow clone of one 6px dot, which means eight particles cost one element and zero extra DOM.
## HTML
```html
<div class="tbh-24-group w-full min-h-svh flex flex-wrap">
<section class="tbh-24a flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh24-sans bg-tbh24a-stage" aria-label="Particle burst button">
  <button type="button" class="group/btn relative overflow-visible cursor-pointer border-0 rounded-full px-[42px] py-4 text-base font-extrabold text-white bg-tbh24a-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span aria-hidden="true" class="absolute left-1/2 top-1/2 w-1.5 h-1.5 rounded-full bg-tbh24a-p4 opacity-0 pointer-events-none shadow-[34px_-18px_var(--color-tbh24a-p1),-40px_-10px_var(--color-tbh24a-p2),54px_12px_var(--color-tbh24a-p3),-30px_20px_var(--color-tbh24a-p4)] group-hover/btn:animate-tbh24a-burst group-focus-visible/btn:animate-tbh24a-burst motion-reduce:group-hover/btn:animate-none"></span>
    <span aria-hidden="true" class="absolute left-1/2 top-1/2 w-1.5 h-1.5 rounded-full bg-tbh24a-p2 opacity-0 pointer-events-none shadow-[20px_-30px_var(--color-tbh24a-p2),-52px_6px_var(--color-tbh24a-p4),44px_26px_var(--color-tbh24a-p1),-18px_-26px_var(--color-tbh24a-p3)] group-hover/btn:animate-tbh24a-burst group-focus-visible/btn:animate-tbh24a-burst motion-reduce:group-hover/btn:animate-none"></span>
    <span class="relative z-[1]">Like</span>
  </button>
</section>
<section class="tbh-24b flex-[1_1_340px] min-w-[300px] grid place-items-center px-6 py-14 font-tbh24-sans bg-tbh24b-stage" aria-label="Spark ring button">
  <button type="button" class="group/btn relative overflow-visible cursor-pointer border-0 rounded-full px-[42px] py-4 text-base font-extrabold text-tbh24b-ink bg-tbh24b-acc focus-visible:outline-3 focus-visible:outline-white focus-visible:outline-offset-4">
    <span aria-hidden="true" class="absolute left-1/2 top-1/2 -ml-1 -mt-1 w-2 h-2 rounded-full bg-transparent opacity-0 scale-[.3] pointer-events-none shadow-[0_-34px_var(--color-tbh24b-acc),24px_-24px_var(--color-tbh24b-acc),34px_0_var(--color-tbh24b-acc),24px_24px_var(--color-tbh24b-acc),0_34px_var(--color-tbh24b-acc),-24px_24px_var(--color-tbh24b-acc),-34px_0_var(--color-tbh24b-acc),-24px_-24px_var(--color-tbh24b-acc)] group-hover/btn:animate-tbh24b-spark group-focus-visible/btn:animate-tbh24b-spark motion-reduce:group-hover/btn:animate-none"></span>
    <span class="relative z-[1]">Boost</span>
  </button>
</section>
</div>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbh24a-acc: #e0492f;
  --color-tbh24a-acc: oklch(0.62 0.22 20);
  --color-tbh24a-p1: #ff7ab6;
  --color-tbh24a-p1: oklch(0.78 0.16 350);
  --color-tbh24a-p2: #7ce0ff;
  --color-tbh24a-p2: oklch(0.87 0.11 215);
  --color-tbh24a-p3: #b6ff7a;
  --color-tbh24a-p3: oklch(0.92 0.18 130);
  --color-tbh24a-p4: #ffd15c;
  --color-tbh24a-p4: oklch(0.87 0.15 90);
  --color-tbh24a-stage: #120a0e;
  --color-tbh24a-stage: oklch(0.15 0.02 20);
  --color-tbh24b-acc: #e0b04a;
  --color-tbh24b-acc: oklch(0.78 0.15 90);
  --color-tbh24b-ink: #1a1206;
  --color-tbh24b-ink: oklch(0.22 0.04 85);
  --color-tbh24b-stage: #14100a;
  --color-tbh24b-stage: oklch(0.16 0.02 85);
  --font-tbh24-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tbh24a-burst: tbh24a-burst 0.6s ease-out;
  --animate-tbh24b-spark: tbh24b-spark 0.55s ease-out;
}
/* Stays CSS: two one-shot keyframes. Both hold the -50% centring in translate and animate
   only scale and opacity, so the utilities and the keyframe never fight over a property. */

@keyframes tbh24a-burst {
  0% {
    opacity: 1;
    translate: -50% -50%;
    scale: 0.2;
  }

  100% {
    opacity: 0;
    translate: -50% -50%;
    scale: 1.6;
  }
}

@keyframes tbh24b-spark {
  0% {
    opacity: 1;
    scale: 0.3;
  }

  100% {
    opacity: 0;
    scale: 1.5;
  }
}

.tbh-24-group {
  width: 100%;
  min-height: 100svh;
}

.tbh-24a,
.tbh-24b {
  min-height: 100svh;
}
```
