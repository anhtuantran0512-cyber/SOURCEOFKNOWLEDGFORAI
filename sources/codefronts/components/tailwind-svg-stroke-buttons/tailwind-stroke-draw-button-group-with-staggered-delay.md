---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-group-with-staggered-delay/"
title: "Tailwind Stroke Draw Button Group with Staggered Delay"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "A wave across six platform tabs, driven entirely from the markup: group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] reads each item's own inline…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Draw Button Group with Staggered Delay
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-group-with-staggered-delay/

A wave across six platform tabs, driven entirely from the markup: group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] reads each item's own inline --i, so adding a seventh platform needs no CSS at all. Two named groups do two jobs &mdash; group/rail owns the wave, group/tab owns the individual lift &mdash; and the pointer-origin version stays in CSS, because there is no variant for two siblings after the hovered one.
## HTML
```html
<section class="svgb-18 relative block w-full min-h-svh bg-svgb18-bg text-svgb18-fg font-svgb18-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-18-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-sm border border-current/22 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/14 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-18-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh flex flex-col items-center justify-center gap-[clamp(22px,4vh,42px)] p-[clamp(20px,5vw,64px)]">
    <div class="w-full max-w-205 flex flex-col">
      <div class="grid grid-cols-[74px_1fr_52px_110px] gap-3 items-baseline py-[11px] border-b border-svgb18-rest font-svgb18-mono text-[10px] tracking-[0.2em] uppercase text-svgb18-muted">
        <span>Time</span><span>Destination</span><span>Plat</span><span>Status</span>
      </div>
      <div class="grid grid-cols-[74px_1fr_52px_110px] gap-3 items-baseline py-[11px] border-b border-svgb18-rest text-[clamp(17px,2.4vw,23px)] tracking-[0.02em] uppercase tabular-nums [&>span:nth-child(3)]:text-svgb18-stroke"><span>19:42</span><span>Gent Sint-Pieters</span><span>3</span><span class="text-svgb18-muted text-[0.72em] tracking-[0.14em]">On time</span></div>
      <div class="grid grid-cols-[74px_1fr_52px_110px] gap-3 items-baseline py-[11px] border-b border-svgb18-rest text-[clamp(17px,2.4vw,23px)] tracking-[0.02em] uppercase tabular-nums [&>span:nth-child(3)]:text-svgb18-stroke"><span>19:55</span><span>Antwerpen Centraal</span><span>1</span><span class="text-svgb18-muted text-[0.72em] tracking-[0.14em]">Boarding</span></div>
      <div class="grid grid-cols-[74px_1fr_52px_110px] gap-3 items-baseline py-[11px] border-b border-svgb18-rest text-[clamp(17px,2.4vw,23px)] tracking-[0.02em] uppercase tabular-nums [&>span:nth-child(3)]:text-svgb18-stroke"><span>20:04</span><span>Maastricht</span><span>6</span><span class="text-svgb18-late text-[0.72em] tracking-[0.14em]">+8 min</span></div>
    </div>

    <div class="svgb-18__rail group/rail flex flex-wrap justify-center gap-[clamp(8px,1.6vw,16px)]" role="group" aria-label="Platforms">
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:0">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">1</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:1">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">2</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:2">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">3</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:3">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">4</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:4">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">5</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
      <button class="svgb-18__tab group/tab relative w-30 h-29 flex flex-col items-center justify-center gap-0.5 border-0 p-0 bg-transparent cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb18-stroke focus-visible:outline-offset-4" type="button" style="--i:5">
        <svg class="absolute inset-0 w-full h-full overflow-visible [&_path]:fill-none [&_path]:[stroke-linejoin:miter]" viewBox="0 0 120 116" aria-hidden="true">
          <path class="stroke-svgb18-rest [stroke-width:1.4]" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink stroke-svgb18-stroke [stroke-width:2.2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[520ms] ease-svgb18 delay-[calc((5-var(--i,0))*var(--svgb-18-out))] group-hover/rail:[stroke-dashoffset:0] group-hover/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] group-focus-within/rail:[stroke-dashoffset:0] group-focus-within/rail:delay-[calc(var(--i,0)*var(--svgb-18-step))] motion-reduce:!transition-none motion-reduce:!delay-0 motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover/rail:opacity-100 motion-reduce:group-focus-within/rail:opacity-100" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] order-2 text-[46px] font-semibold leading-none tabular-nums transition-[color,translate] duration-[380ms] ease-svgb18 motion-reduce:transition-none group-hover/rail:text-svgb18-stroke group-focus-within/rail:text-svgb18-stroke group-hover/tab:-translate-y-[3px] motion-reduce:group-hover/tab:translate-y-0">6</span>
        <span class="relative z-[1] order-1 font-svgb18-mono text-[9.5px] tracking-[0.24em] uppercase text-svgb18-muted">Plat</span>
      </button>
    </div>
    <div class="flex flex-wrap justify-center gap-[18px]">
      <span class="font-svgb18-mono text-[10.5px] text-svgb18-muted">hover the rail &rarr; index wave &middot; 70ms step</span>
      <span class="font-svgb18-mono text-[10.5px] text-svgb18-muted">hover one tab &rarr; wave from that tab</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb18-bg: #0a0a09;
  --color-svgb18-bg: oklch(0.145 0.004 90);
  --color-svgb18-fg: #f0eee6;
  --color-svgb18-fg: oklch(0.95 0.01 95);
  --color-svgb18-muted: #8b887c;
  --color-svgb18-muted: oklch(0.66 0.014 95);
  --color-svgb18-rest: rgba(240, 238, 230, 0.14);
  --color-svgb18-rest: oklch(0.95 0.01 95 / 0.14);
  --color-svgb18-stroke: #ffc400;
  --color-svgb18-stroke: oklch(0.85 0.18 90);
  --color-svgb18-late: #ff7043;
  --color-svgb18-late: oklch(0.72 0.17 42);
  --font-svgb18-sans: 'Barlow Condensed', system-ui, sans-serif;
  --font-svgb18-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-svgb18: cubic-bezier(0.22, 1, 0.36, 1);
}
/* One step in, a shorter step out. Every delay in the markup is calc() on
   these two and the item's own inline --i. */

.svgb-18 {
  --svgb-18-step: 70ms;
  --svgb-18-out: 40ms;
}
/* Distance from the hovered tab, which a variant cannot express: these need
   real adjacent-sibling chains and :has(). The index wave lives in the markup;
   this is the pointer-origin wave layered over it. */

.svgb-18__tab:hover .svgb-18__ink {
  transition-delay: 0ms;
}

.svgb-18__tab:hover + .svgb-18__tab .svgb-18__ink {
  transition-delay: var(--svgb-18-step);
}

.svgb-18__tab:hover + .svgb-18__tab + .svgb-18__tab .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 2);
}

.svgb-18__tab:hover + .svgb-18__tab + .svgb-18__tab + .svgb-18__tab .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 3);
}

.svgb-18__tab:has(+ .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: var(--svgb-18-step);
}

.svgb-18__tab:has(+ .svgb-18__tab + .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 2);
}

.svgb-18__tab:has(+ .svgb-18__tab + .svgb-18__tab + .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 3);
}

.svgb-18:has(#svgb-18-theme:checked) {
  --color-svgb18-bg: #f3f2ec;
  --color-svgb18-bg: oklch(0.958 0.008 95);
  --color-svgb18-fg: #14140f;
  --color-svgb18-fg: oklch(0.195 0.008 95);
  --color-svgb18-muted: #5d5b50;
  --color-svgb18-muted: oklch(0.49 0.014 95);
  --color-svgb18-rest: rgba(20, 20, 15, 0.16);
  --color-svgb18-rest: oklch(0.195 0.008 95 / 0.16);
  --color-svgb18-stroke: #7a5200;
  --color-svgb18-stroke: oklch(0.49 0.13 84);
  --color-svgb18-late: #a5401c;
  --color-svgb18-late: oklch(0.48 0.16 42);
}
```
