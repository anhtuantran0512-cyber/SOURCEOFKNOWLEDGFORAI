---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-jelly-bounce-button-animation/"
title: "Tailwind Jelly Bounce Button with Elastic Squash"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Squash, stretch, and a settling wobble &mdash; seven keyframe steps of jelly physics."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Jelly Bounce Button with Elastic Squash
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-jelly-bounce-button-animation/

Squash, stretch, and a settling wobble &mdash; seven keyframe steps of jelly physics. Nothing about the timeline can become a utility, and that is the point: the port keeps the keyframe verbatim and reduces the CSS to a single trigger, hover:animate-tab09-jelly.
## HTML
```html
<section class="tab-09 w-full min-h-svh grid place-items-center bg-tab09-bg font-tab09-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8 py-6">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab09-mut m-0">Hover for jelly effect</p>
    <div class="flex flex-wrap justify-center gap-5">
      <button type="button" class="min-h-11 px-9 text-[1.05rem] font-bold tracking-[0.03em] text-white bg-tab09-pink rounded-full cursor-pointer origin-center will-change-transform shadow-[0_4px_16px_oklch(0_0_0/0.15)] hover:animate-tab09-jelly focus-visible:animate-tab09-jelly focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab09-pink motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:scale-[1.04]">Subscribe!</button>
      <button type="button" class="min-h-11 px-9 text-[1.05rem] font-bold tracking-[0.03em] text-white bg-tab09-green rounded-full cursor-pointer origin-center will-change-transform shadow-[0_4px_16px_oklch(0_0_0/0.15)] hover:animate-tab09-jelly focus-visible:animate-tab09-jelly focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab09-green motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:scale-[1.04]">Let's Go!</button>
      <button type="button" class="min-h-11 px-9 text-[1.05rem] font-bold tracking-[0.03em] text-white bg-tab09-sky rounded-full cursor-pointer origin-center will-change-transform shadow-[0_4px_16px_oklch(0_0_0/0.15)] hover:animate-tab09-jelly focus-visible:animate-tab09-jelly focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tab09-sky motion-reduce:hover:animate-none motion-reduce:focus-visible:animate-none motion-reduce:hover:scale-[1.04]">Join Now!</button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab09-bg: #fdf2ff;
  --color-tab09-bg: oklch(0.97 0.03 320);
  --color-tab09-mut: #a855f7;
  --color-tab09-mut: oklch(0.63 0.24 303);
  --color-tab09-pink: #db2777;
  --color-tab09-pink: oklch(0.59 0.22 354);
  --color-tab09-green: #16a34a;
  --color-tab09-green: oklch(0.58 0.16 149);
  --color-tab09-sky: #0284c7;
  --color-tab09-sky: oklch(0.56 0.15 240);
  --font-tab09-sans: 'Space Grotesk', system-ui, sans-serif;
  --animate-tab09-jelly: tab09-jelly 0.7s cubic-bezier(0.4, 0, 0.2, 1) both;
}

@keyframes tab09-jelly {
  0% {
    scale: 1 1;
  }

  10% {
    scale: 1.2 0.85;
  }

  25% {
    scale: 0.85 1.15;
  }

  40% {
    scale: 1.1 0.92;
  }

  55% {
    scale: 0.95 1.05;
  }

  70% {
    scale: 1.03 0.98;
  }

  85% {
    scale: 0.99 1.01;
  }

  100% {
    scale: 1 1;
  }
}

.tab-09 {
  width: 100%;
  min-height: 100svh;
}

.tab-09 ::selection {
  background: var(--color-tab09-pink);
  color: #fff;
}
```
