---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-circular-progress-ring/"
title: "Tailwind Accordion with Circular Progress Ring"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "A course-syllabus accordion where every module header wears a conic-gradient progress ring."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Accordion with Circular Progress Ring
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-accordion-circular-progress-ring/

A course-syllabus accordion where every module header wears a conic-gradient progress ring. Each ring shows its module's completion at rest; opening the module sweeps a bright arc around to that value, animated by a registered @property angle and driven entirely by group-open:[--tac17-arc:var(--tac17-to)]. The panel underneath grows with ::details-content + interpolate-size, and it is all native <details> with no JavaScript.
## HTML
```html
<section class="tac-17 w-full min-h-svh grid place-items-center bg-tac17-bg bg-[radial-gradient(80%_55%_at_50%_-5%,var(--color-tac17-glow),transparent_70%)] px-5 py-14 font-tac17-sans text-tac17-ink [interpolate-size:allow-keywords]" aria-label="Circular progress ring accordion demo">
  <div class="grid w-full justify-items-center gap-7">
    <div class="w-full max-w-[600px] rounded-3xl bg-tac17-card/80 p-[clamp(20px,4vw,32px)] shadow-[0_1px_0_oklch(1_0_0/0.06)_inset,0_30px_80px_-30px_oklch(0_0_0/0.75)] ring-1 ring-white/10">
      <header class="mb-6">
        <p class="text-xs font-semibold tracking-[0.16em] uppercase text-tac17-acc">Course · Frontend Foundations</p>
        <h2 class="mt-2 text-[clamp(22px,3.4vw,27px)] font-bold tracking-[-0.02em] text-balance">Modern CSS Layout Systems</h2>
        <div class="mt-4 flex items-center gap-3">
          <div class="h-1.5 flex-1 overflow-hidden rounded-full bg-tac17-track" aria-hidden="true"><div class="h-full w-[47%] rounded-full bg-linear-to-r from-tac17-acc2 to-tac17-acc shadow-[0_0_12px_var(--color-tac17-acc)]"></div></div>
          <p class="font-tac17-mono text-xs text-tac17-mut"><span class="text-tac17-ink">47%</span> · 9 of 19 lessons</p>
        </div>
      </header>

      <div class="divide-y divide-white/8 border-y border-white/8">
        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.7,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" style="--tac17-to:360deg">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-xl px-2 py-3.5 transition-colors hover:bg-white/[0.035] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac17-acc [&::-webkit-details-marker]:hidden">
            <span class="relative grid size-12 flex-none place-items-center" aria-hidden="true">
              <span class="absolute inset-0 rounded-full [background:conic-gradient(color-mix(in_oklab,var(--color-tac17-ok)_38%,transparent)_var(--tac17-to),var(--color-tac17-track)_0)] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))]"></span>
              <span class="absolute inset-0 rounded-full [--tac17-arc:0deg] [background:conic-gradient(var(--color-tac17-ok)_calc(var(--tac17-arc)-0.5deg),transparent_var(--tac17-arc))] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))] drop-shadow-[0_0_6px_var(--color-tac17-ok)] transition-[--tac17-arc] duration-[1100ms] ease-[cubic-bezier(.3,.7,.2,1)] group-open:[--tac17-arc:var(--tac17-to)] motion-reduce:transition-none"></span>
              <svg class="relative size-4 text-tac17-ok" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold tracking-[-0.01em]">Module 1 · Flexbox, properly</span>
              <span class="mt-1 block font-tac17-mono text-xs text-tac17-mut">5 lessons · 52 min</span>
            </span>
            <span class="rounded-full bg-tac17-ok/12 px-2.5 py-1 text-[11.5px] font-semibold text-tac17-ok ring-1 ring-tac17-ok/25 max-sm:hidden">Complete</span>
            <svg class="size-4 flex-none text-tac17-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac17-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-5 pl-[4.5rem] pr-2 max-sm:pl-2">
            <ol class="grid gap-1 text-sm">
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-ok/15 text-tac17-ok" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">The two axes, finally explained</span><span class="font-tac17-mono text-xs text-tac17-mut">9:40</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-ok/15 text-tac17-ok" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">flex-basis vs width</span><span class="font-tac17-mono text-xs text-tac17-mut">11:05</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-ok/15 text-tac17-ok" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">Gap, wrap and the min-width trap</span><span class="font-tac17-mono text-xs text-tac17-mut">13:20</span></li>
            </ol>
            <p class="mt-3 text-[13px] text-tac17-mut">Certificate badge earned on May 14 · <span class="text-tac17-ok">quiz 9/10</span></p>
          </div>
        </details>

        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.7,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" style="--tac17-to:223deg" open>
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-xl px-2 py-3.5 transition-colors hover:bg-white/[0.035] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac17-acc [&::-webkit-details-marker]:hidden">
            <span class="relative grid size-12 flex-none place-items-center" aria-hidden="true">
              <span class="absolute inset-0 rounded-full [background:conic-gradient(color-mix(in_oklab,var(--color-tac17-acc)_38%,transparent)_var(--tac17-to),var(--color-tac17-track)_0)] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))]"></span>
              <span class="absolute inset-0 rounded-full [--tac17-arc:0deg] [background:conic-gradient(var(--color-tac17-acc)_calc(var(--tac17-arc)-0.5deg),transparent_var(--tac17-arc))] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))] drop-shadow-[0_0_6px_var(--color-tac17-acc)] transition-[--tac17-arc] duration-[1100ms] ease-[cubic-bezier(.3,.7,.2,1)] group-open:[--tac17-arc:var(--tac17-to)] motion-reduce:transition-none"></span>
              <span class="relative font-tac17-mono text-[11px] font-semibold text-tac17-ink">62<span class="text-tac17-mut">%</span></span>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold tracking-[-0.01em] group-open:text-tac17-acc">Module 2 · Grid &amp; subgrid</span>
              <span class="mt-1 block font-tac17-mono text-xs text-tac17-mut">6 lessons · 1h 04m</span>
            </span>
            <span class="rounded-full bg-tac17-acc/12 px-2.5 py-1 text-[11.5px] font-semibold text-tac17-acc ring-1 ring-tac17-acc/25 max-sm:hidden">In progress</span>
            <svg class="size-4 flex-none text-tac17-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac17-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-5 pl-[4.5rem] pr-2 max-sm:pl-2">
            <ol class="grid gap-1 text-sm">
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-acc/15 text-tac17-acc" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">Tracks, lines and areas</span><span class="font-tac17-mono text-xs text-tac17-mut">12:10</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-acc/15 text-tac17-acc" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">minmax(), auto-fit and auto-fill</span><span class="font-tac17-mono text-xs text-tac17-mut">10:45</span></li>
              <li class="flex items-center gap-3 rounded-lg bg-white/[0.04] px-2 py-1.5 -mx-2 ring-1 ring-tac17-acc/20"><span class="grid size-5 flex-none place-items-center rounded-full ring-2 ring-tac17-acc" aria-hidden="true"><span class="size-1.5 rounded-full bg-tac17-acc"></span></span><span class="flex-1 font-medium text-tac17-ink">Subgrid in practice: aligned card footers</span><span class="font-tac17-mono text-xs text-tac17-acc">4:12 left</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="size-5 flex-none rounded-full ring-1 ring-inset ring-white/20" aria-hidden="true"></span><span class="flex-1 text-tac17-soft">Masonry-style layouts without JS</span><span class="font-tac17-mono text-xs text-tac17-mut">14:30</span></li>
            </ol>
            <button type="button" class="mt-4 inline-flex min-h-11 items-center gap-2 rounded-xl bg-tac17-acc px-4 text-sm font-semibold text-tac17-bg shadow-[0_8px_24px_-8px_var(--color-tac17-acc)] transition hover:brightness-110 active:scale-[0.98] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac17-acc">
              <svg class="size-4" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.5v9l7.5-4.5z" fill="currentColor"/></svg>Resume lesson 3
            </button>
          </div>
        </details>

        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.7,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" style="--tac17-to:90deg">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-xl px-2 py-3.5 transition-colors hover:bg-white/[0.035] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac17-acc [&::-webkit-details-marker]:hidden">
            <span class="relative grid size-12 flex-none place-items-center" aria-hidden="true">
              <span class="absolute inset-0 rounded-full [background:conic-gradient(color-mix(in_oklab,var(--color-tac17-acc)_38%,transparent)_var(--tac17-to),var(--color-tac17-track)_0)] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))]"></span>
              <span class="absolute inset-0 rounded-full [--tac17-arc:0deg] [background:conic-gradient(var(--color-tac17-acc)_calc(var(--tac17-arc)-0.5deg),transparent_var(--tac17-arc))] [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))] drop-shadow-[0_0_6px_var(--color-tac17-acc)] transition-[--tac17-arc] duration-[1100ms] ease-[cubic-bezier(.3,.7,.2,1)] group-open:[--tac17-arc:var(--tac17-to)] motion-reduce:transition-none"></span>
              <span class="relative font-tac17-mono text-[11px] font-semibold text-tac17-ink">25<span class="text-tac17-mut">%</span></span>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold tracking-[-0.01em] group-open:text-tac17-acc">Module 3 · Container queries</span>
              <span class="mt-1 block font-tac17-mono text-xs text-tac17-mut">4 lessons · 46 min</span>
            </span>
            <span class="rounded-full bg-tac17-acc/12 px-2.5 py-1 text-[11.5px] font-semibold text-tac17-acc ring-1 ring-tac17-acc/25 max-sm:hidden">Started</span>
            <svg class="size-4 flex-none text-tac17-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac17-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-5 pl-[4.5rem] pr-2 max-sm:pl-2">
            <ol class="grid gap-1 text-sm">
              <li class="flex items-center gap-3 py-1.5"><span class="grid size-5 flex-none place-items-center rounded-full bg-tac17-acc/15 text-tac17-acc" aria-hidden="true"><svg class="size-3" viewBox="0 0 16 16"><path d="M3.5 8.4 6.6 11.4 12.5 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span><span class="flex-1 text-tac17-soft">Size queries vs media queries</span><span class="font-tac17-mono text-xs text-tac17-mut">10:15</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="size-5 flex-none rounded-full ring-1 ring-inset ring-white/20" aria-hidden="true"></span><span class="flex-1 text-tac17-soft">Container units: cqi and cqb</span><span class="font-tac17-mono text-xs text-tac17-mut">11:40</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="size-5 flex-none rounded-full ring-1 ring-inset ring-white/20" aria-hidden="true"></span><span class="flex-1 text-tac17-soft">Style queries for theming</span><span class="font-tac17-mono text-xs text-tac17-mut">12:05</span></li>
              <li class="flex items-center gap-3 py-1.5"><span class="size-5 flex-none rounded-full ring-1 ring-inset ring-white/20" aria-hidden="true"></span><span class="flex-1 text-tac17-soft">Project: a responsive pricing card</span><span class="font-tac17-mono text-xs text-tac17-mut">12:00</span></li>
            </ol>
          </div>
        </details>

        <details class="group [&::details-content]:h-0 [&::details-content]:overflow-clip [&::details-content]:transition-[height,content-visibility] [&::details-content]:duration-500 [&::details-content]:ease-[cubic-bezier(.2,.7,.2,1)] [&::details-content]:[transition-behavior:allow-discrete] open:[&::details-content]:h-auto motion-reduce:[&::details-content]:transition-none" style="--tac17-to:0deg">
          <summary class="flex min-h-11 cursor-pointer list-none items-center gap-4 rounded-xl px-2 py-3.5 transition-colors hover:bg-white/[0.035] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac17-acc [&::-webkit-details-marker]:hidden">
            <span class="relative grid size-12 flex-none place-items-center" aria-hidden="true">
              <span class="absolute inset-0 rounded-full bg-tac17-track [mask:radial-gradient(farthest-side,transparent_calc(100%-4px),#000_calc(100%-3.5px))]"></span>
              <span class="relative font-tac17-mono text-[11px] font-semibold text-tac17-mut">0%</span>
            </span>
            <span class="min-w-0 flex-1">
              <span class="block text-[15.5px] font-semibold tracking-[-0.01em] group-open:text-tac17-acc">Module 4 · Anchor positioning</span>
              <span class="mt-1 block font-tac17-mono text-xs text-tac17-mut">4 lessons · 58 min</span>
            </span>
            <span class="rounded-full bg-white/6 px-2.5 py-1 text-[11.5px] font-semibold text-tac17-mut ring-1 ring-white/12 max-sm:hidden">Up next</span>
            <svg class="size-4 flex-none text-tac17-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac17-ink motion-reduce:transition-none" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </summary>
          <div class="pb-5 pl-[4.5rem] pr-2 max-sm:pl-2">
            <p class="text-sm leading-relaxed text-tac17-soft text-pretty">Tooltips, popovers and menus that stay attached to their trigger, with zero JavaScript positioning. Unlocks after the Module 3 project.</p>
          </div>
        </details>
      </div>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tac17-mono text-[11.5px] text-tac17-mut ring-1 ring-white/10">@property &lt;angle&gt; · group-open:[--tac17-arc:…] · conic-gradient + mask</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac17-bg: #070b14;
  --color-tac17-bg: oklch(0.15 0.02 260);
  --color-tac17-glow: #0f3a4a99;
  --color-tac17-glow: oklch(0.33 0.07 220 / 0.6);
  --color-tac17-card: #111827;
  --color-tac17-card: oklch(0.21 0.025 262);
  --color-tac17-track: #263044;
  --color-tac17-track: oklch(0.31 0.03 262);
  --color-tac17-ink: #eef3f9;
  --color-tac17-ink: oklch(0.96 0.01 250);
  --color-tac17-soft: #c5cedb;
  --color-tac17-soft: oklch(0.85 0.02 255);
  --color-tac17-mut: #98a3b6;
  --color-tac17-mut: oklch(0.72 0.025 260);
  --color-tac17-acc: #3fd6f0;
  --color-tac17-acc: oklch(0.81 0.13 215);
  --color-tac17-acc2: #5b7cfa;
  --color-tac17-acc2: oklch(0.63 0.18 268);
  --color-tac17-ok: #4ade9a;
  --color-tac17-ok: oklch(0.82 0.16 158);
  --font-tac17-sans: 'Sora', system-ui, sans-serif;
  --font-tac17-mono: 'Geist Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-17 {
  width: 100%;
  min-height: 100svh;
}
/* Registered so the arc interpolates: an untyped custom property can only snap from 0 to its target. */

@property --tac17-arc {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
```
