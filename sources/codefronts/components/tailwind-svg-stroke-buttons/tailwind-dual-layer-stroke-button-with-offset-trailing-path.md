---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-dual-layer-stroke-button-with-offset-trailing-path/"
title: "Tailwind Dual Layer Stroke Button with Offset Trailing Path"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "A crisp leader and a blurred follower 90ms behind it, which the eye reads as speed rather than as two lines."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Dual Layer Stroke Button with Offset Trailing Path
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-dual-layer-stroke-button-with-offset-trailing-path/

A crisp leader and a blurred follower 90ms behind it, which the eye reads as speed rather than as two lines. The offset is two utilities &mdash; duration-[620ms] on the leader, duration-[800ms] delay-[90ms] on the trail &mdash; and the comet pair animates the offset negative, so a 4.5% fraction of pathLength="1" travels the path instead of a line being drawn.
## HTML
```html
<section class="svgb-12 relative block w-full min-h-svh overflow-hidden bg-svgb12-bg text-svgb12-fg font-svgb12-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-12-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded border border-current/22 bg-current/8 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-12-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="relative min-h-svh grid place-items-center p-[clamp(22px,5vw,70px)]">
    <div class="flex flex-col items-start gap-[clamp(16px,3vw,26px)] w-full max-w-105">
      <div class="grid grid-cols-2 gap-x-5 gap-y-2.5 w-full">
        <div class="flex flex-col gap-0.5 pb-2 border-b border-svgb12-rest"><span class="font-svgb12-mono text-[9.5px] tracking-[0.22em] uppercase text-svgb12-muted">Lap</span><span class="text-[26px] font-bold italic tracking-[-0.01em] tabular-nums">14</span></div>
        <div class="flex flex-col gap-0.5 pb-2 border-b border-svgb12-rest"><span class="font-svgb12-mono text-[9.5px] tracking-[0.22em] uppercase text-svgb12-muted">Delta</span><span class="text-[26px] font-bold italic tracking-[-0.01em] tabular-nums text-svgb12-good">-0.412</span></div>
        <div class="flex flex-col gap-0.5 pb-2 border-b border-svgb12-rest"><span class="font-svgb12-mono text-[9.5px] tracking-[0.22em] uppercase text-svgb12-muted">Tyre</span><span class="text-[26px] font-bold italic tracking-[-0.01em] tabular-nums">C3 &middot; 62%</span></div>
        <div class="flex flex-col gap-0.5 pb-2 border-b border-svgb12-rest"><span class="font-svgb12-mono text-[9.5px] tracking-[0.22em] uppercase text-svgb12-muted">ERS</span><span class="text-[26px] font-bold italic tracking-[-0.01em] tabular-nums">2.1 MJ</span></div>
      </div>

      <button class="group relative w-[min(340px,92vw)] h-[78px] grid place-items-center border-0 p-0 bg-transparent isolate text-xl font-semibold italic tracking-[0.1em] uppercase cursor-pointer focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-svgb12-stroke)_34%,transparent)]" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 340 78" aria-hidden="true">
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-rest [stroke-width:1.4]" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-stroke text-svgb12-stroke [filter:drop-shadow(0_0_10px_currentColor)] [mix-blend-mode:var(--svgb-12-blend)] motion-reduce:!filter-none motion-reduce:opacity-0 [stroke-width:7] opacity-36 [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[800ms] delay-[90ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-stroke [stroke-width:2] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[620ms] ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="relative z-[2] transition-[color,letter-spacing] duration-[400ms] motion-reduce:transition-none group-hover:text-svgb12-stroke group-hover:tracking-[0.16em] group-focus-visible:text-svgb12-stroke group-focus-visible:tracking-[0.16em]">Push lap</span>
      </button>

      <button class="group relative w-[min(340px,92vw)] h-[78px] grid place-items-center border-0 p-0 bg-transparent isolate text-xl font-semibold italic tracking-[0.1em] uppercase cursor-pointer focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-svgb12-stroke)_34%,transparent)]" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 340 78" aria-hidden="true">
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-rest [stroke-width:1.4]" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-stroke text-svgb12-stroke [filter:drop-shadow(0_0_10px_currentColor)] [mix-blend-mode:var(--svgb-12-blend)] motion-reduce:!filter-none motion-reduce:opacity-0 [stroke-width:6] opacity-32 [stroke-dasharray:0.16_0.84] [stroke-dashoffset:0.16] transition-[stroke-dashoffset] duration-[900ms] ease-linear group-hover:[stroke-dashoffset:-0.84] group-focus-visible:[stroke-dashoffset:-0.84] motion-reduce:!transition-none" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke-linejoin:miter] stroke-svgb12-fg [stroke-width:2.4] [stroke-dasharray:0.045_0.955] [stroke-dashoffset:0.045] transition-[stroke-dashoffset] duration-[900ms] ease-linear group-hover:[stroke-dashoffset:-0.955] group-focus-visible:[stroke-dashoffset:-0.955] motion-reduce:!transition-none motion-reduce:opacity-0" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="relative z-[2] transition-[color,letter-spacing] duration-[400ms] motion-reduce:transition-none group-hover:text-svgb12-stroke group-hover:tracking-[0.16em] group-focus-visible:text-svgb12-stroke group-focus-visible:tracking-[0.16em]">Deploy overtake</span>
      </button>

      <p class="m-0 font-svgb12-mono text-[10.5px] tracking-[0.04em] text-svgb12-muted">leader 620ms &middot; trail 800ms + 90ms &middot; paint order: trail first</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb12-bg: #08090a;
  --color-svgb12-bg: oklch(0.145 0.002 250);
  --color-svgb12-fg: #edeff1;
  --color-svgb12-fg: oklch(0.95 0.003 250);
  --color-svgb12-muted: #83878d;
  --color-svgb12-muted: oklch(0.645 0.008 250);
  --color-svgb12-rest: rgba(237, 239, 241, 0.14);
  --color-svgb12-rest: oklch(0.95 0.003 250 / 0.14);
  --color-svgb12-stroke: #00e5ff;
  --color-svgb12-stroke: oklch(0.85 0.15 205);
  --color-svgb12-good: #7cff8f;
  --color-svgb12-good: oklch(0.89 0.18 145);
  --font-svgb12-sans: 'Saira Condensed', system-ui, sans-serif;
  --font-svgb12-mono: 'JetBrains Mono', ui-monospace, monospace;
}
/* screen over a dark rack, multiply over a light one: the blend mode itself is
   scheme-dependent, which no utility can express as one class */

.svgb-12 {
  --svgb-12-blend: screen;
}

.svgb-12::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: var(--svgb-12-weave), radial-gradient(70% 60% at 50% 40%, color-mix(in oklab, var(--color-svgb12-stroke) 8%, transparent), transparent 70%);
}

.svgb-12 {
  --svgb-12-weave: repeating-linear-gradient(45deg, oklch(1 0 0 / 0.022) 0 2px, transparent 2px 5px), repeating-linear-gradient(-45deg, oklch(1 0 0 / 0.022) 0 2px, transparent 2px 5px);
}

.svgb-12:has(#svgb-12-theme:checked) {
  --color-svgb12-bg: #f1f2f4;
  --color-svgb12-bg: oklch(0.955 0.003 250);
  --color-svgb12-fg: #101214;
  --color-svgb12-fg: oklch(0.185 0.004 250);
  --color-svgb12-muted: #555a60;
  --color-svgb12-muted: oklch(0.49 0.008 250);
  --color-svgb12-rest: rgba(16, 18, 20, 0.16);
  --color-svgb12-rest: oklch(0.185 0.004 250 / 0.16);
  --color-svgb12-stroke: #00647f;
  --color-svgb12-stroke: oklch(0.45 0.11 215);
  --color-svgb12-good: #0d6b2c;
  --color-svgb12-good: oklch(0.46 0.14 148);
  --svgb-12-blend: multiply;
  --svgb-12-weave: repeating-linear-gradient(45deg, oklch(0 0 0 / 0.03) 0 2px, transparent 2px 5px), repeating-linear-gradient(-45deg, oklch(0 0 0 / 0.03) 0 2px, transparent 2px 5px);
}
```
