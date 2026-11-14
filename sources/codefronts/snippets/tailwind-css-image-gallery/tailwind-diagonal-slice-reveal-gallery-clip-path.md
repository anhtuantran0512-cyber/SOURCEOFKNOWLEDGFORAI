---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-diagonal-slice-reveal-gallery-clip-path/"
title: "Tailwind Diagonal Slice Reveal Gallery with clip-path Halves"
section: "snippets"
category: "tailwind-css-image-gallery"
category_name: "Tailwind CSS Image Gallery"
description: "Tiles split by a sharp diagonal; on hover the two angled halves slide apart along the cut to reveal the photograph beneath."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Diagonal Slice Reveal Gallery with clip-path Halves
Source: https://codefronts.com/snippets/tailwind-css-image-gallery/tailwind-diagonal-slice-reveal-gallery-clip-path/

Tiles split by a sharp diagonal; on hover the two angled halves slide apart along the cut to reveal the photograph beneath. Two arbitrary clip-path values and two opposite translates — the whole effect, declared on the two elements that move.
## HTML
```html
<section class="tgl-15 w-full min-h-svh grid place-items-center bg-tgl15-bg font-tgl15-sans px-5 py-10" aria-label="Diagonal slice reveal gallery">
  <div class="flex flex-wrap justify-center gap-5 w-[min(880px,100%)]">
    <a href="#" class="group relative block w-[260px] aspect-square rounded-[14px] overflow-hidden no-underline bg-tgl15-well focus-visible:outline-3 focus-visible:outline-tgl15-acc focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1511818966892-d7d671e672a2?q=80&w=500&h=500&auto=format&fit=crop" alt="Snowy mountain range" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c1),oklch(0.32_0.1_285))] [clip-path:polygon(0_0,100%_0,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(-101%,-101%)] group-focus-visible:[transform:translate(-101%,-101%)] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c2),oklch(0.38_0.12_330))] [clip-path:polygon(100%_0,100%_100%,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(101%,101%)] group-focus-visible:[transform:translate(101%,101%)] motion-reduce:transition-none"></span>
      <span class="absolute inset-0 z-[2] grid place-items-center text-white text-xl font-extrabold tracking-[0.08em] uppercase pointer-events-none transition-opacity duration-300 group-hover:opacity-0 group-focus-visible:opacity-0 motion-reduce:transition-none">Alps</span>
    </a>
    <a href="#" class="group relative block w-[260px] aspect-square rounded-[14px] overflow-hidden no-underline bg-tgl15-well focus-visible:outline-3 focus-visible:outline-tgl15-acc focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1444723121867-7a241cacace9?q=80&w=500&h=500&auto=format&fit=crop" alt="Desert dunes at midday" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c1),oklch(0.32_0.1_285))] [clip-path:polygon(0_0,100%_0,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(-101%,-101%)] group-focus-visible:[transform:translate(-101%,-101%)] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c2),oklch(0.38_0.12_330))] [clip-path:polygon(100%_0,100%_100%,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(101%,101%)] group-focus-visible:[transform:translate(101%,101%)] motion-reduce:transition-none"></span>
      <span class="absolute inset-0 z-[2] grid place-items-center text-white text-xl font-extrabold tracking-[0.08em] uppercase pointer-events-none transition-opacity duration-300 group-hover:opacity-0 group-focus-visible:opacity-0 motion-reduce:transition-none">Sahara</span>
    </a>
    <a href="#" class="group relative block w-[260px] aspect-square rounded-[14px] overflow-hidden no-underline bg-tgl15-well focus-visible:outline-3 focus-visible:outline-tgl15-acc focus-visible:outline-offset-[3px]">
      <img src="https://images.unsplash.com/photo-1599566150163-29194dcaad36?q=80&w=500&h=500&auto=format&fit=crop" alt="Coral reef underwater" loading="lazy" decoding="async" class="absolute inset-0 w-full h-full object-cover">
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c1),oklch(0.32_0.1_285))] [clip-path:polygon(0_0,100%_0,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(-101%,-101%)] group-focus-visible:[transform:translate(-101%,-101%)] motion-reduce:transition-none"></span>
      <span aria-hidden="true" class="absolute inset-0 bg-[linear-gradient(135deg,var(--color-tgl15-c2),oklch(0.38_0.12_330))] [clip-path:polygon(100%_0,100%_100%,0_100%)] transition-transform duration-500 ease-[cubic-bezier(0.5,0,0.2,1)] group-hover:[transform:translate(101%,101%)] group-focus-visible:[transform:translate(101%,101%)] motion-reduce:transition-none"></span>
      <span class="absolute inset-0 z-[2] grid place-items-center text-white text-xl font-extrabold tracking-[0.08em] uppercase pointer-events-none transition-opacity duration-300 group-hover:opacity-0 group-focus-visible:opacity-0 motion-reduce:transition-none">Reef</span>
    </a>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgl15-bg: #0e0c14;
  --color-tgl15-bg: oklch(0.14 0.015 300);
  --color-tgl15-well: #1a1622;
  --color-tgl15-well: oklch(0.21 0.02 300);
  --color-tgl15-c1: #6a4fd0;
  --color-tgl15-c1: oklch(0.5 0.17 285);
  --color-tgl15-c2: #d054b0;
  --color-tgl15-c2: oklch(0.62 0.19 330);
  --color-tgl15-acc: #b558e0;
  --color-tgl15-acc: oklch(0.65 0.19 305);
  --font-tgl15-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tgl-15 {
  width: 100%;
  min-height: 100svh;
}

.tgl-15 ::selection {
  background: var(--color-tgl15-acc);
  color: #fff;
}
```
