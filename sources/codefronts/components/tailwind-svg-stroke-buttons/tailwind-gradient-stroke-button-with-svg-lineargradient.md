---
source: "codefronts"
url: "https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-gradient-stroke-button-with-svg-lineargradient/"
title: "Tailwind Gradient Stroke Button with SVG linearGradient"
section: "components"
category: "tailwind-svg-stroke-buttons"
category_name: "Tailwind SVG Stroke Buttons"
description: "A gradient border with no background-clip hack anywhere: the stroke is a paint-server reference, written as the arbitrary property…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Gradient Stroke Button with SVG linearGradient
Source: https://codefronts.com/components/tailwind-svg-stroke-buttons/tailwind-gradient-stroke-button-with-svg-lineargradient/

A gradient border with no background-clip hack anywhere: the stroke is a paint-server reference, written as the arbitrary property [stroke:url(#svgb-07-grad)] because an id lookup is not a colour value. The pill and the badge both draw with [stroke-dasharray:1] [stroke-dashoffset:1] &mdash; two very different perimeters, one constant, because both paths carry pathLength="1".
## HTML
```html
<section class="svgb-07 relative block w-full min-h-svh overflow-hidden isolate bg-svgb07-bg text-svgb07-fg font-svgb07-sans">
  <input class="peer absolute opacity-0 pointer-events-none" type="checkbox" id="svgb-07-theme">
  <label class="absolute z-[5] top-4 right-4 grid place-items-center size-11 rounded-full border border-current/22 bg-current/10 backdrop-blur-lg cursor-pointer transition-[background-color,transform] duration-150 hover:bg-current/16 active:scale-95 peer-focus-visible:outline-2 peer-focus-visible:outline-current peer-focus-visible:outline-offset-[3px] peer-checked:[&_svg]:rotate-180" for="svgb-07-theme">
    <svg class="size-[18px] transition-transform duration-[400ms] ease-[cubic-bezier(0.2,0.7,0.3,1)]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="absolute size-px overflow-hidden [clip-path:inset(50%)] whitespace-nowrap">Switch colour scheme</span>
  </label>
  <img class="absolute inset-0 -z-2 w-full h-full object-cover [filter:grayscale(1)_contrast(1.25)] [opacity:var(--svgb-07-img-op,0.34)]" src="https://picsum.photos/seed/svgb07crowd/1600/1100" alt="" width="1600" height="1100" loading="lazy" decoding="async">
  <div class="relative min-h-svh flex flex-col justify-center gap-[clamp(14px,2.5vw,26px)] p-[clamp(24px,6vw,84px)] max-w-300 mx-auto">
    <div class="flex flex-wrap gap-x-[26px] gap-y-2 font-svgb07-mono text-[11.5px] tracking-[0.22em] uppercase text-svgb07-muted">
      <span>Pier 44 &middot; Rotterdam</span>
      <span>19 &mdash; 21 June</span>
    </div>
    <h1 class="m-0 text-[clamp(58px,16vw,200px)] font-extrabold leading-[0.82] tracking-[-0.055em] uppercase [&_span]:block [&_span]:text-transparent [&_span]:ps-[0.12em] [&_span]:[-webkit-text-stroke:1.5px_var(--color-svgb07-fg)]">Chroma<span>Nights</span></h1>
    <p class="m-0 mb-[clamp(8px,2vw,16px)] max-w-[46ch] text-[clamp(14px,1.6vw,18px)] leading-relaxed text-svgb07-muted">Aurelia &middot; K&aacute;rmen &middot; Low Static &middot; Nadir &middot; Volta Kids &middot; Sonnet 8</p>
    <div class="flex flex-wrap gap-[18px] items-center">
      <button class="group relative w-[min(300px,88vw)] h-18 grid place-items-center border-0 p-0 rounded-full bg-transparent text-[15.5px] tracking-[0.01em] cursor-pointer focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-svgb07-c)_55%,transparent)]" type="button">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 300 72" aria-hidden="true">
          <defs>
            <linearGradient id="svgb-07-grad" gradientUnits="userSpaceOnUse" x1="0" y1="72" x2="300" y2="0">
              <stop class="svgb-07-s1" offset="0"/>
              <stop class="svgb-07-s2" offset="0.5"/>
              <stop class="svgb-07-s3" offset="1"/>
            </linearGradient>
          </defs>
          <path class="stroke-svgb07-rest [stroke-width:1.4] [stroke-linejoin:round] [stroke-linecap:round] [fill:var(--svgb-07-basefill,oklch(1_0_0/0.05))]" d="M14 14q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0C300 24 300 48 286 58q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0C0 48 0 24 14 14Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke:url(#svgb-07-grad)] [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] [filter:drop-shadow(0_0_10px_color-mix(in_oklab,var(--color-svgb07-b)_55%,transparent))] transition-[stroke-dashoffset] duration-[980ms] ease-svgb07 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M14 14q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0q8.5 -16 17 0q8.5 16 17 0C300 24 300 48 286 58q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0q-8.5 16 -17 0q-8.5 -16 -17 0C0 48 0 24 14 14Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="relative z-[1]">Three-day pass &mdash; &euro;89</span>
      </button>
      <button class="group relative size-18 grid place-items-center border-0 p-0 rounded-full bg-transparent cursor-pointer focus-visible:outline-none focus-visible:shadow-[0_0_0_3px_color-mix(in_oklab,var(--color-svgb07-c)_55%,transparent)]" type="button" aria-label="Play the lineup mix">
        <svg class="absolute inset-0 w-full h-full overflow-visible" viewBox="0 0 72 72" aria-hidden="true">
          <path class="stroke-svgb07-rest [stroke-width:1.4] [stroke-linejoin:round] [stroke-linecap:round] [fill:var(--svgb-07-basefill,oklch(1_0_0/0.05))]" d="M36.00 6.00A18 18 0 0 1 53.63 11.73A18 18 0 0 1 64.53 26.73A18 18 0 0 1 64.53 45.27A18 18 0 0 1 53.63 60.27A18 18 0 0 1 36.00 66.00A18 18 0 0 1 18.37 60.27A18 18 0 0 1 7.47 45.27A18 18 0 0 1 7.47 26.73A18 18 0 0 1 18.37 11.73A18 18 0 0 1 36.00 6.00Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="fill-none [stroke:url(#svgb-07-grad)] [stroke-width:2.6] [stroke-linecap:round] [stroke-linejoin:round] [stroke-dasharray:1] [stroke-dashoffset:1] transition-[stroke-dashoffset] duration-[700ms] ease-svgb07 group-hover:[stroke-dashoffset:0] group-focus-visible:[stroke-dashoffset:0] motion-reduce:transition-none motion-reduce:[stroke-dasharray:none] motion-reduce:[stroke-dashoffset:0] motion-reduce:opacity-0 motion-reduce:group-hover:opacity-100 motion-reduce:group-focus-visible:opacity-100" d="M36.00 6.00A18 18 0 0 1 53.63 11.73A18 18 0 0 1 64.53 26.73A18 18 0 0 1 64.53 45.27A18 18 0 0 1 53.63 60.27A18 18 0 0 1 36.00 66.00A18 18 0 0 1 18.37 60.27A18 18 0 0 1 7.47 45.27A18 18 0 0 1 7.47 26.73A18 18 0 0 1 18.37 11.73A18 18 0 0 1 36.00 6.00Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <svg class="relative z-[1] size-[22px] fill-svgb07-fg" viewBox="0 0 24 24" aria-hidden="true"><path d="M9.5 7 17 12l-7.5 5Z"/></svg>
      </button>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-svgb07-bg: #07070c;
  --color-svgb07-bg: oklch(0.14 0.01 285);
  --color-svgb07-fg: #f4f2f8;
  --color-svgb07-fg: oklch(0.965 0.006 285);
  --color-svgb07-muted: #a49fb4;
  --color-svgb07-muted: oklch(0.72 0.02 290);
  --color-svgb07-rest: rgba(244, 242, 248, 0.22);
  --color-svgb07-rest: oklch(0.965 0.006 285 / 0.22);
  --color-svgb07-a: #ff5db1;
  --color-svgb07-a: oklch(0.72 0.22 350);
  --color-svgb07-b: #7b5cff;
  --color-svgb07-b: oklch(0.60 0.24 290);
  --color-svgb07-c: #35e8c5;
  --color-svgb07-c: oklch(0.85 0.15 175);
  --font-svgb07-sans: 'Bricolage Grotesque', system-ui, sans-serif;
  --font-svgb07-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --ease-svgb07: cubic-bezier(0.16, 1, 0.3, 1);
}
/* A gradient is a paint server, not a colour: it lives in <defs>, the stroke
   points at it by id, and the stops are the only place its colours exist.
   None of that is expressible as a utility. */

.svgb-07-s1 {
  stop-color: #ff5db1;
  stop-color: var(--color-svgb07-a);
  animation: svgb-07-cyc 7s linear infinite;
}

.svgb-07-s2 {
  stop-color: #7b5cff;
  stop-color: var(--color-svgb07-b);
  animation: svgb-07-cyc 7s linear infinite -2.33s;
}

.svgb-07-s3 {
  stop-color: #35e8c5;
  stop-color: var(--color-svgb07-c);
  animation: svgb-07-cyc 7s linear infinite -4.66s;
}

@keyframes svgb-07-cyc {
  0% {
    stop-color: oklch(0.72 0.22 350);
  }

  33% {
    stop-color: oklch(0.60 0.24 290);
  }

  66% {
    stop-color: oklch(0.85 0.15 175);
  }

  100% {
    stop-color: oklch(0.72 0.22 350);
  }
}

.svgb-07::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background: radial-gradient(70% 50% at 20% 15%, color-mix(in oklab, var(--color-svgb07-b) 34%, transparent), transparent 62%), radial-gradient(60% 50% at 85% 85%, color-mix(in oklab, var(--color-svgb07-a) 26%, transparent), transparent 62%), linear-gradient(180deg, transparent 40%, var(--color-svgb07-bg));
}

.svgb-07:has(#svgb-07-theme:checked) {
  --color-svgb07-bg: #f3f1f7;
  --color-svgb07-bg: oklch(0.955 0.006 285);
  --color-svgb07-fg: #121017;
  --color-svgb07-fg: oklch(0.185 0.012 285);
  --color-svgb07-muted: #565064;
  --color-svgb07-muted: oklch(0.49 0.022 290);
  --color-svgb07-rest: rgba(18, 16, 23, 0.2);
  --color-svgb07-rest: oklch(0.185 0.012 285 / 0.2);
  --color-svgb07-a: #b3006b;
  --color-svgb07-a: oklch(0.48 0.22 355);
  --color-svgb07-b: #3f27c8;
  --color-svgb07-b: oklch(0.40 0.22 288);
  --color-svgb07-c: #00705f;
  --color-svgb07-c: oklch(0.46 0.10 175);
  --svgb-07-img-op: 0.16;
  --svgb-07-basefill: oklch(0 0 0 / 0.04);
}

.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s1,
.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s2,
.svgb-07:has(#svgb-07-theme:checked) .svgb-07-s3 {
  animation-name: svgb-07-cyc-light;
}

@keyframes svgb-07-cyc-light {
  0% {
    stop-color: oklch(0.48 0.22 355);
  }

  33% {
    stop-color: oklch(0.40 0.22 288);
  }

  66% {
    stop-color: oklch(0.46 0.10 175);
  }

  100% {
    stop-color: oklch(0.48 0.22 355);
  }
}

@media (prefers-reduced-motion: reduce) {
  .svgb-07-s1,
    .svgb-07-s2,
    .svgb-07-s3 {
    animation: none;
  }
}
```
