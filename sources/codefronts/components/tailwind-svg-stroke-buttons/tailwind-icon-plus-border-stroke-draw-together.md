---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-icon-plus-border-stroke-draw-together/"
title: "Tailwind Icon Plus Border Stroke Draw Together"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "A ring hundreds of units round and a glyph a few dozen, drawing in perfect step because both carry pathLength=\"1\" and share one duration-[640ms]."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Icon Plus Border Stroke Draw Together
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-icon-plus-border-stroke-draw-together/

A ring hundreds of units round and a glyph a few dozen, drawing in perfect step because both carry pathLength="1" and share one duration-[640ms]. Multi-stroke glyphs are split into separate paths &mdash; a dash pattern restarts at every M &mdash; and the second gets delay-[60ms], which is the difference between drawn and switched on.
## HTML
```html
<section class="svgb-14 relative block w-full min-h-svh bg-svgb14-bg text-svgb14-fg font-svgb14-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-14-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-14-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-items-center p-[clamp(22px,5vw,70px)]">
    <div class="w-full max-w-215 flex flex-col gap-[clamp(20px,3.5vw,34px)]">
      <div class="flex flex-col gap-1.5">
        <h1 class="m-0 text-[clamp(28px,4.6vw,46px)] font-semibold tracking-[-0.03em]">Fjord House</h1>
        <p class="m-0 text-[15px] text-svgb14-muted">Light rain easing after noon &middot; 11&deg;</p>
      </div>
      <div class="grid gap-[clamp(12px,2vw,20px)] grid-cols-[repeat(auto-fit,minmax(min(100%,150px),1fr))]">
        <button class="group relative flex flex-col items-center gap-3.5 px-3 py-[clamp(18px,3vw,26px)] border-0 rounded-[22px] bg-svgb14-panel cursor-pointer [box-shadow:var(--svgb-14-card-sh)] transition-[transform,box-shadow] duration-[320ms] ease-svgb14 motion-reduce:!transition-none hover:-translate-y-[3px] hover:[box-shadow:var(--svgb-14-card-sh-h)] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-svgb14-stroke focus-visible:outline-offset-[3px]" type="button">
          <span class="font-svgb14-mono text-[11px] tracking-[0.16em] uppercase text-svgb14-muted">Mon</span>
          <span class="relative size-22 grid place-items-center">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:round]" viewBox="0 0 88 88" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.4]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:2]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="relative size-10 overflow-visible text-svgb14-stroke [&_path]:fill-none [&_circle]:fill-none" viewBox="0 0 32 32" aria-hidden="true">
              <circle class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" cx="16" cy="16" r="7" pathLength="1"/>
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M16 3v3m0 20v3M3 16h3m20 0h3M6.8 6.8l2.1 2.1m14.3 14.3 2.1 2.1M25.2 6.8l-2.1 2.1M8.9 23.1l-2.1 2.1" pathLength="1"/>
              <circle class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8]" cx="16" cy="16" r="7" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8] delay-[60ms]" d="M16 3v3m0 20v3M3 16h3m20 0h3M6.8 6.8l2.1 2.1m14.3 14.3 2.1 2.1M25.2 6.8l-2.1 2.1M8.9 23.1l-2.1 2.1" pathLength="1"/>
            </svg>
          </span>
          <span class="text-[21px] font-semibold tracking-[-0.02em] tabular-nums transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb14-stroke group-focus-visible:text-svgb14-stroke">14&deg;</span>
        </button>
        <button class="group relative flex flex-col items-center gap-3.5 px-3 py-[clamp(18px,3vw,26px)] border-0 rounded-[22px] bg-svgb14-panel cursor-pointer [box-shadow:var(--svgb-14-card-sh)] transition-[transform,box-shadow] duration-[320ms] ease-svgb14 motion-reduce:!transition-none hover:-translate-y-[3px] hover:[box-shadow:var(--svgb-14-card-sh-h)] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-svgb14-stroke focus-visible:outline-offset-[3px]" type="button">
          <span class="font-svgb14-mono text-[11px] tracking-[0.16em] uppercase text-svgb14-muted">Tue</span>
          <span class="relative size-22 grid place-items-center">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:round]" viewBox="0 0 88 88" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.4]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:2]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="relative size-10 overflow-visible text-svgb14-stroke [&_path]:fill-none [&_circle]:fill-none" viewBox="0 0 32 32" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M9 19a5.5 5.5 0 0 1 .8-11A7 7 0 0 1 23 10.5a4.3 4.3 0 0 1 0 8.5Z" pathLength="1"/>
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M12 23l-1.5 4M18 23l-1.5 4M24 23l-1.5 4" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8]" d="M9 19a5.5 5.5 0 0 1 .8-11A7 7 0 0 1 23 10.5a4.3 4.3 0 0 1 0 8.5Z" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8] delay-[60ms]" d="M12 23l-1.5 4M18 23l-1.5 4M24 23l-1.5 4" pathLength="1"/>
            </svg>
          </span>
          <span class="text-[21px] font-semibold tracking-[-0.02em] tabular-nums transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb14-stroke group-focus-visible:text-svgb14-stroke">11&deg;</span>
        </button>
        <button class="group relative flex flex-col items-center gap-3.5 px-3 py-[clamp(18px,3vw,26px)] border-0 rounded-[22px] bg-svgb14-panel cursor-pointer [box-shadow:var(--svgb-14-card-sh)] transition-[transform,box-shadow] duration-[320ms] ease-svgb14 motion-reduce:!transition-none hover:-translate-y-[3px] hover:[box-shadow:var(--svgb-14-card-sh-h)] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-svgb14-stroke focus-visible:outline-offset-[3px]" type="button">
          <span class="font-svgb14-mono text-[11px] tracking-[0.16em] uppercase text-svgb14-muted">Wed</span>
          <span class="relative size-22 grid place-items-center">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:round]" viewBox="0 0 88 88" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.4]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:2]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="relative size-10 overflow-visible text-svgb14-stroke [&_path]:fill-none [&_circle]:fill-none" viewBox="0 0 32 32" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M3 12h15a4 4 0 1 0-4-4" pathLength="1"/>
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M3 20h20a4 4 0 1 1-4 4" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8]" d="M3 12h15a4 4 0 1 0-4-4" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8] delay-[60ms]" d="M3 20h20a4 4 0 1 1-4 4" pathLength="1"/>
            </svg>
          </span>
          <span class="text-[21px] font-semibold tracking-[-0.02em] tabular-nums transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb14-stroke group-focus-visible:text-svgb14-stroke">9&deg;</span>
        </button>
        <button class="group relative flex flex-col items-center gap-3.5 px-3 py-[clamp(18px,3vw,26px)] border-0 rounded-[22px] bg-svgb14-panel cursor-pointer [box-shadow:var(--svgb-14-card-sh)] transition-[transform,box-shadow] duration-[320ms] ease-svgb14 motion-reduce:!transition-none hover:-translate-y-[3px] hover:[box-shadow:var(--svgb-14-card-sh-h)] motion-reduce:hover:translate-y-0 focus-visible:outline-2 focus-visible:outline-svgb14-stroke focus-visible:outline-offset-[3px]" type="button">
          <span class="font-svgb14-mono text-[11px] tracking-[0.16em] uppercase text-svgb14-muted">Thu</span>
          <span class="relative size-22 grid place-items-center">
            <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:round]" viewBox="0 0 88 88" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.4]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:2]" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="relative size-10 overflow-visible text-svgb14-stroke [&_path]:fill-none [&_circle]:fill-none" viewBox="0 0 32 32" aria-hidden="true">
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M16 5v22M6.5 10.5l19 11M25.5 10.5l-19 11" pathLength="1"/>
              <path class="stroke-svgb14-rest [stroke-width:1.6] [stroke-linecap:round] [stroke-linejoin:round]" d="M16 5l-3 3m3-3 3 3m-3 22-3-3m3 3 3-3" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8]" d="M16 5v22M6.5 10.5l19 11M25.5 10.5l-19 11" pathLength="1"/>
              <path class="stroke-svgb14-stroke [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[640ms] ease-svgb14 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 [stroke-width:1.8] delay-[60ms]" d="M16 5l-3 3m3-3 3 3m-3 22-3-3m3 3 3-3" pathLength="1"/>
            </svg>
          </span>
          <span class="text-[21px] font-semibold tracking-[-0.02em] tabular-nums transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb14-stroke group-focus-visible:text-svgb14-stroke">4&deg;</span>
        </button>
      </div>
      <div class="flex flex-wrap gap-4">
        <span class="font-svgb14-mono text-[10.5px] text-svgb14-muted">scalloped ring &middot; 12 lobes</span>
        <span class="font-svgb14-mono text-[10.5px] text-svgb14-muted">glyph 40&ndash;90 units</span>
        <span class="font-svgb14-mono text-[10.5px] text-svgb14-muted">pathLength 1 &middot; one duration</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb14-bg: #eef1e9;
  --color-svgb14-bg: oklch(0.945 0.015 130);
  --color-svgb14-fg: #1a201a;
  --color-svgb14-fg: oklch(0.225 0.015 145);
  --color-svgb14-muted: #6b7568;
  --color-svgb14-muted: oklch(0.545 0.018 140);
  --color-svgb14-panel: #f8faf5;
  --color-svgb14-panel: oklch(0.982 0.008 130);
  --color-svgb14-rest: rgba(26, 32, 26, 0.14);
  --color-svgb14-rest: oklch(0.225 0.015 145 / 0.14);
  --color-svgb14-stroke: #2f6b4f;
  --color-svgb14-stroke: oklch(0.47 0.10 158);
  --font-svgb14-sans: 'Nunito', system-ui, sans-serif;
  --font-svgb14-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-svgb14: cubic-bezier(0.22, 1, 0.36, 1);
}
/* Card elevation is scheme-dependent: a cast shadow on paper, an inset hairline
   on ink. Two variables keep both states out of the markup. */

.svgb-14 {
  --svgb-14-card-sh: 0 1px 2px oklch(0 0 0 / 0.04);
  --svgb-14-card-sh-h: 0 10px 26px -18px oklch(0 0 0 / 0.4);
}

.svgb-14:has(#svgb-14-theme:checked) {
  --color-svgb14-bg: #101410;
  --color-svgb14-bg: oklch(0.185 0.012 145);
  --color-svgb14-fg: #eaf0e8;
  --color-svgb14-fg: oklch(0.945 0.012 140);
  --color-svgb14-muted: #8b978a;
  --color-svgb14-muted: oklch(0.665 0.018 140);
  --color-svgb14-panel: #171d17;
  --color-svgb14-panel: oklch(0.235 0.014 145);
  --color-svgb14-rest: rgba(234, 240, 232, 0.16);
  --color-svgb14-rest: oklch(0.945 0.012 140 / 0.16);
  --color-svgb14-stroke: #86e0ac;
  --color-svgb14-stroke: oklch(0.86 0.13 155);
  --svgb-14-card-sh: inset 0 0 0 1px oklch(1 0 0 / 0.05);
  --svgb-14-card-sh-h: inset 0 0 0 1px oklch(1 0 0 / 0.08), 0 14px 30px -22px #000;
}
```
