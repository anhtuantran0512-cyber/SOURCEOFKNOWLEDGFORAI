---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-airport-departures-board-tooltip-flight-detail-card/"
title: "Tailwind Airport Departures Board Tooltip with Flight Detail Card"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A Solari-flap departures board in amber on charcoal: hover a flight row and a detail card drops with airline, route diagram, aircraft grid and gate timing."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Airport Departures Board Tooltip with Flight Detail Card
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-airport-departures-board-tooltip-flight-detail-card/

A Solari-flap departures board in amber on charcoal: hover a flight row and a detail card drops with airline, route diagram, aircraft grid and gate timing. The port's neat trick is that the six-column grid track list is declared once as an arbitrary value and reused by the header and every row.
## HTML
```html
<section class="ttp-13 w-full min-h-svh bg-ttp13-bg px-7 pt-9 pb-[320px] font-ttp13-mono">
  <div class="mx-auto max-w-[720px] rounded border border-ttp13-edge bg-ttp13-board">
    <div class="grid grid-cols-[60px_90px_1fr_50px_50px_90px] gap-3 border-b border-ttp13-edge px-4.5 py-2.5 text-[9.5px] uppercase tracking-[0.14em] text-ttp13-dim">
      <span>Time</span><span>Flight</span><span>Destination</span><span>Term</span><span>Gate</span><span>Status</span>
    </div>

    <div class="group relative grid cursor-help grid-cols-[60px_90px_1fr_50px_50px_90px] items-center gap-3 border-b border-ttp13-edge px-4.5 py-3.25 transition-colors duration-100 hover:bg-white/3" tabindex="0" role="button" aria-describedby="ttp13-f1">
      <span class="text-base font-medium tracking-[0.06em] text-ttp13-amber">06:15</span>
      <span class="text-xs text-ttp13-ink">AA 2847</span>
      <span class="text-[13px] tracking-[0.02em] text-ttp13-bright">New York <small class="ml-1.5 text-[10px] text-ttp13-dim">JFK</small></span>
      <span class="text-xs text-ttp13-ink">T3</span>
      <span class="text-[13px] font-medium text-ttp13-gate">B12</span>
      <span class="text-[10.5px] font-medium tracking-[0.05em] text-ttp13-dim">Departed</span>
      <div id="ttp13-f1" role="tooltip" class="ttp13-card">
        <div class="ttp13-head"><div><div class="ttp13-airline">American Airlines</div><div class="ttp13-num">AA 2847</div></div><span class="ttp13-badge border-ttp13-edge bg-white/5 text-ttp13-ink">Departed</span></div>
        <div class="ttp13-route"><div class="text-center"><div class="ttp13-code">LAX</div><div class="ttp13-city">Los Angeles</div></div><div class="relative flex flex-1 items-center"><div class="relative h-px flex-1 bg-linear-to-r from-ttp13-edge via-ttp13-line to-ttp13-edge"><div class="absolute -top-3.25 w-full text-center text-[9px] tracking-[0.08em] text-ttp13-dim">5h 22m</div></div><div class="shrink-0 text-[13px] text-ttp13-ink">→</div></div><div class="text-center"><div class="ttp13-code">JFK</div><div class="ttp13-city">New York</div></div></div>
        <div class="grid grid-cols-4 border-b border-ttp13-edge"><div class="ttp13-cell"><div class="ttp13-clabel">Aircraft</div><div class="ttp13-cval">B737-800</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Seats</div><div class="ttp13-cval">162</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Class</div><div class="ttp13-cval">F / Y</div></div><div class="ttp13-cell border-r-0"><div class="ttp13-clabel">Meals</div><div class="ttp13-cval">Yes</div></div></div>
        <div class="ttp13-foot"><span>Departed 06:09 · 6 min early</span><span>T3 · Gate B12</span></div>
      </div>
    </div>

    <div class="group relative grid cursor-help grid-cols-[60px_90px_1fr_50px_50px_90px] items-center gap-3 border-b border-ttp13-edge px-4.5 py-3.25 transition-colors duration-100 hover:bg-white/3" tabindex="0" role="button" aria-describedby="ttp13-f2">
      <span class="text-base font-medium tracking-[0.06em] text-ttp13-amber">07:40</span>
      <span class="text-xs text-ttp13-ink">UA 5512</span>
      <span class="text-[13px] tracking-[0.02em] text-ttp13-bright">Chicago <small class="ml-1.5 text-[10px] text-ttp13-dim">ORD</small></span>
      <span class="text-xs text-ttp13-ink">T7</span>
      <span class="text-[13px] font-medium text-ttp13-gate">C04</span>
      <span class="text-[10.5px] font-medium tracking-[0.05em] text-ttp13-ok">On Time</span>
      <div id="ttp13-f2" role="tooltip" class="ttp13-card">
        <div class="ttp13-head"><div><div class="ttp13-airline">United Airlines</div><div class="ttp13-num">UA 5512</div></div><span class="ttp13-badge border-ttp13-ok/25 bg-ttp13-ok/12 text-ttp13-ok">On Time</span></div>
        <div class="ttp13-route"><div class="text-center"><div class="ttp13-code">LAX</div><div class="ttp13-city">Los Angeles</div></div><div class="relative flex flex-1 items-center"><div class="relative h-px flex-1 bg-linear-to-r from-ttp13-edge via-ttp13-line to-ttp13-edge"><div class="absolute -top-3.25 w-full text-center text-[9px] tracking-[0.08em] text-ttp13-dim">3h 55m</div></div><div class="shrink-0 text-[13px] text-ttp13-ink">→</div></div><div class="text-center"><div class="ttp13-code">ORD</div><div class="ttp13-city">Chicago</div></div></div>
        <div class="grid grid-cols-4 border-b border-ttp13-edge"><div class="ttp13-cell"><div class="ttp13-clabel">Aircraft</div><div class="ttp13-cval">A320neo</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Seats</div><div class="ttp13-cval">150</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Class</div><div class="ttp13-cval">J / Y</div></div><div class="ttp13-cell border-r-0"><div class="ttp13-clabel">Wi-Fi</div><div class="ttp13-cval">Yes</div></div></div>
        <div class="ttp13-foot"><span>Boards 07:10 · Gate closes 07:25</span><span>T7 · Gate C04</span></div>
      </div>
    </div>

    <div class="group relative grid cursor-help grid-cols-[60px_90px_1fr_50px_50px_90px] items-center gap-3 border-b border-ttp13-edge px-4.5 py-3.25 transition-colors duration-100 hover:bg-white/3" tabindex="0" role="button" aria-describedby="ttp13-f3">
      <span class="text-base font-medium tracking-[0.06em] text-ttp13-amber">08:20</span>
      <span class="text-xs text-ttp13-ink">DL 8831</span>
      <span class="text-[13px] tracking-[0.02em] text-ttp13-bright">London <small class="ml-1.5 text-[10px] text-ttp13-dim">LHR</small></span>
      <span class="text-xs text-ttp13-ink">TB</span>
      <span class="text-[13px] font-medium text-ttp13-gate">A22</span>
      <span class="text-[10.5px] font-medium tracking-[0.05em] text-ttp13-amber animate-ttp13-blink motion-reduce:animate-none">Boarding</span>
      <div id="ttp13-f3" role="tooltip" class="ttp13-card">
        <div class="ttp13-head"><div><div class="ttp13-airline">Delta Air Lines</div><div class="ttp13-num">DL 8831</div></div><span class="ttp13-badge border-ttp13-amber/25 bg-ttp13-amber/12 text-ttp13-amber">Boarding</span></div>
        <div class="ttp13-route"><div class="text-center"><div class="ttp13-code">LAX</div><div class="ttp13-city">Los Angeles</div></div><div class="relative flex flex-1 items-center"><div class="relative h-px flex-1 bg-linear-to-r from-ttp13-edge via-ttp13-line to-ttp13-edge"><div class="absolute -top-3.25 w-full text-center text-[9px] tracking-[0.08em] text-ttp13-dim">10h 15m</div></div><div class="shrink-0 text-[13px] text-ttp13-ink">→</div></div><div class="text-center"><div class="ttp13-code">LHR</div><div class="ttp13-city">London</div></div></div>
        <div class="grid grid-cols-4 border-b border-ttp13-edge"><div class="ttp13-cell"><div class="ttp13-clabel">Aircraft</div><div class="ttp13-cval">B767-400</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Seats</div><div class="ttp13-cval">245</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Class</div><div class="ttp13-cval">F / J / Y</div></div><div class="ttp13-cell border-r-0"><div class="ttp13-clabel">Meals</div><div class="ttp13-cval">Yes</div></div></div>
        <div class="ttp13-foot"><span>Now boarding all groups · Final call</span><span>TB · Gate A22</span></div>
      </div>
    </div>

    <div class="group relative grid cursor-help grid-cols-[60px_90px_1fr_50px_50px_90px] items-center gap-3 px-4.5 py-3.25 transition-colors duration-100 hover:bg-white/3" tabindex="0" role="button" aria-describedby="ttp13-f4">
      <span class="text-base font-medium tracking-[0.06em] text-ttp13-amber">10:30</span>
      <span class="text-xs text-ttp13-ink">SQ 7736</span>
      <span class="text-[13px] tracking-[0.02em] text-ttp13-bright">Singapore <small class="ml-1.5 text-[10px] text-ttp13-dim">SIN</small></span>
      <span class="text-xs text-ttp13-ink">TB</span>
      <span class="text-[13px] font-medium text-ttp13-gate">B44</span>
      <span class="text-[10.5px] font-medium tracking-[0.05em] text-ttp13-late">Delayed 45m</span>
      <div id="ttp13-f4" role="tooltip" class="ttp13-card">
        <div class="ttp13-head"><div><div class="ttp13-airline">Singapore Airlines</div><div class="ttp13-num">SQ 7736</div></div><span class="ttp13-badge border-ttp13-late/25 bg-ttp13-late/12 text-ttp13-late">Delayed 45m</span></div>
        <div class="ttp13-route"><div class="text-center"><div class="ttp13-code">LAX</div><div class="ttp13-city">Los Angeles</div></div><div class="relative flex flex-1 items-center"><div class="relative h-px flex-1 bg-linear-to-r from-ttp13-edge via-ttp13-line to-ttp13-edge"><div class="absolute -top-3.25 w-full text-center text-[9px] tracking-[0.08em] text-ttp13-dim">17h 30m</div></div><div class="shrink-0 text-[13px] text-ttp13-ink">→</div></div><div class="text-center"><div class="ttp13-code">SIN</div><div class="ttp13-city">Singapore</div></div></div>
        <div class="grid grid-cols-4 border-b border-ttp13-edge"><div class="ttp13-cell"><div class="ttp13-clabel">Aircraft</div><div class="ttp13-cval">A350-900ULR</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Seats</div><div class="ttp13-cval">161</div></div><div class="ttp13-cell"><div class="ttp13-clabel">Class</div><div class="ttp13-cval">J / Y</div></div><div class="ttp13-cell border-r-0"><div class="ttp13-clabel">Meals</div><div class="ttp13-cval">2× hot</div></div></div>
        <div class="ttp13-foot"><span>Late inbound aircraft · New ETD 11:15</span><span>TB · Gate B44</span></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp13-bg: #111111;
  --color-ttp13-bg: oklch(0.18 0 0);
  --color-ttp13-board: #181818;
  --color-ttp13-board: oklch(0.21 0 0);
  --color-ttp13-card: #1c1c1c;
  --color-ttp13-card: oklch(0.23 0 0);
  --color-ttp13-head: #232323;
  --color-ttp13-head: oklch(0.26 0 0);
  --color-ttp13-edge: #333333;
  --color-ttp13-edge: oklch(0.33 0 0);
  --color-ttp13-line: #4a4a4a;
  --color-ttp13-line: oklch(0.44 0 0);
  --color-ttp13-bright: #e0e0e0;
  --color-ttp13-bright: oklch(0.9 0 0);
  --color-ttp13-ink: #a8a8a8;
  --color-ttp13-ink: oklch(0.73 0 0);
  --color-ttp13-dim: #8c8c8c;
  --color-ttp13-dim: oklch(0.63 0 0);
  --color-ttp13-amber: #e8a020;
  --color-ttp13-amber: oklch(0.75 0.14 70);
  --color-ttp13-gate: #d8952c;
  --color-ttp13-gate: oklch(0.71 0.12 72);
  --color-ttp13-ok: #3ec971;
  --color-ttp13-ok: oklch(0.74 0.17 150);
  --color-ttp13-late: #f2694a;
  --color-ttp13-late: oklch(0.68 0.17 35);
  --font-ttp13-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-ttp13-blink: ttp13-blink 1.2s ease-in-out infinite;
}

@keyframes ttp13-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0.45;
  }
}

.ttp-13 {
  width: 100%;
  min-height: 100svh;
}
/* Four flight cards of identical anatomy; the per-flight data is the
   only thing that differs, so the shell and its five sections are
   @apply classes and the rows stay scannable in source. */

.ttp-13 .ttp13-card {
  @apply pointer-events-none invisible absolute top-[calc(100%+8px)] left-1/2 z-100 w-90 max-w-[calc(100vw-48px)] -translate-x-1/2 translate-y-1.5 overflow-hidden rounded-lg border border-ttp13-edge bg-ttp13-card text-left opacity-0 shadow-[0_20px_60px_rgba(0,0,0,0.95)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-y-0 group-focus-within:opacity-100;
}

.ttp-13 .ttp13-head {
  @apply flex items-start justify-between border-b border-ttp13-edge bg-ttp13-head px-4 py-3.25;
}

.ttp-13 .ttp13-airline {
  @apply text-[10.5px] tracking-[0.08em] text-ttp13-dim;
}

.ttp-13 .ttp13-num {
  @apply mt-0.5 text-lg font-medium text-ttp13-amber;
}

.ttp-13 .ttp13-badge {
  @apply rounded-[3px] border px-2.25 py-0.75 text-[9.5px] font-medium tracking-[0.08em];
}

.ttp-13 .ttp13-route {
  @apply flex items-center gap-3 border-b border-ttp13-edge px-4 py-3.5;
}

.ttp-13 .ttp13-code {
  @apply text-xl font-medium tracking-[0.04em] text-ttp13-bright;
}

.ttp-13 .ttp13-city {
  @apply mt-0.75 text-[9px] uppercase tracking-[0.1em] text-ttp13-dim;
}

.ttp-13 .ttp13-cell {
  @apply border-r border-ttp13-edge px-3.5 py-2.25;
}

.ttp-13 .ttp13-clabel {
  @apply mb-1 text-[8.5px] uppercase tracking-[0.1em] text-ttp13-dim;
}

.ttp-13 .ttp13-cval {
  @apply text-[11.5px] text-ttp13-ink;
}

.ttp-13 .ttp13-foot {
  @apply flex justify-between px-4 py-2.25 text-[9.5px] tracking-[0.06em] text-ttp13-dim;
}
```
