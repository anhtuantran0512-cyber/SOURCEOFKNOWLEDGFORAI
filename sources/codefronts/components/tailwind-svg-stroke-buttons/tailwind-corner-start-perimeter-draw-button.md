---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-corner-start-perimeter-draw-button/"
title: "Tailwind Corner Start Perimeter Draw Button"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "The measured draw, ported with its three layers still reading one clock."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Corner Start Perimeter Draw Button
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-corner-start-perimeter-draw-button/

The measured draw, ported with its three layers still reading one clock. duration-[760ms] ease-svgb03 appears on the tape, the ink and the head alike, with the curve declared once in @theme &mdash; and reversing a cell needs no modifier class at all, just [stroke-dashoffset:-592] on the path. offset-path stays in CSS, because it takes literal path data and needs an @supports guard.
## HTML
```html
<section class="svgb-03 relative block w-full min-h-svh bg-svgb03-bg text-svgb03-fg font-svgb03-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-03-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 border border-current/25 bg-current/8 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-03-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="relative min-h-svh grid content-center justify-items-center gap-[clamp(24px,5vh,48px)] p-[clamp(22px,5vw,70px)]">
    <div class="grid gap-[clamp(34px,5vw,62px)] grid-cols-[repeat(auto-fit,minmax(min(100%,290px),1fr))] w-full max-w-200 p-[clamp(36px,5.5vw,60px)] border border-svgb03-rest outline-1 outline-svgb03-grid outline-offset-[5px]">
      <div class="flex flex-col gap-6">
        <button class="group relative w-full max-w-60 h-16 grid place-items-center border-0 p-0 bg-svgb03-fg/5 text-[15px] font-medium tracking-[0.01em] cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb03-stroke focus-visible:outline-offset-[16px]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-tl" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="fill-none stroke-white [stroke-width:18] [stroke-linecap:butt] [stroke-dasharray:672] [stroke-dashoffset:672] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0]" d="M-8 -8H248V72H-8V-8"/>
              </mask>
            </defs>
            <path class="fill-none stroke-svgb03-rest [stroke-width:1]" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-tl)">
              <path class="fill-none stroke-svgb03-stroke [stroke-width:7] [stroke-dasharray:1_7] [stroke-linecap:butt] opacity-50 pointer-events-none motion-reduce:opacity-0 motion-reduce:group-hover:opacity-50 motion-reduce:group-focus-visible:opacity-50" d="M-8 -8H248V72H-8V-8"/>
            </g>
            <path class="fill-none stroke-svgb03-stroke [stroke-width:1.6] [stroke-dasharray:592] [stroke-dashoffset:592] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M2 2H238V62H2V2" vector-effect="non-scaling-stroke"/>
            <g class="opacity-85 transition-opacity duration-300 group-hover:opacity-100 motion-reduce:transition-none [&_path]:fill-none [&_path]:stroke-svgb03-stroke [&_path]:[stroke-width:1] [&_path]:opacity-50"><path d="M2 -8V12M-8 2H12" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--tl motion-reduce:hidden">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="relative z-[1] transition-[letter-spacing,color] duration-400 motion-reduce:transition-none group-hover:tracking-[0.06em] group-hover:text-svgb03-stroke group-focus-visible:tracking-[0.06em] group-focus-visible:text-svgb03-stroke">Elevation A</span>
        </button>
        <span class="font-svgb03-mono text-[10.5px] tracking-[0.06em] uppercase text-svgb03-muted">P1 2,2 &middot; CW &middot; 592</span>
      </div>
      <div class="flex flex-col gap-6">
        <button class="group relative w-full max-w-60 h-16 grid place-items-center border-0 p-0 bg-svgb03-fg/5 text-[15px] font-medium tracking-[0.01em] cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb03-stroke focus-visible:outline-offset-[16px]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-tr" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="fill-none stroke-white [stroke-width:18] [stroke-linecap:butt] [stroke-dasharray:672] [stroke-dashoffset:672] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0]" d="M248 -8V72H-8V-8H248"/>
              </mask>
            </defs>
            <path class="fill-none stroke-svgb03-rest [stroke-width:1]" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-tr)">
              <path class="fill-none stroke-svgb03-stroke [stroke-width:7] [stroke-dasharray:1_7] [stroke-linecap:butt] opacity-50 pointer-events-none motion-reduce:opacity-0 motion-reduce:group-hover:opacity-50 motion-reduce:group-focus-visible:opacity-50" d="M248 -8V72H-8V-8H248"/>
            </g>
            <path class="fill-none stroke-svgb03-stroke [stroke-width:1.6] [stroke-dasharray:592] [stroke-dashoffset:592] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M238 2V62H2V2H238" vector-effect="non-scaling-stroke"/>
            <g class="opacity-85 transition-opacity duration-300 group-hover:opacity-100 motion-reduce:transition-none [&_path]:fill-none [&_path]:stroke-svgb03-stroke [&_path]:[stroke-width:1] [&_path]:opacity-50"><path d="M238 -8V12M228 2H248" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--tr motion-reduce:hidden">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="relative z-[1] transition-[letter-spacing,color] duration-400 motion-reduce:transition-none group-hover:tracking-[0.06em] group-hover:text-svgb03-stroke group-focus-visible:tracking-[0.06em] group-focus-visible:text-svgb03-stroke">Elevation B</span>
        </button>
        <span class="font-svgb03-mono text-[10.5px] tracking-[0.06em] uppercase text-svgb03-muted">P1 238,2 &middot; CW &middot; 592</span>
      </div>
      <div class="flex flex-col gap-6">
        <button class="group relative w-full max-w-60 h-16 grid place-items-center border-0 p-0 bg-svgb03-fg/5 text-[15px] font-medium tracking-[0.01em] cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb03-stroke focus-visible:outline-offset-[16px]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-br" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="fill-none stroke-white [stroke-width:18] [stroke-linecap:butt] [stroke-dasharray:672] [stroke-dashoffset:672] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0]" d="M248 72H-8V-8H248V72"/>
              </mask>
            </defs>
            <path class="fill-none stroke-svgb03-rest [stroke-width:1]" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-br)">
              <path class="fill-none stroke-svgb03-stroke [stroke-width:7] [stroke-dasharray:1_7] [stroke-linecap:butt] opacity-50 pointer-events-none motion-reduce:opacity-0 motion-reduce:group-hover:opacity-50 motion-reduce:group-focus-visible:opacity-50" d="M248 72H-8V-8H248V72"/>
            </g>
            <path class="fill-none stroke-svgb03-stroke [stroke-width:1.6] [stroke-dasharray:592] [stroke-dashoffset:592] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M238 62H2V2H238V62" vector-effect="non-scaling-stroke"/>
            <g class="opacity-85 transition-opacity duration-300 group-hover:opacity-100 motion-reduce:transition-none [&_path]:fill-none [&_path]:stroke-svgb03-stroke [&_path]:[stroke-width:1] [&_path]:opacity-50"><path d="M238 52V72M228 62H248" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--br motion-reduce:hidden">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="relative z-[1] transition-[letter-spacing,color] duration-400 motion-reduce:transition-none group-hover:tracking-[0.06em] group-hover:text-svgb03-stroke group-focus-visible:tracking-[0.06em] group-focus-visible:text-svgb03-stroke">Section C</span>
        </button>
        <span class="font-svgb03-mono text-[10.5px] tracking-[0.06em] uppercase text-svgb03-muted">P1 238,62 &middot; CCW &middot; 592</span>
      </div>
      <div class="flex flex-col gap-6">
        <button class="svgb-03__btn--rev group relative w-full max-w-60 h-16 grid place-items-center border-0 p-0 bg-svgb03-fg/5 text-[15px] font-medium tracking-[0.01em] cursor-pointer focus-visible:outline-dashed focus-visible:outline-1 focus-visible:outline-svgb03-stroke focus-visible:outline-offset-[16px]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-bl" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="fill-none stroke-white [stroke-width:18] [stroke-linecap:butt] [stroke-dasharray:672] [stroke-dashoffset:-672] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0]" d="M-8 72V-8H248V72H-8"/>
              </mask>
            </defs>
            <path class="fill-none stroke-svgb03-rest [stroke-width:1]" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-bl)">
              <path class="fill-none stroke-svgb03-stroke [stroke-width:7] [stroke-dasharray:1_7] [stroke-linecap:butt] opacity-50 pointer-events-none motion-reduce:opacity-0 motion-reduce:group-hover:opacity-50 motion-reduce:group-focus-visible:opacity-50" d="M-8 72V-8H248V72H-8"/>
            </g>
            <path class="fill-none stroke-svgb03-stroke [stroke-width:1.6] [stroke-dasharray:592] [stroke-dashoffset:-592] transition-[stroke-dashoffset] duration-[760ms] ease-svgb03 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M2 62V2H238V62H2" vector-effect="non-scaling-stroke"/>
            <g class="opacity-85 transition-opacity duration-300 group-hover:opacity-100 motion-reduce:transition-none [&_path]:fill-none [&_path]:stroke-svgb03-stroke [&_path]:[stroke-width:1] [&_path]:opacity-50"><path d="M2 52V72M-8 62H12" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--bl motion-reduce:hidden">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="relative z-[1] transition-[letter-spacing,color] duration-400 motion-reduce:transition-none group-hover:tracking-[0.06em] group-hover:text-svgb03-stroke group-focus-visible:tracking-[0.06em] group-focus-visible:text-svgb03-stroke">Section D</span>
        </button>
        <span class="font-svgb03-mono text-[10.5px] tracking-[0.06em] uppercase text-svgb03-muted">P1 2,62 &middot; negative offset</span>
      </div>
    </div>
    <div class="grid grid-cols-[auto_1fr] gap-x-[18px] gap-y-1 w-full max-w-200 px-[18px] py-3.5 border border-svgb03-rest font-svgb03-mono text-[10.5px] uppercase tracking-[0.08em]">
      <span class="text-svgb03-muted">Drawing</span><span class="text-svgb03-fg">Corner-start perimeter &middot; surveyor&rsquo;s tape</span>
      <span class="text-svgb03-muted">Tape</span><span class="text-svgb03-fg">1&times;7 tick dash on a 672-unit offset path, mask-revealed</span>
      <span class="text-svgb03-muted">Head</span><span class="text-svgb03-fg">offset-path rides the same path from P1</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb03-bg: #0d2233;
  --color-svgb03-bg: oklch(0.27 0.055 245);
  --color-svgb03-fg: #dcecf7;
  --color-svgb03-fg: oklch(0.92 0.025 230);
  --color-svgb03-muted: #8fb3c9;
  --color-svgb03-muted: oklch(0.735 0.04 235);
  --color-svgb03-grid: rgba(220, 236, 247, 0.09);
  --color-svgb03-grid: oklch(0.92 0.025 230 / 0.09);
  --color-svgb03-rest: rgba(220, 236, 247, 0.26);
  --color-svgb03-rest: oklch(0.92 0.025 230 / 0.26);
  --color-svgb03-stroke: #ffffff;
  --color-svgb03-stroke: oklch(0.99 0.01 230);
  --font-svgb03-sans: 'Archivo', system-ui, sans-serif;
  --font-svgb03-mono: 'JetBrains Mono', ui-monospace, monospace;
  --ease-svgb03: cubic-bezier(0.36, 0, 0.24, 1);
}
/* Four things below have no utility equivalent, and that is the honest reason
   they are still CSS: a four-layer decorative paint, offset-path values, an
   @supports guard, and the token flip. Everything else is a utility. */

.svgb-03::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(var(--color-svgb03-grid) 1px, transparent 1px) 0 0 / 100% 24px, linear-gradient(90deg, var(--color-svgb03-grid) 1px, transparent 1px) 0 0 / 24px 100%, linear-gradient(var(--color-svgb03-grid) 1px, transparent 1px) 0 0 / 100% 120px, linear-gradient(90deg, var(--color-svgb03-grid) 1px, transparent 1px) 0 0 / 120px 100%;
}
/* the head rides the identical path data, so it always leaves from P1 */

.svgb-03__pen {
  opacity: 0;
}

@supports (offset-path: path('M0 0H1')) {
  .svgb-03__pen {
    offset-distance: 0%;
    offset-rotate: 0deg;
    transition: offset-distance 760ms var(--ease-svgb03), opacity 220ms ease 540ms;
  }

  .svgb-03__pen path {
    fill: none;
    stroke: var(--color-svgb03-stroke);
    stroke-width: 1.2px;
  }

  .svgb-03__pen circle {
    fill: var(--color-svgb03-stroke);
    stroke: none;
  }

  .group:hover .svgb-03__pen,
    .group:focus-visible .svgb-03__pen {
    opacity: 1;
    offset-distance: 100%;
    transition-delay: 0s, 0s;
  }

  .svgb-03__pen--tl {
    offset-path: path('M-8 -8H248V72H-8V-8');
  }

  .svgb-03__pen--tr {
    offset-path: path('M248 -8V72H-8V-8H248');
  }

  .svgb-03__pen--br {
    offset-path: path('M248 72H-8V-8H248V72');
  }

  .svgb-03__pen--bl {
    offset-path: path('M-8 72V-8H248V72H-8');
  }

  .svgb-03__btn--rev .svgb-03__pen {
    offset-distance: 100%;
  }

  .svgb-03__btn--rev:hover .svgb-03__pen,
    .svgb-03__btn--rev:focus-visible .svgb-03__pen {
    offset-distance: 0%;
  }
}

.svgb-03:has(#svgb-03-theme:checked) {
  --color-svgb03-bg: #eef3f7;
  --color-svgb03-bg: oklch(0.955 0.008 235);
  --color-svgb03-fg: #0e2a3d;
  --color-svgb03-fg: oklch(0.29 0.05 240);
  --color-svgb03-muted: #4e6d80;
  --color-svgb03-muted: oklch(0.505 0.04 235);
  --color-svgb03-grid: rgba(14, 42, 61, 0.09);
  --color-svgb03-grid: oklch(0.29 0.05 240 / 0.09);
  --color-svgb03-rest: rgba(14, 42, 61, 0.28);
  --color-svgb03-rest: oklch(0.29 0.05 240 / 0.28);
  --color-svgb03-stroke: #0a3f8f;
  --color-svgb03-stroke: oklch(0.40 0.18 262);
}
```
