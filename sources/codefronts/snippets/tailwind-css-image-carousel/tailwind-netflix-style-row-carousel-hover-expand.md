---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-netflix-style-row-carousel-hover-expand/"
title: "Tailwind Netflix-Style Content Row Carousel with Hover Expand"
section: "snippets"
category: "tailwind-css-image-carousel"
category_name: "Tailwind CSS Image Carousel"
description: "The canonical streaming content row: 16:9 title cards that scale up and reveal metadata on hover, side arrows that appear on row-hover, and edge-fade…"
has_js: "true"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Netflix-Style Content Row Carousel with Hover Expand
Source: https://codefronts.com/snippets/tailwind-css-image-carousel/tailwind-netflix-style-row-carousel-hover-expand/

The canonical streaming content row: 16:9 title cards that scale up and reveal metadata on hover, side arrows that appear on row-hover, and edge-fade gradients hinting at off-screen titles. Five lines of JS page the row; everything else is utilities.
## HTML
```html
<section class="tcar-09 w-full min-h-svh flex flex-col justify-center bg-tcar09-bg font-tcar09-sans py-10 [--tile-w:clamp(220px,28vw,300px)] max-sm:[--tile-w:clamp(180px,60vw,240px)]" aria-label="Trending now">
  <h3 class="text-tcar09-ink text-xl font-extrabold tracking-[-0.02em] mb-3.5 px-[clamp(16px,5vw,48px)]">Trending now</h3>
  <div class="group/wrap relative">
    <button type="button" data-dir="-1" aria-label="Scroll row left" class="absolute left-0 top-[15px] z-[4] w-10 h-[calc(100%-30px)] max-sm:hidden flex items-center justify-center border-0 p-0 cursor-pointer bg-tcar09-navbg text-white opacity-0 transition-[opacity,background-color] duration-200 group-hover/wrap:opacity-100 group-focus-within/wrap:opacity-100 hover:bg-tcar09-navbghover focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:-outline-offset-4">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M15 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
    <div class="[mask-image:linear-gradient(90deg,transparent,#000_4%,#000_96%,transparent)]">
      <ul tabindex="0" role="group" aria-label="Trending titles, scrollable" class="tcar09-row list-none flex gap-1.5 overflow-x-auto py-[34px] px-[clamp(16px,5vw,48px)] m-0 snap-x snap-proximity [scrollbar-width:none] focus-visible:outline-none">
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-a/640/360" width="640" height="360" decoding="async" alt="Nightfall" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Nightfall</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Series &middot; 2025 &middot; Thriller</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-b/640/360" width="640" height="360" loading="lazy" decoding="async" alt="The Long Coast" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">The Long Coast</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Film &middot; 2024 &middot; Drama</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-c/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Ember" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Ember</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Series &middot; 2025 &middot; Sci-Fi</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-d/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Static" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Static</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Series &middot; 2023 &middot; Mystery</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-e/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Meridian" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Meridian</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Film &middot; 2025 &middot; Adventure</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-f/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Halflight" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Halflight</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Series &middot; 2024 &middot; Horror</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-g/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Undertow" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Undertow</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Film &middot; 2025 &middot; Thriller</span></span>
          </a>
        </li>
        <li class="group flex-none basis-[var(--tile-w)] snap-start relative transition-[scale] duration-300 ease-[cubic-bezier(0.2,0.8,0.2,1)] hover:scale-[1.32] hover:z-[3] focus-within:scale-[1.32] focus-within:z-[3] first:hover:origin-left last:hover:origin-right first:focus-within:origin-left last:focus-within:origin-right motion-reduce:transition-none motion-reduce:hover:scale-100 motion-reduce:focus-within:scale-100">
          <a href="#" class="block relative rounded-md overflow-hidden no-underline bg-tcar09-tile shadow-[0_12px_26px_-18px_#000] transition-shadow duration-300 group-hover:shadow-[0_24px_48px_-16px_oklch(0_0_0/0.9),0_0_0_2px_oklch(1_0_0/0.08)] focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:outline-offset-2">
            <span class="block relative w-full aspect-video overflow-hidden bg-tcar09-tile"><img src="https://picsum.photos/seed/flix-h/640/360" width="640" height="360" loading="lazy" decoding="async" alt="Blackwater" class="absolute inset-0 size-full object-cover block"></span>
            <span class="absolute inset-x-0 bottom-0 px-3 pt-11 pb-2.5 flex flex-col gap-0.5 bg-[linear-gradient(transparent,oklch(0_0_0/0.88)_55%,oklch(0_0_0/0.96))] opacity-0 pointer-events-none transition-opacity duration-300 delay-75 group-hover:opacity-100 group-focus-within:opacity-100"><span class="text-sm font-bold text-white leading-tight">Blackwater</span><span class="text-[10.5px] font-semibold text-tcar09-sub tracking-[0.02em]">Series &middot; 2024 &middot; Crime</span></span>
          </a>
        </li>
      </ul>
    </div>
    <button type="button" data-dir="1" aria-label="Scroll row right" class="absolute right-0 top-[15px] z-[4] w-10 h-[calc(100%-30px)] max-sm:hidden flex items-center justify-center border-0 p-0 cursor-pointer bg-tcar09-navbg text-white opacity-0 transition-[opacity,background-color] duration-200 group-hover/wrap:opacity-100 group-focus-within/wrap:opacity-100 hover:bg-tcar09-navbghover focus-visible:opacity-100 focus-visible:outline-2 focus-visible:outline-tcar09-acc focus-visible:-outline-offset-4">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcar09-bg: #0b0b0f;
  --color-tcar09-bg: oklch(0.15 0.006 280);
  --color-tcar09-tile: #1a1a20;
  --color-tcar09-tile: oklch(0.24 0.008 280);
  --color-tcar09-ink: #f5f5f7;
  --color-tcar09-ink: oklch(0.97 0.002 280);
  --color-tcar09-sub: #c2c2c9;
  --color-tcar09-sub: oklch(0.82 0.005 280);
  --color-tcar09-acc: #e50914;
  --color-tcar09-acc: oklch(0.55 0.23 27);
  --color-tcar09-navbg: #141414;
  --color-tcar09-navbg: oklch(0.2 0 0 / 0.55);
  --color-tcar09-navbghover: #141414;
  --color-tcar09-navbghover: oklch(0.2 0 0 / 0.88);
  --font-tcar09-sans: 'Archivo', system-ui, sans-serif;
}

.tcar-09 {
  width: 100%;
  min-height: 100svh;
}

.tcar-09 ::selection {
  background: var(--color-tcar09-acc);
  color: #fff;
}
/* Scrollbar hiding needs the -webkit- pseudo; there is no variant form. */

.tcar09-row::-webkit-scrollbar {
  display: none;
}
/* Safari < 15.4 mask prefix for the edge fade. */

.tcar-09 [class*="mask-image"] {
  -webkit-mask: linear-gradient(90deg, transparent, #000 4%, #000 96%, transparent);
}

@media (prefers-reduced-motion: reduce) {
  .tcar09-row {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
// Five lines of paging, plus one branch the CSS variant cannot express.
const row = document.querySelector('.tcar09-row');
const calm = window.matchMedia('(prefers-reduced-motion: reduce)');
document.querySelectorAll('.tcar-09 button[data-dir]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const dir = Number(btn.dataset.dir);
    row.scrollBy({ left: dir * row.clientWidth * 0.9, behavior: calm.matches ? 'auto' : 'smooth' });
  });
});
```
