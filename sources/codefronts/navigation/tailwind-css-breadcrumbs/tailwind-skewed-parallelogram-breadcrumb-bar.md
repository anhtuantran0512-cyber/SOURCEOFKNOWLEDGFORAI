---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-skewed-parallelogram-breadcrumb-bar/"
title: "Tailwind Skewed Parallelogram Breadcrumb Bar"
section: "navigation"
category: "tailwind-css-breadcrumbs"
category_name: "Tailwind CSS Breadcrumbs"
description: "Angular parallelogram segments for sports, gaming and automotive UIs: each crumb is skewed &minus;20&deg; and its label counter-skewed back so the type stays…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Skewed Parallelogram Breadcrumb Bar
Source: https://codefronts.com/navigation/tailwind-css-breadcrumbs/tailwind-skewed-parallelogram-breadcrumb-bar/

Angular parallelogram segments for sports, gaming and automotive UIs: each crumb is skewed &minus;20&deg; and its label counter-skewed back so the type stays upright. Both transforms are real Tailwind utilities, which makes the pairing obvious instead of clever.
## HTML
```html
<section class="tbc-35 w-full min-h-svh flex items-center justify-center bg-tbc35-bg font-tbc35-sans px-8 py-8">
  <nav aria-label="Breadcrumb">
    <ol class="flex gap-1.25 list-none m-0 p-0">
      <li><a href="#" class="block overflow-hidden skew-x-[-20deg] bg-tbc35-step1 no-underline transition-colors duration-200 hover:bg-tbc35-hover focus-visible:outline-none focus-visible:[&amp;>span]:outline-2 focus-visible:[&amp;>span]:outline-white focus-visible:[&amp;>span]:-outline-offset-3 motion-reduce:transition-none"><span class="flex items-center h-10 px-5.5 skew-x-[20deg] text-[13px] font-bold uppercase tracking-[0.03em] text-tbc35-ink">Home</span></a></li>
      <li><a href="#" class="block overflow-hidden skew-x-[-20deg] bg-tbc35-step2 no-underline transition-colors duration-200 hover:bg-tbc35-hover focus-visible:outline-none focus-visible:[&amp;>span]:outline-2 focus-visible:[&amp;>span]:outline-white focus-visible:[&amp;>span]:-outline-offset-3 motion-reduce:transition-none"><span class="flex items-center h-10 px-5.5 skew-x-[20deg] text-[13px] font-bold uppercase tracking-[0.03em] text-tbc35-ink">Garage</span></a></li>
      <li><a href="#" class="block overflow-hidden skew-x-[-20deg] bg-tbc35-step3 no-underline transition-colors duration-200 hover:bg-tbc35-hover focus-visible:outline-none focus-visible:[&amp;>span]:outline-2 focus-visible:[&amp;>span]:outline-white focus-visible:[&amp;>span]:-outline-offset-3 motion-reduce:transition-none"><span class="flex items-center h-10 px-5.5 skew-x-[20deg] text-[13px] font-bold uppercase tracking-[0.03em] text-tbc35-ink">Models</span></a></li>
      <li><a href="#" aria-current="page" class="block overflow-hidden skew-x-[-20deg] bg-tbc35-current no-underline cursor-default focus-visible:outline-none focus-visible:[&amp;>span]:outline-2 focus-visible:[&amp;>span]:outline-white focus-visible:[&amp;>span]:-outline-offset-3"><span class="flex items-center h-10 px-5.5 skew-x-[20deg] text-[13px] font-bold uppercase tracking-[0.03em] text-white">GT-R Spec</span></a></li>
    </ol>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tbc35-bg: #21242b;
  --color-tbc35-bg: oklch(0.16 0.015 250);
  --color-tbc35-step1: #565d6b;
  --color-tbc35-step1: oklch(0.4 0.03 250);
  --color-tbc35-step2: #5d6579;
  --color-tbc35-step2: oklch(0.44 0.04 250);
  --color-tbc35-step3: #656f86;
  --color-tbc35-step3: oklch(0.48 0.05 250);
  --color-tbc35-hover: #74809c;
  --color-tbc35-hover: oklch(0.55 0.08 250);
  --color-tbc35-current: #b83f2c;
  --color-tbc35-current: oklch(0.55 0.19 25);
  --color-tbc35-ink: #e7e9ee;
  --color-tbc35-ink: oklch(0.92 0.01 250);
  --font-tbc35-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tbc-35 {
  width: 100%;
  min-height: 100svh;
}
```
