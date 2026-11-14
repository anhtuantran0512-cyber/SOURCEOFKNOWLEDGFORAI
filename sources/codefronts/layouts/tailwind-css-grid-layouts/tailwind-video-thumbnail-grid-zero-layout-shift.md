---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-video-thumbnail-grid-zero-layout-shift/"
title: "Tailwind Video Thumbnail Grid with Zero Layout Shift"
section: "layouts"
category: "tailwind-css-grid-layouts"
category_name: "Tailwind CSS Grid Layouts"
description: "A course catalogue: 16:9 thumbnails reserved before any pixel loads, duration badges, progress bars on started lessons, and instructor lines."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Thumbnail Grid with Zero Layout Shift
Source: https://codefronts.com/layouts/tailwind-css-grid-layouts/tailwind-video-thumbnail-grid-zero-layout-shift/

A course catalogue: 16:9 thumbnails reserved before any pixel loads, duration badges, progress bars on started lessons, and instructor lines. Tailwind ships aspect-video, so the CLS fix is one word.
## HTML
```html
<section class="tgx-19 w-full min-h-svh bg-tgx19-bg font-tgx19-sans p-6">
  <header class="flex items-end justify-between gap-4 flex-wrap mb-5">
    <div class="flex flex-col gap-1">
      <p class="text-[0.66rem] tracking-[0.18em] uppercase text-tgx19-dim">Layout School · Track 2</p>
      <h2 class="text-[1.35rem] font-semibold text-tgx19-ink tracking-[-0.01em]">CSS Grid, end to end</h2>
    </div>
    <p class="text-[0.76rem] text-tgx19-dim tabular-nums">4 of 18 lessons · 2h 12m left</p>
  </header>
  <div class="grid grid-cols-[repeat(auto-fit,minmax(min(220px,100%),1fr))] gap-5">
    <article class="group flex flex-col gap-2.5">
      <a href="#0" class="block no-underline rounded-xl focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2">
        <div class="grid w-full aspect-video rounded-xl overflow-hidden bg-tgx19-cell relative outline-offset-2 outline-tgx19-cyan group-hover:outline-2">
          <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=640&h=360&q=80&auto=format&fit=crop" alt="Laptop screen showing code in a dim room" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          <span class="relative place-self-end m-2 text-[0.66rem] tabular-nums text-white bg-black/75 rounded px-1.5 py-0.5">12:04</span>
        </div>
      </a>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-[0.9rem] leading-[1.35] font-medium text-tgx19-ink"><a href="#0" class="no-underline text-inherit hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2 rounded">Tracks, lines and the implicit grid</a></h3>
        <p class="text-[0.74rem] text-tgx19-dim">Marit Solheim · Lesson 1</p>
        <div role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson 1 progress" class="h-1 rounded-full bg-tgx19-track overflow-hidden"><span class="block h-full w-full bg-tgx19-done"></span></div>
      </div>
    </article>
    <article class="group flex flex-col gap-2.5">
      <a href="#0" class="block no-underline rounded-xl focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2">
        <div class="grid w-full aspect-video rounded-xl overflow-hidden bg-tgx19-cell relative outline-offset-2 outline-tgx19-cyan group-hover:outline-2">
          <img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=640&h=360&q=80&auto=format&fit=crop" alt="Close-up of code on a monitor with syntax colours" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          <span class="relative place-self-end m-2 text-[0.66rem] tabular-nums text-white bg-black/75 rounded px-1.5 py-0.5">8:47</span>
        </div>
      </a>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-[0.9rem] leading-[1.35] font-medium text-tgx19-ink"><a href="#0" class="no-underline text-inherit hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2 rounded">Subgrid in practice</a></h3>
        <p class="text-[0.74rem] text-tgx19-dim">Marit Solheim · Lesson 2</p>
        <div role="progressbar" aria-valuenow="62" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson 2 progress" class="h-1 rounded-full bg-tgx19-track overflow-hidden"><span class="block h-full w-[62%] bg-tgx19-cyan"></span></div>
      </div>
    </article>
    <article class="group flex flex-col gap-2.5">
      <a href="#0" class="block no-underline rounded-xl focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2">
        <div class="grid w-full aspect-video rounded-xl overflow-hidden bg-tgx19-cell relative outline-offset-2 outline-tgx19-cyan group-hover:outline-2">
          <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=640&h=360&q=80&auto=format&fit=crop" alt="Terminal window and editor split across a widescreen display" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          <span class="relative place-self-end m-2 text-[0.66rem] tabular-nums text-white bg-black/75 rounded px-1.5 py-0.5">21:33</span>
        </div>
      </a>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-[0.9rem] leading-[1.35] font-medium text-tgx19-ink"><a href="#0" class="no-underline text-inherit hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2 rounded">Container queries, deep dive</a></h3>
        <p class="text-[0.74rem] text-tgx19-dim">Tomás Rivas · Lesson 3</p>
        <div role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson 3 progress" class="h-1 rounded-full bg-tgx19-track overflow-hidden"><span class="block h-full w-0 bg-tgx19-cyan"></span></div>
      </div>
    </article>
    <article class="group flex flex-col gap-2.5">
      <a href="#0" class="block no-underline rounded-xl focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2">
        <div class="grid w-full aspect-video rounded-xl overflow-hidden bg-tgx19-cell relative outline-offset-2 outline-tgx19-cyan group-hover:outline-2">
          <img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=640&h=360&q=80&auto=format&fit=crop" alt="Laptop open on a desk beside a notebook and coffee" loading="lazy" class="absolute inset-0 w-full h-full object-cover">
          <span class="relative place-self-end m-2 text-[0.66rem] tabular-nums text-white bg-black/75 rounded px-1.5 py-0.5">6:15</span>
        </div>
      </a>
      <div class="flex flex-col gap-1.5">
        <h3 class="text-[0.9rem] leading-[1.35] font-medium text-tgx19-ink"><a href="#0" class="no-underline text-inherit hover:underline underline-offset-2 focus-visible:outline-2 focus-visible:outline-tgx19-cyan focus-visible:outline-offset-2 rounded">clip-path shapes without SVG</a></h3>
        <p class="text-[0.74rem] text-tgx19-dim">Tomás Rivas · Lesson 4</p>
        <div role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson 4 progress" class="h-1 rounded-full bg-tgx19-track overflow-hidden"><span class="block h-full w-0 bg-tgx19-cyan"></span></div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tgx19-bg: #14181c;
  --color-tgx19-bg: oklch(0.18 0.01 220);
  --color-tgx19-cell: #202830;
  --color-tgx19-cell: oklch(0.25 0.015 220);
  --color-tgx19-track: #2c363e;
  --color-tgx19-track: oklch(0.3 0.015 220);
  --color-tgx19-ink: #eef2f4;
  --color-tgx19-ink: oklch(0.95 0.01 220);
  --color-tgx19-dim: #9fabb2;
  --color-tgx19-dim: oklch(0.74 0.015 220);
  --color-tgx19-cyan: #79d2e3;
  --color-tgx19-cyan: oklch(0.82 0.1 210);
  --color-tgx19-done: #8ce0ae;
  --color-tgx19-done: oklch(0.85 0.14 150);
  --font-tgx19-sans: 'Inter Tight', system-ui, sans-serif;
}

.tgx-19 {
  width: 100%;
  min-height: 100svh;
}
```
