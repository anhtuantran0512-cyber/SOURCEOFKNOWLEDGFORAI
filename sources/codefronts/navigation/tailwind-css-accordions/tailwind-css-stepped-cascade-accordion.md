---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-stepped-cascade-accordion/"
title: "Tailwind CSS Stepped Cascade Accordion"
section: "navigation"
category: "tailwind-css-accordions"
category_name: "Tailwind CSS Accordions — Vertical & Horizontal"
description: "Items descend like a staircase: each level is indented by ml-[calc(var(--i)*var(--tac16-pitch))] and hooked to the step above by an L-shaped bracket, so the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Stepped Cascade Accordion
Source: https://codefronts.com/navigation/tailwind-css-accordions/tailwind-css-stepped-cascade-accordion/

Items descend like a staircase: each level is indented by ml-[calc(var(--i)*var(--tac16-pitch))] and hooked to the step above by an L-shaped bracket, so the closed list is already a diagram of depth. Opening a level transitions its margin to zero &mdash; it steps forward out of the stair to full width while the others hold formation. Shown as a four-level learning path with progress states, on a warm sand stage with deep-teal ink.
## HTML
```html
<section class="tac-16 w-full min-h-svh grid place-items-center bg-tac16-bg bg-[radial-gradient(70%_50%_at_100%_0%,var(--color-tac16-glow),transparent_70%)] px-5 py-14 font-tac16-sans text-tac16-ink [--tac16-pitch:2.5rem] [interpolate-size:allow-keywords] max-sm:[--tac16-pitch:1.125rem]" aria-label="Stepped cascade accordion demo">
  <div class="grid w-full max-w-2xl gap-9">
    <header class="grid gap-5 sm:grid-cols-[1fr_auto] sm:items-end">
      <div class="grid gap-3">
        <p class="font-tac16-mono text-[12px] font-semibold tracking-[0.16em] text-tac16-acc uppercase">Learning path</p>
        <h2 class="text-[clamp(28px,5vw,40px)] leading-[1.05] font-extrabold tracking-[-0.03em] text-balance">Rust for backend engineers</h2>
        <p class="max-w-md text-[15px] leading-relaxed text-tac16-mut">Four levels, each one deeper than the last. Open a level to step into it.</p>
      </div>
      <div class="grid gap-2 rounded-2xl bg-tac16-card p-4 ring-1 ring-tac16-line sm:w-52">
        <p class="flex items-baseline justify-between text-[13px] text-tac16-mut"><span>Progress</span><span class="font-tac16-mono font-semibold text-tac16-ink">2 / 4</span></p>
        <div aria-hidden="true" class="flex gap-1"><span class="h-1.5 flex-1 rounded-full bg-tac16-acc"></span><span class="h-1.5 flex-1 rounded-full bg-tac16-acc"></span><span class="h-1.5 flex-1 rounded-full bg-tac16-amb"></span><span class="h-1.5 flex-1 rounded-full bg-tac16-line"></span></div>
        <p class="text-[12.5px] text-tac16-mut">About 6 hours left</p>
      </div>
    </header>

    <div class="flex flex-col gap-3">
      <details name="tac16-path" style="--i:0" class="group relative ml-[calc(var(--i)*var(--tac16-pitch))] rounded-2xl bg-tac16-card ring-1 ring-tac16-line transition-[margin-left,box-shadow] duration-500 hover:ring-tac16-acc/50 open:shadow-[0_1px_2px_oklch(0.27_0.035_205/0.06),0_22px_44px_-20px_oklch(0.27_0.035_205/0.35)] open:ring-2 open:ring-tac16-acc ease-[cubic-bezier(0.4,0,0.2,1)] open:ml-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
        <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac16-acc [&::-webkit-details-marker]:hidden">
          <span class="grid size-9 flex-none place-items-center rounded-lg bg-tac16-soft font-tac16-mono text-[12px] font-semibold text-tac16-acc">L1</span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="truncate text-[16px] font-bold tracking-[-0.01em]">Foundations</span>
            <span class="font-tac16-mono text-[11.5px] text-tac16-mut">8 lessons · 1h 40m</span>
          </span>
          <span class="grid size-6 flex-none place-items-center rounded-full bg-tac16-acc text-white" role="img" aria-label="Completed"><svg aria-hidden="true" viewBox="0 0 16 16" width="12" height="12"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <svg aria-hidden="true" class="flex-none text-tac16-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac16-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <div class="mx-4 grid gap-3 border-t border-tac16-line pt-4 pb-4">
          <p class="text-[14.5px] leading-relaxed text-tac16-mut">Cargo, the type system and pattern matching &mdash; enough Rust to read any codebase and write small CLIs with confidence.</p>
          <ol class="grid gap-1.5 font-tac16-mono text-[12.5px]">
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">01 · Cargo &amp; crates</span><span class="text-tac16-mut">12m</span></li>
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">02 · Enums &amp; match</span><span class="text-tac16-mut">15m</span></li>
          </ol>
        </div>
      </details>

      <details name="tac16-path" style="--i:1" class="group relative ml-[calc(var(--i)*var(--tac16-pitch))] rounded-2xl bg-tac16-card ring-1 ring-tac16-line transition-[margin-left,box-shadow] duration-500 hover:ring-tac16-acc/50 open:shadow-[0_1px_2px_oklch(0.27_0.035_205/0.06),0_22px_44px_-20px_oklch(0.27_0.035_205/0.35)] open:ring-2 open:ring-tac16-acc ease-[cubic-bezier(0.4,0,0.2,1)] open:ml-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
        <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac16-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute -top-[18px] -left-[calc(var(--tac16-pitch)*0.6)] h-[46px] w-[calc(var(--tac16-pitch)*0.6-4px)] rounded-bl-xl border-b-2 border-l-2 border-tac16-line transition-opacity duration-300 group-open:opacity-0"></span>
          <span class="grid size-9 flex-none place-items-center rounded-lg bg-tac16-soft font-tac16-mono text-[12px] font-semibold text-tac16-acc">L2</span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="truncate text-[16px] font-bold tracking-[-0.01em]">Ownership &amp; borrowing</span>
            <span class="font-tac16-mono text-[11.5px] text-tac16-mut">6 lessons · 2h 05m</span>
          </span>
          <span class="grid size-6 flex-none place-items-center rounded-full bg-tac16-acc text-white" role="img" aria-label="Completed"><svg aria-hidden="true" viewBox="0 0 16 16" width="12" height="12"><path d="M3.5 8.5 6.5 11.5 12.5 4.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <svg aria-hidden="true" class="flex-none text-tac16-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac16-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <div class="mx-4 grid gap-3 border-t border-tac16-line pt-4 pb-4">
          <p class="text-[14.5px] leading-relaxed text-tac16-mut">Moves, borrows and lifetimes, explained with diagrams instead of compiler errors. The level most people quit on &mdash; and the one that makes everything after it click.</p>
          <ol class="grid gap-1.5 font-tac16-mono text-[12.5px]">
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">01 · Who owns this value?</span><span class="text-tac16-mut">18m</span></li>
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">02 · Lifetimes without tears</span><span class="text-tac16-mut">24m</span></li>
          </ol>
        </div>
      </details>

      <details name="tac16-path" style="--i:2" class="group relative ml-[calc(var(--i)*var(--tac16-pitch))] rounded-2xl bg-tac16-card ring-1 ring-tac16-line transition-[margin-left,box-shadow] duration-500 hover:ring-tac16-acc/50 open:shadow-[0_1px_2px_oklch(0.27_0.035_205/0.06),0_22px_44px_-20px_oklch(0.27_0.035_205/0.35)] open:ring-2 open:ring-tac16-acc ease-[cubic-bezier(0.4,0,0.2,1)] open:ml-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none" open>
        <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac16-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute -top-[18px] -left-[calc(var(--tac16-pitch)*0.6)] h-[46px] w-[calc(var(--tac16-pitch)*0.6-4px)] rounded-bl-xl border-b-2 border-l-2 border-tac16-line transition-opacity duration-300 group-open:opacity-0"></span>
          <span class="grid size-9 flex-none place-items-center rounded-lg bg-tac16-soft font-tac16-mono text-[12px] font-semibold text-tac16-acc">L3</span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="truncate text-[16px] font-bold tracking-[-0.01em]">Async &amp; concurrency</span>
            <span class="font-tac16-mono text-[11.5px] text-tac16-mut">7 lessons · 2h 30m</span>
          </span>
          <span class="relative size-6 flex-none rounded-full bg-[conic-gradient(var(--color-tac16-amb)_0_40%,var(--color-tac16-line)_40%_100%)] after:absolute after:inset-[4px] after:rounded-full after:bg-tac16-card" role="img" aria-label="In progress, 40 percent"></span>
          <svg aria-hidden="true" class="flex-none text-tac16-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac16-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <div class="mx-4 grid gap-3 border-t border-tac16-line pt-4 pb-4">
          <p class="text-[14.5px] leading-relaxed text-tac16-mut">Tokio, futures and channels. You'll build a rate-limited HTTP fetcher that handles ten thousand requests without a single <code class="rounded bg-tac16-soft px-1 font-tac16-mono text-[12.5px] text-tac16-ink">Mutex</code>.</p>
          <ol class="grid gap-1.5 font-tac16-mono text-[12.5px]">
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">01 · What a Future really is</span><span class="text-tac16-mut">20m</span></li>
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-bg/60 px-3 py-2 ring-1 ring-tac16-line"><span class="truncate">02 · Spawning tasks on Tokio</span><span class="text-tac16-mut">22m</span></li>
            <li class="flex items-center justify-between gap-3 rounded-lg bg-tac16-amb-soft px-3 py-2 ring-1 ring-tac16-amb/40"><span class="truncate font-semibold">03 · Channels &amp; backpressure</span><span class="text-tac16-amb-ink">Up next</span></li>
          </ol>
          <button type="button" class="mt-1 inline-flex min-h-11 w-fit items-center gap-2 rounded-xl bg-tac16-ink px-4 text-[14px] font-semibold text-tac16-bg transition hover:bg-tac16-acc focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tac16-acc">Continue lesson 3 <svg aria-hidden="true" viewBox="0 0 16 16" width="14" height="14"><path d="M3 8h9M8.5 4.5 12 8l-3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        </div>
      </details>

      <details name="tac16-path" style="--i:3" class="group relative ml-[calc(var(--i)*var(--tac16-pitch))] rounded-2xl bg-tac16-card ring-1 ring-tac16-line transition-[margin-left,box-shadow] duration-500 hover:ring-tac16-acc/50 open:shadow-[0_1px_2px_oklch(0.27_0.035_205/0.06),0_22px_44px_-20px_oklch(0.27_0.035_205/0.35)] open:ring-2 open:ring-tac16-acc ease-[cubic-bezier(0.4,0,0.2,1)] open:ml-0 details-content:h-0 details-content:overflow-clip details-content:transition-[height,content-visibility] details-content:duration-500 details-content:ease-[cubic-bezier(0.2,0.7,0.2,1)] details-content:[transition-behavior:allow-discrete] open:details-content:h-auto motion-reduce:transition-none motion-reduce:details-content:transition-none">
        <summary class="flex min-h-14 cursor-pointer list-none items-center gap-3.5 rounded-2xl px-4 py-3 focus-visible:outline-2 focus-visible:outline-offset-3 focus-visible:outline-tac16-acc [&::-webkit-details-marker]:hidden">
          <span aria-hidden="true" class="pointer-events-none absolute -top-[18px] -left-[calc(var(--tac16-pitch)*0.6)] h-[46px] w-[calc(var(--tac16-pitch)*0.6-4px)] rounded-bl-xl border-b-2 border-l-2 border-tac16-line transition-opacity duration-300 group-open:opacity-0"></span>
          <span class="grid size-9 flex-none place-items-center rounded-lg bg-tac16-soft font-tac16-mono text-[12px] font-semibold text-tac16-acc">L4</span>
          <span class="grid min-w-0 flex-1 gap-0.5">
            <span class="truncate text-[16px] font-bold tracking-[-0.01em]">Shipping to prod</span>
            <span class="font-tac16-mono text-[11.5px] text-tac16-mut">9 lessons · 3h 15m</span>
          </span>
          <span class="grid size-6 flex-none place-items-center rounded-full bg-tac16-soft text-tac16-mut ring-1 ring-tac16-line" role="img" aria-label="Locked"><svg aria-hidden="true" viewBox="0 0 16 16" width="12" height="12"><rect x="3.5" y="7" width="9" height="6.5" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M5.5 7V5.5a2.5 2.5 0 0 1 5 0V7" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></span>
          <svg aria-hidden="true" class="flex-none text-tac16-mut transition-transform duration-300 group-open:rotate-180 group-open:text-tac16-acc motion-reduce:transition-none" viewBox="0 0 16 16" width="16" height="16"><path d="M4 6.2 8 10l4-3.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </summary>
        <div class="mx-4 grid gap-3 border-t border-tac16-line pt-4 pb-4">
          <p class="text-[14.5px] leading-relaxed text-tac16-mut">Tracing, graceful shutdown, zero-downtime deploys and profiling a real service under load. Unlocks when you finish Async &amp; concurrency.</p>
        </div>
      </details>
    </div>

    <p aria-hidden="true" class="justify-self-center rounded-full border border-tac16-line bg-tac16-card px-3.5 py-2 text-center font-tac16-mono text-[11.5px] text-tac16-mut">ml-[calc(var(--i)*var(--tac16-pitch))] · open:ml-0 · details name</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tac16-bg: #f7efe0;
  --color-tac16-bg: oklch(0.955 0.022 85);
  --color-tac16-glow: #d2f3f0;
  --color-tac16-glow: oklch(0.94 0.035 190);
  --color-tac16-card: #fefbf6;
  --color-tac16-card: oklch(0.99 0.008 85);
  --color-tac16-line: #e1d6c2;
  --color-tac16-line: oklch(0.88 0.03 85);
  --color-tac16-ink: #0e2b2f;
  --color-tac16-ink: oklch(0.27 0.035 205);
  --color-tac16-mut: #476063;
  --color-tac16-mut: oklch(0.47 0.03 205);
  --color-tac16-acc: #007a78;
  --color-tac16-acc: oklch(0.52 0.1 192);
  --color-tac16-soft: #d2f3f0;
  --color-tac16-soft: oklch(0.94 0.035 190);
  --color-tac16-amb: #bb731b;
  --color-tac16-amb: oklch(0.62 0.13 65);
  --color-tac16-amb-soft: #f4e3bf;
  --color-tac16-amb-soft: oklch(0.92 0.05 85);
  --color-tac16-amb-ink: #7f4500;
  --color-tac16-amb-ink: oklch(0.47 0.11 60);
  --font-tac16-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-tac16-mono: 'IBM Plex Mono', ui-monospace, monospace;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tac-16 {
  width: 100%;
  min-height: 100svh;
}
```
