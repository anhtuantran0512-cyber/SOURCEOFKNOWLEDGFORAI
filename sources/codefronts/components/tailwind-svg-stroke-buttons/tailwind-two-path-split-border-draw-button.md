---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-two-path-split-border-draw-button/"
title: "Tailwind Two Path Split Border Draw Button"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Two halves, one constant &mdash; and in Tailwind the constant is literally shared, because both paths carry the same class list character for character."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Two Path Split Border Draw Button
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-two-path-split-border-draw-button/

Two halves, one constant &mdash; and in Tailwind the constant is literally shared, because both paths carry the same class list character for character. The seam flash is built entirely from pseudo-element variants, from after:content-[''] through hover:after:delay-[620ms], where the delay equals the draw duration so the tear lands exactly as the two heads meet.
## HTML
```html
<section class="svgb-04 relative block w-full min-h-svh overflow-hidden bg-svgb04-bg text-svgb04-fg font-svgb04-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-04-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/8 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-04-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="relative min-h-svh grid place-items-center p-[clamp(24px,6vw,72px)]">
    <div class="flex flex-col items-center gap-[clamp(12px,2vw,18px)] text-center">
      <p class="m-0 font-svgb04-mono text-[11px] tracking-[0.34em] uppercase text-svgb04-stroke">Now showing</p>
      <h1 class="m-0 font-svgb04-display text-[clamp(46px,11vw,116px)] leading-[0.88] tracking-[-0.02em] uppercase">The Long<br>Exposure</h1>
      <p class="m-0 mb-[clamp(10px,2vw,18px)] text-[13px] tracking-[0.12em] uppercase text-svgb04-muted">70mm &middot; 142 min &middot; Screen 4 &middot; 20:45</p>

      <button class="group relative w-[min(300px,92vw)] h-23 flex items-stretch border-0 p-0 bg-svgb04-fg/5 cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb04-stroke focus-visible:outline-offset-[5px] after:content-[''] after:absolute after:inset-x-[42%] after:-bottom-[7px] after:h-0.5 after:bg-svgb04-stroke after:opacity-0 after:scale-x-[0.2] after:[transition:opacity_200ms_ease,transform_320ms_var(--ease-svgb04)] hover:after:opacity-90 hover:after:scale-x-100 hover:after:delay-[620ms] focus-visible:after:opacity-90 focus-visible:after:scale-x-100 focus-visible:after:delay-[620ms] motion-reduce:after:transition-none" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 300 92" aria-hidden="true">
          <path class="fill-none stroke-svgb04-rest [stroke-width:1.4]" d="M150 2H290A8 8 0 0 1 298 10V37A9 9 0 0 0 298 55V82A8 8 0 0 1 290 90H150" vector-effect="non-scaling-stroke"/>
          <path class="fill-none stroke-svgb04-rest [stroke-width:1.4]" d="M150 2H10A8 8 0 0 0 2 10V37A9 9 0 0 1 2 55V82A8 8 0 0 0 10 90H150" vector-effect="non-scaling-stroke"/>
          <path class="fill-none stroke-svgb04-rest [stroke-width:1.4] [stroke-dasharray:3_5] [stroke-linecap:round]" d="M150 12V80" vector-effect="non-scaling-stroke"/>
          <path class="fill-none stroke-svgb04-stroke [stroke-width:2] [stroke-linecap:butt] [stroke-dasharray:392] [stroke-dashoffset:392] transition-[stroke-dashoffset] duration-[620ms] ease-svgb04 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M150 2H290A8 8 0 0 1 298 10V37A9 9 0 0 0 298 55V82A8 8 0 0 1 290 90H150" vector-effect="non-scaling-stroke"/>
          <path class="fill-none stroke-svgb04-stroke [stroke-width:2] [stroke-linecap:butt] [stroke-dasharray:392] [stroke-dashoffset:392] transition-[stroke-dashoffset] duration-[620ms] ease-svgb04 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M150 2H10A8 8 0 0 0 2 10V37A9 9 0 0 1 2 55V82A8 8 0 0 0 10 90H150" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="relative z-[1] flex-1 flex flex-col justify-center gap-1">
          <span class="font-svgb04-mono text-[9.5px] tracking-[0.2em] uppercase text-svgb04-muted">Seat</span>
          <span class="text-[19px] font-bold tracking-[-0.01em] transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb04-stroke group-focus-visible:text-svgb04-stroke">J-14</span>
        </span>
        <span class="relative z-[1] flex-[1.4] flex flex-col justify-center gap-1">
          <span class="font-svgb04-mono text-[9.5px] tracking-[0.2em] uppercase text-svgb04-muted">Admit one</span>
          <span class="text-[19px] font-bold tracking-[-0.01em] transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb04-stroke group-focus-visible:text-svgb04-stroke">Reserve</span>
        </span>
      </button>

      <div class="flex flex-col items-center gap-2.5 mt-[clamp(14px,3vw,24px)]">
        <button class="group relative w-44 h-13 grid place-items-center border-0 p-0 bg-transparent text-[13.5px] font-medium cursor-pointer focus-visible:outline-2 focus-visible:outline-svgb04-stroke focus-visible:outline-offset-4" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 176 52" aria-hidden="true">
            <path class="fill-none stroke-svgb04-rest [stroke-width:1.4]" d="M2 26V10A8 8 0 0 1 10 2H166A8 8 0 0 1 174 10V26" vector-effect="non-scaling-stroke"/>
            <path class="fill-none stroke-svgb04-rest [stroke-width:1.4]" d="M2 26V42A8 8 0 0 0 10 50H166A8 8 0 0 0 174 42V26" vector-effect="non-scaling-stroke"/>
            <path class="fill-none stroke-svgb04-fg [stroke-width:1.8] [stroke-linecap:butt] [stroke-dasharray:218] [stroke-dashoffset:218] transition-[stroke-dashoffset] duration-[520ms] ease-svgb04 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M2 26V10A8 8 0 0 1 10 2H166A8 8 0 0 1 174 10V26" vector-effect="non-scaling-stroke"/>
            <path class="fill-none stroke-svgb04-fg [stroke-width:1.8] [stroke-linecap:butt] [stroke-dasharray:218] [stroke-dashoffset:218] transition-[stroke-dashoffset] duration-[520ms] ease-svgb04 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M2 26V42A8 8 0 0 0 10 50H166A8 8 0 0 0 174 42V26" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1]">Add to calendar</span>
        </button>
        <span class="font-svgb04-mono text-[10.5px] tracking-[0.08em] text-svgb04-muted">side seam &middot; 213.1 measured &rarr; 218 + 218</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb04-bg: #1b0e0c;
  --color-svgb04-bg: oklch(0.20 0.04 30);
  --color-svgb04-fg: #f6ece0;
  --color-svgb04-fg: oklch(0.95 0.02 70);
  --color-svgb04-muted: #b09287;
  --color-svgb04-muted: oklch(0.70 0.035 40);
  --color-svgb04-rest: rgba(246, 236, 224, 0.2);
  --color-svgb04-rest: oklch(0.95 0.02 70 / 0.2);
  --color-svgb04-stroke: #ffb84d;
  --color-svgb04-stroke: oklch(0.83 0.14 70);
  --font-svgb04-sans: 'Manrope', system-ui, sans-serif;
  --font-svgb04-display: 'Anton', 'Archivo', system-ui, sans-serif;
  --font-svgb04-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --ease-svgb04: cubic-bezier(0.33, 1, 0.68, 1);
}
/* Projector haze plus scan lines: two stacked decorative layers, which stay in
   CSS because as one arbitrary utility they would be unreadable. */

.svgb-04::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(120% 80% at 50% -10%, color-mix(in oklab, var(--color-svgb04-stroke) 16%, transparent), transparent 60%), repeating-linear-gradient(0deg, oklch(0 0 0 / 0.14) 0 1px, transparent 1px 4px);
}

.svgb-04:has(#svgb-04-theme:checked) {
  --color-svgb04-bg: #f7efe4;
  --color-svgb04-bg: oklch(0.955 0.02 75);
  --color-svgb04-fg: #24110d;
  --color-svgb04-fg: oklch(0.235 0.045 32);
  --color-svgb04-muted: #7a5346;
  --color-svgb04-muted: oklch(0.50 0.05 40);
  --color-svgb04-rest: rgba(36, 17, 13, 0.24);
  --color-svgb04-rest: oklch(0.235 0.045 32 / 0.24);
  --color-svgb04-stroke: #b62d0e;
  --color-svgb04-stroke: oklch(0.51 0.19 33);
}
```
