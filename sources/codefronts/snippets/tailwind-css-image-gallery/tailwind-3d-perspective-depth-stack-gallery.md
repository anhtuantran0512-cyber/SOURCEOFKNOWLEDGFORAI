---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-perspective-depth-stack-gallery/"
title: "Tailwind 3D Perspective Depth Stack Gallery That Fans on Focus"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A deck of photographs stacked in 3D that fans into a cascade when you hover or focus it."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind 3D Perspective Depth Stack Gallery That Fans on Focus
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-3d-perspective-depth-stack-gallery/

A deck of photographs stacked in 3D that fans into a cascade when you hover or focus it. Each card's resting depth and fanned position are two utilities on the card itself, which replaces four nth-child rules with markup you can reorder freely.
## HTML
```html
<section class="tgl-18 w-full min-h-svh flex flex-col items-center justify-center gap-7 bg-tgl18-bg font-tgl18-sans px-5 py-10" aria-label="Perspective depth stack gallery">
  <div class="group relative w-[260px] h-[330px] [perspective:1200px]">
    <a href="#" class="absolute inset-0 rounded-2xl overflow-hidden transform-3d origin-bottom shadow-[0_20px_40px_-20px_rgba(0,0,0,0.7)] [transform:translateZ(60px)] transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:[transform:translateX(-150px)_rotate(-9deg)] group-focus-within:[transform:translateX(-150px)_rotate(-9deg)] focus-visible:outline-3 focus-visible:outline-tgl18-acc focus-visible:outline-offset-[3px] focus-visible:z-[5] motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1607746882042-944635dfe10e?q=80&w=500&h=620&auto=format&fit=crop" alt="Studio portrait in high contrast" loading="lazy" decoding="async" class="block w-full h-full object-cover">
    </a>
    <a href="#" class="absolute inset-0 rounded-2xl overflow-hidden transform-3d origin-bottom shadow-[0_20px_40px_-20px_rgba(0,0,0,0.7)] [transform:translateZ(40px)_translateY(10px)_scale(0.97)] transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:[transform:translateX(-50px)_rotate(-3deg)] group-focus-within:[transform:translateX(-50px)_rotate(-3deg)] focus-visible:outline-3 focus-visible:outline-tgl18-acc focus-visible:outline-offset-[3px] focus-visible:z-[5] motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1505691938895-1758d7feb511?q=80&w=500&h=620&auto=format&fit=crop" alt="Minimal landscape study" loading="lazy" decoding="async" class="block w-full h-full object-cover">
    </a>
    <a href="#" class="absolute inset-0 rounded-2xl overflow-hidden transform-3d origin-bottom shadow-[0_20px_40px_-20px_rgba(0,0,0,0.7)] [transform:translateZ(20px)_translateY(20px)_scale(0.94)] transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:[transform:translateX(50px)_rotate(3deg)] group-focus-within:[transform:translateX(50px)_rotate(3deg)] focus-visible:outline-3 focus-visible:outline-tgl18-acc focus-visible:outline-offset-[3px] focus-visible:z-[5] motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=500&h=620&auto=format&fit=crop" alt="Street scene in late light" loading="lazy" decoding="async" class="block w-full h-full object-cover">
    </a>
    <a href="#" class="absolute inset-0 rounded-2xl overflow-hidden transform-3d origin-bottom shadow-[0_20px_40px_-20px_rgba(0,0,0,0.7)] [transform:translateZ(0)_translateY(30px)_scale(0.91)] transition-transform duration-[550ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] group-hover:[transform:translateX(150px)_rotate(9deg)] group-focus-within:[transform:translateX(150px)_rotate(9deg)] focus-visible:outline-3 focus-visible:outline-tgl18-acc focus-visible:outline-offset-[3px] focus-visible:z-[5] motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?q=80&w=500&h=620&auto=format&fit=crop" alt="Botanical detail on black" loading="lazy" decoding="async" class="block w-full h-full object-cover">
    </a>
  </div>
  <p class="font-tgl18-mono text-[11px] tracking-[0.16em] uppercase text-tgl18-mut m-0">hover or focus the stack to fan it out</p>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl18-bg: #14101a;
  --color-tgl18-bg: oklch(0.18 0.018 310);
  --color-tgl18-mut: #a396ad;
  --color-tgl18-mut: oklch(0.72 0.02 315);
  --color-tgl18-acc: #d06fc8;
  --color-tgl18-acc: oklch(0.7 0.17 330);
  --font-tgl18-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl18-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}

.tgl-18 {
  width: 100%;
  min-height: 100svh;
}

.tgl-18 ::selection {
  background: var(--color-tgl18-acc);
  color: #fff;
}
```
