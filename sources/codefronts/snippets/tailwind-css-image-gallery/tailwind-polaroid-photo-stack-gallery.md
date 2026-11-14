---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-polaroid-photo-stack-gallery/"
title: "Tailwind Polaroid Photo Stack Gallery with Rotate-on-Hover"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Photographs styled as vintage Polaroid prints — thick white frame, deep bottom border, handwritten caption — tossed at casual angles and straightening with a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Polaroid Photo Stack Gallery with Rotate-on-Hover
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-polaroid-photo-stack-gallery/

Photographs styled as vintage Polaroid prints — thick white frame, deep bottom border, handwritten caption — tossed at casual angles and straightening with a lift as you reach for one. Each print's resting angle is a utility on the print, not an nth-child rule.
## HTML
```html
<section class="tgl-21 w-full min-h-svh grid place-items-center bg-tgl21-bg font-tgl21-sans px-5 py-10 bg-[radial-gradient(rgba(120,100,80,0.14)_1px,transparent_1px)] [background-size:6px_6px]" aria-label="Polaroid stack gallery">
  <div class="flex flex-wrap items-center justify-center gap-1.5 w-[min(820px,100%)]">
    <figure tabindex="0" class="relative m-0 w-[190px] p-3 pb-11 rounded-sm bg-tgl21-print rotate-[-6deg] shadow-[0_10px_24px_-10px_rgba(60,40,20,0.5)] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:rotate-0 hover:scale-[1.06] hover:z-[5] hover:shadow-[0_24px_44px_-16px_rgba(60,40,20,0.6)] focus-visible:rotate-0 focus-visible:scale-[1.06] focus-visible:z-[5] focus-visible:outline-3 focus-visible:outline-tgl21-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=400&h=400&auto=format&fit=crop" alt="Friends on a summer trip" loading="lazy" decoding="async" class="block w-full aspect-square object-cover bg-tgl21-well sepia-[0.18] contrast-[1.02]">
      <figcaption class="mt-3 text-center font-tgl21-hand text-[19px] text-tgl21-ink">Summer '24</figcaption>
    </figure>
    <figure tabindex="0" class="relative m-0 w-[190px] p-3 pb-11 rounded-sm bg-tgl21-print rotate-[4deg] shadow-[0_10px_24px_-10px_rgba(60,40,20,0.5)] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:rotate-0 hover:scale-[1.06] hover:z-[5] hover:shadow-[0_24px_44px_-16px_rgba(60,40,20,0.6)] focus-visible:rotate-0 focus-visible:scale-[1.06] focus-visible:z-[5] focus-visible:outline-3 focus-visible:outline-tgl21-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=400&h=400&auto=format&fit=crop" alt="Sunset on the beach" loading="lazy" decoding="async" class="block w-full aspect-square object-cover bg-tgl21-well sepia-[0.18] contrast-[1.02]">
      <figcaption class="mt-3 text-center font-tgl21-hand text-[19px] text-tgl21-ink">Last light</figcaption>
    </figure>
    <figure tabindex="0" class="relative m-0 w-[190px] p-3 pb-11 rounded-sm bg-tgl21-print rotate-[-3deg] shadow-[0_10px_24px_-10px_rgba(60,40,20,0.5)] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:rotate-0 hover:scale-[1.06] hover:z-[5] hover:shadow-[0_24px_44px_-16px_rgba(60,40,20,0.6)] focus-visible:rotate-0 focus-visible:scale-[1.06] focus-visible:z-[5] focus-visible:outline-3 focus-visible:outline-tgl21-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1499346030926-9a72daac6c63?q=80&w=400&h=400&auto=format&fit=crop" alt="Road trip stop at a filling station" loading="lazy" decoding="async" class="block w-full aspect-square object-cover bg-tgl21-well sepia-[0.18] contrast-[1.02]">
      <figcaption class="mt-3 text-center font-tgl21-hand text-[19px] text-tgl21-ink">Route 1</figcaption>
    </figure>
    <figure tabindex="0" class="relative m-0 w-[190px] p-3 pb-11 rounded-sm bg-tgl21-print rotate-[5deg] shadow-[0_10px_24px_-10px_rgba(60,40,20,0.5)] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:rotate-0 hover:scale-[1.06] hover:z-[5] hover:shadow-[0_24px_44px_-16px_rgba(60,40,20,0.6)] focus-visible:rotate-0 focus-visible:scale-[1.06] focus-visible:z-[5] focus-visible:outline-3 focus-visible:outline-tgl21-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1620121692029-d088224ddc74?q=80&w=400&h=400&auto=format&fit=crop" alt="Picnic in the park" loading="lazy" decoding="async" class="block w-full aspect-square object-cover bg-tgl21-well sepia-[0.18] contrast-[1.02]">
      <figcaption class="mt-3 text-center font-tgl21-hand text-[19px] text-tgl21-ink">Sunday</figcaption>
    </figure>
    <figure tabindex="0" class="relative m-0 w-[190px] p-3 pb-11 rounded-sm bg-tgl21-print rotate-[-5deg] shadow-[0_10px_24px_-10px_rgba(60,40,20,0.5)] transition-transform duration-[350ms] ease-[cubic-bezier(0.2,0.7,0.2,1)] hover:rotate-0 hover:scale-[1.06] hover:z-[5] hover:shadow-[0_24px_44px_-16px_rgba(60,40,20,0.6)] focus-visible:rotate-0 focus-visible:scale-[1.06] focus-visible:z-[5] focus-visible:outline-3 focus-visible:outline-tgl21-acc focus-visible:outline-offset-4 motion-reduce:transition-none">
      <img src="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=400&h=400&auto=format&fit=crop" alt="Mountain hike above the treeline" loading="lazy" decoding="async" class="block w-full aspect-square object-cover bg-tgl21-well sepia-[0.18] contrast-[1.02]">
      <figcaption class="mt-3 text-center font-tgl21-hand text-[19px] text-tgl21-ink">The climb</figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl21-bg: #d9cfc0;
  --color-tgl21-bg: oklch(0.85 0.02 80);
  --color-tgl21-print: #fffdf8;
  --color-tgl21-print: oklch(0.99 0.006 90);
  --color-tgl21-well: #e7e0d4;
  --color-tgl21-well: oklch(0.9 0.014 85);
  --color-tgl21-ink: #4a3c2c;
  --color-tgl21-ink: oklch(0.38 0.03 70);
  --color-tgl21-acc: #8a5a2c;
  --color-tgl21-acc: oklch(0.5 0.1 60);
  --font-tgl21-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-tgl21-hand: 'Caveat', 'Segoe Script', cursive;
}

.tgl-21 {
  width: 100%;
  min-height: 100svh;
}

.tgl-21 ::selection {
  background: var(--color-tgl21-acc);
  color: #fff;
}
```
