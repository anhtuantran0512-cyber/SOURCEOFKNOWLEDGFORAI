---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-corner-peel-card-clip-path/"
title: "Tailwind Corner Peel Card with clip-path Triangles"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "A sticker-style promo whose top-right corner peels back to expose a hidden subscriber discount, with a soft shadow under the lifted flap."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Corner Peel Card with clip-path Triangles
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-corner-peel-card-clip-path/

A sticker-style promo whose top-right corner peels back to expose a hidden subscriber discount, with a soft shadow under the lifted flap. clip-path has no utility and never should &mdash; the arbitrary [clip-path:polygon(…)] with underscore-escaped values is the idiomatic answer.
## HTML
```html
<section class="tch-12 w-full min-h-svh grid place-items-center bg-tch12-bg bg-[radial-gradient(circle_at_30%_20%,#e2f0eb,#b9d4cb)] font-tch12-sans p-8">
  <article tabindex="0" class="group relative w-[320px] h-[400px] rounded-[14px] overflow-hidden cursor-pointer outline-none bg-tch12-paper shadow-[0_14px_30px_rgb(40_70_60/0.18)] focus-visible:outline-3 focus-visible:outline-tch12-acc focus-visible:outline-offset-4">
    <div class="absolute top-0 right-0 z-3 size-0 grid place-items-center pointer-events-none bg-[linear-gradient(135deg,#1f5c4d,#2f8f76)] [clip-path:polygon(100%_0,0_0,100%_100%)] transition-[width,height] duration-450 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:size-[110px] group-focus-visible:size-[110px] motion-reduce:transition-none">
      <span class="absolute top-3.5 right-3.5 rotate-45 text-white font-bold text-[0.65rem] opacity-0 transition-opacity duration-300 delay-200 group-hover:opacity-100 group-focus-visible:opacity-100">-20%</span>
    </div>
    <div class="absolute top-0 right-0 z-4 size-0 pointer-events-none origin-top-right bg-[linear-gradient(135deg,#f7efe0,#e7dcc6)] [clip-path:polygon(100%_0,0_0,100%_100%)] transition-[width,height,box-shadow] duration-450 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:size-[110px] group-hover:shadow-[-6px_6px_14px_rgb(0_0_0/0.25)] group-focus-visible:size-[110px] motion-reduce:transition-none"></div>
    <div class="relative z-1 h-full p-[2.2rem] flex flex-col justify-between text-tch12-ink">
      <span class="self-start bg-tch12-tag text-white font-bold text-[0.7rem] tracking-[0.12em] uppercase px-3 py-1.5 rounded-full">Members Only</span>
      <h2 class="font-tch12-display text-[3rem] leading-[0.95] text-tch12-acc">Spring<br>Harvest Box</h2>
      <p class="text-[0.9rem] leading-[1.6] text-tch12-body">Peel the corner to uncover this week's hidden subscriber discount on farm-fresh produce.</p>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch12-bg: #cfe3dd;
  --color-tch12-bg: oklch(0.89 0.03 175);
  --color-tch12-paper: #fffdf7;
  --color-tch12-paper: oklch(0.99 0.008 95);
  --color-tch12-ink: #2a3d36;
  --color-tch12-ink: oklch(0.33 0.03 165);
  --color-tch12-body: #5a6e66;
  --color-tch12-body: oklch(0.5 0.025 165);
  --color-tch12-acc: #1f5c4d;
  --color-tch12-acc: oklch(0.42 0.07 168);
  --color-tch12-tag: #ff7a59;
  --color-tch12-tag: oklch(0.72 0.17 40);
  --font-tch12-sans: 'Nunito Sans', system-ui, sans-serif;
  --font-tch12-display: 'Caveat', cursive;
}

.tch-12 {
  width: 100%;
  min-height: 100svh;
}
```
