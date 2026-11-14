---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-prismatic-light-sweep-card/"
title: "Tailwind Prismatic Light Sweep Card with Screen Blend Bar"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A soft rainbow bar travels diagonally across an optics-lab card, blurred and screen-blended so it reads as light refracting through coated glass."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Prismatic Light Sweep Card with Screen Blend Bar
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-prismatic-light-sweep-card/

A soft rainbow bar travels diagonally across an optics-lab card, blurred and screen-blended so it reads as light refracting through coated glass. The sweep is one rotated, blurred element animating a single left value &mdash; the simplest possible implementation of the most expensive-looking effect here.
## HTML
```html
<section class="tch-31 w-full min-h-svh grid place-items-center bg-tch31-bg font-tch31-sans p-8">
  <article tabindex="0" class="group relative w-[340px] h-[440px] rounded-[20px] overflow-hidden cursor-pointer outline-none bg-[linear-gradient(160deg,#14141f,#0a0a12)] border border-white/7 focus-visible:outline-2 focus-visible:outline-tch31-acc focus-visible:outline-offset-4">
    <div class="absolute -top-3/5 -left-[120%] w-3/5 h-[220%] z-1 pointer-events-none rotate-[22deg] blur-[8px] mix-blend-screen transition-[left] duration-700 ease-[cubic-bezier(0.4,0,0.2,1)] group-hover:left-[160%] group-focus-visible:left-[160%] motion-reduce:transition-none bg-[linear-gradient(90deg,transparent,rgb(255_0_128/0.5),rgb(255_200_0/0.5),rgb(0_255_170/0.5),rgb(0_170_255/0.5),rgb(180_80_255/0.5),transparent)]"></div>
    <div class="absolute inset-0 z-1 pointer-events-none bg-[repeating-linear-gradient(115deg,transparent_0_40px,rgb(255_255_255/0.015)_40px_41px)]"></div>
    <div class="relative z-2 h-full p-[2.4rem] flex flex-col justify-between text-tch31-ink">
      <span class="font-tch31-mono text-[0.72rem] tracking-[0.22em] uppercase text-tch31-mut">Optics Lab</span>
      <h2 class="font-extrabold text-[2.5rem] leading-none">Refraction<br>No. 9</h2>
      <p class="text-[0.86rem] leading-[1.6] text-tch31-body">A coated-glass installation. Light enters white and leaves as a spectrum sweeping the wall.</p>
      <div class="flex gap-6 font-tch31-mono text-[0.74rem] text-tch31-mut">
        <span><b class="block text-[1.1rem] text-tch31-ink">540nm</b>peak</span>
        <span><b class="block text-[1.1rem] text-tch31-ink">1.52</b>index</span>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch31-bg: #06060c;
  --color-tch31-bg: oklch(0.09 0.008 285);
  --color-tch31-ink: #eef0f7;
  --color-tch31-ink: oklch(0.95 0.005 275);
  --color-tch31-body: #a3a7bd;
  --color-tch31-body: oklch(0.72 0.02 280);
  --color-tch31-mut: #8b8fa6;
  --color-tch31-mut: oklch(0.63 0.02 280);
  --color-tch31-acc: #6ad6ff;
  --color-tch31-acc: oklch(0.83 0.12 225);
  --font-tch31-sans: 'Sora', system-ui, sans-serif;
  --font-tch31-mono: 'Geist Mono', ui-monospace, monospace;
}

.tch-31 {
  width: 100%;
  min-height: 100svh;
}
```
