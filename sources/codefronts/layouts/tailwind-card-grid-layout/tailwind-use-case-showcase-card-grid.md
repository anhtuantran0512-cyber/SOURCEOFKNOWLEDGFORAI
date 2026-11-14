---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-use-case-showcase-card-grid/"
title: "Tailwind Use-Case Showcase Card Grid"
section: "layouts"
category: "tailwind-card-grid-layout"
category_name: "Tailwind Card Grid Layouts"
description: "Four cards, each a fully-drawn page archetype inside a browser frame &mdash; a photo gallery with a carousel and filmstrip, a contact page with labelled…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Use-Case Showcase Card Grid
Source: https://codefronts.com/layouts/tailwind-card-grid-layout/tailwind-use-case-showcase-card-grid/

Four cards, each a fully-drawn page archetype inside a browser frame &mdash; a photo gallery with a carousel and filmstrip, a contact page with labelled fields and an inline-SVG map, a five-column shop grid and a four-column team grid. Every one of those miniatures is nested Tailwind grids and flexbox, which makes this the demo that proves utilities scale down to a 12px-tall mock.
## HTML
```html
<section class="tcg-09 w-full min-h-svh flex items-center justify-center bg-tcg09-bg font-tcg09-sans px-9 py-6" aria-label="Use-case showcase card grid demo">
  <div class="w-full max-w-[760px] grid grid-cols-2 max-[640px]:grid-cols-1 gap-x-9 gap-y-4.5 max-[640px]:gap-8">

    <article class="group flex flex-col items-center gap-3.5 transition-transform duration-350 ease-tcg09 hover:-translate-y-1.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[16/10] flex flex-col rounded-md overflow-hidden bg-tcg09-tile shadow-[0_8px_22px_oklch(0_0_0/0.25)]">
        <div class="h-7 shrink-0 flex items-center gap-1.25 px-2.5 bg-tcg09-chrome" aria-hidden="true">
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="flex-1 max-w-[60%] ml-2 px-2.5 py-0.75 rounded-[10px] truncate bg-white/92 text-tcg09-urlink text-[.52rem] font-semibold">photos.app / albums</span>
          <span class="ml-auto text-white/90 text-[.85rem] font-bold leading-none">&#8943;</span>
        </div>
        <div class="flex-1 min-h-0 flex flex-col gap-1.75 px-3 py-2.5 bg-white" aria-hidden="true">
          <div class="flex items-center justify-between">
            <span class="text-[.62rem] font-bold text-tcg09-ink">Albums</span>
            <span class="text-[.5rem] font-semibold text-tcg09-mut">All &#9662;</span>
          </div>
          <div class="relative flex-1 min-h-0 flex items-center justify-center rounded">
            <span class="absolute left-1.5 z-1 flex items-center justify-center w-4 h-4 rounded-full bg-black/28 text-white text-[.7rem] leading-none">&#8249;</span>
            <div class="flex-1 h-full flex items-end px-2 py-1.5 rounded bg-[linear-gradient(180deg,oklch(0_0_0/0)_60%,oklch(0_0_0/0.42)),linear-gradient(135deg,#5b8fd9_0%,#3c5f9a_50%,#1f3866_100%)]">
              <span class="text-white text-[.5rem] font-bold tracking-[0.04em] [text-shadow:0_1px_2px_oklch(0_0_0/0.4)]">Iceland &middot; 2026</span>
            </div>
            <span class="absolute right-1.5 z-1 flex items-center justify-center w-4 h-4 rounded-full bg-black/28 text-white text-[.7rem] leading-none">&#8250;</span>
          </div>
          <div class="flex gap-1 h-[18%] shrink-0">
            <span class="flex-1 rounded-sm border-[1.5px] border-transparent bg-linear-[135deg,#86b58a,#3d7a4a]"></span>
            <span class="flex-1 rounded-sm border-[1.5px] border-transparent bg-linear-[135deg,#e8b08a,#a85d3d]"></span>
            <span class="flex-1 rounded-sm border-[1.5px] border-tcg09-active bg-linear-[135deg,#5b8fd9,#1f3866]"></span>
            <span class="flex-1 rounded-sm border-[1.5px] border-transparent bg-linear-[135deg,#d987a8,#7a3855]"></span>
            <span class="flex-1 rounded-sm border-[1.5px] border-transparent bg-linear-[135deg,#c4b88a,#7a6a3d]"></span>
          </div>
        </div>
      </div>
      <p class="text-tcg09-label text-[.92rem] font-medium tracking-[0.01em]">Gallery</p>
    </article>

    <article class="group flex flex-col items-center gap-3.5 transition-transform duration-350 ease-tcg09 hover:-translate-y-1.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[16/10] flex flex-col rounded-md overflow-hidden bg-tcg09-tile shadow-[0_8px_22px_oklch(0_0_0/0.25)]">
        <div class="h-7 shrink-0 flex items-center gap-1.25 px-2.5 bg-tcg09-chrome" aria-hidden="true">
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="flex-1 max-w-[60%] ml-2 px-2.5 py-0.75 rounded-[10px] truncate bg-white/92 text-tcg09-urlink text-[.52rem] font-semibold">acme.co / contact</span>
          <span class="ml-auto text-white/90 text-[.85rem] font-bold leading-none">&#8943;</span>
        </div>
        <div class="flex-1 min-h-0 flex flex-col gap-1.75 px-3 py-2.5 bg-white" aria-hidden="true">
          <span class="text-[.62rem] font-bold text-tcg09-ink">Get in touch</span>
          <div class="flex-1 min-h-0 grid [grid-template-columns:1.1fr_1fr] gap-2">
            <div class="flex flex-col gap-1.25">
              <label class="flex flex-col gap-px"><span class="text-[.42rem] font-semibold tracking-[0.04em] text-tcg09-mut">Name</span><b class="block px-1.25 py-0.75 rounded-sm border border-tcg09-line bg-tcg09-field text-tcg09-ink text-[.46rem] font-medium truncate">Sarah Patel</b></label>
              <label class="flex flex-col gap-px"><span class="text-[.42rem] font-semibold tracking-[0.04em] text-tcg09-mut">Email</span><b class="block px-1.25 py-0.75 rounded-sm border border-tcg09-line bg-tcg09-field text-tcg09-ink text-[.46rem] font-medium truncate">[email protected]</b></label>
              <label class="flex flex-col gap-px"><span class="text-[.42rem] font-semibold tracking-[0.04em] text-tcg09-mut">Message</span><b class="block px-1.25 pt-0.75 pb-2 rounded-sm border border-tcg09-line bg-tcg09-field text-tcg09-ink text-[.46rem] font-medium truncate">Hi team, I would love a demo&hellip;</b></label>
              <span class="self-start mt-0.5 px-2 py-1 rounded-[3px] bg-tcg09-ink text-white text-[.46rem] font-bold">Send &rarr;</span>
            </div>
            <div class="rounded-[3px] overflow-hidden">
              <svg viewBox="0 0 60 60" class="block w-full h-full" preserveAspectRatio="none" role="presentation">
                <rect width="60" height="60" fill="#dde6ef"></rect>
                <path d="M0 20 L60 16" stroke="#fff" stroke-width="2" fill="none"></path>
                <path d="M0 36 L60 32" stroke="#fff" stroke-width="2" fill="none"></path>
                <path d="M14 0 L18 60" stroke="#fff" stroke-width="2" fill="none"></path>
                <path d="M42 0 L46 60" stroke="#fff" stroke-width="2" fill="none"></path>
                <rect x="20" y="22" width="14" height="10" fill="#c0cbd8"></rect>
                <circle cx="34" cy="34" r="6" fill="#ef4444"></circle>
                <circle cx="34" cy="34" r="2" fill="#fff"></circle>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <p class="text-tcg09-label text-[.92rem] font-medium tracking-[0.01em]">Contact Page</p>
    </article>

    <article class="group flex flex-col items-center gap-3.5 transition-transform duration-350 ease-tcg09 hover:-translate-y-1.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[16/10] flex flex-col rounded-md overflow-hidden bg-tcg09-tile shadow-[0_8px_22px_oklch(0_0_0/0.25)]">
        <div class="h-7 shrink-0 flex items-center gap-1.25 px-2.5 bg-tcg09-chrome" aria-hidden="true">
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="flex-1 max-w-[60%] ml-2 px-2.5 py-0.75 rounded-[10px] truncate bg-white/92 text-tcg09-urlink text-[.52rem] font-semibold">shop.co / products</span>
          <span class="ml-auto text-white/90 text-[.85rem] font-bold leading-none">&#8943;</span>
        </div>
        <div class="flex-1 min-h-0 flex flex-col gap-1.75 px-3 py-2.5 bg-white" aria-hidden="true">
          <span class="text-[.62rem] font-bold text-tcg09-ink">Shop &middot; 247 items</span>
          <div class="flex-1 min-h-0 grid [grid-template-columns:repeat(5,1fr)] [grid-template-rows:repeat(2,1fr)] gap-1.25">
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#f7b88a,#d97f4f]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$32</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#a7c8e7,#5b8fd9]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$48</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#c5da9c,#7aa852]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$19</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#f9c1cf,#d97a99]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$74</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#c4b5fd,#9b87e5]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$58</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#fef0a3,#e6c54a]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$24</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#86b58a,#3d7a4a]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$96</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#e8b08a,#a85d3d]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$12</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#5b8fd9,#1f3866]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$45</b></span>
            <span class="relative flex items-end justify-end overflow-hidden px-1 py-0.75 rounded-[3px] bg-linear-[135deg,#d987a8,#7a3855]"><b class="px-0.75 rounded-sm bg-black/55 text-white text-[.42rem] font-extrabold">$67</b></span>
          </div>
        </div>
      </div>
      <p class="text-tcg09-label text-[.92rem] font-medium tracking-[0.01em]">5 Column Grid</p>
    </article>

    <article class="group flex flex-col items-center gap-3.5 transition-transform duration-350 ease-tcg09 hover:-translate-y-1.5 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="w-full aspect-[16/10] flex flex-col rounded-md overflow-hidden bg-tcg09-tile shadow-[0_8px_22px_oklch(0_0_0/0.25)]">
        <div class="h-7 shrink-0 flex items-center gap-1.25 px-2.5 bg-tcg09-chrome" aria-hidden="true">
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="w-1.75 h-1.75 rounded-full bg-white/55 transition-colors duration-300 group-hover:bg-white/95"></span>
          <span class="flex-1 max-w-[60%] ml-2 px-2.5 py-0.75 rounded-[10px] truncate bg-white/92 text-tcg09-urlink text-[.52rem] font-semibold">acme.co / team</span>
          <span class="ml-auto text-white/90 text-[.85rem] font-bold leading-none">&#8943;</span>
        </div>
        <div class="flex-1 min-h-0 flex flex-col gap-1.75 px-3 py-2.5 bg-white" aria-hidden="true">
          <span class="text-[.62rem] font-bold text-tcg09-ink">Meet the team</span>
          <div class="flex-1 min-h-0 grid [grid-template-columns:repeat(4,1fr)] [grid-template-rows:repeat(2,1fr)] gap-1.25">
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#f9c1cf,#d97a99]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Maya &middot; CEO</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#a7c8e7,#5b8fd9]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Liam &middot; CTO</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#c5da9c,#7aa852]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Aria &middot; Design</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#f7b88a,#d97f4f]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Noah &middot; Eng</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#c4b5fd,#9b87e5]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Zoe &middot; Ops</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#86b58a,#3d7a4a]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Sam &middot; Sales</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#fef0a3,#e6c54a]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Ivy &middot; CS</em></span>
            <span class="flex flex-col items-center justify-center gap-0.5 px-0.5 py-1 overflow-hidden rounded-[3px] border border-tcg09-line bg-white"><i class="block w-[54%] aspect-square rounded-full bg-linear-[135deg,#e8b08a,#a85d3d]"></i><em class="not-italic text-center text-[.4rem] font-semibold leading-[1.1] text-tcg09-ink">Kai &middot; Eng</em></span>
          </div>
        </div>
      </div>
      <p class="text-tcg09-label text-[.92rem] font-medium tracking-[0.01em]">4 Column Grid</p>
    </article>

  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tcg09-bg: #2a3450;
  --color-tcg09-bg: oklch(0.32 0.05 265);
  --color-tcg09-chrome: #2f7fb8;
  --color-tcg09-chrome: oklch(0.55 0.11 240);
  --color-tcg09-tile: #f4f6fa;
  --color-tcg09-tile: oklch(0.97 0.006 260);
  --color-tcg09-field: #eef1f6;
  --color-tcg09-field: oklch(0.95 0.008 260);
  --color-tcg09-line: #dde1ea;
  --color-tcg09-line: oklch(0.89 0.01 260);
  --color-tcg09-ink: #1f2942;
  --color-tcg09-ink: oklch(0.27 0.04 265);
  --color-tcg09-mut: #5b6478;
  --color-tcg09-mut: oklch(0.49 0.03 265);
  --color-tcg09-urlink: #3f495e;
  --color-tcg09-urlink: oklch(0.4 0.03 265);
  --color-tcg09-active: #5b8fd9;
  --color-tcg09-active: oklch(0.63 0.13 255);
  --color-tcg09-label: #e6e8ef;
  --color-tcg09-label: oklch(0.93 0.008 265);
  --font-tcg09-sans: 'Space Grotesk', system-ui, sans-serif;
  --ease-tcg09: cubic-bezier(0.4, 0.2, 0.2, 1);
}
/* Root rule: the full-bleed contract. */

.tcg-09 {
  width: 100%;
  min-height: 100svh;
}

.tcg-09 ::selection {
  background: #3b82f6;
  color: #fff;
}
```
