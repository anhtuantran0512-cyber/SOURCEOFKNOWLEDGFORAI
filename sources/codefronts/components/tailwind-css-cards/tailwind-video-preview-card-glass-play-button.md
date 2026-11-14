---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-video-preview-card-glass-play-button/"
title: "Tailwind Video Preview Card with Glass Play Button"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A video shelf card: 16:9 thumbnail, glass play button with a breathing ring, LIVE and 4K pills, a watch-progress bar, and a creator row with subscriber delta."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Video Preview Card with Glass Play Button
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-video-preview-card-glass-play-button/

A video shelf card: 16:9 thumbnail, glass play button with a breathing ring, LIVE and 4K pills, a watch-progress bar, and a creator row with subscriber delta. The port's win is that three infinite animations become three animate-* utilities minted from @theme, each carrying its own motion-reduce:animate-none beside it.
## HTML
```html
<section class="twc-09 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc09-bg [background-image:radial-gradient(ellipse_at_20%_20%,oklch(0.68_0.2_350/0.06),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.6_0.2_295/0.06),transparent_50%)] font-twc09-sans">

  <article class="group/card relative isolate w-full max-w-[380px] overflow-hidden rounded-[22px] bg-white border border-black/5 shadow-[0_30px_60px_-30px_oklch(0.35_0.15_320/0.24),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow] duration-300 hover:-translate-y-[3px] hover:shadow-[0_40px_80px_-30px_oklch(0.35_0.15_320/0.34)] motion-reduce:transition-none motion-reduce:hover:translate-y-0">

    <div aria-hidden="true" class="absolute -top-20 -right-20 size-65 -z-10 pointer-events-none blur-[30px] [background:radial-gradient(circle,oklch(0.68_0.2_350/0.18)_0%,transparent_55%),radial-gradient(circle_at_30%_30%,oklch(0.6_0.2_295/0.16)_0%,transparent_55%)]"></div>

    <a href="#play" aria-label="Play video: Building Container Queries in 8 Minutes" class="relative block w-full aspect-video overflow-hidden no-underline rounded-t-[22px] focus-visible:outline-2 focus-visible:outline-twc09-acc focus-visible:outline-offset-[-2px]">
      <img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?w=800&q=80&auto=format&fit=crop" alt="CSS Container Queries tutorial" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-[transform,filter] duration-600 ease-out group-hover/card:scale-105 group-hover/card:brightness-110 group-hover/card:saturate-110 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
      <div aria-hidden="true" class="absolute inset-0 pointer-events-none [background:linear-gradient(180deg,oklch(0_0_0/0.15)_0%,oklch(0_0_0/0.4)_100%)]"></div>
      <div aria-hidden="true" class="absolute top-[40%] left-1/2 -translate-x-1/2 -translate-y-1/2 w-3/5 h-3/5 pointer-events-none transition-opacity duration-350 group-hover/card:opacity-70 [background:radial-gradient(ellipse,oklch(1_0_0/0.2),transparent_70%)]"></div>

      <span class="absolute top-3 left-3 inline-flex items-center gap-1.5 px-2 py-1 rounded-md bg-twc09-red/95 text-white font-twc09-mono text-[9.5px] font-extrabold tracking-[0.14em] shadow-[0_4px_12px_oklch(0.58_0.22_25/0.35)]">
        <span aria-hidden="true" class="size-[5px] rounded-full bg-white animate-twc09-blink motion-reduce:animate-none"></span>
        LIVE
      </span>
      <span class="absolute top-3 right-3 px-[7px] py-[3px] rounded-[5px] bg-black/72 backdrop-blur-[6px] border border-white/15 text-white font-twc09-mono text-[9.5px] font-extrabold tracking-[0.06em]">4K</span>

      <span aria-hidden="true" class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex items-center justify-center size-14 rounded-full bg-black/60 backdrop-blur-[8px] border-[1.5px] border-white/28 shadow-[0_8px_24px_oklch(0_0_0/0.35)] transition-[transform,background,box-shadow] duration-250 ease-[cubic-bezier(0.34,1.2,0.64,1)] group-hover/card:scale-108 group-hover/card:bg-twc09-acc/80 group-hover/card:shadow-[0_12px_32px_oklch(0.68_0.2_350/0.45)] motion-reduce:transition-[background] motion-reduce:group-hover/card:scale-100">
        <span class="absolute -inset-1.5 rounded-full border-[1.5px] border-white/20 animate-twc09-ring motion-reduce:animate-none"></span>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="#fff" class="ml-[3px]" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
      </span>

      <div aria-hidden="true" class="absolute bottom-0 inset-x-0 px-3 pb-2 pointer-events-none [background:linear-gradient(180deg,transparent_0%,oklch(0_0_0/0.6)_100%)]">
        <div class="h-[3px] mb-1.5 rounded-sm overflow-hidden bg-white/16">
          <span class="block w-[42%] h-full rounded-sm [background:linear-gradient(90deg,#ec4899,#f472b6)]"></span>
        </div>
        <div class="flex items-center justify-between text-white">
          <span class="inline-flex items-center gap-1 text-[10px] font-bold tracking-[0.02em]">
            <span class="size-[5px] rounded-full bg-twc09-green shadow-[0_0_6px_oklch(0.78_0.14_165)] animate-twc09-pulse motion-reduce:animate-none"></span>
            2.4k watching
          </span>
          <span class="font-twc09-mono text-[10.5px] font-bold tracking-[0.02em]">12:47</span>
        </div>
      </div>
    </a>

    <div class="relative z-1 px-4 py-3.5">
      <span class="inline-block mb-2 px-2 py-0.5 rounded-full font-twc09-mono text-[9.5px] font-bold tracking-[0.14em] uppercase text-twc09-indigoink bg-twc09-indigo/8 border border-twc09-indigo/16">CSS &middot; Tutorial</span>
      <h3 class="m-0 mb-3 text-[15px]/[1.3] font-bold tracking-[-0.015em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Building Container Queries in 8 Minutes</h3>

      <div class="grid grid-cols-[36px_1fr_auto] items-center gap-2.5 mb-3">
        <span aria-hidden="true" class="relative flex items-center justify-center size-9 rounded-full border-2 border-white [background:linear-gradient(135deg,#ec4899,#f97316)] text-white text-xs font-extrabold shadow-[0_2px_6px_oklch(0_0_0/0.1)]">
          JC
          <span class="absolute -bottom-[3px] -right-[3px] flex items-center justify-center size-3.5 rounded-full bg-twc09-blue border-[1.5px] border-white">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          </span>
        </span>
        <div class="flex flex-col gap-px min-w-0">
          <span class="inline-flex items-center gap-1">
            <span class="text-[13px] font-bold tracking-[-0.01em] text-twc09-ink">Josh Comeau</span>
            <svg role="img" aria-label="Verified creator" width="12" height="12" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>
          <span class="text-[11px] text-twc09-muted truncate">128k subscribers &middot; <span class="font-twc09-mono text-[10.5px] font-bold text-twc09-greenink">+2.1k this week</span></span>
        </div>
        <button type="button" aria-label="Save video" class="inline-flex items-center justify-center size-11 rounded-[10px] bg-transparent border border-black/6 text-twc09-muted cursor-pointer transition-[color,background,border-color,transform] duration-200 hover:text-twc09-acc hover:bg-twc09-acc/6 hover:border-twc09-acc/25 hover:-translate-y-px focus-visible:outline-2 focus-visible:outline-twc09-acc focus-visible:outline-offset-2 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
        </button>
      </div>

      <div class="flex items-center justify-between gap-3 pt-2.5 border-t border-black/5">
        <div class="flex gap-2.5">
          <span class="inline-flex items-center gap-1 text-[11.5px] font-bold text-twc09-ink2 [font-variant-numeric:tabular-nums]">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc09-dim"><polygon points="12 2 15 9 22 9 17 14 19 21 12 17 5 21 7 14 2 9 9 9"/></svg>
            8.2k
          </span>
          <span class="inline-flex items-center gap-1 text-[11.5px] font-bold text-twc09-ink2 [font-variant-numeric:tabular-nums]">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc09-dim"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            342
          </span>
          <span class="inline-flex items-center gap-1 text-[11.5px] font-bold text-twc09-ink2 [font-variant-numeric:tabular-nums]">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="flex-none text-twc09-dim"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/><line x1="15.4" y1="6.5" x2="8.6" y2="10.5"/></svg>
            892
          </span>
        </div>
        <div class="flex items-center gap-1 text-[11px] text-twc09-dim">
          <time datetime="2026-07-05">Jul 5</time>
          <span aria-hidden="true" class="text-twc09-hair">&middot;</span>
          <span>24.7k views</span>
        </div>
      </div>
    </div>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc09-bg: #f8f7f4;
  --color-twc09-bg: oklch(0.97 0.005 90);
  --color-twc09-ink: #1a1a1a;
  --color-twc09-ink: oklch(0.21 0.005 270);
  --color-twc09-ink2: #4b4b57;
  --color-twc09-ink2: oklch(0.4 0.015 280);
  --color-twc09-muted: #6b6b7c;
  --color-twc09-muted: oklch(0.51 0.02 285);
  --color-twc09-dim: #9ca3af;
  --color-twc09-dim: oklch(0.71 0.02 265);
  --color-twc09-hair: #cbd5e1;
  --color-twc09-hair: oklch(0.85 0.02 250);
  --color-twc09-acc: #ec4899;
  --color-twc09-acc: oklch(0.68 0.2 350);
  --color-twc09-red: #dc2626;
  --color-twc09-red: oklch(0.58 0.22 25);
  --color-twc09-green: #34d399;
  --color-twc09-green: oklch(0.78 0.14 165);
  --color-twc09-greenink: #059669;
  --color-twc09-greenink: oklch(0.56 0.13 163);
  --color-twc09-blue: #3b82f6;
  --color-twc09-blue: oklch(0.62 0.17 255);
  --color-twc09-indigo: #6366f1;
  --color-twc09-indigo: oklch(0.55 0.2 275);
  --color-twc09-indigoink: #4338ca;
  --color-twc09-indigoink: oklch(0.42 0.21 275);
  --font-twc09-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc09-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --animate-twc09-blink: twc09-blink 1.4s ease-in-out infinite;
  --animate-twc09-ring: twc09-ring 2.4s ease-in-out infinite;
  --animate-twc09-pulse: twc09-pulse 2s ease-in-out infinite;
}
/* Three keyframe blocks, three @theme entries: the blocks stay CSS because
   keyframes are not utilities, the entries mint animate-twc09-* so each
   element can pair its animation with motion-reduce:animate-none inline. */

@keyframes twc09-blink {
  0%,
    100% {
    opacity: 1;
    transform: scale(1);
  }

  50% {
    opacity: 0.5;
    transform: scale(0.85);
  }
}

@keyframes twc09-ring {
  0%,
    100% {
    transform: scale(1);
    opacity: 0.5;
  }

  50% {
    transform: scale(1.15);
    opacity: 0.1;
  }
}

@keyframes twc09-pulse {
  0%,
    100% {
    transform: scale(1);
    box-shadow: 0 0 6px #34d399;
  }

  50% {
    transform: scale(1.3);
    box-shadow: 0 0 10px #34d399;
  }
}

.twc-09 {
  width: 100%;
  min-height: 100svh;
}
```
