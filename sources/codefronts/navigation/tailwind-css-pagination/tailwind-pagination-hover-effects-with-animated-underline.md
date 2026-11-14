---
source: "codefronts"
url: "https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-hover-effects-with-animated-underline/"
title: "Tailwind Pagination Hover Effects with Animated Underline"
section: "navigation"
category: "tailwind-css-pagination"
category_name: "Tailwind CSS Pagination"
description: "A typographic pagination row where the interaction is the design: an accent rule wipes in from the left and retreats to the right, the serif digit lifts a…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Pagination Hover Effects with Animated Underline
Source: https://codefronts.com/navigation/tailwind-css-pagination/tailwind-pagination-hover-effects-with-animated-underline/

A typographic pagination row where the interaction is the design: an accent rule wipes in from the left and retreats to the right, the serif digit lifts a fraction, and both run on :hover and :focus-visible so keyboard users get identical feedback. Built from after:scale-x-0 after:origin-right hover:after:origin-left hover:after:scale-x-100 — nothing animated touches layout.
## HTML
```html
<section class="tpg-15 w-full min-h-svh grid place-items-center bg-tpg15-bg bg-[radial-gradient(60%_45%_at_50%_0%,var(--color-tpg15-glow),transparent_70%),radial-gradient(40%_35%_at_100%_100%,var(--color-tpg15-glow2),transparent_70%)] px-5 py-14 font-tpg15-sans text-tpg15-ink antialiased" aria-label="Pagination hover effects with animated underline demo">
  <div class="grid w-full max-w-[44rem] justify-items-center gap-10">
    <div class="grid w-full gap-8">
      <header class="grid gap-3">
        <p class="text-xs font-semibold tracking-[0.18em] uppercase text-tpg15-a">Field Notes &middot; Archive</p>
        <h2 class="font-tpg15-serif text-[clamp(2.4rem,6vw,3.6rem)] leading-[0.98] tracking-[-0.01em] text-balance">Every issue, <em class="bg-linear-to-r from-tpg15-a to-tpg15-gold-ink bg-clip-text pe-[0.06em] text-transparent">in order.</em></h2>
      </header>

      <ol class="grid border-t border-tpg15-line" role="list">
        <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-x-4 gap-y-1 border-b border-tpg15-line py-5 sm:grid-cols-[5.5rem_1fr_auto]">
          <span class="font-tpg15-serif text-2xl text-tpg15-mut tabular-nums">No. 40</span>
          <a href="#tpg-15-issue-40" class="relative justify-self-start rounded-sm text-[17px] font-medium tracking-[-0.01em] after:absolute after:inset-x-0 after:-bottom-0.5 after:h-px after:origin-right after:scale-x-0 after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg15-ring motion-reduce:after:transition-none">On drawing with light at dusk</a>
          <time datetime="2026-09" class="col-start-2 font-tpg15-mono text-xs text-tpg15-mut sm:col-start-3">Sep 2026</time>
        </li>
        <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-x-4 gap-y-1 border-b border-tpg15-line py-5 sm:grid-cols-[5.5rem_1fr_auto]">
          <span class="font-tpg15-serif text-2xl text-tpg15-mut tabular-nums">No. 39</span>
          <a href="#tpg-15-issue-39" class="relative justify-self-start rounded-sm text-[17px] font-medium tracking-[-0.01em] after:absolute after:inset-x-0 after:-bottom-0.5 after:h-px after:origin-right after:scale-x-0 after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg15-ring motion-reduce:after:transition-none">A grammar of quiet interfaces</a>
          <time datetime="2026-08" class="col-start-2 font-tpg15-mono text-xs text-tpg15-mut sm:col-start-3">Aug 2026</time>
        </li>
        <li class="grid grid-cols-[4.5rem_1fr] items-baseline gap-x-4 gap-y-1 border-b border-tpg15-line py-5 sm:grid-cols-[5.5rem_1fr_auto]">
          <span class="font-tpg15-serif text-2xl text-tpg15-mut tabular-nums">No. 38</span>
          <a href="#tpg-15-issue-38" class="relative justify-self-start rounded-sm text-[17px] font-medium tracking-[-0.01em] after:absolute after:inset-x-0 after:-bottom-0.5 after:h-px after:origin-right after:scale-x-0 after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-tpg15-ring motion-reduce:after:transition-none">Paper, ink and the 8-point grid</a>
          <time datetime="2026-07" class="col-start-2 font-tpg15-mono text-xs text-tpg15-mut sm:col-start-3">Jul 2026</time>
        </li>
      </ol>

      <nav class="@container" aria-label="Pagination">
        <div class="flex items-center justify-between gap-2">
          <a href="#tpg-15-p3" rel="prev" class="group/e inline-flex min-h-11 min-w-11 items-center justify-center gap-2 rounded-full px-4 text-sm font-medium text-tpg15-ink ring-1 ring-tpg15-a/30 transition-[box-shadow,background-color,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-tpg15-a/8 hover:text-tpg15-a hover:shadow-tpg15-ember hover:ring-tpg15-a/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring @max-[30rem]:px-0"><svg class="transition-transform duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/e:-translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M13 8H3.5M7.5 3.5 3 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="@max-[30rem]:sr-only">Newer</span></a>
          <ol class="flex items-center gap-0.5 sm:gap-1.5" role="list">
            <li><a href="#tpg-15-p1" aria-label="Page 1" class="group/n relative grid min-h-11 min-w-11 place-items-center rounded-md px-1 font-tpg15-serif text-[1.7rem] leading-none tabular-nums text-tpg15-mut transition-colors duration-300 hover:text-tpg15-a focus-visible:text-tpg15-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[2px] after:origin-right after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:shadow-tpg15-wire after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:italic aria-[current=page]:bg-[radial-gradient(closest-side,var(--color-tpg15-halo),transparent)] aria-[current=page]:after:h-[3px] aria-[current=page]:after:origin-left aria-[current=page]:after:scale-x-100 motion-reduce:transition-none motion-reduce:after:transition-none"><span class="block transition-[translate,scale] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/n:-translate-y-0.5 group-hover/n:scale-110 group-focus-visible/n:-translate-y-0.5 group-focus-visible/n:scale-110 group-aria-[current=page]/n:bg-linear-to-br group-aria-[current=page]/n:from-tpg15-a group-aria-[current=page]/n:to-tpg15-gold-ink group-aria-[current=page]/n:bg-clip-text group-aria-[current=page]/n:pe-[0.08em] group-aria-[current=page]/n:text-transparent motion-reduce:transition-none">1</span></a></li>
            <li aria-hidden="true" class="grid min-h-11 w-5 place-items-center font-tpg15-serif text-xl text-tpg15-gold-ink">&hellip;</li>
            <li class="@max-[26rem]:hidden"><a href="#tpg-15-p3" aria-label="Page 3" class="group/n relative grid min-h-11 min-w-11 place-items-center rounded-md px-1 font-tpg15-serif text-[1.7rem] leading-none tabular-nums text-tpg15-mut transition-colors duration-300 hover:text-tpg15-a focus-visible:text-tpg15-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[2px] after:origin-right after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:shadow-tpg15-wire after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:italic aria-[current=page]:bg-[radial-gradient(closest-side,var(--color-tpg15-halo),transparent)] aria-[current=page]:after:h-[3px] aria-[current=page]:after:origin-left aria-[current=page]:after:scale-x-100 motion-reduce:transition-none motion-reduce:after:transition-none"><span class="block transition-[translate,scale] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/n:-translate-y-0.5 group-hover/n:scale-110 group-focus-visible/n:-translate-y-0.5 group-focus-visible/n:scale-110 group-aria-[current=page]/n:bg-linear-to-br group-aria-[current=page]/n:from-tpg15-a group-aria-[current=page]/n:to-tpg15-gold-ink group-aria-[current=page]/n:bg-clip-text group-aria-[current=page]/n:pe-[0.08em] group-aria-[current=page]/n:text-transparent motion-reduce:transition-none">3</span></a></li>
            <li><a href="#tpg-15-p4" aria-current="page" aria-label="Page 4, current page" class="group/n relative grid min-h-11 min-w-11 place-items-center rounded-md px-1 font-tpg15-serif text-[1.7rem] leading-none tabular-nums text-tpg15-mut transition-colors duration-300 hover:text-tpg15-a focus-visible:text-tpg15-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[2px] after:origin-right after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:shadow-tpg15-wire after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:italic aria-[current=page]:bg-[radial-gradient(closest-side,var(--color-tpg15-halo),transparent)] aria-[current=page]:after:h-[3px] aria-[current=page]:after:origin-left aria-[current=page]:after:scale-x-100 motion-reduce:transition-none motion-reduce:after:transition-none"><span class="block transition-[translate,scale] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/n:-translate-y-0.5 group-hover/n:scale-110 group-focus-visible/n:-translate-y-0.5 group-focus-visible/n:scale-110 group-aria-[current=page]/n:bg-linear-to-br group-aria-[current=page]/n:from-tpg15-a group-aria-[current=page]/n:to-tpg15-gold-ink group-aria-[current=page]/n:bg-clip-text group-aria-[current=page]/n:pe-[0.08em] group-aria-[current=page]/n:text-transparent motion-reduce:transition-none">4</span></a></li>
            <li class="@max-[26rem]:hidden"><a href="#tpg-15-p5" aria-label="Page 5" class="group/n relative grid min-h-11 min-w-11 place-items-center rounded-md px-1 font-tpg15-serif text-[1.7rem] leading-none tabular-nums text-tpg15-mut transition-colors duration-300 hover:text-tpg15-a focus-visible:text-tpg15-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[2px] after:origin-right after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:shadow-tpg15-wire after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:italic aria-[current=page]:bg-[radial-gradient(closest-side,var(--color-tpg15-halo),transparent)] aria-[current=page]:after:h-[3px] aria-[current=page]:after:origin-left aria-[current=page]:after:scale-x-100 motion-reduce:transition-none motion-reduce:after:transition-none"><span class="block transition-[translate,scale] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/n:-translate-y-0.5 group-hover/n:scale-110 group-focus-visible/n:-translate-y-0.5 group-focus-visible/n:scale-110 group-aria-[current=page]/n:bg-linear-to-br group-aria-[current=page]/n:from-tpg15-a group-aria-[current=page]/n:to-tpg15-gold-ink group-aria-[current=page]/n:bg-clip-text group-aria-[current=page]/n:pe-[0.08em] group-aria-[current=page]/n:text-transparent motion-reduce:transition-none">5</span></a></li>
            <li aria-hidden="true" class="grid min-h-11 w-5 place-items-center font-tpg15-serif text-xl text-tpg15-gold-ink">&hellip;</li>
            <li><a href="#tpg-15-p12" aria-label="Page 12, oldest issues" class="group/n relative grid min-h-11 min-w-11 place-items-center rounded-md px-1 font-tpg15-serif text-[1.7rem] leading-none tabular-nums text-tpg15-mut transition-colors duration-300 hover:text-tpg15-a focus-visible:text-tpg15-a focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring after:absolute after:inset-x-2.5 after:bottom-1.5 after:h-[2px] after:origin-right after:scale-x-0 after:rounded-full after:bg-linear-to-r after:from-tpg15-a after:to-tpg15-gold after:shadow-tpg15-wire after:transition-[scale] after:duration-300 after:ease-[cubic-bezier(.16,1,.3,1)] hover:after:origin-left hover:after:scale-x-100 focus-visible:after:origin-left focus-visible:after:scale-x-100 aria-[current=page]:italic aria-[current=page]:bg-[radial-gradient(closest-side,var(--color-tpg15-halo),transparent)] aria-[current=page]:after:h-[3px] aria-[current=page]:after:origin-left aria-[current=page]:after:scale-x-100 motion-reduce:transition-none motion-reduce:after:transition-none"><span class="block transition-[translate,scale] duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/n:-translate-y-0.5 group-hover/n:scale-110 group-focus-visible/n:-translate-y-0.5 group-focus-visible/n:scale-110 group-aria-[current=page]/n:bg-linear-to-br group-aria-[current=page]/n:from-tpg15-a group-aria-[current=page]/n:to-tpg15-gold-ink group-aria-[current=page]/n:bg-clip-text group-aria-[current=page]/n:pe-[0.08em] group-aria-[current=page]/n:text-transparent motion-reduce:transition-none">12</span></a></li>
          </ol>
          <a href="#tpg-15-p5" rel="next" class="group/e inline-flex min-h-11 min-w-11 items-center justify-center gap-2 rounded-full px-4 text-sm font-medium text-tpg15-ink ring-1 ring-tpg15-a/30 transition-[box-shadow,background-color,color] duration-300 ease-[cubic-bezier(.16,1,.3,1)] hover:bg-tpg15-a/8 hover:text-tpg15-a hover:shadow-tpg15-ember hover:ring-tpg15-a/60 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-tpg15-ring @max-[30rem]:px-0"><span class="@max-[30rem]:sr-only">Older</span><svg class="transition-transform duration-300 ease-[cubic-bezier(.16,1,.3,1)] group-hover/e:translate-x-0.5 motion-reduce:transition-none" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M3 8h9.5M8.5 3.5 13 8l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        </div>
        <p class="mt-4 text-center font-tpg15-mono text-xs text-tpg15-mut tabular-nums">Page 4 of 12 &middot; issues 31&ndash;40</p>
      </nav>
    </div>
    <p aria-hidden="true" class="rounded-full px-3.5 py-2 font-tpg15-mono text-[11.5px] text-tpg15-mut ring-1 ring-tpg15-line">hover:after:origin-left · group-hover/n:</p>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-tpg15-bg: #faf4ec;
  --color-tpg15-bg: oklch(0.970 0.012 75);
  --color-tpg15-glow: #f8d3a8a6;
  --color-tpg15-glow: oklch(0.888 0.070 71 / 0.65);
  --color-tpg15-glow2: #fde68a66;
  --color-tpg15-glow2: oklch(0.924 0.115 96 / 0.40);
  --color-tpg15-ink: #1f140c;
  --color-tpg15-ink: oklch(0.203 0.024 57);
  --color-tpg15-mut: #6b5443;
  --color-tpg15-mut: oklch(0.465 0.040 58);
  --color-tpg15-line: #ead9c6;
  --color-tpg15-line: oklch(0.894 0.032 70);
  --color-tpg15-a: #c2410c;
  --color-tpg15-a: oklch(0.553 0.174 38);
  --color-tpg15-gold: #eab308;
  --color-tpg15-gold: oklch(0.795 0.162 86);
  --color-tpg15-gold-ink: #a16207;
  --color-tpg15-gold-ink: oklch(0.554 0.121 66);
  --color-tpg15-halo: #fbbf2440;
  --color-tpg15-halo: oklch(0.837 0.164 84 / 0.25);
  --color-tpg15-ring: #c2410c;
  --color-tpg15-ring: oklch(0.553 0.174 38);
  --font-tpg15-serif: 'Instrument Serif', Georgia, serif;
  --font-tpg15-sans: 'Manrope', system-ui, sans-serif;
  --font-tpg15-mono: 'Fragment Mono', ui-monospace, monospace;
  --shadow-tpg15-wire: 0 0 6px oklch(0.75 0.16 70 / 0.55);
  --shadow-tpg15-ember: 0 6px 18px -8px oklch(0.55 0.18 40 / 0.5);
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.tpg-15 {
  width: 100%;
  min-height: 100svh;
}
/* Dark theme (the original's home): espresso night, copper and gold brighten to orange-400 / yellow-400; same tokens, re-pointed. */

@media (prefers-color-scheme: dark) {
  .tpg-15:not([data-theme="light"]) {
    --color-tpg15-bg: #15100c;
    --color-tpg15-bg: oklch(0.178 0.012 61);
    --color-tpg15-glow: #7c2d1273;
    --color-tpg15-glow: oklch(0.408 0.116 38 / 0.45);
    --color-tpg15-glow2: #713f1259;
    --color-tpg15-glow2: oklch(0.421 0.090 58 / 0.35);
    --color-tpg15-ink: #f6ece2;
    --color-tpg15-ink: oklch(0.948 0.017 68);
    --color-tpg15-mut: #b8a593;
    --color-tpg15-mut: oklch(0.733 0.034 66);
    --color-tpg15-line: #33261d;
    --color-tpg15-line: oklch(0.281 0.025 56);
    --color-tpg15-a: #fb923c;
    --color-tpg15-a: oklch(0.758 0.159 56);
    --color-tpg15-gold: #facc15;
    --color-tpg15-gold: oklch(0.861 0.173 92);
    --color-tpg15-gold-ink: #fcd34d;
    --color-tpg15-gold-ink: oklch(0.879 0.153 92);
    --color-tpg15-halo: #f59e0b2e;
    --color-tpg15-halo: oklch(0.769 0.165 70 / 0.18);
    --color-tpg15-ring: #fdba74;
    --color-tpg15-ring: oklch(0.837 0.117 66);
    --shadow-tpg15-wire: 0 0 10px oklch(0.8 0.16 70 / 0.75);
    --shadow-tpg15-ember: 0 0 20px -6px oklch(0.75 0.16 50 / 0.55);
  }
}

.tpg-15[data-theme="dark"] {
  --color-tpg15-bg: #15100c;
  --color-tpg15-bg: oklch(0.178 0.012 61);
  --color-tpg15-glow: #7c2d1273;
  --color-tpg15-glow: oklch(0.408 0.116 38 / 0.45);
  --color-tpg15-glow2: #713f1259;
  --color-tpg15-glow2: oklch(0.421 0.090 58 / 0.35);
  --color-tpg15-ink: #f6ece2;
  --color-tpg15-ink: oklch(0.948 0.017 68);
  --color-tpg15-mut: #b8a593;
  --color-tpg15-mut: oklch(0.733 0.034 66);
  --color-tpg15-line: #33261d;
  --color-tpg15-line: oklch(0.281 0.025 56);
  --color-tpg15-a: #fb923c;
  --color-tpg15-a: oklch(0.758 0.159 56);
  --color-tpg15-gold: #facc15;
  --color-tpg15-gold: oklch(0.861 0.173 92);
  --color-tpg15-gold-ink: #fcd34d;
  --color-tpg15-gold-ink: oklch(0.879 0.153 92);
  --color-tpg15-halo: #f59e0b2e;
  --color-tpg15-halo: oklch(0.769 0.165 70 / 0.18);
  --color-tpg15-ring: #fdba74;
  --color-tpg15-ring: oklch(0.837 0.117 66);
  --shadow-tpg15-wire: 0 0 10px oklch(0.8 0.16 70 / 0.75);
  --shadow-tpg15-ember: 0 0 20px -6px oklch(0.75 0.16 50 / 0.55);
}
```
