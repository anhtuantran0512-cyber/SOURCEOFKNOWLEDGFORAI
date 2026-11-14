---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-elastic-bounce-dropdown-menu/"
title: "Tailwind Elastic Bounce Dropdown Menu"
section: "navigation"
category: "tailwind-dropdown-menus"
category_name: "Tailwind Dropdown Menus"
description: "The springy one: the panel snaps open on scale-y with an overshoot curve, so it briefly overshoots its own height and settles."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Elastic Bounce Dropdown Menu
Source: https://codefronts.com/navigation/tailwind-dropdown-menus/tailwind-elastic-bounce-dropdown-menu/

The springy one: the panel snaps open on scale-y with an overshoot curve, so it briefly overshoots its own height and settles. Porting it is mostly about the easing token — an overshoot curve is a design decision, so it belongs in @theme as --ease-tdd04, not inline as an arbitrary value.
## HTML
```html
<section class="tdd-04 w-full min-h-svh grid justify-center content-start bg-linear-[135deg,var(--color-tdd04-bg1),var(--color-tdd04-bg2),var(--color-tdd04-bg3)] font-tdd04-sans text-tdd04-ink px-5 py-8" aria-label="Elastic bounce dropdown demo">
  <nav class="relative z-10 flex items-center gap-2 rounded-full bg-white py-2 pr-2 pl-6 shadow-[0_4px_24px_oklch(0.65_0.2_350/0.15)]" aria-label="Primary">
    <span class="mr-2 text-base font-bold tracking-[-0.3px] text-tdd04-acc">&#9670; Bounce</span>
    <div class="flex gap-0.5">
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#explore" class="flex items-center gap-1 rounded-full px-4 py-2 text-sm font-semibold text-tdd04-ink no-underline transition-colors duration-150 group-hover:bg-tdd04-tint group-hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd04-acc">Explore &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-48 -translate-x-1/2 scale-y-0 origin-top flex-col gap-0.5 rounded-2xl border border-tdd04-acc/12 bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0.65_0.2_350/0.18)] transition-[scale,opacity] duration-500 ease-tdd04 group-hover:pointer-events-auto group-hover:scale-y-100 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:scale-y-100 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#featured" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#127775; Featured</a>
          <a href="#trending" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128293; Trending</a>
          <a href="#new" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128640; New Arrivals</a>
          <a href="#top" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#127942; Top Rated</a>
          <div class="my-1 h-px bg-tdd04-edge" aria-hidden="true"></div>
          <a href="#all" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-bold text-tdd04-acc no-underline transition-colors duration-150 hover:bg-tdd04-tint focus-visible:bg-tdd04-tint focus-visible:outline-none">View All &#8594;</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#learn" class="flex items-center gap-1 rounded-full px-4 py-2 text-sm font-semibold text-tdd04-ink no-underline transition-colors duration-150 group-hover:bg-tdd04-tint group-hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd04-acc">Learn &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-48 -translate-x-1/2 scale-y-0 origin-top flex-col gap-0.5 rounded-2xl border border-tdd04-acc/12 bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0.65_0.2_350/0.18)] transition-[scale,opacity] duration-500 ease-tdd04 group-hover:pointer-events-auto group-hover:scale-y-100 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:scale-y-100 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#tutorials" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128218; Tutorials</a>
          <a href="#courses" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#127916; Video Courses</a>
          <a href="#workshops" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#127881; Workshops</a>
        </div>
      </div>
      <div class="group relative after:absolute after:inset-x-0 after:top-full after:h-2.5 after:content-['']">
        <a href="#connect" class="flex items-center gap-1 rounded-full px-4 py-2 text-sm font-semibold text-tdd04-ink no-underline transition-colors duration-150 group-hover:bg-tdd04-tint group-hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tdd04-acc">Connect &#9662;</a>
        <div class="pointer-events-none absolute top-[calc(100%+10px)] left-1/2 flex min-w-48 -translate-x-1/2 scale-y-0 origin-top flex-col gap-0.5 rounded-2xl border border-tdd04-acc/12 bg-white p-2 opacity-0 shadow-[0_12px_40px_oklch(0.65_0.2_350/0.18)] transition-[scale,opacity] duration-500 ease-tdd04 group-hover:pointer-events-auto group-hover:scale-y-100 group-hover:opacity-100 group-focus-within:pointer-events-auto group-focus-within:scale-y-100 group-focus-within:opacity-100 motion-reduce:duration-150">
          <a href="#community" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128172; Community</a>
          <a href="#forum" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128101; Forum</a>
          <a href="#newsletter" class="block rounded-[10px] px-3.5 py-2.5 text-[13.5px] font-medium text-tdd04-ink no-underline transition-colors duration-150 hover:bg-tdd04-tint hover:text-tdd04-acc focus-visible:bg-tdd04-tint focus-visible:outline-none">&#128236; Newsletter</a>
        </div>
      </div>
    </div>
  </nav>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tdd04-bg1: #fdf2f8;
  --color-tdd04-bg1: oklch(0.97 0.02 350);
  --color-tdd04-bg2: #fce7f3;
  --color-tdd04-bg2: oklch(0.94 0.04 350);
  --color-tdd04-bg3: #ede9fe;
  --color-tdd04-bg3: oklch(0.94 0.03 295);
  --color-tdd04-ink: #1e1b4b;
  --color-tdd04-ink: oklch(0.26 0.08 285);
  --color-tdd04-edge: #f3f4f6;
  --color-tdd04-edge: oklch(0.96 0.003 265);
  --color-tdd04-tint: #fdf2f8;
  --color-tdd04-tint: oklch(0.97 0.02 350);
  --color-tdd04-acc: #ec4899;
  --color-tdd04-acc: oklch(0.65 0.2 350);
  --font-tdd04-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
  --ease-tdd04: cubic-bezier(0.34, 1.56, 0.64, 1);
}

.tdd-04 {
  width: 100%;
  min-height: 100svh;
}

.tdd-04 ::selection {
  background: var(--color-tdd04-acc);
  color: #fff;
}
```
