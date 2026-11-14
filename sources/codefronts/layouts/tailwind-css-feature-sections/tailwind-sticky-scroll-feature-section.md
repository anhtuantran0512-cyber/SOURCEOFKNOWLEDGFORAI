---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-sticky-scroll-feature-section/"
title: "Tailwind Sticky Scroll Feature Section"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "Scroll storytelling without a library: a sticky left column holds the headline and a progress rail that fills as you read, while four step cards scroll past…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Sticky Scroll Feature Section
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-sticky-scroll-feature-section/

Scroll storytelling without a library: a sticky left column holds the headline and a progress rail that fills as you read, while four step cards scroll past on the right, each easing into focus. The rail is driven by a named view timeline shared through timeline-scope — all arbitrary properties, gated behind supports-[animation-timeline:view()]:.
## HTML
```html
<section class="tfs-12 w-full min-h-svh bg-tfs12-bg px-5 py-20 font-tfs12-sans text-tfs12-ink antialiased [timeline-scope:--tfs12] sm:py-28" aria-labelledby="tfs-12-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12 lg:grid-cols-[1fr_1.2fr] lg:gap-20">
    <div class="lg:sticky lg:top-12 lg:self-start">
      <div class="grid gap-6">
        <p class="text-sm font-semibold text-tfs12-acc">How Ranger works</p>
        <h2 id="tfs-12-h" class="text-balance font-tfs12-display text-4xl font-bold tracking-tight sm:text-6xl">From signup to first insight in four steps</h2>
        <p class="text-pretty text-lg text-tfs12-mut">No onboarding call, no SDK sprint. Most teams finish before lunch.</p>
        <div aria-hidden="true" class="hidden h-1.5 w-full max-w-xs overflow-hidden rounded-full bg-tfs12-line lg:block"><div class="h-full w-full origin-left scale-x-25 rounded-full bg-tfs12-acc supports-[animation-timeline:view()]:animate-tfs12-rail supports-[animation-timeline:view()]:[animation-timeline:--tfs12] supports-[animation-timeline:view()]:[animation-range:entry_60%_exit_40%]"></div></div>
        <a href="#tfs-12-h" class="group inline-flex min-h-11 w-fit items-center gap-2 rounded-full bg-tfs12-ink px-6 text-sm font-semibold text-white transition hover:bg-tfs12-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tfs12-acc">Start free <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 transition group-hover:translate-x-0.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
      </div>
    </div>
    <ol class="grid gap-6 [view-timeline-name:--tfs12]">
      <li class="grid gap-5 rounded-3xl bg-white p-7 shadow-[0_20px_50px_-30px_rgb(20_40_30/0.3)] ring-1 ring-tfs12-line supports-[animation-timeline:view()]:animate-tfs12-focus supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_10%_cover_40%] motion-reduce:animate-none sm:p-9">
        <div class="flex items-center gap-4"><span class="font-tfs12-display text-5xl font-bold text-tfs12-line">01</span><span class="grid size-11 place-items-center rounded-2xl bg-tfs12-acc/10 text-tfs12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/></svg></span></div>
        <h3 class="font-tfs12-display text-2xl font-semibold">Connect a source</h3>
        <p class="text-pretty text-tfs12-mut">Paste a read-only warehouse URL or install the Segment destination. Ranger maps your schema in seconds.</p>
        <p class="inline-flex w-fit items-center gap-2 rounded-full bg-sky-100 text-sky-800 px-3 py-1.5 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg>Schema mapped · 214 tables</p>
      </li>
      <li class="grid gap-5 rounded-3xl bg-white p-7 shadow-[0_20px_50px_-30px_rgb(20_40_30/0.3)] ring-1 ring-tfs12-line supports-[animation-timeline:view()]:animate-tfs12-focus supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_10%_cover_40%] motion-reduce:animate-none sm:p-9">
        <div class="flex items-center gap-4"><span class="font-tfs12-display text-5xl font-bold text-tfs12-line">02</span><span class="grid size-11 place-items-center rounded-2xl bg-tfs12-acc/10 text-tfs12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg></span></div>
        <h3 class="font-tfs12-display text-2xl font-semibold">Pick a template</h3>
        <p class="text-pretty text-tfs12-mut">Activation, retention or revenue — templates come pre-wired to the events you already send.</p>
        <p class="inline-flex w-fit items-center gap-2 rounded-full bg-violet-100 text-violet-800 px-3 py-1.5 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg>Retention template applied</p>
      </li>
      <li class="grid gap-5 rounded-3xl bg-white p-7 shadow-[0_20px_50px_-30px_rgb(20_40_30/0.3)] ring-1 ring-tfs12-line supports-[animation-timeline:view()]:animate-tfs12-focus supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_10%_cover_40%] motion-reduce:animate-none sm:p-9">
        <div class="flex items-center gap-4"><span class="font-tfs12-display text-5xl font-bold text-tfs12-line">03</span><span class="grid size-11 place-items-center rounded-2xl bg-tfs12-acc/10 text-tfs12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg></span></div>
        <h3 class="font-tfs12-display text-2xl font-semibold">Invite the team</h3>
        <p class="text-pretty text-tfs12-mut">Share a live board. Comments thread onto the exact data point they reference.</p>
        <p class="inline-flex w-fit items-center gap-2 rounded-full bg-amber-100 text-amber-800 px-3 py-1.5 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg>6 teammates joined</p>
      </li>
      <li class="grid gap-5 rounded-3xl bg-white p-7 shadow-[0_20px_50px_-30px_rgb(20_40_30/0.3)] ring-1 ring-tfs12-line supports-[animation-timeline:view()]:animate-tfs12-focus supports-[animation-timeline:view()]:[animation-timeline:view()] supports-[animation-timeline:view()]:[animation-range:entry_10%_cover_40%] motion-reduce:animate-none sm:p-9">
        <div class="flex items-center gap-4"><span class="font-tfs12-display text-5xl font-bold text-tfs12-line">04</span><span class="grid size-11 place-items-center rounded-2xl bg-tfs12-acc/10 text-tfs12-acc"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></span></div>
        <h3 class="font-tfs12-display text-2xl font-semibold">Get the alert</h3>
        <p class="text-pretty text-tfs12-mut">Ranger watches every metric and pings Slack the moment one moves outside its band.</p>
        <p class="inline-flex w-fit items-center gap-2 rounded-full bg-emerald-100 text-emerald-800 px-3 py-1.5 text-sm font-medium"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4"><path d="M20 6 9 17l-5-5"/></svg>Activation ↑ 12% this week</p>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs12-bg: #f4f6f1;
  --color-tfs12-bg: oklch(0.97 0.007 124);
  --color-tfs12-ink: #16241b;
  --color-tfs12-ink: oklch(0.244 0.026 156);
  --color-tfs12-mut: #4d5b52;
  --color-tfs12-mut: oklch(0.456 0.023 157);
  --color-tfs12-line: #dde4d9;
  --color-tfs12-line: oklch(0.91 0.017 134);
  --color-tfs12-acc: #16a34a;
  --color-tfs12-acc: oklch(0.627 0.17 149);
  --font-tfs12-display: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tfs12-sans: 'Geist', system-ui, sans-serif;
  --animate-tfs12-rail: tfs12-rail linear both;
  --animate-tfs12-focus: tfs12-focus linear both;

  @keyframes tfs12-rail {
    from {
      transform: scaleX(0.04);
    }

    to {
      transform: scaleX(1);
    }
  }

  @keyframes tfs12-focus {
    from {
      opacity: 0.25;
      transform: translateY(40px) scale(0.96);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-12 {
  width: 100%;
  min-height: 100svh;
}

@media (prefers-reduced-motion: reduce) {
  .tfs-12 * {
    animation: none !important;
  }
}
```
