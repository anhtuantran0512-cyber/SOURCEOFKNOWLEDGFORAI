---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-ripple-effect-button-no-javascript/"
title: "Tailwind Ripple Effect Button with No JavaScript"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A Material-style ripple that fires on press with no JavaScript at all."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Ripple Effect Button with No JavaScript
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-ripple-effect-button-no-javascript/

A Material-style ripple that fires on press with no JavaScript at all. The port's interesting line is active:after:animate-tab03-ripple &mdash; two variants stacked, reading "while pressed, run the ripple on my own after-layer", which is the entire behaviour in one class.
## HTML
```html
<section class="tab-03 w-full min-h-svh grid place-items-center bg-tab03-bg font-tab03-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab03-violet/70 m-0">Click or tap to trigger</p>
    <div class="flex flex-wrap justify-center gap-4">
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-white bg-tab03-violet rounded-[10px] cursor-pointer transition-[filter] duration-200 hover:brightness-110 active:brightness-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab03-violet after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:size-0 after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:bg-white/40 after:opacity-0 after:pointer-events-none active:after:animate-tab03-ripple motion-reduce:active:after:animate-none">Get Started</button>
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-white bg-tab03-teal rounded-[10px] cursor-pointer transition-[filter] duration-200 hover:brightness-110 active:brightness-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab03-teal after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:size-0 after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:bg-white/40 after:opacity-0 after:pointer-events-none active:after:animate-tab03-ripple motion-reduce:active:after:animate-none">Learn More</button>
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-white bg-tab03-rose rounded-[10px] cursor-pointer transition-[filter] duration-200 hover:brightness-110 active:brightness-90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab03-rose after:content-[''] after:absolute after:top-1/2 after:left-1/2 after:size-0 after:-translate-x-1/2 after:-translate-y-1/2 after:rounded-full after:bg-white/40 after:opacity-0 after:pointer-events-none active:after:animate-tab03-ripple motion-reduce:active:after:animate-none">Subscribe</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab03-bg: #0f0c1a;
  --color-tab03-bg: oklch(0.14 0.03 295);
  --color-tab03-violet: #7c3aed;
  --color-tab03-violet: oklch(0.53 0.25 295);
  --color-tab03-teal: #0d9488;
  --color-tab03-teal: oklch(0.56 0.11 184);
  --color-tab03-rose: #e11d48;
  --color-tab03-rose: oklch(0.57 0.22 13);
  --font-tab03-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab03-ripple: tab03-ripple 0.6s linear forwards;
}

@keyframes tab03-ripple {
  0% {
    width: 0;
    height: 0;
    opacity: 0.4;
  }

  80% {
    width: 400%;
    height: 400%;
    opacity: 0.1;
  }

  100% {
    width: 500%;
    height: 500%;
    opacity: 0;
  }
}

.tab-03 {
  width: 100%;
  min-height: 100svh;
}

.tab-03 ::selection {
  background: var(--color-tab03-violet);
  color: #fff;
}
```
