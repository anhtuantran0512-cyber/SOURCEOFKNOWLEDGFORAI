---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-tabs-sliding-pill-indicator/"
title: "Tailwind Tabs with Animated Sliding Pill Indicator"
section: "navigation"
category: "tailwind-css-mobile-navbar"
category_name: "Tailwind CSS Mobile Navbars & Menus"
description: "A dark music-app segmented control whose pill glides between four tabs and changes colour per section, with pages that fade-lift into place and a mini player…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Tabs with Animated Sliding Pill Indicator
Source: https://codefronts.com/navigation/tailwind-css-mobile-navbar/tailwind-tabs-sliding-pill-indicator/

A dark music-app segmented control whose pill glides between four tabs and changes colour per section, with pages that fade-lift into place and a mini player docked at the bottom. The port moves the pill with GPU translate instead of animating left and width. Zero JavaScript.
## HTML
```html
<section class="tmn-08 w-full min-h-svh grid place-items-center bg-tmn08-stage px-4 py-6 font-tmn08-sans antialiased" aria-label="Tailwind tabs with sliding pill indicator demo">
  <div class="group relative h-[min(667px,calc(100svh-3rem))] w-full max-w-[375px] overflow-hidden rounded-[2.25rem] bg-tmn08-bg text-tmn08-ink shadow-[0_40px_100px_-30px_oklch(0_0_0/0.9)] ring-1 ring-white/8">
    <input type="radio" name="tmn-08-tab" id="tmn-08-t1" class="sr-only" checked>
    <input type="radio" name="tmn-08-tab" id="tmn-08-t2" class="sr-only">
    <input type="radio" name="tmn-08-tab" id="tmn-08-t3" class="sr-only">
    <input type="radio" name="tmn-08-tab" id="tmn-08-t4" class="sr-only">

    <header class="flex items-center justify-between px-5 pt-7">
      <p class="bg-linear-to-r from-tmn08-c1 to-tmn08-c3 bg-clip-text text-[22px] font-extrabold tracking-[-0.03em] text-transparent">Wavify</p>
      <button type="button" class="relative grid size-11 place-items-center rounded-full border border-tmn08-line bg-tmn08-surface after:absolute after:top-2.5 after:right-3 after:size-2 after:rounded-full after:bg-red-500 after:ring-2 after:ring-tmn08-surface after:content-['']"><span class="sr-only">Notifications (new)</span><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg></button>
    </header>

    <div role="radiogroup" aria-label="Section" class="relative mx-4 my-5 flex rounded-[20px] border border-tmn08-line bg-tmn08-surface p-1">
      <span aria-hidden="true" class="absolute inset-y-1 left-1 w-[calc((100%-8px)/4)] rounded-2xl bg-tmn08-c1 transition-[translate,background-color] duration-350 ease-[cubic-bezier(.4,0,.2,1)] group-has-[#tmn-08-t2:checked]:translate-x-full group-has-[#tmn-08-t2:checked]:bg-tmn08-c2 group-has-[#tmn-08-t3:checked]:translate-x-[200%] group-has-[#tmn-08-t3:checked]:bg-tmn08-c3 group-has-[#tmn-08-t4:checked]:translate-x-[300%] group-has-[#tmn-08-t4:checked]:bg-tmn08-c4"></span>
      <label for="tmn-08-t1" class="relative z-[1] flex min-h-13 flex-1 cursor-pointer flex-col items-center justify-center gap-0.5 rounded-2xl text-[10px] font-bold tracking-[0.06em] text-tmn08-mut uppercase transition-colors group-has-[#tmn-08-t1:checked]:text-tmn08-bg group-has-[#tmn-08-t1:focus-visible]:ring-2 group-has-[#tmn-08-t1:focus-visible]:ring-white"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>Music</label>
      <label for="tmn-08-t2" class="relative z-[1] flex min-h-13 flex-1 cursor-pointer flex-col items-center justify-center gap-0.5 rounded-2xl text-[10px] font-bold tracking-[0.06em] text-tmn08-mut uppercase transition-colors group-has-[#tmn-08-t2:checked]:text-tmn08-bg group-has-[#tmn-08-t2:focus-visible]:ring-2 group-has-[#tmn-08-t2:focus-visible]:ring-white"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0M12 17v5"/></svg>Pods</label>
      <label for="tmn-08-t3" class="relative z-[1] flex min-h-13 flex-1 cursor-pointer flex-col items-center justify-center gap-0.5 rounded-2xl text-[10px] font-bold tracking-[0.06em] text-tmn08-mut uppercase transition-colors group-has-[#tmn-08-t3:checked]:text-tmn08-bg group-has-[#tmn-08-t3:focus-visible]:ring-2 group-has-[#tmn-08-t3:focus-visible]:ring-white"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8a6 6 0 0 1 0 8.4M7.8 16.2a6 6 0 0 1 0-8.4M19 5a10 10 0 0 1 0 14M5 19A10 10 0 0 1 5 5"/></svg>Radio</label>
      <label for="tmn-08-t4" class="relative z-[1] flex min-h-13 flex-1 cursor-pointer flex-col items-center justify-center gap-0.5 rounded-2xl text-[10px] font-bold tracking-[0.06em] text-tmn08-mut uppercase transition-colors group-has-[#tmn-08-t4:checked]:text-tmn08-bg group-has-[#tmn-08-t4:focus-visible]:ring-2 group-has-[#tmn-08-t4:focus-visible]:ring-white"><svg viewBox="0 0 24 24" class="size-5" aria-hidden="true"><path d="M4 4v16M9 4v16M14 4l6 16"/></svg>Library</label>
    </div>

    <div class="absolute inset-x-0 top-[170px] bottom-[84px]">
      <div class="invisible absolute inset-0 translate-y-2.5 overflow-y-auto px-4 opacity-0 transition duration-300 group-has-[#tmn-08-t1:checked]:visible group-has-[#tmn-08-t1:checked]:translate-y-0 group-has-[#tmn-08-t1:checked]:opacity-100">
        <h2 class="mb-3 text-xl font-bold tracking-[-0.02em]">Trending now</h2>
        <a href="#" class="mb-2.5 flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3 transition-colors hover:border-tmn08-c1/50"><span class="size-12 flex-none rounded-xl bg-linear-135 from-cyan-400 to-indigo-500"></span><span class="flex-1"><span class="block text-sm font-semibold">Neon Lights</span><span class="block text-xs text-tmn08-mut">Synthwave Collective · 3:42</span></span><span class="text-lg text-tmn08-mut" aria-hidden="true">⋯</span></a>
        <a href="#" class="mb-2.5 flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3 transition-colors hover:border-tmn08-c1/50"><span class="size-12 flex-none rounded-xl bg-linear-135 from-orange-400 to-rose-500"></span><span class="flex-1"><span class="block text-sm font-semibold">Midnight Drive</span><span class="block text-xs text-tmn08-mut">Neon Atlas · 4:18</span></span><span class="text-lg text-tmn08-mut" aria-hidden="true">⋯</span></a>
        <a href="#" class="flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3 transition-colors hover:border-tmn08-c1/50"><span class="size-12 flex-none rounded-xl bg-linear-135 from-violet-400 to-pink-500"></span><span class="flex-1"><span class="block text-sm font-semibold">Electric Dream</span><span class="block text-xs text-tmn08-mut">Pixel Sound · 5:01</span></span><span class="text-lg text-tmn08-mut" aria-hidden="true">⋯</span></a>
      </div>
      <div class="invisible absolute inset-0 translate-y-2.5 overflow-y-auto px-4 opacity-0 transition duration-300 group-has-[#tmn-08-t2:checked]:visible group-has-[#tmn-08-t2:checked]:translate-y-0 group-has-[#tmn-08-t2:checked]:opacity-100">
        <h2 class="mb-3 text-xl font-bold tracking-[-0.02em]">Popular podcasts</h2>
        <div class="grid grid-cols-2 gap-2.5">
          <a href="#" class="rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="mb-2.5 block aspect-square rounded-xl bg-[radial-gradient(circle_at_30%_30%,#fb923c,#7c2d12)]"></span><span class="block text-[13px] font-semibold">Deep Dives</span><span class="block text-[11px] text-tmn08-mut">128 episodes</span></a>
          <a href="#" class="rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="mb-2.5 block aspect-square rounded-xl bg-[radial-gradient(circle_at_70%_30%,#fde047,#a16207)]"></span><span class="block text-[13px] font-semibold">Tech Talks</span><span class="block text-[11px] text-tmn08-mut">84 episodes</span></a>
          <a href="#" class="rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="mb-2.5 block aspect-square rounded-xl bg-[radial-gradient(circle_at_30%_70%,#38bdf8,#1e3a8a)]"></span><span class="block text-[13px] font-semibold">World News</span><span class="block text-[11px] text-tmn08-mut">312 episodes</span></a>
          <a href="#" class="rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="mb-2.5 block aspect-square rounded-xl bg-[radial-gradient(circle_at_70%_70%,#f472b6,#831843)]"></span><span class="block text-[13px] font-semibold">Interviews</span><span class="block text-[11px] text-tmn08-mut">56 episodes</span></a>
        </div>
      </div>
      <div class="invisible absolute inset-0 translate-y-2.5 overflow-y-auto px-4 opacity-0 transition duration-300 group-has-[#tmn-08-t3:checked]:visible group-has-[#tmn-08-t3:checked]:translate-y-0 group-has-[#tmn-08-t3:checked]:opacity-100">
        <h2 class="mb-3 text-xl font-bold tracking-[-0.02em]">Live radio</h2>
        <a href="#" class="mb-2.5 flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="size-12 flex-none rounded-xl bg-linear-135 from-violet-400 to-violet-700"></span><span class="flex-1"><span class="block text-sm font-semibold">Synthwave FM</span><span class="flex items-center gap-1.5 text-xs text-tmn08-mut"><span class="size-1.5 rounded-full bg-red-500 animate-pulse"></span>Live · 2.4k listening</span></span><svg viewBox="0 0 24 24" class="size-5 fill-current" aria-hidden="true"><path d="m7 4 13 8-13 8z"/></svg></a>
        <a href="#" class="flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="size-12 flex-none rounded-xl bg-linear-135 from-green-400 to-green-700"></span><span class="flex-1"><span class="block text-sm font-semibold">Chill Beats</span><span class="flex items-center gap-1.5 text-xs text-tmn08-mut"><span class="size-1.5 rounded-full bg-red-500 animate-pulse"></span>Live · 8.1k listening</span></span><svg viewBox="0 0 24 24" class="size-5 fill-current" aria-hidden="true"><path d="m7 4 13 8-13 8z"/></svg></a>
      </div>
      <div class="invisible absolute inset-0 translate-y-2.5 overflow-y-auto px-4 opacity-0 transition duration-300 group-has-[#tmn-08-t4:checked]:visible group-has-[#tmn-08-t4:checked]:translate-y-0 group-has-[#tmn-08-t4:checked]:opacity-100">
        <h2 class="mb-3 text-xl font-bold tracking-[-0.02em]">Your library</h2>
        <a href="#" class="mb-2.5 flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="grid size-12 flex-none place-items-center rounded-xl bg-linear-135 from-green-400 to-cyan-500 text-tmn08-bg"><svg viewBox="0 0 24 24" class="size-5 fill-current" aria-hidden="true"><path d="M12 21s-8-4.5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 6.5-8 11-8 11z"/></svg></span><span class="flex-1"><span class="block text-sm font-semibold">Liked songs</span><span class="block text-xs text-tmn08-mut">248 tracks</span></span><svg viewBox="0 0 24 24" class="size-4 text-tmn08-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
        <a href="#" class="flex items-center gap-3.5 rounded-2xl border border-tmn08-line bg-tmn08-surface p-3"><span class="size-12 flex-none rounded-xl bg-linear-135 from-amber-400 to-red-500"></span><span class="flex-1"><span class="block text-sm font-semibold">My playlists</span><span class="block text-xs text-tmn08-mut">12 playlists</span></span><svg viewBox="0 0 24 24" class="size-4 text-tmn08-mut" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></a>
      </div>
    </div>

    <div class="absolute inset-x-3 bottom-3 flex h-[68px] items-center gap-3 overflow-hidden rounded-2xl bg-tmn08-surface/90 px-3 ring-1 ring-white/8 backdrop-blur-lg">
      <span class="size-11 flex-none rounded-lg bg-linear-135 from-cyan-400 to-indigo-500"></span>
      <span class="min-w-0 flex-1"><span class="block truncate text-[13px] font-semibold">Neon Lights</span><span class="block truncate text-[11px] text-tmn08-mut">Synthwave Collective</span></span>
      <button type="button" class="grid size-11 place-items-center rounded-full bg-tmn08-ink text-tmn08-bg"><span class="sr-only">Pause</span><svg viewBox="0 0 24 24" class="size-4.5 fill-current stroke-0" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg></button>
      <span aria-hidden="true" class="absolute inset-x-0 bottom-0 h-0.5 bg-white/10"><span class="block h-full w-2/5 bg-tmn08-c1"></span></span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tmn08-stage: #050506;
  --color-tmn08-stage: oklch(0.12 0.003 285);
  --color-tmn08-bg: #09090b;
  --color-tmn08-bg: oklch(0.14 0.005 285);
  --color-tmn08-surface: #18181b;
  --color-tmn08-surface: oklch(0.21 0.006 285);
  --color-tmn08-line: #27272a;
  --color-tmn08-line: oklch(0.27 0.006 286);
  --color-tmn08-ink: #fafafa;
  --color-tmn08-ink: oklch(0.985 0 0);
  --color-tmn08-mut: #a1a1aa;
  --color-tmn08-mut: oklch(0.71 0.013 286);
  --color-tmn08-c1: #22d3ee;
  --color-tmn08-c1: oklch(0.79 0.15 212);
  --color-tmn08-c2: #fb923c;
  --color-tmn08-c2: oklch(0.75 0.17 55);
  --color-tmn08-c3: #a78bfa;
  --color-tmn08-c3: oklch(0.71 0.16 293);
  --color-tmn08-c4: #4ade80;
  --color-tmn08-c4: oklch(0.8 0.18 152);
  --font-tmn08-sans: 'Bricolage Grotesque', system-ui, sans-serif;
}
/* Icon base: utilities (fill-current, stroke-0) still win because this sits in the base layer. */

@layer base {
  .tmn-08 svg {
    fill: none;
    stroke: currentColor;
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex: none;
  }
}
/* Root rule: the full-bleed contract, stated in CSS as well as in utilities, so the stage is
   sized before the browser build compiles. */

.tmn-08 {
  width: 100%;
  min-height: 100svh;
}
```
