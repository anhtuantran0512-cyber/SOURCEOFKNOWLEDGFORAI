---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-background-slide-hover-button/"
title: "Tailwind Background Slide Hover Button (Four Directions)"
section: "motion"
category: "tailwind-css-animated-buttons"
category_name: "Tailwind CSS Animated Buttons"
description: "Four directional fills that sweep across the button face &mdash; left, right, top, bottom."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Background Slide Hover Button (Four Directions)
Source: https://codefronts.com/motion/tailwind-css-animated-buttons/tailwind-background-slide-hover-button/

Four directional fills that sweep across the button face &mdash; left, right, top, bottom. The port collapses eight CSS rules (four resting transforms, four hover transforms) into four class lists, each stating its own direction: before:-translate-x-full hover:before:translate-x-0.
## HTML
```html
<section class="tab-02 w-full min-h-svh grid place-items-center bg-tab02-bg font-tab02-sans px-6 py-10">
  <div class="flex flex-col items-center gap-8">
    <p class="text-[0.8rem] font-semibold tracking-[0.12em] uppercase text-tab02-fill/70 m-0">Background Slide Directions</p>
    <div class="grid grid-cols-2 gap-4">
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-tab02-fill bg-transparent border-2 border-tab02-fill rounded-lg cursor-pointer transition-colors duration-[350ms] before:content-[''] before:absolute before:inset-0 before:bg-tab02-fill before:-translate-x-full before:transition-transform before:duration-[350ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-white hover:before:translate-x-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab02-fill focus-visible:text-white focus-visible:before:translate-x-0 active:scale-[0.97] motion-reduce:before:transition-none motion-reduce:transition-none"><span class="relative z-10">Slide Left</span></button>
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-tab02-fill bg-transparent border-2 border-tab02-fill rounded-lg cursor-pointer transition-colors duration-[350ms] before:content-[''] before:absolute before:inset-0 before:bg-tab02-fill before:translate-x-full before:transition-transform before:duration-[350ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-white hover:before:translate-x-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab02-fill focus-visible:text-white focus-visible:before:translate-x-0 active:scale-[0.97] motion-reduce:before:transition-none motion-reduce:transition-none"><span class="relative z-10">Slide Right</span></button>
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-tab02-fill bg-transparent border-2 border-tab02-fill rounded-lg cursor-pointer transition-colors duration-[350ms] before:content-[''] before:absolute before:inset-0 before:bg-tab02-fill before:-translate-y-full before:transition-transform before:duration-[350ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-white hover:before:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab02-fill focus-visible:text-white focus-visible:before:translate-y-0 active:scale-[0.97] motion-reduce:before:transition-none motion-reduce:transition-none"><span class="relative z-10">Slide Top</span></button>
      <button type="button" class="relative overflow-hidden min-h-11 px-8 text-[0.95rem] font-bold tracking-[0.03em] text-tab02-fill bg-transparent border-2 border-tab02-fill rounded-lg cursor-pointer transition-colors duration-[350ms] before:content-[''] before:absolute before:inset-0 before:bg-tab02-fill before:translate-y-full before:transition-transform before:duration-[350ms] before:ease-[cubic-bezier(0.4,0,0.2,1)] hover:text-white hover:before:translate-y-0 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tab02-fill focus-visible:text-white focus-visible:before:translate-y-0 active:scale-[0.97] motion-reduce:before:transition-none motion-reduce:transition-none"><span class="relative z-10">Slide Bottom</span></button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tab02-bg: #f0eeff;
  --color-tab02-bg: oklch(0.95 0.02 282);
  --color-tab02-fill: #6c63ff;
  --color-tab02-fill: oklch(0.56 0.21 282);
  --font-tab02-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tab-02 {
  width: 100%;
  min-height: 100svh;
}

.tab-02 ::selection {
  background: var(--color-tab02-fill);
  color: #fff;
}
```
