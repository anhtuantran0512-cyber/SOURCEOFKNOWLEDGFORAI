---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-css-cards/tailwind-horizontal-article-card-feed/"
title: "Tailwind Horizontal Article Card Feed with Ranked Covers"
section: "components"
category: "tailwind-css-cards"
category_name: "Tailwind CSS Cards"
description: "A ranked three-article feed of landscape cards: a fixed cover column, then tags, headline, excerpt and an author row with inline actions."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Horizontal Article Card Feed with Ranked Covers
Source: https://codefronts.com/components/tailwind-css-cards/tailwind-horizontal-article-card-feed/

A ranked three-article feed of landscape cards: a fixed cover column, then tags, headline, excerpt and an author row with inline actions. The port's win is the gradient cover &mdash; three stacked paint layers that stay arbitrary properties, sitting directly on the element rather than in three look-alike modifier rules.
## HTML
```html
<section class="twc-07 w-full min-h-svh flex items-center justify-center px-5 py-9 bg-twc07-bg [background-image:radial-gradient(ellipse_at_20%_20%,oklch(0.6_0.2_295/0.06),transparent_50%),radial-gradient(ellipse_at_80%_80%,oklch(0.68_0.2_350/0.05),transparent_50%)] font-twc07-sans">
  <div class="w-full max-w-[640px] flex flex-col gap-3">

    <header class="flex max-[600px]:flex-col max-[600px]:items-start items-center justify-between gap-3 mb-1 px-1">
      <div class="flex items-center gap-2.5">
        <span aria-hidden="true" class="inline-flex items-center justify-center size-9 rounded-xl [background:linear-gradient(135deg,#a5b4fc,#7c3aed)] text-white shadow-[0_2px_8px_oklch(0.5_0.22_290/0.3)]">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        </span>
        <div>
          <h3 class="m-0 mb-px text-[15px] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">For you &middot; Engineering</h3>
          <p class="m-0 text-[10.5px] text-twc07-dim">Curated by editors &middot; updated 4h ago</p>
        </div>
      </div>
      <div role="group" aria-label="Filter feed" class="inline-flex p-[3px] rounded-full bg-twc07-track border border-black/4">
        <button type="button" aria-pressed="true" class="min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[10.5px] font-bold bg-white text-twc07-ink shadow-[0_2px_4px_oklch(0_0_0/0.06),0_0_0_1px_oklch(0_0_0/0.03)] transition-[color,background] duration-200 focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2 motion-reduce:transition-none">Trending</button>
        <button type="button" aria-pressed="false" class="min-h-11 px-3.5 rounded-full border-0 cursor-pointer text-[10.5px] font-bold bg-transparent text-twc07-muted transition-[color,background] duration-200 hover:text-twc07-ink focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2 motion-reduce:transition-none">New</button>
      </div>
    </header>

    <article class="group/card grid grid-cols-[132px_1fr] max-[600px]:grid-cols-1 overflow-hidden rounded-[18px] bg-white [background-image:linear-gradient(90deg,oklch(0.5_0.22_290/0.04)_0%,transparent_40%)] border border-twc07-acc/18 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-0.5 hover:border-twc07-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div aria-hidden="true" class="relative overflow-hidden max-[600px]:min-h-30 [background-image:radial-gradient(circle_at_30%_30%,oklch(1_0_0/0.15)_0%,transparent_45%),linear-gradient(135deg,#4c1d95_0%,#7c3aed_55%,#a855f7_100%)]">
        <div class="absolute inset-0 [background-image:conic-gradient(from_130deg_at_65%_40%,transparent_0deg,oklch(1_0_0/0.25)_60deg,transparent_130deg),radial-gradient(circle_at_75%_75%,oklch(0.68_0.2_350/0.5)_0%,transparent_55%)]"></div>
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-4/5 h-4/5 pointer-events-none [background:radial-gradient(ellipse,oklch(1_0_0/0.14),transparent_65%)]"></div>
        <span class="absolute top-2 left-2 px-[7px] py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 font-twc07-mono text-[9.5px] font-extrabold tracking-[0.02em] text-white">#1</span>
        <span class="absolute bottom-2 right-2 inline-flex items-center gap-1 px-1.5 py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 text-white text-[9.5px] font-bold">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          4 min
        </span>
      </div>
      <div class="flex flex-col gap-1.5 px-4 py-3.5">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="px-[7px] py-0.5 rounded-full font-twc07-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc07-accdeep bg-twc07-acc/8 border border-twc07-acc/15">Product Design</span>
          <span class="inline-flex items-center gap-1 px-[7px] py-0.5 rounded-full font-twc07-mono text-[9px] font-extrabold tracking-[0.12em] uppercase text-twc07-amberink [background:linear-gradient(180deg,#fef3c7,#fde68a)] border border-twc07-amberink/20 shadow-[0_1px_3px_oklch(0.78_0.15_70/0.2)]">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            EDITOR'S PICK
          </span>
        </div>
        <h3 class="m-0 text-[15px]/[1.3] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">The Case Against Perfect Loading States</h3>
        <p class="m-0 text-xs/[1.5] text-twc07-muted line-clamp-2">Skeleton screens promise smoothness but often teach users to distrust the interface. A quieter approach ships faster and reads more honest.</p>
        <div class="grid grid-cols-[26px_1fr_auto] items-center gap-2 mt-1.5 pt-2 border-t border-dashed border-black/10">
          <span aria-hidden="true" class="flex items-center justify-center size-6.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#a5b4fc,#7c3aed)] text-white text-[10px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.08)]">EK</span>
          <div class="flex flex-col min-w-0">
            <span class="inline-flex items-center gap-1 text-[11.5px] font-bold text-twc07-ink truncate">
              Emil Kowalski
              <svg role="img" aria-label="Verified author" width="11" height="11" viewBox="0 0 24 24" fill="none" class="flex-none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#3b82f6"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <time datetime="2026-07-05" class="text-[10px] text-twc07-dim">Jul 5 &middot; 42k reads</time>
          </div>
          <div class="flex gap-1">
            <button type="button" aria-label="Play audio version" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border border-black/6 text-twc07-muted cursor-pointer transition-[color,background,border-color] duration-200 hover:text-twc07-acc hover:bg-twc07-acc/6 hover:border-twc07-acc/20 focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
            </button>
            <button type="button" aria-label="Save article" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border border-black/6 text-twc07-muted cursor-pointer transition-[color,background,border-color] duration-200 hover:text-twc07-acc hover:bg-twc07-acc/6 hover:border-twc07-acc/20 focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>

    <article class="group/card grid grid-cols-[132px_1fr] max-[600px]:grid-cols-1 overflow-hidden rounded-[18px] bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-0.5 hover:border-twc07-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative overflow-hidden max-[600px]:min-h-30 [background-image:radial-gradient(circle_at_30%_30%,oklch(1_0_0/0.15)_0%,transparent_45%),linear-gradient(135deg,#075985_0%,#0891b2_55%,#22d3ee_100%)]">
        <img src="https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=600&q=80&auto=format&fit=crop" alt="CSS code in an editor" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-350 group-hover/card:scale-104 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
        <div aria-hidden="true" class="absolute inset-0 pointer-events-none [background:linear-gradient(180deg,transparent_0%,oklch(0_0_0/0.35)_100%)]"></div>
        <span class="absolute top-2 left-2 px-[7px] py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 font-twc07-mono text-[9.5px] font-extrabold tracking-[0.02em] text-white">#2</span>
        <span class="absolute bottom-2 right-2 inline-flex items-center gap-1 px-1.5 py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 text-white text-[9.5px] font-bold">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          8 min
        </span>
      </div>
      <div class="flex flex-col gap-1.5 px-4 py-3.5">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="px-[7px] py-0.5 rounded-full font-twc07-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc07-accdeep bg-twc07-acc/8 border border-twc07-acc/15">CSS</span>
          <span class="inline-flex items-center gap-0.5 px-1.5 py-0.5 rounded-full font-twc07-mono text-[9.5px] font-extrabold text-twc07-greenink bg-twc07-green/12 border border-twc07-green/22">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg>
            +12%
          </span>
        </div>
        <h3 class="m-0 text-[15px]/[1.3] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Container Queries Are Finally Ready</h3>
        <p class="m-0 text-xs/[1.5] text-twc07-muted line-clamp-2">The most-requested CSS feature landed everywhere. Here's what changes about the way we think about responsive design.</p>
        <div class="grid grid-cols-[26px_1fr_auto] items-center gap-2 mt-1.5 pt-2 border-t border-dashed border-black/10">
          <span aria-hidden="true" class="flex items-center justify-center size-6.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#67e8f9,#0891b2)] text-white text-[10px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.08)]">JC</span>
          <div class="flex flex-col min-w-0">
            <span class="text-[11.5px] font-bold text-twc07-ink truncate">Josh Comeau</span>
            <time datetime="2026-07-02" class="text-[10px] text-twc07-dim">Jul 2 &middot; 28k reads</time>
          </div>
          <div class="flex gap-1">
            <button type="button" aria-label="Save article" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border border-black/6 text-twc07-muted cursor-pointer transition-[color,background,border-color] duration-200 hover:text-twc07-acc hover:bg-twc07-acc/6 hover:border-twc07-acc/20 focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>

    <article class="group/card grid grid-cols-[132px_1fr] max-[600px]:grid-cols-1 overflow-hidden rounded-[18px] bg-white border border-black/5 shadow-[0_12px_30px_-18px_oklch(0.4_0.08_310/0.18),inset_0_0_0_1px_oklch(1_0_0/0.5)] transition-[transform,box-shadow,border-color] duration-300 hover:-translate-y-0.5 hover:border-twc07-acc/25 motion-reduce:transition-none motion-reduce:hover:translate-y-0">
      <div class="relative overflow-hidden max-[600px]:min-h-30 [background-image:radial-gradient(circle_at_30%_30%,oklch(1_0_0/0.15)_0%,transparent_45%),linear-gradient(135deg,#7c2d12_0%,#dc2626_55%,#f59e0b_100%)]">
        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&q=80&auto=format&fit=crop" alt="Server infrastructure at night" loading="lazy" decoding="async" class="absolute inset-0 size-full object-cover block transition-transform duration-350 group-hover/card:scale-104 motion-reduce:transition-none motion-reduce:group-hover/card:scale-100">
        <div aria-hidden="true" class="absolute inset-0 pointer-events-none [background:linear-gradient(180deg,transparent_0%,oklch(0_0_0/0.35)_100%)]"></div>
        <span class="absolute top-2 left-2 px-[7px] py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 font-twc07-mono text-[9.5px] font-extrabold tracking-[0.02em] text-white">#3</span>
        <span class="absolute bottom-2 right-2 inline-flex items-center gap-1 px-1.5 py-0.5 rounded-[5px] bg-black/48 backdrop-blur-[6px] border border-white/16 text-white text-[9.5px] font-bold">
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          6 min
        </span>
      </div>
      <div class="flex flex-col gap-1.5 px-4 py-3.5">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="px-[7px] py-0.5 rounded-full font-twc07-mono text-[9.5px] font-extrabold tracking-[0.14em] uppercase text-twc07-accdeep bg-twc07-acc/8 border border-twc07-acc/15">AI &middot; Engineering</span>
          <span class="px-[7px] py-0.5 rounded-full font-twc07-mono text-[9.5px] font-extrabold tracking-[0.14em] text-twc07-red bg-twc07-red/8 border border-twc07-red/22">NEW</span>
        </div>
        <h3 class="m-0 text-[15px]/[1.3] font-extrabold tracking-[-0.02em] [background-image:linear-gradient(180deg,#1a1a1a_0%,#4b4b57_130%)] bg-clip-text text-transparent">Why Local-First is the Future of Web Apps</h3>
        <p class="m-0 text-xs/[1.5] text-twc07-muted line-clamp-2">Sync engines, CRDTs, and the return of desktop-quality speed. A new class of tools is finally making it practical.</p>
        <div class="grid grid-cols-[26px_1fr_auto] items-center gap-2 mt-1.5 pt-2 border-t border-dashed border-black/10">
          <span aria-hidden="true" class="flex items-center justify-center size-6.5 rounded-full border-[1.5px] border-white [background:linear-gradient(135deg,#fdba74,#ea580c)] text-white text-[10px] font-extrabold shadow-[0_1px_3px_oklch(0_0_0/0.08)]">RF</span>
          <div class="flex flex-col min-w-0">
            <span class="text-[11.5px] font-bold text-twc07-ink truncate">Rauno Freiberg</span>
            <time datetime="2026-07-08" class="text-[10px] text-twc07-dim">Today &middot; 3.2k reads</time>
          </div>
          <div class="flex gap-1">
            <button type="button" aria-label="Save article" class="inline-flex items-center justify-center size-11 rounded-lg bg-transparent border border-black/6 text-twc07-muted cursor-pointer transition-[color,background,border-color] duration-200 hover:text-twc07-acc hover:bg-twc07-acc/6 hover:border-twc07-acc/20 focus-visible:outline-2 focus-visible:outline-twc07-acc focus-visible:outline-offset-2">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
            </button>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-twc07-bg: #faf7f2;
  --color-twc07-bg: oklch(0.975 0.008 85);
  --color-twc07-track: #ede8dc;
  --color-twc07-track: oklch(0.93 0.015 85);
  --color-twc07-ink: #1a1a1a;
  --color-twc07-ink: oklch(0.21 0.005 270);
  --color-twc07-muted: #6b6b7c;
  --color-twc07-muted: oklch(0.51 0.02 285);
  --color-twc07-dim: #9ca3af;
  --color-twc07-dim: oklch(0.71 0.02 265);
  --color-twc07-acc: #7c3aed;
  --color-twc07-acc: oklch(0.5 0.22 290);
  --color-twc07-accdeep: #4338ca;
  --color-twc07-accdeep: oklch(0.42 0.21 275);
  --color-twc07-green: #34d399;
  --color-twc07-green: oklch(0.78 0.14 165);
  --color-twc07-greenink: #059669;
  --color-twc07-greenink: oklch(0.56 0.13 163);
  --color-twc07-red: #dc2626;
  --color-twc07-red: oklch(0.58 0.22 25);
  --color-twc07-amberink: #a16207;
  --color-twc07-amberink: oklch(0.5 0.13 70);
  --font-twc07-sans: 'Space Grotesk', system-ui, sans-serif;
  --font-twc07-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}
/* No @keyframes in this demo: every motion is a transition, so the stylesheet
   carries only the root contract. */

.twc-07 {
  width: 100%;
  min-height: 100svh;
}
```
