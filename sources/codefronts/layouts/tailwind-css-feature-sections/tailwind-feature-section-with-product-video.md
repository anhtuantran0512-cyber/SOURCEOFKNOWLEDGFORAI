---
source: "codefronts"
url: "https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-product-video/"
title: "Tailwind Feature Section with Product Video"
section: "layouts"
category: "tailwind-css-feature-sections"
category_name: "Tailwind CSS Feature Sections"
description: "A product-demo player with synced chapters: a 12-second looping 'video' (three drawn scenes) plays beside a chapter list whose progress bars fill in lockstep."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Feature Section with Product Video
Source: https://codefronts.com/layouts/tailwind-css-feature-sections/tailwind-feature-section-with-product-video/

A product-demo player with synced chapters: a 12-second looping 'video' (three drawn scenes) plays beside a chapter list whose progress bars fill in lockstep. Play/pause is a checkbox read by group-has-checked/player:, which sets animation-play-state: paused on every moving part — one toggle, zero JavaScript.
## HTML
```html
<section class="tfs-05 w-full min-h-svh bg-tfs05-bg px-5 py-20 font-tfs05-sans text-white antialiased sm:py-28" aria-labelledby="tfs-05-h">
  <div class="mx-auto grid w-full max-w-6xl gap-12">
    <header class="mx-auto grid max-w-2xl gap-4 text-center">
      <p class="mx-auto inline-flex items-center gap-2 rounded-full bg-white/5 px-3 py-1 text-xs font-medium text-tfs05-acc ring-1 ring-white/10"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-3 fill-current"><path d="M6 4l14 8-14 8z"/></svg>2-minute demo, in 12 seconds</p>
      <h2 id="tfs-05-h" class="text-balance text-4xl font-semibold tracking-tight sm:text-5xl">Watch Orbit plan a sprint</h2>
    </header>
    <div class="group/player grid gap-6 lg:grid-cols-[1.6fr_1fr]">
      <div class="relative overflow-hidden rounded-3xl bg-tfs05-card shadow-[0_40px_120px_-40px_var(--color-tfs05-acc)] ring-1 ring-white/10">
        <div class="relative aspect-video">
          <div class="absolute inset-0 grid place-items-center bg-[radial-gradient(circle_at_30%_30%,color-mix(in_oklab,var(--color-tfs05-acc)_35%,transparent),transparent_60%)] p-[8%] opacity-0 animate-tfs05-scene motion-reduce:animate-none motion-reduce:opacity-100 group-has-checked/player:[animation-play-state:paused]">
            <div class="grid w-full gap-2 rounded-2xl bg-white/95 p-4 text-tfs05-bg shadow-2xl"><p class="text-xs font-semibold text-slate-500">Backlog · 42 issues</p><div class="h-2.5 w-[80%] rounded bg-slate-200"></div><div class="h-2.5 w-[64%] rounded bg-slate-200"></div><div class="h-2.5 w-[72%] rounded bg-violet-300"></div><div class="h-2.5 w-[50%] rounded bg-slate-200"></div></div>
          </div>
          <div class="absolute inset-0 grid place-items-center bg-[radial-gradient(circle_at_70%_30%,color-mix(in_oklab,var(--color-tfs05-acc2)_35%,transparent),transparent_60%)] p-[8%] opacity-0 animate-tfs05-scene [animation-delay:4s] motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]">
            <div class="grid w-full grid-cols-3 gap-3"><div class="grid gap-2 rounded-xl bg-white/10 p-3"><p class="text-[10px] font-semibold text-white/70">Todo</p><i class="h-8 rounded-md bg-white/90"></i><i class="h-8 rounded-md bg-white/90"></i></div><div class="grid gap-2 rounded-xl bg-white/10 p-3"><p class="text-[10px] font-semibold text-white/70">Doing</p><i class="h-8 rounded-md bg-tfs05-acc"></i></div><div class="grid gap-2 rounded-xl bg-white/10 p-3"><p class="text-[10px] font-semibold text-white/70">Done</p><i class="h-8 rounded-md bg-emerald-400"></i><i class="h-8 rounded-md bg-emerald-400"></i></div></div>
          </div>
          <div class="absolute inset-0 grid place-items-center p-[8%] opacity-0 animate-tfs05-scene [animation-delay:8s] motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]">
            <div class="grid justify-items-center gap-3 text-center"><span class="grid size-16 place-items-center rounded-full bg-emerald-400 text-tfs05-bg shadow-[0_0_60px_var(--color-emerald-400)]"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-8"><path d="M20 6 9 17l-5-5"/></svg></span><p class="text-2xl font-semibold">Sprint 24 planned</p><p class="text-sm text-white/70">18 issues · 34 points · 3 owners</p></div>
          </div>
        </div>
        <div class="flex items-center gap-3 border-t border-white/10 bg-black/30 px-4 py-3 backdrop-blur">
          <label class="grid size-11 cursor-pointer place-items-center rounded-full bg-white text-tfs05-bg transition hover:scale-105 has-focus-visible:outline-2 has-focus-visible:outline-offset-2 has-focus-visible:outline-tfs05-acc">
            <input type="checkbox" class="sr-only" aria-label="Pause demo">
            <span class="group-has-checked/player:hidden"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 fill-current"><path d="M7 4h3v16H7zM14 4h3v16h-3z"/></svg></span><span class="hidden group-has-checked/player:block"><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 fill-current"><path d="M6 4l14 8-14 8z"/></svg></span>
          </label>
          <div class="relative h-1 flex-1 overflow-hidden rounded-full bg-white/15"><div class="absolute inset-0 origin-left scale-x-0 rounded-full bg-tfs05-acc animate-tfs05-track motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]"></div></div>
          <span class="font-mono text-xs text-white/70">0:12</span>
        </div>
      </div>
      <ol class="grid content-center gap-3">
        <li class="grid gap-3 rounded-2xl bg-white/5 p-5 ring-1 ring-white/10"><div class="flex items-baseline gap-3"><span class="font-mono text-xs text-tfs05-acc">01</span><h3 class="font-semibold">Triage the backlog</h3></div><p class="text-sm text-tfs05-mut">AI ranks 42 issues by impact and effort.</p><div class="h-1 overflow-hidden rounded-full bg-white/10"><div class="h-full origin-left scale-x-0 bg-tfs05-acc animate-tfs05-bar motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]"></div></div></li>
        <li class="grid gap-3 rounded-2xl bg-white/5 p-5 ring-1 ring-white/10"><div class="flex items-baseline gap-3"><span class="font-mono text-xs text-tfs05-acc">02</span><h3 class="font-semibold">Drag into the board</h3></div><p class="text-sm text-tfs05-mut">Capacity updates live as you assign.</p><div class="h-1 overflow-hidden rounded-full bg-white/10"><div class="h-full origin-left scale-x-0 bg-tfs05-acc animate-tfs05-bar [animation-delay:4s] motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]"></div></div></li>
        <li class="grid gap-3 rounded-2xl bg-white/5 p-5 ring-1 ring-white/10"><div class="flex items-baseline gap-3"><span class="font-mono text-xs text-tfs05-acc">03</span><h3 class="font-semibold">Ship the plan</h3></div><p class="text-sm text-tfs05-mut">Owners notified, calendars blocked.</p><div class="h-1 overflow-hidden rounded-full bg-white/10"><div class="h-full origin-left scale-x-0 bg-tfs05-acc animate-tfs05-bar [animation-delay:8s] motion-reduce:hidden group-has-checked/player:[animation-play-state:paused]"></div></div></li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tfs05-bg: #0c0a1d;
  --color-tfs05-bg: oklch(0.16 0.039 286);
  --color-tfs05-card: #151230;
  --color-tfs05-card: oklch(0.205 0.058 285);
  --color-tfs05-mut: #b4afd6;
  --color-tfs05-mut: oklch(0.771 0.055 291);
  --color-tfs05-acc: #a78bfa;
  --color-tfs05-acc: oklch(0.709 0.159 294);
  --color-tfs05-acc2: #22d3ee;
  --color-tfs05-acc2: oklch(0.797 0.134 212);
  --font-tfs05-sans: 'Sora', system-ui, sans-serif;
  --animate-tfs05-scene: tfs05-scene 12s linear infinite backwards;
  --animate-tfs05-bar: tfs05-bar 12s linear infinite backwards;
  --animate-tfs05-track: tfs05-track 12s linear infinite;

  @keyframes tfs05-scene {
    0% {
      opacity: 0;
      transform: scale(1.03);
    }

    3%,
        30% {
      opacity: 1;
      transform: none;
    }

    33.33%,
        100% {
      opacity: 0;
    }
  }

  @keyframes tfs05-bar {
    0% {
      transform: scaleX(0);
    }

    33.33% {
      transform: scaleX(1);
    }

    33.34%,
        100% {
      transform: scaleX(0);
    }
  }

  @keyframes tfs05-track {
    from {
      transform: scaleX(0);
    }

    to {
      transform: scaleX(1);
    }
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tfs-05 {
  width: 100%;
  min-height: 100svh;
}
```
