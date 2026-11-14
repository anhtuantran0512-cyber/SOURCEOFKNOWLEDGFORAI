---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-shine-sweep-hover-button/"
title: "Tailwind Shine Sweep Hover Button with Gloss Streak"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A narrow band of light crosses the button face once per hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Shine Sweep Hover Button with Gloss Streak
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-shine-sweep-hover-button/

A narrow band of light crosses the button face once per hover. The port puts the streak's whole identity &mdash; gradient, tilt, starting position &mdash; on the element as before: utilities, and its motion in one hover:before:animate-tab08-shine.
## HTML
```html
<section class="tab-08 w-full min-h-svh grid place-items-center bg-tab08-bg font-tab08-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab08-mut m-0">Hover over the buttons</p>
    <div class="flex flex-wrap justify-center gap-4">
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-tab08-ink bg-tab08-slate rounded-[10px] cursor-pointer transition-[translate,filter] duration-150 hover:brightness-110 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab08-slate before:content-[''] before:absolute before:-top-[10%] before:-left-[20%] before:w-[60%] before:h-[120%] before:bg-[linear-gradient(105deg,transparent_30%,oklch(1_0_0/0.55)_50%,transparent_70%)] before:-skew-x-[15deg] before:-translate-x-full before:pointer-events-none hover:before:animate-tab08-shine focus-visible:before:animate-tab08-shine motion-reduce:hover:before:animate-none motion-reduce:transition-none">Pro Features</button>
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-white bg-[linear-gradient(135deg,#b45309,#d97706,#fbbf24)] rounded-[10px] cursor-pointer transition-[translate,filter] duration-150 hover:brightness-110 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab08-gold before:content-[''] before:absolute before:-top-[10%] before:-left-[20%] before:w-[60%] before:h-[120%] before:bg-[linear-gradient(105deg,transparent_30%,oklch(1_0_0/0.55)_50%,transparent_70%)] before:-skew-x-[15deg] before:-translate-x-full before:pointer-events-none hover:before:animate-tab08-shine focus-visible:before:animate-tab08-shine motion-reduce:hover:before:animate-none motion-reduce:transition-none">Upgrade Now</button>
      <button type="button" class="relative overflow-hidden min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-white bg-[linear-gradient(135deg,#4c1d95,#7c3aed,#a78bfa)] rounded-[10px] cursor-pointer transition-[translate,filter] duration-150 hover:brightness-110 hover:-translate-y-0.5 active:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab08-violet before:content-[''] before:absolute before:-top-[10%] before:-left-[20%] before:w-[60%] before:h-[120%] before:bg-[linear-gradient(105deg,transparent_30%,oklch(1_0_0/0.55)_50%,transparent_70%)] before:-skew-x-[15deg] before:-translate-x-full before:pointer-events-none hover:before:animate-tab08-shine focus-visible:before:animate-tab08-shine motion-reduce:hover:before:animate-none motion-reduce:transition-none">Get Premium</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab08-bg: #f1f5f9;
  --color-tab08-bg: oklch(0.97 0.006 250);
  --color-tab08-mut: #64748b;
  --color-tab08-mut: oklch(0.55 0.03 255);
  --color-tab08-slate: #1e293b;
  --color-tab08-slate: oklch(0.28 0.03 258);
  --color-tab08-ink: #e2e8f0;
  --color-tab08-ink: oklch(0.92 0.01 250);
  --color-tab08-gold: #b45309;
  --color-tab08-gold: oklch(0.53 0.15 62);
  --color-tab08-violet: #4c1d95;
  --color-tab08-violet: oklch(0.36 0.2 296);
  --font-tab08-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab08-shine: tab08-shine 0.55s ease-in-out forwards;
}

@keyframes tab08-shine {
  0% {
    translate: -100% 0;
  }

  100% {
    translate: 400% 0;
  }
}

.tab-08 {
  width: 100%;
  min-height: 100svh;
}

.tab-08 ::selection {
  background: var(--color-tab08-slate);
  color: #fff;
}
```
