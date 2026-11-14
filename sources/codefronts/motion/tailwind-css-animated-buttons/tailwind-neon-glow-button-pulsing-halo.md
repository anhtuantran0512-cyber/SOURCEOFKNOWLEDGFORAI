---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-neon-glow-button-pulsing-halo/"
title: "Tailwind Neon Glow Button with Pulsing Halo"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A neon-lit CTA with a breathing glow halo, ported to a single class list."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Neon Glow Button with Pulsing Halo
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-neon-glow-button-pulsing-halo/

A neon-lit CTA with a breathing glow halo, ported to a single class list. The port's win is --animate-tab01-pulse: the whole animation shorthand is declared once as a token, so the markup says animate-tab01-pulse and the hover override says hover:[animation-play-state:paused] — the trigger reads where the button is, not three rules away.
## HTML
```html
<section class="tab-01 w-full min-h-svh grid place-items-center bg-tab01-bg font-tab01-sans px-6 py-10">
  <div class="w-[min(520px,100%)] text-center">
    <p class="text-xs font-medium tracking-[0.18em] uppercase text-tab01-neon/80 m-0">Premium SaaS &mdash; Launch Your Project</p>
    <h2 class="mt-3 mb-3 text-[clamp(1.8rem,4vw,2.6rem)] font-bold leading-[1.15] text-white">Build faster.<br>Ship smarter.</h2>
    <p class="mb-8 text-[0.95rem] text-tab01-ink/70">Join 50,000+ developers already on the platform.</p>
    <button type="button" class="inline-flex items-center justify-center gap-2 min-h-11 px-10 py-3.5 text-base font-bold uppercase tracking-[0.04em] text-white bg-transparent border-2 border-tab01-neon rounded-lg cursor-pointer animate-tab01-pulse [text-shadow:0_0_8px_var(--color-tab01-glow)] transition-[color,background-color,border-color,box-shadow] duration-300 hover:bg-tab01-neon hover:shadow-[0_0_16px_var(--color-tab01-neon),0_0_40px_var(--color-tab01-neon),inset_0_0_16px_oklch(1_0_0/0.15)] hover:[text-shadow:none] hover:[animation-play-state:paused] focus-visible:outline-3 focus-visible:outline-tab01-neon focus-visible:outline-offset-4 active:scale-[0.97] motion-reduce:animate-none motion-reduce:transition-none">Get Started Free</button>
    <p class="mt-4 text-[0.78rem] text-tab01-ink/45">No credit card required &middot; Cancel anytime</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab01-bg: #0a0010;
  --color-tab01-bg: oklch(0.09 0.04 305);
  --color-tab01-neon: #b829ff;
  --color-tab01-neon: oklch(0.62 0.28 305);
  --color-tab01-glow: #b829ff99;
  --color-tab01-glow: oklch(0.62 0.28 305 / 0.6);
  --color-tab01-ink: #e8d5ff;
  --color-tab01-ink: oklch(0.9 0.06 305);
  --font-tab01-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab01-pulse: tab01-pulse 2s ease-in-out infinite;
}

@keyframes tab01-pulse {
  0%,
    100% {
    box-shadow: 0 0 8px var(--color-tab01-glow), 0 0 20px var(--color-tab01-glow), inset 0 0 10px oklch(0.62 0.28 305 / 0.1);
  }

  50% {
    box-shadow: 0 0 14px var(--color-tab01-neon), 0 0 36px var(--color-tab01-glow), 0 0 60px oklch(0.62 0.28 305 / 0.2), inset 0 0 16px oklch(0.62 0.28 305 / 0.14);
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's
   w-full min-h-svh, so the stage is sized before the browser build has compiled. */

.tab-01 {
  width: 100%;
  min-height: 100svh;
}

.tab-01 ::selection {
  background: var(--color-tab01-neon);
  color: #fff;
}
```
