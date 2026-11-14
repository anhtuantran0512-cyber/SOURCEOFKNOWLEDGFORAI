---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-portfolio-gallery-hover-caption-reveal/"
title: "Tailwind Portfolio Gallery Slider with Hover Caption Reveal"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "A case-study rail where each screenshot reveals its title and category on hover, sliding up from the bottom edge."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Portfolio Gallery Slider with Hover Caption Reveal
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-portfolio-gallery-hover-caption-reveal/

A case-study rail where each screenshot reveals its title and category on hover, sliding up from the bottom edge. Two transforms on two elements, both driven from one group on the link — and the caption is real text, so it is indexable as well as visible.
## HTML
```html
<section class="tcar-08 w-full min-h-svh grid place-items-center bg-tcar08-bg font-tcar08-sans px-3 py-10" aria-label="Selected work">
  <ul tabindex="0" role="group" aria-label="Portfolio projects, scrollable" class="list-none flex gap-[18px] w-[min(820px,100%)] overflow-x-auto p-3.5 m-0 snap-x snap-mandatory [scroll-padding:14px] [scrollbar-width:thin] [scrollbar-color:var(--color-tcar08-track)_transparent] focus-visible:outline-3 focus-visible:outline-tcar08-acc focus-visible:outline-offset-2 focus-visible:rounded-2xl">
    <li class="flex-none basis-[clamp(220px,72%,260px)] snap-start">
      <a href="#" class="group block relative rounded-2xl overflow-hidden no-underline bg-tcar08-card shadow-[0_20px_40px_-30px_oklch(0_0_0/0.9)] focus-visible:outline-3 focus-visible:outline-tcar08-acc focus-visible:outline-offset-2">
        <span class="block aspect-[4/5] overflow-hidden"><img src="https://picsum.photos/seed/work-1/640/800" width="640" height="800" decoding="async" alt="Fintech dashboard redesign" class="size-full object-cover block transition-[scale] duration-500 ease-out group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none motion-reduce:group-hover:scale-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-[18px] pt-11 pb-[18px] bg-[linear-gradient(transparent,oklch(0.14_0.01_265/0.92))] translate-y-full opacity-0 transition-[translate,opacity] duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
          <span class="inline-block text-[11px] tracking-[0.14em] uppercase text-tcar08-acc mb-1.5">Product</span><span class="block text-base font-bold text-white">Ledger &mdash; Fintech Dashboard</span>
        </span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(220px,72%,260px)] snap-start">
      <a href="#" class="group block relative rounded-2xl overflow-hidden no-underline bg-tcar08-card shadow-[0_20px_40px_-30px_oklch(0_0_0/0.9)] focus-visible:outline-3 focus-visible:outline-tcar08-acc focus-visible:outline-offset-2">
        <span class="block aspect-[4/5] overflow-hidden"><img src="https://picsum.photos/seed/work-2/640/800" width="640" height="800" loading="lazy" decoding="async" alt="Coffee brand identity" class="size-full object-cover block transition-[scale] duration-500 ease-out group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none motion-reduce:group-hover:scale-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-[18px] pt-11 pb-[18px] bg-[linear-gradient(transparent,oklch(0.14_0.01_265/0.92))] translate-y-full opacity-0 transition-[translate,opacity] duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
          <span class="inline-block text-[11px] tracking-[0.14em] uppercase text-tcar08-acc mb-1.5">Branding</span><span class="block text-base font-bold text-white">C&ugrave;rrent &mdash; Coffee Identity</span>
        </span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(220px,72%,260px)] snap-start">
      <a href="#" class="group block relative rounded-2xl overflow-hidden no-underline bg-tcar08-card shadow-[0_20px_40px_-30px_oklch(0_0_0/0.9)] focus-visible:outline-3 focus-visible:outline-tcar08-acc focus-visible:outline-offset-2">
        <span class="block aspect-[4/5] overflow-hidden"><img src="https://picsum.photos/seed/work-3/640/800" width="640" height="800" loading="lazy" decoding="async" alt="Travel app case study" class="size-full object-cover block transition-[scale] duration-500 ease-out group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none motion-reduce:group-hover:scale-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-[18px] pt-11 pb-[18px] bg-[linear-gradient(transparent,oklch(0.14_0.01_265/0.92))] translate-y-full opacity-0 transition-[translate,opacity] duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
          <span class="inline-block text-[11px] tracking-[0.14em] uppercase text-tcar08-acc mb-1.5">Mobile</span><span class="block text-base font-bold text-white">Wander &mdash; Travel App</span>
        </span>
      </a>
    </li>
    <li class="flex-none basis-[clamp(220px,72%,260px)] snap-start">
      <a href="#" class="group block relative rounded-2xl overflow-hidden no-underline bg-tcar08-card shadow-[0_20px_40px_-30px_oklch(0_0_0/0.9)] focus-visible:outline-3 focus-visible:outline-tcar08-acc focus-visible:outline-offset-2">
        <span class="block aspect-[4/5] overflow-hidden"><img src="https://picsum.photos/seed/work-4/640/800" width="640" height="800" loading="lazy" decoding="async" alt="E-commerce replatform" class="size-full object-cover block transition-[scale] duration-500 ease-out group-hover:scale-[1.07] group-focus-visible:scale-[1.07] motion-reduce:transition-none motion-reduce:group-hover:scale-100"></span>
        <span class="absolute inset-x-0 bottom-0 px-[18px] pt-11 pb-[18px] bg-[linear-gradient(transparent,oklch(0.14_0.01_265/0.92))] translate-y-full opacity-0 transition-[translate,opacity] duration-400 ease-[cubic-bezier(0.2,0.8,0.2,1)] group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:translate-y-0 group-focus-within:opacity-100 motion-reduce:transition-none motion-reduce:translate-y-0 motion-reduce:opacity-100">
          <span class="inline-block text-[11px] tracking-[0.14em] uppercase text-tcar08-acc mb-1.5">Web</span><span class="block text-base font-bold text-white">Maison &mdash; E-commerce</span>
        </span>
      </a>
    </li>
  </ul>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar08-bg: #111318;
  --color-tcar08-bg: oklch(0.19 0.008 265);
  --color-tcar08-card: #1a1d24;
  --color-tcar08-card: oklch(0.24 0.01 265);
  --color-tcar08-track: #333842;
  --color-tcar08-track: oklch(0.34 0.012 265);
  --color-tcar08-acc: #e6ff4d;
  --color-tcar08-acc: oklch(0.94 0.19 115);
  --font-tcar08-sans: 'Space Grotesk', system-ui, sans-serif;
}

.tcar-08 {
  width: 100%;
  min-height: 100svh;
}

.tcar-08 ::selection {
  background: var(--color-tcar08-acc);
  color: #111;
}

@media (prefers-reduced-motion: reduce) {
  .tcar-08 ul {
    scroll-behavior: auto;
  }
}
```
