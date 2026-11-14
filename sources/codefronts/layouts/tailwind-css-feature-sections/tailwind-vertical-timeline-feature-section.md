---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-vertical-timeline-feature-section/"
title: "Tailwind Vertical Timeline Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A vertical timeline of four milestones: a single rail on phones, an alternating two-sided layout from md: up, with the centre line filling as you scroll…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Vertical Timeline Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-vertical-timeline-feature-section/

A vertical timeline of four milestones: a single rail on phones, an alternating two-sided layout from md: up, with the centre line filling as you scroll (scroll-driven, progressive). Alternation is one variant on the list item — md:even:[&>article]:col-start-3 — not separate left/right markup.
## HTML
```html
<section class="tfs-22 w-full min-h-svh bg-tfs22-bg px-5 py-20 font-tfs22-sans text-white antialiased sm:py-28" aria-labelledby="tfs-22-h">
  <div class="mx-auto grid w-full max-w-5xl gap-16">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="text-sm font-semibold text-tfs22-acc">Your first 30 days</p>
      <h2 id="tfs-22-h" class="text-balance font-tfs22-display text-4xl font-bold tracking-tight sm:text-6xl">From kickoff to fully live</h2>
    </header>
    <div class="relative [view-timeline-name:--tfs22]">
    <div aria-hidden="true" class="absolute bottom-0 left-5 top-0 w-0.5 overflow-hidden rounded-full bg-white/10 md:left-1/2 md:-translate-x-1/2"><span class="block size-full origin-top bg-linear-to-b from-tfs22-acc to-tfs22-acc2 supports-[animation-timeline:view()]:animate-tfs22-fill supports-[animation-timeline:view()]:[animation-timeline:--tfs22] supports-[animation-timeline:view()]:[animation-range:entry_50%_exit_50%] motion-reduce:animate-none"></span></div>
    <ol class="grid gap-10">
      <li class="relative grid grid-cols-[2.5rem_1fr] gap-5 md:grid-cols-[1fr_2.5rem_1fr] md:gap-8 md:even:[&>article]:col-start-3 md:even:[&>article]:text-left md:odd:[&>article]:text-right">
        <span class="relative z-10 grid size-10 place-items-center rounded-full bg-tfs22-card text-tfs22-acc ring-8 ring-tfs22-bg md:col-start-2 md:row-start-1"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span>
        <article class="group grid gap-2 rounded-3xl bg-tfs22-card p-6 ring-1 ring-white/10 transition hover:ring-tfs22-acc/40 md:col-start-1 md:row-start-1 sm:p-7">
          <time datetime="2026-10-01" class="font-tfs22-display text-sm font-semibold text-tfs22-acc">Day 1</time>
          <h3 class="font-tfs22-display text-2xl font-bold">Kickoff call</h3>
          <p class="text-pretty text-tfs22-mut">Meet your solutions engineer and map your current workflows.</p>
        </article>
      </li>
      <li class="relative grid grid-cols-[2.5rem_1fr] gap-5 md:grid-cols-[1fr_2.5rem_1fr] md:gap-8 md:even:[&>article]:col-start-3 md:even:[&>article]:text-left md:odd:[&>article]:text-right">
        <span class="relative z-10 grid size-10 place-items-center rounded-full bg-tfs22-card text-tfs22-acc ring-8 ring-tfs22-bg md:col-start-2 md:row-start-1"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 8c5 0 9-1.3 9-3s-4-3-9-3-9 1.3-9 3 4 3 9 3zM3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/></svg></span>
        <article class="group grid gap-2 rounded-3xl bg-tfs22-card p-6 ring-1 ring-white/10 transition hover:ring-tfs22-acc/40 md:col-start-1 md:row-start-1 sm:p-7">
          <time datetime="2026-10-03" class="font-tfs22-display text-sm font-semibold text-tfs22-acc">Day 3</time>
          <h3 class="font-tfs22-display text-2xl font-bold">Data connected</h3>
          <p class="text-pretty text-tfs22-mut">Warehouse and CRM synced; historical data backfilled overnight.</p>
        </article>
      </li>
      <li class="relative grid grid-cols-[2.5rem_1fr] gap-5 md:grid-cols-[1fr_2.5rem_1fr] md:gap-8 md:even:[&>article]:col-start-3 md:even:[&>article]:text-left md:odd:[&>article]:text-right">
        <span class="relative z-10 grid size-10 place-items-center rounded-full bg-tfs22-card text-tfs22-acc ring-8 ring-tfs22-bg md:col-start-2 md:row-start-1"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg></span>
        <article class="group grid gap-2 rounded-3xl bg-tfs22-card p-6 ring-1 ring-white/10 transition hover:ring-tfs22-acc/40 md:col-start-1 md:row-start-1 sm:p-7">
          <time datetime="2026-10-14" class="font-tfs22-display text-sm font-semibold text-tfs22-acc">Day 14</time>
          <h3 class="font-tfs22-display text-2xl font-bold">Team onboarded</h3>
          <p class="text-pretty text-tfs22-mut">Role-based training for admins, managers and reps.</p>
        </article>
      </li>
      <li class="relative grid grid-cols-[2.5rem_1fr] gap-5 md:grid-cols-[1fr_2.5rem_1fr] md:gap-8 md:even:[&>article]:col-start-3 md:even:[&>article]:text-left md:odd:[&>article]:text-right">
        <span class="relative z-10 grid size-10 place-items-center rounded-full bg-tfs22-card text-tfs22-acc ring-8 ring-tfs22-bg md:col-start-2 md:row-start-1"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg></span>
        <article class="group grid gap-2 rounded-3xl bg-tfs22-card p-6 ring-1 ring-white/10 transition hover:ring-tfs22-acc/40 md:col-start-1 md:row-start-1 sm:p-7">
          <time datetime="2026-10-30" class="font-tfs22-display text-sm font-semibold text-tfs22-acc">Day 30</time>
          <h3 class="font-tfs22-display text-2xl font-bold">Fully live</h3>
          <p class="text-pretty text-tfs22-mut">First automated report lands in every inbox. Success review booked.</p>
        </article>
      </li>
    </ol>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs22-bg: #0b0f1a;
  --color-tfs22-bg: oklch(0.17 0.024 268);
  --color-tfs22-card: #121829;
  --color-tfs22-card: oklch(0.212 0.035 269);
  --color-tfs22-mut: #a9b2c7;
  --color-tfs22-mut: oklch(0.763 0.032 267);
  --color-tfs22-acc: #fb923c;
  --color-tfs22-acc: oklch(0.758 0.159 56);
  --color-tfs22-acc2: #f43f5e;
  --color-tfs22-acc2: oklch(0.645 0.215 16);
  --font-tfs22-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tfs22-sans: 'DM Sans', system-ui, sans-serif;
  --animate-tfs22-fill: tfs22-fill linear both;

  @keyframes tfs22-fill {
    from {
      transform: scaleY(0);
    }

    to {
      transform: scaleY(1);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-22 {
  width: 100%;
  min-height: 100svh;
}
```
