---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-has-hover-spotlight-image-grid/"
title: "Tailwind :has() Hover Spotlight Image Grid"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Hover any card and every other card in the grid dims and desaturates, spotlighting the one you are on."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind :has() Hover Spotlight Image Grid
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-has-hover-spotlight-image-grid/

Hover any card and every other card in the grid dims and desaturates, spotlighting the one you are on. The behaviour that used to need a JavaScript mouseenter loop is one relational selector — and in Tailwind it is one arbitrary variant, declared on the grid that owns the relationship.
## HTML
```html
<section class="tgl-04 w-full min-h-svh grid place-items-center bg-tgl04-bg font-tgl04-sans px-5 py-10" aria-label="Spotlight hover gallery">
  <div class="w-[min(760px,100%)] grid grid-cols-4 gap-3 max-[560px]:grid-cols-2 [&:has(a:hover)>a:not(:hover)]:opacity-40 [&:has(a:hover)>a:not(:hover)]:saturate-[0.35] [&:has(a:hover)>a:not(:hover)]:brightness-[0.7] [&:has(a:focus-visible)>a:not(:focus-visible)]:opacity-40 [&:has(a:focus-visible)>a:not(:focus-visible)]:saturate-[0.35] [&:has(a:focus-visible)>a:not(:focus-visible)]:brightness-[0.7]">
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?q=80&w=400&h=400&auto=format&fit=crop" alt="Neon-lit Tokyo street" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Tokyo</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=400&h=400&auto=format&fit=crop" alt="Paris rooftops at dusk" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Paris</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1467003909585-2f8a72700288?q=80&w=400&h=400&auto=format&fit=crop" alt="New York skyline" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">New York</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=400&h=400&auto=format&fit=crop" alt="London bridge over the Thames" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">London</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?q=80&w=400&h=400&auto=format&fit=crop" alt="Sydney harbour" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Sydney</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1595152452543-e5fc28ebc2b8?q=80&w=400&h=400&auto=format&fit=crop" alt="Roman architecture" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Rome</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?q=80&w=400&h=400&auto=format&fit=crop" alt="Dubai towers" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Dubai</span>
    </a>
    <a href="#" class="relative block rounded-xl overflow-hidden bg-tgl04-cell no-underline transition-[transform,opacity,filter] duration-[400ms] hover:scale-[1.06] hover:z-[2] hover:shadow-[0_20px_40px_-18px_rgba(0,0,0,0.7)] focus-visible:scale-[1.06] focus-visible:z-[2] focus-visible:outline-3 focus-visible:outline-tgl04-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-visible:scale-100">
      <img src="https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?q=80&w=400&h=400&auto=format&fit=crop" alt="Cairo skyline" loading="lazy" decoding="async" class="block w-full aspect-square object-cover">
      <span class="absolute inset-x-0 bottom-0 px-2.5 pt-5 pb-2 text-white text-xs font-bold tracking-[0.03em] bg-[linear-gradient(0deg,rgba(0,0,0,0.8),transparent)]">Cairo</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl04-bg: #0f1013;
  --color-tgl04-bg: oklch(0.16 0.006 265);
  --color-tgl04-cell: #1a1c20;
  --color-tgl04-cell: oklch(0.23 0.008 265);
  --color-tgl04-acc: #f0a63a;
  --color-tgl04-acc: oklch(0.78 0.15 65);
  --font-tgl04-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-04 {
  width: 100%;
  min-height: 100svh;
}

.tgl-04 ::selection {
  background: var(--color-tgl04-acc);
  color: #111;
}
```
