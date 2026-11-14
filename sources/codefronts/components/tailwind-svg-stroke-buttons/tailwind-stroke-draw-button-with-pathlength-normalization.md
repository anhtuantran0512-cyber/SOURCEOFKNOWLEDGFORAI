---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-with-pathlength-normalization/"
title: "Tailwind Stroke Draw Button with pathLength Normalization"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Five silhouettes &mdash; hexagon, diamond, shield, octagon, ring &mdash; animated by one class string, character for character, apart from colour."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Draw Button with pathLength Normalization
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-with-pathlength-normalization/

Five silhouettes &mdash; hexagon, diamond, shield, octagon, ring &mdash; animated by one class string, character for character, apart from colour. Because every path carries pathLength="1", [stroke-dasharray:1] [stroke-dashoffset:1] is a complete outline on all of them, which means the string is genuinely reusable: extract it into an @utility and it animates any shape you point it at.
## HTML
```html
<section class="svgb-11 relative block w-full min-h-svh overflow-hidden bg-svgb11-bg text-svgb11-fg font-svgb11-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-11-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 border border-current/24 bg-current/8 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/16 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-11-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="relative min-h-svh flex flex-col items-center justify-center gap-[clamp(14px,3vh,30px)] p-[clamp(22px,5vw,70px)] text-center">
    <p class="m-0 font-svgb11-mono text-[11px] tracking-[0.3em] uppercase text-svgb11-alt animate-svgb11-blink motion-reduce:animate-none">Insert coin &middot; 1 credit</p>
    <h1 class="m-0 text-[clamp(40px,9vw,96px)] font-bold tracking-[-0.02em] uppercase leading-[0.95] [text-shadow:var(--svgb-11-logo-sh)] [&_span]:text-svgb11-stroke">Vector<span>Runner</span></h1>
    <div class="flex flex-wrap justify-center items-center gap-[clamp(12px,2.4vw,26px)]">
      <button class="group relative grid place-items-center border-0 p-0 bg-transparent text-[15px] font-semibold tracking-[0.14em] uppercase cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb11-alt focus-visible:outline-offset-[6px] w-50 h-24" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 96" aria-hidden="true">
          <path class="fill-none stroke-svgb11-rest [stroke-width:1.6]" d="M40 4H160L196 48L160 92H40L4 48Z" pathLength="1"/>
          <path class="fill-none [stroke-width:2.4] [stroke-linecap:butt] [stroke-linejoin:miter] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 stroke-svgb11-stroke [filter:var(--svgb-11-glow)]" d="M40 4H160L196 48L160 92H40L4 48Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] transition-[color,text-shadow] duration-[260ms] motion-reduce:transition-none group-hover:text-svgb11-stroke group-hover:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)] group-focus-visible:text-svgb11-stroke group-focus-visible:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)]">Start</span>
      </button>
      <button class="group relative grid place-items-center border-0 p-0 bg-transparent text-[15px] font-semibold tracking-[0.14em] uppercase cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb11-alt focus-visible:outline-offset-[6px] w-40 h-24" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 160 96" aria-hidden="true">
          <path class="fill-none stroke-svgb11-rest [stroke-width:1.6]" d="M80 4L156 48L80 92L4 48Z" pathLength="1"/>
          <path class="fill-none [stroke-width:2.4] [stroke-linecap:butt] [stroke-linejoin:miter] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 stroke-svgb11-alt [filter:var(--svgb-11-glow-alt)]" d="M80 4L156 48L80 92L4 48Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] transition-[color,text-shadow] duration-[260ms] motion-reduce:transition-none group-hover:text-svgb11-alt group-hover:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-alt)_70%,transparent)] group-focus-visible:text-svgb11-alt group-focus-visible:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-alt)_70%,transparent)]">Co-op</span>
      </button>
      <button class="group relative grid place-items-center border-0 p-0 bg-transparent text-[15px] font-semibold tracking-[0.14em] uppercase cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb11-alt focus-visible:outline-offset-[6px] w-40 h-26" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 160 104" aria-hidden="true">
          <path class="fill-none stroke-svgb11-rest [stroke-width:1.6]" d="M80 4L152 24V58C152 82 118 96 80 100C42 96 8 82 8 58V24Z" pathLength="1"/>
          <path class="fill-none [stroke-width:2.4] [stroke-linecap:butt] [stroke-linejoin:miter] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 stroke-svgb11-stroke [filter:var(--svgb-11-glow)]" d="M80 4L152 24V58C152 82 118 96 80 100C42 96 8 82 8 58V24Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] transition-[color,text-shadow] duration-[260ms] motion-reduce:transition-none group-hover:text-svgb11-stroke group-hover:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)] group-focus-visible:text-svgb11-stroke group-focus-visible:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)]">Armory</span>
      </button>
      <button class="group relative grid place-items-center border-0 p-0 bg-transparent text-[15px] font-semibold tracking-[0.14em] uppercase cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb11-alt focus-visible:outline-offset-[6px] w-50 h-24" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 200 96" aria-hidden="true">
          <path class="fill-none stroke-svgb11-rest [stroke-width:1.6]" d="M28 4H172L196 28V68L172 92H28L4 68V28Z" pathLength="1"/>
          <path class="fill-none [stroke-width:2.4] [stroke-linecap:butt] [stroke-linejoin:miter] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 stroke-svgb11-stroke [filter:var(--svgb-11-glow)]" d="M28 4H172L196 28V68L172 92H28L4 68V28Z" pathLength="1"/>
        </svg>
        <span class="relative z-[1] transition-[color,text-shadow] duration-[260ms] motion-reduce:transition-none group-hover:text-svgb11-stroke group-hover:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)] group-focus-visible:text-svgb11-stroke group-focus-visible:[text-shadow:0_0_14px_color-mix(in_oklab,var(--color-svgb11-stroke)_70%,transparent)]">Options</span>
      </button>
      <button class="group relative grid place-items-center border-0 p-0 bg-transparent text-[15px] font-semibold tracking-[0.14em] uppercase cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb11-alt focus-visible:outline-offset-[6px] w-24 h-24" type="button" aria-label="Quit to attract mode">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 96 96" aria-hidden="true">
          <circle class="fill-none stroke-svgb11-rest [stroke-width:1.6]" cx="48" cy="48" r="44" pathLength="1"/>
          <circle class="fill-none [stroke-width:2.4] [stroke-linecap:butt] [stroke-linejoin:miter] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100 stroke-svgb11-alt [filter:var(--svgb-11-glow-alt)]" cx="48" cy="48" r="44" pathLength="1"/>
        </svg>
        <span class="relative z-[1] text-[26px] tracking-normal transition-[color,text-shadow] duration-[260ms] motion-reduce:transition-none group-hover:text-svgb11-alt group-focus-visible:text-svgb11-alt">&times;</span>
      </button>
    </div>
    <div class="grid grid-cols-[repeat(4,auto)] gap-x-3.5 gap-y-1 px-[18px] py-3 border border-svgb11-rest font-svgb11-mono text-[10.5px] tracking-[0.1em] uppercase">
      <span class="text-svgb11-muted">dasharray</span><span class="text-svgb11-stroke">1</span>
      <span class="text-svgb11-muted">dashoffset</span><span class="text-svgb11-stroke">1 &rarr; 0</span>
      <span class="text-svgb11-muted">shapes</span><span class="text-svgb11-stroke">5</span>
      <span class="text-svgb11-muted">constants</span><span class="text-svgb11-stroke">0</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb11-bg: #06070d;
  --color-svgb11-bg: oklch(0.145 0.02 265);
  --color-svgb11-fg: #e8f6ff;
  --color-svgb11-fg: oklch(0.96 0.02 220);
  --color-svgb11-muted: #7d90a8;
  --color-svgb11-muted: oklch(0.645 0.035 250);
  --color-svgb11-rest: rgba(232, 246, 255, 0.16);
  --color-svgb11-rest: oklch(0.96 0.02 220 / 0.16);
  --color-svgb11-stroke: #22f0ff;
  --color-svgb11-stroke: oklch(0.88 0.16 200);
  --color-svgb11-alt: #ff3ecb;
  --color-svgb11-alt: oklch(0.72 0.26 340);
  --font-svgb11-sans: 'Chakra Petch', system-ui, sans-serif;
  --font-svgb11-mono: 'JetBrains Mono', ui-monospace, monospace;
  --animate-svgb11-blink: svgb11-blink 1.8s steps(1, end) infinite;
}

@keyframes svgb11-blink {
  0%,
    60% {
    opacity: 1;
  }

  61%,
    100% {
    opacity: 0.25;
  }
}
/* Glows live in variables so the light scheme can switch them off without
   touching a single utility, and so both tones read the same class shape. */

.svgb-11 {
  --svgb-11-glow: drop-shadow(0 0 7px color-mix(in oklab, var(--color-svgb11-stroke) 60%, transparent));
  --svgb-11-glow-alt: drop-shadow(0 0 7px color-mix(in oklab, var(--color-svgb11-alt) 60%, transparent));
  --svgb-11-logo-sh: 0 0 22px color-mix(in oklab, var(--color-svgb11-stroke) 55%, transparent);
}
/* CRT scanlines and cabinet bloom: two decorative pseudo-element layers */

.svgb-11::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background: repeating-linear-gradient(0deg, oklch(0 0 0 / 0.34) 0 1px, transparent 1px 3px);
  opacity: var(--svgb-11-scan, 0.55);
}

.svgb-11::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 50% at 50% 0%, color-mix(in oklab, var(--color-svgb11-stroke) 14%, transparent), transparent 65%), radial-gradient(70% 60% at 50% 110%, color-mix(in oklab, var(--color-svgb11-alt) 14%, transparent), transparent 65%);
}

.svgb-11:has(#svgb-11-theme:checked) {
  --color-svgb11-bg: #eef2f6;
  --color-svgb11-bg: oklch(0.95 0.008 235);
  --color-svgb11-fg: #0b1220;
  --color-svgb11-fg: oklch(0.19 0.025 260);
  --color-svgb11-muted: #4f5f75;
  --color-svgb11-muted: oklch(0.49 0.03 255);
  --color-svgb11-rest: rgba(11, 18, 32, 0.2);
  --color-svgb11-rest: oklch(0.19 0.025 260 / 0.2);
  --color-svgb11-stroke: #006d8f;
  --color-svgb11-stroke: oklch(0.47 0.11 218);
  --color-svgb11-alt: #9c1173;
  --color-svgb11-alt: oklch(0.44 0.20 340);
  --svgb-11-glow: none;
  --svgb-11-glow-alt: none;
  --svgb-11-logo-sh: none;
  --svgb-11-scan: 0.18;
}
```
