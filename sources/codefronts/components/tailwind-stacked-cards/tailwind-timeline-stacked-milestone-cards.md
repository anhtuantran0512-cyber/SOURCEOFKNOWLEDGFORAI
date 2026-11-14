---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-stacked-cards/tailwind-timeline-stacked-milestone-cards/"
title: "Tailwind Timeline Stacked Milestone Cards"
section: "components"
category: "tailwind-stacked-cards"
category_name: "Tailwind Stacked Cards"
description: "A gradient-spine timeline whose cards slide right and whose nodes bloom on hover."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Timeline Stacked Milestone Cards
Source: https://codefronts.com/components/tailwind-stacked-cards/tailwind-timeline-stacked-milestone-cards/

A gradient-spine timeline whose cards slide right and whose nodes bloom on hover. The port's contribution is semantic rather than visual: the div soup becomes a real <ol> with <time datetime> elements, and both the spine and the milestone nodes become before: utilities on the elements they belong to instead of two floating pseudo-element rules.
## HTML
```html
<section class="stk-35 grid w-full min-h-svh place-items-center px-5 py-15 font-stk35-sans bg-linear-[180deg,var(--color-stk35-p1),var(--color-stk35-p2)]" aria-label="Company timeline">
  <ol class="relative m-0 w-[min(340px,92vw)] list-none pl-10 before:absolute before:inset-y-2.5 before:left-3.5 before:w-[3px] before:rounded before:bg-linear-[180deg,var(--color-stk35-spine1),var(--color-stk35-spine2)]">
    <li class="group relative mb-3.5 before:absolute before:-left-[33px] before:top-4.5 before:size-4 before:rounded-full before:border-[3px] before:border-stk35-spine1 before:bg-white before:transition-[transform,background-color] before:duration-350 hover:before:scale-130 hover:before:bg-stk35-accent motion-reduce:before:transition-none">
      <div class="cursor-pointer rounded-[14px] bg-white px-5 py-4 shadow-[0_8px_20px_rgba(120,60,80,0.12)] transition-[transform,box-shadow] duration-350 ease-stk35 group-hover:translate-x-3 group-hover:shadow-[0_14px_30px_rgba(120,60,80,0.2)] motion-reduce:transition-none motion-reduce:translate-none!">
        <time class="font-stk35-display text-[0.8rem] tracking-[0.08em] text-stk35-accent" datetime="2021-03">2021</time>
        <h3 class="m-0 mt-0.5 mb-1 font-stk35-display text-[1.1rem] text-stk35-ink">The Beginning</h3>
        <p class="m-0 text-[0.85rem] text-stk35-body">First prototype shipped to ten beta users.</p>
      </div>
    </li>
    <li class="group relative mb-3.5 before:absolute before:-left-[33px] before:top-4.5 before:size-4 before:rounded-full before:border-[3px] before:border-stk35-spine1 before:bg-white before:transition-[transform,background-color] before:duration-350 hover:before:scale-130 hover:before:bg-stk35-accent motion-reduce:before:transition-none">
      <div class="cursor-pointer rounded-[14px] bg-white px-5 py-4 shadow-[0_8px_20px_rgba(120,60,80,0.12)] transition-[transform,box-shadow] duration-350 ease-stk35 group-hover:translate-x-3 group-hover:shadow-[0_14px_30px_rgba(120,60,80,0.2)] motion-reduce:transition-none motion-reduce:translate-none!">
        <time class="font-stk35-display text-[0.8rem] tracking-[0.08em] text-stk35-accent" datetime="2023-06">2023</time>
        <h3 class="m-0 mt-0.5 mb-1 font-stk35-display text-[1.1rem] text-stk35-ink">Going Public</h3>
        <p class="m-0 text-[0.85rem] text-stk35-body">Launched the open platform to everyone.</p>
      </div>
    </li>
    <li class="group relative mb-3.5 before:absolute before:-left-[33px] before:top-4.5 before:size-4 before:rounded-full before:border-[3px] before:border-stk35-spine1 before:bg-white before:transition-[transform,background-color] before:duration-350 hover:before:scale-130 hover:before:bg-stk35-accent motion-reduce:before:transition-none">
      <div class="cursor-pointer rounded-[14px] bg-white px-5 py-4 shadow-[0_8px_20px_rgba(120,60,80,0.12)] transition-[transform,box-shadow] duration-350 ease-stk35 group-hover:translate-x-3 group-hover:shadow-[0_14px_30px_rgba(120,60,80,0.2)] motion-reduce:transition-none motion-reduce:translate-none!">
        <time class="font-stk35-display text-[0.8rem] tracking-[0.08em] text-stk35-accent" datetime="2025-01">2025</time>
        <h3 class="m-0 mt-0.5 mb-1 font-stk35-display text-[1.1rem] text-stk35-ink">Scale</h3>
        <p class="m-0 text-[0.85rem] text-stk35-body">Crossed one million active accounts.</p>
      </div>
    </li>
    <li class="group relative before:absolute before:-left-[33px] before:top-4.5 before:size-4 before:rounded-full before:border-[3px] before:border-stk35-spine2 before:bg-white before:transition-[transform,background-color] before:duration-350 hover:before:scale-130 hover:before:bg-stk35-accent motion-reduce:before:transition-none">
      <div class="cursor-pointer rounded-[14px] bg-white px-5 py-4 shadow-[0_8px_20px_rgba(120,60,80,0.12)] transition-[transform,box-shadow] duration-350 ease-stk35 group-hover:translate-x-3 group-hover:shadow-[0_14px_30px_rgba(120,60,80,0.2)] motion-reduce:transition-none motion-reduce:translate-none!">
        <time class="font-stk35-display text-[0.8rem] tracking-[0.08em] text-stk35-accent" datetime="2026-09">2026</time>
        <h3 class="m-0 mt-0.5 mb-1 font-stk35-display text-[1.1rem] text-stk35-ink">What&rsquo;s Next</h3>
        <p class="m-0 text-[0.85rem] text-stk35-body">Reimagining the experience from scratch.</p>
      </div>
    </li>
  </ol>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-stk35-p1: #fffaf0;
  --color-stk35-p1: oklch(0.98 0.014 90);
  --color-stk35-p2: #f0e8dc;
  --color-stk35-p2: oklch(0.93 0.016 80);
  --color-stk35-spine1: #ff8a5c;
  --color-stk35-spine1: oklch(0.74 0.145 45);
  --color-stk35-spine2: #a83279;
  --color-stk35-spine2: oklch(0.47 0.170 350);
  --color-stk35-accent: #a83279;
  --color-stk35-accent: oklch(0.47 0.170 350);
  --color-stk35-ink: #2a2024;
  --color-stk35-ink: oklch(0.26 0.014 20);
  --color-stk35-body: #6a5a60;
  --color-stk35-body: oklch(0.50 0.018 10);
  --font-stk35-sans: 'Schibsted Grotesk', system-ui, sans-serif;
  --font-stk35-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --ease-stk35: cubic-bezier(0.3, 0.9, 0.3, 1);
}
```
