---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-that-reverses-on-mouse-leave/"
title: "Tailwind Stroke Draw Button That Reverses on Mouse Leave"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "Three keycaps, three transition declarations, side by side in the markup where you can actually compare them."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Stroke Draw Button That Reverses on Mouse Leave
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-stroke-draw-button-that-reverses-on-mouse-leave/

Three keycaps, three transition declarations, side by side in the markup where you can actually compare them. The symmetric key reverses from wherever the pointer left it; the broken key uses group-hover:animate-svgb08-draw and snaps, because an animation has no memory of an interrupted position; the third declares a full [transition:...] twice to get 300ms in and 760ms out.
## HTML
```html
<section class="svgb-08 relative block w-full min-h-svh bg-svgb08-bg text-svgb08-fg font-svgb08-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-08-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/20 bg-current/7 cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/15 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-08-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <div class="min-h-svh grid place-content-center justify-items-center gap-[clamp(22px,4vh,40px)] p-[clamp(20px,5vw,70px)]">
    <div class="flex flex-wrap justify-center gap-[clamp(18px,3vw,34px)]">
      <div class="flex flex-col items-center gap-3.5">
        <button class="group relative size-33 grid place-items-center border-0 p-0 rounded-[18px] [background:linear-gradient(180deg,color-mix(in_oklab,var(--color-svgb08-cap)_88%,#fff_12%),var(--color-svgb08-cap))] [box-shadow:var(--svgb-08-key-sh)] transition-[translate,box-shadow] duration-100 motion-reduce:transition-none active:translate-y-[5px] active:[box-shadow:var(--svgb-08-key-sh-a)] focus-visible:outline-none focus-visible:[box-shadow:var(--svgb-08-key-sh-f)]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="fill-none stroke-svgb08-rest [stroke-width:1.4] [stroke-linecap:round]" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="fill-none [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:490] [stroke-dashoffset:490] stroke-svgb08-stroke transition-[stroke-dashoffset] duration-[520ms] ease-[cubic-bezier(0.45,0,0.55,1)] group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:!transition-none motion-reduce:!animate-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1] flex flex-col items-center gap-2">
            <span class="text-3xl leading-none transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb08-stroke group-focus-visible:text-svgb08-stroke">&#8630;</span>
            <span class="font-svgb08-mono text-[10.5px] tracking-[0.16em] uppercase text-svgb08-muted">reverse</span>
          </span>
        </button>
        <span class="inline-flex items-center gap-[7px] font-svgb08-mono text-[11px] text-[color-mix(in_oklab,var(--color-svgb08-stroke)_62%,var(--color-svgb08-muted))] before:content-[''] before:size-1.5 before:rounded-full before:bg-current">transition &middot; 520 / 520</span>
      </div>
      <div class="flex flex-col items-center gap-3.5">
        <button class="group relative size-33 grid place-items-center border-0 p-0 rounded-[18px] [background:linear-gradient(180deg,color-mix(in_oklab,var(--color-svgb08-cap)_88%,#fff_12%),var(--color-svgb08-cap))] [box-shadow:var(--svgb-08-key-sh)] transition-[translate,box-shadow] duration-100 motion-reduce:transition-none active:translate-y-[5px] active:[box-shadow:var(--svgb-08-key-sh-a)] focus-visible:outline-none focus-visible:[box-shadow:var(--svgb-08-key-sh-f)]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="fill-none stroke-svgb08-rest [stroke-width:1.4] [stroke-linecap:round]" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="fill-none [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:490] [stroke-dashoffset:490] stroke-svgb08-warn group-hover:animate-svgb08-draw group-focus-visible:animate-svgb08-draw motion-reduce:!transition-none motion-reduce:!animate-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1] flex flex-col items-center gap-2">
            <span class="text-3xl leading-none transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb08-warn group-focus-visible:text-svgb08-warn">&#9633;</span>
            <span class="font-svgb08-mono text-[10.5px] tracking-[0.16em] uppercase text-svgb08-muted">snap</span>
          </span>
        </button>
        <span class="inline-flex items-center gap-[7px] font-svgb08-mono text-[11px] text-[color-mix(in_oklab,var(--color-svgb08-warn)_62%,var(--color-svgb08-muted))] before:content-[''] before:size-1.5 before:rounded-full before:bg-current">keyframes &middot; no memory</span>
      </div>
      <div class="flex flex-col items-center gap-3.5">
        <button class="group relative size-33 grid place-items-center border-0 p-0 rounded-[18px] [background:linear-gradient(180deg,color-mix(in_oklab,var(--color-svgb08-cap)_88%,#fff_12%),var(--color-svgb08-cap))] [box-shadow:var(--svgb-08-key-sh)] transition-[translate,box-shadow] duration-100 motion-reduce:transition-none active:translate-y-[5px] active:[box-shadow:var(--svgb-08-key-sh-a)] focus-visible:outline-none focus-visible:[box-shadow:var(--svgb-08-key-sh-f)]" type="button">
          <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 132 132" aria-hidden="true">
            <rect class="fill-none stroke-svgb08-rest [stroke-width:1.4] [stroke-linecap:round]" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
            <rect class="fill-none [stroke-width:2.4] [stroke-linecap:round] [stroke-dasharray:490] [stroke-dashoffset:490] stroke-svgb08-stroke [transition:stroke-dashoffset_760ms_cubic-bezier(0.22,1,0.36,1)_40ms] group-hover:[stroke-dashoffset:0] group-hover:[transition:stroke-dashoffset_300ms_cubic-bezier(0.4,0,0.2,1)_0ms] group-focus-visible:[stroke-dashoffset:0] group-focus-visible:[transition:stroke-dashoffset_300ms_cubic-bezier(0.4,0,0.2,1)_0ms] motion-reduce:!transition-none motion-reduce:!animate-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" x="2" y="2" width="128" height="128" rx="18" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="relative z-[1] flex flex-col items-center gap-2">
            <span class="text-3xl leading-none transition-colors duration-300 motion-reduce:transition-none group-hover:text-svgb08-stroke group-focus-visible:text-svgb08-stroke">&#8677;</span>
            <span class="font-svgb08-mono text-[10.5px] tracking-[0.16em] uppercase text-svgb08-muted">asym</span>
          </span>
        </button>
        <span class="inline-flex items-center gap-[7px] font-svgb08-mono text-[11px] text-[color-mix(in_oklab,var(--color-svgb08-stroke)_62%,var(--color-svgb08-muted))] before:content-[''] before:size-1.5 before:rounded-full before:bg-current">300 in &middot; 760 out</span>
      </div>
    </div>
    <div class="px-[18px] py-3 rounded-[10px] bg-svgb08-fg/4 border border-svgb08-rest">
      <span class="font-svgb08-mono text-[11px] text-svgb08-muted">interrupt a draw halfway &mdash; only a transition can walk it back</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb08-bg: #17181b;
  --color-svgb08-bg: oklch(0.225 0.004 250);
  --color-svgb08-cap: #23252a;
  --color-svgb08-cap: oklch(0.275 0.006 255);
  --color-svgb08-fg: #e9ebee;
  --color-svgb08-fg: oklch(0.94 0.004 250);
  --color-svgb08-muted: #868b93;
  --color-svgb08-muted: oklch(0.655 0.011 250);
  --color-svgb08-rest: rgba(233, 235, 238, 0.14);
  --color-svgb08-rest: oklch(0.94 0.004 250 / 0.14);
  --color-svgb08-stroke: #c6ff4f;
  --color-svgb08-stroke: oklch(0.92 0.20 122);
  --color-svgb08-warn: #ff7a6b;
  --color-svgb08-warn: oklch(0.75 0.16 30);
  --font-svgb08-sans: 'Figtree', system-ui, sans-serif;
  --font-svgb08-mono: 'JetBrains Mono', ui-monospace, monospace;
  /* the wrong way, kept on purpose: a keyframe cannot resume from an
       interrupted position, so this key snaps back on mouse-out */
  --animate-svgb08-draw: svgb-08-draw 520ms cubic-bezier(0.45, 0, 0.55, 1) forwards;
}

@keyframes svgb-08-draw {
  from {
    stroke-dashoffset: 490;
  }

  to {
    stroke-dashoffset: 0;
  }
}
/* Four-layer keycap shadows, one set per interaction state. Kept as variables
   so the markup reads [box-shadow:var(--svgb-08-key-sh)] rather than three
   200-character arbitrary values, and so the light scheme swaps all of them. */

.svgb-08 {
  --svgb-08-key-sh: inset 0 1px 0 oklch(1 0 0 / 0.09), inset 0 -3px 0 oklch(0 0 0 / 0.35), 0 8px 0 color-mix(in oklab, var(--color-svgb08-cap) 70%, #000), 0 18px 30px -14px oklch(0 0 0 / 0.7);
  --svgb-08-key-sh-a: inset 0 1px 0 oklch(1 0 0 / 0.07), inset 0 -2px 0 oklch(0 0 0 / 0.3), 0 3px 0 color-mix(in oklab, var(--color-svgb08-cap) 70%, #000), 0 8px 16px -10px oklch(0 0 0 / 0.7);
  --svgb-08-key-sh-f: 0 0 0 3px color-mix(in oklab, var(--color-svgb08-stroke) 40%, transparent), 0 8px 0 color-mix(in oklab, var(--color-svgb08-cap) 70%, #000);
}

.svgb-08:has(#svgb-08-theme:checked) {
  --color-svgb08-bg: #e8e9ec;
  --color-svgb08-bg: oklch(0.935 0.004 250);
  --color-svgb08-cap: #fbfbfc;
  --color-svgb08-cap: oklch(0.985 0.002 250);
  --color-svgb08-fg: #14171b;
  --color-svgb08-fg: oklch(0.20 0.005 250);
  --color-svgb08-muted: #5a6068;
  --color-svgb08-muted: oklch(0.50 0.011 250);
  --color-svgb08-rest: rgba(20, 23, 27, 0.16);
  --color-svgb08-rest: oklch(0.20 0.005 250 / 0.16);
  --color-svgb08-stroke: #3f6b00;
  --color-svgb08-stroke: oklch(0.48 0.16 126);
  --color-svgb08-warn: #b03a26;
  --color-svgb08-warn: oklch(0.50 0.17 30);
  --svgb-08-key-sh: inset 0 1px 0 oklch(1 0 0 / 0.9), inset 0 -3px 0 oklch(0 0 0 / 0.08), 0 8px 0 color-mix(in oklab, var(--color-svgb08-cap) 78%, #000 22%), 0 18px 30px -18px oklch(0 0 0 / 0.4);
}
```
