---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-accordion-image-gallery-flex-grow/"
title: "Tailwind Accordion Image Gallery with Flex-Grow on Hover & Focus"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "A compact row of vertical image strips that expand on hover or keyboard focus while their neighbours shrink."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion Image Gallery with Flex-Grow on Hover & Focus
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-accordion-image-gallery-flex-grow/

A compact row of vertical image strips that expand on hover or keyboard focus while their neighbours shrink. Every panel is a real <button>, so the accordion opens on focus exactly as it does on hover — the port states both on the same element, one class apart.
## HTML
```html
<section class="tgl-12 w-full min-h-svh grid place-items-center bg-tgl12-bg font-tgl12-sans px-5 py-10" aria-label="Accordion image gallery">
  <div class="flex gap-2 w-[min(880px,100%)] h-[min(440px,60vh)]">
    <button type="button" style="--img:url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?q=80&w=700&h=900&auto=format&fit=crop')" class="group relative flex-1 min-w-0 p-0 border-0 cursor-pointer rounded-xl overflow-hidden bg-[image:var(--img)] bg-cover bg-center brightness-[0.72] saturate-[0.95] transition-[flex-grow,filter] duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:grow-[4] hover:brightness-100 hover:saturate-[1.05] focus:grow-[4] focus:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl12-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,rgba(10,6,4,0.7),transparent_55%)]"></span>
      <span class="absolute right-3 top-4 z-[2] text-white text-[15px] font-bold tracking-[0.06em] [writing-mode:vertical-rl] rotate-180 [text-shadow:0_1px_4px_rgba(0,0,0,0.7)] transition-all duration-300 group-hover:[writing-mode:horizontal-tb] group-hover:rotate-0 group-hover:inset-x-0 group-hover:top-auto group-hover:bottom-4 group-hover:text-lg group-focus:[writing-mode:horizontal-tb] group-focus:rotate-0 group-focus:inset-x-0 group-focus:top-auto group-focus:bottom-4 group-focus:text-lg">Peaks</span>
    </button>
    <button type="button" style="--img:url('https://images.unsplash.com/photo-1522199755839-a2bacb67c546?q=80&w=700&h=900&auto=format&fit=crop')" class="group relative flex-1 min-w-0 p-0 border-0 cursor-pointer rounded-xl overflow-hidden bg-[image:var(--img)] bg-cover bg-center brightness-[0.72] saturate-[0.95] transition-[flex-grow,filter] duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:grow-[4] hover:brightness-100 hover:saturate-[1.05] focus:grow-[4] focus:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl12-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,rgba(10,6,4,0.7),transparent_55%)]"></span>
      <span class="absolute right-3 top-4 z-[2] text-white text-[15px] font-bold tracking-[0.06em] [writing-mode:vertical-rl] rotate-180 [text-shadow:0_1px_4px_rgba(0,0,0,0.7)] transition-all duration-300 group-hover:[writing-mode:horizontal-tb] group-hover:rotate-0 group-hover:inset-x-0 group-hover:top-auto group-hover:bottom-4 group-hover:text-lg group-focus:[writing-mode:horizontal-tb] group-focus:rotate-0 group-focus:inset-x-0 group-focus:top-auto group-focus:bottom-4 group-focus:text-lg">Forests</span>
    </button>
    <button type="button" style="--img:url('https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?q=80&w=700&h=900&auto=format&fit=crop')" class="group relative flex-1 min-w-0 p-0 border-0 cursor-pointer rounded-xl overflow-hidden bg-[image:var(--img)] bg-cover bg-center brightness-[0.72] saturate-[0.95] transition-[flex-grow,filter] duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:grow-[4] hover:brightness-100 hover:saturate-[1.05] focus:grow-[4] focus:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl12-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,rgba(10,6,4,0.7),transparent_55%)]"></span>
      <span class="absolute right-3 top-4 z-[2] text-white text-[15px] font-bold tracking-[0.06em] [writing-mode:vertical-rl] rotate-180 [text-shadow:0_1px_4px_rgba(0,0,0,0.7)] transition-all duration-300 group-hover:[writing-mode:horizontal-tb] group-hover:rotate-0 group-hover:inset-x-0 group-hover:top-auto group-hover:bottom-4 group-hover:text-lg group-focus:[writing-mode:horizontal-tb] group-focus:rotate-0 group-focus:inset-x-0 group-focus:top-auto group-focus:bottom-4 group-focus:text-lg">Coast</span>
    </button>
    <button type="button" style="--img:url('https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=700&h=900&auto=format&fit=crop')" class="group relative flex-1 min-w-0 p-0 border-0 cursor-pointer rounded-xl overflow-hidden bg-[image:var(--img)] bg-cover bg-center brightness-[0.72] saturate-[0.95] transition-[flex-grow,filter] duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:grow-[4] hover:brightness-100 hover:saturate-[1.05] focus:grow-[4] focus:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl12-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,rgba(10,6,4,0.7),transparent_55%)]"></span>
      <span class="absolute right-3 top-4 z-[2] text-white text-[15px] font-bold tracking-[0.06em] [writing-mode:vertical-rl] rotate-180 [text-shadow:0_1px_4px_rgba(0,0,0,0.7)] transition-all duration-300 group-hover:[writing-mode:horizontal-tb] group-hover:rotate-0 group-hover:inset-x-0 group-hover:top-auto group-hover:bottom-4 group-hover:text-lg group-focus:[writing-mode:horizontal-tb] group-focus:rotate-0 group-focus:inset-x-0 group-focus:top-auto group-focus:bottom-4 group-focus:text-lg">Desert</span>
    </button>
    <button type="button" style="--img:url('https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=700&h=900&auto=format&fit=crop')" class="group relative flex-1 min-w-0 p-0 border-0 cursor-pointer rounded-xl overflow-hidden bg-[image:var(--img)] bg-cover bg-center brightness-[0.72] saturate-[0.95] transition-[flex-grow,filter] duration-500 ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:grow-[4] hover:brightness-100 hover:saturate-[1.05] focus:grow-[4] focus:brightness-100 focus-visible:outline-3 focus-visible:outline-tgl12-acc focus-visible:-outline-offset-[3px] motion-reduce:transition-none">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(0deg,rgba(10,6,4,0.7),transparent_55%)]"></span>
      <span class="absolute right-3 top-4 z-[2] text-white text-[15px] font-bold tracking-[0.06em] [writing-mode:vertical-rl] rotate-180 [text-shadow:0_1px_4px_rgba(0,0,0,0.7)] transition-all duration-300 group-hover:[writing-mode:horizontal-tb] group-hover:rotate-0 group-hover:inset-x-0 group-hover:top-auto group-hover:bottom-4 group-hover:text-lg group-focus:[writing-mode:horizontal-tb] group-focus:rotate-0 group-focus:inset-x-0 group-focus:top-auto group-focus:bottom-4 group-focus:text-lg">Cities</span>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl12-bg: #14110f;
  --color-tgl12-bg: oklch(0.17 0.008 50);
  --color-tgl12-acc: #e2683f;
  --color-tgl12-acc: oklch(0.66 0.17 35);
  --font-tgl12-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-12 {
  width: 100%;
  min-height: 100svh;
}

.tgl-12 ::selection {
  background: var(--color-tgl12-acc);
  color: #fff;
}
```
