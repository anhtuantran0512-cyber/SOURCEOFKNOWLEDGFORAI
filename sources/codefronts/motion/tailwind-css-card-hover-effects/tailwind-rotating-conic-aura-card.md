---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-rotating-conic-aura-card/"
title: "Tailwind Rotating Conic Aura Card with Blurred Gradient Bloom"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A creative-suite card sitting inside a heavily blurred conic gradient that rotates behind an inset inner panel, so the card wears a live rainbow aura."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Rotating Conic Aura Card with Blurred Gradient Bloom
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-rotating-conic-aura-card/

A creative-suite card sitting inside a heavily blurred conic gradient that rotates behind an inset inner panel, so the card wears a live rainbow aura. Same @property machinery as demo 08, but the gradient is oversized and blurred rather than masked &mdash; a softer, cheaper ring.
## HTML
```html
<section class="tch-21 w-full min-h-svh grid place-items-center bg-tch21-bg font-tch21-sans p-8">
  <article class="group relative w-[330px] h-[430px] rounded-3xl overflow-hidden isolate cursor-pointer bg-tch21-card
    before:content-[''] before:absolute before:-inset-[40%] before:z-0 before:opacity-65 before:blur-[40px] before:saturate-[1.2] before:transition-opacity before:duration-500 group-hover:before:opacity-100 group-focus-within:before:opacity-100 before:bg-[conic-gradient(from_var(--tch21-angle,0deg),#ff4d6d,#ffa64d,#ffe14d,#4dffa6,#4dd2ff,#b04dff,#ff4d6d)] before:animate-tch21-spin before:[animation-play-state:paused] group-hover:before:[animation-play-state:running] motion-reduce:before:animate-none
    after:content-[''] after:absolute after:inset-0.5 after:z-1 after:rounded-[22px] after:bg-[linear-gradient(160deg,#15151e,#0c0c12)]">
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch21-ink">
      <span class="font-tch21-mono text-[0.72rem] tracking-[0.2em] text-tch21-mut">AI · CREATIVE SUITE</span>
      <h2 class="font-bold text-[2.6rem] leading-none bg-[linear-gradient(120deg,#ff8aa0,#ffd24d,#6ad6ff)] bg-clip-text text-transparent">Spectra<br>Studio</h2>
      <p class="font-light text-[0.88rem] leading-[1.6] text-tch21-body">Generate, remix, and color-grade in one canvas. The aura rotates while the engine warms up.</p>
      <a href="#" class="inline-flex items-center min-h-11 font-tch21-mono text-[0.78rem] tracking-[0.1em] text-tch21-acc no-underline rounded transition-colors duration-200 hover:text-white focus-visible:outline-2 focus-visible:outline-tch21-acc focus-visible:outline-offset-2">→ START FREE TRIAL</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@property --tch21-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@keyframes tch21-spin {
  to {
    --tch21-angle: 360deg;
  }
}

@theme {
  --color-tch21-bg: #0a0a0f;
  --color-tch21-bg: oklch(0.11 0.006 285);
  --color-tch21-card: #111118;
  --color-tch21-card: oklch(0.15 0.008 285);
  --color-tch21-ink: #f2f2f7;
  --color-tch21-ink: oklch(0.96 0.003 285);
  --color-tch21-body: #a6a6bc;
  --color-tch21-body: oklch(0.72 0.02 285);
  --color-tch21-mut: #9a9ab0;
  --color-tch21-mut: oklch(0.67 0.02 285);
  --color-tch21-acc: #ffd24d;
  --color-tch21-acc: oklch(0.88 0.15 88);
  --font-tch21-sans: 'Outfit', system-ui, sans-serif;
  --font-tch21-mono: 'Azeret Mono', ui-monospace, monospace;
  --animate-tch21-spin: tch21-spin 6s linear infinite;
}

.tch-21 {
  width: 100%;
  min-height: 100svh;
}
```
