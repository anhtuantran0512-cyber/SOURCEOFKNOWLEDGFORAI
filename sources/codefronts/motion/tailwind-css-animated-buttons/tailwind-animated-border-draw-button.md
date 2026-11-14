---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-border-draw-button/"
title: "Tailwind Animated Border Draw Button with Staged Delays"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "A border that draws itself around the perimeter on hover, two pseudo-elements sharing the work."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Animated Border Draw Button with Staged Delays
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-animated-border-draw-button/

A border that draws itself around the perimeter on hover, two pseudo-elements sharing the work. The port's real content is timing: before:delay-0, before:transition-[width,height] and a staggered after:delay-[400ms] put the whole four-stage cascade in the class list instead of a comment.
## HTML
```html
<section class="tab-04 w-full min-h-svh grid place-items-center bg-tab04-bg font-tab04-sans px-6 py-10">
  <div class="flex flex-col items-center gap-10">
    <p class="text-[0.78rem] tracking-[0.14em] uppercase text-tab04-indigo/70 m-0">Hover to draw the border</p>
    <div class="flex flex-wrap justify-center gap-5">
      <button type="button" class="relative min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-tab04-indigo bg-transparent cursor-pointer transition-[color,background-color] duration-[400ms] hover:text-white hover:bg-tab04-indigo/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab04-indigo before:content-[''] before:absolute before:top-0 before:left-0 before:size-0 before:border-t-2 before:border-r-2 before:border-tab04-indigo before:pointer-events-none before:transition-[width,height] before:duration-200 after:content-[''] after:absolute after:right-0 after:bottom-0 after:size-0 after:border-b-2 after:border-l-2 after:border-tab04-indigo after:pointer-events-none after:transition-[width,height] after:duration-200 after:delay-[400ms] hover:before:size-full hover:after:size-full motion-reduce:before:size-full motion-reduce:after:size-full motion-reduce:before:transition-none motion-reduce:after:transition-none"><span class="relative z-10">Explore Docs</span></button>
      <button type="button" class="relative min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-tab04-emerald bg-transparent cursor-pointer transition-[color,background-color] duration-[400ms] hover:text-white hover:bg-tab04-emerald/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab04-emerald before:content-[''] before:absolute before:top-0 before:left-0 before:size-0 before:border-t-2 before:border-r-2 before:border-tab04-emerald before:pointer-events-none before:transition-[width,height] before:duration-200 after:content-[''] after:absolute after:right-0 after:bottom-0 after:size-0 after:border-b-2 after:border-l-2 after:border-tab04-emerald after:pointer-events-none after:transition-[width,height] after:duration-200 after:delay-[400ms] hover:before:size-full hover:after:size-full motion-reduce:before:size-full motion-reduce:after:size-full motion-reduce:before:transition-none motion-reduce:after:transition-none"><span class="relative z-10">Start Building</span></button>
      <button type="button" class="relative min-h-11 px-9 text-[0.95rem] font-bold tracking-[0.04em] text-tab04-rose bg-transparent cursor-pointer transition-[color,background-color] duration-[400ms] hover:text-white hover:bg-tab04-rose/12 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab04-rose before:content-[''] before:absolute before:top-0 before:left-0 before:size-0 before:border-t-2 before:border-r-2 before:border-tab04-rose before:pointer-events-none before:transition-[width,height] before:duration-200 after:content-[''] after:absolute after:right-0 after:bottom-0 after:size-0 after:border-b-2 after:border-l-2 after:border-tab04-rose after:pointer-events-none after:transition-[width,height] after:duration-200 after:delay-[400ms] hover:before:size-full hover:after:size-full motion-reduce:before:size-full motion-reduce:after:size-full motion-reduce:before:transition-none motion-reduce:after:transition-none"><span class="relative z-10">Contact Sales</span></button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab04-bg: #09090f;
  --color-tab04-bg: oklch(0.1 0.01 275);
  --color-tab04-indigo: #818cf8;
  --color-tab04-indigo: oklch(0.7 0.14 279);
  --color-tab04-emerald: #34d399;
  --color-tab04-emerald: oklch(0.78 0.15 165);
  --color-tab04-rose: #fb7185;
  --color-tab04-rose: oklch(0.71 0.17 13);
  --font-tab04-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-04 {
  width: 100%;
  min-height: 100svh;
}

.tab-04 ::selection {
  background: var(--color-tab04-indigo);
  color: #0b0b12;
}
```
