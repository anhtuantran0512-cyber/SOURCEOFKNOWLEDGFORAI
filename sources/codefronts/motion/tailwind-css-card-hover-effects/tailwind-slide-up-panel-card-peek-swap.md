---
source: "codefronts"
url: "https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-slide-up-panel-card-peek-swap/"
title: "Tailwind Slide-Up Panel Card with Peek Header Swap"
section: "motion"
category: "tailwind-css-card-hover-effects"
category_name: "Tailwind CSS Card Hover Effects"
description: "The pattern at its plainest: a hero image with a small label that slides away as an opaque detail panel rises to replace it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Slide-Up Panel Card with Peek Header Swap
Source: https://codefronts.com/motion/tailwind-css-card-hover-effects/tailwind-slide-up-panel-card-peek-swap/

The pattern at its plainest: a hero image with a small label that slides away as an opaque detail panel rises to replace it. No zoom, no frost flourish &mdash; and that makes it the version to copy when the disclosure is the point.
## HTML
```html
<section class="tch-18 w-full min-h-svh grid place-items-center bg-tch18-bg font-tch18-sans p-8">
  <article class="group relative w-[330px] h-[440px] rounded-[20px] overflow-hidden cursor-pointer shadow-[0_18px_40px_rgb(0_0_0/0.2)]">
    <div class="absolute inset-0 bg-[linear-gradient(160deg,#ff6b4a,#c91f5f_60%,#5b1e6b)] after:content-[''] after:absolute after:inset-0 after:bg-[radial-gradient(circle_at_30%_25%,rgb(255_255_255/0.3),transparent_50%)]"></div>
    <div class="absolute inset-x-0 bottom-0 z-3 p-7 text-white transition-[translate,opacity] duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:-translate-y-32 group-hover:opacity-0 group-focus-within:-translate-y-32 group-focus-within:opacity-0 motion-reduce:transition-opacity">
      <span class="font-tch18-mono text-[0.7rem] tracking-[0.18em] uppercase opacity-85">Travel · 12 min</span>
      <h2 class="font-extrabold text-[1.9rem] leading-[1.05] mt-1">Sunset Over<br>Cartagena</h2>
    </div>
    <div class="absolute inset-x-0 bottom-0 z-4 p-7 bg-tch18-panel/95 backdrop-blur-[8px] text-tch18-ink translate-y-full transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:translate-y-0 group-focus-within:translate-y-0 motion-reduce:transition-none">
      <span class="font-tch18-mono text-[0.7rem] tracking-[0.18em] uppercase text-tch18-acc">Travel · 12 min read</span>
      <h3 class="font-extrabold text-[1.7rem] leading-[1.05] mt-1.5 mb-3">Sunset Over Cartagena</h3>
      <p class="text-[0.85rem] leading-[1.6] text-tch18-body">Walled-city rooftops, fruit carts at dusk, and where to find the best ceviche after dark.</p>
      <a href="#" class="inline-flex items-center min-h-11 mt-3 font-tch18-mono text-[0.78rem] tracking-[0.08em] text-tch18-acc no-underline rounded transition-colors duration-200 hover:text-white focus-visible:outline-2 focus-visible:outline-tch18-acc focus-visible:outline-offset-2">READ STORY →</a>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tch18-bg: #e8e4dd;
  --color-tch18-bg: oklch(0.92 0.008 85);
  --color-tch18-panel: #0c0810;
  --color-tch18-panel: oklch(0.12 0.015 300);
  --color-tch18-ink: #f0ece6;
  --color-tch18-ink: oklch(0.94 0.008 85);
  --color-tch18-body: #c4bdb4;
  --color-tch18-body: oklch(0.79 0.015 85);
  --color-tch18-acc: #ff8a6b;
  --color-tch18-acc: oklch(0.76 0.15 35);
  --font-tch18-sans: 'Sora', system-ui, sans-serif;
  --font-tch18-mono: 'JetBrains Mono', ui-monospace, monospace;
}

.tch-18 {
  width: 100%;
  min-height: 100svh;
}
```
